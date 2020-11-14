from ticket import Ticket
import requests
import datetime


class Viewer:

    def __init__(self, user, pwd):
        # holds list of Ticket objects and processes them
        self._tickets = self.__get_tickets(user, pwd)

    def get_ticket(self, ticket_id):
        if isinstance(ticket_id, str):
            return False
        start = 0
        end = len(self._tickets) - 1
        # Binary search making it a O(logN) search instead of O(N), better for scalability
        while start <= end:
            mid = start + (end - start) // 2
            current = self._tickets[mid]
            if current.ticket_id == ticket_id:
                # returns when found making it not have to continue after found
                current.display()
                return True
            elif ticket_id < current.ticket_id:
                end = mid - 1
            else:
                start = mid + 1
        print("Ticket Not Found")
        return False

    def display(self):
        # number of tickets displayed per page
        tickets_per_page = 24
        # nothing in list so it has nothing to display
        if len(self._tickets) <= 0:
            print("Nothing Here To Display..")
            return False
        amount_tickets = len(self._tickets)
        # index of current ticket index
        record_index = 0
        # index of records per page
        i = 0
        # resets to 0 if onto new page
        if amount_tickets > tickets_per_page:
            i = 0
        while i < amount_tickets:
            # option to go to next page or not (any other input then y,Y returns user to menu)
            if record_index > tickets_per_page:
                user = input("Next page Y/N: ")
                if user.lower() != 'y':
                    print("Returning to menu..")
                    break
                record_index = 0
            # displays ticket
            self._tickets[i].display()
            # increments index's
            record_index += 1
            i += 1
        return True

    def __get_tickets(self, user, pwd):
        # API url subdomain
        url = 'https://aaronreihill.zendesk.com/api/v2/tickets.json'
        # Do the HTTP get request, user and pwd are passed in
        response = requests.get(url, auth=(user, pwd))
        # Check for HTTP codes other than 200
        status_code = response.status_code
        if status_code != 200:
            # status code isn't 200 meaning their is a problem
            if status_code == 404:
                print('Status:', status_code, 'Problem with the request to the API.')
            elif status_code == 401:
                print("Status:", status_code, "Couldn't authenticate you")
            return []
        # Decode the JSON response into a dictionary and pass data to create_tickets for parsing
        data = response.json()
        return self.__create_tickets(data)

    @staticmethod
    def __create_tickets(data):
        ticket_list = []
        # string to date format
        format_str = "%Y-%m-%dT%H:%M:%SZ"
        # loops through data and parses making new ticket object form it
        for d in data['tickets']:
            ticket_id = d['id']
            created = d['created_at']
            updated = d['updated_at']
            created_date = datetime.datetime.strptime(created, format_str).date()
            updated_date = datetime.datetime.strptime(updated, format_str).date()
            ticket_type = d['type']
            subject = d['subject']
            priority = d['priority']
            status = d['status']
            ticket = Ticket(ticket_id, created_date, updated_date, ticket_type, subject, priority, status)
            # add new ticket to list of tickets
            ticket_list.append(ticket)
        return ticket_list
