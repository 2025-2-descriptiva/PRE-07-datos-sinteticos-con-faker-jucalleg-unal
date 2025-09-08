"""Autograding script"""

import os


def test_01():
    """Test app"""

    assert os.path.exists("files/drivers.csv")
    assert os.path.exists("files/timesheet.csv")
