import os


def file_writer(destination):
    with open(".gitignore", "w", encoding="utf-8") as file:
        pass

    with open("main.py", "w", encoding="utf-8") as file:
        pass

    with open("requirements.txt", "w", encoding="utf-8") as file:
        pass

    with open("README.md", "w", encoding="utf-8") as file:
        pass

    with open("setup.py", "w", encoding="utf-8") as file:
        pass

    os.chdir(os.path.join(destination, "src"))
    with open("__init__.py", "w", encoding="utf-8") as file:
        pass
    with open("module1.py", "w", encoding="utf-8") as file:
        pass

    with open("module2.py", "w", encoding="utf-8") as file:
        pass

    os.chdir(os.path.join(destination, "tests"))

    with open("__init__.py", "w", encoding="utf-8") as file:
        pass

    with open("test_module1.py", "w", encoding="utf-8") as file:
        pass

    with open("test_module2.py", "w", encoding="utf-8") as file:
        pass

    os.chdir(os.path.join(destination, "config"))

    with open("settings.yaml", "w", encoding="utf-8") as file:
        pass

    with open("logging.conf", "w", encoding="utf-8") as file:
        pass
