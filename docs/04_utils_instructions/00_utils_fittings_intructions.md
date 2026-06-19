# Fitting Data Helper Utility

## Overview

The fitting data helper utility provides two capabilities:

1. **Calculation traceability** — documents how hydraulic values in `fittings_data.py` were derived.
2. **Database verification** — checks that values in `fittings_data.py` have not been accidentally changed.

---

## Files

| File | Role |
| ---- | ---- |
| `src/utils/fitting_data_helper_calcs.py` | Derivation calculations and verification function |
| `src/data/fittings_data.py` | The fitting database being supported |

---

## How to Run the Verification

From the project root directory:

```bash
python -m src.utils.fitting_data_helper_calcs
```

No arguments are required. The verification runs automatically when the module is executed directly.

---

## What the Verification Checks

The verifier checks **13 Crane-derived fittings** — those whose Le/D values come directly from Crane TP-410 Table A-29 or are interpolated from it.

For each fitting, two values are checked:

| Field | Check Type | Basis |
| ----- | ---------- | ----- |
| `equivalent_length_ratio` (Le/D) | Exact match | Crane TP-410 Table A-29 (tabulated or interpolated) |
| `k_factor` | Exact match | Intentionally rounded representative values from fixed-K textbook references |

---

## What the Verification Does Not Check

The following fittings are **not verified** because their values are representative engineering estimates with no computable derivation basis:

* Tee — combining flow
* Wye — standard and combination
* Butterfly valve
* Ball check valve
* Concentric and eccentric reducers
* Concentric and eccentric expansions
* Venturi, magnetic, and turbine meters

Changes to these values require manual engineering review rather than automated verification.

---

## Reading the Output

### All Checks Pass

```
========================================================================
  FITTINGS DATABASE VERIFICATION REPORT
========================================================================
  Checking 13 Crane-derived fittings
  Le/D source : Crane TP-410 Table A-29 (tabulated or interpolated)
  K source    : Fixed-K textbook reference values (intentionally rounded)
------------------------------------------------------------------------
  PASS  11_25_deg_bend_standard_radius
        Le/D = 4 ✓    K = 0.10 ✓
  PASS  90_deg_bend_standard_radius
        Le/D = 30 ✓    K = 0.75 ✓
  ...
------------------------------------------------------------------------
  13 fittings checked   13 passed   0 failed
========================================================================
```

No action required.

---

### A Check Fails

```
  FAIL  swing_check_valve
        Le/D = 100 ✗  (expected 135)    K = 2.30 ✓

------------------------------------------------------------------------
  13 fittings checked   12 passed   1 failed
========================================================================

  ACTION REQUIRED: One or more database values do not match
  the expected values recorded in this file.
  Review fittings_data.py and update either the data or the
  expected values in _CRANE_DERIVED_CHECKS with engineering
  justification.
```

A failure means a stored value in `fittings_data.py` does not match the expected value recorded in `_CRANE_DERIVED_CHECKS`. This requires engineering review.

---

## How to Respond to a Failure

A FAIL result has two possible causes:

### Cause 1 — Accidental Edit

The value in `fittings_data.py` was changed without engineering justification.

**Action:** Restore the original value in `fittings_data.py` and re-run verification.

---

### Cause 2 — Intentional Change

The value in `fittings_data.py` was intentionally updated based on a new engineering reference or revised judgment.

**Action:** Update `_CRANE_DERIVED_CHECKS` in `fitting_data_helper_calcs.py` to match the new value. Include a comment documenting the reason for the change and the supporting reference.

Example:

```python
"swing_check_valve": {
    "le_d_source": "Crane TP-410 Table A-29",
    "expected_le_d": 135,   # Updated from 100 — corrected to Table A-29 value
    "expected_k": 2.30,
},
```

Never update `_CRANE_DERIVED_CHECKS` without also updating the corresponding entry in `fittings_data.py` and documenting the engineering basis.

---

## When to Run the Verification

### Minimum Recommended Frequency

| Trigger | Run Verification |
| ------- | ---------------- |
| After any edit to `fittings_data.py` | Always |
| After any edit to `fitting_data_helper_calcs.py` | Always |
| Before committing changes to the database | Always |
| During peer review of hydraulic database changes | Always |
| At the start of a new design phase | Recommended |
| Quarterly during active development | Recommended |

---

### Priority Situations

Run immediately if:

* A fitting value in `fittings_data.py` was edited and the change was not reviewed by a licensed engineer.
* A merge conflict was resolved in `fittings_data.py`.
* A new fitting was added and surrounding entries may have been disturbed.
* Any refactoring touched the `src/data/` directory.

---

## How to Use the Verification in Tests

The `verify_database_values()` function returns `True` if all checks pass and `False` if any fail. It can be called from the test suite:

```python
from src.utils.fitting_data_helper_calcs import verify_database_values

def test_fittings_database_integrity():
    assert verify_database_values(), (
        "One or more Crane-derived values in fittings_data.py do not match "
        "the expected values in fitting_data_helper_calcs.py."
    )
```

Adding this test to the test suite provides automatic verification on every test run.

---

## How to Add a New Fitting to Verification

When a new Crane-derived fitting is added to `fittings_data.py`:

1. Add the fitting to `_CRANE_DERIVED_CHECKS` in `fitting_data_helper_calcs.py`.
2. Document the Le/D source (`"Crane TP-410 Table A-29"` or `"Interpolated from Table A-29"`).
3. Record the expected Le/D and K values.
4. Run verification to confirm the new entry passes.
5. Add the corresponding derivation calculation to the K-factor derivation section of the helper file.

If the new fitting is not Crane-derived (representative values from Hydraulic Institute, Pumping Station Design, or similar), it does not need to be added to `_CRANE_DERIVED_CHECKS`. Document its source in the `source` and `source_reference` fields of the database entry.

---

## Engineering Traceability Notes

The verification function enforces traceability between two documents:

```
fittings_data.py                   ←→    fitting_data_helper_calcs.py
(stores the values used at runtime)       (documents how values were derived)
```

If these two files ever disagree, the verification will fail. This is the intended behavior.

The verification does not perform hydraulic calculations — it only confirms that stored values match expected values. Hydraulic correctness is the responsibility of the engineer who sourced or derived the values.

---

## Summary

| Task | How |
| ---- | --- |
| Run verification | `python -m src.utils.fitting_data_helper_calcs` |
| Integrate with tests | Call `verify_database_values()` and assert return value |
| Respond to FAIL — accidental edit | Restore value in `fittings_data.py` |
| Respond to FAIL — intentional change | Update `_CRANE_DERIVED_CHECKS` with engineering justification |
| Add new Crane fitting to verification | Add entry to `_CRANE_DERIVED_CHECKS` and derivation section |
| Add non-Crane fitting | Document source in `fittings_data.py` only — no verification entry needed |
