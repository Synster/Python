"""
Model for tambola game

ask (c) 2020. All rights reserved.
"""


from enum import Enum

from main.models import Prizes
from main.models.tickets import Tickets


class MODE(Enum):
    AUTO = 1
    MANUAL = 2


class Game:
    """
    Tambola Game
    """

    def __init__(self, date, time):
        self._date = date
        self._time = time
        self._mode = MODE.AUTO
        self._tickets = Tickets()
        self.prizes = Prizes()

    def get_ticket(self, ticket_no):
        return self._tickets.get_ticket(ticket_no)

    def get_tickets(self):
        return self._tickets

    def set_tickets(self, tickets):
        self._tickets = tickets

    def get_time(self):
        return self._time

    def set_time(self, time):
        self._time = time

    def get_date(self):
        return self._time

    def set_date(self, date):
        self._date = date

    def get_mode(self):
        return self._mode

    def set_mode(self, mode):
        self._mode = mode
