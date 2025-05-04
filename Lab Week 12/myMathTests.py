import pytest
import math
from myMath import add, subtract, multiply, divide, power, factorial, is_prime, sum_of_digits, gcd, celsius_to_fahrenheit, fahrenheit_to_celsius

# Error was in divide, fahrenheit_to_celsius and celsuis_to_fahrenheit functions.

def test_add():
    assert add(1, 2) == 3
    assert add(-5, 3) == -2
    assert add(-5, -2) == -7
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(-5, -5) == 0
    assert subtract(-5, 2) == -7
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(0, 5) == 0
    assert multiply(-1, 5) == -5
    assert multiply(5, 2) == 10
    assert multiply(-5, -2) == 10

def test_divide():
    assert divide(10, 5) == 2
    assert divide(5, 2) == 2.5
    assert divide(-10, 5)  == -2
    assert divide(-10, -5) == 2
    assert divide(1, 0) == "ERROR: Can't divide with '0'"

def test_power():
    assert power(2, 4) == 16
    assert power(-2, 4) == 16
    assert power(2, -4) == 1/16
    assert power(-2, 3) == -8 
    assert power(-2, -3) == -1/8
    assert power(0, 0) == 1
    assert power(8, 0) == 1

def test_factorial():
    assert factorial(0) == 1 
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(1) == 1
    assert factorial(-1) == "Input cannot be negative"

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-1) == False
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(9) == False
    assert is_prime(13) == True
    assert is_prime(11) == True 

def test_sum_of_digits():
    assert sum_of_digits(524) == 11
    assert sum_of_digits(628) == 16

def test_gcd():
    assert gcd(15, 10) == 5
    assert gcd(10, 2) == 2
    assert gcd(81, 18) == 9

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(30) == 86
    assert celsius_to_fahrenheit(-5) == 23

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(86) == 30
    assert fahrenheit_to_celsius(23) == -5