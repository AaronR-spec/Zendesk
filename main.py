from viewer import Viewer


def menu():
    ticket_viewer = Viewer()
    print("\nZendesk Ticket Viewer")
    ticket_display_header = "{:<5} {:<10} {:<10} {:<10} {:<14} {:<14} {:<60}".format("Id", "Type", "Priority",
                                                                                     "Status", "Updated",
                                                                                     "Created", "Subject")
    while True:
        print("\n1.Display Tickets \n2.Display Ticket By Id \n3.Exit/Quit")
        user = input("Option: ")

        if user == '1':
            print(ticket_display_header, '\n', '-' * 74)
            ticket_viewer.display()
        elif user == '2':
            try:
                ticket_id = int(input("Id: "))
                print(ticket_display_header, '\n', '-' * 74)
                ticket_viewer.get_ticket(ticket_id)
            except ValueError:
                print("Id entered is not a valid, please try again..")
        elif user == '3':
            print("Goodbye... Have a good day")
            break
        else:
            print("Sorry " + user + " was not an option..")


if __name__ == "__main__":
    menu()
