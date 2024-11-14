#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

def read_file_content(file_path):
    """
    Read file content, only processing text files.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return {
                'type': 'text',
                'encoding': 'utf-8',
                'content': file.read()
            }
    except UnicodeDecodeError:
        # Skip binary files
        return {
            'type': 'skipped',
            'error': 'Binary file - skipped'
        }
    except Exception as e:
        return {
            'type': 'error',
            'error': str(e)
        }

def parse_repository(repo_path, output_file, ignore_patterns=None):
    """
    Parse all text files in a repository and save them to a JSON file.
    """
    if ignore_patterns is None:
        ignore_patterns = ['.git', '__pycache__', '.pyc', '.pyo', '.pyd', '.so', '.dll']
    
    files_data = []
    
    def should_ignore(path):
        return any(pattern in path for pattern in ignore_patterns)
    
    # Walk through the repository
    for root, dirs, files in os.walk(repo_path):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if not should_ignore(d)]
        
        for file in files:
            if not should_ignore(file):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, repo_path)
                
                print(f"Processing: {relative_path}")
                
                file_content = read_file_content(file_path)
                if file_content['type'] != 'skipped':
                    file_data = {
                        'fileName': file,
                        'filePath': relative_path,
                        'fileContent': file_content
                    }
                    files_data.append(file_data)
                else:
                    print(f"Skipping binary file: {relative_path}")
    
    # Save to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(files_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nRepository parsed successfully. Output saved to: {output_file}")
    print(f"Total files processed: {len(files_data)}")

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct paths relative to the script location
    repo_path = os.path.join(script_dir, "./")
    output_file = os.path.join(script_dir, "repository_contents.txt")
    
    # Additional patterns to ignore
    ignore_patterns = [
        '.git',
        '__pycache__',
        '.pyc',
        '.pyo',
        '.pyd',
        '.so',
        '.dll',
        '.coverage',
        '.pytest_cache',
        '.venv',
        'venv',
        '.tox',
        'dist',
        'build',
        'egg-info',
        # Add common binary file extensions to ignore
        '.png',
        '.jpg',
        '.jpeg',
        '.gif',
        '.bmp',
        '.ico',
        '.pdf',
        '.zip',
        '.tar',
        '.gz',
        '.7z',
        '.exe',
        '.bin'
    ]
    
    try:
        # Check if repository exists
        if not os.path.exists(repo_path):
            print(f"Error: Repository not found at {repo_path}")            
            return
        
        parse_repository(repo_path, output_file, ignore_patterns)
    except Exception as e:
        print(f"Error processing repository: {e}")

if __name__ == "__main__":
    main()
