# Hydraulic Analysis Suite

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![uv](https://img.shields.io/badge/package%20manager-uv-purple.svg)
![Platform](https://img.shields.io/badge/platform-CLI-lightgrey.svg)
![Status](https://img.shields.io/badge/status-In%20Development-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Python-based hydraulic engineering analysis platform for modeling and evaluating pressurized pipe systems, force mains, lift stations, and pumping infrastructure.

The project began as a learning exercise focused on friction loss calculations and is evolving into a broader engineering toolkit that combines hydraulic analysis, software development, and infrastructure engineering concepts.

The long-term goal is to create a modular suite of reusable tools capable of supporting common water and wastewater engineering workflows, including pipe hydraulics, total dynamic head calculations, pump system analysis, wet well sizing, force main evaluation, and lift station design studies.

This project serves two primary purposes:

* Strengthen understanding of hydraulic engineering and pump station design.
* Develop professional software engineering skills through the implementation of real-world engineering workflows.

---

## Project Goals

This project is being developed incrementally to:

* Strengthen understanding of water and wastewater hydraulic systems.
* Reinforce Python software engineering practices.
* Model real-world hydraulic infrastructure using object-oriented design.
* Build reusable engineering analysis tools.
* Explore computational approaches to pump system design and evaluation.
* Create a foundation for future infrastructure analytics applications.
* Develop a portfolio-quality engineering software project.

---

## Design Philosophy

The Hydraulic Analysis Suite is organized around engineering components rather than individual equations.

Examples include:

* Pipe
* Pump
* Force Main
* Wet Well
* Fittings

Engineering calculations are implemented as independent computational modules that operate on these system components.

This approach allows the project to grow from simple friction loss calculations into more advanced hydraulic analyses while maintaining a clean and scalable software architecture.

The intent is to model infrastructure systems, not simply perform isolated calculations.

---

## Current Features

### Version 1 - Core Pipe Hydraulics

* Hazen-Williams headloss calculations
* Velocity calculations
* Headloss per 1,000 feet reporting
* Command-line interface

---

## Planned Roadmap

### Version 2 - Material Libraries & Validation

* Pipe material library
* Automatic Hazen-Williams C-factor selection
* Input validation
* Engineering validation checks

### Version 3 - Total Dynamic Head Analysis

* Static head calculations
* Minor loss calculations
* Total Dynamic Head (TDH) calculations

### Version 4 - Force Main & Lift Station Analysis

* Force main hydraulic analysis
* Valve and fitting loss estimation
* Lift station hydraulic calculations
* Expanded wastewater design workflows

### Version 5 - Pump System Analysis

* Pump curve integration
* System curve generation
* Operating point determination
* CSV-based pump data import

### Version 6 - Hydraulic System Modeling

* Multi-segment pipelines
* Parallel force mains
* Advanced hydraulic workflows
* Infrastructure system modeling

### Future Enhancements

* Wet well storage calculations
* Pump cycling analysis
* Generator sizing
* Report generation
* Streamlit interface
* Scenario analysis
* Infrastructure planning modules
* Asset management integrations

---

## Engineering Topics Covered

* Hazen-Williams Equation
* Darcy-Weisbach Equation
* Manning Equation
* Velocity Calculations
* Friction Headloss
* Minor Losses
* Total Dynamic Head (TDH)
* Pump Curves
* System Curves
* Force Main Design
* Lift Station Hydraulics
* Wet Well Analysis
* Pump System Evaluation

---

## Documentation

Project documentation is organized within the `docs/` directory.

Key project documentation includes:

* Project Overview
* Architecture and Design Decisions
* Development Strategy
* Engineering Notes
* Reference Material
* Future Roadmap

For the current project structure, see:

```text
docs/01_structure/00_project_structure.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd hydraulic-analysis-suite
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
python main.py
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
* Independent engineering checks when possible

The software is intended as an educational and engineering support tool and should not replace professional engineering judgment.

Users are responsible for verifying all calculations prior to design, construction, procurement, permitting, or operational decision-making.

---

## References

Primary references include:

* Pumping Station Design, Third Edition
* Hydraulic Institute Standards
* AWWA Publications
* Ten States Standards
* Utility Design Manuals and Technical Specifications
* Manufacturer Pump Curves and Technical Literature

---

## License

MIT License

---

## Author

Brice Nelson

**Civil Engineer | Infrastructure Analytics | Python Developer**

Focused on the intersection of infrastructure engineering, hydraulic systems, data analytics, and software development.

Areas of interest include:

* Water and wastewater infrastructure
* Lift station and force main design
* Hydraulic modeling
* Infrastructure analytics
* Applied machine learning
* Engineering software development
