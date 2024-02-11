from typing import Dict, Union, Optional
from pydantic import BaseModel, EmailStr
import logging

# Модель пользователя
class User(BaseModel):
    name: str
    mail: EmailStr
    address: str

# Модель банка
class Bank(BaseModel):
    name: str
    rating: int
    opened: bool

# Модель карты
class Card(BaseModel):
    cardholder: User
    which_bank: Bank
    opened: bool

# Модель баланса
class Balance(BaseModel):
    card: Card
    amount: float
    currency: str

# Функция сложения с явной типизацией и возвратом словаря
def addition(a: int, b: int) -> Dict[str, Union[int, str]]:
    result = a + b
    return {"result": result, "operation": f"{a} + {b}"}

# Функция вычитания с явной типизацией и возвратом словаря
def subtraction(a: int, b: int) -> Dict[str, Union[int, str]]:
    result = a - b
    return {"result": result, "operation": f"{a} - {b}"}

# Функция умножения с явной типизацией и возвратом словаря
def multiplication(a: int, b: int) -> Dict[str, Union[int, str]]:
    result = a * b
    return {"result": result, "operation": f"{a} * {b}"}

# Функция для записи ошибок в лог файл
def log_error(error_message: str):
    with open("error.log", "a") as file:
        file.write(error_message + "\n")

# Пример обработки ошибочной записи
try:
    result = addition("2", 3)  # Пытаемся сложить строку и число
except TypeError as e:
    log_error(str(e))  # Записываем ошибку в лог файл

# Пример использования моделей
user1 = User(name="Alice", mail="alice@example.com", address="123 Main St")
bank1 = Bank(name="Example Bank", rating=5, opened=True)
card1 = Card(cardholder=user1, which_bank=bank1, opened=True)
balance1 = Balance(card=card1, amount=1000.0, currency="USD")

print(balance1)
