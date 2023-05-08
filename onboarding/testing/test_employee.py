import pytest as pytest

from testing.employee import Employee


@pytest.fixture
def employee():
    """Create Employee"""
    employee = Employee('pesho', 'peshov', 65_000)
    return employee


def test_give_default_raise():
    """Test that default salary work correctly"""
    employee.give_raise()
    assert employee.annual_salary == 70_000


def test_give_custom_raise():
    """Test that custom salary work correctly"""
    employee.give_raise(1000)
    assert employee.annual_salary == 75_000
