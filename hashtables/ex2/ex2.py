class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    Reconstruct a trip itinerary using hash tables
    """
    # Create a dictionary to hold each ticket source mapped to its destination
    # Skip the first source destination of "NONE"
    # Use a while loop, and starting with that first source location,
    # keep looping until the destination is equal to "NONE"
    # On each loop, find the next destination by looking it up in the dict
    # Return the itinerary

    return route
