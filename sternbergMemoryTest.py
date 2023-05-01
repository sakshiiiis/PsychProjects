import numpy as np
import time
"""
    Sternberg Memory Task is used in cognitive psychology where participants are given a list
    of items to memorize and then given a single items and the participants must decide if the item
    given is one they memorized or not.
    
    
"""

# Set the number of items to be displayed in each set
set_size = 7

# Set the number of trials to be performed
num_trials = 2

# Set the duration of each item presentation in seconds
presentation_duration = 5

# Generate a list of random items to be used in the memory test
items = list(range(1, 100))
#Shuffle from numpy library shuffles order of items randomly
np.random.shuffle(items)

'''
Generate a list of random target items to be asked about in the memory test
replace = false makes sure that there are no repeated letters
Choice function from numpy library randomly selects size = 5 items from items list
'''
target_items = np.random.choice(items, size=5, replace=False)

'''
Initialize arrays to store results -> num_trials and set_size
response time is saved as floats
correct answers are saved as booleans
Found this way of array initilization example on geeks4geeks
'''
#response_times = [[0.0] * set_size for _ in range(num_trials)]
#correct_answers = [[False] * set_size for _ in range(num_trials)]
response_times = np.zeros((num_trials, set_size), dtype=float)
correct_answers = np.zeros((num_trials, set_size), dtype=bool)

# Perform the memory test
for trial in range(num_trials):
    # new set of set_size items is randomly choosen from the items list and displayed for presentation_duration
    set_items = np.random.choice(items, size=set_size, replace=False)
    #Print the items
    print(f"\nTrial {trial + 1}: Memorize the following items for {presentation_duration} seconds:")
    print(set_items)
    
    ''''
    time.sleep in python allows you to add a pause to code output
    found on google when trying to pause the printing of the response
    part of the python module
    '''
    
    time.sleep(presentation_duration)
    
    '''
     Hide the displayed items
     Could not find a way to make stimuli disappear so I thought I would add a space
     so the stimuli kind of disappeared off of output shell
    '''
    print(6 * "\n" )
    
    # Ask the user to recall whether each target item was in the set or not
    print(f"Trial {trial + 1}: Target items: {target_items}")
    #enumerate iterates over target_items and keeps track of the index position of each item
    for i, item in enumerate(target_items):
        response_start = time.time()
        #.lower takes user input as lowercase
        response = input(f"Please enter whether {item} was in the set (y/n): ").lower()
        response_end = time.time()
        #response time is calculates by subtracting the start time from the end time 
        response_times[trial, i] = response_end - response_start
        #checks if response was correct or not
        #response == y gives true if the target item was in the set; false otherwise
        correct_answers[trial, i] = response == "y"

# Calculate the mean response time for each target item
# Mean function from numpy
mean_response_times = np.mean(response_times)

# Print the results
print("\nResults:")
#Prints table header
print("Trial\tItem\tCorrect\tResponse Time")
# Iterate over each trial
for trial in range(num_trials):
    #enumerate gets the index i and value of item target_items
    for i, item in enumerate(target_items):
        #Prints trial number, target item number, correct item boolean, and response time upto 2 decimal places
        print(f"{trial + 1}\t{item}\t{correct_answers[trial, i]}\t{response_times[trial, i]:.2f} seconds")
#prints mean response time 
print(f"\nMean response time for each target item: {mean_response_times}")

