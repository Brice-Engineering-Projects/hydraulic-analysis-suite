# pipe_materials.py

## Purpose

The `pipe_materials.py` module serves as the centralized repository for pipe material properties used throughout the Hydraulic Analysis Suite.

Rather than requiring users to manually enter hydraulic properties such as Hazen-Williams C-factors or pipe roughness values, the system stores these values in a single location and retrieves them automatically based on the selected pipe material.

This approach improves consistency, reduces user input errors, and simplifies future expansion of the hydraulic modeling framework.

---

## Responsibilities

The module is responsible for:

* Storing hydraulic properties associated with common pipe materials.
* Providing a single source of truth for material data.
* Supporting automatic property lookup during Pipe object creation.
* Eliminating duplicate material data throughout the application.
* Supporting future hydraulic equations and analysis methods.

---

## Design Philosophy

Users should identify the physical pipe material rather than manually entering equation-specific parameters.

For example:

```text
PVC
```

is a physical pipe material.

```text
C = 150
```

is a parameter used by the Hazen-Williams equation.

The Hydraulic Analysis Suite should model real-world infrastructure components whenever possible. Therefore, users select a material and the software determines the associated hydraulic properties.

This design improves usability and more closely reflects how engineering software typically handles material properties.

---

## Current Properties

Initial material properties may include:

* Hazen-Williams C-Factor
* Pipe Material Name

Example:

```python
PIPE_MATERIALS = {
    "PVC": {
        "c_factor": 150
    },
    "HDPE": {
        "c_factor": 150
    },
    "DIP_NEW": {
        "c_factor": 140
    }
}
```
### Cast Iron Pipe (CIP) Condition Table

| Condition | Typical Age Range |
| --------- | ----------------- |
| Excellent | 0-10 years        |
| Good      | 10-25 years       |
| Fair      | 25-50 years       |
| Poor      | 50+ years         |

---

## Future Properties

As the Hydraulic Analysis Suite expands, additional material properties may be added, including:

* Absolute Roughness
* Manning Roughness Coefficient (n)
* Wall Thickness
* Pressure Class
* DR Rating
* Unit Weight
* Pipe Interior Diameter Adjustments

Example future structure:

```python
PIPE_MATERIALS = {
    "PVC": {
        "c_factor": 150,
        "roughness_ft": 0.000005,
        "manning_n": 0.009,
        "wall_thickness_in": 0.50
    }
}
```

---

## Relationship to Pipe Class

During Pipe object initialization:

```text
User Input
    ↓
Pipe Material
    ↓
pipe_materials.py Lookup
    ↓
Hydraulic Properties Retrieved
    ↓
Pipe Object Created
```

The Pipe class should retrieve material properties from this module and store them as object attributes for use by equation classes and engineering calculators.

---

## Relationship to Future Modules

The material database will support:

* Pipe Class
* Hazen-Williams Equation
* Darcy-Weisbach Equation
* Manning Equation
* Force Main Calculator
* System Curve Calculator
* Pump Selection Calculator
* Future Hydraulic Analysis Modules

By centralizing material properties, future enhancements can be implemented without modifying individual equation or calculator classes.

---

## Summary

The `pipe_materials.py` module serves as the authoritative source for pipe material data within the Hydraulic Analysis Suite. It supports consistency, maintainability, and scalability by centralizing hydraulic material properties and providing a common interface for future hydraulic analyses.
