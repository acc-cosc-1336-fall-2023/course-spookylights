from random import randint

class Die:
    __roll_value = 0

    def roll(self):
        self.__roll_value = randint(1,6)
        return self.__roll_value
        
    def get_rolled_value(self):
       return self.roll()

    def __str__(self):
        return 'The rolled value is ' + str(self.get_rolled_value())




    