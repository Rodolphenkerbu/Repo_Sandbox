from src.group_tickets import group_tickets

def test_group_tickets():
    tickets = [
        ("A", 1),
        ("B", 2),
        ("A", 3)
    ]

    expected = {
        "A": [1, 3],
        "B": [2]
    }

    assert group_tickets(tickets) == expected