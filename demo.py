def add(a: int, b: int) -> int: return a + b
def sub(a: int, b: int) -> int: return a - b
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def main():
    print('Addition:', add(10, 5))
    print('Subtraction:', sub(10, 5))
if __name__ == '__main__':
    main()
