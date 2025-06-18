from conftest import login

def test_admin_create_ticket_navigation(test_client, test_admin):
    #Arrage
    login(test_client, test_admin["username"], test_admin["password"])
    
    #Act
    response = test_client.get("/tickets/create", follow_redirects=True)

    #Assert
    assert response.status_code == 200
    assert response.request.path == "/tickets/create"

def test_user_create_ticket_navigation(test_client, test_user):
    #Arrage
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.get("/tickets/create", follow_redirects=True)

    #Assert
    assert response.status_code == 200
    assert response.request.path == "/tickets/create"


def test_admin_can_create_ticket(test_client, test_admin):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.post("/tickets/create", data={
        "title": "Admin Test Ticket",
        "description": "Created by admin for testing"
    }, follow_redirects=True)

    #Assert
    assert response.status_code == 200
    assert "Admin Test Ticket" in response.get_data(as_text=True)

def test_user_can_create_ticket(test_client, test_user):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])
    
    #Act
    response = test_client.post("/tickets/create", data={
        "title": "User Test Ticket",
        "description": "Created by regular user"
    }, follow_redirects=True)

    #Assert
    assert response.status_code == 200
    assert "User Test Ticket" in response.get_data(as_text=True)

def test_user_cannot_create_ticket_with_invalid_title(test_client, test_user):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.post("/tickets/create", data={
        "title": "12345!!!",
        "description": "This should fail due to title format"
    }, follow_redirects=True)

    #Assert
    assert response.status_code == 200
    assert "Title must contain at least three letters and can only include letters and spaces." in response.get_data(as_text=True)