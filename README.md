# CS 202 Spring '26 | Lab 2: Foundations
**Instructor:** Duran  
**Duration:** 4-Day Lab

### Schedule
* **4/6 Day 1:** Recursion
* **4/8 Day 2:** Time Complexity
* **4/10 Day 3:** Data Definitions
* **4/13 Day 4:** Design Recipe

---

## Submission
* You have been provided with a sign-off sheet requiring a signature for each of the four days.
* Signatures do not need to be acquired on the exact day of the assignment, but all must be collected by the deadline.
* Sign-offs can be authorized by the instructor or your designated TA (202-07 TA Sofia, 202-13 TA Laura).
* Avoid waiting until the final day to acquire all signatures; high student volume may preclude us from evaluating everyone.
* Submit the fully completed sign-off sheet on the final day.

## Day 1 Details
* Analyze the provided iterative linear search implementation.
* Refactor the algorithm into a recursive function.
* Employ non-destructive methodologies exclusively.
* Verify the integrity of your solution by ensuring all provided test cases continue to pass.

Day 2 Details
* Review the quadratic search algorithm provided to you.

* Determine the asymptotic time complexity (Big O notation) for the function. Hint: I can tell you right away that the time complexity is neither linear nor quadratic.

* Consider the worst-case scenario. The worst case is not finding the last element, but rather the second-to-last element.

* Analyze the jumps. Finding the last element requires k jumps, landing at index k^2 (meaning n = k^2). However, for the worst-case second-to-last element, the algorithm must jump back and linearly iterate through the resulting "mini-list" between jumps.

* Articulate a rigorous justification for your analysis in the designated space on your sign-off sheet. To solve this, you need to answer: how many elements are in that mini-list?

* Mini-list size = k^2 - (k-1)^2 = Expand the polynomial: k^2 - (k^2 - 2k + 1)

## Day 3 Details
* **Specification:** "Design a function that processes a collection of stock data (comprising open price, close price, and date) to compute an aggregate metric, such as a collection of average weekly prices."
* **Today's Sole Objective:** Complete **Step 1 of the Design Recipe** (Data Definitions). 
* Identify and construct the specific Data Types or Data Classes required to strictly represent the input and output structures for the prompt.
* *Note:* Implementation of the core algorithmic logic is strictly excluded from today's requirements. Your only task is the formal coding of these structural data definitions.

## Day 4 Details
* Continue with the specification established on Day 3 and proceed with the formal design recipe.
* **Step 2:** Synthesize the prompt into a precise, single-sentence purpose statement.
* **Step 3:** Define an appropriate function signature/header.
* **Step 4:** Construct one comprehensive test case representing nominal (valid) input.
* *Note:* You are exempt from completing Step 5 (full implementation) for this exercise.

