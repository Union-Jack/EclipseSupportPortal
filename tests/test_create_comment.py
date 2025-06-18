from conftest import login

def test_user_can_create_comment(test_client, test_user, user_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])
    
    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/comment",
        data={"content": "This is a test comment from a user"},
        follow_redirects=True
    )

    #Assert
    assert response.status_code == 200
    assert "This is a test comment from a user" in response.get_data(as_text=True)

def test_admin_can_create_comment(test_client, test_admin, user_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.post(
        f"/tickets/{user_ticket['ticket_id']}/comment",
        data={"content": "This is a test comment from an admin"},
        follow_redirects=True
    )

    #Assert
    assert response.status_code == 200
    assert "This is a test comment from an admin" in response.get_data(as_text=True)