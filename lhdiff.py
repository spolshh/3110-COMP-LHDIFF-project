import difflib
import utils

class LHDiff:
    def __init__(self, old_file_content, new_file_content):
        # Store original lines for context extraction
        self.old_lines = old_file_content.splitlines()
        self.new_lines = new_file_content.splitlines()
        
        # Preprocess lines once
        self.norm_old = [utils.preprocess_line(l) for l in self.old_lines]
        self.norm_new = [utils.preprocess_line(l) for l in self.new_lines]
        
        # Determine mapping: old_index (0-based) -> list of new_indices (0-based)
        self.mapping = {} 
        self.mapped_new_indices = set()

    def run(self):
        """
        Executes the LHDiff pipeline.
        Returns a dictionary: { old_line_index: [new_line_index, ...] }
        """
        self._step2_detect_unchanged()
        self._step3_candidate_generation()
        self._step5_detect_splits() # Step 4 (Conflict Resolution) is implicit in Step 3's greedy selection
        
        return self.mapping

    def _step2_detect_unchanged(self):
        """
        Uses Unix Diff (via difflib) to find exact matches first.
        """
        matcher = difflib.SequenceMatcher(None, self.norm_old, self.norm_new)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == 'equal':
                for k in range(i2 - i1):
                    old_idx = i1 + k
                    new_idx = j1 + k
                    self.mapping[old_idx] = [new_idx]
                    self.mapped_new_indices.add(new_idx)
                    
    def _step3_candidate_generation(self):
        """
        Generates candidates using SimHash and scores them using hybrid similarity.
        """
        # 1. Generate Candidates via SimHash
        candidates = self._generate_simhash_candidates()
        
        matches = []
        
        # 2. Score Candidates
        for old_idx, candidate_list in candidates.items():
            if old_idx in self.mapping: continue 

            best_score = -1
            best_new_idx = -1

            for new_idx in candidate_list:
                if new_idx in self.mapped_new_indices: continue

                # Content Similarity (Levenshtein)
                content_sim = utils.normalized_levenshtein(self.norm_old[old_idx], self.norm_new[new_idx])
                
                # Context Similarity (Cosine on Window)
                old_ctx = self._get_context(self.old_lines, old_idx)
                new_ctx = self._get_context(self.new_lines, new_idx)
                context_sim = utils.cosine_similarity(old_ctx, new_ctx)

                # Combined Score Formula
                combined = (0.6 * content_sim) + (0.4 * context_sim)
                
                if combined > best_score:
                    best_score = combined
                    best_new_idx = new_idx

            # Threshold
            if best_score > 0.4: 
                matches.append((best_score, old_idx, best_new_idx))

        # 3. Resolve Conflicts (Greedy sort)
        matches.sort(key=lambda x: x[0], reverse=True)
        
        for score, old_idx, new_idx in matches:
            if old_idx not in self.mapping and new_idx not in self.mapped_new_indices:
                self.mapping[old_idx] = [new_idx]
                self.mapped_new_indices.add(new_idx)
