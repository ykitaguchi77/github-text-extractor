import os
import argparse
import xml.etree.ElementTree as ET
from git import Repo
from treelib import Tree

def clone_repository(repository_url, clone_dir):
    os.makedirs(clone_dir, exist_ok=True)
    Repo.clone_from(repository_url, clone_dir)

def display_file_hierarchy(directory, exclude_dirs):
    tree = Tree()
    tree.create_node(directory, directory)

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for dir in dirs:
            tree.create_node(dir, os.path.join(root, dir), parent=root)
        for file in files:
            tree.create_node(file, os.path.join(root, file), parent=root)

    tree_file = os.path.join(directory, "tree_structure.txt")
    with open(tree_file, 'w') as file:
        pass
    tree.save2file(tree_file)
    print(f"Directory structure saved to {tree_file}")

    with open(tree_file, 'r') as file:
        print(file.read())

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return str(e)

def directory_to_xml(directory, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = []

    root_element = ET.Element("directory", name=os.path.basename(directory))

    for root, dirs, files in os.walk(directory, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            sub_element = ET.SubElement(root_element, "directory", name=dir_name)
            append_files_and_dirs(sub_element, dir_path, exclude_dirs)

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_element = ET.SubElement(root_element, "file", name=file_name)
            content = read_file_content(file_path)
            file_element.text = content

        break

    return root_element

def append_files_and_dirs(parent_element, path, exclude_dirs):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path) and item not in exclude_dirs:
            dir_element = ET.SubElement(parent_element, "directory", name=item)
            append_files_and_dirs(dir_element, item_path, exclude_dirs)
        elif os.path.isfile(item_path):
            file_element = ET.SubElement(parent_element, "file", name=item)
            content = read_file_content(item_path)
            file_element.text = content

def write_xml_to_file(element, file_name):
    tree = ET.ElementTree(element)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)

def write_xml_to_text_file(xml_element, text_file_name):
    with open(text_file_name, 'w', encoding='utf-8') as file:
        file.write(ET.tostring(xml_element, encoding='unicode'))

def main():
    parser = argparse.ArgumentParser(description='GitHub Text Extractor')
    parser.add_argument('repository_url', help='URL of the GitHub repository')
    parser.add_argument('output_path', help='Path to save the output file')
    parser.add_argument('xml_or_txt', choices=['xml', 'txt'], help='Output format: xml or txt')
    args = parser.parse_args()

    clone_dir = "./temp_repo"
    exclude_dirs = ['.git']

    clone_repository(args.repository_url, clone_dir)
    display_file_hierarchy(clone_dir, exclude_dirs)

    root_element = directory_to_xml(clone_dir, exclude_dirs)

    if args.xml_or_txt == 'xml':
        write_xml_to_file(root_element, args.output_path)
    else:
        write_xml_to_text_file(root_element, args.output_path)

    print(f"Output saved to {args.output_path}")

if __name__ == '__main__':
    main()
