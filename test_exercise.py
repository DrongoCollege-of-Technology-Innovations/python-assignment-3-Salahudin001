from exercise import get_average


def test_get_average():
    assert get_average() == 48.0, "Error"


if __name__ == '__main__':
    test_get_average()
    print("Test passed")
