from ticket import Ticket
import requests


class Viewer:

    def __init__(self):
        self.tickets = self.__get_tickets()

    def get_ticket(self, ticket_id):
        start = 0
        end = len(self.tickets) - 1
        # Binary search making it a O(logN) search instead of O(N), better for scalability
        while start <= end:
            mid = start + (end - start) // 2
            current = self.tickets[mid]
            if current.ticket_id == ticket_id:
                return current
            elif ticket_id < current.ticket_id:
                end = mid - 1
            else:
                start = mid + 1
        print("Ticket Not Found")

    def add(self, ticket):
        self.tickets.append(ticket)

    def display(self):
        tickets_per_page = 24
        if len(self.tickets) <= 0:
            print("Nothing To Display")
            return
        amount_tickets = len(self.tickets)
        record_index = 0
        i = 0
        if amount_tickets > tickets_per_page:
            i = 0
        while i < amount_tickets:
            if record_index > tickets_per_page:
                user = input("Next page Y/N: ")
                if user.lower() != 'y':
                    break
                record_index = 0
            self.tickets[i].display()
            record_index += 1
            i += 1

    def __get_tickets(self):
        url = 'https://aaronreihill.zendesk.com/api/v2/tickets.json'
        user = 'd00222467@student.dkit.ie'
        pwd = 'aaronreihillzendesk'

        # Do the HTTP get request
        response = requests.get(url, auth=(user, pwd))

        # Check for HTTP codes other than 200
        status_code = response.status_code
        if status_code != 200:
            if status_code == 404:
                print('Status:', status_code, 'Problem with the request to the API.')
            elif status_code == 401:
                print("Couldn't authenticate you")
            return []
        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        return self.__create_tickets(data)

    @staticmethod
    def __create_tickets(data):
        ticket_list = []
        for d in data['tickets']:
            # #    # ticket_id, created_date, updated_date, ticket_type, subject, priority, status):
            ticket_id = d['id']
            created_date = d['created_at']
            updated_date = d['updated_at']
            ticket_type = d['type']
            subject = d['subject']
            priority = d['priority']
            status = d['status']
            ticket = Ticket(ticket_id, created_date, updated_date, ticket_type, subject, priority, status)
            ticket_list.append(ticket)
        return ticket_list
