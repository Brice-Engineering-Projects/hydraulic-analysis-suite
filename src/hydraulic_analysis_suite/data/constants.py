"""
Engineering constants and unit conversion factors used throughout
the Hydraulic Analysis Suite.

References
----------
Pumping Station Design, Third Edition
Hydraulic Institute Standards
AWWA Manuals
"""

# =============================================================================
# Unit Conversion Factors
# =============================================================================

GPM_TO_CFS = 0.002228
"""Gallons per minute to cubic feet per second."""

INCHES_PER_FOOT = 12.0
"""Inches per foot."""

FEET_PER_MILE = 5280.0
"""Feet per mile."""

HP_TO_KW = 0.746
"""Horsepower to kilowatts."""

KW_PER_HP = 1.341
"""Kilowatts per horsepower."""

SQFT_PER_ACRE = 43560.0
"""Square feet per acre."""

GALLONS_PER_CUBIC_FOOT = 7.48052
"""Gallons per cubic foot."""

CFS_TO_GPM = 448.831
"""Cubic feet per second to gallons per minute conversion factor."""


# =============================================================================
# Time Constants
# =============================================================================

SECONDS_PER_DAY = 86400
"""Seconds per day."""


# =============================================================================
# Physical Constants
# =============================================================================

GRAVITY_FTPS2 = 32.174
"""Acceleration due to gravity (ft/s²)."""

WATER_DENSITY_LB_PER_FT3 = 62.4
"""Density/specific weight of water at typical design temperatures (lb/ft³)."""


# =============================================================================
# Hydraulic Equation Constants
# =============================================================================

HAZEN_WILLIAMS_US_COEFFICIENT = 4.727
"""
Coefficient used in the Hazen-Williams equation for U.S. customary units.
"""

MANNING_US_COEFFICIENT = 1.49
"""
Coefficient used in the Manning equation for U.S. customary units.
"""

# =============================================================================
# Geometry
# =============================================================================

PI = 3.141592653589793
"""The value of pi."""

# =============================================================================
# Electrical
# =============================================================================

THREE_PHASE_FACTOR = 1.732
"""Three-phase power factor."""

DEFAULT_POWER_FACTOR = 0.80
"""
Typical power factor assumed for wastewater pumping
and motor-driven systems during preliminary electrical
and generator sizing calculations.

Note
----
This value is an engineering assumption and should be
replaced with manufacturer-provided data whenever
available.
"""
