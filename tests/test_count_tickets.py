from src.count_tickets import revermapping

def test_revermapping():
    tickets = {
        1: "A",
        2: "B",
        3: "A",
        4: "B",
        5: "A",
        6: "C"
    }

    expected = {
        "A": 3,
        "B": 2,
        "C": 1
    }

    assert revermapping(tickets) == expected