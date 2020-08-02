"""
Model for tambola ticket
Enums for Status Ticket Type

ask (c) 2020. All rights reserved.
"""

from enum import Enum

import numpy as np

from main.models import Player


class Status(Enum):
    UNSOLD = 1
    SOLD = 2


class Type(Enum):
    REGULAR = 1
    PREMIUM = 2


class Ticket:
    """
    Tambola ticket
    """

    def __init__(self, ticket_no, ticket, price):
        self._ticket_no = ticket_no
        self._player = Player(ticket_no)
        self._ticket_type = Type.REGULAR
        self._status = Status.UNSOLD
        self._price = price
        self.__ticket = ticket
        self._ticket = ticket.copy()

    def get_ticket_no(self):
        return self._ticket_no

    def set_ticket_no(self, ticket_no):
        self._ticket_no = ticket_no

    def get_player_name(self):
        return self._player

    def set_player(self, player):
        self._player = player

    def get_type(self):
        return self._ticket_type

    def set_type(self, ticket_type):
        self._ticket_type = ticket_type

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price:
            self._price = price

    def get_ticket(self):
        return self._ticket

    def set_ticket(self, ticket):
        self._ticket = ticket
        self.__ticket = ticket.copy()

    def strike_number(self, number):
        self.__ticket[self.__ticket == number] = -1

    def has_top_line(self):
        return np.sum(self.__ticket[0]) == -5

    def has_middle_line(self):
        return np.sum(self.__ticket[1]) == -5

    def has_bottom_line(self):
        return np.sum(self.__ticket[2]) == -5

    def has_full_house1(self):
        return np.sum(self.__ticket) == -15

    def has_full_house2(self):
        return np.sum(self.__ticket) == -15

    def has_full_house3(self):
        return np.sum(self.__ticket) == -15

    def has_early_five(self):
        return np.sum(self.__ticket) == -5

    def has_star(self):
        pass

    def has_box_bonus(self):
        pass

    def has_half_sheet(self):
        pass
