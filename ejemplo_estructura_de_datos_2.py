import pprint

theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}

## pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] +'I'+ board['top-M'] +'I'+ board['top-R'])
    print("-----")
    print(board['mid-L'] +'I'+ board['mid-M'] +'I'+ board['mid-R'])
    print('-----')
    print(board['low-L'] +'I'+ board['low-M'] +'I'+ board['low-R'])

printBoard(theBoard)
