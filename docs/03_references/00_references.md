# Engineering References

## Purpose

This document catalogues the authoritative engineering references used throughout the Hydraulic Analysis Suite.

All hydraulic coefficients, material properties, and design values stored within the application database shall be traceable to one or more of the references listed here. No engineering value shall exist within the application without an identifiable source.

This document supports:

* QA/QC review
* Peer review
* Design documentation
* Regulatory review
* Future database maintenance and expansion
* Verification of assumptions and limitations

---

## Reference Categories

* [Standards](#standards)
* [Industry References](#industry-references)
* [Textbooks and Handbooks](#textbooks-and-handbooks)
* [Application Usage by Module](#application-usage-by-module)
* [Methodology Notes](#methodology-notes)

---

## Edition Verification Note

Entries marked **[VERIFY EDITION]** contain bibliographic details that could not be confirmed with certainty at the time of writing. Before using this document for design, QA/QC, or regulatory submittals, confirm the edition, year, and publisher against the physical copy in use and update accordingly.

The engineer of record is responsible for documenting the specific edition of each reference used in final design calculations.

---

## Standards

### AWWA Manual M11 — Steel Pipe

**Full Title:** Steel Pipe: A Guide for Design and Installation

**Issuing Organization:** American Water Works Association (AWWA)

**Publisher:** American Water Works Association, Denver, CO

**Edition:** **[VERIFY EDITION]** — AWWA manuals are periodically revised. Confirm edition number and publication year against the copy in use.

**Application within this project:**

* Steel pipe hydraulic properties
* Fitting minor loss guidance for steel pipe systems
* Engineering notes for pressure pipe design

---

### AWWA Manual M23 — PVC Pipe

**Full Title:** PVC Pipe: Design and Installation

**Issuing Organization:** American Water Works Association (AWWA)

**Publisher:** American Water Works Association, Denver, CO

**Edition:** **[VERIFY EDITION]** — AWWA manuals are periodically revised. Confirm edition number and publication year against the copy in use.

**Application within this project:**

* PVC pipe hydraulic properties
* Fitting minor loss guidance for PVC pipe systems
* Engineering notes for pressure pipe design

---

### AWWA Manual M41 — Ductile-Iron Pipe

**Full Title:** Ductile-Iron Pipe and Fittings

**Issuing Organization:** American Water Works Association (AWWA)

**Publisher:** American Water Works Association, Denver, CO

**Edition:** **[VERIFY EDITION]** — AWWA manuals are periodically revised. Confirm edition number and publication year against the copy in use.

**Application within this project:**

* Ductile iron pipe hydraulic properties
* Fitting minor loss guidance for ductile iron pipe systems
* Engineering notes for pressure pipe design

---

## Industry References

### Crane Technical Paper No. 410 (TP-410)

**Full Title:** Flow of Fluids Through Valves, Fittings, and Pipe

**Issuing Organization:** Crane Co., Stamford, CT

**Common Reference:** Crane TP-410

**Publication History:**

Crane TP-410 is a technical paper, not a book issued in numbered editions. It has been continuously updated by Crane Co. since its original publication in 1942. Because it is not versioned by edition number, the specific printing or revision year in use should be documented by the engineer of record.

The engineer of record should record the printing year of the copy used for design calculations in the project calculation package.

**Application within this project:**

* Equivalent length ratios (Le/D) for common fittings and valves
* Minor loss coefficient (K-factor) methodology
* Contraction and enlargement loss guidance
* Gate valve, plug valve, and swing check valve resistance data
* Standard and long radius elbow resistance data
* Tee resistance data (through run and branch flow)

**Key Tables Referenced:**

| Table | Content |
| ----- | ------- |
| Table A-29 | Equivalent Length of Fittings — primary source for Le/D values |

**Methodology Note:**

Crane TP-410 defines the resistance coefficient K as:

```text
K = f_T × (Le/D)
```

where `f_T` is the Darcy-Weisbach friction factor for fully turbulent flow in clean commercial steel pipe, which varies by pipe diameter. Crane TP-410 does not publish fixed K-factor values independent of pipe size.

K-factor values stored in `fittings_data.py` are representative values appropriate for mid-range water and wastewater pipe diameters (approximately 4-inch to 24-inch). For diameter-specific analysis, K shall be computed as:

```text
K = f_T × (Le/D)
```

using the pipe-diameter-appropriate f_T value per Crane TP-410.

---

### Hydraulic Institute Engineering Data Book

**Full Title:** Engineering Data Book

**Issuing Organization:** Hydraulic Institute

**Publisher:** Hydraulic Institute, Parsippany, NJ

**Edition:** **[VERIFY EDITION]** — Confirm edition number and publication year against the copy in use.

**Application within this project:**

* Butterfly valve resistance data
* Combining tee minor loss coefficients
* Flow meter resistance data (venturi, magnetic, turbine)
* Valve minor loss reference data

---

### Cameron Hydraulic Data

**Full Title:** Cameron Hydraulic Data

**Publication History:**

Originally published by the Cameron Pump Division of Ingersoll-Rand. Subsequently published by Ingersoll-Dresser Pumps, and later by Flowserve Corporation. The publication has been revised over multiple editions across several decades. Ownership and publisher name have changed with corporate acquisitions.

**Current Publisher:** Flowserve Corporation

**Edition:** **[VERIFY EDITION]** — Multiple editions exist under different publisher names. Confirm edition number, publication year, and publisher against the copy in use.

**Application within this project:**

* Supplemental fitting resistance data
* Pipe material hydraulic properties
* General hydraulic reference

---

## Textbooks and Handbooks

### Pumping Station Design — Third Edition

**Full Title:** Pumping Station Design

**Edition:** Third Edition

**Editor:** Robert L. Sanks

**Publisher:** Butterworth-Heinemann (an imprint of Elsevier)

**Year:** 1998 **[VERIFY YEAR]** — Confirm publication year against the copy in use.

**Application within this project:**

* Check valve minor loss data (swing check, ball check)
* Wye fitting minor loss data
* General minor loss references for pump station components
* Pipe material properties for pump station applications

---

### MWH Water Distribution Systems Handbook

**Full Title:** Water Distribution Systems Handbook

**Editor:** Larry W. Mays **[VERIFY EDITOR]**

**Organization:** MWH Global (Montgomery Watson Harza)

**Publisher:** McGraw-Hill

**Edition:** **[VERIFY EDITION]** — Confirm edition number and publication year against the copy in use.

**Application within this project:**

* Pipe material properties
* Fitting minor loss guidance
* General hydraulic reference for water distribution applications

---

### MWH Water Treatment: Principles and Design

**Full Title:** Water Treatment: Principles and Design

**Organization:** MWH Global (Montgomery Watson Harza)

**Publisher:** John Wiley & Sons

**Edition:** Second Edition **[VERIFY EDITION]** — A second edition exists; confirm edition number and publication year against the copy in use.

**Year:** approximately 2005 **[VERIFY YEAR]**

**Application within this project:**

* Pipe material properties
* Hydraulic design guidance
* General reference for water treatment system hydraulics

---

## Application Usage by Module

The table below identifies which references apply to each application module.

| Module | Primary References |
| ------ | ------------------ |
| `src/data/pipe_materials.py` | Crane TP-410, Hydraulic Institute, AWWA M11, M23, M41, Cameron Hydraulic Data, MWH Handbooks |
| `src/data/fittings_data.py` | Crane TP-410, Hydraulic Institute, Cameron Hydraulic Data, Pumping Station Design |
| `src/models/pipe.py` | AWWA M11, M23, M41, Hydraulic Institute |
| `src/models/fitting.py` | Crane TP-410, Hydraulic Institute, AWWA M11, M23, M41 |

---

## Methodology Notes

### Equivalent Length Method

The equivalent length method represents fitting losses as an equivalent length of straight pipe producing the same head loss:

```text
Le = (Le/D) × D
```

where:

* `Le` = equivalent pipe length (ft)
* `Le/D` = equivalent length ratio (dimensionless), sourced from Crane TP-410 Table A-29
* `D` = internal pipe diameter (ft)

The equivalent length method is compatible with both the Hazen-Williams and Darcy-Weisbach friction loss equations and is the primary method used in this application.

---

### K-Factor Method

The K-factor method computes minor head loss directly from velocity head:

```text
h_L = K × (V² / 2g)
```

where:

* `h_L` = minor head loss (ft)
* `K` = dimensionless loss coefficient
* `V` = flow velocity (fps)
* `g` = gravitational acceleration (32.174 ft/s²)

Per Crane TP-410, K is calculated as:

```text
K = f_T × (Le/D)
```

K-factor values stored in this application are representative values for mid-range pipe diameters. Diameter-specific values should be computed using the above relationship with the appropriate f_T for the pipe size.

---

### Interpolated Values

Some fitting entries in `fittings_data.py` contain Le/D values interpolated from tabulated data rather than directly extracted from a published table. These entries are identified by the note `"Table A-29, interpolated"` in the `source_reference` field.

Interpolated entries include:

* 11.25-degree bends (standard and long radius)
* 22.5-degree bends (standard and long radius)

These values are interpolated from the 45-degree and 90-degree elbow tabulated values in Crane TP-410 Table A-29.

---

### Geometry-Dependent Fittings

Reducer and expansion (enlargement) loss coefficients depend on fitting geometry, specifically the diameter ratio (D₂/D₁) and taper angle. The values stored in `fittings_data.py` for these fitting types represent typical gradual fittings and are appropriate for preliminary design.

For final design, refer to Crane TP-410 for geometry-specific loss coefficients.

---

### Check Valve and Specialty Valve Notes

Check valve and specialty valve resistance values vary significantly with:

* Flow velocity
* Valve size
* Manufacturer
* Installation configuration

Values stored in this application represent typical design conditions for properly sized valves at normal operating velocities. Manufacturer data should be consulted for final design.

---

### Flow Meter Notes

Flow meter resistance values vary significantly with:

* Meter type and manufacturer
* Pipe size and installation
* Beta ratio (venturi meters)

Values stored in this application represent typical permanent pressure loss at normal operating conditions. Manufacturer data should be consulted for final design.
