import sys

from file_rw import copy_files, generate_pages_recursive

print("hello world")

basepath = "/"
if len(sys.argv) >= 2:
    basepath = sys.argv[1]

def main() -> None:

    copy_files("./static", "./docs")
    generate_pages_recursive("content/", "template.html", "docs/", basepath)
main()
