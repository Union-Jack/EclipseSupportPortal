from conftest import login

def test_admin_can_delete_ticket_navigation(test_client, test_admin, user_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/delete", follow_redirects=True
    )

    #Assert
    assert response.status_code == 200

def test_user_cannot_delete_ticket_navigation(test_client, test_user, user_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/delete", follow_redirects=False
    )
    
    #Assert
    assert response.status_code == 403

def test_admin_can_delete_ticket(test_client, test_admin, user_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/delete",
        follow_redirects=True,
    )

    #Assert
    assert response.status_code == 200
    assert response.request.path == "/homepage"
