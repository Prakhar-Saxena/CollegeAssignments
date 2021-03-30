(define (maxmin L)
  (cond
    ((null? L) '()) ;; empty list represents error
    ((null? (cdr L)) (list (car L) (car L))) ;; list of 2 items
    (else (let ((mmtemp (maxmin (cdr L)))
                (first (car L)))
            (cond
              ((> first (car mmtemp))
               (cons first (cdr mmtemp)))
              ((< first (car (cdr mmtemp)))
               (list (car mmtemp) first))
              (else mmtemp))))))
