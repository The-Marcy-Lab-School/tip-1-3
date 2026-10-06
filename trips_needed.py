# Independent check: Moving day
# Work alone: no AI, no notes. Write your prediction on paper BEFORE you run anything.
#
# 1. Predict: write the exact output of this program on paper.
# 2. Debug:   make the code do what the comment inside trips_needed says.
# 3. Adjust:  each van trip takes 45 minutes. Write a function minutes_for(rooms)
#             that uses trips_needed and gives back the total minutes. After the
#             van message, print:  Moving takes ___ minutes
# 4. Test:    change the move to 2 rooms. Predict the output on paper, then run it.

def boxes_for(rooms):
    return rooms * 12

def trips_needed(rooms):
    print(boxes_for(rooms) / 20)   # gives back the number of van trips

trips = trips_needed(5)
if trips > 2:
    print("Rent a bigger van")
else:
    print("One van is fine")

# 1. Prediction:
#
# Actual:
#
# Because (name a big idea number):
#
# 4. Test prediction (2 rooms):
#
# Actual:
