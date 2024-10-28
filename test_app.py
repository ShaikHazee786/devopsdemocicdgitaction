from app import app

def test_home():
    response=app.test_client().get("/")
    
    assert response.status_code==200
    assert response.data == "Hello, This is CICD with GitAction for Flask App"