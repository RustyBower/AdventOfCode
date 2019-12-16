#!/usr/bin/env python
import part2


def test_calculate_fuel():
    assert part2.calculate_fuel(14) == 2
    assert part2.calculate_fuel(1969) == 966
    assert part2.calculate_fuel(100756) == 50346
