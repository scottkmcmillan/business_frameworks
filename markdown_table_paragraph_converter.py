import re
import sys
import os
import logging

def clean_cell_content(content):
    """
    Clean cell content by removing 'NaN', stripping whitespace, 
    and handling newline characters.
    """
    if content is None:
        return ""
    
    # Remove 'NaN', 'Nan', etc.
    content = re.sub(r'\b[Nn][Aa][Nn]\b', '', content, flags=re.IGNORECASE)
    
    # Strip whitespace
    content = content.strip()
    
    # Replace newline characters with spaces
    content = re.sub(r'\n+', ' ', content)
    
    return content

def extract_markdown_table(content):
    """
    Robustly extract markdown table from content.
    Handles different table formats and header detection.
    """
    # Split content into lines
    lines = content.split('\n')
    
    # Find table start and end
    table_start = None
    table_end = None
    
    for i, line in enumerate(lines):
        # Look for line that starts with '|' and contains multiple '|'
        if line.strip().startswith('|') and line.count('|') > 1:
            if table_start is None:
                table_start = i
            table_end = i
    
    if table_start is None or table_end is None:
        logging.warning("No markdown table found in the content")
        return None, None
    
    # Extract table lines
    table_lines = lines[table_start:table_end+1]
    
    # Find header row (typically the first row with content after separator)
    header_row = None
    for i, line in enumerate(table_lines):
        # Skip separator line
        if re.match(r'^\s*\|[-:\s|]+$', line):
            continue
        
        # First non-separator line is likely the header
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        if cells and any(cells):
            header_row = cells
            break
    
    # Extract data rows
    data_rows = []
    for line in table_lines[i+1:]:
        if not line.strip().startswith('|'):
            break
        
        cells = [clean_cell_content(cell.strip()) for cell in line.split('|')[1:-1]]
        if any(cells):  # Only add rows with some content
            data_rows.append(cells)
    
    return header_row, data_rows

def markdown_table_to_paragraphs(content):
    """
    Convert a markdown table to paragraphs with headings.
    More robust version that handles various table formats.
    """
    # Extract table headers and rows
    headers, data_rows = extract_markdown_table(content)
    
    if not headers or not data_rows:
        logging.error("Could not extract table from content")
        return ""
    
    # Construct paragraphs
    paragraphs = []
    for row in data_rows:
        row_paragraphs = []
        for i, cell in enumerate(row):
            # Ensure we don't go out of bounds of headers
            heading = headers[i] if i < len(headers) else f"Column {i+1}"
            
            # Skip empty cells
            if not cell:
                continue
            
            row_paragraphs.append(f"### {heading}\n\n{cell}\n")
        
        # Only add row if it has content
        if row_paragraphs:
            paragraphs.extend(row_paragraphs)
    
    return '\n'.join(paragraphs)

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s: %(message)s')
    
    # Check command line arguments
    if len(sys.argv) != 3:
        logging.error("Usage: python script.py <input_file> <output_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    # Read the content of the file
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        sys.exit(1)

    # Convert table to paragraphs
    converted_paragraphs = markdown_table_to_paragraphs(content)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Define output file path
    output_file = os.path.join(output_dir, 'converted_paragraphs.md')

    # Write converted paragraphs
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(converted_paragraphs)
        logging.info(f"Successfully converted table to paragraphs: {output_file}")
    except Exception as e:
        logging.error(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
