# Hydraulic Calculator

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![uv](https://img.shields.io/badge/package%20manager-uv-purple.svg)
![Platform](https://img.shields.io/badge/platform-CLI-lightgrey.svg)
![Status](https://img.shields.io/badge/status-In%20Development-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Python-based engineering calculator for analyzing friction losses and hydraulic behavior in pressurized pipe systems. The project implements common water and wastewater design equations, including Hazen-Williams and Darcy-Weisbach, and is being developed as part of a broader study of lift station and force main hydraulics.

The project serves as both a software development exercise and an engineering learning tool, focusing on common hydraulic calculations used in force main design, lift station design, and pump system analysis.

---

## Project Goals

This project is being developed incrementally to:

* Strengthen understanding of hydraulic engineering concepts.
* Reinforce Python software development skills.
* Create reusable engineering calculation tools.
* Explore pump system behavior through computational methods.
* Build a foundation for future infrastructure analytics applications.

---

## Current Features

### Version 1

* Hazen-Williams headloss calculations
* Velocity calculations
* Headloss per 1,000 feet reporting
* Command-line interface

---

## Planned Roadmap

### Version 2

* Pipe material library
* Automatic Hazen-Williams C-factor selection
* Input validation

### Version 3

* Total Dynamic Head (TDH) calculations
* Static head inputs
* Minor loss calculations

### Version 4

* Lift station hydraulic calculator
* Valve and fitting loss estimation
* Expanded force main analysis

### Version 5

* Pump curve integration
* System curve generation
* Operating point determination
* CSV-based pump data import

### Future Enhancements

* Multi-segment pipelines
* Parallel force mains
* Wet well storage calculations
* Pump cycling analysis
* Report generation
* Streamlit interface
* Infrastructure planning modules

---

## Engineering Topics Covered

* Hazen-Williams Equation
* Darcy-Weisbach Equation
* Velocity Calculations
* Friction Headloss
* Minor Losses
* Total Dynamic Head (TDH)
* Pump Curves
* System Curves
* Force Main Design
* Lift Station Hydraulics

---

## Project Structure

```text
hydraulic_calculator/
│
├── docs/
│   ├── project_plan.md
│   ├── engineering_notes.md
│   └── references.md
│
├── src/
│   └── hydraulic_calculator/
│
├── tests/
│
├── data/
│
├── pyproject.toml
│
├── uv.lock
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd hydraulic_calculator
```

### Create Virtual Environment

```bash
uv venv
```

### Activate Environment

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### Install Dependencies

```bash
uv sync
```

---

## Running the Application

```bash
python -m hydraulic_calculator
```

---

## Development

Install development dependencies:

```bash
uv sync --extra dev
```

Run tests:

```bash
pytest
```

Run formatting:

```bash
ruff format .
```

Run linting:

```bash
ruff check .
```

---

## Verification Philosophy

Engineering calculations should never be treated as a black box.

All calculations implemented in this project should be verified against:

* Published engineering references
* Hand calculations
* Spreadsheet calculations
* Manufacturer data where applicable

The software is intended as an educational and engineering support tool and should not replace professional engineering judgment.

---

## References

Primary references include:

* Pumping Station Design, Third Edition
* Hydraulic Institute Standards
* AWWA Publications
* Ten States Standards
* Utility Design Manuals and Technical Specifications

---

## License

MIT License

---

## Author

Brice Nelson

Civil Engineer | Infrastructure Analytics | Python Developer

Focused on the intersection of infrastructure engineering, hydraulic systems, data analytics, and software development.
