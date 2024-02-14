---
title: "Lecture 4: Probabilistic models"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 4: Probabilistic models</li>
                <li><a href="#video-000">Learning with probability</a></li>
                <li><a href="#video-021">(Naive) Bayes classifiers</a></li>
                <li><a href="#video-042">Logistic regression</a></li>
                <li><a href="#video-070">Information theory</a></li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/31.ProbabilisticModels1.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">

        <section class="video" id="video-000">
            <a class="slide-link" href="https://mlvu.github.io/probability#video-0">link here</a>
           <video controls>
                <source src="https://surfdrive.surf.nl/files/index.php/s/zRr6EpCfNiPLmtn/download" type="video/mp4" />

                Download the <a href="https://surfdrive.surf.nl/files/index.php/s/zRr6EpCfNiPLmtn/download">video</a>.
           </video>
        </section>


       <section id="slide-001">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-001" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we'll start to connect <strong>probability theory</strong> with machine learning. We will first focus on <em>model selection</em>. We will not yet worry about abstract tasks like classification or regression, we will simply look a the case where we see some data, and we use probability theory to select a <em>model</em> for that data. In the next video, we will see how this translates to classification.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-002">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-002" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0002.svg" class="slide-image" />

            <figcaption>
            <p    >Before we start, note that we assume a certain familiarity with probability theory. There is a video in <a href="https://mlvu.github.io/preliminaries/"><strong class="blue">the preliminaries lecture</strong></a> to help you brush up on the basics.<br></p><aside    >As you may be able to tell, that part of the preliminaries lecture used to be part of this lecture, so it should work very well as an introduction to the basics. Be sure to look at it if you feel lost in the early part of this lecture.<br></aside><p    >The concepts shown here are probably the most important for this course.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-003" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-003" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0003anim0.png" data-images="31.ProbabilisticModels1.key-stage-0003anim0.png,31.ProbabilisticModels1.key-stage-0003anim1.png" class="slide-image" />

            <figcaption>
            <p    >Here is an analogy for the way probability is usually applied in statistics and machine learning. We assume some “machine” (which could be any natural process, the universe, or an actual machine) has <em>generated</em> our data, by a process that is partly deterministic and partly random. The configuration of this machine is determined by its <strong>parameters </strong>(theta). <span class="blue">θ</span> could be a single number, several numbers in a vector, or even a complicated data structure containing a lot of numbers in a complex arrangement.<br></p><p    >We know how the machine works, so if we know <span class="blue">θ</span>, we know the probability of seeing any given dataset. Given <span class="blue">θ</span>, we can easily work out the probability of all possible datasets. The problem is that we are not given <span class="blue">θ</span>, we are given the data, and we want to work out the state of the machine. <br></p><p    >In practice, the "machine" takes the form of a probability distribution, and the configuration of the machine is determined by its parameters <span class="blue">θ</span>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-004" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-004" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0004anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0004anim0.svg,31.ProbabilisticModels1.key-stage-0004anim1.svg" class="slide-image" />

            <figcaption>
            <p    >In <strong>frequentist learning</strong>, we are given some data and our job is to guess the true model (out of a set of models) that generated some data. In other words, pick the right parameters <span class="blue">θ</span> so that the probability distribution fits the data well.<br></p><p    >In the frequentist view of the world, <strong>the true model is not subject to probability</strong>. Which model generated the data doesn’t change if we repeat the experiment, so we shouldn’t apply probability to it. We just try to guess which one it is. We won't be exactly right, but we can hopefully get close. This is typical of frequentist approaches: we build algorithms that gives us a <strong>point estimate</strong> for our model parameters. That is, they return <em>one </em>point in our model space. One guess for <span class="blue">θ</span>.<br></p><p    >We can use different criteria to decide which model we want to pick. Probably the most common criterion is that we should guess the model for which the probability of seeing the data that we saw is highest. This is called the<em> </em><strong>maximum likelihood principle</strong>. Under the maximum likelihood principle picking a model becomes an<em> optimization </em>problem.<br></p><aside    >It’s fine if this sounds a little abstract right now, we’ll look at plenty of examples. Note however, that this single idea is how almost every modern machine learning model defines its loss function. It is going to come back again and again in the course, so you’ll need to become very familiar with this idea.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-005">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-005" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0005.svg" class="slide-image" />

            <figcaption>
            <p    >To explain maximum likelihood fitting, let’s look at a simple example. We have two coins, a bent one and a straight one. Flipping these coins gives us different probabilities of heads and tails. <br></p><p    >We ask a friend to pick a random coin once without showing us, and to flip it twelve times. The resulting sequence has more heads than tails, but not such a disparity that you would never expect it from a fair coin. If we had to guess which coin our friend had picked, which should we guess?<br></p><p    >image source: <a href="https://www.magictricks.com/bent.html"><strong class="blue">https://www.magictricks.com/bent.html</strong></a><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-006">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-006" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0006.svg" class="slide-image" />

            <figcaption>
            <p    >This is a simple version of a <strong>model selection</strong> problem. Our model class consists of two models (the two coins) and our data consists of 12 instances (the results of the coin flips).<br></p><p    >In more technical terms, the coins are Bernoulli distributions with parameter 1/2 and  and 4/5 respectively. We could also look at the model space of all Bernoulli distributions, but to simplify matters we are looking at just these two. <br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-007">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-007" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0007.svg" class="slide-image" />

            <figcaption>
            <p    >The maximum likelihood principle tells us to pick the coin for which the likelihood is the greatest. We simply compute, for both coins, the probability of the data that we saw given the coin. The coin that gives us the highest value is the coin we choose.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-008">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-008" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0008.svg" class="slide-image" />

            <figcaption>
            <p    >Since the coin flips are independent, the probability over the whole sequence is just the product over the probabilities of the individual flips. There’s not much in it, but the likelihood for the <em>bent </em>coin is slightly higher, so that’s the preferred model under the maximum likelihood criterion.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-009">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-009" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0009.svg" class="slide-image" />

            <figcaption>
            <p    >When we do this kind of computation, we often take the <strong>logarithm of the likelihood</strong>, instead of the plain likelihood. The logarithm is a monotonic function (it always gets bigger if the input gets bigger) so the likelihood and the log-likelihood have their maxima in the same place, but the log-likelihood is often easier to manipulate symbolically (see the first homework exercise). It can also provide a smoother loss landscape for methods like gradient descent.<br></p><p    >The log-likelihood of a probability distribution is a lot like the loss functions we’ve already encountered.<br></p><p    >In fact, if we want to fit a probability distribution with a gradient based method, we usually take the <em>negative</em> log-likelihood, so that we can do gradient <em>descent</em> to find the optimum. <br></p><aside    >We could also use gradient <span>ascent</span> on the log-likelihood, but it's nice to keep the convention that you always minimize functions, and as we will see at the end of the lecture, the negative logarithm of a probability actually has a very natural interpretation.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-010">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-010" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0010.svg" class="slide-image" />

            <figcaption>
            <p    >As a second example of maximum likelihood, let's look at the univariate (i.e. 1D) normal distribution. This is defined by a complicated probability density function, which we don't fully understand yet. What we want to show here is how much of this complexity disappear just by taking the logarithm.<br></p><p    >The probability density of our whole data, given some mean and standard deviation, is simply the product of all individual probability densities. This follows from the assumption that instance data is independently drawn from the same distribution.  <br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-011" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-011" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0011anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0011anim0.svg,31.ProbabilisticModels1.key-stage-0011anim1.svg,31.ProbabilisticModels1.key-stage-0011anim10.svg,31.ProbabilisticModels1.key-stage-0011anim11.svg,31.ProbabilisticModels1.key-stage-0011anim12.svg,31.ProbabilisticModels1.key-stage-0011anim13.svg,31.ProbabilisticModels1.key-stage-0011anim14.svg,31.ProbabilisticModels1.key-stage-0011anim2.svg,31.ProbabilisticModels1.key-stage-0011anim3.svg,31.ProbabilisticModels1.key-stage-0011anim4.svg,31.ProbabilisticModels1.key-stage-0011anim5.svg,31.ProbabilisticModels1.key-stage-0011anim6.svg,31.ProbabilisticModels1.key-stage-0011anim7.svg,31.ProbabilisticModels1.key-stage-0011anim8.svg,31.ProbabilisticModels1.key-stage-0011anim9.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    >Here’s an illustration of what it looks like to find the maximum likelihood value for the mean of a normal distribution (in one dimension). We will fix the variance to some arbitrary value, and worry about that later.<br></p><p    >If we pick some arbitrary mean on the left side, we see that all the data points on the right side get a very low probability density. This means that the likelihood of the whole dataset under this model is probably poor (that is, a relatively low value).<br></p><p    >If we pick a mean on the right side of the axis, the data points on the left are given low probability density, and we get equally low likelihood for this data.<br></p><p    >To find a model which gives the data a high likelihood, we need to align the cluster of datapoints in the middle with the region of high probability density in the middle of the bell curve.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-012">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-012" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0012.svg" class="slide-image" />

            <figcaption>
            <p    >If we keep the mean fixed, and look at the variance, we see that there is a tradeoff: high variance gives the outliers a high density, but hurts the density we get from the cluster in the middle.<br></p><p    >The maximum likelihood objective balances this tradeoff for us, putting most of the density in the middle, without letting the density of any point get too low.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-013" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-013" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0013anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0013anim0.svg,31.ProbabilisticModels1.key-stage-0013anim1.svg,31.ProbabilisticModels1.key-stage-0013anim2.svg,31.ProbabilisticModels1.key-stage-0013anim3.svg,31.ProbabilisticModels1.key-stage-0013anim4.svg,31.ProbabilisticModels1.key-stage-0013anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s how that idea works out mathematically.<br></p><p    >We assume that X is a list of single numbers. We want to find the parameters that maximize the log probability density of this data given the parameters. The probability density of the whole dataset is simply the product of the individual probability densities, if we assume that the data was independently drawn from the same distribution.<br></p><p    >Since there's a factor raised to the power of <em>e</em> inside this function, we'll use the natural logarithm (base e). With a bit of luck, these will cancel out.<br></p><p    >We can turn this product into a sum by moving the logarithm inside. <em>This is explained in detail in the first homework.</em><br></p><p    >We fill in the definition of the actual probability density function we’re using (line 3). This function is the product of two factors (the division and the exponent). Both of these become terms if we work them out of the logarithm. In the second term the exponent cancels against the logarithm. Already the function we are maximizing looks a lot simpler.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-014">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-014" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0014.svg" class="slide-image" />

            <figcaption>
            <p    >This is enough to show that with the log likelihood we have another “landscape” on top of our model space. The <span>mean</span> and <span class="blue">variance</span> that give us the best fit to our data (under the maximum likelihood principle) are in the center of the bright area.<br></p><p    >If we didn’t want to work out the rest analytically, we could just find the optimum by gradient descent or even by random search. <br></p><aside    >In statistics courses, you will often take the derivative of the objective function and set it equal to zero to find that the optimal value for the mean is actually the mean of your sample, and the optimal value for the variance is actually the variance of your sample.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-015" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-015" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0015anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0015anim0.svg,31.ProbabilisticModels1.key-stage-0015anim1.svg,31.ProbabilisticModels1.key-stage-0015anim2.svg,31.ProbabilisticModels1.key-stage-0015anim3.svg,31.ProbabilisticModels1.key-stage-0015anim4.svg" class="slide-image" />

            <figcaption>
            <p    >If we look at each parameter individually, we can reduce the problem even more. We'll try this for<span> the mean </span>just to show the principle.<br></p><p    >We can remove the first term, since it doesn't contain the mean. The factor 1/(2<span class="blue">σ</span><sup>2</sup>) can be moved outside the sum and then removed (since a positive constant factor won't affect where the maximum is).<br></p><p    >Maximizing a function is the same as minimizing the negative of that function, so we can remove the minus and turn the argmax into an argmin.<br></p><p    >This shows that the maximum likelihood solution for the mean is just the value that minimizes the sum of the squared distances between the mean and the values in the dataset. This is how assuming a normal distribution leads to a least squares loss. For now, the main message is that even if your likelihood function looks really complicated, it's often the case that when you take the logarithm and maximize it, all that complexity disappears.<br></p><aside    >If you work this out analytically, as we'll do in the next lecture, you'll see that the minimum for this is the (arithmetic) mean of the data. <br></aside><aside    >This connection between the normal distribution, the least squares loss and the artihmetic mean is a deep one. Don't worry if you don't quite get it yet, we'll come back to this a few more times.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-016" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-016" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0016anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0016anim0.svg,31.ProbabilisticModels1.key-stage-0016anim1.svg,31.ProbabilisticModels1.key-stage-0016anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We'll finish up with a quick look at <strong>Bayesian learning</strong>. We are now using subjectivist probability, so <strong>we are free to assign each potential model a probability</strong>. We don’t know the true parameters, but the data gives us some idea, so we express that uncertainty with a probability distribution <em>over the model space</em>.<br></p><p    >That is, we'd like to know the distribution p(<span class="blue">θ</span>|D): a distribution over all available models, given the data that we've observed. As usual, the distribution with the reverse conditional p(D|<span class="blue">θ</span>) is much easier to work out. So the first thing we do is apply Bayes' rule to relate the two conditionals to one another.<br></p><p    >The distribution we want to work out is called the <strong>posterior distribution</strong>. Posterior means "after", as in: this is our belief about the true model <em>after</em> we've seen the data.<br></p><p    >The three parts of the right-hand side have these names. The <strong>prior distribution</strong> is a name you’ll hear often. Prior means before, as in: this is our belief about the true model <em>before</em> we've seen the data. For instance, if we do spam classification in a Bayesian way, we might have a prior belief about the probability of getting a spam email, which we then <strong>update</strong> by looking at the content of the email (the data). Our beliefs about the parameters after seeing the data, is expressed by the posterior distribution. <br></p><p    >Note that Bayesian learning does, in principle, not require us to search or optimize anything. If we can work out the function on the right hand side of this equation, we get the posterior distribution and that gives us everything we need. If we need a good model, we can pick the one to which p(<span class="blue">θ</span>|X) assigns the highest probability, or we can sample a model and get a good fit with high probability. We can also study other properties of the distribution: for instance the variance of this distribution is a good indication of how uncertain we still are about the parameters of the model. <br></p><aside    >In some cases, like for normal distributions, we can work all of this out analytically, and we get a formula expressing the posterior distribution. For more complicated models, it’s usually impossible to work out the posterior analytically, and we have to make do with a function that approximates it, or with an algorithm that samples from the posterior. At that point, working out the posterior usually starts to look a lot like the searching we have to do in frequentist methods and general machine learning.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-017" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-017" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0017anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0017anim0.svg,31.ProbabilisticModels1.key-stage-0017anim1.svg" class="slide-image" />

            <figcaption>
            <p    >That may all sound a little abstract, so let's return to our coin example and see what a Bayesian approach would look like there.<br></p><p    >We first need to establish a prior. What is the probability of each coin in our model space? We said that we’d asked a friend to pick a coin at random. If we assume that he follows our instructions, then we believe each coin is equally likely so both get 0.5 probability. If we had two fair coins and one bent one, we could set the prior to 1/3 for bent and 2/3 for fair. Or, if we expected our friend to have a preference for the bent coin, we might set our prior differently.<br></p><p    >This is an important thing to understand about choosing a prior: <strong>it allows us to encode our </strong><em>assumptions</em><strong> about the problem</strong>. As we will see again and again, encoding your assumptions is a very important part of designing machine learning models.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-018" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-018" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0018anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0018anim0.svg,31.ProbabilisticModels1.key-stage-0018anim1.svg,31.ProbabilisticModels1.key-stage-0018anim2.svg,31.ProbabilisticModels1.key-stage-0018anim3.svg" class="slide-image" />

            <figcaption>
            <p    >After the prior, we need to work out the model evidence p(D). This is the probability of the data with the model marginalized out. Independent of the model, how likely are we to see this data at all? We work this out by making the marginalization explicit, and replacing the joint probabilities by their conditionals.<br></p><p    >Then, the posterior is just the proportion of one of the terms in this sum to the total.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-019">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-019" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0019.svg" class="slide-image" />

            <figcaption>
            <p    >Here's how we looked at Bayes' rule before.<br></p><p    >We see the available models (bent and straight) as the two possible causes for our data. The marginal probability of seeing this data is the probability of picking straight and seeing it plus picking bent and seeing it. The proportion of the straight term in this sum is the probability of seeing straight given the data.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-020" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-020" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0020anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0020anim0.svg,31.ProbabilisticModels1.key-stage-0020anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If we choose a  uniform prior (each model gets the same probability), then the priors cancel out and we are just left with a function of the conditional data probabilities that we've worked out already for the frequentist example.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-021">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-021" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0021.svg" class="slide-image" />

            <figcaption>
            <p    >Filling these in gives us these posterior probabilities for the <span class="red">straight</span> and the <span>bent</span> coins.<br></p><p    >Compare this with the maximum likelihood case. Both approaches prefer the <span>bent</span> model as an explanation for the data.<br></p><p    >However, in the maximum likelihood case, even though the differences between the two likelihoods were small, we only provided<em> one </em>guess for the true model. In the Bayesian approach we get a <em>distribution</em> on the model space. It tells us not just that <span>bent</span> is the more likely model, but also that<em> both models</em> are still quite likely. In this sense, getting a posterior distribution is a much more valuable result than getting a point estimate for your model.<br></p><p    >The downside of Bayesian analysis is that as the models get more complex, it gets more and more difficult to accurately approximate the posterior, and trying to do so is what has led to some of the most complicated material in machine learning. Working out the posterior for the mean of a normal distribution is already a bit too technical for this course, but it's a good exercise to try and imagine what it would involve.</p><p    ></p>
            </figcaption>
       </section>



        <section class="video" id="video-021">
            <a class="slide-link" href="https://mlvu.github.io/probability#video-21">link here</a>
           <video controls>
                <source src="https://surfdrive.surf.nl/files/index.php/s/JBXnid4OXnbfZQM/download" type="video/mp4" />

                Download the <a href="https://surfdrive.surf.nl/files/index.php/s/JBXnid4OXnbfZQM/download">video</a>.
           </video>
        </section>


       <section id="slide-022">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-022" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0022.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we’ll try to connect this probability business to the abstract tasks of machine learning. Specifically, we’ll look at <strong>classification</strong>.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-023">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-023" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0023.svg" class="slide-image" />

            <figcaption>
            <p    >We will focus on building <strong>probabilistic classifiers</strong>. These are classifiers that return not just a class for a given instance x (or a ranking) but a <em>probability over all classes</em>.<br></p><p    >This can be very useful. We can use the probabilities to extract a ranking (and plot an ROC curve) or we can use the probabilities to assess how certain the classifier is about its judgement. <br></p><p    >Note that a probabilistic classifier is also immediately a ranking classifier (if we rank by how likely the positive class is) and a regular classifier (if we pick the class with the highest probability).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-024" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-024" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0024anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0024anim0.svg,31.ProbabilisticModels1.key-stage-0024anim1.svg" class="slide-image" />

            <figcaption>
            <p    >There are two approaches to casting the classification problem in probabilistic terms. <br></p><p    >A <strong>generative classifier</strong> focuses on learning a distribution on the feature space given the class p(X=<strong>s</strong>|<span>Y</span>). This distribution is then combined with Bayes’ rule to get the probability over the classes, conditioned on the data. <br></p><aside    >The key part of this process is to work out the probability of the instance X given that its class is Y. We can think of this as a probability distribution that generates the data (hence the name).<br></aside><p    >A<strong> discriminative classifier</strong> learns the function p(<span class="blue">Y</span>|X=<strong>x</strong>) directly with X as input and class probabilities as output. It functions as a kind of regression, mapping <strong>x</strong> to a vector of class probabilities.<br></p><p    > We’ll look at some simple generative classifiers in this video, and then we'll describe a discriminative classifier in the next video.<br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-025">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-025" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0025.svg" class="slide-image" />

            <figcaption>
            <p    >Here are three approaches, arranged from impractical but entirely correct to highly practical, but based on largely incorrect assumptions.<br></p><p    >We won’t discuss the Bayes optimal classifier in this course, but it’s worth knowing that it exists, and that it means something different than a (naive) Bayes classifier.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-026">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-026" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0026.svg" class="slide-image" />

            <figcaption>
            <p    >For the Bayes classifier, we start with the probability we’re interested in p(<span class="blue">Y</span>|X): the probability of the class given the data. Note that X in the conditional refers to a single instance.<br></p><aside    >We'll focus on binary classification to make things concrete, but the methods in this video translate naturally to multiclass problems.<br></aside><p    >We rewrite p(<span class="blue">Y</span>|X) using Bayes’ rule. From the final form, we see that if we compute, for all classes, the probability functions p(X|<span class="blue">Y</span>), the data given the class and p(<span class="blue">Y</span>), the prior probability of the class, we can compute the probabilities we are interested in: the class probabilities given the data.<br></p><p    >So, the task becomes to learn functions for those two probabilities. The most important part will be P(X|<span class="blue">Y</span>). We can model this by separating the data by class and fitting a probability distribution to each subset individually.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-027" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-027" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0027anim0.png" data-images="31.ProbabilisticModels1.key-stage-0027anim0.png,31.ProbabilisticModels1.key-stage-0027anim1.png" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    >For this example, we will use a multivariate normal distribution (MVN). This is just an extension of the normal distribution to multiple dimensions. Its density curve (for a two dimesnsional space) looks like a rotation of the familiar bell curve, as shown on the left.<br></p><p    >In two dimensions we often draw MVNs as ellipses, since this is a natural way of expressing where most of the probability mass is concentrated. The picture on the right shows three MVNs fitted to three subsets of a data set.<br></p><p    >The formula for the MVN is given below. It’s a complicated beast, but all you really need to know is that for a given dataset, of N features, we can work out analytically which vector <strong>μ</strong> and which matrix <strong class="blue">Σ</strong> give us the best fitting MVN (under the maximum likelihood principle). As you might expect, these are the sample mean, and the sample covariance matrix. If you can compute those, you can fit an MVN to your dataset.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-028" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-028" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0028anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0028anim0.svg,31.ProbabilisticModels1.key-stage-0028anim1.svg,31.ProbabilisticModels1.key-stage-0028anim2.svg,31.ProbabilisticModels1.key-stage-0028anim3.svg,31.ProbabilisticModels1.key-stage-0028anim4.svg,31.ProbabilisticModels1.key-stage-0028anim5.svg,31.ProbabilisticModels1.key-stage-0028anim6.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the algorithm for a simple Bayes classifier. We choose a model class for P(X|<span class="blue">Y</span>). In this case, multivariate normal distributions (MVNs), but other distributions would work too.<br></p><p    >We then separate the points by classes and fit a separate MVN to each of these subsets of the data. We use the maximum likelihood estimates to fit the MVNs to the instances. <br></p><aside    >Note that this make the Bayes classifier a bit of a Bayesian/frequentist chimera: we are using Bayes' rule to reverse the conditional, but we are using point esitmates to fit our distributions.<br></aside><p    >The <strong>class prior</strong> p(<span class="blue">Y</span>) is a simple categorical distribution over the classes. We can estimate this from the data, or use some kind of prior knowledge that we have about the domain.<br></p><p    >Strictly speaking, we are mixing probabilities and probability densities, but in this case that doesn't cause any problems. The resulting probability on the classes is a categorical distribution.<br></p><aside    >When we compute the class probabilities, we can compute the term p(x | class)p(class) once for each term, and then re-use them in the computation of each class probability. If we are only interested in the most probable class or in the ranking, we can omit the computation of the denominator.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-029">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-029" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0029.svg" class="slide-image" />

            <figcaption>
            <p    >Here is an example of what that looks like with 2 features. On the left we have two classes, blue and black. We fit a 2D normal distribution to each, represented by the blue and black ellipses. Then, for a new point, we see which assigns the new point the highest probability density, or compute the full probabilities.<br></p><p    >The red line provides the decision boundary: the points where the two probability densities are exactly equal.<br></p><p    >source: <a href="http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes"><strong class="blue">http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes</strong></a><br></p><p    ><br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-030">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-030" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0030.svg" class="slide-image" />

            <figcaption>
            <p    >This works well for small numbers of features, but if we have many features, modelling the dependence between each pair of features gets very expensive. <br></p><p    >A crude, but very effective solution is <strong>naive Bayes</strong>. This just assumes that all features are independent, conditional on the class (for all classes).<br></p><p    >Note that <em>we do not assume that the features are independent</em>: it’s perfectly possible for one feature to be dependent on another feature, but they are <em>conditionally</em> independent. Informally, the dependency between the features is “caused” by the class and nothing else. Just like Alice and Bob in the first video: their lateness had only one possible shared cause, the monster, and once we’d isolated that, their lateness was independent.<br></p><p    >Since naive Bayes is often used with<strong> categorical features</strong>, we'll work out an example on those. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-031">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-031" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0031.svg" class="slide-image" />

            <figcaption>
            <p    >Here is an example dataset with binary features. The instances are emails to be classified as ham or spam, and each feature indicates whether a particular word occurs in that instance.<br></p><p    >We are building a generative classifier, so we should start by estimating the probability of the data given the class. The Naive Bayes assumption says that we can do this for each feature independently and just multiply the probabilities. <br></p><p    >We will estimate p(“pill”|<span class="red">spam</span>) as the relative frequency with which the “pill” feature was<span class="blue"> true</span> for <span class="red">spam</span> emails, and similar for the other feature. That is, we simply count the number of times this occurred in the dataset, divided by the total number of spam emails in the dataset.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-032">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-032" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0032.svg" class="slide-image" />

            <figcaption>
            <p    >Here's what those estimates look like.<br></p><aside    >More formally, we could say we are modelling X<sub>1</sub> as a Bernoulli distribution whose parameter we estimate as 2/6. This estimation, using the relative frequency of outcome x as the probability of x, is the maximum likelihood estimate for the Bernoulli distribution. If that sounds too complicated, it hopefully also makes intuitive sense to estimate the probabilities this way.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-033">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-033" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0033.svg" class="slide-image" />

            <figcaption>
            <p    >We do the same for the <span class="red">spam</span> class and for the other feature.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-034">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-034" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0034.svg" class="slide-image" />

            <figcaption>
            <p    >This is the naive Bayes assumption formulaically. We simply factor p(X1,…Xn) into n separate, independent probabilities. That means we can take our estimates for the probability of each feature, and multiply them together to get the probability of the whole instance.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-035" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-035" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0035anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0035anim0.svg,31.ProbabilisticModels1.key-stage-0035anim1.svg,31.ProbabilisticModels1.key-stage-0035anim2.svg,31.ProbabilisticModels1.key-stage-0035anim3.svg" class="slide-image" />

            <figcaption>
            <p    >This gives us a probability for the whole instance space. Now, let's imagine a new email comes in, one which contains the words <em>pill</em> and <em>meeting</em>. What class do we think it is? <br></p><p    >The probability of it being ham is proportional to the probability of seeing a ham email with these characteristics times the probability of seeing a ham email at all. The first factor breaks up by the naive Bayes assumption, and we can simply fill in our three probability estimates. We do the same thing for spam and report wich class gets the high probability <br></p><aside    >Note that we are only computing the numerator of Bayes' rule. This is enough to work out which class gets the higher probability.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-036" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-036" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0036anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0036anim0.svg,31.ProbabilisticModels1.key-stage-0036anim1.svg,31.ProbabilisticModels1.key-stage-0036anim2.svg,31.ProbabilisticModels1.key-stage-0036anim3.svg" class="slide-image" />

            <figcaption>
            <p    >If we work out the probability of spam in the same way, we see that the Naive Bayes classifier assigns the class ham the most probability. If we want proper class probabilities all we have to do is normalize these values (that is, divide by (5/33) + (3/55)).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-037">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-037" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0037.svg" class="slide-image" />

            <figcaption>
            <p    >While naive Bayes can work surprisingly well with these estimators, we do run into a problem if for some feature a particular value does not occur. In that case, we estimate the probability as 0.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-038">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-038" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0038.svg" class="slide-image" />

            <figcaption>
            <p    >Since the whole estimate of our probability is just a long product, if one of the factors becomes zero, <strong>the whole thing collapses</strong>. Even if all the other features gave this class a very high probability, that information is lost.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-039">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-039" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >To remedy this, we need to apply <strong>smoothing</strong>. The simplest way to do that is to add <strong>pseudo-observations</strong>. For each possible value, we add one instance where all the features have that value. This may seem like we're ruining our data with fake examples, but if we have a large dataset the impact should be minimal (and we'll see a way to minimize the impact even further later).<br></p><p    >(We should do the same for the class <span>ham</span>).<br></p><aside    >If we have features with different sets of values (like gender and country of origin), we can no longer add the pseudo-observations so neatly to the dataset. In that case, we just adjust the estimators for p(Gender | C) and p(Country | C) as shown in the next slide.<br></aside><aside    >We can do this because of the conditional independence: the estimators for feature 1 don’t look at the data of feature 2, so we can actually add pseudo-observations to one feature but not to the other.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-040" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-040" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0040anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0040anim0.svg,31.ProbabilisticModels1.key-stage-0040anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This changes our estimates as shown here. In practice, we don’t actually need to add the pseudo-observations literally, we just change our estimator.<br></p><p    >Here, v is the number of different values X<sub>1</sub> can take. Note that we have to change the denominator as well as the numerator, or the probabilities will sum to more than 1 over all values of the feature.<br></p><p    >If we are worried about the impact of the pseudo-observations, we can reduce the<em> weight</em> they have among the observations. For all other observations we assume that the weight is 1. By replacing 1 for the pseudo-observations with <span class="blue">λ</span>, and setting this to a low value like 0.01, we get the <span class="blue">λ</span>-smoothed<span class="blue"> </span>estimator shown. This makes the impact of the pseudo-observations very small, but it still ensures that we will never see a zero.<br></p><aside    >If you do a Bayesian analysis, you can derive exactly this estimator by setting a particular prior. In fact, many common priors can be framed as pseudo-obervations. We won't dig into this in the course, but it's pretty neat.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-041">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-041" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0041.svg" class="slide-image" />

            <figcaption>
            <p    >Naive Bayes is commonly associated with categorical features (to which Bernoulli or Categorical distributions are fitted), but it can also be used with numerical features. If we use normal distributions, then the independence assumption means that we fit a univariate normal distribution to each feature independently. The distribution over the whole space for each class then becomes a multivariate normal whose covariance matrix is diagonal (all off-diagonal elements are zero). <br></p><p    >Visually, this means that the distribution looks like an ellipsoid that is stretched along the axes. Put more technically, its<em> major axis</em> is not horizontal or vertical.<br></p><p    >The kind of ellipse shown on the bottom, which is stretched in an arbitrary direction <em>is</em> a multivariate normal distribution, but not one where the features are independent. So this kind of fit would only be allowed in a non-naive Bayes classifier. <br></p><aside    >Note that non-naive Bayes with MVNs requires us to specify a full covariance matrix, so the number of model parameters grows quadratically with the number of features, while the number of parameters for the naive Bayes classifier only grows linearly, since we need just one scalar variance per dimension.<br></aside><p    >image source: <a href="http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes"><strong class="blue">http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes</strong></a></p><p    ><a href="http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>





       <section id="slide-042">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-042" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0042.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>



        <section class="video" id="video-042">
            <a class="slide-link" href="https://mlvu.github.io/probability#video-42">link here</a>
           <video controls>
                <source src="https://surfdrive.surf.nl/files/index.php/s/3RGE2wmJ3LXdkPy/download" type="video/mp4" />

                Download the <a href="https://surfdrive.surf.nl/files/index.php/s/3RGE2wmJ3LXdkPy/download">video</a>.
           </video>
        </section>


       <section id="slide-043">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-043" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0043.svg" class="slide-image" />

            <figcaption>
            <p    ><br><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-044">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-044" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0044.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we’ll look at an example of a discriminative classifier: <strong>logistic regression</strong>. This is a classifier that learns to map the features directly to class probabilities, without using Bayes’ rule to reverse the conditional probability. <br></p><p    >This is basically a small extension of the linear classifier we've already seen. You can also think of it as a linear classifier with a specific loss function.<br></p><aside    >The name logistic <span>regression</span> is very confusing, but in the modern view it is a classifier, not a regression model.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-045">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-045" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0045.svg" class="slide-image" />

            <figcaption>
            <p    >Remember that we were still on the lookout for good loss functions for the classification problem. We’ll use the language of probability to define one for us.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-046">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-046" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0046.svg" class="slide-image" />

            <figcaption>
            <p    >This was our last attempt: the <em>least squares loss</em>.<br></p><p    >Our thinking was: the hyperplane classifier checks if <strong>w</strong><sup>T</sup><strong>x </strong>+ <span class="blue">b</span> is positive or negative, to decide whether to assign classes <span class="blue">positive</span> (blue discs) or <span class="red">negative </span>(red diamonds), respectively. Why not just give the classes some arbitrary positive and negative values (-1 and +1), and treat it as a regression problem?</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-047">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-047" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    >Here is another option: instead of assigning the two classes arbitrary values, we assign them <em>probabilities</em>: specifically, <em>the probability of being positive.</em> This is 1 for all points in the <span class="blue">positive</span> class and 0 for all points in the <span class="red">negative</span> class. Compared to the least squares approach, we just assign the <span class="red">negative</span> class points the value 0 instead of -1.<br></p><p    >Does this give us a probabilistic classifier? Can we fit a linear regression line to these points and interpret the output as the probability, p(<span class="blue">pos</span>|x),  that the instance is positive? If we fit a line through these points, it doesn’t look substantially different to the previous slide, because our function <strong>w</strong><sup>T</sup><strong>x </strong>+ <span class="blue">b</span> still ranges from negative infinity to positive infinity. We'd like it to produce values between 0 and 1, so we can always interpret them as probabilities, but it only does that for a very narrow and arbitrary range.<br></p><p    >What we need, is a way to squeeze the whole infinite range of the linear function into the range [0, 1], so that the model will only ever produce valid probabilities.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-048" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-048" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0048anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0048anim0.svg,31.ProbabilisticModels1.key-stage-0048anim1.svg" class="slide-image" />

            <figcaption>
            <p    >For this purpose, we will use the <strong>logistic sigmoid</strong> function shown here. A sigmoid function is a function that makes an s-shape like this: its domain is the entire real number line, its range is between two finite values, 0 and 1 in this case, and it increases monotonically. Informally, it squeezes the whole real number line into a finite interval in a smooth way. The<em> logistic</em> sigmoid shown here is just one of many sigmoid functions.<br></p><aside    >The second definition, in grey, is equal to the first. You can show this easily by multiplying both the numerator and the denominator by e<sup class="red">t</sup> in the first definition.<br></aside><p    >source: By Qef (talk) - Created from scratch with gnuplot, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=4310325"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=4310325</strong></a><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-049">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-049" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0049.svg" class="slide-image" />

            <figcaption>
            <p    >We'll see a lot more of the logistic sigmoid as the course progresses, so make sure to remember it. The reason we like to use this specific sigmoid in machine learning settings is that it has a few nice properties that make analysis easier.<br></p><p    >The first is its <strong>symmetry</strong>: if you flip it upside down, or left to right, you get the same function, which is the sigmoid running in the opposite direction σ(-t). Basically the remainder between σ(t) and 1, is itself a sigmoid. We'll use this property later in this video.<br></p><p    >The second property is that the<strong> derivative</strong> of the sigmoid has a particularly simple form: it's equal to the sigmoid itself times one of these flipped sigmoids.<br></p><aside    >Both of these properties are easy enough to work out from the definition on the previous slide. We'll save you this to keep the lecture simple, but it's a good exercise if you have the time to try. If not, take a minute to burn them into your memory, so you'll be able to follow along later when they pop up.<br></aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-050" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-050" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0050anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0050anim0.svg,31.ProbabilisticModels1.key-stage-0050anim1.svg" class="slide-image" />

            <figcaption>
            <p    >With the sigmoid in hand, we can build our new classifier: we compute the linear function <strong>w</strong><sup>T</sup><strong>x </strong>+ <span class="blue">b</span> as before, but we apply the logistic sigmoid to its output, squeezing it into the interval [0, 1]. This means that we can interpret the output as the probability of the positive class being true, according to our classifier. <br></p><p    >This may be a very accurate probability, or a very inaccurate one, depending on how we choose <strong>w</strong> and <span class="blue">b</span>, but it’s always a value between 0 and 1. Hopefully, if we choose the parameters <strong>w</strong> and <span class="blue">b</span> well, we'll get a probability distribution that assigns high probability to the<span class="blue"> blue</span> discs and low probability to the<span class="red"> red </span>diamonds.<br></p><p    >Now all we need is a<strong> loss function</strong> that tells us how well the probabilities produced by the classifier match what we see in the data.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-051">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-051" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0051.svg" class="slide-image" />

            <figcaption>
            <p    >For this we'll introduce the <strong>log(arithmic) loss</strong>. This is also know as the (binary) cross-entropy loss, for reasons we'll explain in the next video.<br></p><p    >At heart, this is just the maximum likelihood principle at work. We have some data, the class labels, and a model with some parameters, <strong>w</strong> and <span class="blue">b</span>. We are looking for the parameters that maximize the probability of the data. <br></p><p    >We'll call the probability distribution that our classifier produces for x q<sub>x</sub>. This is the probability of the class conditioned on the data, but we'll move the conditional to the subscript to clarify the notation a little.<br></p><aside    >We call it q because it’s a probability distribution, but one that we “build” rather than one that describes the real world. That is, q could be very accurate, or very inaccurate, depending on how we choose <strong>w</strong> and <span class="blue">b</span>.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-052" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-052" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0052anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0052anim0.svg,31.ProbabilisticModels1.key-stage-0052anim1.svg" class="slide-image" />

            <figcaption>
            <p    >We assume that the instances in our data are independent, so that the probability of all class labels is just the probabilities of the individual class labels multiplied together. Since we have a discriminative classifier, we are not modeling the features. We take them as given and directly maximize the probability of the labels given the features.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-053" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-053" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0053anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0053anim0.svg,31.ProbabilisticModels1.key-stage-0053anim1.svg,31.ProbabilisticModels1.key-stage-0053anim2.svg,31.ProbabilisticModels1.key-stage-0053anim3.svg,31.ProbabilisticModels1.key-stage-0053anim4.svg" class="slide-image" />

            <figcaption>
            <p    >Since, as we've seen, the logarithm of the probability is often better behaved, we will maximize the log-probability of the class labels given the features. Since we like to minimize—we are looking for a<em> loss function</em> so lower should be better—we stick a minus in front of the log probability and change the argmax to an argmin.<br></p><p    >Then, the multiplication can be moved out of the logarithm, turning it into a sum. <br></p><p    >Finally, we separate the data into the positive and negative instances. Our loss function says that for the positive points we want to maximize the log probability the classifier assigned to the point being positive and for the negative classes we want to maximize the probability that the classifier assigns to the point being negative. Hopefully, this sounds intuitive so far.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-054">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-054" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >Before we move on, let's try to visualize what we have so far.<br></p><p    >In the least-squares case, the loss function could be thought of in terms of the <em>residuals</em><span> </span>between the prediction and the true values. They pull on the line like rubber bands.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-055">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-055" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0055.svg" class="slide-image" />

            <figcaption>
            <p    >For the logarithmic loss on the logistic classifier, we can imagine the "residuals" as the lines drawn here: the probabilities of the true classes. The logarithmic loss tries to maximize the sum of their logarithm (or minimize their negative logarithm).<br></p><p    >You can think of them as little rods pushing up (for the blue rods) and down (for the red rods) on the sigmoid function to push it towards the relevant instances.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-056">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-056" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0056.svg" class="slide-image" />

            <figcaption>
            <p    >Remember that in the least squares loss we squared the residuals before summing them, to punish outliers. Taking the logarithm has a similar effect. For those instances where the probability is near the value it should be, we are taking the negative logarithm of a value very close to zero. That means that these points, which are far away from the decision boundary, contribute very little to the loss, and the points for which the rods are smaller contribute proportionally much more.<br></p><p    >The next question is how do we minimize this loss? We'll use gradient descent, which means that we need to work out the derivatives with respect to the parameters. <br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-057">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-057" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0057.svg" class="slide-image" />

            <figcaption>
            <p    >The next couple of slides show a (somewhat) complicated derivation. You should do your best to go through this step by step. There are a couple more of these coming up in the course, so if you don't take the time to get used to them, you'll struggle later on. If you do take the time, I promise it gets easier with a little practice.<br></p><p    >You don't, however, have to understand this <em>right away</em>. If you struggle to follow along,<em> just look at the start and end points</em>. Try to figure out what the derivation is trying to show and why this is important. Then, move on to the rest of the lecture and come back for the details later. <br></p><aside    >If you haven't done the second homework exercise yet, it may be better to do that first, and then come back to this part of the video. After that exercise, you should have a more practical understanding of what we're trying to do here.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-058" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-058" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0058anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0058anim0.svg,31.ProbabilisticModels1.key-stage-0058anim1.svg,31.ProbabilisticModels1.key-stage-0058anim2.svg,31.ProbabilisticModels1.key-stage-0058anim3.svg" class="slide-image" />

            <figcaption>
            <p    >What we need is the derivative of the loss with respect to every parameter of the model. We'll work it out for the weights <span>w</span><sub>i</sub> and take the bias <span class="blue">b</span> as read. <br></p><p    >We’ll show you the basics of working out the gradient for logistic regression. The first step is to break the loss apart into separate terms for the positive and negative points. We'll look at the positive term in detail (the negative term can be derived in a similar way).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-059" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-059" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0059anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0059anim0.svg,31.ProbabilisticModels1.key-stage-0059anim1.svg,31.ProbabilisticModels1.key-stage-0059anim2.svg,31.ProbabilisticModels1.key-stage-0059anim3.svg,31.ProbabilisticModels1.key-stage-0059anim4.svg,31.ProbabilisticModels1.key-stage-0059anim5.svg,31.ProbabilisticModels1.key-stage-0059anim6.svg,31.ProbabilisticModels1.key-stage-0059anim7.svg,31.ProbabilisticModels1.key-stage-0059anim8.svg,31.ProbabilisticModels1.key-stage-0059anim9.svg" class="slide-image" />

            <figcaption>
            <p    >To simplify the derivation, we first take the output of the linear part of our model (before it goes into the sigmoid) and call it <span class="red">y</span>. Note that the derivative of <span class="red">y</span> with respect <span>w</span><sub>i</sub> is just x<sub>i</sub>, because the dot product is a simple sum of element-wise multiplications, so the only term that <span>w</span><sub>i</sub> appears in is <span>w</span><sub>i </sub>x<sub>i</sub>.<br></p><p    >With this, we can work out the partial derivative with respect to <span>w</span><sub>i</sub> in a relatively clean and simple manner. We start (line 1) by filling in q<sub>x</sub>(<span class="blue">P</span>), the probability according to our current classifier that the point x is in the <span class="blue">positive</span> class (which it is). This is just the output <span class="red">y</span> of the linear function, passed through the logistic sigmoid σ.<br></p><p    >Next (line 2), we apply the chain rule twice. First to move out of the logarithm, and then to move out of the sigmoid. Note that each denominator is the numerator of the previous factor.<br></p><p    >For each of these three factors, we can work out the derivative (line 3). The derivative of log(x) is 1/x. That is, assuming we are using the natural logarithm. If we want to use a different logarithm (like base-2), then we get a constant multiplier, which we can ignore if we are using gradient descent (because we are scaling the gradient by η anyway). The derivative of the sigmoid w.r.t. to <span class="red">y</span> is the sigmoid times the flipped sigmoid, and the derivative of <span class="red">y</span> wrt to <span>w</span><sub>i</sub> we have already worked out.<br></p><p    >The factor σ(<span class="red">y</span>) appears above and below the division line, so these cancel out (line 4), leaving us with just the flipped sigmoid times x<sub>i</sub>. We note that the flipped sigmoid is one minus the probability of the positive class (according to our classifier). Since there are only two classes, this equals the probability of the negative class q<sub>x</sub>(<span class="red">N</span>). We fill this in, which provides our answer.<br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-060">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-060" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0060.svg" class="slide-image" />

            <figcaption>
            <p    >Despite the complicated business in the middle, the result is actually very simple. This is one of the pleasing properties of the logistic sigmoid, it tends to cancel itself out when the derivative is taken.<br></p><p    >In short, for this particular instance, and weight i, the derivative is the i-th feature times the probability (according to the current parameters) that this instance is negative.<br></p><p    >Consider what this means in a gradient descent setting: this value here is what we want to subtract from the current value of <span>w</span><sub>i</sub> to better fit the classifier to this particular point x.  Imagine that the classifier does badly at the moment: to this<span class="blue"> positive</span> point x, it assigns a large probability for the <span class="red">negative</span> class, so q<sub>x</sub>(<span class="red">N</span>) is large. <br></p><p    >If x<sub>i</sub> is a large positive value, then gradient descent subtracts a large negative number, - q<sub>x</sub>(<span class="red">N</span>)x<sub>i</sub>, from <span>w</span><sub>i</sub>. This makes it bigger, increasing the sum <strong>w</strong><sup>T</sup><strong>x</strong> + <span class="blue">b</span> and increasing the probability σ(<strong>w</strong><sup>T</sup><strong>x</strong> + <span class="blue">b</span>) that the classifier assigns to the <span class="blue">positive</span> class. If x<sub>i</sub> is a large <em class="red">negative</em> number, we go in the opposite direction.<br></p><p    >If, however, the classifier already does well, assigning this positive point a large <span class="blue">positive</span> probability, then q<sub>x</sub>(<span class="red">N</span>) is very close to 0, and this particular instance has very little influence on the gradient descent step (unless the magnitude of x<sub>i</sub> is so big that x<sub>i</sub>q<sub>x</sub>(<span class="red">N</span>) is still a substantial value).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-061">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-061" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0063.svg" class="slide-image" />

            <figcaption>
            <p    >If we work out the derivative for the other term, we get a predictable result: the same form, but with q<sub>x</sub>(<span class="blue">P</span>) instead of q<sub>x</sub>(<span class="red">N</span>) and a minus instead of a plus.<br></p><aside    >If you’re wondering why the sign changes, it’s in the first line, we replace q<sub>x</sub>(<span class="blue">P</span>) by σ(<span class="red">y</span>), but we replace q<sub>x</sub>(<span class="red">N</span>) by 1- σ(<span class="red">y</span>), so the derivation is slightly more complex.<br></aside><p    >So there we have it: the gradient for a linear classifier, fed through a sigmoid function, producing a logarithmic loss.<br></p><aside    >For the bias <span class="blue">b</span>, we get the same result, but without the x<sub>i</sub> factors. The derivation is the same, except that in the second line of the derivation the third factor is 1 instead of x<sub>i</sub>.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-062">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-062" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0064.svg" class="slide-image" />

            <figcaption>
            <p    ><em>Regression</em> is a bit of misnomer, since we’re building a classifier. I suppose the confusing terminology comes from the fact that we’re fitting a (curved) line through the probability values in the data. Just one of the many confusing names in the field of machine learning, I'm afraid.<br></p><p    >Anyway, now that we have a gradient, we can apply gradient descent. Let's see the model in action.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-063">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-063" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0065.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a 2D dataset that shows a common failure case for the least squares classifier. The points at the top are so far away from the ideal decision boundary that they will have huge residuals under the least squares model, and this is not balanced out by a similar cluster of negative points.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-064">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-064" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0066.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what the least-squares regression converges to. Clearly, this is not a satisfying solution for such an easily separable dataset. The blue points at the top are so far from the decision boundary.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-065">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-065" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0067.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a 1D view of a similar situation. The green bar is the decision boundary that we want, but any line that crosses the horizontal axis there has really big residuals for the far away points, or really big residuals for all the other points. These pull on the line with a quadratic strength, so the decision boundary will always be pulled toward them.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-066" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-066" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0068anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0068anim0.svg,31.ProbabilisticModels1.key-stage-0068anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The logistic model doesn’t have this problem. If the model fits well around the ideal decision boundary, it doesn’t have to worry at all about points that are far away (if they’re on the right side of the boundary). The log loss for these points is very close to -log(1), so very close to 0.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-067">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-067" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0069.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what the logistic regression chooses as a decision boundary. Unlike the least squares regression, the points are perfectly separated.<br></p><p    >Another thing to note is that while we added some non-linearity to our classifier with the sigmoid function, the <strong>decision boundary</strong> is still linear. This is because the decision boundary is the curve where σ(<strong>w</strong><sup>T</sup><strong>x</strong> + b) = 0.5. The input to the sigmoid that results in an output of 0.5 is 0.<br></p><p    >In other words, we previously put the decision boundary at <strong>w</strong><sup>T</sup><strong>x</strong> + b = 0 and we are still doing the same thing here. What changed was the loss function.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-068">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-068" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0070.svg" class="slide-image" />

            <figcaption>
            <p    >We can also plot the probability function using a color map (blue is high probability of <span class="blue">positive</span>, red is high probability of <span class="red">negative</span>). The white band in the middle is where the probability of positive is near 0.5. That is, in this region, the classifier is <em>uncertain</em>. <br></p><p    >Uncertainty in machine learning is a difficult problem, and models like these that that can express their certainty about a classification are usually much more certain than they should be, so be sure to take this with a grain of salt. Still, it's nice that the model can at least <em>express</em> its uncertainty, even if it may not be doing so accurately.<br></p><aside    >This plot shows where the non-linearity came in: the probability density function is nonlinear. It looks like the 1D sigmoid function extended in some direction to cover the whole feature space. The place where it’s equal to 0.5 the decision boundary, still makes a line, or in higher dimensions, a hyperplane.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-069">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-069" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0071.svg" class="slide-image" />

            <figcaption>
            <p    >Note that for such well-separable classes, there are many suitable decision boundaries, and logistic regression has little reason to prefer one over the other (all points are assigned the correct probability very close to 1). We’ll see a solution to this problem next lecture, when we meet our final loss function: the maximum margin loss.<br></p><aside    >If we want to stick with logistic regression we can solve this problem to some extent by widening the "region of uncertainty" as much as possible, without sacrificing too much of the log loss. One way to achieve this is by adding L2 regularization, which we will learn about in a later lecture.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-070">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-070" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0072.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>



        <section class="video" id="video-070">
            <a class="slide-link" href="https://mlvu.github.io/probability#video-70">link here</a>
           <video controls>
                <source src="https://surfdrive.surf.nl/files/index.php/s/b7EKqDsMkGt3SuW/download" type="video/mp4" />

                Download the <a href="https://surfdrive.surf.nl/files/index.php/s/b7EKqDsMkGt3SuW/download">video</a>.
           </video>
        </section>


       <section id="slide-071">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-071" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0073.svg" class="slide-image" />

            <figcaption>
            <p    >The last video was all about defining a probability p(x) and then taking the negative logarithm of that probability. We justified this by saying that the logarithm of the likelihood is easier to work with, and that as a convention we tend to minimize rather than maximize in machine learning  so we took the negative of the log likelihood. All very pragmatic.<br></p><p    >But actually, there is a very concrete meaning to the negative log likelihood of a probability, that can really help to deepen our understanding of what we are doing when we use probabilities in machine learning. To understand this, we need to dig briefly into the topic of <strong>information theory</strong>. This will not just help us understand probability from a new perspective, it will also provide us with the concept of <strong>entropy</strong>, which is an important tool we will use at different points in the course.<br></p><p    ><br><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-072">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-072" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0074.svg" class="slide-image" />

            <figcaption>
            <p    >Imagine you’re on holiday, and you’ve brought your travel monopoly. Unfortunately, the dice have gone missing. You do, however, have a coin with you. Can you use a coin flip to simulate the throw of a six sided  die?<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-073">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-073" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    >For a four sided die, the solution is easy. We flip the coin twice, and assign a number to each possible outcome.<br></p><p    >source: <a href="http://www.midlamminiatures.co.uk/blackpolydice/D4Black.html"><strong class="blue">http://www.midlamminiatures.co.uk/blackpolydice/D4Black.html</strong></a></p><p    ><a href="http://www.midlamminiatures.co.uk/blackpolydice/D4Black.html"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>





       <section id="slide-074">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-074" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0076.svg" class="slide-image" />

            <figcaption>
            <p    >A six sided die is more tricky. We’ll show the solution for three “sides”. You can just add another coin flip to decide whether to interpret the result as picking between 1,2 and 3 or as picking between 4, 5 and 6.<br></p><p    >The trick is to assign the fourth outcome to a “reset”. If you throw two tails in a row, you just start again. Theoretically you could be coin flipping forever, but the probability of resetting more than five times is already less than one in one-thousand.<br></p><p    >With these kind of resets, it turns out that you can model any probability distribution you like. This will allow you to play your monopoly game.<br></p><p    >The downside is that you have to assign one outcome to multiple leaves in your tree. What if we restrict ourselves to trees where each leaf has a distinct outcome? In that case, we can't model the six-sided die perfectly with coin flips. What distributions can we still model?</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-075">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-075" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0077.svg" class="slide-image" />

            <figcaption>
            <p    >Here are two distributions on the natural numbers that we can model this way. One with an exponentially decaying tail, and one with a fatter tail. <br></p><p    >Note that both trees are infinite in size. This we don't mind. The only constraint we care about is that each leaf node has a unique label.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-076">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-076" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0078.svg" class="slide-image" />

            <figcaption>
            <p    >In probability distributions expressed like this, it's really simple to see the relation between probabilities and <strong>codes</strong>. Functions that assign a binary string to each of our outcomes.<br></p><p    >We simply replace the <span class="red">heads</span> and <span>tails</span> by <span class="red">zeros</span> and <span>ones </span>and describe each outcome by the sequence of steps required to get from the root of the tree to that particular outcome.<br></p><p    >Codes are used to transmit information. If we roll a die and we want to tell somebody that we rolled a 3, we can send them the code <span>1</span><span class="red">0</span>.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-077" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-077" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0079anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0079anim0.svg,31.ProbabilisticModels1.key-stage-0079anim1.svg" class="slide-image" />

            <figcaption>
            <p    >These kinds of trees are called<strong> prefix-free trees</strong>, and the resulting codes <strong>prefix-free codes</strong>. The name comes from the fact that no codeword will be the prefix of any other code word. That is, the first bits of one code will never be a codeword by themselves.<br></p><p    >The nice thing about prefix free codes is that if we want to encode a sequence of these outcomes, we can just stick the codes one after another and we won’t need any delimiters. A decoder that has access to the tree will know exactly where each codeword ends and the next begins.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-078" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-078" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0080anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0080anim0.svg,31.ProbabilisticModels1.key-stage-0080anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Another, more relevant, nice property is that there is a direct relation between the length of the code we assign an outcome, and its probability: <strong>the more coinflips we require to get to a particular outcome, the lower the probability that we will get there, and the longer the code. </strong>Low probability outcomes get long codes and high probability outcomes get short codes.<strong><br></strong></p><p    >In this tree here, if we generate outcomes by flipping coins randomly, the probability of getting <span class="blue">a</span> is the probability of flipping <span>heads</span> twice in a row: 1/4. The probability of getting <span>b</span> is the probability of flipping<span> heads</span>, then <span class="red">tails</span>, then <span>heads</span>: 1/8. <br></p><p    >This is expressed in the lengths of the codes for <span class="blue">a</span> and <span>b</span>. <span>b</span> has a longer codelength and is therefore less likely.<br></p><p    >If the probabilities from this tree match the probabilities with which we expect to see the outcomes, then this is a very nice property for a code to have: when frequent outcomes have short codes, we end up with shorter messages overall.<br></p><p    >This was realized as early as the invention of Morse code. Samuel Morse explicitly assigned short codewords to letters like e and t, because he knew that they would occur frequently, so that the telegraph messages would be shorter.<br></p><aside    >Information theory didn't exist yet, so his codelengths were a little ad-hoc. He also didn't know about prefix-free codes, so Morse code does have a delimiter symbol.<strong><br></strong></aside><p    ><strong><br></strong></p><p    ><strong></strong></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-079" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-079" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0081anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0081anim0.svg,31.ProbabilisticModels1.key-stage-0081anim1.svg,31.ProbabilisticModels1.key-stage-0081anim2.svg,31.ProbabilisticModels1.key-stage-0081anim3.svg" class="slide-image" />

            <figcaption>
            <p    >Let's make all this a little more precise. Let's start with an arbitrary tree, and assume that we sample from it by flipping a coin to decide our path from the root to the leaves. What probability distribution does this define? This is very simple: each coinflip multiplies the probability by 1/2, so if the length of the code for outcome <span>b</span> is 3, then the outcome <span>b</span> has probability (1/2)<sup>3</sup> = 1/8.<br></p><p    >In general the probability for an outcome x with a code of length L(x) is p(x) = 2<sup>-L(x)</sup>.<br></p><p    >With this equation in place, we can reverse the question. If we are given a probability distribution p(x), and we are assured that there is some prefix-free tree corresponding to it, what can we say about the codelengths that this probability tree describes? Rewriting the equation to isolate L(x), we get L(x) = -log<sub>2</sub>p(x)<br></p><p    >There it is! The negative logarithm of a probability. If we have a probability distribution that can be expressed by a prefix-free tree, the negative logarithm of its probabilities has a very concrete meaning: <strong>it's the codelengths of the outcomes under the corresponding codes</strong>.<br></p><aside    >The base 2 of the logarithm is a consequence of using bits to encode our data. If we used trits (0, 1, 2) we'd get a base-3 logarithm and if we used digits, we'd get a base-10 logarithm. You can even go the other way around and start with the natural logarithm, which will give you a unit for amount of information called "nats". These are a little more abstract; I can't imagine what a codeword written in nats looks like, but it still works to quantify the amount of information in the outcome of a sample from a probability distribution.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-080">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-080" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0082.svg" class="slide-image" />

            <figcaption>
            <p    >The only drawback with this view is that we are restricted to probability distributions that we can model as prefix-free codes with unique labels on the leaves. If we investigate closer, it turns out that this is not as much of a restriction as we may fear. We can show that for any probability distribution L we can find a prefix-free code so that the value -log p(x) and the code-length L(x) differ by no more than one bit for any outcome x.<br></p><p    >If we handwave this small difference, we can<strong> equate codes with probability distributions</strong>: every code gives us a distribution and every distribution gives us a code. And all of these codes have the nice property that the higher the probability of an outcome is, the shorter its codelength.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-081" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-081" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0083anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0083anim0.svg,31.ProbabilisticModels1.key-stage-0083anim1.svg,31.ProbabilisticModels1.key-stage-0083anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We already noted that this is a nice property for a code to have, because it reduces the amount of bits we can expect to use. How much does it reduce it? If we know the things we are going to encode come from distribution x, then can we say something about whether using the corresponding code is in some sense the optimal choice?<br></p><p    >The simplest way to answer this question is to compute<strong> the expected number of bits we will have to use per outcome</strong>. This is simply the codelength of each outcome, multiplied by its probability, summed over all outcomes. This quantity is called the <strong>entropy</strong>. <br></p><p    >The entropy of a distribution is the expected codelength of an element sampled from that distribution.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-082" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-082" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0084anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0084anim0.svg,31.ProbabilisticModels1.key-stage-0084anim1.svg,31.ProbabilisticModels1.key-stage-0084anim2.svg,31.ProbabilisticModels1.key-stage-0084anim3.svg" class="slide-image" />

            <figcaption>
            <p    >The entropy of a distribution is a very commonly used function, because it expresses in a single number how much<strong> uncertainty </strong>we have over the outcome. Or in other words, how uniformly spread out the probability mass is among the outcomes.<br></p><p    >The more uniform our distribution is, the less we know about what will happen, and the higher the entropy. <br></p><p    >On the left we see<span class="red"> a perfectly uniform distribution</span>. Each outcome has equal probability 1/4, so each outcome gets a 2-bit codewords, and the expected codelength is 2.<br></p><p    >In <span class="blue">the middle</span>, we know something more about our distribution, for instance that <span>a</span> is very likely, so we can make the codeword for "a" a little shorter, reducing the expected codelength to 1.75 bits. <br></p><p    >On the right, we see the extreme case of<span> perfect knowledge</span>. We are certain that outcome "a" will happen every time. We can label the root of our tree with "a". This is like having a single "empty" codeword with a length of 0 bits. More practically, if I had to sample an outcome from this distribution and send you a message saying what had happened, the best option would be no message at all: we both know the distribution, so I don't need to tell you what happened.<br></p><p    >This last example requires the assumption that we assume 0 · log(0) = 0. This is not always true, but it’s an assumption we make when we compute entropies, since it leads to the most intuitive results.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-083" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-083" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0085anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0085anim0.svg,31.ProbabilisticModels1.key-stage-0085anim1.svg" class="slide-image" />

            <figcaption>
            <p    >What if we don’t use the code that corresponds to the source of our data <span class="red">p</span> to encode our data, but some other code based on distribution <span class="blue">q</span>. What is our expected codelength then? This is called the<em> </em><strong>cross entropy</strong>.<br></p><p    >It can be shown that the cross entropy is minimal when <span class="red">p</span>=<span class="blue">q</span>. That is, when the cross entropy corresponds to the entropy.<br></p><p    >We can conclude two things:<br></p><p     class="list-item">The code corresponding to<span class="red"> p</span> provides the best expected codelength out of all possible prefix-free codes.<br></p><p     class="list-item">The cross entropy is a good way to <strong>quantify the distance between two distributions</strong> (because it’s minimal when the two are the same).<br></p><aside    >The proof that the cross entropy is always bigger than the entropy is too complicated for now. If you’re up for a challenge and you know about Lagrange multipliers (explained in the optional SVM lecture), you can apply these to the problem of minimizing the cross entropy for vector <strong class="blue">q</strong>, subject to the constraints that the elements of <strong class="blue">q</strong> are positive and sum to 1.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-084">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-084" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0086.svg" class="slide-image" />

            <figcaption>
            <p    >The cross-entropy is a nice measure, but it’s not zero when <span class="red">p</span> and <span class="blue">q</span> are equal. Instead, it’s equal to the entropy of <span class="red">p</span>.<br></p><p    >To get a measure that is zero when the two are equal, and larger than zero otherwise, we can just subtract the the entropy of <span class="red">p</span>. This is called the Kullback-Leibler (KL) divergence. The KL divergence between two distributions is zero if and only if they are equal. <br></p><p    >You can think of this a little bit like the "distance" between two distributions, although unlike a distance, it's not symmetric.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-085">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-085" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0087.svg" class="slide-image" />

            <figcaption>
            <p    >For probability distributions on continuous spaces, we can also define entropy, known as the<strong> differential entropy</strong>, and KL divergence. We lose the interpretation of prefix-free codes, and there are some technical hurdles here, but the long and short of it is that we replace the summation by an integration.<br></p><p    >To avoid this complexity, in the rest of the course we will often write the entropy and the KL divergence using the expectation notation. This automatically implies that we are summing for discrete sample spaces and integrating for continuous ones, and if we know the basic properties of the expectation (see homework 1), then we'll never need to open the expectation operator up anyway.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-086" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-086" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0088anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0088anim0.svg,31.ProbabilisticModels1.key-stage-0088anim1.svg,31.ProbabilisticModels1.key-stage-0088anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Now that we have our interpretation of -log(x) as a codelength, let's see what it says about the places where we've used it. <br></p><p    >One such place was the log loss. One interpretation we now have is that if we minmize -q<sub>x</sub>(<span class="blue">P</span>) in logistic regression, we are minimizing the amount of bits we would need to transmit to communicate that x is of the positive class, if we assume that both the sender and receiver have access to the classifier and x, but not to the class label (more about this in a bit).<br></p><p    >Another interpretation comes from the fact that we characterized the cross entropy/KL divergence as the "distance" between two probability distributions. What if we see the labels in the dataset as one probability distribution p (with all probabilities 0 or 1), and the classifier as another distribution q? What happens if we explicitly try to minimize the cross entropy between p and q by changing the parameters of q?<br></p><p    >As you can see, with a little rewriting, we recover the logarithmic loss we already derived. For this reason <strong>log-loss is also known as cross-entropy loss</strong>. This is not just a mathematical curiosity, it can actually be useful. There may be cases, where the data provides class probabilities rather than explicit class labels. In such cases, the cross entropy view tells us exactly what to do, but the log-loss perspective becomes useless.<br></p><aside    >We can also do this with the KL divergence instead of the cross-entropy. In that case, we get a constant term - log p(x), which is independent of the parameters of q. This usually doesn't affect the gradient, but in some cases it does.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-087">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-087" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0089.svg" class="slide-image" />

            <figcaption>
            <p    >Just a little heads up: entropy is an important subject. It may feel a little abstract now, and it's fine if you don't quite get it, but we will see it in use a number of times throughout the course. <br></p><p    >We will practice it in the homework exercises, so you'll get another chance to get comfortable with it.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-088">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-088" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0090.svg" class="slide-image" />

            <figcaption>
            <p    >We'll finish up with a brief look at the field that aims to apply this coding perspective to problems of learning more rigorously. The family of methods based on the principle of <strong>Minimum Description Length</strong>.<br></p><p    >The idea is very simple: compression is similar to learning. We look at some data and try to isolate recurring patterns in the data. Using the ideas of coding and entropy, we can make this idea rigorous.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-089">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-089" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0091.svg" class="slide-image" />

            <figcaption>
            <p    >The simplest way to think of MDL is in a <strong>sender and receiver framework</strong>. The sender is going to see some data, and is going to send it to the receiver. Before observing the data, the sender and receiver are allowed to come up with any scheme they like. But afterwards, the data must be sent using the scheme, and in a way that is perfectly decodable by the receiver without further communication. <br></p><p    >One way this is often done is called <strong>two-part coding</strong>:<strong> <br></strong></p><p     class="list-item">The sender and receiver agree beforehand on a family of models (for example the normal distributions, as indexed by parameters <span>μ</span> and <span class="blue">σ</span>)<br></p><p     class="list-item">Then, once the sender has seen the data, she picks a model best suited to the data, and sends this choice of model to the receiver (fopr instance by sending the <span>μ</span> and <span class="blue">σ </span>for the chosen model). <br></p><p     class="list-item">Next, the sender uses the model to encode the data and sends it over<br></p><p     class="list-item">The receiver unpacks the model and then uses the model to decode the data.<br></p><p    >This allows us to frame the problem of model selection using the MDL principle. The best choice of model is the one that minimizes the size of the total package: <span class="blue">the cost of communicating the model</span> plus <span>the cost of communicating the data given the model</span>. If the model is very good at compressing the data, then it might be a very good choice, unless the model is so complex that the cost of sending the model over negates the gains made on communicating the data.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-090" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-090" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0092anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0092anim0.svg,31.ProbabilisticModels1.key-stage-0092anim1.svg,31.ProbabilisticModels1.key-stage-0092anim2.svg,31.ProbabilisticModels1.key-stage-0092anim3.svg,31.ProbabilisticModels1.key-stage-0092anim4.svg" class="slide-image" />

            <figcaption>
            <p    >This idea is often used to solve the problem of over- and underfitting. Without going into the technical details, here is the basic principle of two-part coding applied to a regression problem. <br></p><p    >In a regression (or classification) problems, we take the instances and their features as fixed: both the sender and receiver have access to them. The data that we want to send over the wire is the <em>target labels</em>; in this case the regression targets. How you encode a continuous value is a technical matter that requires some assumptions. For now we can just discretize the range of outputs, and assume that we are using a code that means that <strong>bigger numbers cost more bits</strong>. The same goes for the parameters of the model: these are also continuous values, but we’ll discretize them somehow. Here we only need to assume that using <strong>more parameters in your model takes more bits</strong>.<br></p><p    >Once we’ve chosen a model we can reconstruct the data by sending the <span class="blue">model parameters</span> and the <span>residual values</span>. We see that if we pick a linear model we have many large residuals to transmit. On the other hand, our model is described by only two parameters, so we can transmit that part very cheaply. If we make our model a parabola, we require three numbers to transmit it, so that part of  our message gets bigger, but because the model fits so much better, the residuals are much smaller, and the overall length of our message gets much smaller.<br></p><p    >If we make our model a 15-th order polynomial, we get a slightly tighter fit, but not by much, and the price we pay in storing the 16 numbers required to describe our model means that our total message length is bigger than for the parabola. So overall we prefer the model in  the middle, according to the minimum description length principle. </p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-091" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-091" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0093anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0093anim0.svg,31.ProbabilisticModels1.key-stage-0093anim1.svg,31.ProbabilisticModels1.key-stage-0093anim2.svg,31.ProbabilisticModels1.key-stage-0093anim3.svg,31.ProbabilisticModels1.key-stage-0093anim4.svg,31.ProbabilisticModels1.key-stage-0093anim5.svg" class="slide-image" />

            <figcaption>
            <p    >There are many correspondences between using MDL and using Bayesian methods. In fact they are often different perspectives on the same thing.<br></p><p    >Here is one example. Let's say we are picking a single model <span class="red">M</span> that maximizes the posterior probability  of the data (this requires us to maximize only the numerator of Bayes rule, since the denominator is constant).<br></p><aside    >A full Bayesian analysis would compute the entire posterior distribution, but sometimes we are only interested in its maximum.<br></aside><p    >As we've seen before, we can stick a logarithm in front of any probability without changing the maximum, and we can add a minus to change the maximum into a minimum.<br></p><p    >Then, using the basic properties of the logarithm, we find that we are minimizing the sum of two code-lengths: the cost of describing the model, and the cost of describing the data once the model is known. This is exactly what we do in two-part coding.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-092">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-092" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0094.svg" class="slide-image" />

            <figcaption>
            <p    >When we talked about the problem of induction and the no free lunch theorem, we noted that <em>some assumption</em> about the source of our data was always necessary to make learning possible at all. Some aspects of our problem we need to assume before we start learning.<br></p><p    >You can think of MDL as <strong>encoding a simplicity assumption</strong>. We prefer simple solutions over complex ones, <strong>and we define a simple solution as one that compresses the data well</strong>. The assumption we make about the universe, is that it generates compressible data for us. Or, more precisely, that the compressible aspects of the data that we see are likely to carry over to the test set, and that the incompressible aspects of the data are likely random noise.<br></p><p    >The nice thing about MDL is that it tells us how to trade off the desire to fit the data well with the desire for a simple solution.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-093">
            <a class="slide-link" href="https://mlvu.github.io/probability#slide-093" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0095.svg" class="slide-image" />

            <figcaption>
            <p    >source: <a href="https://xkcd.com/1236/"><strong class="blue">https://xkcd.com/1236/</strong></a></p><p    ><a href="https://xkcd.com/1236/"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


</article>
