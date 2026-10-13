"""
A mixed number has a whole part and a fraction part.

17 ÷ 7 = 2 3/7
    whole part: 2
    fraction part: 3/7
"""

numerator = 17
denominator = 7

# ------------------------------------------------------------
# STEP 1: Recall
# TODO: Print numerator ÷ denominator as a mixed number.
#       Use the variables, not the numbers 17 and 7.
# Expected output: 2 3/7
#
# Check: change the values to 23 and 5.
# Expected output: 4 3/5
# Then change them back to 17 and 7.


# ------------------------------------------------------------
# STEP 2: Wrap it in a function
# TODO: Define a function named mixed_print with two parameters:
#       numerator and denominator.
#       Move your Step 1 print line inside it.
# TODO: Call mixed_print with the arguments 17 and 7.
# Expected output: 2 3/7
#
# TODO: Call it again with the arguments in the other order: 7 and 17.
#   Prediction:
#   Actual:
#
# TODO: Make a copy of mixed_print named mixed_return.
#       In the copy, replace the print line with a return line
#       that uses the same text.
#
# TODO: Predict each result first. Then add these and run:
#       - store mixed_return(17, 7) in a variable named answer,
#         then print "Answer:" and answer
#       - store mixed_print(17, 7) in a variable named result,
#         then print "Result:" and result
#   Prediction for answer:
#   Actual:
#   Prediction for result:
#   Actual:
#
# Discuss with your table, then write in your own words:
# What is different about the two functions?
#


# ------------------------------------------------------------
# STEP 3: Why it matters
# TODO: Predict first, then try each one:
#       - add the text " cups" to answer and print it
#       - add the text " cups" to result and print it
#   Prediction for answer:
#   Actual:
#   Prediction for result:
#   Actual:
#
# Discuss with your table, then write in your own words:
# What does return do?
#
# What does print do?
#


# ------------------------------------------------------------
# STEP 4: Fix it
# TODO: Change ONE line inside mixed_print so that result
#       holds the mixed number.
# Expected output: Result: 2 3/7


# ------------------------------------------------------------
# STEP 5: Nothing left over
# TODO: Predict, then print mixed_return(14, 7).
#   Prediction:
#   Actual:
#
# TODO: Change mixed_return so that when nothing is left over,
#       it gives back just the whole number.
# Expected:
#   mixed_return(14, 7) -> 2
#   mixed_return(17, 7) -> 2 3/7


# ------------------------------------------------------------
# STEP 6: Helpers
# TODO: Define a function named whole_part(numerator, denominator)
#       that PRINTS the whole part.
# TODO: Define a function named leftover(numerator, denominator)
#       that RETURNS what's left over.
# Examples:
#   whole_part(17, 7) -> 2
#   leftover(17, 7)   -> 3
#
# TODO: Change mixed_return so it uses whole_part and leftover
#       instead of doing the math itself.
#       Predict, then print mixed_return(17, 7).
#   Prediction:
#   Actual:
#
# TODO: Fix it with ONE change.
# Expected:
#   mixed_return(17, 7) -> 2 3/7
#   mixed_return(14, 7) -> 2
#
# Discuss with your table, then write in your own words:
# What does a helper need to do for the function that uses it?
#


# ------------------------------------------------------------
# STEP 7: Make: weeks and days
# Problem: Given a number of days, give back the weeks and days as text.
#          If there are no extra days, give back just the weeks.
#
# TODO: Before you code, plan with IPO:
#   Input:
#   Process:
#   Output:
#
# TODO: Define a function named weeks_and_days(days).
#       It must use whole_part and leftover.
#       Don't do the division math inside weeks_and_days.
# Examples:
#   weeks_and_days(17) -> 2 weeks, 3 days
#   weeks_and_days(14) -> 2 weeks
#   weeks_and_days(30) -> 4 weeks, 2 days
#
# TODO: Print the three results with labels.
# Expected output:
#   Trip: 2 weeks, 3 days
#   Stay: 2 weeks
#   Project: 4 weeks, 2 days