
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
        # string format so table is neat and readable
        # string 'none' is read in as a None (null) object so str() is needed for print
        print("{:<5} {:<10} {:<10} {:<10} {:<14} {:<14} {:<60}"
              .format(str(self.ticket_id), self.ticket_type, self.priority,
                      self.status, str(self.updated_date), str(self.created_date), self.subject))