#!/bin/bash
#
#python generate.py \
#  --title "Course details" \
#  --dst ../lecture00 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/00 Course details/CourseDetails.2021.key" \
#  --base-url "https://mlvu.github.io/lecture00" \
#  --pdf-link "https://mlvu.github.io/lectures/Course details.2021.pdf"
#
#python generate.py \
#  --title "Lecture 1: Introduction" \
#  --dst ../lecture01 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/11 Introduction/11.Introduction.0.key" \
#  --base-url "https://mlvu.github.io/lecture01" \
#  --pdf-link "https://mlvu.github.io/lectures/11.Introduction.annotated.pdf"
#
#python generate.py \
#  --title "Lecture 2: Linear Models and Search" \
#  --dst ../lecture02 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/12 Linear Models 1/12.Linear1.key" \
#  --base-url "http://mlvu.github.io/lecture02" \
#  --pdf-link "https://mlvu.github.io/lectures/12.LinearModels1.annotated.pdf"

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
#  --pdf-link "https://mlvu.github.io/lectures/22.Methodology2.annotated.pdf"

#python generate.py \
#  --title "Lecture 6: Beyond linear models" \
#  --dst ../lecture06 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/32 Linear Models 2/32.Linear.key" \
#  --base-url "https://mlvu.github.io/lecture06" \
#  --pdf-link "https://mlvu.github.io/lectures/32.LinearModels2.annotated.pdf"

#python generate.py \
#  --title "Lecture 7: Deep learning" \
#  --dst ../lecture07 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/41 Deep Learning 1/32.DeepLearning1.key" \
#  --base-url "https://mlvu.github.io/lecture07" \
#  --pdf-link "https://mlvu.github.io/lectures/41.DeepLearning1.annotated.pdf"

#python generate.py \
#  --title "Lecture 8: Density estimation" \
#  --dst ../lecture08 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/42 Probabilistic Models 2/42.ProbabilisticModels2.3.key" \
#  --base-url "https://mlvu.github.io/lecture08" \
#  --pdf-link "https://mlvu.github.io/lectures/42.ProbabilisticModels2.annotated.pdf"
#
#python generate.py \
#  --title "Lecture 9: Deep generative models" \
#  --dst ../lecture09 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/51 Deep Learning 2/51.DeepLearning2.key" \
#  --base-url "https://mlvu.github.io/lecture09" \
#  --pdf-link "https://mlvu.github.io/lectures/51.Deep%20Learning2.annotated.pdf"
#
#python generate.py \
#  --title "Lecture 10: Trees and ensembles" \
#  --dst ../lecture10 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/52 Tree Models/52.Trees.key" \
#  --base-url "https://mlvu.github.io/lecture10" \
#  --pdf-link "https://mlvu.github.io/lectures/52.Trees.annotated.pdf"
#
#python generate.py \
#  --title "Lecture 11: Sequences" \
#  --dst ../lecture11 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/61 Sequences/61.SequentialData.1.key" \
#  --base-url "https://mlvu.github.io/lecture11" \
#  --pdf-link "https://mlvu.github.io/lectures/61.SequentialModels.annotated.pdf"

#python generate.py \
#  --title "Lecture 12: Embedding models" \
#  --dst ../lecture12 \
#  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/62 Matrices/62.Matrices.key" \
#  --base-url "https://mlvu.github.io/lecture12" \
#  --pdf-link "https://mlvu.github.io/lectures/62.Matrices.annotated.pdf"

python generate.py \
  --title "Lecture 13: Reinforcement learning" \
  --dst ../lecture13 \
  --source "/Users/peter/Dropbox/onderwijs/Machine Learning/Lectures/71 Reinforcement Learning/71.ReinforcementLearning.key" \
  --base-url "https://mlvu.github.io/lecture13" \
  --pdf-link "https://mlvu.github.io/lectures/71.Reinforcement%20Learning.annotated.pdf"

cd ..
git add lecture* style.css index.md script/ mlvu.script.js
git commit -m "Auto-update."
git push