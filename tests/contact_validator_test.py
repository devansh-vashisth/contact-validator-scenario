import pytest

from src.contact_validator import (
    is_valid_email,
    is_valid_phone,
    mask_email,
    normalize_phone,
)


# ==========================================
# Tests for is_valid_email()
# ==========================================

def test_valid_email():
    assert is_valid_email("priya@example.com") is True


def test_invalid_email():
    assert is_valid_email("priyaexample.com") is False


def test_is_valid_email_non_string():
    with pytest.raises(TypeError):
        is_valid_email(12345)


# ==========================================
# Tests for is_valid_phone()
# ==========================================

def test_valid_phone():
    assert is_valid_phone("5551234567") is True


def test_valid_phone_with_dashes():
    assert is_valid_phone("555-123-4567") is True


def test_invalid_phone():
    assert is_valid_phone("12345") is False


def test_phone_non_string():
    with pytest.raises(TypeError):
        is_valid_phone(1234567890)


# ==========================================
# Tests for mask_email()
# ==========================================

def test_mask_email_basic():
    assert mask_email("priya@example.com") == "pr***@example.com"


def test_mask_email_short_local():
    assert mask_email("ab@example.com") == "a*@example.com"


def test_mask_email_invalid():
    with pytest.raises(ValueError):
        mask_email("invalid-email")


# ==========================================
# Tests for normalize_phone()
# ==========================================

def test_normalize_phone_valid():
    assert normalize_phone("555-123-4567") == "5551234567"


def test_normalize_phone_without_dashes():
    assert normalize_phone("5551234567") == "5551234567"


def test_normalize_phone_invalid():
    with pytest.raises(ValueError):
        normalize_phone("12345")