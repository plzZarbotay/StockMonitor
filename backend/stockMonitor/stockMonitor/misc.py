import os

__all__ = []

TRUE_STATE = (
    "",
    "true",
    "yes",
    "1",
    "y",
)


def get_env_bool(key: str, default: str | None) -> bool:
    """Get a boolean value from environment variables or return default"""
    data = os.environ.get(key, default).lower()
    return data in TRUE_STATE


def get_env_str(key: str, default: str | None) -> str:
    """Get a string value from environment variables or return default"""
    return os.environ.get(key, default)


def get_env_int(key: str, default: int | None) -> int:
    """Get a integer value from environment variables or return default"""
    return int(os.environ.get(key, default))


def get_env_list(key: str, default: str | None) -> list[str]:
    """Get a list of values from environment variables or return default"""
    data = os.environ.get(key, default).split(",")
    return list(filter(None, data))
