def discount(price: float, percent: float) -> float:
    return price * (1 - percent / 100)

def reserve(stock: int, quantity: int) -> int:
    return stock - quantity

def valid_email(value: str) -> bool:
    return '@' in value
