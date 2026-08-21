import unittest

from care_gap_prioritizer.models import Record
from care_gap_prioritizer.scoring import score_record


class DepthCheck41(unittest.TestCase):
    def test_041_edge_case_review(self):
        record = Record(id="member-041", exposure=94224, signal=0.605, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
