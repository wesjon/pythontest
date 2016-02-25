import os
import csv
import sys

# Classes
class Account:
    def __init__(self,id,balance):
        self.id = id
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return str(self.id) + ',' + str(self.balance)

    def processTransaction(self, transaction):
        fee = 0
        if self.balance + transaction < 0:
            fee = -5

        self.balance = self.balance + transaction + fee
        self.transactions.append(transaction)

class Bank:
    accountsMap = dict({})
    def __init__(self):
        self.accounts = []

    def __str__(self):
        output = ''
        for account in self.accounts:
            output += str(account) + '\n'

        return output;

    def loadAccountsFromCsv(self, csvFilePath):
        try:
            with open(csvFilePath) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    account = Account(int(row['id']), int(row['balance']))
                    self.accountsMap[row['id']] = account
                    self.accounts.append(account)
        except (KeyError, ValueError):
            raise InvalidFormatException(csvFilePath)
        except IOError:
            raise IOException(csvFilePath)

    def processTransactionsFromCsv(self, csvFilePath):
        try:
            with open(csvFilePath) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    accountId = row['account_id']
                    if accountId in self.accountsMap:
                        account = self.accountsMap[accountId]
                        account.processTransaction(int(row['value']))
        except (KeyError, ValueError):
            raise InvalidFormatException(csvFilePath)
        except IOError:
            raise IOException(csvFilePath)

# Exceptions
class InvalidArgsException(Exception):
    def __init__(self):
        if __name__ == '__main__':
            sys.exit('Invalid arguments')

class IOException(Exception):
    def __init__(self, file):
        if __name__ == '__main__':
            sys.exit('Error reading the file' + file + '. Please check if the file exists')

class InvalidFormatException(Exception):
    def __init__(self, file):
        if __name__ == '__main__':
            sys.exit('Error processing the file ' + file + '. Please make sure you are using a valid CSV')

def checkArgs(args):
    if len(args) != 3:
        raise InvalidArgsException

#############
# Begging
#############
if __name__ == '__main__':
    print('- Welcome do Dinda Bank')
    checkArgs(sys.argv)

    dinda = Bank()
    dinda.loadAccountsFromCsv(sys.argv[1])
    dinda.processTransactionsFromCsv(sys.argv[2])
    print dinda
