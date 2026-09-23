from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def detect_incident(events):
    event_types = [event["type"] for event in events]

    if (
        "failed_login" in event_types
        and "successful_login" in event_types
        and "unusual_file_access" in event_types
    ):
        return True

    return False


@app.route("/")
def home():
    return jsonify({"message": "Security Event Correlation API is running"})


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True)

    if not data or "events" not in data:
        return jsonify({"error": "Request body must include an 'events' list"}), 400

    events = data["events"]

    if not isinstance(events, list) or len(events) == 0:
        return jsonify({"error": "'events' must be a non-empty list"}), 400

    incident_detected = detect_incident(events)

    result = {
        "events": events,
        "incident_detected": incident_detected,
    }

    if incident_detected:
        result["severity"] = "HIGH"
        result["recommended_response"] = "Investigate the account and review file activity."
    else:
        result["severity"] = "NONE"
        result["recommended_response"] = "No suspicious incident detected."

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
