class Ticket(object):

    def __init__(self, ticket_id, created_date, updated_date, ticket_type, subject, priority, status):
        self.ticket_id = ticket_id
        self.created_date = created_date
        self.updated_date = updated_date
        self.ticket_type = ticket_type
        self.subject = subject
        self.priority = priority
        self.status = status

    def display(self):
        print(str(self.ticket_id) + ", " + self.created_date + ", " + self.updated_date + ", " + str(self.ticket_type) + ", "
              + self.subject + ", " + str(self.priority) + ", " + self.status)


