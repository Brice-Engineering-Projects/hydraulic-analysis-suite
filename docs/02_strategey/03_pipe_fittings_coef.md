# fitting_coefficients.py

## Purpose

The `fitting_coefficients.py` module serves as the centralized repository for minor loss coefficients used throughout the Hydraulic Analysis Suite.

The purpose of this module is to provide a consistent source of fitting loss data for hydraulic calculations involving valves, bends, tees, reducers, expansions, and other pipe system components.

By centralizing fitting coefficients, the application avoids duplicated data, promotes consistency between calculations, and simplifies future expansion of the hydraulic modeling framework.

---

## Responsibilities

The module is responsible for:

* Storing minor loss coefficients (K-values).
* Providing a single source of truth for fitting loss data.
* Supporting automatic fitting loss calculations.
* Eliminating duplicate fitting data throughout the application.
* Supporting future hydraulic analysis workflows.

---

## Design Philosophy

Minor losses are commonly represented using loss coefficients:

h_L=K\frac{V^2}{2g}

where:

* hL = Minor head loss
* K = Loss coefficient
* V = Flow velocity
* g = Gravitational acceleration

The Hydraulic Analysis Suite should allow users to identify physical fittings rather than manually entering loss coefficients whenever possible.

For example:

```text
90 Degree Standard Elbow
```

instead of:

```text
K = 0.90
```

The fitting coefficient database translates engineering components into the corresponding hydraulic parameters required by calculation modules.

---

## Current Fitting Categories

The database may initially include:

### Elbows

* 90 Degree Standard Elbow
* 90 Degree Long Radius Elbow
* 45 Degree Elbow

### Tees

* Tee Through Run
* Tee Through Branch

### Valves

* Gate Valve
* Butterfly Valve
* Plug Valve
* Check Valve

### Transitions

* Sudden Expansion
* Sudden Contraction
* Reducers

---

## Example Structure

```python
FITTING_COEFFICIENTS = {

    "90_ELBOW_STD": {
        "k_value": 0.90
    },

    "45_ELBOW_STD": {
        "k_value": 0.40
    },

    "TEE_RUN": {
        "k_value": 0.60
    },

    "TEE_BRANCH": {
        "k_value": 1.80
    },

    "GATE_VALVE_OPEN": {
        "k_value": 0.15
    },

    "SWING_CHECK_VALVE": {
        "k_value": 2.00
    }
}
```

---

## Future Expansion

As the Hydraulic Analysis Suite grows, additional fitting information may be added:

* Equivalent Length Values
* Manufacturer-Specific Data
* Valve Position Adjustments
* Diameter-Based Coefficients
* Utility-Specific Design Standards

Example future structure:

```python
FITTING_COEFFICIENTS = {

    "90_ELBOW_STD": {
        "k_value": 0.90,
        "equivalent_length_ft": 30,
        "reference": "Hydraulic Institute"
    }
}
```

---

## Relationship to Future Modules

The fitting coefficient database will support:

* Minor Loss Calculations
* Total Dynamic Head (TDH) Calculator
* Force Main Calculator
* System Curve Calculator
* Pump Selection Calculator
* Lift Station Design Modules

---

## Relationship to Pipe Class

Unlike pipe material properties, fitting coefficients are not intrinsic properties of a Pipe object.

A Pipe object represents a physical pipe segment.

Fitting coefficients represent hydraulic losses associated with components installed within the piping system.

Therefore, fitting data should be retrieved by calculation modules rather than stored directly within the Pipe class.

---

## Summary

The `fitting_coefficients.py` module serves as the authoritative source for fitting loss coefficients used throughout the Hydraulic Analysis Suite.

By centralizing minor loss data, the project promotes consistency, maintainability, and scalability while supporting future hydraulic analyses involving valves, bends, tees, transitions, and other pipe system components.
