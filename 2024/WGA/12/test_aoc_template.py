# test_aoc_template.py

import pathlib
import pytest
import aoc_template as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example4():
    puzzle_input = (PUZZLE_DIR / "example4.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example5():
    puzzle_input = (PUZZLE_DIR / "example5.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 140

def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part1(example2) == 772

def test_part1_example3(example3):
    """Test part 1 on example input."""
    assert aoc.part1(example3) == 1930

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 80

def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 436

def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc.part2(example3) == 1206

def test_part2_example4(example4):
    """Test part 2 on example input."""
    assert aoc.part2(example4) == 236

def test_part2_example5(example5):
    """Test part 2 on example input."""
    assert aoc.part2(example5) == 368