#!/usr/bin/env python
"""
Markdown Converter Tool
Converts various file formats to Markdown using Markitdown.
Supports drag-and-drop from Windows File Explorer.

Usage:
1. Run from terminal: python convert_to_markdown.py [output_directory] [file1] [file2] ...
2. Or drag and drop files onto the script in Windows Explorer
"""

import os
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
    # Get output directory and file paths from command line arguments
    if len(sys.argv) < 3:
        print("Please provide an output directory and at least one file to convert.")
        print("Usage: python convert_to_markdown.py [output_directory] [file1] [file2] ...")
        print("Or drag and drop files onto this script in Windows Explorer")
        input("Press Enter to exit...")
        return

    output_dir = Path(sys.argv[1])
    if not output_dir.exists() or not output_dir.is_dir():
        print(f"✗ Output directory does not exist: {output_dir}")
        input("Press Enter to exit...")
        return

    # Process each file
    success_count = 0
    total_files = len(sys.argv) - 2
    
    print(f"\nConverting {total_files} file(s) to Markdown...\n")
    
    for file_arg in sys.argv[2:]:
        file_path = Path(file_arg)
        if file_path.exists():
            if convert_file(file_path, output_dir):
                success_count += 1
        else:
            print(f"✗ File not found: {file_arg}")
    
    # Print summary
    print(f"\nConversion complete: {success_count}/{total_files} files converted successfully")
    
    # If run by double-clicking, wait for user input before closing
    if len(sys.argv) == 3:  # When dragged and dropped, there's only one file
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()