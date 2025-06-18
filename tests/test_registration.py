import html

def test_registration_success(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'Valid_User',
        'password': 'SecurePass1!'
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    assert response.status_code == 200
    assert "Account created successfully." in response_text
    
def test_registration_long_username(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'A' * 21,  
        'password': 'SecurePass1!'
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    print(response_text)
    assert "Username must be at least 4-20 characters long and contain at least one uppercase and one lowercase letter and only '. , - _' characters." in response_text

def test_registration_short_username(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'A' * 1,  
        'password': 'SecurePass1!'
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    print(response_text)
    assert "Username must be at least 4-20 characters long and contain at least one uppercase and one lowercase letter and only '. , - _' characters." in response_text

def test_registration_username_missing_case(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'alllowercase', 
        'password': 'SecurePass1!'
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    assert "Username must be at least 4-20 characters long and contain at least one uppercase and one lowercase letter and only '. , - _' characters." in response_text  

def test_registration_username_invalid_chars(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'Invalid$User',  
        'password': 'SecurePass1!'
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    assert "Username must be at least 4-20 characters long and contain at least one uppercase and one lowercase letter and only '. , - _' characters." in response_text  

def test_registration_short_password(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'Valid_User',
        'password': 'Short1!' 
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    assert "Password must be at least 8-20 characters long and contain at least one uppercase letter, one lowercase letter, and one number or special character." in response_text  

def test_registration_long_password(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'Valid_User',
        'password': 'A' * 21 
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    assert "Password must be at least 8-20 characters long and contain at least one uppercase letter, one lowercase letter, and one number or special character." in response_text 

def test_registration_password_missing_criteria(test_client):
    #Arrange
    response = test_client.post('/register', data={
        'username': 'Valid_User',
        'password': 'onlyletters' 
    }, follow_redirects=True)

    #Act
    response_text = html.unescape(response.get_data(as_text=True))

    #Assert
    assert "Password must be at least 8-20 characters long and contain at least one uppercase letter, one lowercase letter, and one number or special character." in response_text 
