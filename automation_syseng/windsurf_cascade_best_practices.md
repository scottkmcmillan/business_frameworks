# Windsurf and Cascade Best Practices

## Memories

### Example 1: Code Modification Preferences

Let me create a memory for code modification preferences that will help maintain existing functionality.

I've created a comprehensive memory about code modification practices. This means that whenever you ask me to modify code, I will:

Prefer extending rather than modifying existing code
Maintain backward compatibility
Follow existing patterns and styles
Preserve existing functionality
Add proper documentation for new changes
For example, if you ask me to add a new feature to a class, I would:

Add new methods rather than modify existing ones
Keep existing method signatures unchanged
Follow the existing error handling patterns
Add new tests without modifying existing ones

### Example 2: Documentation Modification Preferences

Let me create a memory about this important preference to ensure consistent behavior across our interactions.

To prevent inadvertent modifications to other documents, you can:

1. Focus on Active Document: Keep your cursor in the document you want to modify. I'll prioritize modifying the document where your cursor is located.

2. Use Explicit File Paths: When you want me to modify a specific file, provide its path in your request. For example: Update the content in C:\Users\scott\CascadeProjects\frameworks\specific_file.md

3. Close Unnecessary Documents: Keep only the documents you're actively working on open. This reduces the chance of unintended modifications.

I've created a memory of this preference, so I will now:

Only modify files explicitly mentioned in your requests
Default to the active document (where your cursor is) when the request is ambiguous
Not touch other open documents unless specifically requested

### Cascade Memory Feature

#### Overview
Cascade's memory feature allows the AI to maintain persistent context and user preferences across conversations. This helps ensure consistent behavior and adherence to user-defined guidelines without having to repeat instructions in every interaction.

#### Key Characteristics

1. **Persistence**
   - Memories persist across multiple conversations
   - No need to repeat preferences or context in each session
   - Automatically applied in relevant situations

2. **Structure**
   - Each memory has:
     - Unique ID
     - Title
     - Content
     - Tags for categorization
     - Associated workspace (CorpusNames)

3. **Types of Memories**
   - User Preferences
   - Code Development Guidelines
   - Document Modification Rules
   - Best Practices
   - Important Context

#### Common Use Cases

1. **Document Management**
   - File modification preferences
   - Which files to modify/not modify
   - How to handle multiple open documents

2. **Code Development**
   - Maintaining existing functionality
   - Following specific coding patterns
   - Preserving backward compatibility
   - Testing requirements

3. **Project Context**
   - Code organization patterns
   - Architectural decisions
   - Cross-component dependencies
   - Important file locations

#### Benefits

1. **Consistency**
   - Ensures consistent behavior across interactions
   - Maintains coding standards
   - Preserves user preferences

2. **Efficiency**
   - Reduces need for repetitive instructions
   - Automates adherence to best practices
   - Streamlines development process

3. **Quality Control**
   - Enforces development standards
   - Maintains code quality
   - Prevents unintended modifications

#### Creating Memories

Memories can be created:
1. Proactively by Cascade when it identifies important patterns or preferences
2. Explicitly by the user when setting specific requirements
3. Through observed behavior and repeated instructions

#### Memory Management

- Memories can be created, updated, or deleted
- User-defined memories (with <user_> prefix) cannot be overridden by Cascade
- Memories are presented to the user for approval
- Tags help organize and retrieve relevant memories

#### How to Tag and Update Memories

1. **Updating a Memory**
   - You need the memory's ID (a unique identifier)
   - Specify the action as "update"
   - Provide the updated content
   - Can modify title, content, and tags
   - Example: "Update memory db4544df with new content about code practices"

2. **Using Tags**
   - Tags should be in snake_case format
   - Use descriptive, categorical tags
   - Multiple tags can be applied to one memory
   - Examples of good tags:
     - `code_modification`
     - `best_practices`
     - `backward_compatibility`
     - `dependency_injection`
     - `testing`

3. **Best Practices for Tags**
   - Use consistent naming conventions
   - Keep tags focused and specific
   - Use hierarchical tags when appropriate (e.g., `code_style`, `code_testing`)
   - Avoid overly broad or vague tags
   - Consider using tag families for related concepts

#### Finding Memory IDs

When a memory is created, Cascade returns a response in this format:
```
Cascade created a new MEMORY[9ef6819c-c327-4833-9606-7c620bc0ec52]: Memory content...
```

The memory ID is the string inside the square brackets. This ID is needed when you want to:
- Update the memory
- Delete the memory
- Reference the memory in other operations

Example ID: `9ef6819c-c327-4833-9606-7c620bc0ec52`

#### Managing Memory IDs

**Current Limitations:**
- There is no direct command to list all existing memories and their IDs
- IDs need to be tracked when memories are created

**Best Practices for ID Management:**
1. Save memory IDs when they are first created
2. Document important memory IDs in a dedicated file
3. Create new memories if you can't find the ID of an existing one
4. Use descriptive titles and tags to help identify memories
5. Consider maintaining a simple registry of critical memories and their IDs

#### Memory Creation Template

When creating a new memory, use this template to ensure proper documentation:

```markdown
# Memory Creation Request
Title: [Brief, descriptive title]
Tags: [List of relevant tags in snake_case]
Content: [Detailed memory content]

# After Creation
1. Copy the memory ID from Cascade's response:
   Memory ID: [paste the ID string here]
   Example response format: "Cascade created a new MEMORY[abc-123-xyz]: ..."

2. Add to Memory Registry:
   | Date Created | Title | ID | Tags | Purpose |
   |--------------|-------|----|----|---------|
   | YYYY-MM-DD   | Title | ID | tags | Brief description |

3. Save this information in: frameworks/memory_registry.md
```

Example Usage:
```markdown
# Memory Creation Request
Title: Code Review Standards
Tags: code_review, best_practices, quality_control
Content: Standard process for code reviews including:
1. Check for existing test coverage
2. Verify documentation
3. Assess performance impact
4. Review security implications

# After Creation
1. Memory ID: abc-123-xyz (copied from Cascade's response)

2. Added to Registry:
   | Date | Title | ID | Tags | Purpose |
   |------|-------|----|----|---------|
   | 2025-02-08 | Code Review Standards | abc-123-xyz | code_review, best_practices | Define standard code review process |

#### Project Initialization Best Practices

When starting a new project, always set up memory management first:

1. **Create Memory Registry**
   ```markdown
   # Create memory_registry.md in your project root
   - Copy the registry template from an existing project
   - Initialize with empty Active and Archived sections
   ```

2. **Set Up Essential Memories**
   Create these fundamental memories in order:
   1. Document Modification Rules
      - Which files can be modified
      - How to handle multiple open documents
   2. Code Modification Standards
      - How to preserve existing functionality
      - Coding style and patterns
   3. Memory Registration Process
      - How to track memory IDs
      - Registry maintenance rules

3. **First Memory Creation Template**
   ```markdown
   # Project Initialization Memories
   
   ## Memory 1: Document Modification Rules
   Title: Document Modification Rules for [Project Name]
   Tags: document_modification, user_preference, file_handling
   Content: [Your rules for document modification]
   
   ## Memory 2: Code Standards
   Title: Code Modification Standards for [Project Name]
   Tags: code_modification, best_practices, standards
   Content: [Your coding standards]
   
   ## Memory 3: Memory Management
   Title: Memory Registration Process for [Project Name]
   Tags: memory_management, documentation, process
   Content: [Memory tracking rules]
   ```

4. **Document IDs Immediately**
   - After each memory creation, immediately add to registry
   - Use the full template from the Memory Creation section
   - Keep registry updated before proceeding with project work

This initialization process ensures:
- Consistent memory management from project start
- Clear documentation of all memory IDs
- Established rules for code and document modification
- Proper tracking of all future memories

## Markdown Conversion Script
Was first implemented in 2025-02-09 in the Frameworks project. This implementation could be replicated in other projects going forward.

### Summary of Implementation

The Python script `convert_to_markdown.py` is designed to convert various file formats to Markdown using the `Markitdown` library. It supports:

1. **Command-Line Usage**: The script can be run from the terminal with the syntax:
   ```bash
   python convert_to_markdown.py [output_directory] [file1] [file2] ...
   ```

2. **Drag-and-Drop Support**: Users can drag files onto the script to convert them.

3. **Output Directory Specification**: Users can specify an output directory where converted Markdown files will be saved.

### How to Run the Script

1. **Open a terminal or command prompt**.
2. **Navigate to the directory** where the script is located.
3. **Run the script** with the required arguments:
   ```bash
   python convert_to_markdown.py "C:\path\to\output\directory" "C:\path\to\file1.xlsx" "C:\path\to\file2.csv"
   ```
   - Replace `"C:\path\to\output\directory"` with the actual path to the output directory.
   - Replace `"C:\path\to\file1.xlsx"` and `"C:\path\to\file2.csv"` with the paths to the files you want to convert.