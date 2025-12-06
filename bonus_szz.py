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