import pytest
from flask import Flask
from auth import app, users
import bcrypt
import jwt
from datetime import datetime, timedelta

# Mock Flask app for testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test password hashing
def test_password_hashing():
    user = User()
    user.set_password("testpassword")
    assert bcrypt.checkpw("testpassword".encode('utf-8'), user.password_hash.encode('utf-8'))

# Test JWT token generation
def test_jwt_token():
    with app.test_request_context():
        response = app.post('/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        assert response.status_code == 200
        assert 'token' in response.json

# Test rate limiting
def test_rate_limiting(client):
    for _ in range(501):
        response = client.post('/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        if _ == 0:
            assert response.status_code == 200
        else:
            assert response.status_code == 429