# Work Requirement 2 - PRO2002 

## Managing technical debt and improving legacy code 

This repository contains refactored versions of four legacy code examples from Module 3: 

- An undocumented converter 
- A tightly coupled order class 
- Duplicated discount logic 
- A process order method with multiple responsibilities 

Each example will be analyzed and improved with a focus on maintainability, testability, and clarity.

## Undocumented Converter 

The original class used generic names such as `Converter`, `factor`, `offset`, and `value`. Without the explanation provided in the chapter, it was nearly impossible to determine that the class converted Fahrenheit to Celsius. I renamed the class and parameter, added a docstring, and rewrote the calculation in a more recognizable form. This makes the intent clear while preserving the result. 