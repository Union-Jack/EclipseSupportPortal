# Tests were written follwing the 'Testing Flask Applications' Flask documentation (Flask, no date).
from conftest import login

def test_admin_view_own_ticket_navigation(test_client, test_admin, admin_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"]) 
    
    #Act
    response = test_client.get(f'/tickets/{admin_ticket["ticket_id"]}', follow_redirects=True)
    
    #Assert successful navigation to the view the specified ticket
    assert response.status_code == 200 
    assert response.request.path == f"/tickets/{admin_ticket['ticket_id']}"

def test_admin_view_any_ticket_navigation(test_client, test_admin, user_ticket):
    #Arrange
    login(test_client, test_admin["username"], test_admin["password"]) 
    
    #Act
    response = test_client.get(f'/tickets/{user_ticket["ticket_id"]}', follow_redirects=True)
    
    #Assert successful navigation to the view the specified ticket
    assert response.status_code == 200 
    assert response.request.path == f"/tickets/{user_ticket['ticket_id']}"

def test_user_view_own_ticket_navigation(test_client, test_user, user_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"]) 
    
    #Act
    response = test_client.get(f'/tickets/{user_ticket["ticket_id"]}', follow_redirects=True)
    
    #Assert successful navigation to the view the specified ticket
    assert response.status_code == 200 
    assert response.request.path == f"/tickets/{user_ticket['ticket_id']}"

def test_user_cannot_view_any_ticket_navigation(test_client, test_user, admin_ticket):
    #Arrange
    login(test_client, test_user["username"], test_user["password"]) 
    
    #Act
    response = test_client.get(f'/tickets/{admin_ticket["ticket_id"]}', follow_redirects=True)
    
    #Assert unssuccessful navigation to the view the specified ticket
    assert response.status_code == 403 
    assert response.request.path == f"/tickets/{admin_ticket['ticket_id']}"