"""
Tests for src/hydraulic_analysis_suite/utils/fitting_data_helper_calcs.py

Verifies the database verification function, turbulent friction factor
calculation, and K-factor derivation methodology.
"""

import math
import pytest
from hydraulic_analysis_suite.utils.fitting_data_helper_calcs import (
    calc_turbulent_friction_factor,
    F_T_REPRESENTATIVE,
    REPRESENTATIVE_DIAMETER_FT,
    CRANE_ROUGHNESS_FT,
    LE_D_45_STANDARD,
    LE_D_90_STANDARD,
    LE_D_45_LONG,
    LE_D_90_LONG,
    LE_D_22_5_STANDARD,
    LE_D_11_25_STANDARD,
    LE_D_22_5_LONG,
    LE_D_11_25_LONG,
    verify_database_values,
)


# =============================================================================
# Turbulent Friction Factor
# =============================================================================

class TestCalcTurbulentFrictionFactor:

    def test_returns_positive_value(self):
        f_t = calc_turbulent_friction_factor(1.0, 0.00015)
        assert f_t > 0

    def test_larger_pipe_gives_lower_friction_factor(self):
        """Friction factor decreases as pipe diameter increases."""
        f_small = calc_turbulent_friction_factor(0.5, 0.00015)
        f_large = calc_turbulent_friction_factor(2.0, 0.00015)
        assert f_small > f_large

    def test_rougher_pipe_gives_higher_friction_factor(self):
        """Friction factor increases with pipe roughness."""
        f_smooth = calc_turbulent_friction_factor(1.0, 0.000005)
        f_rough  = calc_turbulent_friction_factor(1.0, 0.005)
        assert f_rough > f_smooth

    def test_known_value_commercial_steel_12_inch(self):
        """
        For 12-inch commercial steel pipe:
            D = 1.0 ft, ε = 0.00015 ft
            relative roughness = 0.00015
            1/sqrt(f) = -2 * log10(0.00015 / 3.7)
        """
        f_t = calc_turbulent_friction_factor(1.0, 0.00015)
        relative_roughness = 0.00015 / 1.0
        expected = (1.0 / (-2.0 * math.log10(relative_roughness / 3.7))) ** 2
        assert f_t == pytest.approx(expected, rel=1e-6)

    def test_representative_f_t_matches_module_constant(self):
        computed = calc_turbulent_friction_factor(
            REPRESENTATIVE_DIAMETER_FT,
            CRANE_ROUGHNESS_FT
        )
        assert computed == pytest.approx(F_T_REPRESENTATIVE, rel=1e-6)

    def test_representative_diameter_is_8_inch(self):
        assert REPRESENTATIVE_DIAMETER_FT == pytest.approx(8.0 / 12.0)

    def test_crane_roughness_is_commercial_steel(self):
        assert CRANE_ROUGHNESS_FT == 0.00015


# =============================================================================
# Crane TP-410 Table A-29 Le/D Constants
# =============================================================================

class TestLeD_Constants:

    def test_45_deg_standard_le_d(self):
        """Crane TP-410 Table A-29: 45° standard elbow Le/D = 16."""
        assert LE_D_45_STANDARD == 16

    def test_90_deg_standard_le_d(self):
        """Crane TP-410 Table A-29: 90° standard elbow Le/D = 30."""
        assert LE_D_90_STANDARD == 30

    def test_45_deg_long_le_d(self):
        """Crane TP-410 Table A-29: 45° long radius elbow Le/D = 10."""
        assert LE_D_45_LONG == 10

    def test_90_deg_long_le_d(self):
        """Crane TP-410 Table A-29: 90° long radius elbow Le/D = 16."""
        assert LE_D_90_LONG == 16


# =============================================================================
# Interpolated Le/D Values
# =============================================================================

class TestInterpolatedLeD:

    def test_22_5_standard_interpolated(self):
        """22.5° Le/D is half of 45° tabulated value."""
        assert LE_D_22_5_STANDARD == round(LE_D_45_STANDARD * (22.5 / 45.0))

    def test_11_25_standard_interpolated(self):
        """11.25° Le/D is half of 22.5° interpolated value."""
        assert LE_D_11_25_STANDARD == round(LE_D_22_5_STANDARD * (11.25 / 22.5))

    def test_22_5_long_interpolated(self):
        """22.5° long Le/D is half of 45° long tabulated value."""
        assert LE_D_22_5_LONG == round(LE_D_45_LONG * (22.5 / 45.0))

    def test_11_25_long_interpolated(self):
        """11.25° long Le/D is half of 22.5° long interpolated value."""
        assert LE_D_11_25_LONG == round(LE_D_22_5_LONG * (11.25 / 22.5))

    def test_standard_radius_le_d_ordering(self):
        """Le/D increases with bend angle for standard radius."""
        assert LE_D_11_25_STANDARD < LE_D_22_5_STANDARD < LE_D_45_STANDARD < LE_D_90_STANDARD

    def test_long_radius_le_d_ordering(self):
        """Le/D increases with bend angle for long radius."""
        assert LE_D_11_25_LONG < LE_D_22_5_LONG < LE_D_45_LONG < LE_D_90_LONG

    def test_standard_le_d_greater_than_long_at_same_angle(self):
        """Standard radius always has higher Le/D than long radius at same angle."""
        assert LE_D_45_STANDARD > LE_D_45_LONG
        assert LE_D_90_STANDARD > LE_D_90_LONG


# =============================================================================
# Database Verification
# =============================================================================

class TestVerifyDatabaseValues:

    def test_all_checks_pass(self, capsys):
        result = verify_database_values()
        assert result is True

    def test_returns_bool(self):
        result = verify_database_values()
        assert isinstance(result, bool)

    def test_output_contains_pass(self, capsys):
        verify_database_values()
        output = capsys.readouterr().out
        assert "PASS" in output

    def test_output_contains_fail_count_zero(self, capsys):
        verify_database_values()
        output = capsys.readouterr().out
        assert "0 failed" in output

    def test_13_fittings_checked(self, capsys):
        verify_database_values()
        output = capsys.readouterr().out
        assert "13 fittings checked" in output
