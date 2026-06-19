"""
Fitting hydraulic properties used throughout the
Hydraulic Analysis Suite.

References
----------
Crane Technical Paper No. 410 (TP-410)
Hydraulic Institute Engineering Data Book
Cameron Hydraulic Data
Pumping Station Design, Third Edition
AWWA Manuals (M11, M23, M41)

Notes
-----
K-factors represent dimensionless minor loss coefficients used
in the Darcy-Weisbach head loss equation:

    h_L = K * (V^2 / 2g)

Equivalent length ratios (Le/D) represent the fitting's hydraulic
resistance expressed as an equivalent length of straight pipe per
unit diameter:

    Le = (Le/D) * D

where D is the internal pipe diameter in feet.

Crane TP-410 Methodology Note
------------------------------
Crane Technical Paper 410 (TP-410) does not publish fixed K-factors.
Instead, Crane defines K as:

    K = f_T * (Le/D)

where f_T is the Darcy friction factor for fully turbulent flow in
clean commercial steel pipe, which varies by pipe diameter.

Le/D values cited from Crane TP-410 Table A-29 are tabulated values
from that publication and are directly traceable to that source.

K-factors listed in this database are representative values for typical
water and wastewater pipe sizes (4-inch to 24-inch). These values are
appropriate for engineering planning and preliminary design. Final
design calculations should confirm K using f_T appropriate for the
actual pipe diameter per Crane TP-410.

All coefficients are based on fully turbulent flow conditions
appropriate for water and wastewater engineering applications.
No coefficient shall exist in this database without a traceable
engineering source.
"""

FITTINGS_DATA = {

    # ====================================================
    # Standard Radius Bends (r/D ≈ 1.0)
    # ====================================================

    "11_25_deg_bend_standard_radius": {
        "fitting_name": "11.25 Degree Bend - Standard Radius",
        "fitting_category": "bend",
        "k_factor": 0.10,
        "equivalent_length_ratio": 4,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, interpolated",
        "engineering_notes": "Standard radius bend, r/D ≈ 1.0. "
                             "Le/D interpolated from 45-degree and 90-degree "
                             "standard elbow tabulated values in Table A-29. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    "22_5_deg_bend_standard_radius": {
        "fitting_name": "22.5 Degree Bend - Standard Radius",
        "fitting_category": "bend",
        "k_factor": 0.20,
        "equivalent_length_ratio": 8,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, interpolated",
        "engineering_notes": "Standard radius bend, r/D ≈ 1.0. "
                             "Le/D interpolated from 45-degree and 90-degree "
                             "standard elbow tabulated values in Table A-29. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    "45_deg_bend_standard_radius": {
        "fitting_name": "45 Degree Bend - Standard Radius",
        "fitting_category": "bend",
        "k_factor": 0.40,
        "equivalent_length_ratio": 16,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Standard radius 45-degree elbow, r/D ≈ 1.0. "
                             "Le/D = 16 from Table A-29 for fully turbulent flow. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    "90_deg_bend_standard_radius": {
        "fitting_name": "90 Degree Bend - Standard Radius",
        "fitting_category": "bend",
        "k_factor": 0.75,
        "equivalent_length_ratio": 30,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Standard radius 90-degree elbow, r/D ≈ 1.0. "
                             "Le/D = 30 from Table A-29 for fully turbulent flow. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    # ====================================================
    # Long Radius Bends (r/D ≈ 1.5)
    # ====================================================

    "11_25_deg_bend_long_radius": {
        "fitting_name": "11.25 Degree Bend - Long Radius",
        "fitting_category": "bend",
        "k_factor": 0.06,
        "equivalent_length_ratio": 2,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, interpolated",
        "engineering_notes": "Long radius bend, r/D ≈ 1.5. "
                             "Le/D interpolated from 45-degree and 90-degree "
                             "long radius elbow tabulated values in Table A-29. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    "22_5_deg_bend_long_radius": {
        "fitting_name": "22.5 Degree Bend - Long Radius",
        "fitting_category": "bend",
        "k_factor": 0.12,
        "equivalent_length_ratio": 5,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, interpolated",
        "engineering_notes": "Long radius bend, r/D ≈ 1.5. "
                             "Le/D interpolated from 45-degree and 90-degree "
                             "long radius elbow tabulated values in Table A-29. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    "45_deg_bend_long_radius": {
        "fitting_name": "45 Degree Bend - Long Radius",
        "fitting_category": "bend",
        "k_factor": 0.20,
        "equivalent_length_ratio": 10,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Long radius 45-degree elbow, r/D ≈ 1.5. "
                             "Le/D = 10 from Table A-29 for fully turbulent flow. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    "90_deg_bend_long_radius": {
        "fitting_name": "90 Degree Bend - Long Radius",
        "fitting_category": "bend",
        "k_factor": 0.45,
        "equivalent_length_ratio": 16,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Long radius 90-degree elbow, r/D ≈ 1.5. "
                             "Le/D = 16 from Table A-29 for fully turbulent flow. "
                             "K is representative for mid-range pipe diameters; "
                             "compute K = f_T × (Le/D) for diameter-specific analysis.",
    },

    # ====================================================
    # Tees
    # ====================================================

    "tee_through_run": {
        "fitting_name": "Tee - Through Run",
        "fitting_category": "tee",
        "k_factor": 0.60,
        "equivalent_length_ratio": 20,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Flow passes straight through tee; branch inactive or balanced. "
                             "Le/D = 20 from Table A-29 for fully turbulent flow. "
                             "K is representative for mid-range pipe diameters.",
    },

    "tee_branch": {
        "fitting_name": "Tee - Branch Flow",
        "fitting_category": "tee",
        "k_factor": 1.80,
        "equivalent_length_ratio": 60,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Flow diverts through branch connection; run is inactive. "
                             "Le/D = 60 from Table A-29 for fully turbulent flow. "
                             "Higher loss than through-run configuration. "
                             "K is representative for mid-range pipe diameters.",
    },

    "tee_combining": {
        "fitting_name": "Tee - Combining Flow",
        "fitting_category": "tee",
        "k_factor": 2.00,
        "equivalent_length_ratio": 80,
        "source": "Hydraulic Institute Engineering Data Book",
        "source_reference": "Minor Loss Coefficients",
        "engineering_notes": "Two inlet streams combining into single outlet. "
                             "Applicable to pump station manifold configurations. "
                             "K and Le/D are representative values; "
                             "actual loss depends on flow split ratio and geometry.",
    },

    # ====================================================
    # Wyes
    # ====================================================

    "wye_standard": {
        "fitting_name": "Wye - Standard",
        "fitting_category": "wye",
        "k_factor": 0.50,
        "equivalent_length_ratio": 30,
        "source": "Pumping Station Design, Third Edition",
        "source_reference": "Minor Loss Data",
        "engineering_notes": "Standard 45-degree wye fitting. "
                             "Lower loss than tee-branch due to gradual direction change. "
                             "K and Le/D are representative values for design use.",
    },

    "wye_combination": {
        "fitting_name": "Wye - Combination",
        "fitting_category": "wye",
        "k_factor": 0.75,
        "equivalent_length_ratio": 50,
        "source": "Pumping Station Design, Third Edition",
        "source_reference": "Minor Loss Data",
        "engineering_notes": "Combination wye with 45-degree lateral connection. "
                             "Used in gravity sewer and force main configurations. "
                             "K and Le/D are representative values for design use.",
    },

    # ====================================================
    # Reducers (Contractions)
    # ====================================================

    "concentric_reducer": {
        "fitting_name": "Concentric Reducer",
        "fitting_category": "reducer",
        "k_factor": 0.05,
        "equivalent_length_ratio": 5,
        "source": "Crane Technical Paper 410",
        "source_reference": "Contraction and Enlargement Losses",
        "engineering_notes": "Gradual concentric contraction. "
                             "K value applies to velocity head at the smaller (downstream) diameter. "
                             "Assumes gradual taper angle less than 45 degrees. "
                             "Actual K depends on diameter ratio (D2/D1) and taper angle; "
                             "refer to Crane TP-410 for geometry-specific values.",
    },

    "eccentric_reducer": {
        "fitting_name": "Eccentric Reducer",
        "fitting_category": "reducer",
        "k_factor": 0.08,
        "equivalent_length_ratio": 8,
        "source": "Crane Technical Paper 410",
        "source_reference": "Contraction and Enlargement Losses",
        "engineering_notes": "Eccentric contraction. Flat-side up configuration "
                             "used to prevent air accumulation in force mains. "
                             "Slightly higher loss than concentric due to asymmetric flow. "
                             "Actual K depends on diameter ratio (D2/D1) and taper angle; "
                             "refer to Crane TP-410 for geometry-specific values.",
    },

    # ====================================================
    # Enlargements (Expansions)
    # ====================================================

    "concentric_expansion": {
        "fitting_name": "Concentric Expansion",
        "fitting_category": "expansion",
        "k_factor": 0.10,
        "equivalent_length_ratio": 10,
        "source": "Crane Technical Paper 410",
        "source_reference": "Contraction and Enlargement Losses",
        "engineering_notes": "Gradual concentric enlargement. "
                             "K value applies to velocity head at the smaller (upstream) diameter. "
                             "Assumes gradual taper angle less than 45 degrees. "
                             "Actual K depends on diameter ratio (D2/D1) and taper angle; "
                             "refer to Crane TP-410 for geometry-specific values.",
    },

    "eccentric_expansion": {
        "fitting_name": "Eccentric Expansion",
        "fitting_category": "expansion",
        "k_factor": 0.10,
        "equivalent_length_ratio": 10,
        "source": "Crane Technical Paper 410",
        "source_reference": "Contraction and Enlargement Losses",
        "engineering_notes": "Eccentric enlargement. Flat-side up configuration "
                             "used to prevent air accumulation in force mains. "
                             "Loss coefficient comparable to concentric expansion. "
                             "Actual K depends on diameter ratio (D2/D1) and taper angle; "
                             "refer to Crane TP-410 for geometry-specific values.",
    },

    # ====================================================
    # Valves (Fully Open)
    # ====================================================

    "gate_valve_open": {
        "fitting_name": "Gate Valve - Fully Open",
        "fitting_category": "valve",
        "k_factor": 0.10,
        "equivalent_length_ratio": 8,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Gate valve in fully open position. "
                             "Le/D = 8 from Table A-29 for fully turbulent flow. "
                             "Gate fully retracted from flow path; low resistance. "
                             "Loss increases significantly at partial openings.",
    },

    "butterfly_valve_open": {
        "fitting_name": "Butterfly Valve - Fully Open",
        "fitting_category": "valve",
        "k_factor": 0.60,
        "equivalent_length_ratio": 45,
        "source": "Hydraulic Institute Engineering Data Book",
        "source_reference": "Valve and Fitting Resistance Data",
        "engineering_notes": "Butterfly valve in fully open position. "
                             "Disc remains partially in flow path at full open. "
                             "K and Le/D are representative values; "
                             "actual resistance varies by manufacturer and valve size.",
    },

    "plug_valve_open": {
        "fitting_name": "Plug Valve - Fully Open",
        "fitting_category": "valve",
        "k_factor": 0.20,
        "equivalent_length_ratio": 18,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Plug valve in fully open position; straight-through port type. "
                             "Le/D = 18 from Table A-29 for fully turbulent flow. "
                             "Commonly used in water distribution and pump stations.",
    },

    "swing_check_valve": {
        "fitting_name": "Swing Check Valve",
        "fitting_category": "valve",
        "k_factor": 2.30,
        "equivalent_length_ratio": 135,
        "source": "Crane Technical Paper 410",
        "source_reference": "Table A-29, Equivalent Length of Fittings",
        "engineering_notes": "Swing check valve at normal operating velocity. "
                             "Le/D = 135 from Table A-29 for fully turbulent flow. "
                             "Loss coefficient varies with velocity and valve size. "
                             "K is representative for mid-range pipe diameters.",
    },

    "ball_check_valve": {
        "fitting_name": "Ball Check Valve",
        "fitting_category": "valve",
        "k_factor": 4.00,
        "equivalent_length_ratio": 150,
        "source": "Pumping Station Design, Third Edition",
        "source_reference": "Check Valve Minor Losses",
        "engineering_notes": "Ball-type check valve at normal operating velocity. "
                             "Higher resistance than swing check due to ball obstruction. "
                             "K and Le/D are representative values; "
                             "actual resistance varies by manufacturer and valve size. "
                             "Commonly used in wastewater pump stations.",
    },

    # ====================================================
    # Flow Meters
    # ====================================================

    "venturi_meter": {
        "fitting_name": "Venturi Meter",
        "fitting_category": "meter",
        "k_factor": 0.10,
        "equivalent_length_ratio": 5,
        "source": "Hydraulic Institute Engineering Data Book",
        "source_reference": "Flow Metering Equipment",
        "engineering_notes": "Properly designed venturi meter with gradual inlet cone "
                             "and diffuser recovery section. "
                             "Low permanent pressure loss relative to measured differential. "
                             "K and Le/D are representative values; "
                             "actual loss varies by manufacturer, beta ratio, and installation.",
    },

    "magnetic_flow_meter": {
        "fitting_name": "Magnetic Flow Meter",
        "fitting_category": "meter",
        "k_factor": 0.50,
        "equivalent_length_ratio": 20,
        "source": "Hydraulic Institute Engineering Data Book",
        "source_reference": "Flow Metering Equipment",
        "engineering_notes": "Electromagnetic flow meter (mag meter) with full-bore design. "
                             "No moving parts or flow obstructions. "
                             "Loss primarily from meter body and flange connections. "
                             "K and Le/D are representative values; "
                             "actual loss varies by manufacturer and installation.",
    },

    "turbine_meter": {
        "fitting_name": "Turbine Meter",
        "fitting_category": "meter",
        "k_factor": 1.00,
        "equivalent_length_ratio": 40,
        "source": "Hydraulic Institute Engineering Data Book",
        "source_reference": "Flow Metering Equipment",
        "engineering_notes": "Turbine-type flow meter with rotating element. "
                             "Higher resistance than mag meter due to rotor obstruction. "
                             "K and Le/D are representative values; "
                             "actual loss varies by manufacturer and installation. "
                             "Commonly used for potable water billing and custody transfer.",
    },
}
