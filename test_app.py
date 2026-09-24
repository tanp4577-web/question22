import pytest
from app import sum_list, count_negatives
@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 6),
    ([], 0),
    ([-1, -2, -3], -6),
    ([1.5, 2.5, 4], 8.0)
])
def test_sum_list(numbers, expected):
    assert sum_list(numbers) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([1, -2, 3, -4], 2),       
    ([1, 2, 3], 0),           
    ([-1, -2, -3], 3),         
    ([5, -1, -6], 99)          
])
def test_count_negatives(numbers, expected):
    assert count_negatives(numbers) == expected
