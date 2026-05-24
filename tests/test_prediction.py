def test_prediction_success(
    client,
    valid_prediction_data
):

    response = client.post(
        "/predict",
        json=valid_prediction_data
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "confidence" in data


def test_invalid_input(
    client,
    invalid_prediction_data
):

    response = client.post(
        "/predict",
        json=invalid_prediction_data
    )

    assert response.status_code == 422


def test_diabetic_prediction(
    client,
    diabetic_case
):

    response = client.post(
        "/predict",
        json=diabetic_case
    )

    assert response.status_code == 200

    data = response.json()

    assert data["prediction"] == 1


def test_non_diabetic_prediction(
    client,
    non_diabetic_case
):

    response = client.post(
        "/predict",
        json=non_diabetic_case
    )

    assert response.status_code == 200

    data = response.json()

    assert data["prediction"] == 0