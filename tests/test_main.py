import pytest
from main import sort_by_area, sort_by_population


@pytest.fixture()
def sample_data():
    return [
        ['USA', '1000', '500'],
        ['China', '2000', '1000'],
        ['Russia', '1500', '750'],
        ['India', '1200', '800']
    ]


def test_sort_by_area(sample_data):
    expected_sorted_data = [
        ['USA', '1000', '500'],
        ['India', '1200', '800'],
        ['Russia', '1500', '750'],
        ['China', '2000', '1000']
    ]
    assert sort_by_area(sample_data) == expected_sorted_data


def test_sort_by_population(sample_data):
    expected_sorted_data = [
        ['USA', '1000', '500'],
        ['Russia', '1500', '750'],
        ['India', '1200', '800'],
        ['China', '2000', '1000']
    ]
    assert sort_by_population(sample_data) == expected_sorted_data
