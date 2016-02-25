import unittest
from app import Account
from app import Bank
from app import InvalidArgsException
from app import InvalidFormatException
from app import checkArgs
from app import IOException

class TestDindaBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_check_args(self):
        self.assertRaises(InvalidArgsException, checkArgs, ['python', 'file.csv', 'file2.csv', 'file3.csv'])
        self.assertRaises(InvalidArgsException, checkArgs, ['python', 'file.csv'])

    def test_load_non_existent_account_file(self):
        self.assertRaises(IOException, self.bank.loadAccountsFromCsv, 'non_existent_file.csv')

    def test_load_accounts_file_with_no_accounts(self):
        self.bank.loadAccountsFromCsv('test_resources/empty_accounts.csv')
        self.assertEquals(len(self.bank.accounts), 0)

    def test_load_invalid_accounts_file(self):
        self.assertRaises(InvalidFormatException, self.bank.loadAccountsFromCsv, 'test_resources/invalid_accounts_missing_value.csv')
        self.assertRaises(InvalidFormatException, self.bank.loadAccountsFromCsv, 'test_resources/invalid_accounts_missing_key.csv')

    def test_process_non_existent_transaction_file(self):
        self.assertRaises(IOException, self.bank.processTransactionsFromCsv, 'non_existent_file.csv')

    def test_process_transaction_file_with_no_transactions(self):
        self.bank.processTransactionsFromCsv('test_resources/empty_transactions.csv')

    def test_load_invalid_transaction_file(self):
        self.assertRaises(InvalidFormatException, self.bank.processTransactionsFromCsv, 'test_resources/invalid_transactions_missing_key.csv')

    def test_process_debit_transaction_with_fee(self):
        account = Account(1,0)
        account.processTransaction(-1)
        self.assertEquals(account.balance, -6)

    def test_process_debit_transaction(self):
        account = Account(1,101)
        account.processTransaction(-1)
        self.assertEquals(account.balance, 100)

    def test_process_credit_transaction(self):
        account = Account(1,0)
        account.processTransaction(1000)
        self.assertEquals(account.balance, 1000)

if __name__ == '__main__':
    unittest.main()
