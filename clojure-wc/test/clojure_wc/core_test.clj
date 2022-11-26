(ns clojure-wc.core-test
  (:require [clojure.test :refer :all]
            [clojure-wc.core :refer :all]))

(defmacro -test-count-word
  [title line want]
  `(testing ~title
     (is (= ~want (count-word ~line)))))

(deftest test-count-word
  (-test-count-word "empty line" "" 0)
  (-test-count-word "just a word" "word" 1)
  (-test-count-word "two words" "no where" 2)
  (-test-count-word "splitted by spaces" "splitted  by spaces" 3)
  (-test-count-word "ignore prefix space" "  prefix" 1)
  (-test-count-word "ignore postfix space" "postfix " 1))

(deftest test-add-Count
  (is (new-Count 2 4 7) (add-Count
                         (new-Count 1 3 4)
                         (new-Count 1 1 3))))

(defn into-buffered-reader
  [input]
  (java.io.BufferedReader. (java.io.InputStreamReader. (java.io.ByteArrayInputStream. (.getBytes input)))))

(defmacro -test-run-wc
  [title input want]
  `(testing ~title
     (is (= ~want ~(run-wc (into-buffered-reader input))))))

(deftest test-run-wc
  (-test-run-wc "empty input" "" (new-Count 0 0 0))
  (-test-run-wc "a newline" "a\nb cd" (new-Count 2 3 7)))
