---
title: "Lecture 4: Data Pre-processing"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 4: Data Pre-processing</li>
            <li><a href="#video-000">Missing values and outliers</a></li>
            <li><a href="#video-030">Class imbalance and feature design</a></li>
            <li><a href="#video-052">Normalization</a></li>
            <li><a href="#video-074">Principal Component Analysis</a></li>
        <li class="pdf"><a href="http://localhost:5555/lectures/22.Methodology2.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">
       <section class="video" id="video-000">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-0">link here</a>
           <iframe
                src="https://www.youtube.com/embed/H7Ew_u4z40g?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-001">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-001" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-002">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-002" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0002.svg" class="slide-image" />

            <figcaption>
            <p    >To motivate this lecture, let’s look at a famous historical case of operations research. In the second World War, the allies executed many bombing runs, and often, their planes came back looking like this.<br></p><p    >To investigate where they should reinforce their planes, investigators made a tally of the most common points on the plane they were seeing damage.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-003">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-003" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0003.svg" class="slide-image" />

            <figcaption>
            <p    >The initial instinct was to reinforce those places that registered the most hits.<br></p><p    >However, it was soon pointed out (by a man called Abraham Wald) that this ignores a crucial aspect of the <em>source</em> of the data. They weren’t tallying where planes were most likely to be hit, they were tallying where planes were most likely to be hit <em>and come back</em>.<br></p><p    >The places where they weren’t seeing <em>any</em> hits were exactly the places that should be reinforced, since the planes that were hit there didn’t make it back.<br></p><p    >This specific effect is called <a href="https://en.wikipedia.org/wiki/Survivorship_bias"><strong class="blue">survivorship bias</strong></a>, and it’s worth keeping in mind, but the more general lesson for today, is that you should <strong>not take your data at face value</strong>. <br></p><p    >Don’t just load your data into an ML model and check the predictive performance: consider what you’re ultimately trying to achieve, and consider how the source of your data will affect that goal.<br></p><p    >By McGeddon - Own work, CC BY-SA 4.0, <a href="https://commons.wikimedia.org/w/index.php?curid=53081927"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=53081927</strong></a></p><p    ><a href="https://commons.wikimedia.org/w/index.php?curid=53081927"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-004">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-004" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0004.svg" class="slide-image" />

            <figcaption>
            <p    >Imagine that I gave you four datasets, each with two features x and y. For all datasets all of the following statistics give the same value: the mean and variance of x, the mean and variance of y, the correlation between x and y, the parameters of the linear regression line that best fits, and the r<sup>2</sup> of the correlation.<br></p><p    >You would conclude, that the datasets must be pretty similar, right?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-005">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-005" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0005.svg" class="slide-image" />

            <figcaption>
            <p    >One important aspect of not taking the data at face value is to <em>look</em> at it. <br></p><p    >These are the four datasets from the previous slide. They are a common example, called Anscombe’s quartet. Only when we look at the datasets, do we see how different they are. <br></p><p    >More importantly, only when we look at the data, do we see the patterns that define them. These are the patterns we want to get at if we want to understand the data. And none of them are revealed by the descriptive statistics of the previous slide.<br></p><p    >source: By Schutz: Avenue - Anscombe.svg, CC BY-SA 3.0, <a href="https://commons.wikimedia.org/w/index.php?curid=9838454"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=9838454</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-006">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-006" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0006.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a more modern variant: the datasaurus dozen.<br></p><p    >Recommended reading: <a href="https://www.autodeskresearch.com/publications/samestats"><strong class="blue">https://www.autodeskresearch.com/publications/samestats</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-006" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-007" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0007anim0.svg" data-images="22.Methodology2.key-stage-0007anim0.svg,22.Methodology2.key-stage-0007anim1.png" class="slide-image" />

            <figcaption>
            <p    >In machine learning and data science, our datasets are rarely two-dimensional, so we don’t have the luxury of simply doing a scatter plot. Looking at our data, in a way that provides insight almost always requires a lot of ingenuity and creativity. <br></p><p    >For high-dimensional, multivariate data, of the kind we’ve been dealing with so far, a good place to start is to produce a <strong>scatter plot matrix</strong>. This is simply a large grid of every scatter plot you can produce between any two features in your data. Often, only the plots below or above the diagonal are shown. The scatterplot matrix gives you a good idea of how the features relate to each other.<br></p><p    >If you have a target value (a class or a regression target), it’s a good idea to include it among the features for the scatter plot matrix. That way, you can see what relation each feature has with the target in isolation from the other features.<br></p><p    >On the right, we see the data as a 3D point cloud (in blue), together with the three projections to 2d (in yellow red and gree) that the scatterplot matrix gives us.<br></p><p    >source: RIDC NeuroMat, CC BY-SA 4.0 <a href="https://creativecommons.org/licenses/by-sa/4.0"><strong class="blue">https://creativecommons.org/licenses/by-sa/4.0</strong></a>, via Wikimedia Commons<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-008">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-008" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0008.svg" class="slide-image" />

            <figcaption>
            <p    >In the rest of this video, we’ll look at ways you can clean up your data, to make it useable for a classification or a regression task.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-009">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-009" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0009.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll start with missing data. Quite often, your data will look like this. <br></p><p    >You will need to do something about those gaps, before any machine learning algorithm will accept this data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-010">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-010" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0010.svg" class="slide-image" />

            <figcaption>
            <p    >What approach you should take is different, depending on whether values from the feature columns are missing, or values from the target column are missing.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-011">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-011" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0011.svg" class="slide-image" />

            <figcaption>
            <p    >If you have missing values in one of your features, the simplest way to get rid of them is to just remove the feature(s) for which there are values missing. If you’re lucky, the feature is not important anyway.<br></p><p    >You can also remove the instances with missing data. Here you have to be careful. If the data was not corrupted uniformly, removing rows with missing values will change your data distribution.<br></p><p    >For example, you might have data gathered by volunteers in the street using some electronic equipment. If the volunteer in Amsterdam had problems with their hardware, then their data will contain missing values, and the collected data will not be representative of Amsterdam.<br></p><p    >Another way you might get non-uniformly distributed missing data is if your data comes from a questionnaire , where people sometimes refuse to answer certain questions. For instance, if only rich people refuse to answer questions about their taxes, removing these instances will remove a lot of rich people from your data and give you a different distribution.<br></p><p    ><strong>How can you tell if data is missing uniformly?</strong> There’s no surefire way, but usually you can get a good idea by plotting a histogram of how much data is missing against some other feature. For instance if the number of instance with missing features against income is very different from the regular histogram over income, you can assume that your data was not corrupted uniformly. <br></p><p    >Of course it also helps if you can work out why your data has missing values. Again, don't take the data at face value, look into where it came from, and what the details of that process can tell you.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-012">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-012" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0012.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s zoom out a little before we move on. Whenever you have questions about how to approach something like this, it’s best to think about the <strong>real-world setting </strong>where you might apply your trained model. We often call this “production”, a term used in software development for the system that will be running the final deployed version of the software. Some machine learning models literally end up in a production environment, but we might also use machine learning models to perform business analytics, clinical decision support or in a scientific experiment. Wherever your model is meant to end up after you’ve finished your experimentation, that’s what we’ll call <strong>production</strong>.<br></p><p    >And production is what you’re trying to simulate, when you train your model and test it on a test set. So the choices you make, should make your experiment as close of a <em>simulation</em> of your production setting as you can manage. <br></p><p    >For example, in the case of missing values, the big question is: <strong>can you expect missing data in production?</strong> Or, will your production data be clean, and are the test data just noisy because the production environment isn’t ready yet?<br></p><p    >Examples of production systems that should expect missing data are situations where data comes from a web form with optional values or situations where data is merged from different sources (like online forms and phone surveys). <br></p><p    >You may even find yourself in a situation where the test data has no missing values (since it was carefully gathered) but the production system <em>will</em> have missing values (because there, the data will come from a web form). In that case, you may want to introduce missing values artificially in your test data, to simulate the production setting and study the effect of missing data.<br></p><p    >So remember, whenever you’re stuck on how to process your data: think what the production setting is that you’re trying to simulate, and make your choices based on that.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-013">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-013" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0013.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    >If you expect to see missing in production, then your model needs to be able to consume missing values, and you should keep them in the test set. For categorical features, the easiest way to do this is to add a category for missing values. For numerical features, we’ll see some options in the next slide.<br></p><p    >If your production setting won’t have missing values, then that’s the setting you want to simulate. If at all possible, you should get a test set without missing values, even if the training set has them. You can then freely test what method of dealing with the missing training values gives the best performance on the test set.<br></p><p    >If you cannot get a test set without missing values, one thing you can do is to report performance on both the data that has the instances with missing values removed and the data that has the missing values filled in by some mechanism. Neither are ideal simulations of the production setting, but the combination of both numbers hopefully gives you some idea.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-014">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-014" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0014.svg" class="slide-image" />

            <figcaption>
            <p    >At some point, either in the<span> training data </span>or the<span> test data</span>, we will probably need to fill in the missing values. This is called <strong>imputation</strong>.<br></p><p    >A simple way to do this in categorical data is to use the <strong>mode</strong>, the most common category. For numerical data, the <strong>mean</strong> or <strong>median</strong> are simple options. We’ll look at when you should use which later in this video.<br></p><p    >A more involved, but more powerful way, is to<strong> predict the missing value</strong> from the other features. You just turn the feature column in to a target column and train a classifier for categoric features, and  a regression model for numeric features.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-015">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-015" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0015.svg" class="slide-image" />

            <figcaption>
            <p    >If your target label has missing values, the story is a little different. In the <span class="green">training set</span> you are free to do whatever you think is best. You can remove instances, or impute the missing labels. If you have a lot of missing labels, this essentially becomes a semi-supervised learning setting as we saw in the first lecture.<br></p><p    >On <span class="blue">the test</span> set however, you shouldn’t impute or ignore the missing values, since that changes the task, and most likely makes it easier, which will give you false confidence in the performance of your model. Instead, you should <strong>report the uncertainty</strong> created by the missing values.<br></p><p    >In classification, this is easy: you compute the accuracy under the assumption that your classifier gets all missing values correct and under the assumption that it gets all missing values wrong: this gives you a <span>best case</span><span class="blue"> </span>and a <span>worst case</span> scenario, respectively. Your true accuracy on the test set is somewhere in between.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-016">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-016" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0016.svg" class="slide-image" />

            <figcaption>
            <p    >Another problem that we need to worry about, is <strong>outliers</strong>. Values in our data that take on unusual and unexpected values.<br></p><p    >Outliers come in different shapes and sizes. The most important question is whether your outliers are natural or unnatural.<br></p><p    >Here, the six dots to the right are so oddly, mechanically aligned that we are probably looking at some measurement error. Perhaps someone is using the value -1 for missing data. <br></p><p    >We can remove these, or interpret them as missing data, and use the approaches just discussed.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-017">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-017" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0017.png" class="slide-image" />

            <figcaption>
            <p    >In other cases, however, the “outlier” is very much part of the distribution. This is what we call a <strong>natural outlier</strong>. Bill Gates may have a million times the net worth of anybody you are likely to meet in the street, but that doesn’t mean he isn’t part of the distribution of income. <br></p><p    >If we fit a normal distribution to this data, the outlier would ruin our fit, but that’s because the data <em>isn’t normally distributed</em>. What we should do is recognize that fact, and adapt our model, for instance by removing assumptions of normally distributed data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-018">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-018" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0018.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s a metaphor for natural and unnatural outliers. If our instances are image of faces, the image on the left, that of comedian Marty Feldman,  is an extreme of our data distribution. It looks unusual, but it‘s crucial in fitting a model to this dataset. The image on the right is clearly corrupted data. It tells us nothing about what human faces might look like, and we’re better off removing it from the data.<br></p><p    >However, remember the real-world use-case: if we can expect corrupted data in production as well, then we should either train the model to deal with it, or make the clean-up automatic, so we can perform it in production as well. This would require us to have some way to detect automatically, whether something is an outlier. If the outliers are rare, and we have a lot of data, it may be easier just to leave them in and hope the model can learn to work around them, even if they are unnatural outliers.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-019">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-019" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0019.svg" class="slide-image" />

            <figcaption>
            <p    >If you have very extreme values that are not mistakes (like Bill Gates earlier), your data is probably not normally distributed. If you use a model which assumes normally distributed data, it will be very sensitive to these kinds of “outliers”. It may be a good idea to remove this assumption from your model (or replace it by an assumption of a heavy-tailed distribution).<br></p><p    >Note that you have to know your model really well to know if there are assumptions of normality. For instance anything that uses <em>squared errors</em> essentially has an assumption of normality.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-019" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-020" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0020anim0.svg" data-images="22.Methodology2.key-stage-0020anim0.svg,22.Methodology2.key-stage-0020anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To illustrate: let’s learn which <em>single value</em> best represents our data. We choose a value <span class="blue">m</span>, compute the distance to all our data points (the residuals) and try to minimise their squares.<br></p><p    >We can use such a single value for imputation to replace missing values or outliers, but this is also a kind of simplified picture of linear regression: if we had a regression problem with no features, the best we could do is output a single values for all instances. Which value should we pick to minimize the squared errors?<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-020" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-021" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0021anim0.svg" data-images="22.Methodology2.key-stage-0021anim0.svg,22.Methodology2.key-stage-0021anim1.svg,22.Methodology2.key-stage-0021anim2.svg,22.Methodology2.key-stage-0021anim3.svg,22.Methodology2.key-stage-0021anim4.svg,22.Methodology2.key-stage-0021anim5.svg" class="slide-image" />

            <figcaption>
            <p    >We take the derivative of the objective function and set it equal to zero. No gradient descent required here, we’ll just solve the problem analytically.<br></p><p    >What we find is that the optimum is <strong>the mean</strong>. The assumption of squared errors leads directly to the use of the mean as a<em> representative example</em> of a set of points.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-022">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-022" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0022.svg" class="slide-image" />

            <figcaption>
            <p    >We can now see why the the assumption of squared errors is so disastrous in the case of the income distribution.<br></p><p    >If Bill Gates makes a million times as much as the next person in the dataset, he is not pulling on the mean a million times as much, he’s pulling 10<sup>12</sup> times as much.<br></p><p    >Hence the joke: A billionaire walks into a homeless shelter and says “What a bunch of freeloaders, the average wealth in this place is more than a million dollars!”</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-023">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-023" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0023.svg" class="slide-image" />

            <figcaption>
            <p    >To get rid of the normality assumption, or rather, replace it by another assumption, we can use the<strong> mean absolute error </strong>instead. We take the residuals, but we sum their <em>absolute value</em> instead of their <em>squared value</em>. Which is the most representative value that minimises<em> that</em> error?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-023" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-024" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0024anim0.svg" data-images="22.Methodology2.key-stage-0024anim0.svg,22.Methodology2.key-stage-0024anim1.svg,22.Methodology2.key-stage-0024anim2.svg,22.Methodology2.key-stage-0024anim3.svg,22.Methodology2.key-stage-0024anim4.svg,22.Methodology2.key-stage-0024anim5.svg,22.Methodology2.key-stage-0024anim6.svg" class="slide-image" />

            <figcaption>
            <p    >To work this out, we need to know the derivative of the absolute function. This function is the identity if the argument is positive (so its derivative is 1) and the negative identity if the argument is negative </p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-025">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-025" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0025.svg" class="slide-image" />

            <figcaption>
            <p    >We’ve worked out that the value <span>m</span> that minimizes this error is the one for which the signs of the residuals sum to zero. This happens if the sum contains as many “-1”s as “+1”s, that is, if we have as many instances to the left of <span>m</span> as we have to the right. In other words, <strong>the median minimizes the mean absolute error</strong>.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-026">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-026" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0026.svg" class="slide-image" />

            <figcaption>
            <p    >If we use the median, Bill Gates still has a strong pull on the our representative value <span class="blue">m</span>, but it's proportional to his distance to <span class="blue">m</span>, not to the square of the distance. </p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-027">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-027" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0027.svg" class="slide-image" />

            <figcaption>
            <p    >This mistake, of using the mean when a normal distribution is not an appropriate assumption, is sadly very common.<br></p><p    >For example, you might hear someone say something like “there’s no poverty in the US, it’s the third richest country in the world by average personal wealth”.<br></p><p    >Wikipedia allows us to fact-check this quickly and it is indeed true. But remember that Bill Gates and Jeff Bezos live in the US, and as we saw, such people have a pretty strong pull on the mean. Luckily, Wikipedia also allows us to sort the same list by <em>median</em> wealth.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-027" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-028" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0028anim0.svg" data-images="22.Methodology2.key-stage-0028anim0.svg,22.Methodology2.key-stage-0028anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If we do that, we see that the US suddenly drops to 22nd place. This drop indicates how big the income inequality is.<br></p><p    >The Netherlands drops from 12th to 34, incidentally. So there’s plenty of income inequality over here as well.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-029">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-029" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0029.png" class="slide-image" />

            <figcaption>
            <p    >Here’s an example of this fallacy in the wild. In 2019, there was a discussion in the US about unionisation in the games industry. Here, one of the heads of Take-Two suggests that because the <em>average</em> yearly salary has six figures, unions are unlikely.<br></p><p    >Whether rich people can benefit from unions is a question for a different series of lectures, but the fact that the average wages are high, most likely just means that there is a small number of very rich people in the industry. We’d need to know the <em>median</em> to be sure.<br></p><p    >source: <a href="https://twitter.com/GIBiz/status/1140900959322804224?s=20"><strong class="blue">https://twitter.com/GIBiz/status/1140900959322804224?s=20</strong></a></p><p    ><a href="https://twitter.com/GIBiz/status/1140900959322804224?s=20"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-030">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-030" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0030.svg" class="slide-image" />

            <figcaption>
            <p    >If you want to adapt your model to deal with natural outliers, beware of hidden assumptions of normality. <br></p><p    >Consider modelling your noise with a heavy-tailed distribution instead, in other words, one which makes outliers more likely. Using the median instead of the mean is one way to do this. <br></p><p    >If you are doing regression and your target label is non-normally distributed then you can use the sum of absolute errors as a loss function instead of the sum of squared errors. This will also implicitly assume a more heavy-tailed distribution than the normal, but even more heavy tailed distributions are available. We'll look a little bit more at modeling data with different distributions in later lectures.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-030">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-30">link here</a>
           <iframe
                src="https://www.youtube.com/embed/KiJ1f5Lyh5s?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-031">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-031" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0031.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr><br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-032">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-032" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0032.svg" class="slide-image" />

            <figcaption>
            <p    >In the last lecture, we saw that class imbalance can be a big problem. We know what we can do to help our analysis of imbalanced problems, but how do we actually improve training?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-033">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-033" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0033.svg" class="slide-image" />

            <figcaption>
            <p    >We will assume that the class imbalance will happen in production as well as in your experiments. That means your <span class="blue">test set </span>needs to have the class imbalance in it, to be a fair simulation of the production setting. You can fiddle around with the training data all you like, but the <span class="blue">test</span> data (and by extension the <span>validation</span> data) needs to represent the natural class distribution.<br></p><p    >As a result, you'll need to focus on getting a large test set even more than normal: your problem is essentially that of detecting instances of the minority class. If you only have 25 of them in your test set, you won't get a very good idea of how good your classifier can detect them, even if you have 10000 majority class instances. <br></p><p    >This is usually a painful step, since withholding a lot of test data leaves you with very little training data. However, since you  are allowed to manipulate the training data however you like, you should prioritize the test data. There may be clever tricks to get more mileage out of the imbalanced training data, but without a proper test data, you won't be able to tell if these tricks work.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-034">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-034" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0034.svg" class="slide-image" />

            <figcaption>
            <p    >The most common approach is to <strong>oversample </strong>your minority class by sampling with replacements. The advantage is that this leads to more data. The disadvantage is that you end up with duplicates in you dataset. This may increase the likelihood of overfitting, depending on what algorithm you are using.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-035">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-035" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0035.svg" class="slide-image" />

            <figcaption>
            <p    >You can also <strong>undersample</strong> your majority class. This doesn’t lead to duplicates, but it does mean you’re throwing away data.<br></p><p    >If you have use an algorithm that makes multiple passes over the dataset (like gradient descent) it can help to resample the dataset fresh for every pass.<br></p><p    >Whether you oversample or undersample, you should be aware that you are changing the class distribution in the data. If you increase the proportion of one class, the classifier will be more likely to classify things by the minority class. This will be a tradeoff: you want to oversample to the point where the classifier begins to pick up on the features that indicate the minority class, but not so much that the classifier begins seeing the minority class when the features do not indicate it. <br></p><p    >The simplest way to achieve this is to treat the amount of resampling as a hyperparameter, and to optimize for precision/recall or ROC curves.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-036">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-036" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0036.svg" class="slide-image" />

            <figcaption>
            <p    >A more sophisticated approach is to oversample the minority class with <strong>new data</strong> derived from the existing data.<br></p><p    >SMOTE is a good example: it finds small clusters of points in the minority class, and generates their mean as a new minority class point. This way, the new point is not a duplicate of any existing point, but it is still in a region that contains a lot of points in the minority class, to keep it realistic.<br></p><p    >We don’t have time to go into this deeply. If you run into this problem in your project, click the link for detailed explanation.<br></p><p    >more information: <a href="https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets"><strong class="blue">https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets</strong></a></p><p    ><a href="https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-037">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-037" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0037.svg" class="slide-image" />

            <figcaption>
            <p    >Next, let's look at what we should to with the features in our dataset.<br></p><p    >Even if your data comes in a table, that doesn’t necessary mean that every column can be used as a feature right away (or that this would be a good approach). We'll need to look at the data provided and come up with a good way to translate it to a form in which the machine learning model is likely to learn from it. This depends both on what the data gives you, and on how your chosen model works. <br></p><p    >Translating your raw data into features is more an art than a science, and the ultimate test is the <span class="blue">test set</span> performance. We'll look at a few simple examples, to give you an idea of the general way of thinking you should adopt.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-038">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-038" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0038.svg" class="slide-image" />

            <figcaption>
            <p    >Some algorithms (like linear models or kNN) work only on numeric features. Some work only on categorical features, and some can accept a mix of both (like decision trees). <br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-039">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-039" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >This particular age column is integer valued, while numeric features are usually real-valued. In this case, we can just interpret the age as a real-valued number, and most algorithms won’t be affected.<br></p><p    >If our algorithm only accepts categoric features, we’ll have to group the data into bins. For instance, you can turn the data into a two-category feature with the categories “below the median” and “above the median”.<br></p><p    >We’ll lose information this way, which is unavoidable, but if you have a classifier that only consumes categorical features which works really well on the rest of your features it may be worth it.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-040">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-040" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0040.svg" class="slide-image" />

            <figcaption>
            <p    >We can represent phone numbers as integers too, so you might think a direct translation to numeric values is fine. But here it makes no sense at all. Translating a phone number  to a real value would impose an <em>ordering </em>on the phone numbers that would be totally meaningless. My phone number may represent a higher number than yours, but that has no bearing on any possible target value.<br></p><p    >What<em> is </em>potentially useful information, is the area code. This tells us where a person lives, which gives an indication of their age, their political leanings, their income, etc. Wether or not the phone number is for a mobile or a landline may also be useful. But these are <strong>categorical features</strong>.<br></p><p    >Often in such cases, a single column in your raw data can yield several features for your machine learning model. For instance the phone number can give us area codes, but we can also derive from that whether the person lives in a big city or in the country side, whether the person has a cell phone or a landline, which province the person lives in, whether the person has a phone or not, etc. We could even extract a rough latitude/longitude in the form of two numeric features.<br></p><p    >Some of these require a little work and creativity, but they can be extremely informative features. Especially compared to the raw phone number interpreted as an integer.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-040" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-041" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0041anim0.svg" data-images="22.Methodology2.key-stage-0041anim0.svg,22.Methodology2.key-stage-0041anim1.svg,22.Methodology2.key-stage-0041anim2.svg" class="slide-image" />

            <figcaption>
            <p    >So what if our model only accepts numerical features? This is very common: most modern machine learning algorithms are purely numeric. How do we feed it categorical data? Here are two approaches. <br></p><p    ><strong>Integer coding</strong> gives us the same problem we had earlier. We are imposing a false ordering on unordered data. <br></p><p    ><strong>One-hot coding </strong>(also called one-of-N coding)<strong> </strong>avoids this issue, by turning <em>one </em>categorical feature into<em> several </em>numeric features. Per genre we can say whether it applies to the instance or not.<br></p><p    >In general, the one-hot coding approach is preferable. For almost all models, adding extra features does not substantially affect the runtime, and separating the different classes like this allows most models to use the information much more effectively.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-042">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-042" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0042.png" class="slide-image" />

            <figcaption>
            <p    >Once we’ve turned all our features into data that our model can handle, we can still manipulate the data further, to improve performance.<br></p><p    >How to get the useful information from your data into your classifier depends entirely on what your classifier can handle. The linear classifier is a good example. It’s quite limited in what kinds of relations it can represent. Essentially, each feature can only influence the classification boundary in a simple way. It can push it up or down, but it can’t let its influence depend on the values of the other features. Here is a (slightly contrived) example of when that might be necessary.<br></p><p    >Imagine classifying spam emails on two features: to what extent the email mentions drugs, and to what extent the email is sent to a pharmaceutical company. We'll consider the simplified case where every email that mentions drugs is spam, and every email that does not mention drugs is ham, unless the email is sent to a pharmaceutical company, in which case the roles are reversed. <br></p><p    >With these two features, and this logic, we get the decision boundary shown here. This problem, called the <strong>XOR problem </strong>after the Boolean relation which produces the same picture, is completely impossible for a linear classifier to solve.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-043">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-043" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0043.svg" class="slide-image" />

            <figcaption>
            <p    >We can switch to a more powerful model, but we can also add power to the linear classifier by <strong>adding extra features derived from the existing features</strong>. <br></p><p    >Here, we’ve added the cross-product of d and p (one value multplied by the other). Note the XOR relationship of the signs: two negatives or two positives both make positive, a negative and a positive make a negative. <br></p><p    >If we feed this three-feature dataset to a linear classifier, it can easily solve the problem. All it needs to do is to look at the sign of the third feature, and ignore the rest. We still have a simple linear classifier, which can easily and efficiently be optimally solved, but now it can learn non-linear relations in the original 2D feature space.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-044">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-044" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0044.png" class="slide-image" />

            <figcaption>
            <p    >Here's what the result looks like for our data.<br></p><p    >This is a  linear classier that operates in a 3D space. But since the third dimension is derived from the other two, we can colour our original 2D space with the classifications. Projected down to 2D like this, the classifier solves  our XOR problem perfectly.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-044" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-045" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0045anim0.png" data-images="22.Methodology2.key-stage-0045anim0.png,22.Methodology2.key-stage-0045anim1.png" class="slide-image" />

            <figcaption>
            <p    >One more example. In this dataset points are colored red if the distance to the origin is less than 0.7. Again, this problem is not at all linearly separable. <br></p><p    >Using Pythagoras, however, we can express how the classes are decided: if x<sup>1</sup><sup>2</sup> + x<sup>2</sup><sup>2</sup> &lt; 0.7<sup>2 </sup>then we classify as<span class="orange red"> red</span>, otherwise as <span class="blue">blue</span>. This is a linear decision boundary for the features x<sup>1</sup><sup>2</sup> and x<sup>2</sup><sup>2</sup>. </p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-046">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-046" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0046.png" class="slide-image" />

            <figcaption>
            <p    >So, if we add those features to the data, creating a 4D dataset, a linear decision boundary in that space solves our problem perfectly.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-047">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-047" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    >You can try this yourself at <a href="http://playground.tensorflow.org/#activation=linear&amp;regularization=L1&amp;batchSize=10&amp;dataset=xor&amp;regDataset=reg-plane&amp;learningRate=0.03&amp;regularizationRate=0.01&amp;noise=20&amp;networkShape=&amp;seed=0.64177&amp;showTestData=false&amp;discretize=true&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=false&amp;xSquared=false&amp;ySquared=false&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=false&amp;problem=classification&amp;initZero=false&amp;hideText=false&amp;numHiddenLayers_hide=true&amp;percTrainData_hide=true&amp;regularizationRate_hide=true&amp;learningRate_hide=false&amp;playButton_hide=false&amp;discretize_hide=false&amp;resetButton_hide=false&amp;regularization_hide=true&amp;dataset_hide=false&amp;batchSize_hide=true&amp;noise_hide=true&amp;problem_hide=false&amp;activation_hide=true&amp;stepButton_hide=false&amp;showTestData_hide=true"><strong class="blue">playground.tensorflow.org</strong></a>. The column labeled features contains some extra features derived from the original two by various functions (including the cross product).<br></p><p    >Note that both the XOR and Circle dataset are present.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-048">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-048" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0048.svg" class="slide-image" />

            <figcaption>
            <p    >We can do the same thing with regression. Here, we have a very non-linear relation.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-049">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-049" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0049.svg" class="slide-image" />

            <figcaption>
            <p    >A <span class="green">purely linear classifier</span> does a terrible job.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-050">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-050" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0050.svg" class="slide-image" />

            <figcaption>
            <p    >We<em> can</em> fit a <span>parabola</span> through the data much more closely. We can see this as a more powerful model (a parabola instead of a linear model), but we can also see this as a 2D linear regression problem, where the second feature (x<sup>2</sup>) is derived from the first. <br></p><p    >This is relevant because linear models are extremely simple to fit. By adding derived features we can have our cake and eat it too. A <em>simple</em> model that we can fit quickly and accurately, and a<em> powerful</em> model that can fit many nonlinear aspects of the data.<br></p><p    >If we don’t have any intuition for which extra features might be worth adding, <strong>we can just add all cross products</strong> of all features with each other and with themselves (like x<sup>2</sup>). Other functions like the sine or the logarithm may also help a lot.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-050" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-051" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0051anim0.svg" data-images="22.Methodology2.key-stage-0051anim0.svg,22.Methodology2.key-stage-0051anim1.svg,22.Methodology2.key-stage-0051anim2.svg,22.Methodology2.key-stage-0051anim3.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-052">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-052" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0052.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-052">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-52">link here</a>
           <iframe
                src="https://www.youtube.com/embed/Q0F13NPcoaU?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-053">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-053" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0053.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr><br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-054">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-054" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >For some models, it’s important to make sure that all numeric features have broadly the same minimum and maximum. In other words, that they are <em>normalized</em>. <br></p><p    >To see why, let’s revisit the k nearest neighbors (kNN) classifier from the first lecture.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-054" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-055" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0055anim0.svg" data-images="22.Methodology2.key-stage-0055anim0.svg,22.Methodology2.key-stage-0055anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Imagine we are using a 1-NN classifier (i.e. it only looks at the nearest example, and copies its class).<br></p><p    >In this plot, it looks like the blue and the red dot are the same distance away.<br></p><p    >But note the range of values for the two features: years and pupil dilation. Because years are measured in bigger units than than pupils, the blue dot will always be much closer. But this distinction is not meaningful: we cannot compare durations to distances. The only thing that really matters is how close the point is to our target comapred to the other points in the data. The absolute distance in the natural units doesn't matter.<br></p><p    >What we want to look at is how much spread there is<em> in the data</em>, and use that as our distance. We do that by <strong>normalizing</strong> our data before feeding it to the model.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-056">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-056" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0056.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll discuss three approaches to solving this problem. <strong>Normalization</strong>, which reshapes all values to lie within the range [0, 1], <strong>standardization</strong>, which reshapes the data so that its mean and variance are those of a standard normal distribution (0 and 1 respectively) and <strong>whitening</strong>, which looks at features <em>together</em>, to make sure that as a whole their statistics are those of a multivariate standard normal distribution.<br></p><p    >These terms are often used interchangeably. We’ll stick to these definitions for this course, but in other contexts you should check that they mean what you think they mean.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-056" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-057" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0057anim0.svg" data-images="22.Methodology2.key-stage-0057anim0.svg,22.Methodology2.key-stage-0057anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Normalisation scales the data linearly so that the smallest point becomes 0 and the largest becomes 1. Note that because x<sup>min</sup> is negative (in this example), we are actually moving all data to the right, and then rescaling it.<br></p><p    >We do this independently for each feature.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-057" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-058" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0058anim0.svg" data-images="22.Methodology2.key-stage-0058anim0.svg,22.Methodology2.key-stage-0058anim1.svg,22.Methodology2.key-stage-0058anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Another option is standardization. We rescale the data so that the<span> mean</span> becomes zero, and the <span class="blue">standard deviation</span> becomes 1. In essence, we are transforming our data so that it looks like it was sampled from a standard normal distribution (or as much as we can with a one dimensional linear transformation).<br></p><p    ><br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-058" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-059" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0059anim0.svg" data-images="22.Methodology2.key-stage-0059anim0.svg,22.Methodology2.key-stage-0059anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The standardization operation is pretty simple, and maybe you can see where it comes from intuitively (it's pretty similar to the normalization operation), but even so, it's good to derive it carefully. This will prepare us for whitening, where we will can to do the same thing across multiple features.<br></p><p    >For a rigorous derivation, we can think of the data as being "generated" from a standard normal distribution, followed by multiplication by <span class="blue">sigma</span>, and and adding <span>mu</span>. The result is the distribution of the data that we observed.  You can think of all normally distributed data being generated this way: sampled from a standard normal distribution, and scaled and translated to fit some non-standard distribution. <br></p><p    >If we then compute the mean and the standard deviation of the data, the formula in the slide is essentially <strong>inverting the transformation</strong>. We reverse the order, and replace addition by subtraction and multiplication by division. This takes the distribution that we observed and recovers <strong> </strong>the “original” data as sampled from the standard normal distribution.<br></p><p    >We will build on this perspective several times throughout the course.<br></p><p    >Of course, in practice our data may not be normally distributed at all (standard or otherwise), so we should be a bit careful with these kinds of operations that assume a normal distribution. Still, if the data is roughly equally distributed over a finite range, without any extreme outliers, standardization will work fine for most models. And, if it really fails, then normalization will probably fail too, and you'll need to think about trying more exotic approaches, or even designing your own. <br></p><p    >Remember, the proof is in the pudding: if the validation error is low, you probably did alright.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-059" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-060" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0060anim0.svg" data-images="22.Methodology2.key-stage-0060anim0.svg,22.Methodology2.key-stage-0060anim1.svg,22.Methodology2.key-stage-0060anim2.svg,22.Methodology2.key-stage-0060anim3.png,22.Methodology2.key-stage-0060anim4.png,22.Methodology2.key-stage-0060anim5.png" class="slide-image" />

            <figcaption>
            <p    >Here’s what standardization looks like if we apply it to data with two features. If the data is <em>uncorrelated</em>, we are reducing it to a nice spherical distribution, centered on the origin, with the same variance in each direction. Exactly what data from a <strong>multivariate standard normal distribution</strong> looks like.<br></p><p    >If, however, our data is <span class="orange red">correlated</span>, that is; knowing the value of one feature helps us predict the value of the other, we get a different result. This is because we standardize each feature <em>independently</em>, and the features are not independent. Is there a way to achieve the same effect with the correlated data? Can we transform the features somehow so that it looks like they came from a distribution like the one top right? This is what <strong>whitening</strong> can do for us.<br></p><p    >Note that this is not usually necessary in practice. Normalizing or standardizing each feature independently is usually fine, <span>especially if your model is powerful enough to learn correlations</span>. <span>However, whitening, normalizing across features, can sometimes give you a little boost. It will also help us understand the PCA method, which we will discuss in the next video.</span></p><p    ><span></span></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-060" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-061" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0061anim0.svg" data-images="22.Methodology2.key-stage-0061anim0.svg,22.Methodology2.key-stage-0061anim1.png,22.Methodology2.key-stage-0061anim2.svg" class="slide-image" />

            <figcaption>
            <p    >In essence we want to transform the data top right to something that looks like the data bottom left. Or, the same question asked differently, can we express the data in another <strong>coordinate system</strong>, to that in the new coordinate system, the features are not correlated and the variance in the direction of each axis is 1?<br></p><p    >In order to show how to do this we need to revise some bits of linear algebra. Specifically, we need to look at <strong>linear bases</strong> (the plural of basis).<br></p><p    >We'll go through a bit quickly, because we assume that you've already covered basis transformations in linear algebra. If not, or if your memory of them is hazy, you should take some time to review them.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-061" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-062" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0062anim0.svg" data-images="22.Methodology2.key-stage-0062anim0.svg,22.Methodology2.key-stage-0062anim1.svg,22.Methodology2.key-stage-0062anim2.svg,22.Methodology2.key-stage-0062anim3.svg,22.Methodology2.key-stage-0062anim4.svg" class="slide-image" />

            <figcaption>
            <p    >First, a quick reminder of how summing vectors works. We stick the tail of vector <strong>b</strong> onto the head of vector <strong>a</strong> and draw a line from the tail of <strong>a</strong> to the head of <strong>b</strong>. The point where we end up is the tip of the vector <strong class="orange red">a</strong> + <strong class="green">b</strong>.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-063">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-063" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0063.svg" class="slide-image" />

            <figcaption>
            <p    >We can see our basic Cartesian coordinate system as made up entirely of the two vectors (1 0) and (0 1). To describe a point in the place, we just sum a number of copies of these vectors.<br></p><p    >Every point in the plane is just a linear combination of these two. A coordinate like (3, 2) means: “sum three copies of<span class="orange red"> </span><strong class="orange red">a</strong> and add them to two copies of <strong class="green">b</strong>.” We call these <strong>basis vectors</strong>: vectors that allow us to describe all points in a space in terms of a multiple of each of the basis vectors. The set of points that can be described in this way is the space <strong>spanned</strong> by the basis vectors.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-064">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-064" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0064.svg" class="slide-image" />

            <figcaption>
            <p    >If we choose <em>different</em><strong> basis vectors</strong>, we get a different coordinate system to  express our data in. But (excepting some rare choice of basis vectors), we can still express all the same points as a number of copies of <span>one vector</span>, plus a number of copies of <span>the other</span>.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-064" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-065" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0065anim0.svg" data-images="22.Methodology2.key-stage-0065anim0.svg,22.Methodology2.key-stage-0065anim1.svg,22.Methodology2.key-stage-0065anim2.svg" class="slide-image" />

            <figcaption>
            <p    >If we know the coordinates <strong>x</strong><sup>b</sup> in our non-standard coordinate system, it’s easy to find the coordinates <strong class="blue">x</strong><sup class="blue">s</sup> in the standard basis. We just multiply the first coordinate of x<sup>b</sup> with the first basis vector, the second coordinate with the second basis vector and sum the result.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-065" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-066" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0066anim0.svg" data-images="22.Methodology2.key-stage-0066anim0.svg,22.Methodology2.key-stage-0066anim1.svg,22.Methodology2.key-stage-0066anim2.svg,22.Methodology2.key-stage-0066anim3.svg,22.Methodology2.key-stage-0066anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The basis vectors are usually expressed as the columns of a matrix <strong>B</strong>. That way, transforming a coordinate <strong>x</strong> in basis B to the standard coordinates can be done simply by matrix multiplying <strong>B</strong> by <strong>x</strong>. It also tells us that to go the other way, to transform a standard coordinate to the basis, you multiply by the <em>inverse</em> of <strong>B</strong>.<br></p><p    >Since inverting a matrix is an expensive and numerically unstable business, it’s good to focus (if possible) on <strong>orthonormal bases</strong>. That is, bases for which the basis vectors are <strong>orthogonal</strong> (the angle between any two of them is 90 degrees) and <strong>normal</strong> (all vectors have length 1). In that case the matrix transpose (which is simple to compute without loss of precision) is equal to the matrix inverse, so we can switch back and forth between bases quickly, without losing information.<br></p><p    >Here [<strong>a</strong>,<strong>b</strong>] represents the matrix created by concatenating the vectors <strong>a</strong> and <strong>b</strong>.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-067">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-067" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0067.svg" class="slide-image" />

            <figcaption>
            <p    >We can now re-phrase what we’re aiming to do: we want to find a set of new <em>basis vectors</em> so that we can express the data in a coordinate system where the features are not correlated, and the variance is 1 in every direction.<br></p><p    >Note that the latter means we can’t have an orthonormal basis (the basis vectors can’t be one). <br></p><p    >We can fix this by first computing an orthonormal basis, and then scaling independently along each axis, but we won't go into that here. For now, we'll just allow for non-orthonormal bases.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-068">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-068" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0068.svg" class="slide-image" />

            <figcaption>
            <p    >To figure out how to find this basis, we will follow the same principle as we did with standardisation: we will assume that the data was generated by a standard multivariate normal distribution (MVN), followed by a translation and a change of basis (with the change of basis causing some features to become correlated). We will attempt to reverse the process by:<br></p><p     class="list-item">fitting a (nonstandard) MVN to the data<br></p><p     class="list-item">figuring out the transformation that transforms the standard MVN to this MVN<br></p><p     class="list-item">applying the inverse of this transformation to the observed data<br></p><p    >A multivariate normal distribution is a generalisation of a one-dimensional normal distribution.<span> </span><span>Its mean is a single point</span>, <span>and its variance is determined by a symmetric matrix called a </span><strong>covariance matrix</strong>.<span> </span>The values on the diagonal indicate how much variance there is along each dimension. The off-diagonal elements indicate how much co-variance there is between dimensions.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-069">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-069" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0069.svg" class="slide-image" />

            <figcaption>
            <p    >The <em>standard</em> MVN has its mean at the origin and the identity matrix as its covariance matrix (i.e. its features are uncorrelated, and the variance is 1 along every dimension).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-070">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-070" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0070.svg" class="slide-image" />

            <figcaption>
            <p    >The estimators for the <strong>sample mean</strong><span> </span><strong>m</strong><span> </span>and <strong class="blue">sample covariance S</strong> look like this. Computing these values lets you fit an MVN to your data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-071">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-071" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0072.svg" class="slide-image" />

            <figcaption>
            <p    >As before, we will imagine that our data originall came from a standard MVN, and was then transformed to the data we observed by multiplying each point by some matrix A (changing the basis) and then adding some vector t (moving the mean away from the origin).<br></p><p    >We can<em> sample</em> a point<em> </em><strong>x</strong><em> </em>from an n-dimensional standard MVN by simply filling a with values sampled from a one-dimensional standard normal distribution.<br></p><p    >If we then transform <strong>x</strong> by multiplying it by some matrix <strong>A</strong> and adding some vector <strong>t</strong>, the result is the same as sampling from an MVN with mean<strong> </strong><strong>t</strong><strong> </strong>and covariance <strong class="blue">AA</strong><sup class="blue">T</sup><sup>.<br></sup></p><p    >Any MVN can be described in this way as a transformation of the standard normal distribution.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-071" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-072" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0073anim0.png" data-images="22.Methodology2.key-stage-0073anim0.png,22.Methodology2.key-stage-0073anim1.png,22.Methodology2.key-stage-0073anim2.png" class="slide-image" />

            <figcaption>
            <p    >Here’s what that looks like. For our data. We imagine some data sampled from a standard MVN. We multiply by some some matrix <strong>A</strong> to squish and rotate it. And then we apply a translation vector <strong>t</strong> to translate it to the right point in space.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-073">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-073" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0074.png" class="slide-image" />

            <figcaption>
            <p    >Now, we need to invert this. Given some data, we fit an MVN, find out which A and t match that MVN, and then invert the transformation from the standard MVN to the onserved data.<br></p><p    >In slide 69, we saw that the covariance after our transformation was <strong>AA</strong><sup>T</sup>, so if we  estimate the covariance <strong>S</strong> and find some matrix <strong>A</strong> such that <strong>AA</strong><sup>T</sup> = <strong>S</strong>, we can then use that <strong>A</strong> for the inverse transformation. Finding this <strong>A</strong> can be done in many ways. The most stable and popular one is the Singular Value Decomposition, which leads to a method known as PCA whitening, discussed in the next video.<br></p><p    >Since the multiplication by <strong>A</strong> doesn’t change the mean, we know that the translation vector <strong>t</strong> is equal to the mean <strong>m</strong>.<br></p><p    >Once we know <strong>A</strong> and <strong>t</strong>, we can reverse the transformation as shown here. <br></p><p    >Compare this to the standardisation operation: there, we subtract the mean, and multiply by the inverse of the standard deviation. Here we do the same, but in multiple dimensions <br></p><p    >Note that the standard deviation is the square root of the variance, just like the <strong>A</strong> matrix squared is the covariance.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-074">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-074" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-074">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-74">link here</a>
           <iframe
                src="https://www.youtube.com/embed/JC5rb5FmTjk?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-075">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-075" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0076.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-076">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-076" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0077.svg" class="slide-image" />

            <figcaption>
            <p    >Some datasets have more features than a given model can handle. Or, maybe the model can handle it, but it's overfitting on all the noise that so many features introduce.<br></p><p    >In that case, there are two things we can do: we can try to find a subset of the features that is most informative, and operate on those. This has the benefit that the features retain their meaning and are still interpretable. This is called <strong>feature selection</strong>.<br></p><p    >The alternative is to take information from all <em>all</em> features and to map them to a new (smaller) set of derived features, which retain as much of the original information as possible. This is called <strong>dimensionality reduction</strong>. In this case, the new features don’t always have an obvious meaning, but they may still work well for machine learning purposes.<br></p><p    >In this video we will just look at one dimensionality reduction method: Principal Component Analysis (PCA). We won't discuss feature selection, but if you're interested, a good place to start is the methods that come with sklearn: <a href="https://scikit-learn.org/stable/modules/feature_selection.html"><strong class="blue">https://scikit-learn.org/stable/modules/feature_selection.html</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-077">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-077" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0078.svg" class="slide-image" />

            <figcaption>
            <p    >Dimensionality reduction is the opposite of the feature expansion trick we saw earlier. It describes methods that reduce the number of features in our data (the dimension) by deriving new features from the old ones, hopefully in such a way that we capture all the essential information. There are several reasons you might want to reduce the dimensionality of your data:<br></p><p     class="list-item"><strong>Efficiency.</strong> Some machine learning methods can only handle so many features. If you have a very high dimensional dataset, you may be forced to do some dimensionality reduction in order to be able to run your chosen model.<br></p><p     class="list-item"><strong>Reduce </strong><strong>variance</strong> of the model performance (make the bias/variance tradeoff). Feature expansion boosts the power of your model, likely giving it higher variance and lower bias. Dimensionality reduction does the opposite: it reduces the power of your model likely giving you higher bias and lower variance.<br></p><p     class="list-item"><strong>Visualization.</strong> If you’re lucky (or if you have a very strong dimensionality reduction method), reducing down to just 2 or 3 dimensions preserves the important information in your data. If so, you can do a scatterplot, and use the power of your visual cortex to analyse your data (i.e. you can look at it).</p><p     class="list-item"></p>
            </figcaption>
       </section>


       <section id="slide-078">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-078" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0079.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we will restrict ourselves to <strong>linear reductions</strong>. To create one of the derived features z<sup>1</sup>, the only thin we are allowed to do is to pick one number for each feature, multiply them together and sum the result. These values we multiply by the original features should be the same for all instances.<br></p><p    >If we arrange these multipliers in a vector <strong>c'</strong>, then we can simply say that the reduced feature is the dot product of the original features <strong>x</strong> and the parameter vector <strong>c'</strong>. If we want more than one reduced feature, we can add additional parameter vectors. However, to keep things simple, we start with just one.<br></p><p    >The question is, how do we choose the elements of <strong>c'</strong>?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-078" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-079" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0080anim0.svg" data-images="22.Methodology2.key-stage-0080anim0.svg,22.Methodology2.key-stage-0080anim1.svg,22.Methodology2.key-stage-0080anim2.svg,22.Methodology2.key-stage-0080anim3.svg,22.Methodology2.key-stage-0080anim4.svg,22.Methodology2.key-stage-0080anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Since we're focusing on a single feature for now, we'll drop the subscript and call this feature "z". This is a single scalar value representing our instance <strong>x</strong>.<br></p><p    >The way we’ll find the parameters <strong>c'</strong> for our reconstruction is by optimizing the <strong>reconstruction error</strong>. We’ll come up with some function that reconstructs our data from the reduced points {z}. The closer this reconstruction is to the original point, the better.<br></p><p    >We’ll add the constraint that <em>both</em> the function that reduces the data and the function that reconstructs the data should be <strong>linear</strong>. This means that our reconstruction is just some second vector c, which we also get to choose, multiplied by the reduced feature z. We’ll also assume that the data is <strong>mean-centered</strong>, so that we won’t need to apply any translations: the mean of the original data, the reduced data, and the reconstructed data is zero or the zero vector.<br></p><p    >To recap, under these constraints, the reduction function consist of taking the dot product of our vector with some parameter vector <strong>c’</strong>, and the reconstruction function consists of multiplying our reduced representation with some other parameter vector <strong>c</strong>.<br></p><p    >We will try to choose our parameters <strong>c'</strong> and <strong>c</strong> in such a way that <strong class="blue">x</strong> is as close as possible to <strong class="blue">x'</strong>. Before we figure out how to do this, we can simplify our problem. We can show that for the optimal solution, the vectors <strong>c'</strong> and <strong>c</strong> must be the same. We''l show that first.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-079" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-080" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0082anim0.svg" data-images="22.Methodology2.key-stage-0082anim0.svg,22.Methodology2.key-stage-0082anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the reconstruction of x from z isolated in a diagram. Take a moment to study this picture. Note that we have fixed a line by our choice of <strong>c</strong>, and our reconstruction, because it can only be a multiple of <strong>c</strong>, must be somewhere on the line. <br></p><p    >We’ll work out what our functions should be in the following order. First, we will assume that we have the reconstruction function, and ask what the best reduction function is to use, in terms of that reconstruction function. Then we will work out an optimization objective for both of them together.<br></p><p    >Imagine that <strong>c </strong>is fixed. This could be at the optimal value, or some terrible value, but somebody has chosen <strong>c</strong> for us and we're not allowed to change it. Which value should we choose for z to put <strong class="blue">x'</strong> as close to <strong class="blue">x</strong> as possible?<br></p><p    >The closest we can get <strong class="blue">x’</strong> to <strong class="blue">x</strong> is to put <strong class="blue">x’</strong> where the line between <strong class="blue">x</strong> and <strong class="blue">x’</strong> makes a right angle with the line of <strong>c</strong>. This is the <strong>orthogonal projection</strong> of <strong class="blue">x</strong> onto <strong>c</strong>, and if you know your linear algebra, you’ll know the length of z<strong>c</strong> in this picture is related to the dot product of <strong class="blue">x</strong> and <strong>c</strong>. Why?</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-080" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-081" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0083anim0.svg" data-images="22.Methodology2.key-stage-0083anim0.svg,22.Methodology2.key-stage-0083anim1.svg,22.Methodology2.key-stage-0083anim2.svg" class="slide-image" />

            <figcaption>
            <p    >For our purposes, the length of  <strong>c </strong>doesn’t matter (if we make <strong>c</strong> longer or shorter it still defines the same line), so we’ll assume that it has length 1 (that is, it is a <strong>unit vector</strong>).<br></p><p    >From basic trigonometry, we know that the length of the black line is ||<strong class="blue">x</strong>|| cos α. Because ||<strong>c</strong>|| = 1, we can multiply by that without changing the value, which means that the length of the black line is equal to the dot product between <strong class="blue">x</strong> and <strong>c </strong>(remember the geometric definition of the dot product)<span>.</span><br></p><p    >If this seems a bit magical, see <a href="http://peterbloem.nl/blog/pca"><strong class="blue">peterbloem.nl/blog/pca</strong></a> for a more intuitive proof. It all boils down to the pythagorean theorem in the end.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-081" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-082" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0084anim0.svg" data-images="22.Methodology2.key-stage-0084anim0.svg,22.Methodology2.key-stage-0084anim1.svg" class="slide-image" />

            <figcaption>
            <p    >What this tells us, is that the projection of <strong>x</strong> onto <strong>c</strong> is found by taking their dot product. Since <strong>c</strong> has length one, this is the value that we want to multiply <strong>c</strong> by to get to <strong>x’</strong>.<br></p><p    >In other words, given <strong>c</strong>, we now know how to find our reduced data z, we take the dot product of the original features <strong class="blue">x</strong> with our reconstruction vector <strong>c</strong>.<br></p><p    >Taking the dot product of <strong>x</strong> with a parameter vector happens to be our reduction function. This means that we can set the vector in the reduction function equal to the vector in the reconstruction function: <strong>c'</strong> = <strong>c</strong>.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-083">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-083" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0085.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s how this has simplified our picture. The reduction and and reconstruction now have the same parameters <strong>c</strong>. Note that this required an additional assumption: that <strong>c</strong> is a unit vector.<br></p><p    >So here's the model: we pick some unit vector <strong>c</strong>, project our data onto it to represent it as a single scalar z, and then, to reconstruct the data, multiply <strong>c</strong> by z. As you can see, the reconstructed data necessarily lie on a line. All we are looking to do is to get these reconstructions as close to the original points as possible. If we manage that, it's reasonable to assume that we retained some information from the original features in the single reduced feature z.<br></p><p    >The only remaining question is, which <strong>c</strong> should we choose to minimize the reconstruction error?<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-084">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-084" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0086.svg" class="slide-image" />

            <figcaption>
            <p    >Here's some randomly generated data. Remember, we assumed that the data would be mean centered. Let's first pick a random direction <strong>c</strong>. And see what we get.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-085">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-085" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0087.svg" class="slide-image" />

            <figcaption>
            <p    >Here it is. The red points are our reconstructions. For each point, the new feature z is the distance from the origin to the red point. The grey lines indicate how far the reconstruction is from the original data. Note that these grey lines are orthogonal to the line described by <strong>c</strong>, because we are reducing our data by orthogonally projecting it onto <strong>c</strong>.<br></p><p    >Clearly, this is not a very good choice for <strong>c</strong>. The grey lines could be much shorter. This is how we’ll optimize for c. <strong>We’ll sum up the squares of the grey lines and minimize those.<br></strong></p><p    >We can think of optimizing <strong>c</strong> as making the grey lines rubber bands, that pull on the line representing <strong>c</strong> (which pivots around the origin). <br></p><p    >This is a lot like linear regression, but the task is slightly different. Note that there is no target attribute here, and the "residuals" are not parallel to one of the axes. <br></p><p    >Doing regression with the residuals drawn like this is sometimes called <span>orthogonal regression</span>.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-085" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-086" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0088anim0.svg" data-images="22.Methodology2.key-stage-0088anim0.svg,22.Methodology2.key-stage-0088anim1.svg,22.Methodology2.key-stage-0088anim2.svg,22.Methodology2.key-stage-0088anim3.svg,22.Methodology2.key-stage-0088anim4.svg,22.Methodology2.key-stage-0088anim5.svg" class="slide-image" />

            <figcaption>
            <p    >To find <strong>c</strong>, we will simply state our goal as an optimization objective. We want to find the <strong>c</strong> for which the squared distance between the data and the reconstructed data is minimized. We first fill in the definition of the reconstruction, and then the definition of the optimal z.<br></p><p    >In the definition of the Euclidean distance, the square root cancels our against the square in our optimization, so that we are left with a sum of the squares over every dimension i in every reconstructed instance <strong>x’</strong>.<br></p><p    >This leaves us with a simple objective to which we can apply any search algorithm, like gradient descent. One thing we must remember: we required that <strong>c</strong> is a unit vector. <br></p><p    >This means we have an optimization problem with <em>a constraint</em>. This is a technical subject, that we’ll see more of in lecture 6. For now, we can solve this problem by applying gradient descent and normalizing the vector <strong>c</strong> to scale it back to a unit vector after every gradient update. This is called the projection method for constrained optimization. It doesn’t always work, but it does here.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-087">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-087" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0089.svg" class="slide-image" />

            <figcaption>
            <p    >We run gradient descent and this is the solution that we find.  It looks pretty good. It’s hard to imagine any other line c leading to shorter grey lines.<br></p><p    >Note that the data is much more spread out along this line than it was for our earlier choice of <strong>c</strong>.<br></p><p    >We call this <strong>c</strong> the<strong> first principal component</strong> of the data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-088">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-088" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0090.svg" class="slide-image" />

            <figcaption>
            <p    >If we want to reduce the dimensionality to more than one dimension, we repeat the process. Keeping the first principal component fixed, the second principal component is the one orthogonal to the first that minimizes the reconstruction loss. This gives us two directions, orthogonal to one another, to project onto. Our reduced dataset has two features.<br></p><p    >Each next principal component is the direction orthogonal to all the previous ones, that minimizes the loss, when the data is reconstructed <em>using all of them</em>.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-089">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-089" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0091.svg" class="slide-image" />

            <figcaption>
            <p    >If you’ve heard about PCA before, you may be surprised by this definition using reconstruction loss. Usually, the principal components are defined as the directions in which the<em> variance</em> of the projected data is maximized. The best <strong>c</strong> is the line along which the orthogonal projections are the most spread out.<br></p><p    >The first principal component is the line along which the variance of the data is maximal when projected onto the line. The second principal component is the line orthogonal to the first for which the variance is maximal, and so on.<br></p><p    >It turns out, these two definitions are equivalent.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-090">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-090" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0092.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s look at the one dimensional reduction again to show why.<br></p><p    >The variance of a one-dimensional dataset is defined as the average of the squares of all the distances to the data-mean. In our case, both the data and the reduction are mean-centered, so the variance is just the sum of all the squares of the z’s; our reduced representations. In this picture, the length of the orange vector.<br></p><p    >Thus, maximising the variance, means choosing c so that the (squared) length of the orange vector is maximized<br></p><p    >This arrangement into a right-angled triangle means that the<span class="blue"> magnitude of the original data</span> (<span class="blue">p</span>, the squared distance to the mean) is related to the <span>variance of the projected data</span> (<span>q</span>) and the reconstruction error (r, in black)<span class="blue"> </span>by the Pythagorean theorem. <br></p><p    >Since <span class="blue">p</span>, the magnitude of the original data, is a constant,  <span>q</span><sup>2</sup> + r<sup>2</sup> is constant,  and minimizing the squared reconsturction error r<sup>2 </sup>is equivalent to maximising the variance of the projected data <span>q</span><sup>2</sup>.<br></p><p    >In the variance maximization view of PCA, we often talk about how much variance the reduced data <em>retains</em>, seeing the variance as a kind of “information content” in a representation of the data. A perfect reconstruction has the same total variance as the data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-091">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-091" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0093.svg" class="slide-image" />

            <figcaption>
            <p    >To apply PCA, we need to choose the number of dimensions to reduce to. We can just treat this as a hyperparameter and test different values. <br></p><p    >But if we plot the variance or the reconstruction loss against the number of components, we often see a natural <em>inflection</em> point. In this case, we can retain the majority of the variance in the data by keeping only the first three principal components. The higher components still add a little variance each, but not much.<br></p><p    >What happens if we keep going until the new data has the same number of features as the original?<br></p><p    >source: <a href="http://alexhwilliams.info/itsneuronalblog/2016/03/27/pca/"><strong class="blue">http://alexhwilliams.info/itsneuronalblog/2016/03/27/pca/</strong></a></p><p    ><a href="http://alexhwilliams.info/itsneuronalblog/2016/03/27/pca/"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-092">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-092" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0094.svg" class="slide-image" />

            <figcaption>
            <p    >If we do that, we get perfect reconstructions, but our z’s are still different from the original coordinates. We end up expressing the data in another <strong>basis</strong>. It turns out, that this actually gives us a <strong>whitening</strong> of the data: in the new basis, the data is uncorrelated, with variance 1 along each axis.<br></p><p    >The different principal components <strong>c</strong> are unit vectors, which are by definition all mutually orthogonal. This means that the vectors <span>c</span> form an orthonormal basis. If we multiply each with the standard deviation of the data projected onto <strong>c</strong>, we end up with a whitening basis.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-093">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-093" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0095.svg" class="slide-image" />

            <figcaption>
            <p    >This way of whitening is called <strong>PCA whitening</strong>. We apply PCA with the same number of target dimensions as data dimensions. This gives us an orthonormal basis in which the data is uncorrelated. If we then measure the standard deviation along each component and multiply the basis vectors by that, we get a basis in which the data is whitened.<br></p><p    >While σ and<strong> c</strong> together is not an orthonormal basis, <strong>c</strong> by itself is. Thus, we can still easily transform back and forth between the whitened basis and the original data coordinates.<br></p><p    >Note also that this implies that if we used PCA for dimensionality reduction, the data will also be whitened (if we standardize it afterwards). The first n principal components are always the same, no matter how many more we decide to compute. Thus, the PCA reduction just gives us the k most important dimensions of the PCA whitened data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-094">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-094" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0096.svg" class="slide-image" />

            <figcaption>
            <p    >If you’ve heard about PCA before, you may be wondering why I haven’t discussed eigenvector, or singular value decompositions. These topics are only necessary if you want to know the deeper workings of PCA, and if you want to compute it efficiently.<br></p><p    >Computing PCA by gradient descent, one component at a time is illustrative, but in practice, there are far more efficient and precise ways to do it. <br></p><p    >To understand PCA better, and to see the relation to eigenvectors, see <a href="http://peterbloem.nl/blog/pca-2"><strong class="blue">peterbloem.nl/blog/pca-2</strong></a>.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-095">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-095" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0097.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-096">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-096" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0098.svg" class="slide-image" />

            <figcaption>
            <p    >This may seem like a lot of math and complexity for something so simple as reducing the dimensionality of a dataset. <br></p><p    >But it turns out that these principal components are actually extremely versatile, and can give us a lot of insight into our data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-097">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-097" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0099.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll start with an example of how PCA is often used in research. Imagine you’re a palaeontologist, and you find a shoulder bone, belonging to some great ape.<br></p><p    >If you are a trained anatomist specialising in primates, you can easily tell for a single shoulder bone whether it’s an early hominin fossil, which is a very rare find, or a chimpanzee fossil which isn’t rare. But how do you then substantiate this? “It’s true because I can see that it is” is not very scientific.<br></p><p    >image source: <a href="https://science.sciencemag.org/content/338/6106/514.full"><strong class="blue">https://science.sciencemag.org/content/338/6106/514.full</strong></a></p><p    ><a href="https://science.sciencemag.org/content/338/6106/514.full"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-098">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-098" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0100.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s one common approach. Take a large collection of the same specific bone (the <em>scapula,</em> or shoulder blade, in this case) from different apes and humans, and take a bunch of measurements (features) of each. Do a PCA, and plot the first two principal components. As you can see, the different species form very clear clusters, even in just two dimensions. <br></p><p    >When we find a new fossil, we can see where it ends up in this space, and we can then show that what we’ve found is clearly closer to human than to chimp just by measuring it, and projecting it into this space.<br></p><p    >Note also, that this data gives us some clues about how humans might have developed. The proto-humans <em>Australopithecus Afarensis </em>and <em>Australopithecis Sediba</em>, are both on a straight line between the cluster of Bonobos, Chimps and Gorillas on one side and modern humans on the other. These are indeed the great apes considered to be most like the ones from which we developed.<br></p><p    >source: Fossil hominin shoulders support an African ape-like last common ancestor of humans and chimpanzees. Nathan M. Young, Terence D. Capellini, Neil T. Roach and Zeresenay Alemseged <a href="http://www.pnas.org/content/112/38/11829"><strong class="blue">http://www.pnas.org/content/112/38/11829</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-098" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-099" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0101anim0.png" data-images="22.Methodology2.key-stage-0101anim0.png,22.Methodology2.key-stage-0101anim1.png" class="slide-image" />

            <figcaption>
            <p    >Here is another example of what PCA can tell us about a high-dimensional dataset.<br></p><p    >In this research, the authors took a database of 1387 Europeans and extracted features from their DNA. They used about half a million sites on the DNA sequence where DNA varies among humans (i.e. 1387 instances: people, and 500k features: DNA markers). They also recorded where their subjects (or their immediate ancestors) were from.<br></p><p    >Only the DNA data was fed to the PCA algorithm, with the person’s origin only used afterward to color the points.<br></p><p    >It turns out that the two principal components of this data largely express how far north the person lives, and how far east the person lives. This means that if you plot the data in the first two principal components, <strong>you get a fuzzy picture of Europe</strong>. <br></p><p    >In short, the large scale geography of Europe can be extracted from our DNA. If I sent a large sample of European DNA to some aliens on the other side of the galaxy who’d never seen our planet, they could use it to get a rough idea of our geography.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-100">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-100" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0102.svg" class="slide-image" />

            <figcaption>
            <p    >Finally, possibly the most magical illustration of PCA: <strong>eigenfaces</strong>. <br></p><p    >Here we have a dataset (which you can easily get from sklearn) containing 400 images, in 64x64 grayscale, of a number of people. The lighting is nicely uniform and the facial features are always in approximately the same place.<br></p><p    >We take each pixel as a feature, giving us 400 instances each represented by a 4096-dimensional feature vector. Note that this essentially flattens the image into one long vector, ignoring the grid structure of the pixels.<br></p><p    >The prefix eigen- comes from the eigendecomposition often used to derive the PCA analysis. It’s out of scope for us, but you should hopefully remember eigenvectors from you linear algebra. It turns out the eigenvectors of the covariance matrix <a href="http://peterbloem.nl/blog/pca-2"><strong class="blue">are the principal components</strong></a>.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-101">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-101" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0103.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the sample mean of our data, re-arranged back into an image.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-102">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-102" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0104.svg" class="slide-image" />

            <figcaption>
            <p    >Once we have the principal components, each a 4096-dimensional vector, we can take their values, assign them a color, like red for negative values, blue for positive values, and re-arrange them back into images. Remember, every dimension represents a pixel.<br></p><p    >These are the first 30 principal components displayed this way (top left is the first, to the right of that is the second and so on).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-103">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-103" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0105.svg" class="slide-image" />

            <figcaption>
            <p    >Here is one way to interpret the principal components: the basis vectors that are most natural for our data. Remember, PCA is also a whitening operation. <br></p><p    >The first principal component is the direction that captures most of the variance of our data. Or, projecting our data down to the first principal component gives us the lowest reconstruction error. <br></p><p    >We can visualize this space, by starting at the data mean, and adding a small bit of the nth principal component.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-103" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-104" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0106anim0.svg" data-images="22.Methodology2.key-stage-0106anim0.svg,22.Methodology2.key-stage-0106anim1.svg,22.Methodology2.key-stage-0106anim2.svg,22.Methodology2.key-stage-0106anim3.svg,22.Methodology2.key-stage-0106anim4.svg" class="slide-image" />

            <figcaption>
            <p    >Starting from the mean face (in the middle column), we take little steps along the direction of one of our principal components (or in the opposite direction). These are the first five.<br></p><p    >We see that moving along the first principal component roughly corresponds to ageing the face. Moving along the fourth seems to make the face more feminine.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-105">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-105" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0107.svg" class="slide-image" />

            <figcaption>
            <p    >Instead of starting at the mean face, we can also start at some other point, like one of our instances, and add or subtract small bits of the principal components.<br></p><p    >The reason that we can add the principal components directly to the data like this is that the reduction and reconstruction are linear operations. If we use nonlinear versions of PCA, this trick won't work anymore. Details in the reading materials.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-105" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-106" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0108anim0.svg" data-images="22.Methodology2.key-stage-0108anim0.svg,22.Methodology2.key-stage-0108anim1.svg,22.Methodology2.key-stage-0108anim2.svg,22.Methodology2.key-stage-0108anim3.svg,22.Methodology2.key-stage-0108anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The middle column represents the starting point. To the right we add the k-th principal component, to the left we subtract it. Note, in particular the effect of the fifth principal component: subtracting it opens the mouth, and adding it seems to push the lips closer together.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-106" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-107" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0109anim0.png" data-images="22.Methodology2.key-stage-0109anim0.png,22.Methodology2.key-stage-0109anim1.png,22.Methodology2.key-stage-0109anim2.png,22.Methodology2.key-stage-0109anim3.png,22.Methodology2.key-stage-0109anim4.png" class="slide-image" />

            <figcaption>
            <p    >To reconstruct a point, we start with the mean, and add a bit of the first principal component, then of the second principal component and so on.<br></p><p    >If we think of our principal components as a new<strong> basis</strong> for our data, then we are just looking up our point by first moving some distance along the first axis, then along the second axis and so on. Just like we would look up a point given its coordinates in the standard basis. <br></p><p    ><br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-108">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-108" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0110.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s what that looks like. top left is the mean. To the right is the reconstruction from just the first principal component. Next is what we get is we add the second principal component to that and so on.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-109">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-109" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0111.svg" class="slide-image" />

            <figcaption>
            <p    >After 60 principal components out of a possible 4096, the image starts to look pretty recognizable. We’ve reduced our data from 4096 dimensions to just 60 dimensions, and still retained enough information to tell people apart.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-110">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-110" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0112.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-111">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-111" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0113.svg" class="slide-image" />

            <figcaption>
            <p    >One final thought to consider:the bias/variance view can cast a new light on the topics we've seen today. Imagine if you have a dataset and you train a linear model on it. We've seen that a linear model can be perfectly optimized by analytical means, so this should be a very efficient approach.<br></p><p    >We've also seen that you can expand its features to make the model more expressive. For instance, this allows a linear model to take the shape of a parabola in the original feature space. We are increasing the model expressivity by doing this. This means that the bias will shrink, because the model will fit the data better, but also that we risk an increase in variance, because the model may begin to overfit.<br></p><p    >The key insight here is that dimensionality reduction, like that provided by PCA, is the opposite of this. If we start with a lot of features already (like all the pixels in an image), then even a simple linear model may already overfit, and put us in the high variance regime. PCA allows us to reduce the features to a mixture that retains only the crucial information: we take information from all features, but we throw away the noise that the model would otherwise overfit on. This pushes us away from the high variance regime, and, if we go too far, towards the high bias regime.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-112">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-112" title="Link to this slide.">link here</a>
            <img src="22.Methodology2.key-stage-0114.svg" class="slide-image" />

            <figcaption>
            <p    >In short, don't think of all the learning coming from the modelling and searching part. A skilled machine learning practitioner can get a lot of mileage out of a plain linear model, and a large amount of clever data preparation. <br></p><p    >And the first thing they will do, is to <strong>look at their data</strong>.</p><p    ></p>
            </figcaption>
       </section>

</article>
