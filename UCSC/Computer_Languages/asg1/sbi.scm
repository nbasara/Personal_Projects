#!/afs/cats.ucsc.edu/courses/cse112-wm/usr/racket/bin/mzscheme -qr
;; $Id: sbi.scm,v 1.13 2020-01-10 12:51:12-08 - - $
;; 
;; NATHAN BASARA 
;; nbasara
;;
;;
;; NAME
;;    sbi.scm - silly basic interpreter
;;
;; SYNOPSIS
;;    sbi.scm filename.sbir
;;
;; DESCRIPTION
;;    The file mentioned in argv[1] is read and assumed to be an SBIR
;;    program, which is the executed.  Currently it is only printed.
;;

;;
;; Given Functions
;;
(define *stdin* (current-input-port))
(define *stdout* (current-output-port))
(define *stderr* (current-error-port))

(define *run-file*
    (let-values
        (((dirpath basepath root?)
            (split-path (find-system-path 'run-file))))
        (path->string basepath))
)

(define (die list)
    (for-each (lambda (item) (display item *stderr*)) list)
    (newline *stderr*)
    (exit 1)
)

(define (usage-exit)
    (die `("Usage: " ,*run-file* " filename"))
)

(define (readlist-from-inputfile filename)
    (let ((inputfile (open-input-file filename)))
         (if (not (input-port? inputfile))
             (die `(,*run-file* ": " ,filename ": open failed"))
             (let ((program (read inputfile)))
                  (close-input-port inputfile)
                         program))))

(define (dump-stdin)
    (let ((token (read)))
         (printf "token=~a~n" token)
         (when (not (eq? token eof)) (dump-stdin))))




;;;;
;;;;
;;;;

;; Defining hash tables

(define *func-table*  (make-hash))
(define *var-table*   (make-hash))
(define *array-table* (make-hash))
(define *label-table* (make-hash))

;; put things in the table

(define (put-func! key value)
  (hash-set! *func-table* key value)
  )
(define (put-var! key value)
  (hash-set! *var-table* key value)
  )
(define (put-array! key value)
  (hash-set! *array-table* key value)
  )
(define (put-label! key value)
  (hash-set! *label-table* key value)
  )
(define(get-label key)
  (hash-ref *label-table* key)
  )

;;Line numbers

(define (myLabels program)
    (for-each (lambda (line)
        (cond ((= (length line) 3)
                (put-label! (cadr line) (- (car line)1))
               )
            ((= (length line) 2)
                (when (not(pair? (cadr line)))
                    (put-label! (cadr line) (- (car line) 1))
                   )
             )
            )
           )
        program)
  )

;;evaluates goto
(define (evalgoto lable program)
  (myLine program (get-lable (car lable)))
  )

;;evaluates print
(define (evalPrint myString)
  (map (lambda (x) (display (myExpression x))) myString)
  (newline)
  )

;;evaluates input
(define (evalInput myString)
  (define (evalInput. myString count)
      (if (null? (car myString)) 
          (put-func! 'icount count)
          (let ((token (read)))
            (cond ((eof-object? token)
                (put-func! 'icount (- 1)))
              (else
                (cond ((number? token) 
                  (set! count (+ count 1))
                  (put-func! (car myString) token) 
                  (put-func! 'icount count)
                       )
                (else 
                  (printf "Bad Token")
                 )
                      )
      (when (not (null? (cdr myString))) (evalInput. (cdr myString) count))
               )
              )
            )
          )
    )
  (evalInput. myString 0)
  )

;;evaluates dim
(define (evalDim expression)
  (if (pair? expression)
    (let ((array (car expression)))
      (put-func! (car array) (make-vector (myExpression (cadr array))))
      )
    (die "Invalid Array Declaration : " expression)
      )
  )

;;evaluates let
(define (evalLet arg)
    (put-func! (car arg) (myExpression (cadr arg)))
  )

;filing func table
(for-each 
     (lambda (pair) (put-func! (car pair) (cadr pair)))
     `(
       (+ ,+) 
       (- ,-) 
       (* ,*) 
       (/ ,/) 
       (sin ,sin)
       (cos ,cos)
       (tan ,tan)
       (asin ,asin)
       (acos ,acos)
       (atan ,atan)
       (abs ,abs)
       (sqrt ,sqrt)
       (^ ,expt)
       (log ,log)
       (exp ,exp)
       (ceiling ,ceiling)
       (floor   ,floor)
       (round   ,round)
       (<= ,<=) 
       (>= ,>=) 
       (= ,=) 
       (> ,>)
       (< ,<)
       (log10   ,(lambda (x) (/ (log x) (log 10.0))))
       (log10_2 0.301029995663981)
       (sqrt_2  1.414213562373095)
       (e       2.718281828459045)
       (pi      3.141592653589793)
       (print ,evalPrint)
       (dim   ,evalDim)
       (input ,evalInput)
       (let   ,evalLet)
       (goto  ,evalgoto)
       (if ,(void))
       )
     )

(define (write-program-by-line filename program)
    (printf "==================================================~n")
    (printf "~a: ~s~n" *run-file* filename)
    (printf "==================================================~n")
    (printf "(~n")
    (for-each (lambda (line) (printf "~s~n" line)) program)
    (printf ")~n")
   
  )


;;Takes a number and evaluates the line
(define (myLine program num)
  (when (< num (length program))
    (let* ((line (list-ref program num)) (Len (length line)))
      (cond ((= Len 3)
          (myFunction program (caddr line) num)
             )
        ((and(= Len 2)(not(hash-has-key? *label-table* (cadr line))))
          (myFunction program (cadr line) num)
         )
        (else
          (myLine program (+ num 1))
         )
        )
      )
     )
  )


;;Finds the function and then passes off the expression
(define (myFunction program address num)  
  (when (not (hash-has-key? *func-table* (car address))) 
    (die '((car a) " is not a valid instruction.")))
  (cond ((eq? (car address) 'goto)   
      (if(hash-has-key? *label-table* (cadr address)) 
        (myLine program (hash-ref *label-table* (cadr address)))
        (die '("Bad Label : " (cadr intable)))
         )
     )
    ((eq? (car address) 'if)
      (if (myExpression (cadr address))
        (myLine program (hash-ref *label-table* (caddr address)))
        (myLine program (+ num 1))
          )
     )
    (else
      ((hash-ref *func-table* (car address)) (cdr address))
      (myLine program (+ num 1))
     )
   )
  )

;takes the given expression from hash table and then performs the function
(define (myExpression address)
  (cond ((number? address)(+ address 0.0))
    ((string? address) address)((hash-has-key? *func-table* address)
    (hash-ref *func-table* address))
    ((pair? address)(define func (car address))
      (if (hash-has-key? *func-table* func)
        (let ((X (hash-ref *func-table* func)))
          (cond ((vector? X)
            (when (not(null? (cdr address)))
             (define num (myExpression (cadr address)))
              (if (and( < num (vector-length X))(number? num))
                  (vector-ref X num)
                  (die '("Bad pointer: " func ))
                  )
                  )
                 )
                  ((procedure? X)
                      (apply X (map myExpression (cdr address)))
                   )
                (else
                    (die '("bad expression : " address)))
                )
          )
          (die '("What is?: " func)))
     )
        (else
          (die '("Bad: " address)))
        )
)





(define (main arglist)
    (if (or (null? arglist) (not (null? (cdr arglist))))
        (usage-exit)
        (let* ((sbprogfile (car arglist))
               (program (readlist-from-inputfile sbprogfile)))
              ;;(write-program-by-line sbprogfile program)))
              (myLabels program)
              (myLine program 0)))
  )

(if (terminal-port? *stdin*)
    (main (vector->list (current-command-line-arguments)))
    (printf "sbi.scm: interactive mode~n"))









