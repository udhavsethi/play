;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname mobster) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define-struct goon (street-name abilities))

;; A Goon is a (make-goon Str Abilities).
;; An Abilities is a (list Nat Nat Nat), where the elements represent
;; Loyalty, Wealth, and Influence.
(define goon-btt (make-goon "Bullet Tooth Tony" (list 8 2 5)))
(define goon-ca (make-goon "Cousin Avi" (list 3 9 8)))
(define goon-btb (make-goon "Boris, the Blade" (list 4 6 7)))
(define goon-fff (make-goon "Franky Four Fingers" (list 5 7 3)))
(define applicant-gg (make-goon "Gorgeous George" (list 3 5 4)))
(define applicant-s (make-goon "Sol" (list 5 7 10)))

;; A Gang is a (listof Goon)
(define my-gang (list goon-btt goon-ca goon-btb goon-fff))

;; A Job is a (list Nat Nat Nat), where the elements represent
;; required Loyalty, required Wealth, and required Influence.
(define job-mule (list 5 0 1))
(define job-financer (list 3 8 5))
(define job-bribe (list 5 6 10))

;; A Job-list is a (listof Job)
(define my-jobs (list job-mule job-financer job-bribe))


;; (eval-goon goon job) consumes a goon and a job. The function produces
;; false if one or more of the goon’s abilities do not meet the requirements
;; for the job. If all requirements are met, the function produces sum of
;; differences between the goon’s abilities and the job’s requirements
;; eval-goon: Goon Job -> (anyof Nat false)
;; example
(check-expect (eval-goon goon-ca job-mule) false)
(check-expect (eval-goon goon-ca job-financer) 4)

(define (eval-goon goon job)
  (cond
    [(or (< (first (goon-abilities goon)) (first job))
         (< (second (goon-abilities goon)) (second job))
         (< (third (goon-abilities goon)) (third job))) false]
    [else (+
           (- (first (goon-abilities goon)) (first job))
           (- (second (goon-abilities goon)) (second job))
           (- (third (goon-abilities goon)) (third job)))]))

;; tests
(check-expect (eval-goon goon-fff job-mule) 9)
(check-expect (eval-goon goon-fff job-financer) false)
(check-expect (eval-goon goon-btb job-mule) false)
(check-expect (eval-goon goon-btb job-financer) false)