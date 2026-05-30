# Pump Station Hydraulic Calculator

## Project Overview

The purpose of this project is to develop a command-line Python application capable of performing common hydraulic calculations used in water, wastewater, and pumping station design.

The project serves two objectives:

1. Reinforce hydraulic engineering concepts learned through lift station design studies.
2. Strengthen Python programming skills through incremental software development.

Rather than attempting to build a full-featured engineering application immediately, the project will be developed in stages. Each version introduces additional engineering calculations and software complexity.

---

# Version 1: Hazen-Williams Calculator

## Objective

Develop a basic CLI application that calculates friction headloss using the Hazen-Williams equation.

## User Inputs

* Flow Rate (gpm)
* Pipe Diameter (in)
* Pipe Length (ft)
* Hazen-Williams C Factor

## Outputs

* Velocity (fps)
* Total Friction Headloss (ft)
* Headloss per 1,000 feet (ft/1000 ft)

## Skills Practiced

* User input handling
* Unit conversions
* Function creation
* Engineering calculations
* Formatted console output

---

# Version 2: Material Library

## Objective

Reduce user input requirements by allowing pipe material selection.

## User Inputs

* Pipe Material
* Flow Rate
* Diameter
* Length

## Pipe Materials

Example material library:

| Material | C Value      |
| -------- | ------------ |
| PVC      | 150          |
| HDPE     | 150          |
| New DIP  | 140          |
| Aged DIP | 100          |
| Custom   | User Defined |

## Additional Skills

* Dictionaries
* Menu systems
* Input validation
* Error handling

---

# Version 3: Total Dynamic Head Calculator

## Objective

Expand calculations beyond pipe friction to include complete system head.

## User Inputs

* Flow Rate
* Pipe Material
* Pipe Diameter
* Pipe Length
* Static Head
* Minor Loss Coefficient

## Outputs

* Velocity Head
* Friction Head
* Minor Loss Head
* Total Dynamic Head (TDH)

## Additional Skills

* Multiple calculation modules
* Function decomposition
* Data organization

---

# Version 4: Lift Station Design Tool

## Objective

Create a practical hydraulic calculator applicable to lift station design.

## User Inputs

* Design Flow
* Pipe Material
* Pipe Diameter
* Pipe Length
* Static Head
* Number of Bends
* Check Valves
* Gate Valves
* Other Minor Loss Components

## Outputs

* Velocity
* Friction Head
* Minor Loss Head
* Total Dynamic Head
* Headloss per 1,000 ft

## Additional Skills

* Component-based calculations
* Engineering assumptions
* Modular program structure

---

# Version 5: Pump Curve Integration

## Objective

Introduce pump performance analysis.

## User Inputs

* Pump Curve Data (CSV)
* System Parameters

## Outputs

* System Curve
* Pump Curve
* Operating Point
* Estimated Operating Head
* Estimated Operating Flow

## Additional Skills

* CSV processing
* Data visualization
* Interpolation
* Plotting with Matplotlib

---

# Future Enhancements

Potential future improvements include:

* Multiple pipe segments
* Variable pipe diameters
* Parallel force mains
* Force main system modeling
* Wet well storage calculations
* Pump cycling analysis
* Runtime estimates
* Generator sizing support
* Export reports to PDF
* Streamlit web interface
* Engineering calculation package

---

# Educational Goals

This project is intended to improve understanding of:

* Hazen-Williams headloss calculations
* Darcy-Weisbach headloss calculations
* Velocity calculations
* Total Dynamic Head (TDH)
* Minor losses
* Pump system behavior
* Force main design
* Lift station hydraulics

At the same time, the project reinforces:

* Python fundamentals
* Software architecture
* Modular design
* Input validation
* Documentation practices
* Testing and verification

---

# Long-Term Vision

The ultimate goal is to evolve the application from a simple CLI calculator into a practical engineering tool capable of supporting preliminary lift station and force main design studies.

The project should prioritize:

1. Engineering correctness.
2. Transparent calculations.
3. Clear documentation.
4. Maintainable code structure.
5. Incremental feature development.

The focus is not on building software for software's sake, but on creating a tool that strengthens both hydraulic engineering knowledge and Python development skills.
