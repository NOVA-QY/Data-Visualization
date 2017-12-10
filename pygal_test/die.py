from random import randint

class Die(object):
    ''' 表示一个骰子的类 '''

    def __init__(self,number_sizes=6):
        ''' 骰子默认为6 '''
        self.number_sizes=number_sizes
    
    def roll(self):
        ''' 返回一个位于1和骰子面数之间的随机值 '''
        return randint(1,self.number_sizes)