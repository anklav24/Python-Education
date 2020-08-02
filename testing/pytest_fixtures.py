import pytest


@pytest.fixture()
def tempfile():
    with TemporaryFile() as f:
        yield f


def test_with_tempdir(tempfile):
    tempfile.write(b'hello')
    tempfile.seek(0)
    assert tempfile.read() == b'hello'
