import pytest
from fastapi.testclient import TestClient

from api.app import app


# Fixture 1
@pytest.fixture
def client():
    return TestClient(app)


# Fixture 2
@pytest.fixture
def valid_prediction_data():

    return {
        "gender": "Male",
        "age": 52,
        "hypertension": 1,
        "heart_disease": 0,
        "smoking_history": "former",
        "bmi": 31.2,
        "HbA1c_level": 7.1,
        "blood_glucose_level": 185
    }


# Fixture 3
@pytest.fixture
def invalid_prediction_data():

    return {
        "gender": "Male"
    }


# Fixture 4
@pytest.fixture
def diabetic_case():

    return {
        "gender": "Female",
        "age": 61,
        "hypertension": 1,
        "heart_disease": 1,
        "smoking_history": "current",
        "bmi": 36.5,
        "HbA1c_level": 9.2,
        "blood_glucose_level": 250
    }


# Fixture 5
@pytest.fixture
def non_diabetic_case():

    return {
        "gender": "Male",
        "age": 24,
        "hypertension": 0,
        "heart_disease": 0,
        "smoking_history": "never",
        "bmi": 22.4,
        "HbA1c_level": 4.9,
        "blood_glucose_level": 92
    }