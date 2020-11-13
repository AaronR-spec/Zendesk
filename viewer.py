from ticket import Ticket
import requests


class Viewer:

    def __init__(self):
        self.tickets = self.get_tickets()

    def get_tickets(self):
        url = 'https://aaronreihill.zendesk.com/api/v2/tickets.json'
        user = 'd00222467@student.dkit.ie'
        pwd = 'aaronreihillzendesk'

        # Do the HTTP get request
        response = requests.get(url, auth=(user, pwd))

        # Check for HTTP codes other than 200
        if response.status_code != 200:
            print('Status:', response.status_code, 'Problem with the request. Exiting.')

        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        return self.create_tickets(data)

    @staticmethod
    def create_tickets(data):
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

    def ticket_by_id(self, ticket_id):
        start = 0
        end = len(self.tickets) - 1

        while start <= end:
            mid = start + (end - start) // 2
            current = self.tickets[mid]
            if current.ticket_id == ticket_id:
                return current
            elif ticket_id < current.ticket_id:
                end = mid - 1
            else:
                start = mid + 1
        return None

    def display(self):
        amount_tickets = len(self.tickets)
        record_index = 0
        if amount_tickets > 25:
            i = 0
        while i < amount_tickets:
            if record_index > 25:
                user = input("Next page Y/N: ")
                if user.lower() != 'y':
                    break
                record_index = 0
            self.tickets[i].display()
            record_index = record_index + 1
            i += 1
