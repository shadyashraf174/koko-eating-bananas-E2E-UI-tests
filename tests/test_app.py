import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import minEatingSpeed


def test_minEatingSpeed():
    piles = [3, 6, 7, 11]
    h = 8
    assert minEatingSpeed(piles, h) == 4

    piles = [30, 11, 23, 4, 20]
    h = 5
    assert minEatingSpeed(piles, h) == 30

    piles = [30, 11, 23, 4, 20]
    h = 6
    assert minEatingSpeed(piles, h) == 23
