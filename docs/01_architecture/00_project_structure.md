# Project Structure

```plaintext
hydraulic_analysis_suite
│
├── docs/
│   ├── 00_overview/
│   ├── 01_structure/
│   └── 02_strategy/
│
├── src/hydraulic_analysis_suite
│   │
│   ├── models/
│   │   ├── __init__
│   │   ├── pipe.py
│   │   ├── pump.py
│   │   ├── fitting.py
│   │   ├── wet_well.py
│   │   └── force_main.py
│   │
│   ├── equations/
│   │   ├── __init__
│   │   ├── hazen_williams.py
│   │   ├── darcy_weisbach.py
│   │   ├── manning.py
│   │   ├── minor_losses.py
│   │   └── future equations
│   │
│   ├── calculators/
│   │   ├── __init__
│   │   ├── tdh_calculator.py
│   │   ├── wet_well_calculator.py
│   │   ├── generator_calculator.py
│   │   ├── force_main_calculator.py
│   │   ├── system_curve_calculator.py
│   │   └── pump_selection_calculator.py
│   │
│   ├── db/
│   │   ├── __init__
│   │   ├── pipe_materials.py
│   │   └── constants.py
│   │
│   └── cli/
│       ├── __init__
│       └── menu.py
│
├── tests/
│   ├── data/
│   │   ├── test_fittings_data.py
│   │   └── test_pipe_materials.py
│   ├── models/
│   │   ├── test_fitting.py
│   │   └── test_pipe.py
│   └── utils/
│       └── test_fitting_data_helper_calcs.py
│
├── .gitignore
├── main.py
├── pyproject.toml
└── README.md
```