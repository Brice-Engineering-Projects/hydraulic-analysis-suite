"""
Pipe material properties used throughout the
Hydraulic Analysis Suite.

References
----------
Pumping Station Design, Third Edition
Hydraulic Institute Standards
AWWA Manuals
Crane Technical Paper No. 410
Manning and Hazen-Williams reference tables

Notes
-----
Condition categories represent generalized engineering
assumptions regarding the hydraulic condition of a pipe.

Age is commonly used as a proxy for condition; however,
actual hydraulic performance may vary depending on
lining, water quality, corrosion, maintenance history,
and operating conditions.
"""

PIPE_MATERIALS = {

    # ====================================================
    # Gravity Sewer Materials
    # ====================================================

    "brick_sewer_new": {
        "material_name": "Brick Sewer (New)",
        "application": "gravity",
        "category": "masonry",
        "c_factor": 100,
        "roughness_ft": 0.0030,
        "manning_n": 0.015,
    },

    "brick_sewer_old": {
        "material_name": "Brick Sewer (Old)",
        "application": "gravity",
        "category": "masonry",
        "c_factor": 80,
        "roughness_ft": 0.0100,
        "manning_n": 0.017,
    },

    "vitrified_clay": {
        "material_name": "Vitrified Clay Pipe",
        "application": "gravity",
        "category": "masonry",
        "c_factor": 110,
        "roughness_ft": 0.0015,
        "manning_n": 0.013,
    },

    "concrete_sewer": {
        "material_name": "Concrete Sewer",
        "application": "gravity",
        "category": "concrete",
        "c_factor": 120,
        "roughness_ft": 0.0010,
        "manning_n": 0.013,
    },

    "concrete_sewer_aged": {
        "material_name": "Concrete Sewer (Aged)",
        "application": "gravity",
        "category": "concrete",
        "c_factor": 100,
        "roughness_ft": 0.0030,
        "manning_n": 0.015,
    },


    # ====================================================
    # Concrete Pipe Materials
    # ====================================================

    "rcp": {
        "material_name": "RCP",
        "application": "gravity",
        "category": "concrete",
        "c_factor": 120,
        "roughness_ft": 0.0010,
        "manning_n": 0.013,
    },

    "concrete": {
        "material_name": "Concrete",
        "application": "gravity",
        "category": "concrete",
        "c_factor": 120,
        "roughness_ft": 0.0010,
        "manning_n": 0.013,
    },

    # ====================================================
    # Plastic Pipe Materials
    # ====================================================

    "abs": {
        "material_name": "ABS",
        "application": "gravity",
        "category": "plastic",
        "c_factor": 140,
        "roughness_ft": 0.000005,
        "manning_n": 0.011,
    },

    # ====================================================
    # Asbestos Cement Pipe
    # ====================================================

    "asbestos_cement_new": {
        "material_name": "Asbestos Cement (New)",
        "application": "pressure",
        "category": "abestos_cement",
        "c_factor": 140,
        "roughness_ft": 0.00030,
        "manning_n": 0.011,
    },

    "asbestos_cement_aged": {
        "material_name": "Asbestos Cement (Aged)",
        "application": "pressure",
        "category": "abestos_cement",
        "c_factor": 130,
        "roughness_ft": 0.00050,
        "manning_n": 0.012,
    },

    "asbestos_cement_old": {
        "material_name": "Asbestos Cement (Old)",
        "application": "pressure",
        "category": "abestos_cement",
        "c_factor": 120,
        "roughness_ft": 0.00100,
        "manning_n": 0.013,
    },

    # ====================================================
    # PVC and HDPE Pipe Materials
    # ====================================================

    "pvc": {
        "material_name": "PVC",
        "application": "both",
        "category": "plastic",
        "c_factor": 150,
        "roughness_ft": 0.000005,
        "manning_n": 0.009,
    },

    "hdpe": {
        "material_name": "HDPE",
        "application": "both",
        "category": "plastic",
        "c_factor": 150,
        "roughness_ft": 0.000005,
        "manning_n": 0.009,
    },

    # ====================================================
    # Ductile Iron Pipe Materials
    # ====================================================

    "dip_new": {
        "material_name": "DIP_NEW",
        "application": "pressure",
        "category": "ductile_iron",
        "c_factor": 140,
        "roughness_ft": 0.00085,
        "manning_n": 0.012,
    },

    "dip_aged": {
        "material_name": "DIP_AGED",
        "application": "pressure",
        "category": "ductile_iron",
        "c_factor": 100,
        "roughness_ft": 0.0020,
        "manning_n": 0.014,
    },

    # ==================================================================
    # Cast Iron and Wrought Iron Pipe Materials
    # See docs/02_strategy/01_pipe_materials.md for condition age table
    # ==================================================================

    "cast_iron_unlined_excellent": {
        "material_name": "Cast Iron - Unlined (Excellent)",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 130,
        "roughness_ft": 0.00085,
        "manning_n": 0.013,
    },

    "cast_iron_unlined_good": {
        "material_name": "Cast Iron - Unlined (Good)",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 120,
        "roughness_ft": 0.0010,
        "manning_n": 0.013,
    },

    "cast_iron_unlined_fair": {
        "material_name": "Cast Iron - Unlined (Fair)",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 100,
        "roughness_ft": 0.0020,
        "manning_n": 0.014,
    },

    "cast_iron_unlined_poor": {
        "material_name": "Cast Iron - Unlined (Poor)",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 80,
        "roughness_ft": 0.0050,
        "manning_n": 0.016,
    },

    "cast_iron_cement_lined": {
        "material_name": "Cast Iron - Cement Mortar Lined",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 140,
        "roughness_ft": 0.00030,
        "manning_n": 0.012,
    },

    "cast_iron_bituminous_lined": {
        "material_name": "Cast Iron - Bituminous Lined",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 130,
        "roughness_ft": 0.00085,
        "manning_n": 0.013,
    },

    "cast_iron_asphalt_coated": {
        "material_name": "Cast Iron - Asphalt Coated",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 125,
        "roughness_ft": 0.00100,
        "manning_n": 0.013,
    },

    "cast_iron_seal_coated": {
        "material_name": "Cast Iron - Seal Coated",
        "application": "pressure",
        "category": "cast_iron",
        "c_factor": 125,
        "roughness_ft": 0.00100,
        "manning_n": 0.013,
    },

    "wrought_iron_plain": {
        "material_name": "Wrought Iron - Plain",
        "application": "pressure",
        "category": "wrought_iron",
        "c_factor": 110,
        "roughness_ft": 0.00150,
        "manning_n": 0.014,
    },

    "wrought_iron_coated": {
        "material_name": "Wrought Iron - Coated",
        "application": "pressure",
        "category": "wrought_iron",
        "c_factor": 120,
        "roughness_ft": 0.00100,
        "manning_n": 0.013,
    },

    # ====================================================
    # Metal Pipe Materials
    # ====================================================

    "corrugated_metal_pipe": {
        "material_name": "Corrugated Metal Pipe",
        "application": "gravity",
        "category": "metal",
        "c_factor": 60,
        "roughness_ft": 0.0080,
        "manning_n": 0.024,
    },

    "steel": {
        "material_name": "Steel",
        "application": "pressure",
        "category": "metal",
        "c_factor": 120,
        "roughness_ft": 0.00015,
        "manning_n": 0.012,
    },

    "aluminum": {
        "material_name": "Aluminum",
        "application": "pressure",
        "category": "metal",
        "c_factor": 130,
        "roughness_ft": 0.000005,
        "manning_n": 0.012,
    },

    "galvanized": {
        "material_name": "Galvanized",
        "application": "pressure",
        "category": "metal",
        "c_factor": 120,
        "roughness_ft": 0.0005,
        "manning_n": 0.015,
    },

    "brass": {
        "material_name": "Brass",
        "application": "pressure",
        "category": "metal",
        "c_factor": 130,
        "roughness_ft": 0.000005,
        "manning_n": 0.011,
    },

    "bronze": {
        "material_name": "Bronze",
        "application": "pressure",
        "category": "metal",
        "c_factor": 130,
        "roughness_ft": 0.000005,
        "manning_n": 0.011,
    },

    "stainless_steel": {
        "material_name": "Stainless Steel",
        "application": "pressure",
        "category": "metal",
        "c_factor": 140,
        "roughness_ft": 0.000007,
        "manning_n": 0.011,
    },

    "copper": {
        "material_name": "Copper",
        "application": "pressure",
        "category": "metal",
        "c_factor": 140,
        "roughness_ft": 0.000005,
        "manning_n": 0.011,
    },
}
