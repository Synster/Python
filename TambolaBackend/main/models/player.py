"""
Model for Tambola Player
ask (c) 2020. All rights reserved.
"""


class Player:
    """
    Tambola Player
    """

    def __init__(self, ticket_no, name="", contact_no="", email=""):
        self._ticket_no = ticket_no
        self._name = name
        self._contact_no = contact_no
        self._email = email

    def get_player(self):
        return self

    def set_name(self, name):
        self._name = name

    def set_contact_no(self, contact_no):
        self._contact_no = contact_no

    def set_email(self, email):
        self._email = email
