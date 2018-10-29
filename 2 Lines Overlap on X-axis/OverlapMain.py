from linesOverlap import overlap

# Main method
if __name__ == '__main__':
    try:
        line1=[]             # Empty line 1
        line2=[]             # Empty line 2
        for i in range(2):
            co_ordinate1 = float(input('{0}.Enter co-ordinate for Line 1: \n'.format(i+1)))
            line1.append(co_ordinate1)
        for i in range(2):
            co_ordinate2 = float(input('{0}.Enter co-ordinate for Line 2: \n'.format(i + 1)))
            line2.append(co_ordinate2)

        # Lines --> Tuple
        line1 = tuple(line1)
        line2 = tuple(line2)

        # Calling function Overlap
        result = overlap(line1, line2)
        print(result)

    # Exception handling for entering invalid inputs
    except ValueError:
        print('\n')
        print('_' * 42)
        print('Characters, strings are not allowed\n'
              "Please Enter two co-ordinates on each Line\n{0}".format('_' * 42))
