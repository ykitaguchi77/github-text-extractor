# 📂 GitHubTextExtractor

## 🌟 Overview

`GitHubTextExtractor` is a tool designed to extract the file hierarchy and content of a GitHub repository, making it easier to analyze and understand the structure and contents of the repository.

## 📋 Key Features

- 📡 Clones GitHub repositories to your local machine.
- 🌐 Provides a visual representation of the file hierarchy.
- 📄 Exports the directory structure and file contents in XML or text format for further analysis.
- 🚫 Allows specifying directories to exclude from the extraction process.
- 📝 Supports extracting only the README file or code files.

## 🔍 How to Use

1. **Installing Dependencies:**
  - Install the required dependencies using pip:
    ```bash
    pip install gitpython treelib
    ```

2. **Running the Script:**
  - Run the script with the following command:
    ```bash
    python github-text-extractor.py --repository_url <url> --output_path <path> [--exclude_dirs <dir1> <dir2> ...] [--tree_output <path>] [--readme] [--code]
    ```
  - Provide the following arguments:
    - `--repository_url`: The URL of the GitHub repository you want to extract.
    - `--output_path`: The path where you want to save the output file. The output format will be determined based on the file extension (`.xml` for XML format, or `.txt` for text format).
    - `--exclude_dirs` (optional): Specify the directories to exclude from the extraction process. By default, the `.git` directory is excluded.
    - `--tree_output` (optional): Specify the path to save the file hierarchy to a text file.
    - `--readme` (optional): Extract only the README file.
    - `--code` (optional): Extract only code files (e.g., .py, .java, .c, .cpp, .h, .hpp, .js, .css, .html).

3. **Output:**
  - The script will clone the specified GitHub repository to a temporary directory.
  - It will display the file hierarchy of the repository. If you use the `--tree_output` option, the hierarchy is saved to a text file.
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
python github-text-extractor.py --repository_url https://github.com/username/repo.git --output_path output.txt --exclude_dirs .git
```

- This command will extract its content, exclude the .git directories, and save the output in txt format to the file output.txt.

- To save the directory tree structure in a separate text file, use the --tree_output option:

```bash
python github-text-extractor.py --repository_url https://github.com/username/repo.git --output_path output.txt --exclude_dirs .git --tree_output tree_structure.txt
```

- This command will add saving the directory tree structure to tree_structure.txt.


## 🚀 Colab Demo
-You can also try out GitHubTextExtractor using the provided Colab demo. The demo notebook guides you through the process of running the script and extracting the content of a GitHub repository directly in Colab.

-To access the Colab demo, click on the following link: GitHubTextExtractor Colab Demo



