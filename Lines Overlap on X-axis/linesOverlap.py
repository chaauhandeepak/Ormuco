'''
write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and
returns whether they overlap. As an example, (1,5) and (2,6) overlaps
but not (1,5) and (6,8).
'''

# Function that accepts two lines on x-axis
def OverLap(line1,line2):
    Found = False                # Flag

    # result variable
    result = str(line1) + ' & ' + str(line2) + ' doesn\'t overlaps on x-axis'
    pos=0                        # Index position of Lines

    for i in range(2):
        # Method evaluates negative integers
        if line1[i] < 0 and line2[i] < 0:
            while pos < len(line1) and not Found:
                if line2[pos] >= line1[0] or line2[pos] >= line1[1]:
                    Found = True
                    result = str(line1) + ' & ' + str(line2) + ' overlaps on x-axis'
                else:
                    pos += 1

        # Method evaluates positive integers
        else:
            while pos < len(line1) and not Found:
                if line2[pos] <= line1[0] or line2[pos] <= line1[1]:
                    Found = True
                    result = str(line1) + ' & ' + str(line2) + ' overlaps on x-axis'
                else:
                    pos += 1

    return '\n' + result







