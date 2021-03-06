"""Test secrets reader."""
import os

from websauna.utils import secrets


def test_read_local_secrets():
    """Read file referred by a relative path."""
    data = secrets.read_ini_secrets("test-secrets.ini", strict=False)
    assert data.get("authomatic.secret") == "xxx"


def test_file_secrets():
    """Read file referred by absolute path."""
    data = secrets.read_ini_secrets("file://" + os.path.abspath("test-secrets.ini"), strict=False)
    assert data.get("authomatic.secret") == "xxx"


