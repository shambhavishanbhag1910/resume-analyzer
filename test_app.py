from app import app

def test_predict():

    client = app.test_client()

    response = client.post('/predict', json={
        "resume": "machine learning python"
    })

    data = response.get_json()

    assert response.status_code == 200
    assert data['predicted_role'] == "AI Engineer"
    assert set(data['skills_found']) == {"machine learning", "python"}
