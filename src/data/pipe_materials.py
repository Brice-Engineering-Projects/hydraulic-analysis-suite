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
"""

PIPE_MATERIALS = {

    "steel": {
        "material_name": "Steel",
        "c_factor": 120,
        "roughness_ft": 0.00015,
        "manning_n": 0.012,
    },

    "aluminum": {
        "material_name": "Aluminum",
        "c_factor": 130,
        "roughness_ft": 0.000005,
        "manning_n": 0.012,
    },

    "plastic": {
        "material_name": "Plastic",
        "c_factor": 150,
        "roughness_ft": 0.000005,
        "manning_n": 0.009,
    },

    "copper": {
        "material_name": "Copper",
        "c_factor": 140,
        "roughness_ft": 0.000005,
        "manning_n": 0.011,
    },

    "pvc": {
        "material_name": "PVC",
        "c_factor": 150,
        "roughness_ft": 0.000005,
        "manning_n": 0.009,
    },

    "hdpe": {
        "material_name": "HDPE",
        "c_factor": 150,
        "roughness_ft": 0.000005,
        "manning_n": 0.009,
    },

    "dip_new": {
        "material_name": "DIP_NEW",
        "c_factor": 140,
        "roughness_ft": 0.00085,
        "manning_n": 0.012,
    },

    "dip_aged": {
        "material_name": "DIP_AGED",
        "c_factor": 100,
        "roughness_ft": 0.0020,
        "manning_n": 0.014,
    },

    "concrete": {
        "material_name": "Concrete",
        "c_factor": 120,
        "roughness_ft": 0.0010,
        "manning_n": 0.013,
    },

    "cast_iron": {
        "material_name": "Cast Iron",
        "c_factor": 100,
        "roughness_ft": 0.00085,
        "manning_n": 0.013,
    },

    "galvanized": {
        "material_name": "Galvanized",
        "c_factor": 120,
        "roughness_ft": 0.0005,
        "manning_n": 0.015,
    },

    "brass": {
        "material_name": "Brass",
        "c_factor": 130,
        "roughness_ft": 0.000005,
        "manning_n": 0.011,
    },

    "bronze": {
        "material_name": "Bronze",
        "c_factor": 130,
        "roughness_ft": 0.000005,
        "manning_n": 0.011,
    },

    "stainless_steel": {
        "material_name": "Stainless Steel",
        "c_factor": 140,
        "roughness_ft": 0.000007,
        "manning_n": 0.011,
    },

    "other": {
        "material_name": "Other",
        "c_factor": 120,
        "roughness_ft": 0.0010,
        "manning_n": 0.013,
    },
}

