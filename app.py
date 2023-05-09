import random
import time

"""
011 = ---
100 = - -
000 = ---*
111 = - -*


"""
book = {1:['---','---','---','---','---','---'], 2:['- -','- -','- -','- -','- -','- -']}



class hexagram:
    def __init__(self):
        self.lines = ['---', '- -', '---*', '- -*']
        self.result = []
        self.change = []

    def create_line(self):
        line = []
        coin = [0,1]
        for toss in range(3):
            line.append(random.choice(coin))
        throw = sum(line)
        if throw == 0:
            return '---*'
        elif throw == 1:
            return '- -'
        elif throw == 2:
            return '---'
        elif throw == 3:
            return '- -*'


    def cast(self):
        random.seed(time.time())
        for throws in range(6):
            self.result.append(self.create_line())
        print(self.result)
        if '---*' in self.result:
            old_light = '---*'
            young_darkness = '- -'
            self.change = [young_darkness if x == old_light else x for x in self.result]
            if '- -*' in self.result:
                great_darkness = '- -*'
                young_light = '---'
                self.change = [young_light if x == great_darkness else x for x in self.change]
        elif '- -*' in self.result:
            great_darkness = '- -*'
            young_light = '---'
            self.change = [young_light if x == great_darkness else x for x in self.change]
            if '---*' in self.result:
                old_light = '---*'
                young_darkness = '- -'
                self.change = [young_darkness if x == old_light else x for x in self.result]
        print(self.change)


    def printHex(self):
        printable_hex = self.result[::-1]
        printable_change = self.change[::-1]
        print('##Cast Hexagram##')
        for line in printable_hex:
            print(line+'\n')
        print('#################')
        print('###Transformed###')
        for line in printable_change:
            print(line+'\n')



if __name__ == '__main__':
    ching = hexagram()
    ching.cast()
    ching.printHex()
