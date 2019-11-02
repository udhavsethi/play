;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname not-catan) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define-struct inventory (blocks wood sheep wheat rocks))
;; An Inventory is a (make-inventory Nat Nat Nat Nat Nat)
;; requires: wheat >= sheep
;; wheat >= 4

(define-struct cost (blocks wood sheep wheat rocks))
;; A Cost is a (make-cost Nat Nat Nat Nat Nat)


(define (inventory-template inv)
  (... (inventory-blocks blocks) ...
   ... (inventory-wood wood) ...
   ... (inventory-sheep sheep) ...
   ... (inventory-wheat wheat) ...
   ... (inventory-rocks rocks) ...))

(define min-wheat 4)

;; (valid-inventory? inv) consumes Any as an argument and produces true
;; if the argument is a valid Inventory
;; valid-inventory?: Any -> Bool
;; example
(check-expect (valid-inventory? (make-inventory 0 0 5 7 0)) true)
(check-expect (valid-inventory? (make-inventory 0 0 0 0 0)) false)

(define (valid-inventory? inv)
  (cond
    [(< (inventory-wheat inv) (inventory-sheep inv)) false]
    [(< (inventory-wheat inv) min-wheat) false]
    [else true]))

;; tests
(check-expect (valid-inventory? (make-inventory 0 0 4 4 0)) true)
(check-expect (valid-inventory? (make-inventory 0 0 4 4 0)) true)
(check-expect (valid-inventory? (make-inventory 1 1 6 4 1)) false)