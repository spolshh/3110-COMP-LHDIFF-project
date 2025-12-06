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
