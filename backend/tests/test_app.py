import pytest
from app import app  # นำเข้าแอปพลิเคชันจากไฟล์หลัก

# Fixture สำหรับ client ของ Flask
@pytest.fixture
def client():
    app.config['TESTING'] = True  # ตั้งค่าให้แอปเป็นโหมดทดสอบ
    with app.test_client() as client:
        yield client  # ส่งคืน client ให้ทดสอบ

# ทดสอบ endpoint หลัก
def test_hello(client):
    """ทดสอบ endpoint หลัก"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()  # แปลงเป็น JSON
    assert data['message'] == 'Hello World!'
    assert data['status'] == 'running'

# ทดสอบ endpoint health check
def test_health(client):
    """ทดสอบ health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()  # แปลงเป็น JSON
    assert data['status'] == 'healthy'
    assert 'database' in data  # ตรวจสอบว่ามี key 'database' หรือไม่
    assert 'redis' in data  # ตรวจสอบว่ามี key 'redis' หรือไม่

# ทดสอบการคำนวณเบื้องต้น
def test_math_operations():
    """ทดสอบคำนวณพื้นฐาน"""
    assert 1 + 1 == 2
    assert 2 * 3 == 6
