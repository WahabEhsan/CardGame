# This is the Card Object to be used by the BlackJack or other files
# Wahab Ehsan

class Card:
    __type = ""
    __value = 0
    __color = ""

    def __init__(self, type, value):
        self.__type = type
        self.__value = value
        if type == "Heart" or "Diamond":
            self.__color = "Red"
        else:
            self.__color = "Black"

    def __type(self, type):
        set.__type = type

    def __type(self):
        return self.__type

    def set_value(self, value):
        set.__value = value

    def get_value(self):
        return self.__value

    def get_color(self):
        return self.__color

    def get_weight(self):
        if self.__value == 11:
            return 10
        elif self.__value == 12:
            return 10
        elif self.__value == 13:
            return 10
        elif self.__value == 14:
            return 11
        else:
            return self.__value

    def changeWeightToOne(self):
        if self.__value == 14:
            return 1

    def toString(self):
        val = self.__value
        if self.__value == 11:
            val = "Jack"
        elif self.__value == 12:
            val = "Queen"
        elif self.__value == 13:
            val = "King"
        elif self.__value == 14:
            val = "Ace"
        return "{} of {}".format(val, self.__type)

