import re

def discount(price: float, percent: float) -> float:
    if price < 0 or not 0 <= percent <= 100:
        raise ValueError('price must be non-negative and discount 0..100')
    return price * (1 - percent / 100)

def reserve(stock: int, quantity: int) -> int:
    if quantity <= 0 or quantity > stock:
        raise ValueError('quantity must be available and positive')
    return stock - quantity

def valid_email(value: str) -> bool:
    return bool(re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', value))
