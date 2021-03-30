;(take integer List)
;Select the nth value from the delayed list L
(define (take n L)
	(if (= n 0) '()
		(cons 
			(car (force L)) 
			(take (- n 1) (cdr (force L)))
		)
	)
)

;(intlist int int)
;Create a delayed list of integers in the range m to n
(define (intlist m n)
	(if (> m n) '()
		(cons m (delay (intlist (+ 1 m) n))))
)


;(delayed-map function list)
;Map a function over a delayed evaluation list
(define (delayed-map f L)
	(if (null? L) '()
		(delay (cons (f (car (force L)))
			(delayed-map f (cdr (force L)))
		)
		)
	)
)

;(show x) 
; display the element x
(define (show x) (display x) (newline) x)

;Create a list L storing the delayed map application of show to the list of integers 1 to 100
(define L
	(delayed-map show (delay (intlist 1 100)))
)

