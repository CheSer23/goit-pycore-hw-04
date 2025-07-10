# Task 1 ***************************************************

def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 2:
                    continue
                name, salary_str = parts
                try:
                    salary = float(salary_str)
                except ValueError:
                    continue
                total += salary
                count += 1
            if count == 0:
                return 0, 0
            average = total / count
            return total, average

    except FileNotFoundError:
        print(f"Файл '{path}' відсутній.")
        return 0, 0
    except Exception as e:
        print(f"Файл {e} пошкоджений")
        return 0, 0



# Task 2 ***************************************************

def get_cats_info(path):
    cats = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    continue
                cat_id, name, age = parts
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats.append(cat_info)
        return cats
    except FileNotFoundError:
        print(f"Файл '{path}' відсутній.")
        return []
    except Exception as e:
        print(f"Файл {e} пошкоджений")
        return []



# Task 3 ***************************************************

import sys
from pathlib import Path
from colorama import init, Fore, Style
def print_tree(path: Path, indent=0):
    indent_str = " " * (indent * 4)
    if path.is_dir():
        print(f"{indent_str}{Fore.BLUE}{path.name}/{Style.RESET_ALL}")
        for child in sorted(path.iterdir(), key=lambda x: x.name.lower()):
            print_tree(child, indent + 1)
    else:
        print(f"{indent_str}{Fore.GREEN}{path.name}{Style.RESET_ALL}")
def main():
    init()
    if len(sys.argv) != 2:
        print("Використання: python hw-04.py /шлях/до/директорії")
        sys.exit(1)
    root_path = Path(sys.argv[1])
    if not root_path.exists():
        print(f"Шлях {root_path} не існує.")
        sys.exit(1)
    if not root_path.is_dir():
        print(f"Шлях {root_path} не є директорією.")
        sys.exit(1)
    print_tree(root_path)
if __name__ == "__main__":
    main()

# Я не уверен, правильный это код или нет, так как командой "python hw-04.py "D:\GoIT\PythonCourse\Home work\goit-pycore-hw-04"" он не запускается
# Что бы запустить его, необходимо ввести "python "D:\GoIT\PythonCourse\Home work\goit-pycore-hw-04\hw-04.py" "D:\GoIT\PythonCourse\Home work\goit-pycore-hw-04"
# , а это уже не то, что требовалось в задании



# Task 4 ****************************************************

def parse_input(user_input):
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid input. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
def main_II():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
if __name__ == "__main_II__":
    main_II()
