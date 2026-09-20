# Work Requirement 2 - PRO2002 

## Managing technical debt and improving legacy code 

This repository contains refactored versions of four legacy code examples from Module 3: 

- An undocumented converter 
- A tightly coupled order class 
- Duplicated discount logic 
- A process order method with multiple responsibilities 

Each example has been analyzed and improved with a focus on maintainability, testability, and clarity.

## Undocumented Converter 

The original class used generic names such as `Converter`, `factor`, `offset`, and `value`. Without the explanation provided in the chapter, it was nearly impossible to determine that the class converted Fahrenheit to Celsius. I renamed the class and parameter, added a docstring, and rewrote the calculation in a more recognizable form. This makes the intent clear while preserving the result. 

## Tightly Coupled Order Class

The original `Order` class depended directly on the internal structure of the user object, the database connection, and specific SQL tables and columns. It also used a hardcoded order ID. This mixed domain data, business logic, and persistence in the same class, making the code difficult to test and change.
I changed the `Order` class so that it receives the required user values directly and only contains order data. The storage responsibility was moved to a separate `OrderRepository` class. This repository uses a simple list as a placeholder for a future database. Separating the order data from the storage logic reduces coupling and makes it easier to replace or test the persistence solution later.

## Duplicated Discount Logic 

The original code calculated the total and applied the same discount rule separately in both the shopping cart and the invoice. This duplication could cause inconsistent totals if the discount threshold or rate were changed in only one place. 
I moved the shared calculation into `calculate_discounted_total()`. Both the cart and invoice now use this function, so the discount rule has a single source of truth. I also replaced the numeric values with the named constants `DISCOUNT_THRESHOLD_CENTS` and `DISCOUNT_RATE`. Prices are stored as integer cents to avoid floating-point precision issues. 

## Process Order Method 

The original `process_order()` function had several responsibilities. It calculated the toal, applied discounts, saved the order directly to a database, and sent a notification. Having all these responsibilities in one function made the code difficult to read, test, and change. 
I separated the work into smaller functions for calculating the total, applying the discount, saving the order, and sending the order confirmation. The database and notification functions are simple placeholders because this assignment does not require real persistence or networking. The `process_order()` function now coordinates the different steps, while each separate function has one clear responsibility. 

## Reflection 

I personally found tight coupling the most challenging problem in these examples. At first, I found it difficult to understand why the original `Order` class was problematic, because having all the logic in one place seemed simpler. Through the refactoring, I learned that the issue becomes clearer when the code needs to be tested or changed. If order data, user data, and database logic are closely connected, changing one part may affect several others. Separating the order from the storage logic required more structure, but it also made the responsibilities clearer. This was the example that gave me the best understanding of why maintainability matters. 