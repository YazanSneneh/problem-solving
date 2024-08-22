import pytest
from source.oop.bank_account import BankAccount

@pytest.fixture
def bank_account():
    return BankAccount("Yazan", initial_balance=100)


def test_initialize_bank_account(bank_account):
    assert bank_account.owner == "Yazan"


def test_deposit(bank_account):
        amount = 50
        result = bank_account.deposit(amount)
        assert result == f"Deposited: {amount}", "deposite method failed no match"


def test_withdraw(bank_account):
    amount = 30
    bank_account.deposit(50)
    result = bank_account.withdraw(amount)
    assert result ==  f"Withdraw: {amount}, Balance: {bank_account.balance}"


    def test_check_balance(bank_account):
        result = bank_account.check_balance()
        assert result == f"Your current balance: {0}"


#commented out class based test to apply fixture
# class TestBankAccount:
#
#     def setup_method(self, method):
#         self.account = BankAccount("Yazan A. Sneneh")
#
#     def teardown_method(self, method):
#         del self.account
#
#     def test_init(self):
#         assert self.account.owner == "Yazan A. Sneneh"
#
#     def test_deposit(self):
#         amount = 50
#         result = self.account.deposit(amount)
#         assert result == f"Deposited: {amount}", "deposite method failed no match"
#
#     def test_withdraw(self):
#         amount = 30
#         self.account.deposit(50)
#         result = self.account.withdraw(amount)
#         assert result ==  f"Withdraw: {amount}, Balance: {self.account.balance}"
#
#     def test_check_balance(self):
#         result = self.account.check_balance()
#         assert result == f"Your current balance: {0}"
