
# 🌟 Project Genesis

**Project Genesis** is a tool for automating the generation of a new project's structure. 🚀 It allows you to quickly create standard directories, files, and initialize a project in seconds.

## ✨ Features
- 📁 Create a root project folder in a user-specified location.
- 🗂️ Generate category structures (`parsing`, `scripts`, `web`, etc.).
- 📦 Create subdirectories (`src`, `tests`, `config`, etc.).
- 📝 Automatically initialize standard files:
  - `.gitignore`
  - `main.py`
  - `README.md`
  - `requirements.txt`
  - `setup.py`
  - Templates for modules and tests.

## 🔧 Usage
1. Run `main.py`:
   ```bash
   python main.py
   ```
2. Choose one of the options:
   - `[1] Create a full folder structure` — Create a complete project structure.
   - `[2] Make structure for your project` — Configure the structure for an existing project.

3. Follow the instructions in the terminal.

## 🛠️ Requirements
- Python 3.6+
- SQLite3 (comes pre-installed with Python)
- Operating system with Python support (Windows, Linux, macOS)

## 🗂️ Example Project Structure
After running the program, the structure may look like this:
```
Project/
├── parsing/
├── scripts/
├── web/
├── data-analysis/
├── other/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── module1.py
│   │   └── module2.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_module1.py
│   │   └── test_module2.py
│   ├── config/
│   │   ├── settings.yaml
│   │   └── logging.conf
│   ├── .gitignore
│   ├── main.py
│   ├── README.md
│   ├── requirements.txt
│   └── setup.py
```

## 👨‍💻 Author
Developed to automate and streamline the initialization of new projects. 🎉
