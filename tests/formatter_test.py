import unittest

from src.uwo_ps_app.formatter import BaseFormatter, FoxyFormatter


class FormatterTest(unittest.TestCase):
    def test_base(self):
        with self.assertRaises(NotImplementedError):
            BaseFormatter().apply([])

    def test_is_valid(self):
        fm = BaseFormatter()
        none_name = (None, "100", "0")
        self.assertFalse(fm.is_valid(none_name))
        empty_name = ("", "100", "0")
        self.assertFalse(fm.is_valid(empty_name))
        unknown_name = ("UNKNOWN", "0", "0")
        self.assertFalse(fm.is_valid(unknown_name))
        normal_name = ("Seville", "100", "0")
        self.assertTrue(fm.is_valid(normal_name))

    def test_foxy_bad_params(self):
        fm = FoxyFormatter()
        self.assertEquals("", fm.apply([]))
        self.assertEquals("", fm.apply([("Mace", "180", "0")]))

    def test_foxy(self):
        fm = FoxyFormatter()
        params = [
            ("Mace", "56", "2"),
            ("Malaga", "180", "0"),
            ("Ceuta", "100", "1"),
            ("Faro", "100", "2")
        ]
        expect = '?price "Mace" : "Malaga" 180u; "Ceuta" 100n; "Faro" 100d;'
        self.assertEquals(expect, fm.apply(params))
