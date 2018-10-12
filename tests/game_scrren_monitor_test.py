import unittest

from src.uwo_ps_app.game_screen_monitor import GameScreenMonitor


class GameScreenMonitorTest(unittest.TestCase):
    def test_interval(self):
        gsm = GameScreenMonitor("unittest")
        interval = gsm.get_interval()
        gsm.increase_interval()
        self.assertAlmostEqual(interval + 0.5, gsm.get_interval(), delta=0.01)
        gsm.decrease_interval()
        self.assertAlmostEqual(interval, gsm.get_interval(), delta=0.01)

        self.assertAlmostEqual(5.0, gsm.set_interval(5.0), delta=0.01)
