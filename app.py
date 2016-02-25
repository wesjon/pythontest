import sys
from models import Bank
from models import InvalidArgsException

def checkArgs(args):
    if len(args) != 3:
        raise InvalidArgsException

if __name__ == '__main__':
    print('- Welcome do Dinda Bank')
    checkArgs(sys.argv)

    dinda = Bank()
    dinda.loadAccountsFromCsv(sys.argv[1])
    dinda.processTransactionsFromCsv(sys.argv[2])
    print dinda
