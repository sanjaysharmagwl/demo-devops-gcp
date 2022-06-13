import pytest
from app import create_app, db
from app import Employee


@pytest.fixture(scope='module')
def new_Employee():
    Employee = Employee(400, "Test","email1")
    return Employee


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('test_config.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    Employee1 = Employee(200, "NZM","Delhi",123.00,124.00,"email2","city2","county2","stat2","zipcode2")
    Employee2 = Employee(300, "BLR","Banglore",123.00,124.00,"email3","city3","county3","stat3","zipcode3")
    db.session.add(Employee1)
    db.session.add(Employee2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()
