def group_tickets(tickets):
    result = {}

    for category, ticket_id in tickets:
        if category not in result:
            result[category]=[]
        result[category].append(ticket_id)

    return result