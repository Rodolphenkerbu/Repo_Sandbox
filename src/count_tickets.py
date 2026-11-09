def revermapping(tickets:dict[str,str]) -> dict[str,int]:
    results={}
    for key, value in tickets.items():
        if value not in results:
            results[value]=0
        results[value] += 1
        #results[value] = results.get(value, 0) + 1
    return results