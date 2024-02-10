# Design Document for Quantum Field Visualizer

## Overview
This document outlines the architecture of the Quantum Field Visualizer software. The software is designed to allow users to explore and create visual representations of how electromagnetic (EM) quantum fields can build up to classical radio waves.

## Modules

### `classical_field.py`
Defines the `ClassicalField` class, which is responsible for converting quantum probability expectations into a classical field representation.

### `main.py`
Contains the main entry point of the application, setting up the PyQt5 application loop and initializing the visualizer.

### `parameter_tuner.py`
Defines the `ParameterTuner` class, which allows users to tune the parameters of the quantum field.

### `probability_expectation.py`
Defines the `ProbabilityExpectation` class, which calculates the probability expectation from a psi function.

### `psi_function.py`
Defines the `PsiFunction` class, which integrates quantum fields to create the psi function.

### `quantum_field.py`
Defines the `QuantumField` class, which represents a quantum field for a given particle type and set of parameters.

### `simulation.py`
Defines the `Simulation` class, which orchestrates the creation of quantum fields, psi functions, probability expectations, and classical fields, and then visualizes the results.

### `visualizer.py`
Defines the `Visualizer` class, which is a PyQt5 `QMainWindow` that plots the classical field data using matplotlib.

## Usage
To run the visualizer, execute the `run.sh` script, which sets up a virtual environment, installs dependencies, and starts the main application.

## Extending the Software
Engineers can add new features by creating additional modules or extending the existing ones. Documentation for each module is provided in separate files within this directory to assist with understanding the codebase.

## Best Practices
The software follows best practices in Python development, including the use of virtual environments, clear documentation, and modular design for easy extensibility.