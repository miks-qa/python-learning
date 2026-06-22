## Chapter 03 - Learning Log :pencil2:

### Overview :brain:
This chapter focused on conditional statements, comparison operators, nested decisions, multi-way decision structures, and error handling using `try` and `except`. It also introduced how Python makes decisions step-by-step based on conditions and how program flow changes depending on user input and logic structure.

### What I learned :sparkles:
- how Python uses `if`, `elif`, and `else` to make decisions
- how comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) are used to evaluate conditions
- the difference between assignment (`=`) and comparison (`==`)
- how Boolean expressions evaluate to `True` or `False`
- how indentation defines code blocks and affects execution
- how nested `if` statements allow decision-making inside another condition
- how multi-way decisions work using `elif` and top-to-bottom evaluation
- how only one branch executes in an `if`/`elif`/`else` chain
- how `try` and `except` handle runtime errors and prevent program crashes
- how Python stops the `try` block immediately when an error occurs

### Hands-on practice :computer:
In this chapter, I practiced:
- building an age checker program using conditional statements
- creating a login simulation program using nested `if` statements
- testing different input values to observe how conditions change program output
- experimenting with valid and invalid inputs to understand error handling
- writing programs using `if`, `elif`, `else`, and `try`/`except` structures

### Personal notes :thought_balloon:
One thing that stood out to me in this chapter was how important indentation is in Python. At first, I thought that once an `if` condition was satisfied, Python would automatically skip statements that represented the opposite outcome. After experimenting with different values, I realized only the indented statements belong to the conditional block. Any statement outside the block executes normally unless an `else` statement is explicitly used.

I also found the `try` and `except` examples interesting because they reminded me of the invalid input validation testing I performed as a Quality Engineer. When testing applications, I would often try unexpected inputs to see how the system responded and whether appropriate error messages appeared. Learning how Python handles invalid input helped me connect those testing experiences to what is happening behind the scenes in the code.

Another thing I realized is that the placement of `try` and `except` blocks matters. The course example only placed the risky type conversion inside the `try` block, while my age checker included the conditional logic that depended on the conversion succeeding. Through experimentation, I learned that there can be multiple valid ways to structure error handling depending on how the program should behave. This made me think more intentionally about which parts of the code might fail and which parts should continue running after an error occurs.

Another realization I had while working through `if` statements is that Python only does exactly what I instruct it to do. It does not interpret intent or meaning behind the code. It simply follows the conditions and executes whichever block I explicitly define. This made me more aware of how precise programming needs to be, because the output depends entirely on the instructions written, not on what I expect it to do.

This chapter made me appreciate how important it is to anticipate different user behaviors and handle both expected and unexpected inputs properly.

### Additional learning :snake:
Outside of the official lesson, I also:
- created a simple age validation checker to test how Python handles valid and invalid inputs

:memo: [View Age Checker](../exercises/age-checker.py)

- built a login simulation system that identifies whether the username or password is incorrect

:closed_lock_with_key: [View Login Simulation](../exercises/login-simulation.py)

- experimented with input validation logic similar to real-world application behavior

These exercises helped me understand how conditional logic is used in real systems for validation and decision-making.

### Summary :dart:
Overall, Chapter 03 helped me get comfortable with:
- making decisions using conditional statements in Python
- understanding how program flow changes based on conditions
- working with nested and multi-way decision structures
- handling errors using `try` and `except`
- applying logic to build simple real-world validation programs