import os
import sqlite3
import time

from config import DIR_CATEGORIES, FOLDERS
from file_writer import file_writer

OPTION_CREATE_STRUCTURE = 1
OPTION_ADD_PROJECT = 2
OPTION_FINISH_PROGRAM = 0
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.db")


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
        print(f"[*] Path '{folder_path}' has been added to the database!")
    # conn.commit()

    os.chdir(folder_path)

    for i in range(len(DIR_CATEGORIES)):
        os.mkdir(DIR_CATEGORIES[i])
        print(f"[*] Directory '{DIR_CATEGORIES[i]}' - was created!")
        i += 1
        time.sleep(0.5)


def project_structure():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM path")
        folder_paths = cursor.fetchall()

    if not folder_paths:
        print("[!] No saved paths found in the database!")
        return

    last_path = folder_paths[-1][0]

    for i in range(len(DIR_CATEGORIES)):
        destination = os.path.join(last_path, DIR_CATEGORIES[i])
        os.chdir(destination)

        for i in range(len(FOLDERS)):
            try:
                os.mkdir(f"{FOLDERS[i]}")
                i += 1
            except FileExistsError as ex:
                print(f"{ex}")
                continue

        file_writer(destination)

        i += 1


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
            project_structure()
        elif options == OPTION_FINISH_PROGRAM:
            print("[!] You finished programm! Goodbye!")
            break
        else:
            print("[!] Invalid option. Please enter a valid number.")


if __name__ == "__main__":
    main()
