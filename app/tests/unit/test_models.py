"""
This file (test_models.py) contains the unit tests for the models.py file.
Only one test case is included for demonstration.
"""
from app import Employee

def test_new_Employee():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    Employee1 = Employee(400, "TC1","tc1@tc1.com")
    assert Employee1.id == 400
    assert Employee1.name == "TC1_CITY"
    assert Employee1.email == "TC1_CITY"

    