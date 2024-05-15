def test_version_should_be_available():
    from testing import version

    assert version.__version__
    assert version.__version_tuple__
