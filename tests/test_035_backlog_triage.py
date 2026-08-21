import unittest

from care_gap_prioritizer.models import Record
from care_gap_prioritizer.scoring import score_record


class DepthCheck35(unittest.TestCase):
    def test_035_backlog_triage(self):
        record = Record(id="member-035", exposure=62220, signal=0.737, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
