"""
Model for collection of tickets

ask (c) 2020. All rights reserved.
"""

import utils
from main.models.ticket import Ticket


class Tickets:
    """
    Tambola tickets
    """

    def __init__(self):
        self.__tickets = []

    def create_tickets(self, count, price):
        for i in range(1, count + 1):
            self.__tickets.append(Ticket(i, utils.generate_ticket(), price))

    def get_tickets(self):
        return self.__tickets

    def find_ticket(self, ticket_no: int) -> [int, Ticket]:
        ticket = [ticket for ticket in self.__tickets if ticket.get_ticket_no() == ticket_no]
        if ticket:
            return ticket[0]
        else:
            return -1

    def get_ticket(self, ticket_no: int) -> [int, Ticket]:
        ticket = self.find_ticket(ticket_no)
        return ticket

    def update_ticket(self, ticket_no, price, ticket_type, status, name):
        ticket = self.find_ticket(ticket_no)
        if ticket:
            ticket.set_price(price)
            ticket.set_type(ticket_type)
            ticket.set_status(status)
            ticket.set_name(name)
            return 0
        else:
            return -1
