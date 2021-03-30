Initially I just ran both the algorithms, minimax and minimax with alpha-beta pruning just once on a board. and I made sure that there was only one sensible move possible, and then I computed the time difference between the two algorithms.
Essentially how long it took for each to reach to that move/decision. Following are the results
Time it took to make this decision with minimax without alpha-beta pruning: 0.06086897850036621
Time it took to make this decision with minimax with alpha-beta pruning: 0.004966020584106445

It's clearly evident that the execution time for minimax with alpha-beta pruning clearly went down more than 10 times. It's around 12.25 times.