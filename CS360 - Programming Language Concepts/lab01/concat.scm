; Concatenation of the lists L1 and L2.
;   The concatention of L1 and L2 is equal to L2 if L1 is null.
;   Otherwise it is the list whose first element is the first
;   element of L1 and whose rest is equal to the concatention
;   of the rest of L1 and L2.
;


(define concat 
  (lambda (L1 L2)
    (if (null? L1)
        L2
        (cons (car L1)
              (concat (cdr L1) L2)))))
