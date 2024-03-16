# 📂github-tree-explorer

## 🌟 Overview
`GitRepoTreeExplorer` is a tool designed to visualize and export the file hierarchy of a GitHub repository, making it easier to review and understand the structure and contents.

## 📋 Key Features
- 📡 Clones GitHub repositories to your local machine.
- 🌐 Provides a visual representation of the file hierarchy.
- 📄 Exports the directory structure in XML format for further analysis.

## 🔍 How to Use
1. **Cloning the Repository:**
   - Specify the URL of the repository you want to clone.
     ```python
     repository_url = "https://github.com/yourusername/yourrepository.git"
     clone_dir = "/path/to/clone"
     ```

2. **Displaying File Hierarchy:**
   - Use the tool to display the file hierarchy and understand the repository structure.
     ```python
     display_file_hierarchy(clone_dir, exclude_dir=".git")
     ```

3. **Exporting in XML Format:**
   - Export the directory structure to an XML file for a comprehensive view.
     ```python
     root_element = directory_to_xml(clone_dir, exclude_directory=".git")
     write_xml_to_file(root_element, "directory_structure_with_content.xml")
     ```

## 📊 Application
- `GitRepoTreeExplorer` is perfect for analyzing entire GitHub repositories with Large Language Models (LLMs), facilitating thorough analysis and understanding of code structures and content.

## ⚙️ Setup
- Implemented in Python, requiring libraries like `os`, `git`, `treelib`, and `xml.etree.ElementTree`.
- Install dependencies with:
  ```bash
  pip install gitpython treelib
