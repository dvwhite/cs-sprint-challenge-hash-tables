class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Reconstruct a trip itinerary using hash tables
    """
    # Create a dictionary to hold each ticket source mapped to its destination
    destinations = {}
    for ticket in tickets:
        destinations[ticket.source] = ticket.destination

    # Skip the first source destination of "NONE"
    next_stop = destinations["NONE"]
    route = []
    # Use a while loop, and starting with that first source location,
    # keep looping until the destination is equal to "NONE"
    # On each loop, find the next destination by looking it up in the dict
    for idx in range(len(tickets)):
        route.append(next_stop)
        next_stop = destinations[next_stop]

    # Return the itinerary
    return route


# Manual testing
ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

# expected = ["PDX", "DCA", "NONE"]
result = reconstruct_trip(tickets, 3)
print(result)
