"""
Model for Tambola Prize
ask (c) 2020. All rights reserved.
"""
from enum import Enum


class PrizesEnum(Enum):
    FIRST_LINE = 1
    SECOND_LINE = 2
    THIRD_LINE = 3
    EARLY_FIVE = 4
    FULL_HOUSE_1 = 5
    FULL_HOUSE_2 = 6
    FULL_HOUSE_3 = 7
    BOX = 8
    STAR = 9
    HALF_SHEET = 10


class Prizes:
    _prizes = []

    def __init__(self):
        for prize_category in PrizesEnum:
            self._prizes.append(Prize(prize_category))

    def get_prizes(self):
        return self._prizes

    def get_winners(self):
        return [prize.get_winners() for prize in self._prizes]


class Prize:
    """
    Tambola Prize
    """

    def __init__(self, category, prize="", description=""):
        self._prize = prize
        self._category = category
        self._description = description
        self.is_enabled = True
        self._winners = []

    def get_prize(self):
        return self

    def get_winners(self):
        return self._category, self._winners

    def set_winners(self, winners):
        self._winners = winners
