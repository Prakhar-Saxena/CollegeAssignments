; Compute the length of the list L
;   The length of a list is 0 if it is empty.
;   Otherwise it is 1 plus the length of the rest of the list.
;
(define length (lambda (L)
  (if (null? L)
      0
      (+ (length (cdr L)) 1))))
