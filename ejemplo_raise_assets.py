'''

**************
*            *
*            *
**************

'''
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of lentgh 1.')
    if (width < 2) or (height < 2):
        raise Exception('"width, height" must be greater or equal than 2')
    
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    
    print(symbol * width)
boxPrint('o', 1, 1)
