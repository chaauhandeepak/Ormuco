
class ValueComparsions:
    def __init__(self, valueOne, valueTwo):
        self.val1 = float(valueOne)
        self.val2 = float(valueTwo)

    def greater(self):
        if self.val1 > self.val2:
            return str(self.val1) + ' is greater than ' + str(self.val2)
        else:
            return str(self.val2) + ' is greater than ' + str(self.val1)

    def equal(self):
        if self.val1 == self.val2:
            return str(self.val1) + ' is equal to ' + str(self.val2)
        else:
            return str(self.val1) + ' not equal ' + str(self.val2)

    def lesser(self):
        if self.val1 < self.val2:
            return str(self.val1) + ' is lesser than ' + str(self.val2)
        else:
            return str(self.val2) + ' is lesser than ' + str(self.val1)




