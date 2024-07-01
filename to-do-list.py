def view_list():
    try:
        with open("list.txt", 'r') as f:
            lists = f.read()
            if len(lists.strip()) == 0:
                print("Currently Empty, Add to see")
            else:
                print(lists)
    except FileNotFoundError:
        print("File 'list.txt' not found.")

def add_list(txt):
    try:
        with open("list.txt", 'a+') as f:
            f.write(f"{txt}\n")
            print(f"Task '{txt}' added.")
    except IOError:
        print("Error: Unable to write to 'list.txt'.")

run = True
while run:
    print('''Choose :
    1. View
    2. Add
    3. Remove
    4. Close
    ''')

    ans = input("Enter an option: ")

    if ans == '1':
        view_list()
    elif ans == '2':
        text = input("Enter a task: ")
        add_list(text)
    elif ans == '3':
        try:
            with open("list.txt", 'r+') as f:
                lines = f.readlines()
                # print(lines)
                if len(lines) == 0:
                    print("Nothing to remove, list is empty.")
                else:
                    removed_task = lines.pop().strip()
                    f.seek(0)
                    f.truncate()
                    f.write(''.join(lines))
                    print(f"Removed task: {removed_task}")
        except IOError:
            print("Error: Unable to update 'list.txt'.")

    elif ans == '4':
        run = False
    else:
        print("Enter a valid option (1-4).")
