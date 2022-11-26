(defproject clojure-wc "0.1.0"
  :description "wc"
  :url "https://github.com/berquerant/training-wc"
  :dependencies [[org.clojure/clojure "1.11.1"]]
  :main ^:skip-aot clojure-wc.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all
                       :jvm-opts ["-Dclojure.compiler.direct-linking=true"]}})
