from file_rw import copy_files, generate_pages_recursive

print("hello world")





def main() -> None:
    copy_files("./static", "./public")
    generate_pages_recursive("content/", "template.html", "public/")
main()
