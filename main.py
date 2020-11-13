import requests
from ticket import Ticket


def get_tickets():
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
    return create_tickets(data)


def create_tickets(data):
    ticket_list = []
    for d in data['tickets']:
        # #    # ticket_id, created_date, updated_date, ticket_type, subject, priority, status):
        id = d['id']
        created_date = d['created_at']
        updated_date = d['updated_at']
        ticket_type = d['type']
        subject = d['subject']
        priority = d['priority']
        status = d['status']
        ticket = Ticket(id, created_date, updated_date, ticket_type, subject, priority, status)
        ticket_list.append(ticket)
    return ticket_list


def ticket_by_id(ticket_id, ticket_list):
    start = 0
    end = len(ticket_list) - 1

    while start <= end:
        mid = start + (end - start) // 2
        current = ticket_list[mid]
        if current.ticket_id == ticket_id:
            return current
        elif ticket_id < current.ticket_id:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == "__main__":
    tickets = get_tickets()
    amount_tickets = len(tickets)
    record_index = 0
    ticket_by_id(7, tickets).display()

    # display it in pages
    # if amount_tickets > 25:
    #     i = 0
    #     while i < amount_tickets:
    #         if record_index > 25:
    #             user = input("Next page Y/N: ")
    #             if user.lower() != 'y':
    #                 break
    #             record_index = 0
    #         tickets[i].print()
    #         record_index = record_index + 1
    #         i = i + 1


