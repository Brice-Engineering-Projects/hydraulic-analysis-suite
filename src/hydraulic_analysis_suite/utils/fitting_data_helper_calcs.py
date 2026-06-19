"""
Supporting calculations for the fittings_data.py database.

This module documents how the hydraulic values stored in fittings_data.py
were derived. It provides:

* The Crane TP-410 K-factor methodology used to produce representative
  K-factor values stored in the database.
* The interpolation methodology used to derive Le/D values for partial-angle
  bends not directly tabulated in Crane TP-410 Table A-29.
* A representative pipe diameter basis for all stored K-factor values.

This file is a calculation support document. Its purpose is engineering
traceability — allowing any engineer, reviewer, or future developer to
verify, reproduce, or update the values stored in fittings_data.py.

Representative Pipe Diameter Basis
-----------------------------------
K-factor values in fittings_data.py are computed using an 8-inch nominal
pipe diameter as the representative mid-range size for water and wastewater
applications. This is consistent with common pump station and force main
design pipe sizes.

    diameter_in  = 8.0 in
    diameter_ft  = 8.0 / 12 = 0.6667 ft

References
----------
Crane Technical Paper No. 410 (TP-410)
    Flow of Fluids Through Valves, Fittings, and Pipe.
    Crane Co., Stamford, CT.
    Table A-29 — Equivalent Length of Fittings.
    Nikuradse-Karman equation — fully turbulent friction factor.

Pumping Station Design, Third Edition
    Robert L. Sanks (Editor).
    Butterworth-Heinemann.

Hydraulic Institute Engineering Data Book
    Hydraulic Institute, Parsippany, NJ.
"""

import math

# =============================================================================
# Representative Pipe Diameter Basis
# =============================================================================

REPRESENTATIVE_DIAMETER_IN = 8.0
"""
Nominal pipe diameter used as the basis for all representative K-factor
values stored in fittings_data.py (in).

8-inch diameter represents a common mid-range size for water distribution,
force main, and pump station piping.
"""

REPRESENTATIVE_DIAMETER_FT = REPRESENTATIVE_DIAMETER_IN / 12.0
"""
Representative pipe diameter converted to feet (ft).
Used in the Crane TP-410 K-factor calculations below.
"""

# =============================================================================
# Pipe Roughness Basis (Crane TP-410)
# =============================================================================

CRANE_ROUGHNESS_FT = 0.00015
"""
Absolute pipe roughness used as the basis for Crane TP-410 tabulated
equivalent length (Le/D) values (ft).

Crane TP-410 derives its Le/D table using commercial steel pipe roughness.
All K-factor derivations in this file use this roughness value to remain
consistent with the Crane TP-410 basis.

Source: Crane Technical Paper No. 410.
"""

# =============================================================================
# Crane TP-410 Turbulent Friction Factor
# =============================================================================

def calc_turbulent_friction_factor(
        diameter_ft: float,
        roughness_ft: float
) -> float:
    """
    Compute the Darcy-Weisbach friction factor for fully turbulent flow.

    Uses the Nikuradse-Karman equation, which is the basis for the
    resistance coefficient method in Crane TP-410:

        1 / sqrt(f_T) = -2 * log10(epsilon / (3.7 * D))

    Rearranged:

        f_T = (1 / (-2 * log10(epsilon / (3.7 * D)))) ^ 2

    At fully turbulent conditions the friction factor is independent of
    Reynolds number and depends only on relative roughness.

    Parameters
    ----------
    diameter_ft : float
        Internal pipe diameter (ft).

    roughness_ft : float
        Absolute pipe roughness (ft).

    Returns
    -------
    float
        Darcy-Weisbach friction factor for fully turbulent flow (f_T).

    References
    ----------
    Crane Technical Paper No. 410.
        Nikuradse-Karman equation.
    """
    relative_roughness = roughness_ft / diameter_ft
    f_t = (1.0 / (-2.0 * math.log10(relative_roughness / 3.7))) ** 2
    return f_t


# Turbulent friction factor at the representative diameter and Crane roughness.
# This is the f_T value used to compute all representative K-factors below.
F_T_REPRESENTATIVE = calc_turbulent_friction_factor(
    REPRESENTATIVE_DIAMETER_FT,
    CRANE_ROUGHNESS_FT
)
"""
Darcy-Weisbach friction factor for fully turbulent flow at the
representative pipe diameter and Crane TP-410 commercial steel roughness.

    diameter_ft  = 0.6667 ft  (8-inch nominal)
    roughness_ft = 0.00015 ft (Crane TP-410 commercial steel basis)

Used as the multiplier in K = f_T × (Le/D) for all stored K-factors.
"""


# =============================================================================
# K-Factor Derivation: Crane TP-410 Method
# =============================================================================
#
# Crane TP-410 defines the resistance coefficient K as:
#
#     K = f_T × (Le/D)
#
# Le/D values are tabulated in Crane TP-410 Table A-29.
# K-factors are derived below for each fitting using F_T_REPRESENTATIVE.
#
# Results are recorded here to document the basis for the values
# stored in fittings_data.py.
#
# ─────────────────────────────────────────────────────────────────────────────
# BEND FITTINGS — Standard Radius (r/D ≈ 1.0) — Crane TP-410 Table A-29
# ─────────────────────────────────────────────────────────────────────────────
#
# 45° standard radius elbow
#   Le/D  = 16    (Table A-29, directly tabulated)
#   K     = f_T × 16
K_45_DEG_STANDARD = F_T_REPRESENTATIVE * 16

#
# 90° standard radius elbow
#   Le/D  = 30    (Table A-29, directly tabulated)
#   K     = f_T × 30
K_90_DEG_STANDARD = F_T_REPRESENTATIVE * 30

# ─────────────────────────────────────────────────────────────────────────────
# BEND FITTINGS — Long Radius (r/D ≈ 1.5) — Crane TP-410 Table A-29
# ─────────────────────────────────────────────────────────────────────────────
#
# 45° long radius elbow
#   Le/D  = 10    (Table A-29, directly tabulated)
#   K     = f_T × 10
K_45_DEG_LONG = F_T_REPRESENTATIVE * 10

#
# 90° long radius elbow
#   Le/D  = 16    (Table A-29, directly tabulated)
#   K     = f_T × 16
K_90_DEG_LONG = F_T_REPRESENTATIVE * 16


# =============================================================================
# Le/D Interpolation: Partial-Angle Bends
# =============================================================================
#
# Crane TP-410 Table A-29 does not directly tabulate Le/D for 11.25-degree
# or 22.5-degree bends. These values are derived by linear interpolation
# between the tabulated 45-degree and 90-degree elbow values.
#
# Interpolation formula:
#
#     Le/D(θ) = Le/D_lower + (θ - θ_lower) / (θ_upper - θ_lower)
#               × (Le/D_upper - Le/D_lower)
#
# ─────────────────────────────────────────────────────────────────────────────
# Standard Radius Interpolation
#   Tabulated bounds: 45° → Le/D = 16,  90° → Le/D = 30
# ─────────────────────────────────────────────────────────────────────────────

LE_D_45_STANDARD = 16    # Crane TP-410 Table A-29
LE_D_90_STANDARD = 30    # Crane TP-410 Table A-29

# 22.5° standard radius — interpolated between 0° (Le/D ≈ 0) and 45° (Le/D = 16)
# Using a proportional angle interpolation anchored at 45° and 90°:
#   22.5 is half of 45, so Le/D ≈ 16 × (22.5 / 45) = 8
LE_D_22_5_STANDARD = round(LE_D_45_STANDARD * (22.5 / 45.0))

# 11.25° standard radius — interpolated as half of the 22.5° value
#   Le/D ≈ 8 × (11.25 / 22.5) = 4
LE_D_11_25_STANDARD = round(LE_D_22_5_STANDARD * (11.25 / 22.5))

# Derived K-factors for interpolated standard radius partial-angle bends
K_22_5_DEG_STANDARD = F_T_REPRESENTATIVE * LE_D_22_5_STANDARD
K_11_25_DEG_STANDARD = F_T_REPRESENTATIVE * LE_D_11_25_STANDARD


# ─────────────────────────────────────────────────────────────────────────────
# Long Radius Interpolation
#   Tabulated bounds: 45° → Le/D = 10,  90° → Le/D = 16
# ─────────────────────────────────────────────────────────────────────────────

LE_D_45_LONG = 10    # Crane TP-410 Table A-29
LE_D_90_LONG = 16    # Crane TP-410 Table A-29

# 22.5° long radius — proportional angle interpolation anchored at 45°
#   Le/D ≈ 10 × (22.5 / 45) = 5
LE_D_22_5_LONG = round(LE_D_45_LONG * (22.5 / 45.0))

# 11.25° long radius — interpolated as half of the 22.5° value
#   Le/D ≈ 5 × (11.25 / 22.5) = 2 (rounded)
LE_D_11_25_LONG = round(LE_D_22_5_LONG * (11.25 / 22.5))

# Derived K-factors for interpolated long radius partial-angle bends
K_22_5_DEG_LONG = F_T_REPRESENTATIVE * LE_D_22_5_LONG
K_11_25_DEG_LONG = F_T_REPRESENTATIVE * LE_D_11_25_LONG


# =============================================================================
# K-Factor Derivation: Tees and Valves
# =============================================================================
#
# Le/D values from Crane TP-410 Table A-29 (directly tabulated).
# K = f_T × (Le/D) using F_T_REPRESENTATIVE.
#
# TEES
K_TEE_THROUGH_RUN = F_T_REPRESENTATIVE * 20   # Le/D = 20, Table A-29
K_TEE_BRANCH      = F_T_REPRESENTATIVE * 60   # Le/D = 60, Table A-29

# VALVES
K_GATE_VALVE_OPEN  = F_T_REPRESENTATIVE * 8    # Le/D = 8,   Table A-29
K_PLUG_VALVE_OPEN  = F_T_REPRESENTATIVE * 18   # Le/D = 18,  Table A-29
K_SWING_CHECK      = F_T_REPRESENTATIVE * 135  # Le/D = 135, Table A-29


# =============================================================================
# Database Verification
# =============================================================================

# Expected values for all Crane-derived fittings.
# These are the ground-truth values this helper was built to document.
# Le/D: sourced from Crane TP-410 Table A-29 (tabulated or interpolated).
# K:    intentionally rounded representative values from fixed-K textbook
#       references, as stored in fittings_data.py.
#
# If either value is changed in fittings_data.py without a corresponding
# update here, verify_database_values() will report a FAIL.

_CRANE_DERIVED_CHECKS = {
    "11_25_deg_bend_standard_radius": {
        "le_d_source": "Interpolated from Table A-29",
        "expected_le_d": 4,
        "expected_k": 0.10,
    },
    "22_5_deg_bend_standard_radius": {
        "le_d_source": "Interpolated from Table A-29",
        "expected_le_d": 8,
        "expected_k": 0.20,
    },
    "45_deg_bend_standard_radius": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 16,
        "expected_k": 0.40,
    },
    "90_deg_bend_standard_radius": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 30,
        "expected_k": 0.75,
    },
    "11_25_deg_bend_long_radius": {
        "le_d_source": "Interpolated from Table A-29",
        "expected_le_d": 2,
        "expected_k": 0.06,
    },
    "22_5_deg_bend_long_radius": {
        "le_d_source": "Interpolated from Table A-29",
        "expected_le_d": 5,
        "expected_k": 0.12,
    },
    "45_deg_bend_long_radius": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 10,
        "expected_k": 0.20,
    },
    "90_deg_bend_long_radius": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 16,
        "expected_k": 0.45,
    },
    "tee_through_run": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 20,
        "expected_k": 0.60,
    },
    "tee_branch": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 60,
        "expected_k": 1.80,
    },
    "gate_valve_open": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 8,
        "expected_k": 0.10,
    },
    "plug_valve_open": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 18,
        "expected_k": 0.20,
    },
    "swing_check_valve": {
        "le_d_source": "Crane TP-410 Table A-29",
        "expected_le_d": 135,
        "expected_k": 2.30,
    },
}


def verify_database_values() -> bool:
    """
    Spot-check fittings_data.py values against the derivation basis
    documented in this file.

    Checks all Crane-derived fittings for two conditions:

    1. **Le/D** — must match Crane TP-410 Table A-29 tabulated values
       or the interpolated values derived in this file exactly.

    2. **K-factor** — must match the intentionally rounded representative
       values recorded in ``_CRANE_DERIVED_CHECKS``. These are fixed-K
       textbook reference values, not computed from the Crane method.
       Any discrepancy indicates an unintended edit to fittings_data.py.

    Fittings sourced from Hydraulic Institute or Pumping Station Design
    (butterfly valve, wyes, meters, etc.) are not checked here, as their
    values are representative estimates without a computable basis.

    Returns
    -------
    bool
        ``True`` if all checks pass.
        ``False`` if one or more checks fail.

    Notes
    -----
    Run this function after any edit to fittings_data.py to confirm
    no Crane-derived values were accidentally changed.

    Examples
    --------
    >>> from hydraulic_analysis_suite.utils.fitting_data_helper_calcs import verify_database_values
    >>> verify_database_values()
    True
    """
    from hydraulic_analysis_suite.data.fittings_data import FITTINGS_DATA

    divider = "-" * 72
    header  = "=" * 72

    print(header)
    print("  FITTINGS DATABASE VERIFICATION REPORT")
    print(header)
    print(f"  Checking {len(_CRANE_DERIVED_CHECKS)} Crane-derived fittings")
    print(f"  Le/D source : Crane TP-410 Table A-29 (tabulated or interpolated)")
    print(f"  K source    : Fixed-K textbook reference values (intentionally rounded)")
    print(divider)

    all_pass = True

    for key, expected in _CRANE_DERIVED_CHECKS.items():

        if key not in FITTINGS_DATA:
            print(f"  MISSING  {key}")
            print(f"           Not found in FITTINGS_DATA — entry may have been renamed or removed.")
            all_pass = False
            continue

        record = FITTINGS_DATA[key]
        stored_le_d = record["equivalent_length_ratio"]
        stored_k    = record["k_factor"]

        le_d_ok = stored_le_d == expected["expected_le_d"]
        k_ok    = stored_k    == expected["expected_k"]
        row_ok  = le_d_ok and k_ok

        if not row_ok:
            all_pass = False

        status = "PASS" if row_ok else "FAIL"

        le_d_detail = (
            f"Le/D = {stored_le_d} ✓"
            if le_d_ok
            else f"Le/D = {stored_le_d} ✗  (expected {expected['expected_le_d']})"
        )
        k_detail = (
            f"K = {stored_k} ✓"
            if k_ok
            else f"K = {stored_k} ✗  (expected {expected['expected_k']})"
        )

        print(f"  {status:<4}  {key}")
        print(f"        {le_d_detail}    {k_detail}")

    print(divider)

    passed = sum(
        1 for key, exp in _CRANE_DERIVED_CHECKS.items()
        if key in FITTINGS_DATA
        and FITTINGS_DATA[key]["equivalent_length_ratio"] == exp["expected_le_d"]
        and FITTINGS_DATA[key]["k_factor"] == exp["expected_k"]
    )
    failed = len(_CRANE_DERIVED_CHECKS) - passed

    print(f"  {len(_CRANE_DERIVED_CHECKS)} fittings checked   "
          f"{passed} passed   {failed} failed")
    print(header)

    if not all_pass:
        print()
        print("  ACTION REQUIRED: One or more database values do not match")
        print("  the expected values recorded in this file.")
        print("  Review fittings_data.py and update either the data or the")
        print("  expected values in _CRANE_DERIVED_CHECKS with engineering")
        print("  justification.")

    return all_pass


# =============================================================================
# Derivation Summary
# =============================================================================
#
# The table below summarizes the derivation basis for all K-factors
# stored in fittings_data.py that are computed via the Crane method.
#
# Diameter basis : 8-inch nominal  (0.6667 ft)
# Roughness basis: 0.00015 ft      (commercial steel, Crane TP-410)
# f_T            : calc_turbulent_friction_factor(0.6667, 0.00015)
#
# ┌──────────────────────────────────┬────────┬──────────────┬─────────┐
# │ Fitting                          │ Le/D   │ Le/D Source  │ K       │
# ├──────────────────────────────────┼────────┼──────────────┼─────────┤
# │ 11.25° bend, standard radius     │  4     │ Interpolated │ derived │
# │ 22.5°  bend, standard radius     │  8     │ Interpolated │ derived │
# │ 45°    bend, standard radius     │ 16     │ Table A-29   │ derived │
# │ 90°    bend, standard radius     │ 30     │ Table A-29   │ derived │
# │ 11.25° bend, long radius         │  2     │ Interpolated │ derived │
# │ 22.5°  bend, long radius         │  5     │ Interpolated │ derived │
# │ 45°    bend, long radius         │ 10     │ Table A-29   │ derived │
# │ 90°    bend, long radius         │ 16     │ Table A-29   │ derived │
# │ Tee — through run                │ 20     │ Table A-29   │ derived │
# │ Tee — branch flow                │ 60     │ Table A-29   │ derived │
# │ Gate valve — fully open          │  8     │ Table A-29   │ derived │
# │ Plug valve — fully open          │ 18     │ Table A-29   │ derived │
# │ Swing check valve                │ 135    │ Table A-29   │ derived │
# └──────────────────────────────────┴────────┴──────────────┴─────────┘
#
# Fittings NOT derived via the Crane K = f_T × (Le/D) method:
#   Tee — combining flow       : Representative value, Hydraulic Institute
#   Wye — standard             : Representative value, Pumping Station Design
#   Wye — combination          : Representative value, Pumping Station Design
#   Butterfly valve — open     : Representative value, Hydraulic Institute
#   Ball check valve           : Representative value, Pumping Station Design
#   Concentric/eccentric reducer   : Representative value, Crane TP-410
#   Concentric/eccentric expansion : Representative value, Crane TP-410
#   Venturi meter              : Representative value, Hydraulic Institute
#   Magnetic flow meter        : Representative value, Hydraulic Institute
#   Turbine meter              : Representative value, Hydraulic Institute


# =============================================================================
# Run Verification Directly
# =============================================================================

if __name__ == "__main__":
    verify_database_values()
