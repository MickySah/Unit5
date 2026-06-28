import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import app as app_module


def test_remove_participant_from_activity():
    client = TestClient(app_module.app)
    app_module.activities["Chess Club"]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    signup_response = client.post(
        "/activities/Chess Club/signup?email=test@example.com"
    )
    assert signup_response.status_code == 200

    delete_response = client.delete(
        "/activities/Chess Club/participants/test@example.com"
    )
    assert delete_response.status_code == 200
    assert "test@example.com" not in app_module.activities["Chess Club"]["participants"]
