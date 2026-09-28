"""
Accounts from the .env file.

Students: each line is one pair, login/password.

    STANDARD_USER=standard_user/secret_sauce

Read it with the same short name:

    login.login(get_user("standard"), get_password("standard"))

Short names: standard, locked_out, problem, performance_glitch, error, visual.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# .env sits in the project folder, one level above Data/.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")


def get_user(name: str) -> str:
    """Login (the part before /) for one account."""
    login, _password = _account(name)
    return login


def get_password(name: str) -> str:
    """Password (the part after /) for the same account."""
    _login, password = _account(name)
    return password


def _account(name: str) -> tuple[str, str]:
    """
    Split one .env value into login and password.

    STANDARD_USER=standard_user/secret_sauce
    becomes ("standard_user", "secret_sauce").
    """
    short_name = name.strip().lower()
    raw = _required(f"{short_name.upper()}_USER")
    login, separator, password = raw.partition("/")
    if not separator or not login or not password:
        raise RuntimeError(f"{short_name.upper()}_USER must look like login/password.")
    return login, password


def _required(key: str) -> str:
    value = os.getenv(key, "").strip()
    if not value:
        raise RuntimeError(
            f"Missing {key}. Add it to the .env file in the project folder."
        )
    return value
