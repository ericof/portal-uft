"""Validators."""
import re


def is_valid_email(value: str) -> bool:
    """Check if email is from UFT."""
    return value.endswith("@uft.edu.br")


def is_valid_extension(value: str) -> bool:
    """Check if extension is valid."""
    return re.match(r"^\d{4}$", value)
