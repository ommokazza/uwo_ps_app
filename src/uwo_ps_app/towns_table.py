"""A Utility module to get current town from nearby towns.
"""

TOWNS_TABLE = {}
TOWNS_TABLE[("Malaga", "Faro", "Valencia", "Palma")] = "Seville"
TOWNS_TABLE[("Valencia", "Malaga", "Barcelona")] = "Palma"
TOWNS_TABLE[("Dover", "Plymouth", "Edinburgh", "Dublin", "Portsmouth", "Manchester")] = "London"
#TODO: Add table data

def get_current_town(nearby_towns):
    """Get town from nearby towns

    Arguments:
        nearby_towns (list): list of towns

    Return:
        town name (str)
        None if failed to search
    """
    for towns in TOWNS_TABLE.keys():
        for li in __make_listlist(towns):
            if li == nearby_towns:
                return TOWNS_TABLE.get(towns)

    return None

def __make_listlist(towns):
    """Split list of towns list.

    The nearby towns of a town can be over 5.
    But up to 5 towns can be displayed at once.
    """
    towns_list = list(towns)
    if len(towns) <= 5:
        return [towns_list]
    else:
        lists = []
        for i in range(len(towns)-5+1):
            lists += [towns_list[i:i+5]]
        return lists
