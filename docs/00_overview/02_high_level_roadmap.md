# Hydraulic Analysis Suite - Version 1 Development Roadmap

## Guiding Principle

Focus on building a usable hydraulic analysis workflow rather than a collection of disconnected equations.

The objective of Version 1 is to establish a solid engineering and software foundation that can be expanded later into more advanced hydraulic modeling tools.

---

# Phase 1 - Core Models

## Pipe ✅

Current status: In Progress / Nearly Complete

Responsibilities:

- Store physical pipe properties
- Store hydraulic properties
- Validate user inputs
- Calculate derived properties

Examples:

- Flow rate
- Diameter
- Length
- Material
- C-factor
- Manning's n
- Roughness coefficient
- Velocity
- Area
- Volume

---

## Pump

Responsibilities:

- Store pump information
- Store pump performance data
- Prepare for future pump curve analysis

Suggested Attributes:

- pump_name
- design_flow
- design_head
- efficiency
- horsepower
- pump_curve_points

---

## Fitting

Responsibilities:

- Store fitting information
- Support future minor loss calculations

Suggested Attributes:

- fitting_type
- quantity
- k_factor

Examples:

- 90° Bend
- 45° Bend
- Gate Valve
- Check Valve
- Tee
- Reducer

---

### Phase 1 Build Order

- [x] Pump Class
- [x] constants.py
- [x] pipe_materials.py
- [ ] Fitting Class
- [ ] fitting_coefficients.py
- [x] fittings_data.py
- [ ] Minor Loss Equation Module
- [ ] Pump Class
- [ ] Hazen-Williams Equation Module
- [ ] Friction Loss Calculator
- [ ] TDH Calculator

# Phase 2 - Equation Modules

Create a dedicated equations package.

```text
equations/
├── hazen_williams.py
├── darcy_weisbach.py
├── minor_losses.py
```

### Design Philosophy

Equation modules should:

- Accept inputs
- Perform calculations
- Return results

Equation modules should NOT:

- Request user input
- Print results
- Create objects
- Manage workflows

---

## Hazen-Williams

Functions:

- headloss()
- headloss_per_1000ft()

---

## Darcy-Weisbach

Functions:

- reynolds_number()
- friction_factor()
- headloss()

---

## Minor Losses

Functions:

- headloss()

---

# Phase 3 - Calculators

Calculators combine models and equations into useful engineering tools.

---

## Friction Loss Calculator

Inputs:

- Pipe

Outputs:

```json
{
    "headloss_ft": value,
    "headloss_per_1000ft": value
}
```

Responsibilities:

- Perform Hazen-Williams calculations
- Perform Darcy-Weisbach calculations
- Generate comparison results

---

## TDH Calculator

Inputs:

- Pipe
- Static Head
- Minor Losses

Outputs:

```json
{
    "static_head": value,
    "friction_head": value,
    "minor_head": value,
    "tdh": value
}
```

Responsibilities:

- Calculate Total Dynamic Head
- Summarize system losses

---

# Phase 4 - Force Main Analysis

## ForceMain or PipelineSystem

Represents an actual pipeline system rather than a single pipe.

Suggested Attributes:

- pipe_segments
- fittings
- elevation_difference

Example:

```text
24" DIP - 500 ft
20" DIP - 1,200 ft

3 bends
2 valves
```

Responsibilities:

- Aggregate losses
- Model real-world force mains
- Prepare for pump system analysis

---

# Phase 5 - Pump Analysis

## Pump Analyzer

Responsibilities:

- Determine operating point
- Calculate required horsepower
- Calculate efficiencies

Potential Functions:

- operating_point()
- horsepower_required()
- wire_to_water_efficiency()

---

# Phase 6 - Wet Well Module

## WetWell

Particularly valuable for lift station design.

Suggested Attributes:

- diameter
- depth
- usable_volume
- operating_range
- starts_per_hour

Potential Functions:

- required_volume()
- cycle_time()
- starts_per_hour()

Engineering Applications:

- Lift station sizing
- Pump cycling analysis
- Storage calculations

---

# Phase 7 - Reporting

Generate engineering deliverables.

Supported Formats:

- JSON
- CSV
- PDF

Potential Reports:

- Friction loss summary
- TDH summary
- Pump selection summary
- Lift station design summary

---

# Recommended Version 1 Build Order

```text
1. Pipe
2. Hazen-Williams Equation
3. Darcy-Weisbach Equation
4. Friction Loss Calculator
5. Minor Loss Calculator
6. TDH Calculator
7. Pump Model
8. Pump Analyzer
9. Wet Well Model
10. Reporting
```

---

# Explicitly Out of Scope for Version 1

The following should wait until the engineering foundation is complete:

- GUI
- Database
- Web Application
- AI Features
- Machine Learning
- Cloud Infrastructure
- Docker
- APIs
- Authentication
- Multi-user Support

Version 1 should focus on solving hydraulic engineering problems accurately and reliably before expanding into software platform features.

---

# Version 1 Success Criteria

The project should be able to accurately calculate:

- Flow Velocity
- Pipe Area
- Internal Volume
- Friction Loss
- Minor Losses
- Total Dynamic Head (TDH)
- Pump Horsepower
- Wet Well Storage Volume
- Pump Cycle Time

Achieving these capabilities would result in a credible hydraulic engineering software package that demonstrates both engineering expertise and software development skills.
