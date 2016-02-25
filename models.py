import csv
import sys

# Classes
class Account(object):
    def __init__(self,accountId,balance):
        self.accountId = accountId
        self.balance = balance
        self.transactions = []

    def __str__(self):
        return str(self.accountId) + ',' + str(self.balance)

    def processTransaction(self, transaction):
        fee = 0
        if self.balance + transaction < 0:
            fee = -5

        self.balance = self.balance + transaction + fee
        self.transactions.append(transaction)

class Bank(object):
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
    def __init__(self, filePath):
        if __name__ == '__main__':
            sys.exit('Error reading the file' + filePath + '. Please check if the file exists')

class InvalidFormatException(Exception):
    def __init__(self, filePath):
        if __name__ == '__main__':
            sys.exit('Error processing the file ' + filePath + '. Please make sure you are using a valid CSV')
