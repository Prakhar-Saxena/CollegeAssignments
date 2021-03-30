; Code for Part 2



; (i)

; Non-Tail Recursive factorial

(define factorial_nt
  (lambda (n)
    (if (= n 1)
      1
      (* n (factorial_nt (- n 1))))))


; Tail Recursive factorial

(define factorial_t
  (lambda (n result)
    (if (= n 1)
      result
      (factorial_t (- n 1) (* n result)))))



; (ii)

; Non-Tail Recursive exponent2
(define exponent2_nt
  (lambda (n)
    (if (= n 0) 1)
    (if (= n 1)
      2
      (* 2 (exponent2_nt (- n 1))))))

; Tail Recursive exponent2
(define exponent2_t
  (lambda (n result)
    (if (= n 0) 1)
    (if (= n 1)
      result
      (exponent2_t (- n 1) (* 2 result)))))



; (iii)

(define (compose_nt g f) (lambda (x) (g (f x))))
(define (compose_t g f) (lambda (x) (g (f x 1) 2)))

(define expo_fact_nt (compose_nt exponent2_nt factorial_nt))
(define expo_fact_t (compose_t exponent2_t factorial_t))
