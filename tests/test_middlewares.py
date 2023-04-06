import src.middlewares.cors as cors


def test_all_origin_are_none():
    origin = [None, None]
    assert cors.get_origin_list(origin) == ["*"]


def test_some_origin_are_none():
    origin = ["localhost", None, "google.com"]
    assert cors.get_origin_list(origin) == ["localhost", "google.com"]


def test_empty_list():
    origin = []
    assert cors.get_origin_list(origin) == ["*"]


def test_all_origin_are_not_none():
    origin = ["localhost", "http://localhost", "https://localhost"]
    assert cors.get_origin_list(origin) == origin
