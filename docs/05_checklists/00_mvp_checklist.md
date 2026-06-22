# MVP Checklist — Hydraulic Analysis Suite v1.0

## Purpose

This checklist tracks all tasks required to deliver a Minimum Viable Product (MVP) of the Hydraulic Analysis Suite.

The MVP is considered complete when the application can accurately calculate:

- Flow Velocity
- Pipe Cross-Sectional Area and Volume
- Friction Headloss (Hazen-Williams and Darcy-Weisbach)
- Minor Losses
- Total Dynamic Head (TDH)

The application must accept user inputs from the command line and produce formatted engineering output.

---

## Current Status Summary

| Area | Status |
|---|---|
| Pipe Model | Complete |
| Fitting Model | Partial |
| Pipe Materials Database | Complete |
| Fittings Database | Complete |
| Engineering Constants | Complete |
| Hazen-Williams Equation | Not Started |
| Darcy-Weisbach Equation | Not Started |
| Minor Loss Equation | Not Started |
| Friction Loss Calculator | Not Started |
| TDH Calculator | Not Started |
| CLI / User Input | Stub Only |
| Main Entry Point | Placeholder Only |
| Integration Tests | Not Started |

---

## Phase 1 — Complete Core Models

### 1.1 Fitting Class (`models/fitting.py`)

The Fitting class requires completion before the minor loss calculator can be built.

- [ ] Add `_lookup_fitting_data()` method to retrieve full fitting record from `fittings_data.py`
- [ ] Add `fitting_category` derived property (from database lookup)
- [ ] Add `k_factor` derived property (from database lookup)
- [ ] Add `equivalent_length_ratio` derived property (from database lookup)
- [ ] Add `source` derived property (engineering reference source)
- [ ] Add `source_reference` derived property (specific table, page, or section)
- [ ] Add `engineering_notes` derived property (assumptions and limitations)
- [ ] Add `diameter_ft` computed property (convert `diameter_in` to feet)
- [ ] Add `equivalent_length_ft` computed property (`equivalent_length_ratio × diameter_ft`)
- [ ] Add `total_equivalent_length_ft` computed property (`equivalent_length_ft × quantity`)
- [ ] Add `description` property (human-readable fitting summary string)
- [ ] Add `_validate_fitting_name()` method (check name exists in database)
- [ ] Add `_validate_diameter()` method (check diameter > 0)
- [ ] Add `_validate_quantity()` method (check quantity > 0)
- [ ] Refactor `_validate_data()` to call the three individual validators above
- [ ] Add `summary()` method (formatted multi-line engineering summary output)
- [ ] Update `__str__()` to return a concise single-line description
- [ ] Update `__repr__()` to return a developer-readable representation

### 1.2 Fitting Model Tests (`tests/models/test_fitting.py`)

- [ ] Test valid fitting creation with all required attributes
- [ ] Test `_validate_fitting_name()` raises error for unrecognized fitting name
- [ ] Test `_validate_diameter()` raises error for diameter ≤ 0
- [ ] Test `_validate_quantity()` raises error for quantity ≤ 0
- [ ] Test `k_factor` returns correct value from database
- [ ] Test `equivalent_length_ratio` returns correct value from database
- [ ] Test `equivalent_length_ft` computes correctly
- [ ] Test `total_equivalent_length_ft` scales correctly with quantity
- [ ] Test `fitting_category` returns correct category string
- [ ] Test `source` and `source_reference` return correct engineering references
- [ ] Test `engineering_notes` returns correct notes
- [ ] Test `summary()` returns a non-empty formatted string
- [ ] Test `__str__()` returns a single-line string
- [ ] Test `__repr__()` returns a valid developer string

### 1.3 Pump Model (`models/pump.py`)

- [ ] Create `pump.py` file in `models/`
- [ ] Define `Pump` class with constructor
- [ ] Add `pump_name` attribute (str)
- [ ] Add `design_flow_gpm` attribute (float)
- [ ] Add `design_head_ft` attribute (float)
- [ ] Add `efficiency` attribute (float, 0–1)
- [ ] Add `horsepower` attribute (float)
- [ ] Add `_validate_data()` method
- [ ] Add `__str__()` and `__repr__()` methods
- [ ] Add `summary()` method
- [ ] Write unit tests in `tests/models/test_pump.py`

---

## Phase 2 — Equation Modules

All equation functions must:
- Accept typed inputs
- Perform calculations
- Return results
- Not request user input, print output, or create objects

### 2.1 Hazen-Williams Equation (`equations/hazen_williams.py`)

- [ ] Implement `headloss(flow_rate_gpm, diameter_in, length_ft, c_factor)` function
  - Returns friction headloss in feet using Hazen-Williams formula
  - Formula: `hf = 4.727 × L × Q^1.852 / (C^1.852 × d^4.871)`
- [ ] Implement `headloss_per_1000ft(flow_rate_gpm, diameter_in, c_factor)` function
  - Returns headloss per 1,000 feet in ft/1000 ft
- [ ] Implement `velocity(flow_rate_gpm, diameter_in)` function
  - Returns average flow velocity in fps
- [ ] Add docstrings with formula references, units, and variable definitions
- [ ] Use constants from `constants.py` (no hard-coded numerical values)

### 2.2 Hazen-Williams Tests (`tests/equations/test_hazen_williams.py`)

- [ ] Create `tests/equations/` directory with `__init__.py`
- [ ] Create `test_hazen_williams.py`
- [ ] Test `headloss()` against a known hand-calculated result
- [ ] Test `headloss_per_1000ft()` against a known hand-calculated result
- [ ] Test `velocity()` against a known hand-calculated result
- [ ] Test that zero flow rate returns zero headloss
- [ ] Test that invalid inputs raise appropriate errors

### 2.3 Darcy-Weisbach Equation (`equations/darcy_weisbach.py`)

- [ ] Implement `reynolds_number(velocity_fps, diameter_ft, kinematic_viscosity)` function
  - Returns dimensionless Reynolds number
- [ ] Implement `friction_factor(reynolds_number, roughness_ft, diameter_ft)` function
  - Returns Darcy-Weisbach friction factor (f)
  - Use Colebrook-White or Swamee-Jain approximation
- [ ] Implement `headloss(friction_factor, length_ft, diameter_ft, velocity_fps)` function
  - Returns friction headloss in feet using Darcy-Weisbach formula
  - Formula: `hf = f × (L / D) × (V² / 2g)`
- [ ] Add docstrings with formula references, units, and variable definitions
- [ ] Use constants from `constants.py` (gravity, kinematic viscosity)

### 2.4 Darcy-Weisbach Tests (`tests/equations/test_darcy_weisbach.py`)

- [ ] Test `reynolds_number()` against a known result
- [ ] Test `friction_factor()` in fully turbulent flow regime
- [ ] Test `friction_factor()` in laminar flow regime (f = 64/Re)
- [ ] Test `headloss()` against a known hand-calculated result
- [ ] Test that zero velocity returns zero headloss

### 2.5 Minor Loss Equation (`equations/minor_losses.py`)

- [ ] Implement `headloss(k_factor, velocity_fps)` function
  - Returns minor headloss in feet
  - Formula: `hm = K × V² / 2g`
- [ ] Implement `total_headloss(fittings, velocity_fps)` function
  - Accepts a list of `Fitting` objects
  - Returns total minor headloss for all fittings
- [ ] Add docstrings with formula references, units, and variable definitions
- [ ] Use `GRAVITY_FTPS2` from `constants.py`

### 2.6 Minor Loss Tests (`tests/equations/test_minor_losses.py`)

- [ ] Test `headloss()` against a known hand-calculated result
- [ ] Test `total_headloss()` with multiple fittings
- [ ] Test that zero velocity returns zero headloss
- [ ] Test that zero K-factor returns zero headloss

---

## Phase 3 — Calculators

Calculators combine models and equations into engineering tools. They should not interact with users directly.

### 3.1 Friction Loss Calculator (`calculators/friction_loss.py`)

- [ ] Create `calculators/` directory with `__init__.py` if not present
- [ ] Create `friction_loss.py`
- [ ] Implement `FrictionLossCalculator` class (or equivalent functions)
- [ ] Accept a `Pipe` object as input
- [ ] Run Hazen-Williams calculation
- [ ] Run Darcy-Weisbach calculation
- [ ] Return structured results dictionary:
  ```json
  {
    "method": "Hazen-Williams",
    "headloss_ft": value,
    "headloss_per_1000ft": value,
    "velocity_fps": value
  }
  ```
- [ ] Return results for both methods (HW and DW) for comparison
- [ ] Add docstrings describing inputs, outputs, and calculation approach

### 3.2 Friction Loss Calculator Tests (`tests/calculators/test_friction_loss.py`)

- [ ] Create `tests/calculators/` directory with `__init__.py`
- [ ] Create `test_friction_loss.py`
- [ ] Test calculator accepts a valid `Pipe` object
- [ ] Test Hazen-Williams result matches expected value
- [ ] Test Darcy-Weisbach result matches expected value
- [ ] Test that result keys are present in output

### 3.3 TDH Calculator (`calculators/tdh_calculator.py`)

- [ ] Create `tdh_calculator.py` in `calculators/`
- [ ] Implement `TDHCalculator` class (or equivalent functions)
- [ ] Accept inputs: `Pipe`, `static_head_ft`, list of `Fitting` objects
- [ ] Calculate `friction_head_ft` using Hazen-Williams
- [ ] Calculate `minor_loss_head_ft` using minor losses equation
- [ ] Calculate `velocity_head_ft` = V² / 2g
- [ ] Calculate `tdh_ft` = static_head + friction_head + minor_loss_head + velocity_head
- [ ] Return structured results dictionary:
  ```json
  {
    "static_head_ft": value,
    "friction_head_ft": value,
    "minor_loss_head_ft": value,
    "velocity_head_ft": value,
    "tdh_ft": value
  }
  ```
- [ ] Add docstrings describing inputs, outputs, and calculation approach

### 3.4 TDH Calculator Tests (`tests/calculators/test_tdh_calculator.py`)

- [ ] Test TDH calculator with a known hand-calculated result
- [ ] Test TDH with no minor losses (fittings list is empty)
- [ ] Test TDH with zero static head
- [ ] Test that all result keys are present in output
- [ ] Test that TDH equals the sum of component heads

---

## Phase 4 — CLI and Entry Point

### 4.1 User Input Module (`cli/user_input.py`)

- [ ] Implement `collect_pipe_data()` function
  - Prompt for flow rate (gpm)
  - Prompt for pipe diameter (in)
  - Prompt for pipe length (ft)
  - Prompt for pipe material (display available options)
  - Validate all inputs before returning
  - Return a `Pipe` object
- [ ] Implement `collect_static_head()` function
  - Prompt user for static head (ft)
  - Validate input is a positive number
  - Return float
- [ ] Implement `collect_fittings()` function
  - Allow user to add fittings from available fitting names
  - Allow user to specify quantity for each fitting
  - Return a list of `Fitting` objects
- [ ] Implement `display_material_menu()` helper function
  - Print available pipe materials from `pipe_materials.py`
- [ ] Implement `display_fitting_menu()` helper function
  - Print available fitting names from `fittings_data.py`
- [ ] Add input validation with clear error messages for all inputs
- [ ] Support re-prompting on invalid entries (do not crash)

### 4.2 Results Display (`cli/display.py` or within `user_input.py`)

- [ ] Implement `display_pipe_summary(pipe)` function
  - Print Pipe object summary in formatted table
- [ ] Implement `display_friction_loss_results(results)` function
  - Print Hazen-Williams and Darcy-Weisbach results side by side
- [ ] Implement `display_tdh_results(results)` function
  - Print TDH breakdown with labeled components and total
- [ ] All output must include units with each value

### 4.3 Main Entry Point (`main.py`)

- [ ] Import CLI input and display functions
- [ ] Import Friction Loss Calculator
- [ ] Import TDH Calculator
- [ ] Implement main workflow:
  1. Collect pipe data → create `Pipe` object
  2. Collect static head
  3. Collect fittings → create list of `Fitting` objects
  4. Run Friction Loss Calculator
  5. Run TDH Calculator
  6. Display Pipe Summary
  7. Display Friction Loss Results
  8. Display TDH Results
- [ ] Wrap main logic in `if __name__ == "__main__"` block

---

## Phase 5 — Integration and Verification

### 5.1 End-to-End Verification

- [ ] Manually run the application with a known design scenario
- [ ] Verify velocity output matches a hand calculation
- [ ] Verify Hazen-Williams headloss matches a hand calculation
- [ ] Verify Darcy-Weisbach headloss matches a hand calculation
- [ ] Verify minor losses match a hand calculation
- [ ] Verify TDH matches a hand calculation

**Example verification scenario:**

```text
Flow Rate: 500 gpm
Pipe: 8-inch PVC
Length: 1,000 ft
Static Head: 25 ft
Fittings: 2 × 90° Standard Radius Bend, 1 × Gate Valve (Fully Open)
```

### 5.2 Package and Installation

- [ ] Confirm `pyproject.toml` entry point is correctly configured for CLI execution
- [ ] Confirm application runs with `python main.py` or `has-cli` command
- [ ] Confirm all modules are importable from `hydraulic_analysis_suite` package
- [ ] Confirm all existing tests pass: `pytest tests/`
- [ ] Confirm no orphaned imports or unused modules

---

## Phase 6 — Engineering Validation

Engineering validation confirms that calculated results are accurate and consistent with recognized industry tools and references. This phase is distinct from software testing — it verifies that the engineering is correct, not just that the code runs.

### 6.1 Hand Calculation Verification

Hand calculations serve as the primary baseline. Results must match within an acceptable engineering tolerance (≤ 1% for friction loss, ≤ 2% for TDH).

**Scenario A — Basic Friction Loss**

```text
Flow Rate:  500 gpm
Pipe:       8-inch PVC (C = 150)
Length:     1,000 ft
```

- [ ] Calculate velocity by hand and compare to application output
- [ ] Calculate Hazen-Williams headloss by hand and compare to application output
- [ ] Calculate Darcy-Weisbach headloss by hand and compare to application output
- [ ] Document results in a verification table

**Scenario B — TDH with Minor Losses**

```text
Flow Rate:  500 gpm
Pipe:       8-inch PVC (C = 150)
Length:     1,000 ft
Static Head: 25 ft
Fittings:   2 × 90° Standard Radius Bend, 1 × Gate Valve (Fully Open)
```

- [ ] Calculate minor losses by hand (K × V²/2g for each fitting) and compare to application output
- [ ] Calculate TDH by hand (static + friction + minor + velocity head) and compare to application output
- [ ] Document results in a verification table

**Scenario C — Low Flow / Small Diameter**

```text
Flow Rate:  50 gpm
Pipe:       4-inch DIP (New)
Length:     500 ft
```

- [ ] Verify Hazen-Williams headloss matches hand calculation
- [ ] Verify Darcy-Weisbach friction factor is reasonable (check against Moody chart)
- [ ] Document results in a verification table

**Scenario D — High Flow / Large Diameter**

```text
Flow Rate:  2,500 gpm
Pipe:       16-inch DIP (New)
Length:     5,000 ft
```

- [ ] Verify Hazen-Williams headloss matches hand calculation
- [ ] Verify velocity is within a typical design range (2–8 fps)
- [ ] Document results in a verification table

---

### 6.2 Comparison Against EPA Reference Spreadsheets

The EPA publishes hydraulic design tools and technical guidance used in water and wastewater engineering practice.

- [ ] Identify a relevant EPA friction loss or hydraulic design spreadsheet (e.g., from the EPA SWMM documentation or WaterSense technical resources)
- [ ] Run the same input scenario through the EPA tool and the application
- [ ] Record both results side-by-side
- [ ] Document any discrepancies and identify root cause (formula variation, unit difference, assumption difference)
- [ ] Confirm results agree within acceptable engineering tolerance

---

### 6.3 Comparison Against Bentley WaterGEMS or WaterCAD

WaterGEMS and WaterCAD are industry-standard hydraulic modeling platforms used in water distribution and force main design. Matching output from these tools demonstrates that the application produces credible engineering results.

- [ ] Set up an equivalent pipe segment in WaterGEMS or WaterCAD matching a verification scenario
- [ ] Run steady-state hydraulic analysis
- [ ] Record headloss, velocity, and pressure results from WaterGEMS/WaterCAD
- [ ] Run the same scenario through the application
- [ ] Compare results in a side-by-side table
- [ ] Document any discrepancies and identify root cause
- [ ] Confirm Hazen-Williams results agree within acceptable engineering tolerance
- [ ] Confirm Darcy-Weisbach results agree within acceptable engineering tolerance

---

### 6.4 Comparison Against Utility Design Examples

Utility design standards and engineering manuals often include worked examples that can serve as independent validation benchmarks.

- [ ] Identify at least one worked example from a recognized reference:
  - Pumping Station Design (3rd Edition) — Sanks et al.
  - AWWA M11, M23, or M41 design examples
  - Hydraulic Institute Engineering Data Book
  - Cameron Hydraulic Data worked examples
  - WEF Manual of Practice No. 8 or MOP 11
- [ ] Reproduce the worked example inputs in the application
- [ ] Compare application output to the published solution
- [ ] Document the reference, inputs, expected output, and actual output
- [ ] Note any formula or assumption differences between the reference and the application

---

### 6.5 Validation Documentation

All validation results must be captured and stored for traceability.

- [ ] Create a `docs/06_validation/` directory
- [ ] Create `docs/06_validation/00_validation_summary.md` with:
  - Summary table of all validation scenarios
  - Pass/Fail status for each comparison
  - Reference sources used
  - Acceptable tolerance criteria
- [ ] Create one validation record per scenario (e.g., `01_hand_calc_scenario_a.md`)
  - Input parameters
  - Expected result (from reference)
  - Application result
  - Difference (absolute and percent)
  - Pass/Fail determination
  - Notes on any assumptions or discrepancies
- [ ] Update the validation summary table after each scenario is completed

---

## Phase 7 — Documentation

### 7.1 README

- [ ] Update `README.md` to reflect current project state
- [ ] Add installation instructions
- [ ] Add usage example with sample inputs and expected outputs
- [ ] List all currently supported pipe materials
- [ ] List all currently supported fittings

### 7.2 Inline Documentation

- [ ] Confirm all public functions in equation modules have docstrings
- [ ] Confirm all public classes in model modules have docstrings
- [ ] Confirm all calculator classes have docstrings describing inputs and outputs

---

## MVP Completion Criteria

The MVP is complete when all of the following are true:

- [ ] A user can run the application from the command line
- [ ] The application accepts pipe material, dimensions, flow rate, static head, and fittings as inputs
- [ ] The application calculates and displays velocity, friction headloss (both methods), minor losses, and TDH
- [ ] All calculations have been verified against hand calculations (Phase 6.1)
- [ ] Results have been compared against at least one industry tool (WaterGEMS or EPA reference) (Phase 6.2–6.3)
- [ ] At least one utility design example has been reproduced and validated (Phase 6.4)
- [ ] Validation records have been documented in `docs/06_validation/` (Phase 6.5)
- [ ] All unit tests pass
- [ ] No empty module files remain

---

## Out of Scope for MVP

The following items are explicitly deferred to later versions:

- Pump curve analysis and operating point calculation
- Wet well sizing and pump cycling analysis
- Force main / multi-segment pipeline modeling
- System curve generation
- PDF or CSV report export
- Streamlit or web interface
- GUI
- Database backend
- Cloud infrastructure
- AI features
