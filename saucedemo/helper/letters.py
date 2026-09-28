"""
Random letters for form fields.

Students: call _letters() when a box only needs letters, such as a name.
Faker builds a new string each time, so the test does not hard-code "Denis".
The postal code is digits, so it does not belong here.
"""

from faker import Faker

# One Faker object for the whole project. Creating it is a bit slow.
_fake = Faker()


def _letters(length: int = 8) -> str:
    """A string of random letters, for example "Kjdmqpla"."""
    return "".join(_fake.random_letters(length=length))
