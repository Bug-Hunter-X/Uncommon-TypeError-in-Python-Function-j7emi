# Uncommon TypeError in Python Function
This repository demonstrates an uncommon TypeError that can occur in Python when performing division with unexpected data types.  The bug is caused by attempting to divide a string by an integer.  This isn't a typical ZeroDivisionError, but rather a TypeError because the division operation is not defined for these types.

The solution involves adding a type check within the function to ensure that the inputs are numerical before performing the division.