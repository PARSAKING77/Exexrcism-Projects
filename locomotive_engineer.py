"""Functions which help the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*wagons):
    """
    Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # Using the * operator to accept an arbitrary number of arguments
    # and convert them into a list
    return list(wagons)

# Example usage:
# Output: [1, 7, 12, 3, 14, 8, 5]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """
    Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    return   [each_wagons_id[each_wagons_id.index(1)]] + missing_wagons + each_wagons_id[each_wagons_id.index(1) + 1:] + each_wagons_id[:each_wagons_id.index(1)]



def add_missing_stops(route, **stops):
    """
    Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    stop_list = list(stops.values())
    route['stops'] = stop_list
    return route



def extend_route_information(route, more_route_information):
    """
    Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    route.update(more_route_information)
    return route


def fix_wagon_depot(wagons_rows):
    """
    Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    transposed_rows = list(zip(*wagons_rows))

    fixed_rows = [list(row) for row in transposed_rows]
    return fixed_rows

