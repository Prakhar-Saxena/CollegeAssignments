; Code for Part 3



; (i)

(define range
  (lambda (start step end)
    (if (> start end) '() 
      (if (> (+ start step) end) 
	(cons start '()) 
	(cons start (range (+ start step) step end))))))


; (ii)

;(define seq (start step end f)
;    ((if (> start end) '()
;      (if (> (+ start step) end)
;	(cons (f start) '()
;	(cons (f start) (seq (+ start step) step end f)))))))

;(define seq f start step end
;  (define L (range start step end))
;  (f (car L))
;  (L (cdr L))

