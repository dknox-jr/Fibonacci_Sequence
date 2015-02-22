#  Programming Fibonacci's Sequence in Python (extended and annotated version).
    #  This program will return any single number in the sequence based on user's request.


#0: wrap it all in a function so you can call it any time!
def fibs_sequence():
    #1: create an empty list of numbers.
    nums = []
    #2: populate the first two indices each with the number 1.  Saves many headaches.
    nums.extend([1, 1])
    #3: ask the user for a number.
    print "Which number in the sequence would you like to know (1-indexed)?"
    #4: get input from user, subtract 2 since the first 2 numbers of the sequence are given.
    r = (int(raw_input(">>> "))-2)
    #5: initiate a 'for' loop that iterates 'r' times.
    for i in range(r):
        #6: take the last number in the existing list and add it to the second to last number to get 'x'.
        x = nums[-1] + nums[-2]
        #7: append x to the end of list.
        nums.append(x)
        #8: keep looping until the desired number is reached.
    #9: print the last number in the list!
    print nums[-1]
    #10: run it as many times as you'd like.  CTRL C to quit the vicious cycle.
    fibs_sequence()
#11: initial call of the function.
fibs_sequence()