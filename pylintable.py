import random

def greeting():
    if random.randint(0, 1):
        return "Hi"
    else:
        return"Hello"

def print_hi():
    print(greeting())

if __name__ == "__main__":
    print_hi()
