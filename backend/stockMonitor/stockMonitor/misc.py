import os

__all__ = []

TRUE_STATE = (
    "",
    "true",
    "yes",
    "1",
    "y",
)


def get_env_bool(key: str, default_value: str | None) -> bool:
    """Get a boolean value from environment variables or return default"""
    data = os.environ.get(key, default_value).lower()
    return data in TRUE_STATE


def get_env_str(key: str, default_value: str | None) -> str:
    """Get a string value from environment variables or return default"""
    return os.environ.get(key, default_value)


def get_env_list(key: str, default_value: str | None) -> list[str]:
    """Get a list of values from environment variables or return default"""
    data = os.environ.get(key, default_value).split(",")
    return list(filter(None, data))
