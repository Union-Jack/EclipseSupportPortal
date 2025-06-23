# Tests were written follwing the 'Testing Flask Applications' Flask documentation (Flask, no date).
from conftest import login

def test_user_can_navigate_to_edit_comment(test_client, test_user, user_ticket, user_comment):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.get(
        f"/tickets/{user_ticket['ticket_id']}/comments/{user_comment['comment_id']}/edit",
        follow_redirects=True
    )

    #Assert
    assert response.status_code == 200
    assert response.request.path == f"/tickets/{user_ticket['ticket_id']}/comments/{user_comment['comment_id']}/edit"

def test_admin_can_navigate_to_edit_comment(test_client, test_admin, admin_ticket, admin_comment):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.get(
        f"/tickets/{admin_ticket['ticket_id']}/comments/{admin_comment['comment_id']}/edit",
        follow_redirects=True
    )

    #Assert
    assert response.status_code == 200
    assert response.request.path == f"/tickets/{admin_ticket['ticket_id']}/comments/{admin_comment['comment_id']}/edit"

def test_user_cannot_navigate_to_other_edit_comment(test_client, test_user, admin_ticket, admin_comment):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.get(
        f"tickets/{admin_ticket['ticket_id']}/comments/{admin_comment['comment_id']}/edit",
        follow_redirects=False
    )

    #Assert
    assert response.status_code == 403

def test_admin_cannot_navigate_to_other_edit_comment(test_client, test_admin, user_ticket, user_comment):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.get(
        f"tickets/{user_ticket['ticket_id']}/comments/{user_comment['comment_id']}/edit",
        follow_redirects=False
    )

    #Assert
    assert response.status_code == 403

def test_user_can_submit_edit_comment(test_client, test_user, user_ticket, user_comment):
    #Arrange
    login(test_client, test_user["username"], test_user["password"])

    #Act
    response = test_client.post(
        f"tickets/{user_ticket['ticket_id']}/comments/{user_comment['comment_id']}/edit",
        data={"content": "User edited comment text"},
        follow_redirects=True
    )

    #Assert
    assert response.status_code == 200
    assert "User edited comment text" in response.get_data(as_text=True)

def test_admin_can_submit_edit_comment(test_client, test_admin, admin_ticket, admin_comment):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"])

    #Act
    response = test_client.post(
        f"tickets/{admin_ticket['ticket_id']}/comments/{admin_comment['comment_id']}/edit",
        data={"content": "User edited comment text"},
        follow_redirects=True
    )

    #Assert
    assert response.status_code == 200
    assert "User edited comment text" in response.get_data(as_text=True)

