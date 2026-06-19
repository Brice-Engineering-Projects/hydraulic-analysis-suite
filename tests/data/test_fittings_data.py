"""
Tests for src/hydraulic_analysis_suite/data/fittings_data.py

Verifies database structure, required fields, value types,
engineering plausibility, and coverage of all MVP fitting categories.
"""

import pytest
from hydraulic_analysis_suite.data.fittings_data import FITTINGS_DATA

REQUIRED_KEYS = {
    "fitting_name",
    "fitting_category",
    "k_factor",
    "equivalent_length_ratio",
    "source",
    "source_reference",
    "engineering_notes",
}

VALID_CATEGORIES = {"bend", "tee", "wye", "reducer", "expansion", "valve", "meter"}

MVP_REQUIRED_ENTRIES = [
    "90_deg_bend_standard_radius",
    "45_deg_bend_standard_radius",
    "22_5_deg_bend_standard_radius",
    "11_25_deg_bend_standard_radius",
    "90_deg_bend_long_radius",
    "45_deg_bend_long_radius",
    "22_5_deg_bend_long_radius",
    "11_25_deg_bend_long_radius",
    "tee_through_run",
    "tee_branch",
    "tee_combining",
    "wye_standard",
    "wye_combination",
    "concentric_reducer",
    "eccentric_reducer",
    "concentric_expansion",
    "eccentric_expansion",
    "gate_valve_open",
    "butterfly_valve_open",
    "plug_valve_open",
    "swing_check_valve",
    "ball_check_valve",
    "venturi_meter",
    "magnetic_flow_meter",
    "turbine_meter",
]


# =============================================================================
# Database Structure
# =============================================================================

class TestDatabaseStructure:

    def test_database_is_not_empty(self):
        assert len(FITTINGS_DATA) > 0

    def test_all_entries_have_required_keys(self):
        for key, data in FITTINGS_DATA.items():
            missing = REQUIRED_KEYS - data.keys()
            assert not missing, (
                f"Entry '{key}' is missing required keys: {missing}"
            )

    def test_no_duplicate_keys(self):
        keys = list(FITTINGS_DATA.keys())
        assert len(keys) == len(set(keys))

    @pytest.mark.parametrize("entry_key", MVP_REQUIRED_ENTRIES)
    def test_mvp_entry_present(self, entry_key):
        assert entry_key in FITTINGS_DATA, (
            f"MVP fitting '{entry_key}' is missing from FITTINGS_DATA"
        )


# =============================================================================
# Field Types
# =============================================================================

class TestFieldTypes:

    def test_fitting_name_is_string(self):
        for key, data in FITTINGS_DATA.items():
            assert isinstance(data["fitting_name"], str), (
                f"'{key}': fitting_name must be str"
            )

    def test_fitting_category_is_string(self):
        for key, data in FITTINGS_DATA.items():
            assert isinstance(data["fitting_category"], str), (
                f"'{key}': fitting_category must be str"
            )

    def test_k_factor_is_numeric(self):
        for key, data in FITTINGS_DATA.items():
            assert isinstance(data["k_factor"], (int, float)), (
                f"'{key}': k_factor must be numeric"
            )

    def test_equivalent_length_ratio_is_numeric(self):
        for key, data in FITTINGS_DATA.items():
            assert isinstance(data["equivalent_length_ratio"], (int, float)), (
                f"'{key}': equivalent_length_ratio must be numeric"
            )

    def test_source_is_string(self):
        for key, data in FITTINGS_DATA.items():
            assert isinstance(data["source"], str), (
                f"'{key}': source must be str"
            )

    def test_source_reference_is_string(self):
        for key, data in FITTINGS_DATA.items():
            assert isinstance(data["source_reference"], str), (
                f"'{key}': source_reference must be str"
            )

    def test_engineering_notes_is_string(self):
        for key, data in FITTINGS_DATA.items():
            assert isinstance(data["engineering_notes"], str), (
                f"'{key}': engineering_notes must be str"
            )


# =============================================================================
# Field Values — Engineering Plausibility
# =============================================================================

class TestFieldValues:

    def test_fitting_category_is_valid(self):
        for key, data in FITTINGS_DATA.items():
            assert data["fitting_category"] in VALID_CATEGORIES, (
                f"'{key}': category '{data['fitting_category']}' is not valid. "
                f"Must be one of {VALID_CATEGORIES}"
            )

    def test_k_factor_is_positive(self):
        for key, data in FITTINGS_DATA.items():
            assert data["k_factor"] > 0, (
                f"'{key}': k_factor must be greater than zero"
            )

    def test_equivalent_length_ratio_is_positive(self):
        for key, data in FITTINGS_DATA.items():
            assert data["equivalent_length_ratio"] > 0, (
                f"'{key}': equivalent_length_ratio must be greater than zero"
            )

    def test_fitting_name_is_not_empty(self):
        for key, data in FITTINGS_DATA.items():
            assert data["fitting_name"].strip(), (
                f"'{key}': fitting_name must not be empty"
            )

    def test_source_is_not_empty(self):
        for key, data in FITTINGS_DATA.items():
            assert data["source"].strip(), (
                f"'{key}': source must not be empty"
            )

    def test_engineering_notes_is_not_empty(self):
        for key, data in FITTINGS_DATA.items():
            assert data["engineering_notes"].strip(), (
                f"'{key}': engineering_notes must not be empty"
            )


# =============================================================================
# Category Coverage
# =============================================================================

class TestCategoryCoverage:

    def _entries_for_category(self, category):
        return [k for k, v in FITTINGS_DATA.items() if v["fitting_category"] == category]

    def test_bend_category_has_entries(self):
        assert len(self._entries_for_category("bend")) >= 8

    def test_tee_category_has_entries(self):
        assert len(self._entries_for_category("tee")) >= 2

    def test_wye_category_has_entries(self):
        assert len(self._entries_for_category("wye")) >= 1

    def test_reducer_category_has_entries(self):
        assert len(self._entries_for_category("reducer")) >= 2

    def test_expansion_category_has_entries(self):
        assert len(self._entries_for_category("expansion")) >= 2

    def test_valve_category_has_entries(self):
        assert len(self._entries_for_category("valve")) >= 4

    def test_meter_category_has_entries(self):
        assert len(self._entries_for_category("meter")) >= 2


# =============================================================================
# Spot-Check Known Values (Crane TP-410 Table A-29)
# =============================================================================

class TestKnownValues:

    def test_90_deg_standard_le_d(self):
        """Crane TP-410 Table A-29: 90° standard elbow Le/D = 30."""
        assert FITTINGS_DATA["90_deg_bend_standard_radius"]["equivalent_length_ratio"] == 30

    def test_45_deg_standard_le_d(self):
        """Crane TP-410 Table A-29: 45° standard elbow Le/D = 16."""
        assert FITTINGS_DATA["45_deg_bend_standard_radius"]["equivalent_length_ratio"] == 16

    def test_90_deg_long_le_d(self):
        """Crane TP-410 Table A-29: 90° long radius elbow Le/D = 16."""
        assert FITTINGS_DATA["90_deg_bend_long_radius"]["equivalent_length_ratio"] == 16

    def test_45_deg_long_le_d(self):
        """Crane TP-410 Table A-29: 45° long radius elbow Le/D = 10."""
        assert FITTINGS_DATA["45_deg_bend_long_radius"]["equivalent_length_ratio"] == 10

    def test_gate_valve_le_d(self):
        """Crane TP-410 Table A-29: gate valve fully open Le/D = 8."""
        assert FITTINGS_DATA["gate_valve_open"]["equivalent_length_ratio"] == 8

    def test_swing_check_le_d(self):
        """Crane TP-410 Table A-29: swing check valve Le/D = 135."""
        assert FITTINGS_DATA["swing_check_valve"]["equivalent_length_ratio"] == 135

    def test_tee_through_run_le_d(self):
        """Crane TP-410 Table A-29: tee through run Le/D = 20."""
        assert FITTINGS_DATA["tee_through_run"]["equivalent_length_ratio"] == 20

    def test_tee_branch_le_d(self):
        """Crane TP-410 Table A-29: tee branch flow Le/D = 60."""
        assert FITTINGS_DATA["tee_branch"]["equivalent_length_ratio"] == 60

    def test_long_radius_has_lower_k_than_standard_90_deg(self):
        """Long radius bends have lower loss than standard radius at same angle."""
        k_standard = FITTINGS_DATA["90_deg_bend_standard_radius"]["k_factor"]
        k_long     = FITTINGS_DATA["90_deg_bend_long_radius"]["k_factor"]
        assert k_long < k_standard

    def test_90_deg_has_higher_k_than_45_deg_standard(self):
        """90-degree bend has higher loss than 45-degree at same radius."""
        k_90 = FITTINGS_DATA["90_deg_bend_standard_radius"]["k_factor"]
        k_45 = FITTINGS_DATA["45_deg_bend_standard_radius"]["k_factor"]
        assert k_90 > k_45

    def test_check_valves_higher_k_than_gate_valve(self):
        """Check valves have higher resistance than a fully open gate valve."""
        k_gate  = FITTINGS_DATA["gate_valve_open"]["k_factor"]
        k_swing = FITTINGS_DATA["swing_check_valve"]["k_factor"]
        k_ball  = FITTINGS_DATA["ball_check_valve"]["k_factor"]
        assert k_swing > k_gate
        assert k_ball  > k_gate
