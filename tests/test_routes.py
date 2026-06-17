def test_home_endpoint(client):
    response = client.get('/')

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "DevSecOps Mini Platform is running"
    assert data["status"] == "ok"

def test_health_endpoint(client):
    response = client.get('/health')

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"

def test_app_info_endpoint(client):
    response = client.get('/api/info')

    assert response.status_code == 200

    data = response.get_json()

    assert data["app_name"] == "DevSecOps Mini Platform"
    assert data["version"] == "0.1.0"
    assert data["environment"] == "development"