# Fitting Class Design Specification

## Overview

The `Fitting` class represents localized hydraulic losses associated with pipeline fittings, valves, appurtenances, and pipe transitions.

The class serves as the authoritative source for fitting-related hydraulic properties used throughout the Hydraulic Analysis Suite.

The objective is to provide a standardized, database-driven representation of hydraulic fittings that can be used consistently across:

* Friction loss calculations
* Minor loss calculations
* Total Dynamic Head (TDH) calculations
* Force main design
* Water distribution modeling
* Pump station design
* Future hydraulic network analysis
* Future surge and transient analysis

---

# Design Philosophy

The Fitting class shall:

* Store fitting information
* Validate fitting inputs
* Retrieve hydraulic coefficients from a centralized database
* Provide equivalent length calculations
* Provide engineering traceability for all hydraulic coefficients
* Serve as a reusable hydraulic component throughout the application
* Remain database-driven and easily expandable

The Fitting class shall NOT:

* Perform system-wide hydraulic calculations
* Size pumps
* Solve hydraulic networks
* Calculate pipe friction loss
* Perform surge analysis

These responsibilities belong to other components within the Hydraulic Analysis Suite.

---

# Engineering References

Hydraulic data shall be sourced from recognized engineering references whenever possible.

Primary references include:

## Standards

* AWWA Manuals

  * M11 Steel Pipe
  * M23 PVC Pipe
  * M41 Ductile Iron Pipe
* Hydraulic Institute Standards
* WEF Design Manuals

## Textbooks and Industry References

* MWH Water Distribution Systems Handbook
* MWH Water Treatment Principles and Design
* Pumping Station Design (3rd Edition)
* Cameron Hydraulic Data
* Crane Technical Paper 410 (TP-410)

---

# Engineering Traceability

All hydraulic coefficients contained within the fitting database shall be traceable to an authoritative engineering source.

Each database entry shall include:

* Source publication
* Reference location
* Engineering notes

This supports:

* QA/QC review
* Peer review
* Design documentation
* Regulatory review
* Future database maintenance
* Verification of assumptions

No hydraulic coefficient shall exist within the database without an identifiable source.

---

# File Structure

```text
hydraulic_analysis_suite/

├── models/
│   └── fitting.py
│
├── data/
│   └── fitting_database.py
│
├── equations/
│   └── minor_losses.py
│
└── tests/
    └── test_fitting.py
```

---

# Class Scope (Supported Fitting Categories)

The class shall represent:

## Directional Fittings

### Standard Radius Bends

* 11.25° Bend
* 22.5° Bend
* 45° Bend
* 90° Bend

### Long Radius Bends

* 11.25° Bend
* 22.5° Bend
* 45° Bend
* 90° Bend

---

## Tees

* Tee Through Run
* Tee Branch
* Combining Tee

---

## Wyes

* Standard Wye
* Combination Wye

---

## Reducers

* Concentric Reducer
* Eccentric Reducer

---

## Enlargements

* Concentric Expansion
* Eccentric Expansion

---

## Valves

* Gate Valve (Fully Open)
* Butterfly Valve (Fully Open)
* Plug Valve (Fully Open)
* Swing Check Valve
* Ball Check Valve

---

## Meters

* Venturi Meter
* Magnetic Flow Meter
* Turbine Meter

---

# Constructor Attributes

## Required Attributes

### fitting_name

**Type**

```text
str
```

**Examples**

```text
"11.25_deg_bend_standard_radius"
"22.5_deg_bend_standard_radius"
"45_deg_bend_standard_radius"
"90_deg_bend_standard_radius"

"11.25_deg_bend_long_radius"
"22.5_deg_bend_long_radius"
"45_deg_bend_long_radius"
"90_deg_bend_long_radius"

"tee_through_run"
"tee_branch"

"gate_valve_open"
"butterfly_valve_open"
"plug_valve_open"

"eccentric_reducer"
"concentric_reducer"
```

---

### diameter_in

**Type**

```text
float
```

**Description**

Nominal fitting diameter.

Must be greater than zero.

---

### quantity

**Type**

```text
int
```

**Default**

```text
1
```

Must be greater than zero.

---

# Optional Attributes

## material

**Type**

```text
str
```

**Examples**

```text
PVC
DIP
HDPE
Steel
```

Reserved for future implementation.

---

## manufacturer

**Type**

```text
str
```

Reserved for future manufacturer-specific fitting data.

Examples:

```text
Mueller
Kennedy
Pratt
Clow
```

---

## notes

**Type**

```text
str
```

User-supplied comments.

---

# Database Structure

Each fitting entry shall contain:

```json
{
    "fitting_name": "str",
    "fitting_category": "str",
    "k_factor": "float",
    "equivalent_length_ratio": "float",
    "source": "str",
    "source_reference": "str",
    "engineering_notes": "str"
}
```

---

# Database Field Definitions

## fitting_name

Human-readable fitting identifier.

Example:

```text
"45_deg_bend_long_radius"
```

---

## fitting_category

Example:

```text
"bend"
"tee"
"valve"
"meter"
```

---

## k_factor

Minor loss coefficient.

Used for hydraulic loss calculations.

---

## equivalent_length_ratio

Equivalent length expressed as:

```text
Le / D
```

This value shall be stored in the database rather than fixed equivalent length values.

Equivalent length shall be calculated dynamically:

```text
Equivalent Length = (Le / D) × Diameter
```

This provides scalability across all pipe diameters.

---

## source

Authoritative source publication.

Examples:

```text
"AWWA M41"
"AWWA M11"
"Hydraulic Institute"
"Cameron Hydraulic Data"
```

---

## source_reference

Specific location within the reference.

Examples:

```text
"Table 7-3"
"Section 5.4"
"Appendix B"
"Page 215"
```

---

## engineering_notes

Additional assumptions or limitations.

Examples:

```text
"Fully open condition"
"Long radius fitting"
"Water service application"
```

---

# Public Attributes Checklist

## Input Attributes

* [ ] fitting_name
* [ ] diameter_in
* [ ] quantity
* [ ] material
* [ ] manufacturer
* [ ] notes

---

# Derived Properties Checklist

## Hydraulic Properties

* [ ] fitting_category
* [ ] k_factor
* [ ] equivalent_length_ratio

## Engineering Reference Properties

* [ ] source
* [ ] source_reference
* [ ] engineering_notes

## Calculated Properties

* [ ] diameter_ft
* [ ] equivalent_length_ft
* [ ] total_equivalent_length_ft
* [ ] description

## Future Properties

* [ ] velocity_fps
* [ ] headloss_ft
* [ ] pressure_loss_psi

---

# Validation Methods Checklist

* [ ] _validate_data()
* [ ] _validate_fitting_name()
* [ ] _validate_diameter()
* [ ] _validate_quantity()

---

# Database Methods Checklist

* [ ] _lookup_fitting_data()
* [ ] _get_fitting_category()
* [ ] _get_k_factor()
* [ ] _get_equivalent_length_ratio()
* [ ] _get_source()
* [ ] _get_source_reference()
* [ ] _get_engineering_notes()

---

# Dunder Methods Checklist

* [ ] **repr**()
* [ ] **str**()

---

# Future Public Methods

## Reporting

* [ ] to_dict()
* [ ] generate_reference_report()
* [ ] generate_hydraulic_summary()

## Hydraulic Calculations

* [ ] calculate_headloss()
* [ ] calculate_pressure_loss()

---

# MVP Scope

The Minimum Viable Product shall include:

### Core Functionality

* Fitting object creation
* Database lookup
* Data validation
* K-factor retrieval
* Equivalent length ratio retrieval
* Equivalent length calculations
* Engineering reference retrieval
* String representations
* Unit testing

### Included Fittings

* Standard radius bends
* Long radius bends
* Tees
* Wyes
* Reducers
* Expansions
* Valves
* Meters

### Excluded from MVP

* Headloss calculations
* Pressure loss calculations
* Manufacturer-specific fittings
* Variable valve positions
* Surge analysis
* Transient modeling

---

# Future Enhancements

## Phase 2

* Headloss calculations
* Pressure loss calculations
* Velocity-dependent losses
* Valve position adjustments

---

## Phase 3

* Manufacturer-specific databases
* Product-specific coefficients
* Control valve losses
* Air release valve losses
* Backflow preventer losses

---

## Phase 4

* Surge analysis support
* Transient modeling support
* Hydraulic network solver integration
* Pump class integration
* Force main class integration

---

# Development Checklist

## Class Development

* [ ] Create fitting.py
* [ ] Create constructor
* [ ] Create validation methods
* [ ] Create database lookup methods
* [ ] Create properties
* [ ] Create dunder methods

---

## Database Development

* [ ] Create fitting_database.py
* [ ] Add standard-radius bends
* [ ] Add long-radius bends
* [ ] Add tees
* [ ] Add wyes
* [ ] Add reducers
* [ ] Add expansions
* [ ] Add valves
* [ ] Add meters
* [ ] Add engineering references

---

## Testing

* [ ] Valid fitting creation
* [ ] Invalid fitting name
* [ ] Invalid diameter
* [ ] Invalid quantity
* [ ] Database lookup validation
* [ ] Property validation
* [ ] Engineering reference validation
* [ ] Dunder method validation

---

# Summary

The Fitting class provides a standardized, database-driven representation of localized hydraulic losses throughout the Hydraulic Analysis Suite.

The class shall serve as the authoritative source for fitting hydraulic characteristics, equivalent length values, engineering references, and future hydraulic calculations.

All fitting data shall be traceable to authoritative engineering sources and structured to support future expansion into pump station design, force main analysis, surge analysis, and hydraulic network modeling.
