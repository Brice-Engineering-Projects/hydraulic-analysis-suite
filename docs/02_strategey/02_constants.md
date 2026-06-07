# constants.py

## Purpose

The `constants.py` module serves as the centralized repository for engineering constants, physical constants, unit conversion factors, and commonly used numerical values utilized throughout the Hydraulic Analysis Suite.

The purpose of this module is to eliminate hard-coded values within equation classes, calculators, and engineering models while providing a single source of truth for commonly used constants.

Centralizing these values improves consistency, maintainability, readability, and verification of engineering calculations.

---

## Responsibilities

The module is responsible for:

* Storing engineering constants.
* Storing physical constants.
* Storing unit conversion factors.
* Storing application-wide numerical constants.
* Eliminating duplicate values throughout the codebase.
* Supporting future hydraulic calculations and engineering workflows.

---

## Design Philosophy

Engineering equations frequently rely on constants that are used repeatedly throughout the application.

Rather than embedding these values directly within equation classes:

```python
velocity = flow_rate * 0.002228
```

the value should be referenced from a centralized source:

```python
velocity = flow_rate * GPM_TO_CFS
```

This improves readability and makes the origin of numerical values easier to verify.

---

## Constants Categories

### Unit Conversion Factors

Examples include:

* Gallons per Minute to Cubic Feet per Second
* Inches to Feet
* Feet to Miles
* Horsepower to Kilowatts
* Kilowatts to Horsepower

Example:

```python
GPM_TO_CFS = 0.002228

INCHES_PER_FOOT = 12

FEET_PER_MILE = 5280

HP_TO_KW = 0.746

KW_TO_HP = 1.341
```

---

### Physical Constants

Examples include:

* Acceleration due to gravity
* Water density
* Water specific weight

Example:

```python
GRAVITY_FTPS2 = 32.174

WATER_DENSITY_LBFT3 = 62.4

WATER_UNIT_WEIGHT_LBFT3 = 62.4
```

---

### Mathematical Constants

Where appropriate:

```python
PI = 3.141592653589793
```

Although most mathematical constants should generally be obtained from Python's standard library.

---

### Hydraulic Constants

Frequently used values that appear in hydraulic calculations.

Examples may include:

```python
HAZEN_WILLIAMS_US_COEFFICIENT = 4.727
```

or other equation-specific coefficients that remain constant across calculations.

---

## What Does NOT Belong Here

The following should not be stored in `constants.py`:

### Pipe Material Properties

These belong in:

```text
pipe_materials.py
```

Examples:

```python
PVC

HDPE

DIP_NEW
```

because these are material properties rather than engineering constants.

---

### Fitting Loss Coefficients

These belong in:

```text
fitting_coefficients.py
```

Examples:

```python
90_ELBOW

45_ELBOW

TEE

CHECK_VALVE
```

because these represent component characteristics rather than universal constants.

---

### User Inputs

Examples:

```python
flow_rate

diameter

length
```

should never be stored as constants.

---

## Relationship to Other Modules

The constants module supports:

* Pipe Class
* Hazen-Williams Equation
* Darcy-Weisbach Equation
* Manning Equation
* Minor Loss Calculations
* TDH Calculator
* Force Main Calculator
* System Curve Calculator
* Pump Selection Calculator

and future engineering analysis modules.

---

## Example Future Structure

```python
# Unit Conversions

GPM_TO_CFS = 0.002228

INCHES_PER_FOOT = 12

FEET_PER_MILE = 5280

HP_TO_KW = 0.746

# Physical Constants

GRAVITY_FTPS2 = 32.174

WATER_DENSITY_LBFT3 = 62.4

# Hydraulic Constants

HAZEN_WILLIAMS_US_COEFFICIENT = 4.727
```

---

## Summary

The `constants.py` module provides a centralized location for engineering constants, physical constants, and unit conversion factors used throughout the Hydraulic Analysis Suite.

By separating constants from equation implementations and engineering models, the project becomes easier to maintain, verify, and expand while promoting consistency across all hydraulic calculations.
