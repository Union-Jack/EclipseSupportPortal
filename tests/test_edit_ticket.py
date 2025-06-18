from conftest import login

def test_admin_edit_own_ticket_navigation(test_client, test_admin, admin_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.get(f"/tickets/{admin_ticket['ticket_id']}/edit", follow_redirects=True)
    
    #Assert 
    assert response.status_code == 200  
    assert response.request.path == f"/tickets/{admin_ticket['ticket_id']}/edit"  

def test_admin_edit_any_ticket_navigation(test_client, test_admin, user_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.get(f"/tickets/{user_ticket['ticket_id']}/edit", follow_redirects=True)
    
    #Assert
    assert response.status_code == 200  
    assert response.request.path == f"/tickets/{user_ticket['ticket_id']}/edit"  

def test_user_edit_own_ticket_navigation(test_client, test_user, user_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.get(f"/tickets/{user_ticket['ticket_id']}/edit", follow_redirects=True)
    
    #Assert 
    assert response.status_code == 200  
    assert response.request.path == f"/tickets/{user_ticket['ticket_id']}/edit"  

def test_admin_can_edit_ticket(test_client, test_admin, user_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])
    
    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/edit",
        data={"title": "Edited by Admin", "description": "Admin update"},
        follow_redirects=True,
    )

    #Assert 
    assert response.status_code == 200
    assert "Edited by Admin" in response.get_data(as_text=True)

def test_user_can_edit_own_ticket(test_client, test_user, user_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/edit",
        data={"title": "User Updated", "description": "Update by user"},
        follow_redirects=True,
    )

    #Assert
    assert response.status_code == 200
    assert "User Updated" in response.get_data(as_text=True)

def test_user_cannot_edit_others_ticket_navigation(test_client, test_user, admin_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.get(f"/tickets/{admin_ticket['ticket_id']}/edit", follow_redirects=True)
    
    #Assert uncessful navigation to the edit ticket page
    assert response.status_code == 403  
    assert response.request.path == f"/tickets/{admin_ticket['ticket_id']}/edit"  

def test_user_cannot_edit_others_ticket(test_client, test_user, admin_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.post(
        f"/tickets/{admin_ticket['ticket_id']}/edit",
        data={"title": "Unauthorised User Updated", "description": "Update by unauthorised user"},
        follow_redirects=False,
    )

    #Assert
    assert response.status_code == 403

def test_user_cannot_edit_ticket_with_invalid_title(test_client, test_user, user_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/edit",
        data={
            "title": "!!!###", 
            "description": "Still trying to edit"
        },
        follow_redirects=True
    )

    #Assert
    assert response.status_code == 200
    assert "Title must contain at least three letters and can only include letters and spaces." in response.get_data(as_text=True)
