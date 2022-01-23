#!/bin/bash

python generate.py \
  --title "Lecture 1: Introduction" \
  --dst ../lecture01 \
  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/11 Introduction/11.Introduction.0.key" \
  --base-url "https://mlvu.github.io/lecture01" \
  --pdf-link "https://mlvu.github.io/lectures/11.Introduction.annotated.pdf"

python generate.py \
  --title "Lecture 2: Linear Models and Search" \
  --dst ../lecture02 \
  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/12 Linear Models 1/12.Linear1.key" \
  --base-url "http://mlvu.github.io/lecture02" \
  --pdf-link "https://mlvu.github.io/lectures/12.LinearModels1.annotated.pdf"

#python generate.py \
#  --title "Lecture 3: Model evaluation" \
#  --dst ../lecture03 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/21 Methodology 1/21.Methodology1.key" \
#  --base-url "https://mlvu.github.io/lecture03" \
#  --pdf-link "https://mlvu.github.io/lectures/21.Methodology1.annotated.pdf"

#python generate.py \
#  --title "Lecture 4: Probabilistic models" \
#  --dst ../lecture04 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/31 Probabilistic Models 1/31.ProbabilisticModels1.key" \
#  --base-url "https://mlvu.github.io/lecture04" \
#  --pdf-link "https://mlvu.github.io/lectures/31.ProbabilisticModels1.annotated.pdf"

#python generate.py \
#  --title "Lecture 5: Data Pre-processing" \
#  --dst ../lecture05 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/22 Methodology 2/22.Methodology2.key" \
#  --base-url "https://mlvu.github.io/lecture05" \
#  --pdf-link "https://mlvu.github.io/lectures/22.Methodology2.annotated.pdf"git add home

#python generate.py \
#  --title "Lecture 6: Beyond linear models" \
#  --dst ../lecture06 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/32 Linear Models 2/32.Linear.key" \
#  --base-url "https://mlvu.github.io/lecture06" \
#  --pdf-link "https://mlvu.github.io/lectures/32.LinearModels2.annotated.pdf"

cd ..
git add lecture* style.css index.md script/
git commit -m "Auto-update."
git push