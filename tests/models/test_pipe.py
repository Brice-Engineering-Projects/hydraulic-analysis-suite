"""
Tests for src/hydraulic_analysis_suite/models/pipe.py

Verifies Pipe class construction, input validation, database lookup,
derived properties, and string representations.
"""

import math
import pytest
from hydraulic_analysis_suite.models.pipe import Pipe


# =============================================================================
# Fixtures
# =============================================================================

@pytest.fixture
def pvc_pipe():
    """Standard PVC pipe for reuse across tests."""
    return Pipe(
        flow_rate_gpm=500.0,
        diameter_in=8.0,
        length_ft=1000.0,
        pipe_material="pvc",
    )

@pytest.fixture
def dip_pipe():
    """Ductile iron pipe (good condition)."""
    return Pipe(
        flow_rate_gpm=250.0,
        diameter_in=6.0,
        length_ft=500.0,
        pipe_material="dip_good",
    )


# =============================================================================
# Construction — Valid Inputs
# =============================================================================

class TestConstruction:

    def test_valid_construction(self, pvc_pipe):
        assert pvc_pipe is not None

    def test_stores_flow_rate(self, pvc_pipe):
        assert pvc_pipe.flow_rate_gpm == 500.0

    def test_stores_diameter(self, pvc_pipe):
        assert pvc_pipe.diameter_in == 8.0

    def test_stores_length(self, pvc_pipe):
        assert pvc_pipe.length_ft == 1000.0

    def test_stores_pipe_material(self, pvc_pipe):
        assert pvc_pipe.pipe_material == "pvc"

    def test_material_lookup_sets_c_factor(self, pvc_pipe):
        assert pvc_pipe.c_factor == 150

    def test_material_lookup_sets_roughness(self, pvc_pipe):
        assert pvc_pipe.roughness_ft == 0.000005

    def test_material_lookup_sets_manning_n(self, pvc_pipe):
        assert pvc_pipe.manning_n == 0.009

    def test_material_lookup_sets_material_name(self, pvc_pipe):
        assert isinstance(pvc_pipe.material_name, str)
        assert pvc_pipe.material_name

    def test_material_lookup_sets_application(self, pvc_pipe):
        assert pvc_pipe.application == "both"

    def test_material_lookup_sets_category(self, pvc_pipe):
        assert pvc_pipe.category == "plastic"

    def test_dip_pipe_construction(self, dip_pipe):
        assert dip_pipe.c_factor == 130


# =============================================================================
# Construction — Input Validation
# =============================================================================

class TestInputValidation:

    def test_zero_diameter_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=100.0, diameter_in=0.0, length_ft=100.0, pipe_material="pvc")

    def test_negative_diameter_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=100.0, diameter_in=-6.0, length_ft=100.0, pipe_material="pvc")

    def test_zero_flow_rate_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=0.0, diameter_in=6.0, length_ft=100.0, pipe_material="pvc")

    def test_negative_flow_rate_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=-100.0, diameter_in=6.0, length_ft=100.0, pipe_material="pvc")

    def test_zero_length_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=100.0, diameter_in=6.0, length_ft=0.0, pipe_material="pvc")

    def test_negative_length_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=100.0, diameter_in=6.0, length_ft=-500.0, pipe_material="pvc")

    def test_unknown_material_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=100.0, diameter_in=6.0, length_ft=100.0, pipe_material="unobtanium")

    def test_empty_material_raises(self):
        with pytest.raises(ValueError):
            Pipe(flow_rate_gpm=100.0, diameter_in=6.0, length_ft=100.0, pipe_material="")


# =============================================================================
# Derived Properties
# =============================================================================

class TestDerivedProperties:

    def test_diameter_ft(self, pvc_pipe):
        assert pvc_pipe.diameter_ft == pytest.approx(8.0 / 12.0)

    def test_radius_in(self, pvc_pipe):
        assert pvc_pipe.radius_in == pytest.approx(4.0)

    def test_length_miles(self, pvc_pipe):
        assert pvc_pipe.length_miles == pytest.approx(1000.0 / 5280.0)

    def test_flow_rate_cfs(self, pvc_pipe):
        assert pvc_pipe.flow_rate_cfs == pytest.approx(500.0 * 0.002228)

    def test_area_sf(self, pvc_pipe):
        d_ft = 8.0 / 12.0
        expected = math.pi * d_ft ** 2 / 4
        assert pvc_pipe.area_sf == pytest.approx(expected)

    def test_volume_cf(self, pvc_pipe):
        d_ft = 8.0 / 12.0
        expected = math.pi * 1000.0 * d_ft ** 2 / 4
        assert pvc_pipe.volume_cf == pytest.approx(expected)

    def test_velocity_fps_is_positive(self, pvc_pipe):
        assert pvc_pipe.velocity_fps > 0

    def test_velocity_fps_calculation(self, pvc_pipe):
        expected = pvc_pipe.flow_rate_cfs / pvc_pipe.area_sf
        assert pvc_pipe.velocity_fps == pytest.approx(expected)


# =============================================================================
# String Representations
# =============================================================================

class TestStringRepresentations:

    def test_str_returns_string(self, pvc_pipe):
        assert isinstance(str(pvc_pipe), str)

    def test_str_contains_material(self, pvc_pipe):
        assert "pvc" in str(pvc_pipe).lower()

    def test_str_contains_diameter(self, pvc_pipe):
        assert "8" in str(pvc_pipe)

    def test_repr_returns_string(self, pvc_pipe):
        assert isinstance(repr(pvc_pipe), str)

    def test_repr_contains_flow_rate(self, pvc_pipe):
        assert "500" in repr(pvc_pipe)

    def test_repr_contains_diameter(self, pvc_pipe):
        assert "8" in repr(pvc_pipe)
