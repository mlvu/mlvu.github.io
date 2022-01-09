---
title: "Lecture 3: Model evaluation"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 3: Model evaluation</li>
            <li><a href="#video-000">Experiments</a></li>
            <li><a href="#video-028">Evaluation</a></li>
            <li><a href="#video-056">PR, ROC and AUC</a></li>
            <li><a href="#video-077">Social Impact 2</a></li>
            <li><a href="#video-095">Statistical Testing</a></li>
            <li><a href="#video-116">No Free Lunch</a></li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/21.Methodology1.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">
       <section class="video" id="video-000">
           <a class="slide-link" href="https://mlvu.github.io/lecture03#video-0">link here</a>
           <iframe
                src="https://www.youtube.com/embed/hHLDDJJl2v4?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-001">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-001">link here</a>
            <img src="21.Methodology1.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-001" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-002">link here</a>
            <img src="21.Methodology1.key-stage-0002anim0.svg" data-images="21.Methodology1.key-stage-0002anim0.svg,21.Methodology1.key-stage-0002anim1.svg,21.Methodology1.key-stage-0002anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the basic recipe for machine learning again. This week, we’ll discuss what happens before and after. Today: once you’ve trained some models, how do you figure out which of them is best?</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-003">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-003">link here</a>
            <img src="21.Methodology1.key-stage-0003.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll focus mostly on binary classification today (two-class classification). In this case, we can think of the classifier as a detector for one of the classes (like spam, or a disease). We tend to call this class positive. As in “testing positive for a disease.”<br></p><p    >In classification, the main metric of performance is the proportion of misclassified examples (which we’ve already seen). This is called the <strong>error</strong>. The proportion of correctly classified examples is called the <strong>accuracy</strong>.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-003" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-004">link here</a>
            <img src="21.Methodology1.key-stage-0004anim0.svg" data-images="21.Methodology1.key-stage-0004anim0.svg,21.Methodology1.key-stage-0004anim1.png" class="slide-image" />

            <figcaption>
            <p    >You compare models to figure out which is the best. Ultimately, to choose which model to you want to use in <em>production</em>. (This could be literally the production version of a piece of software, or just the model whose predictions you decide to use in the future.)<br></p><p    >Sometimes you are comparing different models types (decisions tree vs linear), but you might also be comparing different ways of configuring the same model type. For instance in the kNN classifier, how many neighbours (<span class="green">k</span>) should we look at to determine our classification?<br></p><p    >With the 2D dataset, we can look at the decision boundary, and make a visual judgment. Usually, that’s not the case: our feature space will have hundreds of dimensions, and we’ll need to <em>measure</em> the performance of a model.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-004" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-005">link here</a>
            <img src="21.Methodology1.key-stage-0005anim0.svg" data-images="21.Methodology1.key-stage-0005anim0.svg,21.Methodology1.key-stage-0005anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the simplest, most straightforward way to compare two classifiers. You just train them both, so see how many examples they get wrong, and pick the one that made fewest mistakes. This is a very simple approach, but it’s basically what we do. <br></p><p    >We just need to consider<strong class="orange red"> a few questions</strong>, to make sure that we can trust our results.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-006">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-006">link here</a>
            <img src="21.Methodology1.key-stage-0006.svg" class="slide-image" />

            <figcaption>
            <p    >We’ve already seen what happens when you evaluate on the <span class="green">training data</span>. A model that fits the training data perfectly may not be much use when it comes to data you haven't seen before.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-007">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-007">link here</a>
            <img src="21.Methodology1.key-stage-0007.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-008">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-008">link here</a>
            <img src="21.Methodology1.key-stage-0008.svg" class="slide-image" />

            <figcaption>
            <p    >So the first thing we do in machine learning is <strong>withhold</strong> some data. We train our classifiers on the <span class="green">training data</span> and test on the <span class="blue">test data</span>. That way, if we get good performance, we know that we’re likely to get a good performance on future data as well, and we haven’t just memorised random fluctuations in the training data.<br></p><p    >How should we split our data? The most important factor is the size in instances of the<span class="blue"> test data</span>. The bigger this number, the more precise our estimate of our model’s error. Ideally, we separate 10 000 test instances, and use whatever we have left over as training data. Unfortunately, this is not always realistic. We’ll look at this a little more later.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-009">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-009">link here</a>
            <img src="21.Methodology1.key-stage-0009.svg" class="slide-image" />

            <figcaption>
            <p    >But even if we withhold some test data, we can still go wrong. We’ll use k nearest neighbours (kNN) as a running example. Remember, kNN assigns the class of the k nearest points. <br></p><p    >k is what is called a <strong>hyperparameter</strong>. We need to choose its value in some way before we run the algorithm. The algorithm doesn't specify how it should be chosen. One way of choosing k is to try a few values, and to see for which k we get the best performance.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-010">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-010">link here</a>
            <img src="21.Methodology1.key-stage-0010.png" class="slide-image" />

            <figcaption>
            <p    >We will use the data from the first lecture as an example. We will take a small subsample of the dataset, so that the effects that we want to illustrate become exaggerated.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-010" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-011">link here</a>
            <img src="21.Methodology1.key-stage-0011anim0.svg" data-images="21.Methodology1.key-stage-0011anim0.svg,21.Methodology1.key-stage-0011anim1.svg,21.Methodology1.key-stage-0011anim2.png,21.Methodology1.key-stage-0011anim3.png" class="slide-image" />

            <figcaption>
            <p    >Here we’ve tested 25 different values of k on the same <span class="blue">test data</span> (using quite a small test set to illustrate the idea). We can see that for k=23, we get the best performance.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-012">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-012">link here</a>
            <img src="21.Methodology1.key-stage-0012.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the best run. Should we conclude that k=23 is definitely a better setting than k=22 or k=24? Should we conclude that we can expect an error of 0.08 on any future data from the same source?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-012" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-013">link here</a>
            <img src="21.Methodology1.key-stage-0013anim0.png" data-images="21.Methodology1.key-stage-0013anim0.png,21.Methodology1.key-stage-0013anim1.png" class="slide-image" />

            <figcaption>
            <p    >In this case, we have some more data from the same source, so we can do the whole experiment again on fresh data. This is a luxury we don't normally have (we normally use all the data we are given). <br></p><p    >What we see is that k=23 no longer gives us the best performance. In fact, we get a quite radically different best value of k.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-014">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-014">link here</a>
            <img src="21.Methodology1.key-stage-0014.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-015">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-015">link here</a>
            <img src="21.Methodology1.key-stage-0015.svg" class="slide-image" />

            <figcaption>
            <p    >The same source of data, the exact same procedure, and these are the results. We were diligent in splitting our dataset and evaluating only on withheld data, and yet if we had done only one run on one dataset, as we normally would, we would have concluded that k=23 is the best setting and that an error of 0.08 can be expected with that value. <br></p><p    >This conclusion, as we can see, is entirely false. This also suggests that if we were to take this k=23 classifier for the last run and try it on a new test dataset (again from the same source), it's error would probably be much higher than the 0.08 we got on the test set. <br></p><p    >So what's happening here?<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-016">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-016">link here</a>
            <img src="21.Methodology1.key-stage-0016.svg" class="slide-image" />

            <figcaption>
            <p    >This is essentially the overfitting problem again. Our method of choosing the hyperparameter <strong>k</strong> is just another learning algorithm. By testing so many values of k on the test data, we are overfitting our choice of k on the test data.<br></p><p    >This is an instance of the<em> multiple testing</em> problem in statistics. We’re testing so many things, that the likelihood of a noticeable effect popping up by chance increases. We are in danger of ascribing meaning to random fluctuations. <br></p><p    >Specifically, in our case, the k=23 classifier <strong>got lucky</strong> on a few examples, that just happened to fall on the right side of the decision boundary. If we draw some new data, the same classifier won't be lucky again. The more different values of k we try, the more we are in danger of this kind of random luck determining which hyperparameters come out as good.<br></p><p    >The simple answer to the problem of multiple testing is<strong> not to test multiple times</strong>.<br></p><p    >see also: <a href="https://www.explainxkcd.com/wiki/index.php/882:_Significant"><strong class="blue">https://www.explainxkcd.com/wiki/index.php/882:_Significant</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-017">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-017">link here</a>
            <img src="21.Methodology1.key-stage-0017.svg" class="slide-image" />

            <figcaption>
            <p    >There are many different approaches to machine learning experimentation, and not every paper you see will follow this approach, but this is the most common one. <br></p><p    >It’s important to mention in your paper that you followed this approach, since the reader can’t usually see it from the presented results.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-018">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-018">link here</a>
            <img src="21.Methodology1.key-stage-0018.svg" class="slide-image" />

            <figcaption>
            <p    >Just to emphasize the important point: the more you use the test data, the less reliable your conclusions become. Figure out what the end of your project is, and do not touch the test data until the end.<br></p><p    >In really important and long-term projects, it’s not a bad idea to withhold multiple test sets. This allows you to still test your conclusions in case you’ve ended up using the original test data too often.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-019">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-019">link here</a>
            <img src="21.Methodology1.key-stage-0019.svg" class="slide-image" />

            <figcaption>
            <p    >Not only does reusing test data mean that you pick the wrong model, it also means that the error estimate you get is probably much lower that the error you would actually get if you gathered some more test data. </p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-019" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-020">link here</a>
            <img src="21.Methodology1.key-stage-0020anim0.svg" data-images="21.Methodology1.key-stage-0020anim0.svg,21.Methodology1.key-stage-0020anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This means that you need to test which model to use, which hyperparameters to give it, and how to extract your features <strong>only on the training data</strong>. In order not to evaluate on the training data for these evaluations, you usually split the training data <strong>again</strong>: into a (new) <strong class="green">training set</strong> and<strong> a validation set</strong>.<br></p><p    >Ideally, your <span>validation data</span> is the same size as your <span class="blue">test set</span>, but you can make it a little smaller to get some more <span class="green">training data</span>.<br></p><p    >This means that you need to <strong>carefully plan your research process</strong>. If you start out with just a single split and keep testing on the same <span class="blue">test data</span>, there’s no going back (you can’t unsee your<span class="blue"> test data</span>). And usually, you don’t have the means to gather some new dataset.<br></p><p    >It’s usually fine in the final run to append the validation data to your training data. This is not always the case however, so if you use a standard benchmark you should check if this is allowed, and if you use new data you should describe carefully whether you do this.<br></p><p    >Note that this approach by itself doesn't in itself <em>prevent</em> multiple testing. It just provides for a final failsafe to detect it. Before you make the decision to try your model on the test data, you should first convince yourself that the results you see are not down to multiple testing. You can do this by not testing too many hyperparameter values, or if you fear that have, by rerunning your experiment on a different train/validation split to double check.<br></p><p    >There's always a bit of a tense moment when you run the experiment on the test data, and you get to find out how close the real numbers you'll get to report are to the numbers you've seen for the validation. However, if your datasets are large, and you haven't done anything strange in the hyperparameter tuning phase, they will usually be very close together.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-021">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-021">link here</a>
            <img src="21.Methodology1.key-stage-0021.svg" class="slide-image" />

            <figcaption>
            <p    >This may seem like a simple principle to follow, but it goes wrong <strong>a lot</strong>. Not just in student papers, also in published research.<br></p><p    >Here’s what you might come across in a bad machine learning paper. In this (fictional) example, the authors are introducing a new method (labeled <em>ours</em>) which has a hyperparameter k. They are claiming that their model beats every baseline, because their numbers are higher (for specific hyperparameters).<br></p><p    >These numbers create three impressions that are not actually validated by this experiment:<br></p><p     class="list-item">That the authors have a better model than the two other methods shown. <br></p><p     class="list-item">That if you want to run the model on dataset 1,  you should use k=3<br></p><p     class="list-item">That if you have data like dataset 1, you can then expect an error of 0.08.<br></p><p    >None of these conclusions can be drawn from this experiment, because we have not ruled out multiple testing.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-022">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-022">link here</a>
            <img src="21.Methodology1.key-stage-0022.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what we should do instead. We should use the training data (with validation withheld) to select our hyperparameters, make a single choice for k for each different dataset, and then estimate the accuracy of only that model. <br></p><p    >Note that the numbers have changed, because in the previous example the authors gave themselves an advantage by multiple testing. With a proper validation split, that advantage disappears. These numbers are lower, but more accurate. (I made these numbers up, but this is the sort of thing you might see)<br></p><p    >Now, we can actually draw the conclusions that the table implies:<br></p><p     class="list-item">On dataset 3, the new method is the best.<br></p><p     class="list-item">If we want to use the method on dataset 3 (or similar data) we should use k=2<br></p><p     class="list-item">If our data is similar to that of dataset 3, we could expect a performance around 0.24<br></p><p    >Even though most people now use this approach, you should still mention exactly what you did in your report (so people don’t assume you got it wrong).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-023">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-023">link here</a>
            <img src="21.Methodology1.key-stage-0023.svg" class="slide-image" />

            <figcaption>
            <p    >After you’ve split off a test and validation set, you may be left with very little <span>training data</span>. If this is the case, you can make better use of your training data by performing<strong> cross-validation</strong>. You split your data into 5 chunks (“folds”) and for each specific choice of hyperparameters that you want to test, you do five runs: each with one of the folds as validation data. You then average the scores of these runs.<br></p><p    >This can be costly (because you need to train five times as many classifiers), but you ensure that every instance has been used as a training example once.<br></p><p    >After selecting your hyperparameters with crossvalidation, you still test once on the<span class="blue"> test data</span>.<br></p><p    >You may occasionally see papers that estimate error of their finally chosen model by cross validation as well (splitting off multiple <span class="blue">test sets</span>), but this is a complicated business, and has fallen out of fashion. We won’t go into in this course.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-024">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-024">link here</a>
            <img src="21.Methodology1.key-stage-0024.svg" class="slide-image" />

            <figcaption>
            <p    >If your data has special attributes, like a meaningful temporal ordering of the instances, you need to take this into account. In the case of temporal data, training on samples that are in the future compared to the test set is unrealistic, so you can’t sample your test set randomly. You need to maintain the ordering.<br></p><p    >Sometimes data has a timestamp, but there’s no meaningful information in the ordering (like in email classification, seeing emails from the future doesn’t usually give you much of an unfair advantage in the task). In such cases, you can just sample the test set randomly.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-024" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-025">link here</a>
            <img src="21.Methodology1.key-stage-0025anim0.svg" data-images="21.Methodology1.key-stage-0025anim0.svg,21.Methodology1.key-stage-0025anim1.svg,21.Methodology1.key-stage-0025anim2.svg,21.Methodology1.key-stage-0025anim3.svg,21.Methodology1.key-stage-0025anim4.svg" class="slide-image" />

            <figcaption>
            <p    >If you want to do cross-validation in such time sensitive data, you’ll have to slice the dataset like this.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-026">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-026">link here</a>
            <img src="21.Methodology1.key-stage-0026.svg" class="slide-image" />

            <figcaption>
            <p    >In general, don’t just apply split testing and cross validation blindly, think about how you will ultimately train and use your model “in production”. Production may be an actual software production environment, or some other place where you intend to employ your model. Your evaluation on the test set is essentially a <em>simulation</em> of that setting. <br></p><p    >If you're doing something in evaluation that you won't be able to do in production (like training on instances from the future), then you are cheating your evaluation. <br></p><p    >Your <span>validation</span> is essentially a simulation of the <span class="blue">evaluation</span>. If you wan accurate validation results, then your validation should mimic the evaluation as closely as possible. <br></p><p    >Here, however, you are allowed to deviate a little. For instance, you can make your validation data a little smaller than your test data. This is a tradeoff: you are reducing the certainty of your validation results, but you are gaining a little extra training data, which will improve your results in the end. Such tradeoffs are fine, so long as you are honest in your final evaluation on the <span class="blue">test data</span>.<br></p><p    ><span>In general, when in doubt</span> make sure the validation setting is an accurate simulation of that setting.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-027">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-027">link here</a>
            <img src="21.Methodology1.key-stage-0027.svg" class="slide-image" />

            <figcaption>
            <p    >Which values should we try for the hyperparameters? So long as we make sure not to look at our test set, we can do what we like. We can try a few values, we can search a grid of values exhaustively, or we can even use methods like random search, or simulated annealing<br></p><p    >It’s important to mention: <strong>trail and error is fine, and it’s the approach that is most often used</strong>. Often, it’s the most effective, because you (hopefully) have an intuitive understanding of what your hyperparameters mean.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-028">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-028">link here</a>
            <img src="21.Methodology1.key-stage-0028.svg" class="slide-image" />

            <figcaption>
            <p    >If you are going to use some kind of automated search, trying a bunch of different combinations of hyperparameter values, then random samples in the hyper parameter space are often better than a grid. This picture neatly illustrates why. If one parameter turns out not to be important, and another does, a grid search restricts us to only three samples over the important parameter, at the cost training nine different models.<br></p><p    >source: <a href="http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf"><strong class="blue">http://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf</strong></a> (recommended reading)<br></p><p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-028">
           <a class="slide-link" href="https://mlvu.github.io/lecture03#video-28">link here</a>
           <iframe
                src="https://www.youtube.com/embed/oZdWt_Mrg_8?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-029">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-029">link here</a>
            <img src="21.Methodology1.key-stage-0029.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we'll look at how to evaluate regression and classification experiments. There will be a few pointers on regression, but the main topic will be classification experiments.<br></p><p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-030">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-030">link here</a>
            <img src="21.Methodology1.key-stage-0030.svg" class="slide-image" />

            <figcaption>
            <p    >One thing to pay attention to is that if you use MSE loss, you may want to <em>report </em>the square root (the RMSE). The RMSE is minimised at the same places as the MSE, but it’s easier to interpret, because it has the same units as the original output value.<br></p><p    >For instance, if your outputs are in meters, then your MSE is measured in square meters, but your RMSE is also measured in meters.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-030" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-031">link here</a>
            <img src="21.Methodology1.key-stage-0031anim0.svg" data-images="21.Methodology1.key-stage-0031anim0.svg,21.Methodology1.key-stage-0031anim1.svg,21.Methodology1.key-stage-0031anim2.svg,21.Methodology1.key-stage-0031anim3.svg,21.Methodology1.key-stage-0031anim4.svg,21.Methodology1.key-stage-0031anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Normally, we train a regression model once, and get one MSE value. The lower the better. <br></p><p    >However this MSE is an estimate of the “true MSE” This is a value we can’t compute, its the true expected performance of our entire method: from sampling data to training the model to computing the performance. If </p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-031" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-032">link here</a>
            <img src="21.Methodology1.key-stage-0032anim0.svg" data-images="21.Methodology1.key-stage-0032anim0.svg,21.Methodology1.key-stage-0032anim1.svg,21.Methodology1.key-stage-0032anim2.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-033">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-033">link here</a>
            <img src="21.Methodology1.key-stage-0033.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a metaphor that is often used to describe bias and variance: a dartboard.<br></p><p    >Remember, this is a metaphor for our RMSE error estimate. That means that normally, we have only one dart and we can’t tell whether our error is due to high bias or high variance. We’ll return to this topic in week 5, in the context of ensemble methods.<br></p><p    >image source: <a href="http://scott.fortmann-roe.com/docs/BiasVariance.html"><strong class="blue">http://scott.fortmann-roe.com/docs/BiasVariance.html</strong></a> (recommended reading)<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-034">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-034">link here</a>
            <img src="21.Methodology1.key-stage-0034.svg" class="slide-image" />

            <figcaption>
            <p    >High bias tends to happen when the model is too simple to follow the true "shape" of the data. Linear models in low-dimensional spaces often have this problem. Here, we see that the data has a slight curve, which is clearly part of its natural pattern, and something the model should learn. Since it's restricted to a line, however, it cannot make this shape.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-035">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-035">link here</a>
            <img src="21.Methodology1.key-stage-0035.svg" class="slide-image" />

            <figcaption>
            <p    >High variance happens when the model has the capacity to follow the shape of the data perfectly, but it does so so perfectly that it tends to get thrown off by small fluctuations. <br></p><p    >Here, the model doesn't just follow the natural curve of the data, it goes in and out of every random fluctuation to model every single point perfectly.<br></p><p    >Even though this model (a regression tree) fits the data perfectly, if we resample the data, we are stuck with all sorts of weird peaks that won’t fit the new data. This is where the <em>variance</em> comes from. The true error varies wildly, because the model captures every single random fluctuation in the data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-036">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-036">link here</a>
            <img src="21.Methodology1.key-stage-0036.svg" class="slide-image" />

            <figcaption>
            <p    >We will see techniques for all of these in the coming weeks. Note that often, it really is a tradeoff: reducing the bias, increases the variance and vice versa.<br></p><p    >For some algorithms, there is a single parameter that allows us to make the bias/variance tradeoff. kNN is one example: low k values give us high variance, high k values give us high bias. </p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-037">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-037">link here</a>
            <img src="21.Methodology1.key-stage-0037.svg" class="slide-image" />

            <figcaption>
            <p    >In a later lecture, we'll look at <strong>ensembling</strong>. This is a method that allows us to combine different models, so as to control the problems of high bias and high variance.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-038">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-038">link here</a>
            <img src="21.Methodology1.key-stage-0038.svg" class="slide-image" />

            <figcaption>
            <p    >Let's now move to classification. We'll start by explaining these four topics.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-039">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-039">link here</a>
            <img src="21.Methodology1.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >One thing we already know how to estimate: the error. We simply count how many mistakes the classifier makes (either on the validation or the test data).<br></p><p    >Imagine that somebody tells you about a machine learning project they’re doing, and they proudly state that they get a classification error (on their validation set) of <span class="green">0.05</span> (5% of the validation set is misclassified). Should you be impressed?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-040">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-040">link here</a>
            <img src="21.Methodology1.key-stage-0040.svg" class="slide-image" />

            <figcaption>
            <p    >As an example, let’s look at a recurring discussion in the Dutch media: should all women over 50 be screened for breast cancer. This is an analogy for classification: the instances are people and the target label is “<span class="blue">has cancer</span>” or “<span class="orange red">has no cancer</span>.” <br></p><p    >If 1 percent of patients have cancer, an error of 0.05 is not very impressive. We can do much better by just saying that nobody has cancer.<br></p><p    >source: <a href="https://www.volkskrant.nl/wetenschap/redt-preventieve-screening-op-borstkanker-levens~a3761451/"><strong class="blue">https://www.volkskrant.nl/wetenschap/redt-preventieve-screening-op-borstkanker-levens~a3761451/</strong></a></p><p    ><a href="https://www.volkskrant.nl/wetenschap/redt-preventieve-screening-op-borstkanker-levens~a3761451/"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-041">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-041">link here</a>
            <img src="21.Methodology1.key-stage-0041.png" class="slide-image" />

            <figcaption>
            <p    >So the next time you see a headline like this, your first question should be: what was the class distribution in the training data? If 90% of the cases in the training data are acquittals, this is not a very impressive result.<br></p><p    >As it happens, in this case the classes were balanced 50/50, so 80 percent is at least notable. However, now we have a classifier trained on artificially balanced data. In a production environment (whatever that means here), the classes are likely not balanced 50/50, so this specific classifier will be of no further use.<br></p><p    >Here is the original paper: <a href="https://peerj.com/articles/cs-93/#fn-6"><strong class="blue">https://peerj.com/articles/cs-93/#fn-6</strong></a> There are some issues with this  research beyond the class balance. </p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-042">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-042">link here</a>
            <img src="21.Methodology1.key-stage-0043.svg" class="slide-image" />

            <figcaption>
            <p    >Imagine a classifier for breast cancer with 95% accuracy. This may seem impressive at first sight, but the prevalence of breast cancer among women over 50 (the population that is regularly tested) is about 1%. This means that<strong> a classifier that classifies nobody as having cancer</strong> gets 99% accuracy. The range of accuracies that are interesting at all is between 99% and 100%.<br></p><p    >This is called <strong>class imbalance</strong>, and it's the first thing to take into account when you are deciding how to evaluate on a particular data set.<br></p><p    >Another reason to mistrust accuracy is<strong> cost imbalance</strong>. There are two types of misclassification: diagnosing a healthy person with cancer and diagnosing a person with cancer as healthy. Both come with a cost but not the same cost. We can either miss a cancer diagnosis, which means the cancer will be caught much later and be much harder to treat. However, diagnosing a healthy person with cancer means they will be sent for unnecessary invasive testing and suffer great psychological stress. The cost of this is much less that the cost of missing a positive, but it isn't zero.<br></p><p    >Spam classification is another example: both misclassifications should be avoided, but having a genuine email land in your spam is much worse than having to delete a spam email from your inbox.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-043">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-043">link here</a>
            <img src="21.Methodology1.key-stage-0044.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a pretty imbalanced dataset (though still not as imbalanced as the cancer/not cancer problem). It looks pretty difficult. What would be a good performance on this task?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-044">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-044">link here</a>
            <img src="21.Methodology1.key-stage-0045.svg" class="slide-image" />

            <figcaption>
            <p    >Something like an error of 0.05 might sound pretty good, but on an imbalanced dataset like this, there is a very simple classifier that gets that performance easily: the<strong> majority class classifier</strong><br></p><p    >The majority class classifier is an example of a <strong>baseline</strong>, a simple method that is not meant to be used as a real model, but that can help you calibrate the performance scores. In this case, it tells you that you’re really only interested in in the range from 0  to 0.05. Any higher error than that is pretty useless.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-045">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-045">link here</a>
            <img src="21.Methodology1.key-stage-0046.svg" class="slide-image" />

            <figcaption>
            <p    >Here is another way that class imbalance can screw things up for you. You might think you have a pretty decent amount of data with 10 000 instances. However if you split off a test set of 1 000 instances, you 're be left with just 50 instances of the<span class="orange red"> </span><span class="blue">positive</span> class in your data. Practically, your final evaluation will just be a question of how many of these 50 <span class="blue">positives</span> you detect. This means that you can really only have 50 “levels of performance” that you can distinguish between.<br></p><p    >You can make a bigger test set of course (and you probably should) but that leads to problems in your training data. Since you’re essentially building a detector for <span class="blue">positives</span>, it doesn’t help if you can only give it 100 examples of what a<span class="blue"> positive</span> looks like.<br></p><p    >In the next lecture, we’ll look at some tricks we can use to boost performance on such imbalanced data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-046">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-046">link here</a>
            <img src="21.Methodology1.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    >The second thing we need to consider when interpreting errors is <strong>cost imbalance</strong>.<br></p><p    >In all these cases, one misclassification one way costs much more than a misclassification the other way. But both cost <em>something</em>. The time of an expert reviewer is not free, even though five minutes of his time may be much cheaper than the cost of letting a single fraud go unchecked. In such a case, you may decide that missing one fraud is as costly as having an expert review 500 harmless transactions. This is then the general balance you are hoping for: one false negative for every 500 false positives.<br></p><p    >If you’re lucky, both types of misclassification have the same unit, and you can turn your error (an estimate of the number of misclassifications) into a domain specific evaluation function (like estimated dollars lost, or time saved). <strong>You simply assign a cost to each type if misclassification, and multiply it by how often that misclassification occurs in the test set. </strong>The total is the evaluation function you want to minimize.<strong><br></strong></p><p    >If the units are not the same (money saved vs. lives saved) making such a choice can seem very unethical. On the other hand, any classifier you decide to deploy will <em>implicity </em>make such a choice even if you don't do the sums yourselves. Even if you decide not to use machine learning, the alternative (a doctor using their own judgement) is also a “classifier”, with its own cost balance.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-047">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-047">link here</a>
            <img src="21.Methodology1.key-stage-0048.png" class="slide-image" />

            <figcaption>
            <p    >Cost imbalance is particularly important when we consider matters of social impact. If we predict a person’s sex from their physical appearance perfectly, and we use that as a prediction for their gender, we have 99% accuracy. <br></p><p    >However the 1% we then misclassify is precisely that part of the part of the population for which gender is a sensitive attribute. Just because our classifier has high accuracy, doesn’t mean it can do no harm. In a large part because the mistakes it makes are not uniformly distributed. They are focused squarely on the vulnerable part of the population.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-048">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-048">link here</a>
            <img src="21.Methodology1.key-stage-0049.svg" class="slide-image" />

            <figcaption>
            <p    >The best thing to do under class and cost imbalance, is to look at your performance in more detail. We’ll look at six different ways to measure classifier performance.<br></p><p    >Most of these are only relevant if you have class or cost imbalance. If you have a nice, balanced dataset, it’s likely that error or accuracy is all you need.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-048" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-049">link here</a>
            <img src="21.Methodology1.key-stage-0051anim0.svg" data-images="21.Methodology1.key-stage-0051anim0.svg,21.Methodology1.key-stage-0051anim1.svg,21.Methodology1.key-stage-0051anim2.svg" class="slide-image" />

            <figcaption>
            <p    >This is s a <strong>confusion matrix</strong> (also known as a contingency table). It doesn’t give you a single number, so it’s more difficult to compare two classifiers by their confusion matrices, but it’s a good way to get insight into what your classifier is actually doing. <br></p><p    >Note that we are getting the two types of mistakes (false positives and false negatives) along the second diagonal. If we have cost imbalance, the balance between these two values gives us a quick insight into how well the classifier is aligned with our estimate for the misclassification costs.<br></p><p    >You can plot the confusion matrix for either the <span class="green">training</span>, <span>validation</span> or <span>test</span> data. All three can be informative.<br></p><p    >The margins of the table give us four totals: the actual number of each class present in the data, and the number of each class predicted by the classifier.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-050">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-050">link here</a>
            <img src="21.Methodology1.key-stage-0052.svg" class="slide-image" />

            <figcaption>
            <p    >Here we see the confusion matrix for the majority class baseline (the classifier that calls everything positive) in a problem with high class imbalance.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-051">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-051">link here</a>
            <img src="21.Methodology1.key-stage-0053.svg" class="slide-image" />

            <figcaption>
            <p    >Precision and recall are two metrics that express a tradeoff between the two types of mistakes.<br></p><p    ><strong>Precision</strong>: what proportion of the returned positives are actually positive?<br></p><p    ><strong>Recall</strong>: what proportion of the existing positives did we find?<br></p><p    >The idea is that we usually want to find as many positives as possible, so we should be eager to label things positive, increasing the recall, but if we are too eager, we will label lots of negatives as positive as well, which will hurt our precision. Our main challenge in designing a classifier in the face of cost and class imbalance, is to find the right tradeoff between precision and recall.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-052">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-052">link here</a>
            <img src="21.Methodology1.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >It always takes me a minute to figure out what precision and recall mean in any given situation, and I usually consult this diagram from Wikipedia to help me out. <br></p><p    >The idea is that the goal of the classifier is to select the positives in the dataset. The more it selects, the higher its recall, but the lower its precision, as more negatives end up in the selection.<br></p><p    >source: By Walber - own work, CC BY-SA 4.0, <a href="https://commons.wikimedia.org/w/index.php?curid=36926283"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=36926283</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-053">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-053">link here</a>
            <img src="21.Methodology1.key-stage-0055.svg" class="slide-image" />

            <figcaption>
            <p    >There are many more metrics which you can derive from the confusion matrix. Wikipedia provides a helpful table, in case you ever come across them. For most purposes, <strong>precision</strong>, <strong>recall</strong>, <strong>accuracy</strong> and <strong>balanced accuracy</strong> are sufficient.<br></p><p    >Note that some terms, like recall, go by<em> many</em> different names.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-054">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-054">link here</a>
            <img src="21.Methodology1.key-stage-0056.svg" class="slide-image" />

            <figcaption>
            <p    >All of these metrics can be applied to different datasets. When we compute (say) accuracy on the test set, we talk about<strong> test accuracy</strong>. This is computed, only once,  at the very end of our project, to show that our conclusions are true.<br></p><p    >When we compute it on the validation set we call it <strong>validation accuracy</strong>. We compute this to help us choose good hyperparameters.<br></p><p    >And, predictably, when we compute it on the training data, we call it <strong>training accuracy</strong>. Remember that in the first lecture I said, emphatically, that you should never judge your model on how it performs on the training set. Why then, would you ever want to compute the training accuracy (or any other metrics on the training data)?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-054" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-055">link here</a>
            <img src="21.Methodology1.key-stage-0057anim0.svg" data-images="21.Methodology1.key-stage-0057anim0.svg,21.Methodology1.key-stage-0057anim1.svg,21.Methodology1.key-stage-0057anim2.svg,21.Methodology1.key-stage-0057anim3.svg,21.Methodology1.key-stage-0057anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The answer is that the difference between your validation error and your training error, will tell you whether or not your model is <strong>overfitting</strong> (matching the data too well) or underfitting (not matching the data well enough).<br></p><p    >The difference between the training and validation sets is called the generalization gap. As in, it's the amount of performance that won't generalize to data that isn't your training data.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-056">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-056">link here</a>
            <img src="21.Methodology1.key-stage-0058.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-056">
           <a class="slide-link" href="https://mlvu.github.io/lecture03#video-56">link here</a>
           <iframe
                src="https://www.youtube.com/embed/UrqPyE4H2bI?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-057">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-057">link here</a>
            <img src="21.Methodology1.key-stage-0059.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-058">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-058">link here</a>
            <img src="21.Methodology1.key-stage-0060.svg" class="slide-image" />

            <figcaption>
            <p    >Clearly, we want to get both the precision and the recall as high as possible. Since we don’t know how to balance them (this depends on domain specific preferences, i.e. cost imbalance), we can visualize both objectives together in the plane. Each classifier represents a point.<br></p><p    >The <span>points in the corners</span> represent our most extreme options. We can easily get a 1.0 recall by calling everything positive (ensuring that all true positives are among the selected elements). We can get a very likely 1.0 precision by calling only the instance we’re most sure about positive. If we’re wrong we get a precision of 0, but if we’re right we get 1.0.<br></p><p    >Whether we prefer the left or the right <span class="green">green classifier</span> depends on our preferences. However, whatever our preference, we always prefer either <span class="green">green classifier</span> to the<span class="blue"> blue classifier</span>.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-058" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-059">link here</a>
            <img src="21.Methodology1.key-stage-0061anim0.svg" data-images="21.Methodology1.key-stage-0061anim0.svg,21.Methodology1.key-stage-0061anim1.svg" class="slide-image" />

            <figcaption>
            <p    >We  call accurately classified instances <strong>true positives</strong> and<strong> </strong><strong>true negatives</strong>. Misclassifications are called <strong>false positives</strong> and <strong>false negatives</strong>.<br></p><p    >Many performance measures can be computed from the confusion matrix (including the error and accuracy).<br></p><p    >A good pair of metrics to consider, especially when we have class imbalance, is the true and false positive rate:<br></p><p    ><strong>true positive rate</strong>: what proportion of the actual positives did we get <em>right</em>. The higher the better. I.e. How many of the people with cancer did we detect.<br></p><p    ><strong>false positive rate</strong>: what proportion of the actual negatives did we get <em>wrong</em> (by labelling them as positives). The lower the better. I.e. How many healthy people did we diagnose with cancer.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-060">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-060">link here</a>
            <img src="21.Methodology1.key-stage-0062.svg" class="slide-image" />

            <figcaption>
            <p    >We want to get the TPR as high as possible, and the FPR as low as possible. That means the TPR/FPR space has the best classifier in the top left corner. This space is called ROC space.<br></p><p    >Again, the orange points are the extremes, and easy to achieve. <br></p><p    ><br></p><p    >ROC stands for <strong>receiver-operating characteristic</strong>, a leftover from its invention in WWII, to improve the detection of Japanese aircraft from radar signals.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-061">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-061">link here</a>
            <img src="21.Methodology1.key-stage-0063.svg" class="slide-image" />

            <figcaption>
            <p    >So far we’ve tough of FRP/TPR and precision/recall as a way to analyze a given set of models.<br></p><p    >However, what if we had a <em>single</em> classifier, but we could control how eager it was to call things <span>positive</span>? If we made it entirely timid, it would classify nothing as positive and start in the bottom left corner. As it grew more brave, it would start classifying some things as positive, but only if it was really sure, and its true positive rate would go up. If we made it even more daring, it would start getting some things wrong and both the tpr and the fpr would increase. Finally, it would end up classifying everything as positive, and end up on the top right corner. <br></p><p    >The curve this classifier would trace out, would give us an indication of its performance, <em>independent </em>of how brave or how timid we make it. How can we build such a classifier?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-062">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-062">link here</a>
            <img src="21.Methodology1.key-stage-0064.svg" class="slide-image" />

            <figcaption>
            <p    >We can achieve this by turning a regular classifier into a<strong> ranking classifier</strong><em> </em>(also known as a <strong>scoring classifier</strong>). A ranking classifier doesn’t just provide classes, it also give a score of <em>how</em> negative or <em>how</em> positive a point is. We can use this to rank the points from most negative to most positive.<br></p><p    >How to do this depends on the classifier. Here’s how to do it for a linear classifier. We simply measure the distance to the decision boundary.We can now scale our classifier from timid to bold by moving the decision boundary from left to right.<br></p><p    >After we have a ranking, we can scale the eagerness of the classifier to make things positive. by moving the threshold (the dotted line) from left to right, the classifier becomes more eager to call things negative. This allows us to trade off the true positive rate and the false positive rate.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-063">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-063">link here</a>
            <img src="21.Methodology1.key-stage-0065.svg" class="slide-image" />

            <figcaption>
            <p    >Now, we can’t test a ranking on our test data, because we don’t know what the correct ranking is. We don’t get a correct ranking, just a correct<em> labeling</em>. <br></p><p    >However, we can indicate for specific pairs that they are ranked the wrong way around: all pairs of different labels. For instance, <strong class="blue">t</strong> and <strong class="orange red">f</strong> form a ranking error: <strong class="blue">t</strong> is ranked as <span class="orange red">more negative</span> than <strong class="orange red">f</strong>, even though <strong class="blue">t</strong> is <span class="blue">positive</span> and <strong class="orange red">f</strong> is <span class="orange red">negative</span>.<br></p><p    >Note: a ranking error is a <em>pair </em>of instances that is ranked the wrong way around. A single instance can be part of multiple ranking errors.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-064">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-064">link here</a>
            <img src="21.Methodology1.key-stage-0066.svg" class="slide-image" />

            <figcaption>
            <p    >We can make a big matrix of all the pairs for which we know how they should be ranked: <span>negative </span>points on the horizontal axis, <span>positive</span> on the vertical. The more sure we are that a point is positive, the closer we put it to the bottom left corner. This is called a <strong>coverage matrix</strong>. We color a cell <span class="green">green</span> if the corresponding points are ranked the right way round, and<span class="orange red"> red</span> if they are ranked the wrong way round.<br></p><p    >Note that the proportion of this table that is <span class="orange red">red</span>, is the probability of making a ranking error.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-064" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-065">link here</a>
            <img src="21.Methodology1.key-stage-0067anim0.svg" data-images="21.Methodology1.key-stage-0067anim0.svg,21.Methodology1.key-stage-0067anim1.svg,21.Methodology1.key-stage-0067anim2.svg,21.Methodology1.key-stage-0067anim3.svg,21.Methodology1.key-stage-0067anim4.svg,21.Methodology1.key-stage-0067anim5.svg,21.Methodology1.key-stage-0067anim6.svg" class="slide-image" />

            <figcaption>
            <p    >The coverage matrix shows us exactly what happens to the true positive rate and the false positive rate if we move the threshold from the right to the left. We get exactly the kind of behaviour we talked about earlier. We move from the all-positive classifier step by step to the all-negative classifier.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-066">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-066">link here</a>
            <img src="21.Methodology1.key-stage-0068.svg" class="slide-image" />

            <figcaption>
            <p    >This is one of the question types on the exam. There are more details in the third homework.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-067">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-067">link here</a>
            <img src="21.Methodology1.key-stage-0069.svg" class="slide-image" />

            <figcaption>
            <p    >As an example of what real ROC curves look like, here are the ROC curves for predicting gender from every single physical measurement in the ANSUR II data used in the first lecture and in the second worksheet. The red curve, that makes a right angle is what we get when we use the target label itself as a feature.<br></p><p    >The lowest AUC comes from using buttock circumference as a feature, and the high from using neck circumference. Remember that the male class are all soldiers in this dataset, so it’s likely we’re actually predicting whether somebody is a soldier more than their gender<br></p><p    >This plot is for the complete data so there is a 4:1 class imbalance (male:female).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-068">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-068">link here</a>
            <img src="21.Methodology1.key-stage-0070.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    >If we draw a line between two classifiers we know we can create, we can create a classifier for every point on that line simply by picking the output of one of the classifiers at random. If we pick with 50/50 probability we end up precisely halfway between the two.<br></p><p    >If we vary the probability we can get closer to either classifier.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-069">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-069">link here</a>
            <img src="21.Methodology1.key-stage-0071.svg" class="slide-image" />

            <figcaption>
            <p    >The area under the curve (AUC) of classifiers that we can create (the <em>convex hull </em>of all classifiers we’ve seen) is a good indication of the quality of the classifier. The bigger this area, the more useful classifiers we can achieve.<br></p><p    >The AUC is a good way to compare classifiers with class or cost imbalance, where we don’t know what our preferences are.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-070">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-070">link here</a>
            <img src="21.Methodology1.key-stage-0072.svg" class="slide-image" />

            <figcaption>
            <p    >As we saw before: normalizing the coverage matrix gives us the ROC space (barring some small differences that disappear for large datasets). The area under the ROC curve is an estimate of the green proportion of the coverage matrix. This gives us a good way to interpret the AUC. <br></p><p    ><strong>The AUC (in ROC space) is an estimate of the probability that a ranking classifier puts a randomly drawn pair of positive and negative examples in the correct order. </strong></p><p    ><strong></strong></p>
            </figcaption>
       </section>


       <section id="slide-071">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-071">link here</a>
            <img src="21.Methodology1.key-stage-0073.svg" class="slide-image" />

            <figcaption>
            <p    >To re-iterate, <strong>how we get a ranking from a classifier depends entirely on the model</strong>. Let’s look at one more example: the tree classifier that we saw earlier.  Again, we’ll discuss the actual algorithm for training decision trees later. For now, we’ll just <br></p><p    >The decision tree is an example of a <em>partitioning </em>classifier. Is splits the feature space into partitions, and assigns each partition, also known as a <strong>segment</strong>, a class. All instances in the segment get the same class.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-072">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-072">link here</a>
            <img src="21.Methodology1.key-stage-0074.svg" class="slide-image" />

            <figcaption>
            <p    >In this example we have an instance space that has been split into four segments by a decision tree. We rank the segments by the proportion of positive points. We then put all points in one region on the same level in the ranking.<br></p><p    >In this example, <strong class="orange red">b</strong> is more <span class="orange red">negative</span> than <strong class="orange red">a</strong>, because <strong class="orange red">b</strong>’s segment contains only negative examples, whereas <strong class="orange red">a</strong>’s segment contains a mix of<span class="blue"> positive </span>and <span class="orange red">negative</span> examples.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-073">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-073">link here</a>
            <img src="21.Methodology1.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    >This means that for some pairs (like <strong class="orange red">f</strong>,<strong class="blue">z</strong>), the classifier ranks them as “the same”. We’ll color these <strong>orange</strong>. <br></p><p    >For large datasets, these regions will not contribute much to the  total area under the curve.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-074">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-074">link here</a>
            <img src="21.Methodology1.key-stage-0076.svg" class="slide-image" />

            <figcaption>
            <p    >To interpret the AUC, you should know not just what classifier was used, but how it was made into a collection of classifiers. You should also know whether it’s a the area under an ROC curve, or a precision/recall curve.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-075">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-075">link here</a>
            <img src="21.Methodology1.key-stage-0077.png" class="slide-image" />

            <figcaption>
            <p    >An alternative to the ROC is the <strong>precision/recall curve</strong>. It works in exactly the same way, but has precision and recall on the axes.<br></p><p    >As you can see in this tweet, in many settings the PR curve can be much more informative, especially when you’re a plotting the curves. Practically, it’s little effort to just plot both, and judge which one is more informative. <br></p><p    >ROC has the benefit of an intuitive interpretation for the AUC (the probability of ordering a random pair the right way round). I haven’t yet found a similar interpretation for the PR-AUC.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-076">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-076">link here</a>
            <img src="21.Methodology1.key-stage-0078.svg" class="slide-image" />

            <figcaption>
            <p    >To put a classifier into production, a ranking may not be enough. Sometimes, you just need to produce a single answer. In that case, you can still use the ROC and PR curves to tune your hyperparameters and choose your model, but ultimately, you’ll need to choose a threshold as well: the point at which you decide to call something a positive.<br></p><p    >This is more of a software development issue than a scientific choice. Often, you have to look carefully at the curves, perhaps together with the end users, to make a decision.<br></p><p    >The second approach works best with probabilistic classifiers, which we’ll discuss next week.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-077">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-077">link here</a>
            <img src="21.Methodology1.key-stage-0079.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-077">
           <a class="slide-link" href="https://mlvu.github.io/lecture03#video-77">link here</a>
           <iframe
                src="https://www.youtube.com/embed/XJ_StAFefUk?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-078">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-078">link here</a>
            <img src="21.Methodology1.key-stage-0080.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr><br></p><p    >Model evaluation is not just about showing how well your model works. It’s also about working out what it <em>means</em> to get a certain performance. And more importantly, what it doesn’t mean.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-079">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-079">link here</a>
            <img src="21.Methodology1.key-stage-0081.png" class="slide-image" />

            <figcaption>
            <p    >In this video, we will use the following research as a running example. In 2017 researchers from Stanford built a classifier that predicted sexual orientation (restricted to the classes “heterosexual” and “gay”) from profile image taken from a dating site. They reported 91% ROC-AUC on men and 83% ROC-AUC on women.<br></p><p    >The results were immediately cited as evidence of a biological link between biology and sexual orientation. The following important caveats were largely overlooked in media reports:<br></p><p     class="list-item">Some of theperformance came from facial landmarks (roundness, length of nose, distance between eyes, etc), but some came from superficial details like hairstyle, lighting and grooming. The accuracy <br></p><p     class="list-item">The results were true when averaged over a large population. It’s true that women live longer than men on average, but that doesn’t mean that there are no old men. Likewise,  the fact that you can guess orientation based on, say, the length of the nose, with better than chance accuracy, may only be due to a very small difference between the two distributions, with plenty of overlap.<br></p><p     class="list-item">~90% ROC-AUC may sound impressive, but it basically means that you will make 1 ranking error for every 10 attempts.<br></p><p    >The study authors make may of these points themselves, but that didn’t stop the paper from being wildly misrepresented: <a href="https://docs.google.com/document/d/11oGZ1Ke3wK9E3BtOFfGfUQuuaSMR8AO2WfWH3aVke6U/edit#"><strong>https://docs.google.com/document/d/11oGZ1Ke3wK9E3BtOFfGfUQuuaSMR8AO2WfWH3aVke6U/edit#</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-080">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-080">link here</a>
            <img src="21.Methodology1.key-stage-0082.svg" class="slide-image" />

            <figcaption>
            <p    >Like in the previous video, we’ll look at some important questions to ask yourself when you come up against a topic like this. Let’s ask the same questions again (with some new ones thrown in for good measure).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-081">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-081">link here</a>
            <img src="21.Methodology1.key-stage-0083.svg" class="slide-image" />

            <figcaption>
            <p    >In these cases, it’s important to know your history. Physiognomy is the study which attempts to infer character from facial features.<br></p><p    >In this case there’s is a long history of scientists claiming to be able to divine personal attributes (most often “criminality”) from the structure of a subject’s face. This is called physiogmony and almost any claim made has been conclusively disproven as false, and based on poor scientific practice and spurious correlations.<br></p><p    >That doesn’t mean, of course, that the entire idea of physiognomy is conclusively disproven. But is does mean that when we are stumbling into the same area with new tools, we should be aware of the mistake made in the past and, so that we can be careful not to repeat them.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-082">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-082">link here</a>
            <img src="21.Methodology1.key-stage-0084.png" class="slide-image" />

            <figcaption>
            <p    >The first thing to be aware of is what you’re looking at. This is especially important with modern systems that can look at raw image data without extracting specific, interpretable features.<br></p><p    >Here a visualization of a classifier looking at a chest x-ray and making a prediction of whether the patient has Cardiomegaly (an enlarged heart). The positive values in the heat map indicate that those regions are important for the current classification. The largest values are near the heart, which is what we expect. <br></p><p    >However, the classifier is also getting a positive contribution from the “PORTABLE” label in the top right corner and the marker on the right. These indicate that the x-ray was taken with a portable scanner. Such scanners are only used when a patient’s condition has progressed so far that they can’t leave their house. In such cases it’s a safe bet that they have Cardiomegaly.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-083">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-083">link here</a>
            <img src="21.Methodology1.key-stage-0085.svg" class="slide-image" />

            <figcaption>
            <p    >These problems are often called “Clever Hans” effects. Clever Hans, or der Kluge Hans, was an early-20th century German horse, who appeared to be able to do arithmetic.<br></p><p    >As it turned out, Hans was not doing arithmetic, but just reading the body language of its handler, to see whether it was moving towards the right answer. This is impressive in itself,  of course, but it does mean that Hans didn’t show the kind of intelligence that was being attributed to him. <br></p><p    >Crucially, this was <em>not</em> a hoax. The handler truly believed that Hans was able to do arithmetic, and had no idea that he was guiding him subconsciously. This, incidentally is also why double-blind experiments are so important in other fields.<br></p><p    >For us, Hans serves as a powerful reminder that just because we’re seeing the <em>performance</em> we were hoping for, doesn’t mean we’re seeing it for the<em> reasons </em>we were hoping for as well.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-083" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-084">link here</a>
            <img src="21.Methodology1.key-stage-0086anim0.svg" data-images="21.Methodology1.key-stage-0086anim0.svg,21.Methodology1.key-stage-0086anim1.svg" class="slide-image" />

            <figcaption>
            <p    >A related question you should ask when you find that you can successfully predict X from Y is <strong>which causes which</strong>?<br></p><p    >The image on the left shows a feature that researchers found when attempting to predict criminality based on a dataset of faces of criminals and non-criminals. One of their  findings is that the angle made by the corners of the mouth and the tip of the nose is a highly predictive feature. The authors suggest that such facial features are indicative of criminality<br></p><p    >However, when we look at the dataset we see that it’s not the features of the face, so much as the expression that differs. In the “non-criminal” photographs, the subjects hold a light smile, as is common, whereas in the criminal set the expressions have a more explicitly relaxed jaw. What we’re seeing here are not facial <em>features</em>, so much as facial <em>expressions</em>.<br></p><p    >This is important, because it changes the interpretation of the results completely. The physiognomical interpretation is that there is a biological mechanism that causes both criminality and a particular wideness of the mouth, and that this is determined at birth. The alternative explanation is that when people with a criminal background have their photographs taken, they are more likely to prefer a menacing expression than the average person is.<br></p><p    >Note, incidentally, that the photos of criminals are not mugshots. The are described as “normal ID photos” by the authors.<br></p><p    >Further discussion: <a href="https://www.callingbullshit.org/case_studies/case_study_criminal_machine_learning.html"><strong>https://www.callingbullshit.org/case_studies/case_study_criminal_machine_learning.html</strong></a><br></p><p    ><br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-085">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-085">link here</a>
            <img src="21.Methodology1.key-stage-0087.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s go back to the sexuality classifier. what might a Clever Hans effect look like here? In the most extreme case, you might expect a classifier just to look at the background of the image. The authors were more careful here than you might expect:<br></p><p     class="list-item">The background of the image was blurred and the the facial features (eyes, nose, mouth) were detected and aligned. <br></p><p     class="list-item">The focus of the classifier was investigated with saliency maps (indicators of where the model is looking). This is a fallible method, but it does show a general focus on the face.<br></p><p     class="list-item">A second classifier was fed only facial landmarks: the position of the eyes, roundness of the jaw, etc. The suggestion being that this prevents Clever Hans effects.<br></p><p     class="list-item">The deep neural network used to extract features from pixels was not trained on this data, but on another facial dataset. Only its<em> features </em>were fed to a shallow classifier that learned from these labels. This limits the ability of the classifier to pick up on surface detail.</p><p     class="list-item"></p>
            </figcaption>
       </section>


       <section id="slide-086">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-086">link here</a>
            <img src="21.Methodology1.key-stage-0088.svg" class="slide-image" />

            <figcaption>
            <p    >Another question we suggested in the last video is whether the target label you’ve chosen is saying what you think it’s saying.<br></p><p    >Here, the authors inferred sexuality from the stated preference in the dating profile. This is clearly correlated with sexuality, but not the same thing. Firstly, sexuality is one of those attributes (like movie genre) that can only be crudely approximated by a set of finite categories. Moreover, for many people it’s not a fixed attribute, and it is subject to some evolution throughout their life.<br></p><p    >The stated preference on a dating profile also means that you are capturing only those gay people who are willing to live (relatively) openly as gay. This may be highly dependent on social background. It’s certainly conceivable that in poorer subcultures, people are less likely to come out as gay, either to their community or to themselves.<br></p><p    >This means that what we’re detecting when we’re classifying a face in this dataset as “gay” is more likely a combination of factors that are correlation to that label.<br></p><p    >Incidentally, note the size of the dataset. One thing the authors can’t be accused of is finding spurious correlations. It’s a question of what the correlations that they found mean, but with this amount of data, as we saw before, we get very small confidence intervals, so the observed effects are definitely there.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-086" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-087">link here</a>
            <img src="21.Methodology1.key-stage-0089anim0.svg" data-images="21.Methodology1.key-stage-0089anim0.svg,21.Methodology1.key-stage-0089anim1.svg,21.Methodology1.key-stage-0089anim2.svg,21.Methodology1.key-stage-0089anim3.svg" class="slide-image" />

            <figcaption>
            <p    >So, what kind of hypotheses can we think of for what is causing the performance of the classifier?<br></p><p    >The authors observe that in their dataset the heterosexual men are more likely have facial hair. That’s most likely to be a grooming choice, based on the differences in gay and heterosexual subcultures. <br></p><p    >For other correlations, such as that between sexuality and nose length, the authors suggest the prenatal hormone theory, a theory that relates prenatal hormone levels in the mother with the sexuality of the subject. In short, a biological mechanism that is responsible for both the (slight) variation in facial features and the variation in sexual preference.<br></p><p    >But that’s not the only possibility. In the previous slide, we saw that it’s difficult to separate facial features from facial expressions. However, even if we somehow eliminate the expression, that doesn’t mean that every facial feature we see is determined at birth. For instance, the roundness of the jaw is also influenced by body weight, which is strongly influenced by social class (for instance, whether somebody grows up poor or rich). And while there’s no evidence that social class influences the probability of <em>being gay</em>, it most likely does influence how likely a gay person is to end up setting up a dating profile.<br></p><p    >Note that these are purely hypotheses, intended to show which kinds of causalities can cause these correlations. I’m not in the least bit qualified to say which is more likely to be true.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-088">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-088">link here</a>
            <img src="21.Methodology1.key-stage-0090.svg" class="slide-image" />

            <figcaption>
            <p    >The authors plotted the four averages faces for the classes male/female and gay/heterosexual in their dataset. Here are the four options. It’s a peculiar property of datasets of (aligned) faces that the mean is often quite a realistic face itself.<br></p><p    >Consider this plot with the hypotheses on the previous slide. What differences do you see? Pay particular attention to the differences in skin tone, grooming, body weight, and the presence of glasses. <br></p><p    >I’ll leave you to decide which you think is the more likely explanation for these difference: choice of presentation, social class, or sexuality. <br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-089">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-089">link here</a>
            <img src="21.Methodology1.key-stage-0091.png" class="slide-image" />

            <figcaption>
            <p    >The authors repeated their experiments by classifying based purely on facial landmarks. The idea is that we can detect landmarks very accurately, and classifying on these alone removes a lot of sources for potential Clever Hans effects.<br></p><p    >We see that all subsets of the face landmarks allow for some predictive performance, but there is a clear difference between them. Note that just because we are isolating landmarks, doesn’t mean that we are focusing only on biological causes. As we saw earlier, the shape of the mouth is determined more by expression than by facial features, and the roundness of the jaw is partly determined by body weight, which is correlated with social class.<br></p><p    >We will discuss the AUC metric in the third lecture. For now, you can think of a classifier with 81% AUC as one that, given a random pair of gay and heterosexual instances from the data, will successfully select the gay instance 81% of the time.<br></p><p    >Let’s assume that the shape of the nose is mostly unaffected by grooming and expression. I have no idea whether this assumption is valid, but say that it is. Focusing purely on the shape of the nose, we see that performance drops to 0.65 AUC for men and 0.56 AUC for women. This is still better than chance level. <br></p><p    >Can we say that homosexuality can be<em> detected</em> based on the shape of the nose? Can we conclude a biological relation based on this correlation?<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-089" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-090">link here</a>
            <img src="21.Methodology1.key-stage-0092anim0.svg" data-images="21.Methodology1.key-stage-0092anim0.svg,21.Methodology1.key-stage-0092anim1.svg,21.Methodology1.key-stage-0092anim2.svg,21.Methodology1.key-stage-0092anim3.svg,21.Methodology1.key-stage-0092anim4.svg,21.Methodology1.key-stage-0092anim5.svg" class="slide-image" />

            <figcaption>
            <p    >To interpret numbers like these, it’s good to get some points of reference. If we try to guess somebody’s gender or sex (the distinction doesn’t matter much for such a crude guess), knowing nothing about them except their age, the best we can expect to do is slightly better than chance level (51% of our guesses will be correct). The reason we can get better than chance level is that women tend to live longer than men. This means that if we guess “female” for older people, we are a little bit more likely to be correct.<br></p><p    >If we restrict ourselves to older people, the effect becomes more pronounced and we can get an accuracy as high as the sexuality classifier got based purely on noses in the female part of the data. This can help us to interpret the AUC the authors achieved. Note that this accuracy is achieved by calling everybody female, and the AUC is achieved by guessing that the older person in a pair is always female. Think about that. <strong>If you walk into a carehome blindfolded and simply call everybody female, can you really claim to be </strong><em>detecting </em><strong>their gender?<br></strong></p><p    >If we look purely at people’s height, we get an accuracy and AUC that is comparable to what the authors achieved from the pixel data. This is also an important point to consider. Height and gender are correlated, but that doesn’t mean that there are no tall women or short men. It also doesn’t make tall women “masculine”, or short men “feminine”. It’s just a slight correlation that allows us to make an educated guess for certain parts of the range of heights.<br></p><p    >This is how you should always interpret accuracy and AUC values in the range 0.8 to 0.95: it's as impressive as guessing somebody's sex or gender based purely on their height. Yes, it can be done better than chance level, and yes there is a definite correlation, but it doesn't much more than that there is a very subtle correlation.<br></p><p    >NB: In the ANSUR II data, the subjects are soldiers. It’s possible that some sex differences are more pronounced in this population due to selection effects or physical training. We balanced the ANSUR data by subsampling to make the numbers of male and female subjects equal.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-091">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-091">link here</a>
            <img src="21.Methodology1.key-stage-0093.svg" class="slide-image" />

            <figcaption>
            <p    >Here are the histograms per sex or gender for the ANSUR data. There is a big discrepancy, but notice also how big the area of overlap is. <br></p><p    >This is always what we should imagine when people say that property A is predictive for attribute B. Just because there’s some difference between the populations doesn’t mean that there are no short men or tall women. And most importantly it doesn’t mean that being short makes you in some way more feminine or being tall makes you in some way more masculine.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-092">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-092">link here</a>
            <img src="21.Methodology1.key-stage-0094.svg" class="slide-image" />

            <figcaption>
            <p    >So, are we really justified in calling this a detector?<br></p><p    >Are you really <em>detecting</em> gender when you call somebody male just because they’re tall? The authors compare their classifiers to medical diagnostic tools to provide an interpretation of the AUC scores.<br></p><p    >This is where we must make a clear distinction between what a classifier like this does and what a diagnostic test does. A test like that for breast cancer looks explicitly only at one particular source of information. In this case the mammogram. The clinician will likely take the result of this test, and factor in contextual clues like age and lifestyle if the test is unclear. The test can be said to <strong>detect</strong> something, because it is strictly confined to look at only one thing. <br></p><p    >The clinician is then <strong>predicting</strong> or <strong>guessing</strong> something based on different factors. One of which is the test.<br></p><p    >The diagnosis of Parkinson’s is different. It much more similar to the way this classifier works, there is no unambiguous diagnostic tool like a blood test, so the diagnostician can only look at contextual clues like symptoms, medical history, age and risk factors. <br></p><p    >There is still a difference, however, in that the features are made more explicit. The pixel-based sexuality classifier may be inferring social class from the image, but it’s not <em>telling</em> us that it’s doing this. A doctor may be guilty of such subconscious inferences as well, but we can expect a greater level of <em>interpretability</em> from them.<br></p><p    >NB: The authors use the word accuracy to refer to ROC-AUC.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-093">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-093">link here</a>
            <img src="21.Methodology1.key-stage-0095.svg" class="slide-image" />

            <figcaption>
            <p    >After all that, it’s natural to ask whether this research project was a mistake. In short, were the authors wrong to do this, and if so in what way? This is a question of values rather than science, so it’s up to you to decide. I’ll just note some important points to consider.<br></p><p    >Firstly, the authors weren’t looking to prove this point one way or another, and they initially stumbled on to their findings. Given that a result has been established, it’s most often unethical <em>not </em>to report it. So long as that reporting is done carefully and responsibly, of course.<br></p><p    >The stated aim of the paper is not to make any claims about causal mechanisms. The authors are less interested in whether the classifier picks up on grooming choices of biological features, than in whether the guess can be made with some success at all. <br></p><p    >If we decide that the result did need to be reported, we may consider whether the authors were guilty of poor framing. The use of the word <em>detecting </em>is subject to misinterpretation. To be fair, that’s something I only became aware of when looking into this matter including all the fallout from this particular paper, so for me at least it would be hypocritical to be too judgemental of poor word choice.<br></p><p    >Another odd thing, is that in both the paper and the explanatory notes, <em>prenatal hormone theory </em>a suggested biological causal mechanism for homosexuality, is often mentioned. As we have seen the experiments shown here provide no evidence for one causal hypothesis over another, so it would probably have been better to make no claims about causal effect whatsoever.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-093" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-094">link here</a>
            <img src="21.Methodology1.key-stage-0096anim0.svg" data-images="21.Methodology1.key-stage-0096anim0.svg,21.Methodology1.key-stage-0096anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If you find yourself in the unfortunate situation of having to publish something controversial like this, or having to interpret somebody else's work on a controversial topic, keep these tips in mind. <br></p><p    >Finally, and this is a personal opinion, so make of it what you will: if you read about research like this in a newspaper, or on social media, remember that you are an <em>academic</em> (or at least you will be when you graduate). That comes with a certain responsibility to dig into the primary research before you make a judgment. Don't just trust the journalists, or worse, the commenters on twitter. If you really want to give your opinion on a situation like this, dig out the original paper and read it. If you don't, the most honest thing to do is to withhold judgment.<br></p><p    >What you you will find when you dig down, is almost always that the truth is much more subtle than the news and social media make it look. In this specific case, the majority of criticism leveled at the authors was simply inaccurate. There are valid and serious criticisms of the paper, but you really need to dig down to get past a lot of invalid criticisms. The truth, as is so often the case is subtle and complex. Our job as academics is to embrace that complexity, and </p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-095">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-095">link here</a>
            <img src="21.Methodology1.key-stage-0097.svg" class="slide-image" />

            <figcaption>
            <p    >I’m indebted to people on twitter for helping me to see the different angles on this topic. </p><p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-095">
           <a class="slide-link" href="https://mlvu.github.io/lecture03#video-95">link here</a>
           <iframe
                src="https://www.youtube.com/embed/BfoeXjX2v0Q?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-096">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-096">link here</a>
            <img src="21.Methodology1.key-stage-0098.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-097">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-097">link here</a>
            <img src="21.Methodology1.key-stage-0099.svg" class="slide-image" />

            <figcaption>
            <p    >As noted in the first lecture, statistics an ML are very closely related. It’s surprising, then that when we perform ML experiments, we use relatively little of the statistics toolkit. We don’t often do <strong>significance tests</strong>, for instance.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-098">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-098">link here</a>
            <img src="21.Methodology1.key-stage-0100.svg" class="slide-image" />

            <figcaption>
            <p    >Note everybody agrees. Hypothesis testing comes with a lot of downsides. Given that we usually have very big sample sizes (10000 instances in the test set), our efforts may be better spent elsewhere.<br></p><p    >Another consideration is that the ultimate validation of research is replication, not statistical significance. Somebody else should repeat your research and get the same results. Because all of our experimentation is computer code, a basic replication could be as simple as downloading and running a docker image. After that it’s easy to try the same on new data, or check the model for bugs.<br></p><p    >Since the community is so divided on the question, we won’t emphasise reporting statistics on experimental results too much for this course. However, there are a few points worth mentioning.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-099">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-099">link here</a>
            <img src="21.Methodology1.key-stage-0101.svg" class="slide-image" />

            <figcaption>
            <p    >This is the main question that statistical analysis is meant to answer.<br></p><p    >When it comes to reporting results, the question arises whether we should report our results with some sort of statistics. If we report that <span class="green">classifier A is better than classifier B</span> because their accuracies are .997 and .998 respectively, can we really trust <span class="green">that statement</span>? We’ve seen how much difference a little bit of noise can make, shouldn’t we be reporting some kind of hypothesis test on that statement, to show that we’ve used enough <span class="blue">test data</span>?<br></p><p    ><br></p><p    >quote source: <a href="http://www.icmla-conference.org/icmla11/PE_Tutorial.pdf"><strong class="blue">http://www.icmla-conference.org/icmla11/PE_Tutorial.pdf</strong></a></p><p    ><a href="http://www.icmla-conference.org/icmla11/PE_Tutorial.pdf"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-100">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-100">link here</a>
            <img src="21.Methodology1.key-stage-0102.svg" class="slide-image" />

            <figcaption>
            <p    >First, error bars.<br></p><p    >If you see a picture like this, showing the mean runtime of an experiment, measured for three models, and averaged over a number of runs, what would you imagine the error bars denote?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-100" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-101">link here</a>
            <img src="21.Methodology1.key-stage-0103anim0.svg" data-images="21.Methodology1.key-stage-0103anim0.svg,21.Methodology1.key-stage-0103anim1.svg,21.Methodology1.key-stage-0103anim2.svg,21.Methodology1.key-stage-0103anim3.svg,21.Methodology1.key-stage-0103anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The truth is, that there is no standard definition for what error bars denote, and if the authors didn’t specify what their error bars indicate, the authors messed up.<br></p><p    >These are the three most common options. Before we explain exactly what they mean, let’s look at how they behave, specifically when we increase the amount of data. <br></p><p    >If we sample more data, the estimate of our<strong> standard deviation </strong>becomes <em>more accurate</em>. It’s an estimate of a property of our data distribution.<br></p><p    >The standard error and the confidence interval are indicators of how confident we are about our estimate of the mean (indicated by the height of the error bar). There more data we have,<em> the smaller they get</em>.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-102">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-102">link here</a>
            <img src="21.Methodology1.key-stage-0104.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll assume you know what the standard deviation of a dataset is.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-102" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-103">link here</a>
            <img src="21.Methodology1.key-stage-0105anim0.svg" data-images="21.Methodology1.key-stage-0105anim0.svg,21.Methodology1.key-stage-0105anim1.svg,21.Methodology1.key-stage-0105anim2.svg,21.Methodology1.key-stage-0105anim3.svg,21.Methodology1.key-stage-0105anim4.svg,21.Methodology1.key-stage-0105anim5.svg,21.Methodology1.key-stage-0105anim6.svg" class="slide-image" />

            <figcaption>
            <p    >Here is how the standard error (SEM) works. If we sample some data (like error values) and calculate their mean, the result is random value too. If we resample, we get a (slightly) different mean. This means we can plot the probability distribution of this value. <br></p><p    >If our original distribution is normal with standard deviation <span class="green">sigma</span>, the distribution of the sample mean is approximately normal too (for large enough samples), with standard deviation sigma divided by the square of the number of samples.<br></p><p    >The original standard deviation is not usually known, so it is estimated from the data. The bottom distribution is a Student’s-t distribution. For large enough sample sizes (more than 100), we can treat this as a normal distribution.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-104">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-104">link here</a>
            <img src="21.Methodology1.key-stage-0106.svg" class="slide-image" />

            <figcaption>
            <p    >As you may know, the region of four standard deviations around the mean of a normal distribution contains roughly 95% of the probability mass. This is what the confidence interval error bar is: it is simply twice the standard error on both sides of our estimate, and it gives us a region for which we are 95% confident that it contains the true mean.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-105">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-105">link here</a>
            <img src="21.Methodology1.key-stage-0107.svg" class="slide-image" />

            <figcaption>
            <p    >This is an important distinction. These are frequentist methods, so there is no probability associated with the true mean at all. It is simply an objective, determined value (which we don’t know). The probability comes from sampling, and from computing the interval from a sample.<br></p><p    >So instead of having a fixed interval, with the true mean jumping around probabilistically, we have a fixed true mean around which we get an interval that jumps around if we resample the data The probability of it jumping so much that it no longer contains the true mean is 5%.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-106">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-106">link here</a>
            <img src="21.Methodology1.key-stage-0108.svg" class="slide-image" />

            <figcaption>
            <p    >Say you plot the mean squared error for regression models <strong class="orange red">A</strong> and <strong class="blue">B</strong>, together with some error bars. Does the the fact that the error bars overlap or not tell you whether the measured difference between the two models is statistically significant?<br></p><p    >Yes, for standard error bars, the existence of overlap implies that there is no significant difference between the two effects (i.e. the possibility that the difference is due to random chance is high, and a repeat of the experiment on new data may show a different result). If you plot confidence interval error bars, and there is no overlap, you may conclude that the difference between the models is significant. If you repret the experiment on fresh data, it is very likely that model <strong class="orange red">A</strong> would beat model <strong class="blue">B</strong> again.<br></p><p    >In both cases, the converse does not hold. If the SEM  error bars do not overlap, there may or may not be a significant difference. If the confidence interval error bars do overlap, there may still be a significant difference, depending on how much they overlap.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-106" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-107">link here</a>
            <img src="21.Methodology1.key-stage-0109anim0.svg" data-images="21.Methodology1.key-stage-0109anim0.svg,21.Methodology1.key-stage-0109anim1.svg,21.Methodology1.key-stage-0109anim2.svg,21.Methodology1.key-stage-0109anim3.svg,21.Methodology1.key-stage-0109anim4.svg,21.Methodology1.key-stage-0109anim5.svg,21.Methodology1.key-stage-0109anim6.svg,21.Methodology1.key-stage-0109anim7.svg,21.Methodology1.key-stage-0109anim8.svg,21.Methodology1.key-stage-0109anim9.svg" class="slide-image" />

            <figcaption>
            <p    >The true accuracy of a classifier (the probability of a correct classification) is also one of these “true values”, which we can’t see, but that we estimate by a sample mean, where the sample is our <span class="blue">test set</span>. The accuracy that we actually see is an estimate of a true value. Each instance in our test set is like a flip of an unfair coin that lands heads for a correct classification and tails for an incorrect one. This is called a <em>Bernoulli </em>distribution. <br></p><p    >Since this is a random process (our test set is randomly sampled), we can work out the distribution over the outcome (the number of correct classifications). The number of positive outcomes over a fixed-size sample from a Bernoulli distribution is described by a Binomial distribution. A region around our sample of 7 successes that contains 95% of the probability mass is a 95% confidence interval for our estimate of the accuracy. <br></p><p    >This is the same process as shown on slide 67, but with a Bernoulli distribution instead of a Normal one.<br></p><p    >source: <a href="https://homepage.divms.uiowa.edu/~mbognar/applets/bin.html"><strong class="blue">https://homepage.divms.uiowa.edu/~mbognar/applets/bin.html</strong></a><br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-108">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-108">link here</a>
            <img src="21.Methodology1.key-stage-0110.svg" class="slide-image" />

            <figcaption>
            <p    >The size of this confidence interval depends on two factors: the true accuracy* and the size of the test set. Here are some examples for different accuracies and test set sizes.<br></p><p    >This tells us that if the true success probability (accuracy) of a classifier is 0.5, and the test set contains 100 examples, our confidence interval has size 0.2. This means that even if we report 0.5 as the accuracy, we may well be wrong by as much as 0.1 either side. <br></p><p    >Even if these confidence intervals are usually not reported, you can easily work them out (or look them up) yourself. So, if you see someone say that classifier A is better than classifier B because A scored 60% accuracy and and B score 59%, on a test set of 100 instances, you have reason to be sceptical.<br></p><p    >We don’t know the true accuracy, but it’s accepted practice to assume that the estimate is close enough to get a reasonable estimate of the confidence interval.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-109">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-109">link here</a>
            <img src="21.Methodology1.key-stage-0111.svg" class="slide-image" />

            <figcaption>
            <p    >Here are the full curves, in case you every need to look it up.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-110">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-110">link here</a>
            <img src="21.Methodology1.key-stage-0112.svg" class="slide-image" />

            <figcaption>
            <p    >The main takeaway here is that confidence intervals are usually not necessary if your test set is big enough. With a test set of 10 000 instances, you can comfortably tell the difference between 98% and 99% accuracy without having to worry about random effects.<br></p><p    >If you don’t have the luxury of a large test set, you may need to do some statistical testing to see whether the effect you’ve observed (classifier A is better than classifier B) is genuine or down to random chance. It’s generally accepted that Alpaydin’s 5x2 cross validation is the best test for this purpose. It’s out of scope for this course, but follow the link if you run into this problem.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-111">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-111">link here</a>
            <img src="21.Methodology1.key-stage-0113.svg" class="slide-image" />

            <figcaption>
            <p    >Showing confidence means showing how reliable our numbers are. Standard error and confidence intervals are good ways to show confidence (or lack thereof). <br></p><p    >Showing spread is more about providing insight to the user. Say I train a classifier by gradient descent. If I have a big <span class="blue">test set</span>, I  can very <em>confidently</em> measure and report the accuracy of this particular classifier. However, gradient descent uses <em>random </em>initialization. If I repeat the training process, I may end up in a different local minimum, and get a different classification performance. It’s likely that I also want to communicate how much the measured performance is dependent on this randomness.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-112">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-112">link here</a>
            <img src="21.Methodology1.key-stage-0114.svg" class="slide-image" />

            <figcaption>
            <p    >If we have a large enough test set, we know that the confidence interval is small enough. But we do want to know how much the randomness in our process affects the result. What is the probability that repeating the process (on the same data, or on new data) produces wildly different results?<br></p><p    >For factors like the initialisation of gradient descent, this is easy to test: you just rerun a few times on the same data. But how do you test how robust the result are against sampling a new dataset?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-113">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-113">link here</a>
            <img src="21.Methodology1.key-stage-0115.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-114">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-114">link here</a>
            <img src="21.Methodology1.key-stage-0116.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-115">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-115">link here</a>
            <img src="21.Methodology1.key-stage-0117.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-116">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-116">link here</a>
            <img src="21.Methodology1.key-stage-0118.svg" class="slide-image" />

            <figcaption>
            <p    >If you’re interested in the difference between machine learning and statistics, I can recommend this paper by Leo Breiman. It shows the difference between the two cultures. It makes clear that the machine learning approach of measuring models purely for predictive accuracy on a large test set, has a lot of benefits and makes the business of statistics a lot simpler and more effective. </p><p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-116">
           <a class="slide-link" href="https://mlvu.github.io/lecture03#video-116">link here</a>
           <iframe
                src="https://www.youtube.com/embed/gnmCkRYrlEA?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-117">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-117">link here</a>
            <img src="21.Methodology1.key-stage-0119.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-118">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-118">link here</a>
            <img src="21.Methodology1.key-stage-0120.svg" class="slide-image" />

            <figcaption>
            <p    >We end with a very short, but important discussion.  <br></p><p    >A question that often arises is: <em>which classifier, model, search method, etc. is the best, independent of the data?</em> Before we see the data, can we make a best guess for which approaches to try? Are there some methods that always work really well?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-119">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-119">link here</a>
            <img src="21.Methodology1.key-stage-0121.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-120">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-120">link here</a>
            <img src="21.Methodology1.key-stage-0122.svg" class="slide-image" />

            <figcaption>
            <p    >Note that, intuitively, method D would be an absolutely insane method to choose a model.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-121">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-121">link here</a>
            <img src="21.Methodology1.key-stage-0123.svg" class="slide-image" />

            <figcaption>
            <p    >Here is another example. We know that gradient descent works well: to find the lowest point on a loss surface, you just follow the curve of the loss surface downward. However, for every loss surface and which gradient descent works, we can create a loss surface (like the one on the right) for which gradient ascent fails miserably, and actually, the <em>opposite strategy</em> works better: for almost all of the search, you have to climb to find the lowest point.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-122">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-122">link here</a>
            <img src="21.Methodology1.key-stage-0124.svg" class="slide-image" />

            <figcaption>
            <p    >I a way, we’re back to the problem of induction. For any given situation where a learning method works, there’s a situation where it doesn’t. Induction (aka. learning from experience) works in practice, but there are exceptions, and we can't tell just by looking at the data when it will and won't work.<br></p><p    >Note that if there were some algorithm that could tell us which sitation we were in, we could just use this algorithm to select our learning method, and beat the NFL theorem.<br></p><p    >In short, we need to make some <strong>assumptions</strong> about the nature whatever it was that created our data. Without such assumptions, learning doesn't work.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-123">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-123">link here</a>
            <img src="21.Methodology1.key-stage-0125.svg" class="slide-image" />

            <figcaption>
            <p    >One “out” to the NFL Theorem, is that there is a “universal distribution” governing all processes that create data.<br></p><p    >The NFL Theorem implicitly assumes that all datasets are equally likely. Since this is not the case, there is some other, non-uniform distribution that tells us which datasets are more likely than others, averaged over all possible settings.<br></p><p    >Using such a universal data distribution, we could work out a universally best learning algorithm. </p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-124">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-124">link here</a>
            <img src="21.Methodology1.key-stage-0126.svg" class="slide-image" />

            <figcaption>
            <p    >We don't have too many practical ideas about the properties of such a universal distribution, but one thing that crops up a lot is that simple data is necessarily more likely than complex data.<br></p><p    >This suggests that in learning we should have a <strong>simplicity bias</strong>. If there are two models that both fit the data, one very simple (like a linear model) and one very complex (like a very big decision tree), then it's more likely that the simple model generated the data.<br></p><p    >Such simplicity biases can be implemented in many different ways, and we'll see some concrete examples as the course progresses.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-125">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-125">link here</a>
            <img src="21.Methodology1.key-stage-0127.svg" class="slide-image" />

            <figcaption>
            <p    >Whether or not the NFL theorem means anything for us in practice, it has also given rise to a general <strong>principle</strong>, commonly followed in machine learning practice. The principle is that we should choose our method to deal with the task at hand, and not look for a universally best method.<br></p><p    >Note that this is distinct from the NFL theorem, because everybody still uses data splitting universally to evaluate <em>which of these many methods</em> is the best. And by the NFL theorem, model selection by data splitting is also not a universal algorithm. So the NFL theorem and the NFL principle are really two very different things.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-126">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-126">link here</a>
            <img src="21.Methodology1.key-stage-0128.svg" class="slide-image" />

            <figcaption>
            <p    >This is an increasingly important phrase in machine learning. The inductive bias of a method or model are those assumptions about the domain that are, explicitly or implicitly, hardcoded into the model. <br></p><p    >For instance, in a linear regression model, the assumption is that all instances lie on a line (or the higher-dimensional equivalent). If this assumption isn't violated too much, the model is a good fit for the data. If the assumption is violated very badly,  we need to look for ways to change the inductive bias, for instance by picking a different model, or by enriching the linear model with extra features, like we will do in the next lecture.<br></p><p    >We can summarize the business of machine learning and data science as follows. The business of the machine learning researcher is create a variety of models with helpful inductive biases. The business of the data scientist is to figure out which of the available inductive biases is helpful for any given problem.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-127">
            <a class="slide-link" href="https://mlvu.github.io/lecture03#slide-127">link here</a>
            <img src="21.Methodology1.key-stage-0129.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

</article>
