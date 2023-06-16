from view_specific_report_options import *
from colors import *

def view_specific_report_top_menu(conn):
    """Top level menu for viewing a specific report."""
    choice_action = """1. View all records from a selected field
2. View all films from a selected year
3. View all films with a selected rating
4. View all films from a selected genre
5. Exit this sub-menu\n""" 
    
    while True:
        try:
            choice_action = int(input(choice_action))
            match choice_action:
                case 1:
                    view_specific_report_1()
                    continue 
                case 2:
                    view_specific_report_2()
                    continue
                case 3:
                    view_specific_report_3()
                    continue
                case 4:
                    view_specific_report_4()
                    continue
                case 5:
                    print("Exiting")
                    break
                case _:
                    print(f"{bcolors.FAIL}input error, please try again{bcolors.ENDC}")
                    continue
        except ValueError:
                print(f"{choice_action} is not a valid value.")
                continue

    # top_level_choice = get_view_specific_report_top_level_menu()

    # the_description = "View report of: "
    # the_query = f"""SELECT * FROM films WHERE {column}={value};"""
    # table_print_to_terminal(conn, the_description, the_query)