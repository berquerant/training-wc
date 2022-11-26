(ns clojure-wc.core
  (:gen-class)
  (:require [clojure.string :refer [split]]))

(defstruct Count :line :word :char)

(defn add-Count
  [self other]
  (struct Count
          (+ (:line self) (:line other))
          (+ (:word self) (:word other))
          (+ (:char self) (:char other))))

(defn new-Count
  [line word char]
  (struct Count line word char))

(defn zero-Count
  "Return a zero of Count."
  []
  (new-Count 0 0 0))

(defn count-char
  "Return a number of characters."
  [line]
  (count (.getBytes line)))

(defn count-word
  "Return a number of words."
  [line]
  (cond
    (= "" line) 0
    :else (count (split (.trim line) #"\s+"))))

(defn line-to-Count
  [line]
  "Return a new Count."
  (new-Count
   1
   (count-word line)
   (+ 1 (count-char line)))) ;; TODO: fix newline

(defn run-wc
  [buffered-reader]
  (reduce add-Count (zero-Count)
          (for [line (line-seq buffered-reader)] ;; TODO: count newlines
            (line-to-Count line))))

(defn -main
  [& args]
  (let [result (run-wc (java.io.BufferedReader. *in*))]
    (printf "%d %d %d\n"
            (:line result) (:word result) (:char result))))
