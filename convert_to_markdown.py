#!/usr/bin/env python
"""
Markdown Converter Tool
Converts various file formats to Markdown using Markitdown.
Supports command-line usage and drag-and-drop from Windows File Explorer.

Usage:
1. Run from terminal: python convert_to_markdown.py [output_directory] [file1] [file2] ...
2. Or drag and drop files onto the script in Windows Explorer
"""

import sys
from pathlib import Path
from markitdown import MarkItDown

def convert_file(file_path, output_dir):
    """Convert a single file to markdown format."""
    try:
        # Create MarkItDown instance
        md = MarkItDown()
        
        # Convert the file
        result = md.convert(str(file_path))
        
        # Create output filename (same name but with .md extension)
        output_path = output_dir / (file_path.stem + '.md')
        
        # Write the converted content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.text_content)
            
        print(f"✓ Successfully converted: {file_path.name} -> {output_path.name}")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {file_path.name}: {str(e)}")
        return False

def main():
    # Check if output directory is provided
    if len(sys.argv) < 3:
        print("Usage: python convert_to_markdown.py [output_directory] [file1] [file2] ...")
        sys.exit(1)

    # Get output directory and create it if it doesn't exist
    output_dir = Path(sys.argv[1])
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get list of files to convert
    files = [Path(f) for f in sys.argv[2:]]
    success_count = 0
    total_files = len(files)

    print(f"\nConverting {total_files} file(s) to Markdown...\n")

    # Convert each file
    for file in files:
        if file.exists():
            if convert_file(file, output_dir):
                success_count += 1
        else:
            print(f"✗ File not found: {file}")

    # Print summary
    print(f"\nConversion complete: {success_count}/{total_files} files converted successfully")

if __name__ == '__main__':
    main()