import unittest

from care_gap_prioritizer.models import Record
from care_gap_prioritizer.scoring import score_record


class DepthCheck32(unittest.TestCase):
    def test_032_operator_handoff(self):
        record = Record(id="member-032", exposure=82033, signal=0.579, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
