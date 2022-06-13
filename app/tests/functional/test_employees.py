
def test_valid_login_logout(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/Employees' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/Employees',
                                data=dict(id='500', name='test500',email='test500@test.com'),
                                follow_redirects=True)
    
    assert response.status_code == 200
    assert b'id' in response.data
    assert b'name' in response.data
    assert b'email' in response.data

    """
    GIVEN a Flask application configured for testing
    WHEN the '/Employees' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/Employees', follow_redirects=True)
    assert response.status_code == 200
    assert b'id' not in response.data
    assert b'name' in response.data
    assert b'login' in response.data




def test_valid_employee_creation(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/Employees' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/Employees',
                     data=dict(id='800',
                               name='test8',
                               email='test8@email.com'),
                     follow_redirects=True)

    assert response.status_code == 200
    assert b'id' in response.data
    assert b'name' in response.data
    assert b'email' in response.data



def test_invalid_employee(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/Employees' page is posted to with invalid email (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/Employees',
                     data=dict(id='900',
                               name='test9',
                               email='test@email'),
                     follow_redirects=True)

    assert response.status_code == 400


def test_duplicate_employee(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/Employees' page is posted to (POST) using an email email already used
    THEN check an error message is returned to the user
    """
    # Create New employee
    test_client.post('/Employees',
                     data=dict(id='100',
                               name='test1',
                               email='test@email.com'),
                     follow_redirects=True)
    
    # Try creating new employee with the same email
    response = test_client.post('/Employees',
                                data=dict(id='200',
                                          name='test2',
                                          email='test@email.com'),
                                follow_redirects=True)
    
    assert response.status_code == 400
