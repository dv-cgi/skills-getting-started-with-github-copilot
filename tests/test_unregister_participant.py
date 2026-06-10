from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = activities[activity_name]["participants"][0]

    response = client.delete(f"/activities/{activity_name}/participants?email={email}")

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]


def test_signup_updates_activity_participants():
    activity_name = "Chess Club"
    email = "signup-refresh@example.com"

    if email in activities[activity_name]["participants"]:
        activities[activity_name]["participants"].remove(email)

    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    assert response.status_code == 200
    refreshed = client.get("/activities")
    assert email in refreshed.json()[activity_name]["participants"]

    activities[activity_name]["participants"].remove(email)
