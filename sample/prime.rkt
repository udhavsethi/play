;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname prime) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; (check-divisible number i) consumes a number
;; and returns true if is not divisible by any number
;; between i and given number, and false otherwise
;; check-divisible: Nat Nat -> Bool
;; example:
(check-expect (check-divisible 17 2) true)
(check-expect (check-divisible 15 5) false)

(define (check-divisible number i)
  (cond
    [(= number i) true]
    [(= (remainder number i) 0) false]
    [else (check-divisible number (+ i 1))]))

;; tests
(check-expect (check-divisible 15 10) true)
(check-expect (check-divisible 20 7) false)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; (prime? number) consumes a natural number and produces
;; true if that number is prime, and false otherwise.
;; prime?: Nat -> Bool
;; example:
(check-expect (prime? 17) true)
(check-expect (prime? 2) true)

(define (prime? number)
  (cond
    [(<= number 1) false]
    [(= number 2) true]
    [else (check-divisible number 2)]))

;; tests
(check-expect (prime? 23) true)
(check-expect (prime? 43) true)
(check-expect (prime? 1) false)
(check-expect (prime? 24) false)
(check-expect (prime? 100) false)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; (prime-range start end) consumes two natural numbers
;; start and end and produces the list of all prime numbers
;; in the interval that starts with the number start and ends
;; with the number end (inclusive).
;; prime-range: Nat Nat -> (listof Nat)
;; example:
(check-expect (prime-range 1 10)
                       (cons 2 (cons 3 (cons 5 (cons 7 empty)))))
(check-expect (prime-range 10 1) empty)

(define (prime-range start end)
  (cond
    [(> start end) '()]
    [(prime? start) (cons start (prime-range (+ start 1) end))]
    [else (prime-range (+ start 1) end)]))

;; tests
(check-expect (prime-range 1 10)
                       (cons 2 (cons 3 (cons 5 (cons 7 empty)))))
(check-expect (prime-range 10 1) empty)

(check-expect (prime-range 1 15)
                       (cons 2 (cons 3 (cons 5 (cons 7 (cons 11 (cons 13 empty)))))))
(check-expect (prime-range 1 19)
                       (cons 2 (cons 3 (cons 5 (cons 7 (cons 11 (cons 13 (cons 17 (cons 19 empty)))))))))