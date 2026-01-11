from typing import Any

SENSITIVE_KEYS = {
    "password",
    "hashed_password",
    "token",
    "access_token",
    "refresh_token",
    "secret",
}


def sanitize_payload(data: Any) -> Any:
    """
    Recursively sanitize dictionaries & lists.
    Replaces sensitive values with '[REDACTED]'.
    """
    if isinstance(data, dict):
        return {
            k: "[REDACTED]" if k in SENSITIVE_KEYS else sanitize_payload(v)
            for k, v in data.items()
        }

    if isinstance(data, list):
        return [sanitize_payload(item) for item in data]

    return data
