class Ticket:

    def __init__(self, ticket_id, created_date, updated_date, ticket_type, subject, priority, status):
        self.ticket_id = ticket_id
        self.created_date = created_date
        self.updated_date = updated_date
        self.ticket_type = str(ticket_type)
        self.subject = str(subject)
        self.priority = str(priority)
        self.status = str(status)

    def display(self):
        print(str(self.ticket_id) + ", " + self.created_date + ", " + self.updated_date + ", " + self.ticket_type + ", "
              + self.subject + ", " + self.priority + ", " + self.status)
