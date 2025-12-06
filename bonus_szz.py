import re
import difflib
from lhdiff import LHDiff

class BugIdentifier:
    def __init__(self, commit_history):
        self.commits = commit_history 
        self.bug_inducing_commits = set()

    def identify_fixes(self):
        """
        Scans commit messages for fix keywords.
        """
        fix_keywords = [r"fix", r"bug", r"error", r"issue", r"close #"]
        
        print("\n[Bonus] Scanning for bug fixes...")
        for commit in self.commits:
            msg = commit['msg'].lower()
            if any(re.search(kw, msg) for kw in fix_keywords):
                print(f"  > Fix Commit Found: {commit['id']} | Msg: {commit['msg']}")
                self._trace_back(commit)

    def _trace_back(self, fix_commit):
        """
        Identifies changed lines in the fix and traces them back.
        """
        # 1. Diff the fix to find lines REMOVED (these were the buggy lines)
        prev_lines = fix_commit['file_prev'].splitlines()
        curr_lines = fix_commit['file_curr'].splitlines()
        
        diff = difflib.ndiff(prev_lines, curr_lines)
        buggy_indices_prev = []
        
        idx = 0
        for line in diff:
            if line.startswith('- '): # Line removed in fix -> it was buggy
                buggy_indices_prev.append(idx)
                idx += 1
            elif line.startswith('  '):
                idx += 1
        
        if not buggy_indices_prev:
            print("    (No lines removed in fix, simplified logic skips complex refactors)")
            return

        print(f"    Buggy lines in previous version: {buggy_indices_prev}")
        self._blame(fix_commit['parent_id'], buggy_indices_prev)
