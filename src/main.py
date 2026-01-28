from src.utils.startup_utils import *

"""
main.py

Program entry point.
Responsible for the main menu loop and user interaction flow.
"""

print('Welcome to the APOD Logger.')
print('Startup Banner & Startup Art Here')
startup_banner()
startup_art()

if not check_if_data_exists():
    create_data_directory()

if not check_if_user_settings_exist():
    create_user_settings()

if not check_if_json_output_exists():
    create_json_output_file()

if not check_if_csv_output_exists():
    create_csv_output_file()
    print()

# Entry Prompt
entry_flag = True
while entry_flag:
    try:
        entry_choice = int(input(
            "[1] Get started\n"
            "[2] Quit\n\n"
            "Option: "
        ))

        match entry_choice:
            case 1:
                entry_flag = False
            case 2:
                print("\nGoodbye 👋")
                exit()
            case _:
                print("Invalid input: Please enter 1 or 2.")
    except ValueError:
        print("Invalid input: Please enter 1 or 2.")


# Main Menu
flag = True
while flag:
    print('\n======================= Main Menu ☄️ =======================\n')
    increment_launch_count(int(get_launch_count()['launch_count']))

    try:
        user_choice = int(input(
            "[1] Make a NASA APOD Request\n"
            "[2] View/Manage saved logs\n"
            "[3] Change Setting\n"
            "[4] Goodbye 👋\n\n"
            "Option: "
        ))

        match user_choice:
            case 1:
                nasa_apods_menu()
            case 2:
                output_files_menu()
            case 3:
                user_settings_menu()
            case 4:
                print("\nGoodbye 👋")
                flag = False

    except ValueError:
        print("Invalid input: Please enter a number from 1 to 4.")
    except Exception as e:
        print(e)