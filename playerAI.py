# This is the Card Object to be used by the BlackJack or other files
# Wahab Ehsan

import random


class AiBlackJack:
    __player_name = ""
    ai_hand = []
    aipicked = []

    def __init__(self):
        player_num = random.randrange(0, 5)
        if player_num == 0:
            self.__player_name = "George"
        elif player_num == 1:
            self.__player_name = "Bob"
        elif player_num == 2:
            self.__player_name = "John"
        elif player_num == 3:
            self.__player_name = "Billy"
        elif player_num == 4:
            self.__player_name = "Steve"
        elif player_num == 5:
            self.__player_name = "Max"
        print(self.__player_name + " is your computer opponent.")

    def get_name(self):
        return self.get_name()

    def ai_processing(self):
        risk = random.randrange(0,5)
        permission = random.randrange(0,1)
        while loop2:
            if (risk == 5) and sum > 18 :
                hitai
            if sum < 18:
                hitai
            else:
                if permission == 1:
                    hitai
                else:
                    loop2 = False