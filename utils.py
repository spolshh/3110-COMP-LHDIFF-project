import math
import re
from collections import Counter

def preprocess_line(line):
    """
    Standardizes a line for comparison: 
    - Trims whitespace
    - Lowercases
    - Normalizes internal spacing
    """
    line = line.strip().lower()
    line = re.sub(r'\s+', ' ', line)
    return line

def levenshtein_distance(s1, s2):
    """
    Calculates the Levenshtein distance between two strings.
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def normalized_levenshtein(s1, s2):
    """
    Returns a score between 0.0 (different) and 1.0 (identical).
    """
    max_len = max(len(s1), len(s2))
    if max_len == 0: return 1.0
    dist = levenshtein_distance(s1, s2)
    return 1.0 - (dist / max_len)


