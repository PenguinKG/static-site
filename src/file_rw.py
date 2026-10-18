import os
import shutil

from markdown_to_html import markdown_to_html_node


def copy_files(sourcedir: str, destdir: str):
    if not os.path.exists(sourcedir):
        raise ValueError("The specified source directory does not exist")
    if os.path.exists(destdir):
        shutil.rmtree(destdir)
    if not os.path.exists(destdir):
        os.makedirs(destdir)

    for path in os.listdir(sourcedir):
        if os.path.isfile(os.path.join(sourcedir, path)):
            shutil.copy(os.path.join(sourcedir, path), destdir)
        if not os.path.isfile(os.path.join(sourcedir, path)):
            os.mkdir(os.path.join(destdir, path))
            copy_files(os.path.join(sourcedir, path), os.path.join(destdir, path))

def extract_title(markdown: str):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise RuntimeError("A title couldn't be found")

def generate_page(from_path: str, template_path: str, dest_path:str, basepath:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    with open(from_path) as mdfile:
        mdcontents = mdfile.read()
    with open(template_path) as template:
        template_contents = template.read()


    html_string = markdown_to_html_node(mdcontents).to_html()
    title = extract_title(mdcontents)

    semifinal_page = template_contents.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    final_page = semifinal_page.replace("href=\"/", f"href={basepath}").replace("src=\"/", f"src={basepath}")
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as dest_file:
        dest_file.write(final_page)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str):
    for path in os.listdir(dir_path_content):
        file_dir = os.path.join(dir_path_content, path)
        print(file_dir)
        if os.path.isfile(file_dir) and path.endswith(".md"):
            generate_page(file_dir, template_path, os.path.join(dest_dir_path, path.replace(".md", ".html")), basepath)
        elif not os.path.isfile(file_dir):
            generate_pages_recursive(file_dir, template_path, os.path.join(dest_dir_path, path), basepath)
