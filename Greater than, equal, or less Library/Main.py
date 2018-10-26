
from twostring import ValueComparsions

if __name__ == '__main__':
    str1 = input('Enter a string Number 1\n')
    str2 = input('Enter a string Number 2 \n')
    result = ValueComparsions(str1,str2)
    print(result.greater())
    print(result.equal())
    print(result.lesser())



