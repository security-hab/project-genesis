import os
import sqlite3
import time

from config import DIR_CATEGORIES, FOLDERS
from file_writer import file_writer

OPTION_CREATE_STRUCTURE = 1
OPTION_ADD_PROJECT = 2
OPTION_FINISH_PROGRAM = 0
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.db")
AVAILABLE_PROJECT_TYPES = """
[1] - parsing
[2] - scripts
[3] - web
[4] - data analysis
[5] - other
"""


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def db_creation():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS path(
            path TEXT
            )
            """
        )

        conn.commit()


#    conn.close()


def full_folder_structure():
    location = input(
        "[*] Enter absolute path where the full structure will be created: "
    ).strip()

    if not os.path.exists(location):
        print(f"[!] Error: The specified location {location} does not exist.")
        return

    if not os.path.isdir(location):
        print(f'[!] Error: "{location}" is not a directory.')
        return

    folder_name = input(
        "[*] Input folder name inside which will be created scructure: "
    ).strip()

    folder_path = os.path.join(location, folder_name)

    try:
        os.makedirs(folder_path, exist_ok=True)
    except OSError as ex:
        print(f"[!] Error while creating folder {ex}")
        return

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO path(path) VALUES (?)", (folder_path,))
        conn.commit()
        print(f"\n[*] Path '{folder_path}' has been added to the database!\n")
    # conn.commit()

    os.chdir(folder_path)

    for i in range(len(DIR_CATEGORIES)):
        os.mkdir(DIR_CATEGORIES[i])
        print(f"[*] Directory '{DIR_CATEGORIES[i]}' - was created!")
        i += 1
        time.sleep(0.5)


def project_structure(project_name, project_type: int):
    print(f"[*] Starting project scructure creation for project: {project_name}")

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM path")
        folder_paths = cursor.fetchall()

    if not folder_paths:
        print("[!] No saved paths found in the database!")
        return

    last_path = folder_paths[-1][0]
    print(f"[!] Using the last saved path: {last_path}")

    category_map = {
        1: DIR_CATEGORIES[0],
        2: DIR_CATEGORIES[1],
        3: DIR_CATEGORIES[2],
        4: DIR_CATEGORIES[3],
        5: DIR_CATEGORIES[4],
    }

    if project_type in category_map:
        final_path = os.path.join(last_path, category_map[project_type])
        print(f"[*] Target directory for project type: {project_type}: {final_path}")

        try:
            os.chdir(final_path)
            os.mkdir(project_name)
            print(f"[*] Created project folder: {project_name}")

            project_directory = os.path.join(final_path, project_name)
            os.chdir(project_directory)
            print(f"[*] Navigated to project directory: {project_directory}")

            folder_maker(FOLDERS)
            print(f"[*] Created additional folders for project: {FOLDERS}")

            file_writer(project_directory)
            print(
                f"[*] Files for the project were successfully created in: {project_directory}"
            )
        except OSError as ex:
            print(f"[!] Error occured while creating the project structure: {ex}")
    else:
        print(f"[!] Invalid project type selected!")

    # if project_type == 1:
    #     final_path = os.path.join(last_path, DIR_CATEGORIES[0])
    #     os.chdir(final_path)
    #     os.mkdir(project_name)
    #     project_directory = os.path.join(final_path, project_name)
    #     os.chdir(project_directory)
    #
    #     folder_maker(FOLDERS)
    #     file_writer(project_directory)
    #
    # elif project_type == 2:
    #     final_path = os.path.join(last_path, DIR_CATEGORIES[1])
    #     os.chdir(final_path)
    #     os.mkdir(project_name)
    #     project_directory = os.path.join(final_path, project_name)
    #     os.chdir(project_directory)
    #
    #     folder_maker(FOLDERS)
    #     file_writer(project_directory)
    #
    # elif project_type == 3:
    #     final_path = os.path.join(last_path, DIR_CATEGORIES[2])
    #     os.chdir(final_path)
    #     os.mkdir(project_name)
    #     project_directory = os.path.join(final_path, project_name)
    #     os.chdir(project_directory)
    #
    #     folder_maker(FOLDERS)
    #     file_writer(project_directory)
    # elif project_type == 4:
    #     final_path = os.path.join(last_path, DIR_CATEGORIES[3])
    #     os.chdir(final_path)
    #     os.mkdir(project_name)
    #     project_directory = os.path.join(final_path, project_name)
    #     os.chdir(project_directory)
    #
    #     folder_maker(FOLDERS)
    #     file_writer(project_directory)
    # elif project_type == 5:
    #     final_path = os.path.join(last_path, DIR_CATEGORIES[4])
    #     os.chdir(final_path)
    #     os.mkdir(project_name)
    #     project_directory = os.path.join(final_path, project_name)
    #     os.chdir(project_directory)
    #
    #     folder_maker(FOLDERS)
    #     file_writer(project_directory)
    # else:
    #     print("[!] Invalid input!")


def folder_maker(FOLDERS):
    for i in range(len(FOLDERS)):
        try:
            os.mkdir(f"{FOLDERS[i]}")
            i += 1
        except FileExistsError as ex:
            print(f"{ex}")
            continue


def main():
    clear_console()
    lines = "-----------------------"

    print(f"{lines}")
    print("Welcome to the program!")
    print(f"{lines}\n")

    print("[1] Create a full folder structure (Specify location and root folder name)")
    print("[2] Make a project structure inside an exisiting root folder")

    while True:
        try:
            options = int(input("\n[*] Choose an option (1, 2, 0): ").strip())
        except ValueError:
            print("[!] Invalid input. Please enter a valid number.")
            continue

        if options == OPTION_CREATE_STRUCTURE:
            db_creation()
            full_folder_structure()
        elif options == OPTION_ADD_PROJECT:
            project_name = input("[*] What will be your project name?: ")
            print(AVAILABLE_PROJECT_TYPES)
            project_type = int(input("[*] What type of project is?: "))
            project_structure(project_name, project_type)
        elif options == OPTION_FINISH_PROGRAM:
            print("[!] You finished programm! Goodbye!")
            break
        else:
            print("[!] Invalid option. Please enter a valid number.")


if __name__ == "__main__":
    main()
