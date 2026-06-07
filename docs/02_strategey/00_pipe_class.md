# Pipe Class Purpose

The Pipe class represents a physical pipe segment within a hydraulic
system. It stores the geometric, material, and hydraulic properties
required to perform engineering calculations and analyses.

The Pipe class serves as a foundational model that can be used by
equation classes, hydraulic calculators, and future system-level
analysis tools.

Its responsibilities include:

* Storing pipe characteristics.
* Validating engineering input data.
* Retrieving material properties.
* Providing commonly used derived pipe properties.

The Pipe class does not perform hydraulic analyses directly. Instead,
it supplies validated pipe data to equation and calculator classes.

## Pipe Class Methods

- __init__()
- _validate_data()
- _lookup_material_properties()
- summary()
- __str__()
- __repr__()

### summary()
Summary will be more robust than __str__() and __repr__().  It will summarize the pipe object physical and hydraulic 
properties.

For example:
```text
Pipe Summary
------------
Material: PVC
Flow Rate: 5.50 gpm
Diameter: 12.0 in
Length: 1000.0 ft

Hydraulic Properties
--------------------
C-Factor: 150
Roughness: 0.000005 ft
Manning n: 0.009
```

## Pipe Class Attributes

- flow_rate_gpm
- diameter_in
- length_ft
- material
- c_factor
- roughness_ft
- manning_n
- wall_thickness_in (FUTURE ATTRIBUTE)

## Pipe Class Derived Properties

- flow_rate_cfs
- diameter_ft
- length_miles
- radius_in
- area_sf
- volume_cuft
- velocity_fps
- wetted_perimeter (FUTURE)
- hydraulic_radius_in (FUTURE)

## Pipe Class Structure

```plaintext
Pipe
│
├── Methods
│   ├── __init__()
│   ├── _validate_data()
│   ├── _lookup_material_properties()
│   ├── __str__()
│   ├── __repr__()
│   └── summary()
│
├── Attributes
│   ├── flow_rate_gpm
│   ├── diameter_in
│   ├── length_ft
│   ├── material
│   ├── c_factor
│   ├── roughness_ft
│   ├── manning_n
│   └── wall_thickness_in (FUTURE)
│
└── Properties
    ├── flow_rate_cfs
    ├── wetted_perimeter_ft (FUTURE)
    ├── diameter_ft
    ├── length_miles
    ├── radius_in
    ├── area_sf
    ├── volume_cuft
    ├── velocity_cfs    
    └── hydraulic_radius_in (FUTURE)
```
## Summary
The Pipe class serves as the foundational model for
the Hydraulic Analysis Suite. It stores validated
pipe characteristics, retrieves material properties,
and provides derived geometric properties required
by hydraulic equations and engineering calculators.

By separating pipe data from hydraulic calculations,
the class promotes modular design and supports future
expansion into force main analysis, lift station
design, system curves, and other hydraulic workflows.


## Notes
Hydraulic radius intentionally omitted from Pipe class.

Hydraulic radius is dependent on flow geometry
and wetted perimeter. Future implementations
within Manning or gravity flow analysis modules
will calculate hydraulic radius based on actual
flow conditions rather than assuming full-pipe flow.