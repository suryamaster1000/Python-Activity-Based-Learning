import pytest

from food_waste_monitoring import calculate_wastage


@pytest.mark.parametrize(
    ("prepared", "served", "expected_leftover", "expected_wastage"),
    [
        (100, 95, 5, 5.0),       # Normal waste
        (100, 85, 15, 15.0),     # High waste
        (200, 180, 20, 10.0),    # Exactly at the limit
        (50, 50, 0, 0.0),        # No waste
        (1, 0, 1, 100.0),        # All meals left over
    ],
)
def test_calculate_wastage_valid_inputs(
    prepared, served, expected_leftover, expected_wastage
):
    leftover, wastage = calculate_wastage(prepared, served)

    assert leftover == expected_leftover
    assert wastage == pytest.approx(expected_wastage)


@pytest.mark.parametrize(
    ("prepared", "served"),
    [
        (0, 0),       # No meals prepared
        (-5, 0),      # Negative prepared count
        (100, -1),    # Negative served count
        (100, 120),   # More meals served than prepared
    ],
)
def test_calculate_wastage_rejects_invalid_inputs(prepared, served):
    with pytest.raises(ValueError):
        calculate_wastage(prepared, served)
