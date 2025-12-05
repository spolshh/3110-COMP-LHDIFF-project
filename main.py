import os
import glob
from lhdiff import LHDiff
from xml_parser import parse_all_versions

def evaluate_directory(path):
    """
    Scans directory for files matching *_1.* (the base versions).
    Then looks for ALL subsequent versions defined in the corresponding XML.
    """
    print(f"Scanning directory: {path}...")
    
    # 1. Find all Base Files (Version 1)
    search_pattern = os.path.join(path, "*_1.*")
    base_files = glob.glob(search_pattern)
    
    total_files_checked = 0
    total_correct_mappings = 0
    total_lines_checked = 0
    
    if not base_files:
        print(f"No base files found matching '{search_pattern}'.")
        return

    for base_file_path in base_files:
        if base_file_path.endswith(".xml"): continue

        # Extract info: "tests/BaseTypes_1.java" -> dir="tests", base="BaseTypes", ext=".java"
        dirname, filename = os.path.split(base_file_path)
        name_root, ext = os.path.splitext(filename)
        
        if not name_root.endswith("_1"): continue
        base_name = name_root[:-2] # Remove "_1"
        
        xml_file_path = os.path.join(dirname, f"{base_name}.xml")
        
        if not os.path.exists(xml_file_path):
            print(f"Skipping {base_name}: XML Ground Truth not found.")
            continue

        # 2. Parse XML to find out which versions we need to test
        # returns { 1: {...}, 2: {...}, 3: {...} }
        truth_versions = parse_all_versions(xml_file_path)
        
        if not truth_versions:
            print(f"Skipping {base_name}: XML contained no valid version data.")
            continue

        print(f"Processing Group: {base_name}...")
        
        # Read Base Content (Version 1)
        try:
            with open(base_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content_base = f.read()
        except Exception as e:
            print(f"  Error reading base file: {e}")
            continue