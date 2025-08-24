import sys

from datetime import datetime


thank_you = "\nThank you for using the Journal CLI tool created by BelacEr."
valid_numbers = "\nMake sure to enter only valid numbers."
no_journal = "\nThere is no journal, please write one."
file = "my_journal.txt"

def enter_number(prompt):
    """Make sure that only whole numbers are entered for the menu."""
    while True:
        try:
            return int(input(prompt))
        except EOFError:
            print(thank_you)
            sys.exit()
        except KeyboardInterrupt:
            print(thank_you)
            sys.exit()
        except ValueError:
            print(valid_numbers)


def write_entry():
    """Write the entry and save it to a file with a date stamp."""
    # Ask what you want to write.
    while True:
        try:
            entry = input("\nWhat's on your mind? ")
            break
        except KeyboardInterrupt:
            print(thank_you)
            sys.exit()
        except EOFError:
            print(thank_you)
            sys.exit()
    
    # Get the current data and time.
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")

    # Open your journal file and save your entry.
    with open("my_journal.txt", "a") as file:
        file.write(f"{timestamp} - {entry}\n")
    
    print("\nEntry saved. I'll always keep your words safe. ♡")


def read_entries():
    """Read entries from the file."""
    print("\nOpening your journal...")

    # Open the file in read mode.
    try:
        with open("my_journal.txt", "r") as file:
            entries = file.readlines()
    except FileNotFoundError:
        print(no_journal)
    else:
        # Check if it's empty.
        if not entries:
            print("\nYour journal is empty. Please write a journal.")
        else:
            # Print each entry one by one.
            for entry in entries:
                print(entry.strip())


def delete_entry():
    try:
        with open("my_journal.txt", "r") as file:
            entries = file.readlines()
    except FileNotFoundError:
        print(no_journal)
        return

    if not entries:
        print("\nThere's no journal to delete from. Write something first.")
        return

    print("\nHere are your entries: ")
    for index, entry in enumerate(entries, start=1):
        print(f"{index}. {entry}")

    
    choice = enter_number("\nWhich entry would you like to remove (Enter the number): ")
    if 1 <= choice <= len(entries):
        # Remove the chosen entry
        del entries[choice - 1]

        # Write the remaining entries back to the file:
        with open("my_journal.txt", "w") as file:
            file.writelines(entries)

        print("\nEntry deleted.")
    else:
        print("\nThat entry doesn't exist. Let's try again?")
    

def show_menu():
    print("""
==== JOURNAL CLI TOOL MENU ====
1. Write journal
2. Read journal
3. Delete journal
4. Exit
""")


def main():
    """Main function of the program."""
    while True:
        show_menu()
        choice = enter_number("Enter your choice: ")
        
        if choice == 1:
            write_entry()
        elif choice == 2:
            read_entries()
        elif choice == 3:
            delete_entry()
        elif choice == 4:
            print(thank_you)
            break
        else:
            print(valid_numbers)

