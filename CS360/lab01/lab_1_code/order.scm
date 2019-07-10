; Compute the order of an object (maximum depth)
;  The order of an atom is 0.
;  The order of a list is 1 plus the maximum order of its elements.

(define (order L)
  (if (and (not (null? L)) (not (pair? L)))
      0
      (+ 1 (reduce max 0 (map order L)))))

