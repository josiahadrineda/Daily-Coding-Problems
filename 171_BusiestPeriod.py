def busiest_period(entries):
    """Given a list of ENTRIES in the format
    {"timestamp": <timestamp>, "count": <count>, "type": <type>},
    where "count" = number of people and "type" = "enter" or "exit"
    (some building), determines the time period with the most people
    inside of the building.
    
    *The building always starts and ends with 0 people.*

    >>> entries = [
    ...     {"timestamp": 1526579928, "count": 3, "type": "enter"},
    ...     {"timestamp": 1526579982, "count": 4, "type": "enter"},
    ...     {"timestamp": 1526580054, "count": 5, "type": "exit"},
    ...     {"timestamp": 1526580128, "count": 1, "type": "enter"},
    ...     {"timestamp": 1526580382, "count": 3, "type": "exit"}
    ... ]
    >>> busiest_period(entries)
    (1526579982, 1526580054)
    """
    assert entries, 'ENTRIES must have entries in it.'
    
    busiest_time_s, timestamps = 0, []
    curr_people, max_people = 0, 0
    for entry in entries:
        timestamp, count, type = entry.values()
        timestamps.append(timestamp)
        if type == 'enter':
            curr_people += count
        else:
            curr_people -= count

        if curr_people > max_people:
            busiest_time_s, max_people = timestamp, curr_people
    
    busiest_time_e = timestamps[timestamps.index(busiest_time_s) + 1]
    
    return (busiest_time_s, busiest_time_e)