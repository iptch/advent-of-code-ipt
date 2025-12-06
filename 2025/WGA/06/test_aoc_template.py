# test_aoc_template.py

import pathlib
import pytest
import aoc_template as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text()
    return aoc.parse(puzzle_input)

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 4277556

@pytest.mark.skip(reason="Not implemented")
def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part1(example2) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc.part1(example3) == ...

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 3263827

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc.part2(example3) == ...