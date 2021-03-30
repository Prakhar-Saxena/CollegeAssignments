; Count the number of integers in a list
;  The number of integers in an object that is an integer is 1.
;  The number of integers in a null list is zero.
;  Otherwise the number of integers in L is the number of integers
;  in the car of L plus the number of integers in the cdr of L.


(define numints
  (lambda (L)
    (cond ((integer? L) 1)
          ((null? L) 0)
          (else (+ (numints (car L)) 
                   (numints (cdr L)))))))
