"""
Tests for src/hydraulic_analysis_suite/data/pipe_materials.py

Verifies database structure, required fields, value types,
and engineering plausibility of all pipe material entries.
"""

import pytest
from hydraulic_analysis_suite.data.pipe_materials import PIPE_MATERIALS

REQUIRED_KEYS = {
    "material_name",
    "application",
    "category",
    "c_factor",
    "roughness_ft",
    "manning_n",
}

VALID_APPLICATIONS = {"gravity", "pressure", "both"}


# =============================================================================
# Database Structure
# =============================================================================

class TestDatabaseStructure:

    def test_database_is_not_empty(self):
        assert len(PIPE_MATERIALS) > 0

    def test_all_entries_have_required_keys(self):
        for key, data in PIPE_MATERIALS.items():
            missing = REQUIRED_KEYS - data.keys()
            assert not missing, (
                f"Entry '{key}' is missing required keys: {missing}"
            )

    def test_no_duplicate_keys(self):
        keys = list(PIPE_MATERIALS.keys())
        assert len(keys) == len(set(keys))


# =============================================================================
# Field Types
# =============================================================================

class TestFieldTypes:

    def test_material_name_is_string(self):
        for key, data in PIPE_MATERIALS.items():
            assert isinstance(data["material_name"], str), (
                f"'{key}': material_name must be str"
            )

    def test_application_is_string(self):
        for key, data in PIPE_MATERIALS.items():
            assert isinstance(data["application"], str), (
                f"'{key}': application must be str"
            )

    def test_category_is_string(self):
        for key, data in PIPE_MATERIALS.items():
            assert isinstance(data["category"], str), (
                f"'{key}': category must be str"
            )

    def test_c_factor_is_numeric(self):
        for key, data in PIPE_MATERIALS.items():
            assert isinstance(data["c_factor"], (int, float)), (
                f"'{key}': c_factor must be numeric"
            )

    def test_roughness_ft_is_float(self):
        for key, data in PIPE_MATERIALS.items():
            assert isinstance(data["roughness_ft"], float), (
                f"'{key}': roughness_ft must be float"
            )

    def test_manning_n_is_float(self):
        for key, data in PIPE_MATERIALS.items():
            assert isinstance(data["manning_n"], float), (
                f"'{key}': manning_n must be float"
            )


# =============================================================================
# Field Values — Engineering Plausibility
# =============================================================================

class TestFieldValues:

    def test_application_is_valid(self):
        for key, data in PIPE_MATERIALS.items():
            assert data["application"] in VALID_APPLICATIONS, (
                f"'{key}': application '{data['application']}' is not valid. "
                f"Must be one of {VALID_APPLICATIONS}"
            )

    def test_material_name_is_not_empty(self):
        for key, data in PIPE_MATERIALS.items():
            assert data["material_name"].strip(), (
                f"'{key}': material_name must not be empty"
            )

    def test_c_factor_in_engineering_range(self):
        """Hazen-Williams C-factors for water pipe typically range 60–160."""
        for key, data in PIPE_MATERIALS.items():
            c = data["c_factor"]
            assert 50 <= c <= 165, (
                f"'{key}': c_factor {c} is outside expected range 50–165"
            )

    def test_roughness_ft_is_positive(self):
        for key, data in PIPE_MATERIALS.items():
            assert data["roughness_ft"] > 0, (
                f"'{key}': roughness_ft must be greater than zero"
            )

    def test_roughness_ft_in_engineering_range(self):
        """Absolute roughness for pipe materials typically < 0.05 ft."""
        for key, data in PIPE_MATERIALS.items():
            assert data["roughness_ft"] < 0.05, (
                f"'{key}': roughness_ft {data['roughness_ft']} exceeds expected maximum"
            )

    def test_manning_n_is_positive(self):
        for key, data in PIPE_MATERIALS.items():
            assert data["manning_n"] > 0, (
                f"'{key}': manning_n must be greater than zero"
            )

    def test_manning_n_in_engineering_range(self):
        """Manning's n for pipe materials typically ranges 0.008–0.035."""
        for key, data in PIPE_MATERIALS.items():
            n = data["manning_n"]
            assert 0.007 <= n <= 0.040, (
                f"'{key}': manning_n {n} is outside expected range 0.007–0.040"
            )


# =============================================================================
# Spot-Check Known Entries
# =============================================================================

class TestKnownEntries:

    def test_pvc_exists(self):
        assert "pvc" in PIPE_MATERIALS

    def test_pvc_c_factor(self):
        assert PIPE_MATERIALS["pvc"]["c_factor"] == 150

    def test_pvc_application(self):
        assert PIPE_MATERIALS["pvc"]["application"] == "both"

    def test_hdpe_exists(self):
        assert "hdpe" in PIPE_MATERIALS

    def test_dip_good_exists(self):
        assert "dip_good" in PIPE_MATERIALS

    def test_dip_good_c_factor(self):
        assert PIPE_MATERIALS["dip_good"]["c_factor"] == 130

    def test_steel_exists(self):
        assert "steel" in PIPE_MATERIALS

    def test_gate_valve_condition_ordering(self):
        """DIP condition grades should have decreasing C-factors."""
        assert (
            PIPE_MATERIALS["dip_excellent"]["c_factor"]
            > PIPE_MATERIALS["dip_good"]["c_factor"]
            > PIPE_MATERIALS["dip_fair"]["c_factor"]
            > PIPE_MATERIALS["dip_poor"]["c_factor"]
        )
