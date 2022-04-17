from collections import defaultdict

def get_itinerary(flights, start):
    # Store all the flights into a dictionary key:origin -> val:list of destinations
    flight_map = defaultdict(list)
    for origin, destination in flights:
        flight_map[origin] += [destination]

    def visit(flight_map, total_flights, current_itinerary):
        # If our itinerary uses up all the flights, we're done here.
        if len(current_itinerary) == total_flights + 1:
            return [current_itinerary[:]]

        last_stop = current_itinerary[-1]
        # If we haven't used all the flights yet but we have no way of getting out of this airport, then we're stuck. Backtrack out.
        if not flight_map[last_stop]:
            return []

        # Otherwise, let's try all the options out of the current stop recursively. We temporarily take them out of the mapping once we use them.
        potential_itineraries = []
        for i, flight in enumerate(flight_map[last_stop]):
            flight_map[last_stop].pop(i)
            current_itinerary.append(flight)
            potential_itineraries.extend(visit(flight_map, total_flights, current_itinerary))
            flight_map[last_stop].insert(i, flight)
            current_itinerary.pop()
        return potential_itineraries

    valid_itineraries = visit(flight_map, len(flights), [start])
    if valid_itineraries:
        return sorted(valid_itineraries)[0]