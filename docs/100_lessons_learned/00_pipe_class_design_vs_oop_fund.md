# Lessons Learned: Pipe Class Design and OOP Fundamentals

## Background

While developing the `Pipe` class for Hydraulic Analysis Suite, an important distinction emerged between procedural (functional) programming and object-oriented programming (OOP).

Initially, the goal was to:

1. Store pipe information.
2. Validate engineering inputs.
3. Look up hydraulic properties from the material database.
4. Make those properties available throughout the application.

Although the implementation was relatively straightforward, it revealed a fundamental concept of OOP that was not previously fully understood.

---

# Functional Programming Approach

In a functional approach, functions receive data, perform work, and return results.

Example:

```python
def lookup_pipe_material(pipe_material):
    return PIPE_MATERIALS[pipe_material]
```

Usage:

```python
material_data = lookup_pipe_material("pvc")

c_factor = material_data["c_factor"]
roughness = material_data["roughness_ft"]
```

Characteristics:

* Data enters the function.
* Processing occurs.
* Data is returned.
* The function does not retain state.
* The caller is responsible for storing results.

This style is common for calculations and utility functions.

---

# Object-Oriented Programming Approach

In OOP, objects contain both data and behavior.

Instead of returning data, methods often modify the object itself.

Example:

```python
def _lookup_pipe_material(self):
    pipe_material_data = PIPE_MATERIALS[self.pipe_material]

    self.c_factor = pipe_material_data["c_factor"]
    self.roughness_ft = pipe_material_data["roughness_ft"]
    self.manning_n = pipe_material_data["manning_n"]
```

Nothing is returned.

However, the object is modified.

Before method execution:

```text
Pipe
├── flow_rate
├── diameter
├── length
└── pipe_material
```

After method execution:

```text
Pipe
├── flow_rate
├── diameter
├── length
├── pipe_material
├── c_factor
├── roughness_ft
└── manning_n
```

The data becomes part of the object.

---

# The Key OOP Insight

Methods do not always need to return values.

A method can modify the object through `self`.

Example:

```python
self.c_factor = 150
```

attaches data directly to the object.

Afterward:

```python
pipe.c_factor
```

is available anywhere the object is available.

This was the major conceptual breakthrough.

The data does not disappear when the method exits because it is stored on the object itself.

---

# Object Lifecycle Matters

Another important lesson involved the order of execution inside `__init__()`.

Incorrect:

```python
self._validate_data()

self.pipe_material = pipe_material
```

At validation time:

```python
self.pipe_material
```

does not yet exist.

Correct:

```python
self.pipe_material = pipe_material

self._lookup_pipe_material()
```

The object attributes must be created before methods can use them.

---

# Responsibility Separation

A cleaner design emerged by separating responsibilities.

## _validate_data()

Responsible for:

* Flow rate validation
* Diameter validation
* Length validation

Example:

```python
_validate_data()
```

Validates engineering inputs.

---

## _lookup_pipe_material()

Responsible for:

* Material validation
* Material lookup
* Retrieving hydraulic properties

Example:

```python
_lookup_pipe_material()
```

Retrieves:

* C-factor
* Manning's n
* Darcy roughness

and stores them on the object.

This prevents duplicated logic.

---

# Why OOP Fits Hydraulic Analysis Suite

The Pipe class is intended to represent a real engineering object.

A pipe possesses:

* Diameter
* Length
* Material
* Hydraulic properties

Rather than passing numerous variables between functions:

```python
calculate_headloss(
    flow_rate,
    diameter,
    length,
    c_factor
)
```

a single object can be passed:

```python
calculate_headloss(pipe)
```

The object already contains everything required.

This makes the code easier to maintain and more closely reflects real-world engineering systems.

---

# Final Design Philosophy

The Pipe class should:

* Store pipe characteristics.
* Validate engineering inputs.
* Retrieve material properties.
* Provide derived pipe properties.

The Pipe class should not:

* Perform hydraulic calculations.
* Calculate headloss.
* Generate system curves.
* Size pumps.

Those responsibilities belong to equation and calculator classes.

---

# Biggest Takeaway

The most important lesson learned was that methods in an object-oriented system often exist to modify the object itself rather than return values.

Functional programming:

```text
Input
  ↓
Function
  ↓
Return Result
```

Object-oriented programming:

```text
Object
  ↓
Method
  ↓
Object Updated
```

Understanding this distinction makes it easier to design classes that represent real engineering components rather than simply acting as containers for functions.
