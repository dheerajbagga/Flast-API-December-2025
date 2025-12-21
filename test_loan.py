from loan import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_home_route(client):    
    response = client.get('/') #sending a GET request to the home route
    assert response.status_code == 200 #checking if the response status code is 200 (OK)
    assert b"Welcome to the Loan Management System" in response.data #checking if the expected text is in the response data

def test_predict_route_approved(client):
    data = {
        "Gender": "Male",
        "Married": "Married",
        "ApplicantIncome": 5000,
        "LoanAmount": 100,
        "Credit_History": 1
    }
   
    response = client.post('/predict', json=data) #sending a POST request to
    assert response.status_code == 200
    assert response.json == {"The predicted loan status is": "Approved"}