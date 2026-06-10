def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_all_expected_activities(client):
    # Arrange
    expected_activity_count = 9

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert len(payload) == expected_activity_count
    assert "Chess Club" in payload
    assert payload["Chess Club"]["description"]
    assert payload["Chess Club"]["schedule"]
    assert isinstance(payload["Chess Club"]["max_participants"], int)
    assert isinstance(payload["Chess Club"]["participants"], list)
