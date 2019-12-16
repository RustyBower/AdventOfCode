#!/usr/bin/env python
import part1


def test_calculate_fuel():
    assert part1.calculate_fuel(12) == 2
    assert part1.calculate_fuel(14) == 2
    assert part1.calculate_fuel(1969) == 654
    assert part1.calculate_fuel(100756) == 33583
