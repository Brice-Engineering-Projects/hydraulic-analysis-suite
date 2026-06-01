# Project Structure

```plaintext
pipe_hydraulic_calculator
│
├── docs/
│   ├── 00_overview/
│   ├── 01_structure/
│   └── 02_strategy/
│
├── src/
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
│   ├── test_pipe.py
│   ├── test_hazen_williams.py
│   ├── test_minor_losses.py
│   └── test_system_curve.py
│
├── .gitignore
├── main.py
├── pyproject.toml
└── README.md
```