import unittest

from src.uwo_ps_app import towns_table

class TestTownsTable(unittest.TestCase):
    """
    Tests for towns_table module
    """
    def test_emtpy(self):
        self.assertIsNone(towns_table.get_current_town([]))

    def test_not_founded(self):
        self.assertIsNone(towns_table.get_current_town(['Mars']))

    def test_seville(self):
        nearbys = ['Malaga', 'Faro', 'Valencia', 'Palma']
        self.assertEquals('Seville', towns_table.get_current_town(nearbys))

    def test_london(self):
        nearbys1 = ['Dover', 'Plymouth', 'Edinburgh', 'Dublin', 'Portsmouth']
        self.assertEquals('London', towns_table.get_current_town(nearbys1))

        nearbys2 = ['Plymouth', 'Edinburgh', 'Dublin', 'Portsmouth', 'Manchester']
        self.assertEquals('London', towns_table.get_current_town(nearbys2))
