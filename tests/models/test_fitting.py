"""
Tests for src/hydraulic_analysis_suite/models/fitting.py

Verifies Fitting class construction, input validation,
and string representations.
"""

import pytest
from hydraulic_analysis_suite.models.fitting import Fitting


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def standard_fitting():
    """Standard fitting for reuse across tests."""
    return Fitting(
        diameter_in=8.0,
        quantity=3,
        fitting_material="DIP",
    )


# =============================================================================
# Construction — Valid Inputs
# =============================================================================

class TestConstruction:

    def test_valid_construction(self, standard_fitting):
        assert standard_fitting is not None

    def test_stores_diameter(self, standard_fitting):
        assert standard_fitting.diameter_in == 8.0

    def test_stores_quantity(self, standard_fitting):
        assert standard_fitting.quantity == 3

    def test_stores_fitting_material(self, standard_fitting):
        assert standard_fitting.fitting_material == "DIP"

    def test_quantity_of_one(self):
        f = Fitting(diameter_in=6.0, quantity=1, fitting_material="PVC")
        assert f.quantity == 1

    def test_large_diameter(self):
        f = Fitting(diameter_in=36.0, quantity=2, fitting_material="Steel")
        assert f.diameter_in == 36.0

    def test_fractional_diameter(self):
        f = Fitting(diameter_in=4.5, quantity=1, fitting_material="HDPE")
        assert f.diameter_in == 4.5


# =============================================================================
# Construction — Input Validation
# =============================================================================

class TestInputValidation:

    def test_zero_diameter_raises(self):
        with pytest.raises(ValueError):
            Fitting(diameter_in=0.0, quantity=1, fitting_material="PVC")

    def test_negative_diameter_raises(self):
        with pytest.raises(ValueError):
            Fitting(diameter_in=-8.0, quantity=1, fitting_material="PVC")

    def test_zero_quantity_raises(self):
        with pytest.raises(ValueError):
            Fitting(diameter_in=8.0, quantity=0, fitting_material="PVC")

    def test_negative_quantity_raises(self):
        with pytest.raises(ValueError):
            Fitting(diameter_in=8.0, quantity=-1, fitting_material="PVC")


# =============================================================================
# String Representations
# =============================================================================

class TestStringRepresentations:

    def test_str_returns_string(self, standard_fitting):
        assert isinstance(str(standard_fitting), str)

    def test_str_contains_material(self, standard_fitting):
        assert "DIP" in str(standard_fitting)

    def test_str_contains_diameter(self, standard_fitting):
        assert "8" in str(standard_fitting)

    def test_str_contains_quantity(self, standard_fitting):
        assert "3" in str(standard_fitting)

    def test_repr_returns_string(self, standard_fitting):
        assert isinstance(repr(standard_fitting), str)

    def test_repr_contains_diameter(self, standard_fitting):
        assert "8" in repr(standard_fitting)

    def test_repr_contains_quantity(self, standard_fitting):
        assert "3" in repr(standard_fitting)

    def test_repr_contains_material(self, standard_fitting):
        assert "DIP" in repr(standard_fitting)
