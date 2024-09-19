# import sys
# from stock_monitoring.cli import cli


# def run_cli_command(command):
#     """Directly invoke CLI commands."""
#     try:
#         cli.main(args=command)
#     except Exception as e:
#         print(f"Error executing command: {str(e)}")


# def show_menu():
#     """Display the menu options."""
#     print("Stock Monitoring CLI Application")
#     print("1. Add Item")
#     print("2. Add Stock")
#     print("3. Check Stock")
#     print("4. Create User")
#     print("5. List Items")
#     print("6. List Users")
#     print("7. Remove Item")
#     print("8. Remove User")
#     print("9. Exit")


# def main():
#     """Main function to handle user input and execute commands."""
#     while True:
#         show_menu()
#         choice = input("Enter your choice (1-9): ")

#         if choice == '1':
#             item_name = input("Enter item name: ")
#             item_category = input("Enter item category: ")
#             run_cli_command(['add-item', item_name, item_category])

#         elif choice == '2':
#             item_name = input("Enter item name: ")
#             quantity = input("Enter quantity: ")
#             run_cli_command(['add-stock', item_name, quantity])

#         # elif choice == '3':
#         #     item_name = input("Enter item name: ")
#         #     run_cli_command(['check-stock', item_name])

#         elif choice == '3':
#             item_name = input("Enter item name: ")
#             quantity = int(input("Enter quantity: "))
#             status = input("Enter status (available, damaged, out_of_stock): ")
#             run_cli_command(['add-stock', item_name, quantity, status])

#         elif choice == '4':
#             username = input("Enter username: ")
#             role = input("Enter user role: ")
#             run_cli_command(['create-user', username, role])

#         elif choice == '5':
#             run_cli_command(['list-items'])

#         elif choice == '6':
#             run_cli_command(['list-users'])

#         elif choice == '7':
#             item_name = input("Enter item name: ")
#             run_cli_command(['remove-item', item_name])

#         elif choice == '8':
#             user_id = input("Enter user ID: ")
#             run_cli_command(['remove-user', user_id])

#         elif choice == '9':
#             print("Exiting...")
#             sys.exit(0)

#         else:
#             print("Invalid choice. Please enter a number between 1 and 9.")


# if __name__ == "__main__":
#     main()


import sys
from stock_monitoring.cli import cli

def run_cli_command(command):
    """Directly invoke CLI commands."""
    try:
        cli.main(args=command)
    except Exception as e:
        print(f"Error executing command: {str(e)}")

def show_menu():
    """Display the menu options."""
    print("Stock Monitoring CLI Application")
    print("1. Add Item")
    print("2. Add Stock")
    print("3. Check Stock")
    print("4. Create User")
    print("5. List Items")
    print("6. List Users")
    print("7. Remove Item")
    print("8. Remove User")
    print("9. Exit")

def main():
    """Main function to handle user input and execute commands."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            item_name = input("Enter item name: ")
            item_category = input("Enter item category: ")
            run_cli_command(['add-item', item_name, item_category])

        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            status = input("Enter status (available, damaged, out_of_stock): ")
            run_cli_command(['add-stock', item_name, quantity, status])

        elif choice == '3':
            item_name = input("Enter item name: ")
            run_cli_command(['check-stock', item_name])

        elif choice == '4':
            username = input("Enter username: ")
            role = input("Enter user role: ")
            run_cli_command(['create-user', username, role])

        elif choice == '5':
            run_cli_command(['list-items'])

        elif choice == '6':
            run_cli_command(['list-users'])

        elif choice == '7':
            item_name = input("Enter item name: ")
            run_cli_command(['remove-item', item_name])

        elif choice == '8':
            user_id = int(input("Enter user ID: "))
            run_cli_command(['remove-user', user_id])

        elif choice == '9':
            print("Exiting...")
            sys.exit(0)

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
