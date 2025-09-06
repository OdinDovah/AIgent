from functions.get_file_content import get_file_content


def main():
    print("Result for main.py")
    print(get_file_content("calculator", "main.py"))
    print("Result for pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("Result for /bin/cat")
    print(get_file_content("calculator", "/bin/cat"))
    print("Result for non-existing")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()
