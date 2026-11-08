from src.print_number import print_number

def test_print_number():
    expected = [
        "num 1 of max3",
        "num 2 of max3",
        "num 3 of max3"
    ]

    assert print_number(3) == expected
