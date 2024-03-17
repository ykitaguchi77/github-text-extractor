# 📂 GitHubTextExtractor

## 🌟 Overview

`GitHubTextExtractor` is a tool designed to extract the file hierarchy and content of a GitHub repository, making it easier to analyze and understand the structure and contents of the repository.

## 📋 Key Features

- 📡 Clones GitHub repositories to your local machine.
- 🌐 Provides a visual representation of the file hierarchy.
- 📄 Exports the directory structure and file contents in XML or text format for further analysis.
- 🚫 Allows specifying directories to exclude from the extraction process.

## 🔍 How to Use

1. **Installing Dependencies:**
  - Install the required dependencies using pip:
    ```bash
    pip install gitpython treelib
    ```

2. **Running the Script:**
  - Run the script with the following command:
    ```bash
    python github-text-extractor.py repository_url output_path [--exclude_dirs dir1 dir2 ...]
    ```
  - Provide the following arguments:
    - `repository_url`: The URL of the GitHub repository you want to extract.
    - `output_path`: The path where you want to save the output file. The output format will be determined based on the file extension (`.xml` for XML format, otherwise text format).
    - `--exclude_dirs` (optional): Specify the directories to exclude from the extraction process. By default, the `.git` directory is excluded.

3. **Output:**
  - The script will clone the specified GitHub repository to a temporary directory.
  - It will display the file hierarchy of the repository and save it to a file named `tree_structure.txt`.
  - The file hierarchy and contents will be exported in the specified format (XML or text) to the provided output path.

## 📊 Application

`GitHubTextExtractor` is perfect for extracting the content of entire GitHub repositories for analysis with Large Language Models (LLMs), facilitating thorough understanding of code structures and content.

## ⚙️ Setup
- Implemented in Python, requiring libraries like `os`, `argparse`, `git`, `treelib`, and `xml.etree.ElementTree`.
- Dependencies can be installed with:
 ```bash
 pip install gitpython treelib


## 🖥️ Example Usage
- To extract the content of a GitHub repository and exclude specific directories, run the following command:

 ```bash
python github-text-extractor.py https://github.com/username/repo.git output.txt --exclude_dirs .git node_modules

- This command will clone the repository, extract its content, exclude the .git and node_modules directories, and save the output in XML format to the file output.xml.

