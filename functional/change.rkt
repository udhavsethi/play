;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname change) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; constants for currency symbols
(define nickel 'nickel)
(define dime 'dime)
(define quarter 'quarter)
(define loonie 'loonie)
(define toonie 'toonie)

;; constants for currency values
(define nickel-val 5)
(define dime-val 10)
(define quarter-val 25)
(define loonie-val 100)
(define toonie-val 200)


;; (make-change cents) consumes consumes a value in cents and
;; produces a list of currency symbols adding up to that value.
;; make-change: Nat -> (listof Sym)
;; example:
(check-expect (make-change 11) (cons 'dime empty))
(check-expect (make-change 26) (list 'quarter))

(define (make-change cents)
  (cond
    [(> (quotient cents toonie-val) 0) (cons toonie (make-change (- cents toonie-val)))]
    [(> (quotient cents loonie-val) 0) (cons loonie (make-change (- cents loonie-val)))]
    [(> (quotient cents quarter-val) 0) (cons quarter (make-change (- cents quarter-val)))]
    [(> (quotient cents dime-val) 0) (cons dime (make-change (- cents dime-val)))]
    [(> (quotient cents nickel-val) 0) (cons nickel (make-change (- cents nickel-val)))]
    [(> cents 2) (cons nickel '())]
    [else '()]))

;;tests
(check-expect (make-change 17) (list 'dime 'nickel))
(check-expect (make-change 21) (list 'dime 'dime))
(check-expect (make-change 267) (list 'toonie 'quarter 'quarter 'dime 'nickel))
(check-expect (make-change 367) (list 'toonie 'loonie 'quarter 'quarter 'dime 'nickel))