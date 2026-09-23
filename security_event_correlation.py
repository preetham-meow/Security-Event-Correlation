events = [
    {"user": "user1", "type": "failed_login", "time": "10:00"},
    {"user": "user1", "type": "successful_login", "time": "10:05"},
    {"user": "user1", "type": "unusual_file_access", "time": "10:10"}
]


def detect_incident(events):
    event_types = [event["type"] for event in events]

    if (
        "failed_login" in event_types
        and "successful_login" in event_types
        and "unusual_file_access" in event_types
    ):
        return True

    return False


print("SECURITY EVENT CORRELATION SYSTEM")
print("----------------------------------")

for event in events:
    print(event["time"], "->", event["type"])

if detect_incident(events):
    print("\n🚨 SECURITY INCIDENT DETECTED")
    print("Severity: HIGH")
    print("Recommended Response:")
    print("Investigate the account and review file activity.")
else:
    print("\nNo suspicious incident detected.")
