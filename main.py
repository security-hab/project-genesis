import os
import sqlite3
import time

from config import DIR_CATEGORIES, FOLDERS
from file_writer import file_writer


def db_creation():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS path(
        path TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def full_folder_structure():
    location = input("[*] Enter location where create a full structure: ").strip()
    folder_name = input(
        "[*] Input folder name inside which will be created scructure: "
    )
    folder_path = os.path.join(location, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO path(path) VALUES (?)", (folder_path,))
    conn.commit()

    os.chdir(folder_path)

    for i in range(len(DIR_CATEGORIES)):
        os.mkdir(DIR_CATEGORIES[i])
        print(f"[*] Directory '{DIR_CATEGORIES[i]}' - was created!")
        i += 1
        time.sleep(0.5)


def project_sctructure():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM path")
    folder_path = cursor.fetchall()

    if folder_path:
        data = [row[0] for row in folder_path]

        for i in range(len(DIR_CATEGORIES)):
            destination = os.path.join(data[0], DIR_CATEGORIES[i])
            os.chdir(destination)
            try:
                for i in range(len(FOLDERS)):
                    os.mkdir(f"{FOLDERS[i]}")
                    i += 1
            except FileExistsError as ex:
                print(f"{ex}")
                continue

            file_writer(destination)

            i += 1

    else:
        print("No data found!")


def main():
    lines = "-----------------------"
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{lines}")
    print("Welcome to the program!")
    print(f"{lines}\n")

    print("[1] Create a full folder structure")
    print("[2] Make structure for your project")
    options = int(input("\n[*] Choose option: ").strip())

    if options == 1:
        db_creation()
        full_folder_structure()
    elif options == 2:
        project_sctructure()
    else:
        print("[!] ERROR")


if __name__ == "__main__":
    main()
