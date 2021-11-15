def flights(*args):
    flights_report = {}
    args = list(args)
    for x in range(0, len(args), 2):
        if args[x] == 'Finish':
            break
        if isinstance(args[x], str):
            if args[x] not in flights_report:
                flights_report[args[x]] = 0
        flights_report[args[x]] += args[x + 1]
    return flights_report


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))