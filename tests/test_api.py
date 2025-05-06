import unittest
from matchbot.api import fetch_matches

class TestMatchAPI(unittest.TestCase):

    def test_fetch_dota2_matches(self):
        matches = fetch_matches("dota2")
        self.assertIsInstance(matches, list)
        self.assertGreater(len(matches), 0)
        self.assertIn("team1", matches[0])
        self.assertIn("team2", matches[0])
        self.assertIn("time", matches[0])

    def test_fetch_csgo_matches(self):
        matches = fetch_matches("csgo")
        self.assertIsInstance(matches, list)
        self.assertGreaterEqual(len(matches), 1)

    def test_fetch_unknown_game(self):
        matches = fetch_matches("unknown")
        self.assertEqual(matches, [])

if __name__ == "__main__":
    unittest.main()
