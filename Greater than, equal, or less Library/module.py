
class ValueComparsions:
    def __init__(self,ValueOne,ValueTwo):
        self.val1=float(ValueOne)
        self.val2=float(ValueTwo)

    def Greater(self):
        if self.val1>self.val2:
            return str(self.val1) + ' is greater than ' + str(self.val2)
        else:
            return str(self.val2) + ' is greater than ' + str(self.val1)

    def Equal(self):
        if self.val1==self.val2:
            return str(self.val1) + ' is equal to ' + str(self.val2)
        else:
            return str(self.val1) + ' not equal ' + str(self.val2)
'''
    def Lesser(self):
        if self.val1<self.val2:
            return str(self.val1) + ' is lesser than ' + str(self.val2)
        else:
            return str(self.val2) + ' is lesser than ' + str(self.val1)

'''
class lesser(ValueComparsions):

    def __init__(self, ValueOne, ValueTwo):
        ValueComparsions.__init__(ValueOne, ValueTwo)


    def less(self):
        if self.val1 < self.val2:
            return str(self.val1) + ' is lesser than ' + str(self.val2)
        else:
            return str(self.val2) + ' is lesser than ' + str(self.val1)


