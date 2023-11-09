import unittest

from src.examples.j_classes.bank_account import BankAccount

class TestConfig(unittest.TestCase):
    

    def test_get_balance(self):
        my_account = BankAccount(100)
        self.assertEqual(my_account.get_balance(), 100)
    
    def test_account_deposit(self):
        my_account = BankAccount(100)
        my_account.account_deposit(50)
        self.assertEqual(my_account.get_balance(), 150)