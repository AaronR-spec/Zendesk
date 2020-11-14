from viewer import Viewer


def menu():
    print("\nZendesk Ticket Viewer")
    # user = input('Email: ')
    # Tried using getpass() but ide console isn't the same as getpass
    # pwd = input('Password: ')
    # password and username for testing would use above code for final realise
    user = 'd00222467@student.dkit.ie'
    pwd = 'aaronreihillzendesk'
    # Viewer is initialized
    ticket_viewer = Viewer(user, pwd)
    # string format for the header of the ticket prints
    ticket_display_header = "\n{:<5} {:<10} {:<10} {:<10} {:<14} {:<14} {:<60}".format("Id", "Type", "Priority",
                                                                                       "Status", "Updated",
                                                                                       "Created", "Subject")
    while True:
        # menu options
        print("\n1.Display Tickets \n2.Display Ticket By Id \n3.Exit/Quit")
        # user input option
        user = input("Option: ")
        if user == '1':
            print(ticket_display_header, '\n', '-' * 74)
            ticket_viewer.display()
        elif user == '2':
            # error handling for string to int conversion
            try:
                ticket_id = int(input("Id: "))
                print(ticket_display_header, '\n', '-' * 74)
                ticket_viewer.get_ticket(ticket_id)
            except ValueError:
                print("Id entered is not a valid, please try again..")
        elif user == '3':
            print("Goodbye... Have a good day")
            break
        # any invalid input is handled and response is displayed
        else:
            print("Sorry " + user + " was not an option..")


if __name__ == "__main__":
    # starts the system
    menu()
