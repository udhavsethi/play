;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname functional) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;;*************************************
;;  Functional programming with Racket
;;  Udhav Sethi
;;  University of Waterloo
;;*************************************
;;

;; (make-point x y) consumes two numbers x and y, and produces
;; the list of length 2 containing x and y. 
;; make-point: Num Num -> (listof Num)
(define (make-point x y)
  (cons x (cons y empty)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; (x-coord point) consumes a point and produces its x coordinate
;; x-coord: (listof Num) -> Num
;; Example:
(check-expect (x-coord (make-point 3 1)) 3)
(check-expect (x-coord (make-point 4 2)) 4)

(define (x-coord point)
  (first point))

;; tests
(check-expect (x-coord (make-point 7 9)) 7)
(check-expect (x-coord (make-point 5 6)) 5)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; (y-coord point) consumes a point and produces its y coordinate
;; y-coord: (listof Num) -> Num
;; Example:
(check-expect (y-coord (make-point 3 1)) 1)
(check-expect (y-coord (make-point 4 2)) 2)
(define (y-coord point)
  (first (rest point)))

;; tests
(check-expect (y-coord (make-point 7 9)) 9)
(check-expect (y-coord (make-point 5 6)) 6)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; (increment-x point number) consumes a point and increases the x
;; coordinate of the point by number
;; make-step: (listof Num) Nat -> (listof Num)
;; Example:
(check-expect (increment-x (make-point 0 0) 4) (make-point 4 0))
(check-expect (increment-x (make-point 8 1) 5) (make-point 13 1))

(define (increment-x point number)
  (cons (+ (x-coord point) number) (cons (y-coord point) empty)))

;; tests
(check-expect (increment-x (make-point 2 3) 4) (make-point 6 3))
(check-expect (increment-x (make-point 1 1) 5) (make-point 6 1))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; (increment-y point number) consumes a point and increases the y
;; coordinate of the point by number
;; make-step: (listof Num) Nat -> (listof Num)
;; Example:
(check-expect (increment-y (make-point 0 0) 4) (make-point 0 4))
(check-expect (increment-y (make-point 8 1) 5) (make-point 8 6))

(define (increment-y point number)
  (cons (x-coord point) (cons (+ (y-coord point) number) empty)))

;; tests
(check-expect (increment-y (make-point 2 3) 4) (make-point 2 7))
(check-expect (increment-y (make-point 1 1) 5) (make-point 1 6))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; (below-line? left right point) consumes 3 points left, right and point,
;; and produces true if point lies below the line formed by left and right,
;; and false otherwise.
;; below-line?: (listof Num) (listof Num) (listof Num) -> Bool
;; Example:
(check-expect (below-line? (make-point 0 1) (make-point 1 1) (make-point 0 0)) true)
(check-expect (below-line? (make-point 0 1) (make-point 1 1) (make-point 0 2)) false)

(define (below-line? left right point)
    (cond
    [(<= (- (- (y-coord point) (y-coord left)) (* (/ (- (y-coord right) (y-coord left)) (- (x-coord right) (x-coord left))) (- (x-coord point) (x-coord left)))) 0) true]
    [else false]))

;; tests
(check-expect (below-line? (make-point 0 1) (make-point 1 1) (make-point 2 0)) true)
(check-expect (below-line? (make-point 0 1) (make-point 1 1) (make-point 11 0)) true)
(check-expect (below-line? (make-point 0 2) (make-point 1 1) (make-point 0 0)) true)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; (below-spline? left right point) consumes 3 points left, right and point,
;; and produces true if point lies between the curve formed by (0,0), left, right, and (10,0)
;; and the x-axis, and false otherwise.
;; below-spline?: (listof Num) (listof Num) (listof Num) -> Bool
;; Example:
(check-expect (below-spline? (make-point 1 1) (make-point 9 1) (make-point 0 1)) false)
(check-expect (below-spline? (make-point 1 1) (make-point 9 1) (make-point 1 0)) true)

(define (below-spline? left right point)
    (cond
    [(and (below-line? (make-point 0 0) left point) (below-line? left right point) (below-line? right (make-point 10 0) point)) true]
    [else false]))

;;tests
(check-expect (below-spline? (make-point 1 1) (make-point 9 1) (make-point 4 1)) true)
(check-expect (below-spline? (make-point 1 1) (make-point 9 1) (make-point 11 0)) false)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; (make-step point direction distance) consumes a starting point, a direction
;; (a symbol, either ’N, ’S, ’E, or ’W) and a distance (a positive number) and
;; produces a new point which is the position after moving the specified distance
;; in the specified direction.  
;; make-step: arr sym Nat -> arr
;; Example:
(check-expect (make-step (make-point 2 3) 'E 2) (make-point 4 3))
(check-expect (make-step (make-point 2 3) 'N 1) (make-point 2 4))

(define (make-step point direction distance)
    (cond
    [(equal? direction 'E) (increment-x point distance)]
    [(equal? direction 'W) (increment-x point (* distance -1))]
    [(equal? direction 'N) (increment-y point distance)]
    [(equal? direction 'S) (increment-y point (* distance -1))]))

;;tests
(check-expect (make-step (make-point 2 3) 'E 5) (make-point 7 3))
(check-expect (make-step (make-point 2 3) 'W 5) (make-point -3 3))
(check-expect (make-step (make-point 2 3) 'N 5) (make-point 2 8))
(check-expect (make-step (make-point 2 3) 'S 5) (make-point 2 -2))
