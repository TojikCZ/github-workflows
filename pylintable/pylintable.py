"""Tests that pylint works correctly"""
import random

def greeting():
    """returns Hi or Hello at random"""
    if random.randint(0, 1):
        return "Hi"
    return "Hello"

def print_hi():
    """Prints whatever greeting it's given"""
    print(greeting())

if __name__ == "__main__":
    print_hi()
    print("fixed")
