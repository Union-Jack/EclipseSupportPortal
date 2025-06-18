def test_login_success_redirect(test_client, test_user):
    #Arrange, Act
    response = test_client.post('/login', data={
        'username': test_user["username"],  
        'password': test_user["password"],  
    },follow_redirects=False)  

    #Assert
    assert response.status_code == 302 
    assert response.headers["Location"].endswith("/homepage")

def test_login_wrong_password(test_client, test_user):
    #Arrange
    response = test_client.post('/login', data={
        'username': test_user["username"],  
        'password': 'WrongPass123'  
    }, follow_redirects=True)

    #Act
    response_text = response.get_data(as_text=True)
    
    #Assert
    assert "Incorrect username or password." in response_text  

def test_login_nonexistent_user(test_client):
    #Arrange
    response = test_client.post('/login', data={
        'username': 'FakeUser',  
        'password': 'SecurePass1!'
    }, follow_redirects=True)

    #Act
    response_text = response.get_data(as_text=True)

    #Assert
    assert "Incorrect username or password." in response_text  

def test_homepage_requires_login(test_client):
    # Arrage, Act
    response = test_client.get('/homepage', follow_redirects=False)

    #Assert
    assert response.status_code == 302  
    assert "/login" in response.headers["Location"] 