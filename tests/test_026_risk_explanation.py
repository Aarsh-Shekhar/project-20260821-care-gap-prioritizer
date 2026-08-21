import unittest

from care_gap_prioritizer.models import Record
from care_gap_prioritizer.scoring import score_record


class DepthCheck26(unittest.TestCase):
    def test_026_risk_explanation(self):
        record = Record(id="member-026", exposure=62132, signal=0.659, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
