import pytest
from bank import BankAccount

def test_overdraft_raises_value_error():
    acc = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(250)

def test_negative_deposit_error_message():
    acc = BankAccount(100)
    with pytest.raises(ValueError) as exc_info:
        acc.deposit(-10)
    assert "positive" in str(exc_info.value)

def test_string_input_raises_type_error():
    acc = BankAccount(100)
    with pytest.raises(TypeError):
        acc.withdraw("50")