---
title: "Lecture 2: Linear Models and Search"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 2: Linear Models and Search</li>
            <li><a href="#video-000">Linear regression</a></li>
            <li><a href="#video-019">Searching for a Good Model</a></li>
            <li><a href="#video-046">Gradient descent</a></li>
            <li><a href="#video-075">Gradient Descent and Classification</a></li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/12.LinearModels1.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">
       <section class="video" id="video-000">
           <a class="slide-link" href="mlvu.github.io/lecture02#video-0">link here</a>
           <iframe
                src="https://www.youtube.com/embed/YGBZE6RA7aU?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-001">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-001">link here</a>
            <img src="12.Linear1.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-002">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-002">link here</a>
            <img src="12.Linear1.key-stage-0002.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the "basic recipe" for machine learning we saw in the last lecture. In this lecture, we’ll have a look at <strong>linear models</strong>, both for regression and classification. We’ll see how to define a linear model, how to formulate a loss function and how to search for a model that minimises that loss function.<br></p><p    >Most of the lecture will be focused on <em>search methods</em>. The linear models themselves aren’t that strong, but because they’re pretty simple, we can use them to explain various search methods that we can also apply to more complex models as the course progresses. Specifically, the method of <strong>gradient descent</strong>, which we'll introduce here, will be the search method used for almost all approaches we will discuss.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-002" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-003">link here</a>
            <img src="12.Linear1.key-stage-0003anim0.svg" data-images="12.Linear1.key-stage-0003anim0.svg,12.Linear1.key-stage-0003anim1.svg,12.Linear1.key-stage-0003anim2.svg,12.Linear1.key-stage-0003anim3.svg,12.Linear1.key-stage-0003anim4.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll start with <strong>regression</strong>. Here’s how we explained regression in the last lecture.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-004">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-004">link here</a>
            <img src="12.Linear1.key-stage-0004.png" class="slide-image" />

            <figcaption>
            <p    >data source: ANSUR II<br></p><p    >image source: MEASURER’S HANDBOOK: US ARMY AND MARINE CORPS ANTHROPOMETRIC SURVEYS, 2010-2011 <br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-004" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-005">link here</a>
            <img src="12.Linear1.key-stage-0005anim0.svg" data-images="12.Linear1.key-stage-0005anim0.svg,12.Linear1.key-stage-0005anim1.svg" class="slide-image" />

            <figcaption>
            <p    >And here’s the example we gave, of regression with a single feature (predicting the length of somebody’s legs given their height).<br></p><p    >The linear regression model is simply a linear function that maps the feature(s) to the target value. In the case of one feature, such a function looks like a line. The only decision we have to make is <em>which line fits the data best</em>.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-006">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-006">link here</a>
            <img src="12.Linear1.key-stage-0006.svg" class="slide-image" />

            <figcaption>
            <p    >To simplify things we'll  use this very simple data set. There is one input feature <strong>x</strong>, one output value <strong>t</strong> (for target) and we have six instances.<br></p><p    >We will assume that all our features are <em>numeric</em> for the time being. We will develop linear regression for an arbitrary number of features m, but we will keep visualizing what we’re doing on this one-feature dataset.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-006" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-007">link here</a>
            <img src="12.Linear1.key-stage-0007anim0.svg" data-images="12.Linear1.key-stage-0007anim0.svg,12.Linear1.key-stage-0007anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Throughout the course, we will use the following notation: lowercase non-bold for scalars, lowercase <strong>bold</strong> for vectors and uppercase bold for matrices.<br></p><p    >When we’re indexing <em>individual elements</em> of vectors and matrices, these are scalars, so they are non-bold.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-007" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-008">link here</a>
            <img src="12.Linear1.key-stage-0008anim0.svg" data-images="12.Linear1.key-stage-0008anim0.svg,12.Linear1.key-stage-0008anim1.svg,12.Linear1.key-stage-0008anim2.svg,12.Linear1.key-stage-0008anim3.svg" class="slide-image" />

            <figcaption>
            <p    >As we saw in the last lecture, an instance in machine learning is described by m <em>features</em> (with m fixed for a given dataset). We will represent this as a <strong>vector</strong> for each instance, with each element of the vector representing a feature. <br></p><p    >This can be a little confusing, since we sometimes want to index the instance within the dataset and sometimes the features of a given instance. Pay attention to whether the letter we’re indexing is bold or non-bold: a bold letter <strong>x</strong> with a subscript i refers to the i-th instance in the data (containinig all features). A non-bold letter x with an index i refers to the i-th scalar feature of some instance <strong>x</strong>.<br></p><p    >In the rare cases where we need to refer to both the index of the instance, and the index of the feature, we will usually use an uppercase X. This makes sense if you imagine the data as a big matrix <strong>X</strong>, with the instances  as rows, and the features as columns.<br></p><p    >We’ll occasionally deviate from this notation when doing so makes things clearer, but we’ll point it out when that happens.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-008" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-009">link here</a>
            <img src="12.Linear1.key-stage-0009anim0.svg" data-images="12.Linear1.key-stage-0009anim0.svg,12.Linear1.key-stage-0009anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If we have one feature (as in this example) a standard linear regression model has two <em>parameters </em>(the numbers that determine which line we fit through our data): <span class="orange red">w</span> the <strong>weight</strong> and <span class="blue">b</span><strong>, </strong>the <strong>bias</strong>. The bias is also sometimes called the <em>intercept</em>.<br></p><p    ><span class="blue">b</span> determines where the line crosses the vertical axis (or what value f takes when x = 0).<br></p><p    ><span class="orange red">w</span> determines how much the line rises if we move one step to the right (i.e. increase x by 1)<br></p><p    >For the line drawn here, we have <span class="blue">b</span>=3 and <span class="orange red">w</span>=0.5. <br></p><p    >Note that this isn’t a very good fit for the data. Our job is to find better numbers <span>w</span> and <span class="blue">b</span>.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-010">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-010">link here</a>
            <img src="12.Linear1.key-stage-0010.svg" class="slide-image" />

            <figcaption>
            <p    >If we have two features, each feature gets its own <strong>weight</strong> (also known as a<em> coefficient</em>)</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-011">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-011">link here</a>
            <img src="12.Linear1.key-stage-0011.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s what that looks like. The thick orange lines together indicate a plane (which rises in the x<sup>2</sup> direction, and declines in the x<sup>1</sup> direction). The parameter<strong> </strong><span class="blue">b</span> describes how high above the origin this plane lies (what the value of f is if <em>both features</em> are 0). The value <span>w</span><sup>1</sup> indicates how much f increases if we take a step of 1 along the x<sup>1</sup> axis, and the value <span class="green">w</span><sup class="green">2</sup> indicates how much f increases if we take a step of size 1 along the x<sup>2</sup> axis. </p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-011" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-012">link here</a>
            <img src="12.Linear1.key-stage-0012anim0.svg" data-images="12.Linear1.key-stage-0012anim0.svg,12.Linear1.key-stage-0012anim1.svg" class="slide-image" />

            <figcaption>
            <p    >For an arbitrary number of features, the pattern continues as you’d expect. We summarize the <span class="orange red">w</span>’s in a vector <strong>w</strong> with the same number of elements as <strong>x</strong>.<br></p><p    >We call the <span>w</span>’s the <span>weights</span>, and <span class="blue">b</span> the <span class="blue">bias</span>. The weights and the bias are the <em>parameters </em>of the model. We need to choose these to fit the model to our data.<br></p><p    >The operation of multiplying elements of <strong>w</strong> by the corresponding elements of <strong>x</strong> and summing them is the <strong>dot product</strong> of <strong>w</strong> and <strong>x</strong>.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-012" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-013">link here</a>
            <img src="12.Linear1.key-stage-0013anim0.svg" data-images="12.Linear1.key-stage-0013anim0.svg,12.Linear1.key-stage-0013anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The <strong>dot product</strong> of two vectors is simply the sum of the products of their elements. If we place the features into a vector and the weights, then a linear function is simply their dot product (plus the <span class="blue">b</span> parameter).<br></p><p    >The transpose (superscript T) notation arises from the fact that if we make one vector a row vector and one a column vector, and matrix-multiply them, the result is the dot product (try it).<br></p><p    >The dot product also has a geometric interpretation: the dot product is equal to the lengths of the two vectors, multiplied by the cosine of the angle between them. <br></p><p    >The dot product will come back a lot in the rest of the course. We don't have time to discuss it in depth, but if your memory is hazy, we strongly recommend that you take a minute to go back to your linear algebra book and look up the various interpretations of what the dot product means.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-014">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-014">link here</a>
            <img src="12.Linear1.key-stage-0014.svg" class="slide-image" />

            <figcaption>
            <p    >To build some intuition for the meaning of the weights <strong>w</strong>, let’s look at an example. Imagine we are trying to predict the risk of high blood pressure based on these three features. We’ll assume that the features are expressed in some number that measures these properties.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-015">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-015">link here</a>
            <img src="12.Linear1.key-stage-0015.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s what the dot product expresses. For some features, like job stress, we want to learn a positive weight (since more job stress should contribute to higher risk of high blood pressure). For others, we want to learn a negative weight (the healthier your diet, the lower your risk of high blood pressure). Finally, we can control the <em>magnitude </em>of the weights to control their relative importance: if age and job stress both contribute positively, but age is the bigger risk factor, we make both weights positive, but we make the weight for age bigger.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-016">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-016">link here</a>
            <img src="12.Linear1.key-stage-0016.svg" class="slide-image" />

            <figcaption>
            <p    >So, that's our model defined in detail. But we still don't know which model to choose for a given dataset. Given some data, which values should we choose for the parameters <strong class="orange red">w</strong> and <span class="blue">b</span>?<br></p><p    >In order to answer this question, we need two ingredients. First, we need a<strong> loss function</strong>, which tells us how well a particular choice of model does (for the given data) and second, we need a way to <strong>search</strong> the space of all models for a particular model that results in a low loss (a model for which the loss function returns a low value).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-016" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-017">link here</a>
            <img src="12.Linear1.key-stage-0017anim0.svg" data-images="12.Linear1.key-stage-0017anim0.svg,12.Linear1.key-stage-0017anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a common loss function for regression: the <strong>mean-squared error</strong> (MSE) loss. We saw this briefly already in the previous lecture.<br></p><p    >Note that the loss function takes a <em>model</em> as its argument. The model maps the data to the output, the loss function maps a model to a loss value. The data functions as a constant in the loss function.<br></p><p    >The main thing a regression loss should do is to compare the model predictions to the actual values in our dataset, and return a large value if they are all very different, and a small value if they are all very close together. The difference between the prediction and the actual value is called the <strong>residual</strong>. We've drawn these here as green bars.<br></p><p    >The MSE loss takes the residual for each instance in our data, squares them, and returns the average. One reason for the squaring step is to ensure that negative and positive residuals don’t cancel out (giving us a small loss even though we have big residuals). But that's not the only reason.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-018">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-018">link here</a>
            <img src="12.Linear1.key-stage-0018.svg" class="slide-image" />

            <figcaption>
            <p    >The squares also ensure that big errors affect the loss more heavily than small errors. You can visualise this as shown here: the mean squared error is the mean of the areas of the green squares (it’s also called <em>sum-of-squares loss</em>).<br></p><p    >When we search for a well-fitting model, the search will try to reduce the big squares much more than the small squares.<br></p><p    >If we think of the residuals as rubber bands, pulling on the regression line to pull it closer to the points, the rubber band on the bottom left pulls much harder than all the other ones. Therefore, any search algorithm trying to minimize this loss will be much more interested in moving the left of the line down than in moving the right of the line up.<br></p><p    >It's not guaranteed that this is a good thing. Sometimes this behavior is desirable and sometimes it isn't. For now, this is just a simple loss function to get started.<br></p><p    >In later lectures, we will say more about when this kind of loss is appropriate and when it isn't. We will also see that this loss function follows from the assumption  that our data contains noise coming from a <em>normal distribution</em>.<br></p><p    >Visualization stolen from <a href="https://machinelearningflashcards.com/"><strong class="blue">https://machinelearningflashcards.com/</strong></a><br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-019">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-019">link here</a>
            <img src="12.Linear1.key-stage-0019.svg" class="slide-image" />

            <figcaption>
            <p    >You may see slightly different versions of the MSE loss: sometimes we take the average of the squares, sometimes just the sum. Sometimes we multiply by 1/2 to make the derivative simpler. In practice, the differences don’t mean much because we’re not interested in the <em>absolute</em> value, just in how the loss changes from model to another.<br></p><p    >We will switch between these based on what is most useful in a given context.</p><p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-019">
           <a class="slide-link" href="mlvu.github.io/lecture02#video-19">link here</a>
           <iframe
                src="https://youtube.com/embed/q97nOAYfpHg?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-020">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-020">link here</a>
            <img src="12.Linear1.key-stage-0020.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-021">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-021">link here</a>
            <img src="12.Linear1.key-stage-0021.svg" class="slide-image" />

            <figcaption>
            <p    >Remember the two most important spaces of machine learning: the <strong>feature space</strong> and the <strong>model space</strong>. The loss function maps every point in the model space to a loss value. <br></p><p    >In a single-feature regression problem plotted like this, the<strong> </strong>feature space is just the horizontal axis.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-021" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-022">link here</a>
            <img src="12.Linear1.key-stage-0022anim0.svg" data-images="12.Linear1.key-stage-0022anim0.svg,12.Linear1.key-stage-0022anim1.svg" class="slide-image" />

            <figcaption>
            <p    >As we saw in the previous lecture, we can plot the loss for every point in our model space. This is called the <strong>loss surface</strong> or sometimes the <strong>loss landscape</strong>. If you imagine a 2D model space, you can think of the loss surface as a landscape of rolling hills (or sometimes of jagged cliffs).<br></p><p    >Here is what that actually looks like for the two parameters of the one-feature linear regression. Note that this is specific to the data we saw earlier. For a different dataset, we get a different loss landscape.<br></p><p    >To minimize the loss, we need to search this space to find the brightest point in this picture. Or, the lowest point in the loss landscape. Remember that, normally, we may have hundreds of parameters so it isn’t as easy as it looks. Any method we come up with, needs to work in any number of dimensions.<br></p><p    >We’ve plotted the logarithm of the loss as a trick to make this image visually easier to understand (it maps the values that are easy to tell apart to the values we care about). The logarithm is a monotonic function so log(loss(<span class="orange red">w</span>, <span class="blue">b</span>)) has its minimum at the same place as loss(<span class="orange red">w</span>, <span class="blue">b</span>).</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-022" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-023">link here</a>
            <img src="12.Linear1.key-stage-0023anim0.svg" data-images="12.Linear1.key-stage-0023anim0.svg,12.Linear1.key-stage-0023anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The mathematical name for this sort of search is <strong>optimization</strong>. That is, we are trying to find the input (<strong class="orange red">p</strong>, the<span class="orange red"> model parameters</span>) for  which a particular function (the loss) is at its optimum (a maximum or minimum, in this case a minimum). Failing that, we’d like to find as low a value as possible.<br></p><p    >We’ll start by looking at some very simple approaches.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-024">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-024">link here</a>
            <img src="12.Linear1.key-stage-0024.svg" class="slide-image" />

            <figcaption>
            <p    >We often frame machine learning as an optimization problem, and we use many techniques from optimization, but it’s important to recognize that there is a difference between optimization and machine learning.<br></p><p    ><em>Optimization</em> is concerned with finding the absolute minimum (or maximum) of a function. The lower the better, with no ifs or buts. In <em>machine learning</em>, if we have a very expressive model class (like the regression tree from the last lecture), the model that actually minimizes the loss on the training data is the one that overfits. In such cases, we’re not looking to minize the loss on the training data, since that would mean overfitting, we’re looking to minimize the loss on the <em>test data</em>. Of course, we don’t get to see the test data, so we use the training data as a stand in, and try to control against overfitting as best we can.<br></p><p    >In the case of underpowered models like the linear model, this distinction isn’t too important, since they’re very unlikely to overfit. Here, the model that minimizes the loss on the training data is likely the model that minimizes the loss on the test data as well. For now, we'll just try some simple optimization algorithms to find the absolute minimum of the loss, and worry about overfitting later.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-025">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-025">link here</a>
            <img src="12.Linear1.key-stage-0025.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s start with a very simple example:<strong> random search</strong>. We simply make random steps in the model space, and take a step back whenever the loss goes up.<br></p><p    >You usually stop the loop when the loss gets to a pre-defined level, or you just run it for a fixed number of iterations.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-026">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-026">link here</a>
            <img src="12.Linear1.key-stage-0026.svg" class="slide-image" />

            <figcaption>
            <p    >A common analogy is a<em> hiker in a snowstorm</em>. Imagine you’re hiking in the mountains, and you’re caught in a snowstorm. You can’t see a thing, and you’d like to get down to your hotel in the valley, or failing that, you’d like to get to as low a point as possible.<br></p><p    >You take a step in a random direction. If you're moving up, you step back to where you came from, if you're moving down, you repeat the process with a new random direction. This is, in effect, what random search is doing. More importantly, it’s how <em>blind </em>random search is to the larger structure of the landscape. It can only see what's right in front of it.<br></p><p    >image source: <a href="https://www.wbur.org/hereandnow/2016/12/19/rescue-algonquin-mountain">https://www.wbur.org/hereandnow/2016/12/19/rescue-algonquin-mountain</a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-026" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-027">link here</a>
            <img src="12.Linear1.key-stage-0027anim0.svg" data-images="12.Linear1.key-stage-0027anim0.svg,12.Linear1.key-stage-0027anim1.svg,12.Linear1.key-stage-0027anim2.svg,12.Linear1.key-stage-0027anim3.svg,12.Linear1.key-stage-0027anim4.svg,12.Linear1.key-stage-0027anim5.svg,12.Linear1.key-stage-0027anim6.svg" class="slide-image" />

            <figcaption>
            <p    >To implement the random search we need to define how to pick a point “close to” another in model space.<br></p><p    >One option is to choose the next point by sampling uniformly among all points with some pre-chosen distance <span class="green">r</span> from w. Formally: it picks from the hypersphere (or circle, in 2D) with radius <span class="green">r</span>, centered on <strong>p</strong>.<br></p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-028">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-028">link here</a>
            <img src="12.Linear1.key-stage-0028.svg" class="slide-image" />

            <figcaption>
            <p    >Here is random search in action. The transparent red offshoots are steps that turned out to be worse than the current point (uphill). The algorithm starts on the left, and slowly (with a bit of a detour) stumbles in the direction of the low loss region.<br></p><p    >As we can see, it doesn't exactly make a beeline for the lowest point, but it gets there eventually.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-029">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-029">link here</a>
            <img src="12.Linear1.key-stage-0029.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what it looks like in <strong>feature space</strong>. The first model (bottom-most line) is entirely wrong, and the search slowly moves, step by step, towards a reasonable fit on the data.<br></p><p    >Every blue line in this image corresponds to a red dot in the model space (inset).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-029" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-030">link here</a>
            <img src="12.Linear1.key-stage-0030anim0.svg" data-images="12.Linear1.key-stage-0030anim0.svg,12.Linear1.key-stage-0030anim1.svg,12.Linear1.key-stage-0030anim2.svg" class="slide-image" />

            <figcaption>
            <p    >One of the reasons such a simple approach works well enough here is that our problem is <strong>convex</strong>. A surface (like our loss landscape) is convex if a line drawn between any two points on the surface lies entirely above the surface. One of the implications of convexity is that any point that looks like a minimum locally (because all nearby points are higher) it must be the <strong>global minimum</strong>: it’s lower than any other point on the surface.<br></p><p    >This minimum is the optimal model. So long as we know we’re moving down (to a point with lower loss), we can be sure we’re moving towards the global minimum: the best of all possible models.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-030" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-031">link here</a>
            <img src="12.Linear1.key-stage-0031anim0.png" data-images="12.Linear1.key-stage-0031anim0.png,12.Linear1.key-stage-0031anim1.png,12.Linear1.key-stage-0031anim2.png" class="slide-image" />

            <figcaption>
            <p    >So let’s look at what happens if the loss surface<em> isn’t</em> convex: what if the loss surface has multiple<em> </em><strong>local minima</strong>? These are points that are lower than all nearby points, but if we move far enough away from them, we <em>can</em> find a point that is even lower.<br></p><p    >Here’s a loss surface with a more complex structure.  The two purple points are the lowest point in their respective <em>neighborhoods</em>, but the red point is the lowest point globally.<br></p><p    >NB: This loss surface isn't based on actual data. It's just some function that illustrates the idea.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-032">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-032">link here</a>
            <img src="12.Linear1.key-stage-0032.svg" class="slide-image" />

            <figcaption>
            <p    >Here we see random search on our more complex loss surface. As you can see, it heads quickly for one of the local minima, and then gets stuck there. No matter how many more iterations we give it, it will never escape.<br></p><p    >Note that changing the step size will not help us here. Once the search is stuck, it stays stuck.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-033">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-033">link here</a>
            <img src="12.Linear1.key-stage-0033.svg" class="slide-image" />

            <figcaption>
            <p    >There are a few tricks that can help us to escape local minima. Here’s a popular one, called <strong>simulated annealing</strong>: if the next point chosen isn’t better than the current one, we still pick it, but only with some small probability. In other words, we allow the algorithm to<em> occasionally </em>travel uphill. <br></p><p    >This means that whenever it gets stuck in a local minimum, it still has some probability of escaping, and finding the global minimum.<br></p><p    >The name "simulated annealing" is a bit of a historical accident, so don't read too much in to it. It comes from the fact that this algorithm can be used to simulate the cooling of a material like metal. The carefully controlled cooling of a material to promote the growth of particular kinds of crystals is called annealing. In physical terms this is like looking for the minimum in an energy landscape, which is mathematically similar to our loss landscape. </p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-034">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-034">link here</a>
            <img src="12.Linear1.key-stage-0034.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a run of simulated annealing on our non-convex problem. We see that it still hits the local minimum first, but after a while it manages to jump out, and to find the global minimum.<br></p><p    >Of course, with this algorithm, there is always the possibility that it will jump out of the global minimum again and move to a worse minimum. That shouldn’t worry us, however, so long as we remember the best model we’ve observed over the entire run. Then we can just let simulated annealing jump around the model space driven partly by random noise, and partly by the loss surface.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-035">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-035">link here</a>
            <img src="12.Linear1.key-stage-0035.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-036">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-036">link here</a>
            <img src="12.Linear1.key-stage-0036.svg" class="slide-image" />

            <figcaption>
            <p    >The fixed step size we used so far is just one way to sample the next point. To allow the algorithm to occasionally make smaller steps, you can sample<span> m</span><span>’ </span>so that it is <em>at most</em> some distance away from <span>m</span>, instead of <em>exactly</em>. Another approach is to sample the distance from <strong>a Normal distribution</strong>. That way, most points will be close to the original <span>m</span>, but every point in the model space can theoretically be reached in one step.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-037">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-037">link here</a>
            <img src="12.Linear1.key-stage-0037.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what random search looks when the steps are sampled from a normal distribution. Note that the “failed” steps all have different sizes.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-038">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-038">link here</a>
            <img src="12.Linear1.key-stage-0038.svg" class="slide-image" />

            <figcaption>
            <p    >The space of linear models is <em>continuous</em>: between every two models, there is always another model, no matter how close they are together. * <br></p><p    >The alternative is a discrete model space. For instance, the space of all trees is discrete. If our model takes the form of a tree (like the decision tree we saw in the last lecture), then we don't always have another model "in between" any two given models. In this case, some search algorithms no longer work, but random search and simulated annealing can still be used.  <br></p><p    >You just need to define which models are “close” to each other. In this slide, we say that two trees are close if I can turn one into the other by adding or removing a single node.<br></p><p    >Random search and simulated annealing can now be used to search this space to find the tree model that gives the best performance.<br></p><p    >In practice, we usually use a different method to search for decision trees and regression trees, which will introduce this algorithm in a later lecture. The point here is just that if you are searching a discrete space, random search and simulated annealing still work.<br></p><p    >* Strictly speaking this is not a complete definition of a continuous space, but it's the property that matters for us.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-039">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-039">link here</a>
            <img src="12.Linear1.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >Another thing you can do is just to run random search a couple of times independently (one after the other, or in parallel). If you’re lucky one of these runs may start you off close enough to the global minimum.<br></p><p    >For simulated annealing, doing multiple runs makes less sense. There’s not much difference between 10 runs of 100 iterations and one run of 1000. The only reason to do multiple runs of SA is because it’s easier to parallelize over multiple cores or machines.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-040">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-040">link here</a>
            <img src="12.Linear1.key-stage-0040.svg" class="slide-image" />

            <figcaption>
            <p    >To make parallel search even more useful, we can introduce some form of communication or synchronization between the searches happening in parallel. If we see the parallel searches as a <em>population</em> of agents that occasionally “communicate”, we can guide the search a lot more. Here are some examples of such <strong>population methods</strong>. we won’t go into this too deeply. We will only take a (very) brief look at evolutionary algorithms.<br></p><p    >Often, there are specific variants for discrete and for continuous model spaces.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-041">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-041">link here</a>
            <img src="12.Linear1.key-stage-0041.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a basic outline of an evolutionary method (although many variations exist). In order to instantiate this, we need to define what it means to “breed” a population of new models from an existing population. A common approach is to select to random parents and to somehow average their models. This is easy to do in a continuous model space (we can literally average the two parent models to create a child). <br></p><p    ><br></p><p    >In a discrete model space, it’s more difficult, and it depends on the specifics of the model space. In such case, designing the breeding process (sometimes called the <strong>crossover operator</strong>) is usually the most difficult part of designing an effective evolutionary algorithm.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-041" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-042">link here</a>
            <img src="12.Linear1.key-stage-0042anim0.svg" data-images="12.Linear1.key-stage-0042anim0.svg,12.Linear1.key-stage-0042anim1.svg,12.Linear1.key-stage-0042anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s what that a very basic evolutionary search looks like on our non-convex loss surface. We start with a population of 50 models, and compute the loss for each. We kill the worst 50% (<span class="orange red">the red dots</span>) and keep the best 50% (<span class="green">the green dots</span>). <br></p><p    >We then create a new population (<span class="blue">the blue crosses</span>), by randomly pairing up parents from the green population, and taking the point halfway between the two parents, with a little noise added. Finally, we take the blue crosses as the new population and repeat the process.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-043">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-043">link here</a>
            <img src="12.Linear1.key-stage-0043.svg" class="slide-image" />

            <figcaption>
            <p    >Here are five iterations of the algorithm. Note that in the intermediate stages, the population covers both the local and the global minima.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-044">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-044">link here</a>
            <img src="12.Linear1.key-stage-0044.svg" class="slide-image" />

            <figcaption>
            <p    >Population methods are very powerful, but computing the loss for so many different models is often expensive. They can also come with a lot of different parameters to control the search, each of which you will need to carefully tune.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-045">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-045">link here</a>
            <img src="12.Linear1.key-stage-0045.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-046">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-046">link here</a>
            <img src="12.Linear1.key-stage-0046.svg" class="slide-image" />

            <figcaption>
            <p    >All these search methods are instances of <strong>black box optimization</strong>.<br></p><p    >Black box optimization refers to those methods that only require us to be able to compute the loss function. We don’t need to know anything about the internals of the model.<br></p><p    >In the next video we’ll look at a way to improve the search by opening up the black box: gradient descent.</p><p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-046">
           <a class="slide-link" href="mlvu.github.io/lecture02#video-46">link here</a>
           <iframe
                src="https://youtube.com/embed/DlMKkPrKg5c?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-047">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-047">link here</a>
            <img src="12.Linear1.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-048">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-048">link here</a>
            <img src="12.Linear1.key-stage-0048.svg" class="slide-image" />

            <figcaption>
            <p    >As a stepping stone to what we’ll discuss in this video, let’s take the random search from the previous video, and add a little more inspection of the local neigborhood before taking a step. Instead of taking one random step, we’ll look at k random steps and move in the direction of the one that gives us the lowest loss.<br></p><p    >In the hiker analogy, you can think of this algorithm as the case where the hikertaps his foot on the ground in a couple of random directions, and then moves in the direction with the strongest downward slope.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-049">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-049">link here</a>
            <img src="12.Linear1.key-stage-0049.svg" class="slide-image" />

            <figcaption>
            <p    >Here's what that looks like for a few values of <span class="orange red">k</span>.<br></p><p    >As you can see, the more samples we take, the more directly we head for the region of  low loss. The more closely we inspect our local neighbourhood, to determine in which direction the function decreases quickest, the faster we converge.<br></p><p    >The lesson here is that the better we know in which direction the loss decreases, the faster our search converges. In this case we pay a steep price: we have to evaluate our function 15 times to work out a better direction.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-050">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-050">link here</a>
            <img src="12.Linear1.key-stage-0050.svg" class="slide-image" />

            <figcaption>
            <p    >However, if our model space is continuous, and if our loss function is smooth, we don’t<em> need </em>to take multiple samples to guess the direction of fastest descent: <em>we can simply derive it, using calculus</em>. This is the basis of the <strong>gradient descent algorithm</strong>.<br></p><p    >image source: <a href="http://charlesfranzen.com/posts/multiple-regression-in-python-gradient-descent/"><strong class="blue">http://charlesfranzen.com/posts/multiple-regression-in-python-gradient-descent/</strong></a></p><p    ><a href="http://charlesfranzen.com/posts/multiple-regression-in-python-gradient-descent/"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-051">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-051">link here</a>
            <img src="12.Linear1.key-stage-0051.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-052">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-052">link here</a>
            <img src="12.Linear1.key-stage-0052.svg" class="slide-image" />

            <figcaption>
            <p    >Before we dig in to the gradient descent algorithm, let’s review some basic principles from calculus. First up, <strong>slope</strong>. The slope of a linear function is simply <strong>how much it moves up</strong> if <strong>we move one step to the right</strong>. In the case of f(x) in this picture, the slope is <em>negative</em>, because the line moves down.<br></p><p    >In our 1D regression model, the parameter <span class="orange red">w</span> was the slope. In this case, however we will investigate the slope of the loss landscape, not of the model (be sure not to confuse these two).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-052" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-053">link here</a>
            <img src="12.Linear1.key-stage-0053anim0.svg" data-images="12.Linear1.key-stage-0053anim0.svg,12.Linear1.key-stage-0053anim1.svg,12.Linear1.key-stage-0053anim2.svg,12.Linear1.key-stage-0053anim3.svg,12.Linear1.key-stage-0053anim4.svg,12.Linear1.key-stage-0053anim5.svg" class="slide-image" />

            <figcaption>
            <p    >The <strong>tangent line </strong>of a function at particular point <strong>x</strong> is the line that just touches the function at <strong>x</strong>. The<strong> derivative of the function gives us the slope of the tangent line</strong>. Traditionally we find the minimum of a function by setting the derivative equal to 0 and solving for <strong>x</strong>. This gives us the point where the tangent line has slope 0, and is therefore horizontal.<br></p><p    >For complex models, it may not be possible to solve for x in this way. However, we can still use the gradient to <em>search </em> for the minimum. Looking at the example in the slide, we note that the tangent line moves down (i.e. the slope is negative). This tells us that we should move to the right to follow the function downward. As we take small steps to the right, the derivative stays negative, but gets smaller and smaller as we close in on the minimum. This suggests that the <em>magnitude</em> of the slope lets us know how big the steps are that we should take, and the <em>sign </em>gives us the direction.<br></p><p    >A useful analogy is to think of putting a marble at some point on the curve and following it as it rolls downhill to find the lowest point.<br></p><p    >What we need to do now, is to take the derivative of the function describing the loss surface, and work out <br></p><p     class="list-item">The direction in which the function decreases the quickest. We call this <strong>the direction of steepest descent</strong>.<br></p><p     class="list-item">How quickly the function decreases in that direction.</p><p     class="list-item"></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-054">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-054">link here</a>
            <img src="12.Linear1.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >To apply this principle in machine learning, we’ll need to generalise it for loss functions with multiple inputs (i.e. for models with <span class="orange red">multiple parameters</span>). We do this by generalising the<em> derivative</em> to the<strong> gradient</strong>. The tangent line becomes a tangent (hyper)plane. <br></p><p    >Once we have this hyperplane, we can use it to work out in which direction the function grows and shrinks the quickest. One way of thinking about this is that the tangent hyperplane is a local approximation of the function. Zoomed out like this the hyperplane and the function look nothing alike, but if we zoom in close enough, they behave almost exactly the same. <br></p><p    >This is useful, because in a hyperplane it's very easy to see in which direction it goes down the quickest. Much easier than it is for a complicated beast like our loss function itself. Since the hyperplane approximates the loss function, this is also the direction in which the loss decreases the quickest. At least, so long as we don't move away too far from the area where the hyperplane is a good approximation of the loss function.<br></p><p    >image source: <a href="https://nl.mathworks.com/help/matlab/math/calculate-tangent-plane-to-surface.html?requestedDomain=true"><strong class="blue">https://nl.mathworks.com/help/matlab/math/calculate-tangent-plane-to-surface.html?requestedDomain=true</strong></a></p><p    ><a href="https://nl.mathworks.com/help/matlab/math/calculate-tangent-plane-to-surface.html?requestedDomain=true"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-054" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-055">link here</a>
            <img src="12.Linear1.key-stage-0055anim0.svg" data-images="12.Linear1.key-stage-0055anim0.svg,12.Linear1.key-stage-0055anim1.svg,12.Linear1.key-stage-0055anim2.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    >We’re used to thinking of vectors as points in the plane. But they can also be used to represent<em> directions</em>. In this case we use the vector to represent the arrow from the origin to the point. This gives us a<strong> direction</strong> (the direction in which the arrow points), and a <strong>magnitude </strong>(the length of the arrow). <br></p><p    >So this direction of steepest descent that we’re looking for (in model space) can be expressed as a vector.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-056">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-056">link here</a>
            <img src="12.Linear1.key-stage-0056.svg" class="slide-image" />

            <figcaption>
            <p    >Remember, that this is how we express a linear function in n dimensions: we assign each dimension a slope, and add a single <span class="blue">bias (c)</span>.<br></p><p    >In this image, the two weights of a linear 2D function (<span class="orange red">a</span> and <span class="green">b</span>) representing a hyperplane, are just one slope per dimension. If we move<span> one step</span> in the direction of  x<sup>1</sup>, we move<span class="green"> </span>up by <span class="green">a</span>, and if we move<span> one step</span> in the direction of  x<sup>2</sup>, we move up by <span class="green">b</span>.<br></p><p    >This is the same picture we saw earlier for the linear function, but we're using it in a different way. Earlier, it represented a model with<em> two features</em>. Here, it serves as an approximation for a loss landscape for a model with <em>two parameters</em>.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-056" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-057">link here</a>
            <img src="12.Linear1.key-stage-0057anim0.svg" data-images="12.Linear1.key-stage-0057anim0.svg,12.Linear1.key-stage-0057anim1.svg,12.Linear1.key-stage-0057anim2.svg,12.Linear1.key-stage-0057anim3.svg" class="slide-image" />

            <figcaption>
            <p    >We are now ready to define the gradient. Any function from n inputs to one output has n variables for which we can take the derivative. These are called <strong>partial derivatives</strong>: they work the same way as regular derivatives, except that you when you take the derivative with respect to one variable x, you treat the other variables as constants.<br></p><p    >One thing that is sometimes a little confusing is that the gradient of a function f(·) is another <em>function</em> ∇f(·), which defines the slopes of the tangent hyperplane for all points. At a specific point <strong>p</strong>, the gradient provides the slope of the tangent hyperplane g. The function g is then a function of x where this gradient is a constant..<br></p><p    >If a particular function f(x) has gradient <strong>g</strong> for input x, then f’(<strong>x</strong>) = <strong>g</strong><sup>T</sup><strong>x</strong> + b (for some b) is the tangent hyperplane at <strong>x</strong>. This is a simple function, so we can easily work out what the direction of steepest ascent/descent is on this hyperplane.<br></p><p    >The gradient is sometimes defined as a row vector, and sometimes as a column vector. In machine learning contexts, the latter usually makes most sense.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-057" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-058">link here</a>
            <img src="12.Linear1.key-stage-0058anim0.svg" data-images="12.Linear1.key-stage-0058anim0.svg,12.Linear1.key-stage-0058anim1.svg,12.Linear1.key-stage-0058anim2.svg,12.Linear1.key-stage-0058anim3.svg,12.Linear1.key-stage-0058anim4.svg" class="slide-image" />

            <figcaption>
            <p    >So, now that we have a local linear approximation g to our function f, which is the direction of steepest ascent on the approximation g?<br></p><p    >Since g is linear, many details don’t matter: we can set <span class="blue">b</span> to zero, since that just translates the hyperplane up or down. It doesn’t matter <em>how big </em>a step we take in any direction, so we’ll take a step of size 1. Finally, it doesn’t matter where we start from, so we will just start from the origin. So the question becomes: for which input <strong>x</strong> of magnitude 1 (which unit vector) does g(<strong>x</strong>) provide the biggest output?<br></p><p    >To see the answer, we need to use the geometric interpretation of the dot product. Since we required that ||<strong class="green">x</strong>||= 1<strong>,</strong> this disappears from the equation, and we only need to maximise the quantity ||<strong>w</strong>|| cos(α) (where only α depends on our choice of <strong>x</strong>, and <strong>w</strong> is the gradient we computed). cos(α) is maximal when α is zero: that is, when <strong>x</strong> and <strong>w</strong> are pointing in the same direction.<br></p><p    >In short: <span>w</span>, the gradient,<span> </span> <em>is</em> the direction of steepest ascent. <span>This means that -</span><span>w</span><span> is the direction of steepest </span><em>descent</em><span>.<br></span></p><p    ><span>What we have shown, </span></p><p    ><span></span></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-059">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-059">link here</a>
            <img src="12.Linear1.key-stage-0059.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-060">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-060">link here</a>
            <img src="12.Linear1.key-stage-0060.svg" class="slide-image" />

            <figcaption>
            <p    >Note that the gradient is a <em>vector</em>: it has a direction <em>and a magnitude</em>. The magnitude tells us how quickly the linear function is rising. This is very useful in search, since the more the function is changing, the bigger the steps that we want to take. <br></p><p    ><br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-061">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-061">link here</a>
            <img src="12.Linear1.key-stage-0061.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the <strong>gradient descent algorithm</strong>. Starting from some candidate <strong>p</strong>, we simply compute the gradient at <strong>p</strong>, subtract it from the current choice, and iterate this process:<br></p><p     class="list-item">We<em> subtract</em>, because the gradient points <em>uphill</em>. Since the gradient is the direction of steepest ascent, the negative gradient is the direction of steepest <em>de</em>scent.<br></p><p     class="list-item">Since the gradient is only a<em> local approximation </em>to our loss function, the bigger our step the bigger the approximation error. Usually we scale down the step size indicated by the gradient by multiplying it by a learning rate <span>η</span>. This value is chosen by trial and error, and remains constant throughout the search (at least in the simplest version of the algorithm).<br></p><p    ><strong>Note again a potential point of confusion:</strong> we have two linear functions here.  One is the <em>model</em>, whose parameters are indicated by <strong class="orange red">w</strong> and <span class="blue">b</span>. The other is the tangent hyperplane to the loss function, whose slope is indicated by ∇loss(<strong>p</strong>) here. These are different functions on different spaces.<br></p><p    >We can iterate for a fixed number of iterations, until the loss gets low enough, or until the gradient gets close enough to the zero vector, which implies we've reached a local minimum.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-062">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-062">link here</a>
            <img src="12.Linear1.key-stage-0062.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-063">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-063">link here</a>
            <img src="12.Linear1.key-stage-0063.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s go back to our example problem, and see how we can apply gradient descent here.<br></p><p    >Unlike random search, it’s not enough to just compute the loss for a given model,<strong> we need the gradient of the loss</strong>.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-064">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-064">link here</a>
            <img src="12.Linear1.key-stage-0064.svg" class="slide-image" />

            <figcaption>
            <p    >Here is our loss function again, and the two partial derivatives we need work out to find the gradient.<br></p><p    >To simplify the notation we’ll let x<sup>i</sup> refer to the only feature of instance i.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-064" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-065">link here</a>
            <img src="12.Linear1.key-stage-0065anim0.svg" data-images="12.Linear1.key-stage-0065anim0.svg,12.Linear1.key-stage-0065anim1.svg,12.Linear1.key-stage-0065anim2.svg,12.Linear1.key-stage-0065anim3.svg,12.Linear1.key-stage-0065anim4.svg,12.Linear1.key-stage-0065anim5.svg,12.Linear1.key-stage-0065anim6.svg" class="slide-image" />

            <figcaption>
            <p    >Here are the derivations of the two partial derivatives:<br></p><p     class="list-item">first we use the <em>sum rule</em>, moving the derivative inside the sum symbol<br></p><p     class="list-item">then we use the <em>chain rule</em>, to split the function into the composition of computing the residual and squaring, computing the derivative of each with respect to its argument.<br></p><p    >The second homework exercise provides a list of the most common rules for derivatives.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-065" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-066">link here</a>
            <img src="12.Linear1.key-stage-0066anim0.svg" data-images="12.Linear1.key-stage-0066anim0.svg,12.Linear1.key-stage-0066anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This is wha the iteration of gradient descent looks like for our specific model and loss function. We start with some initial guess, compute the gradient of the loss with the two functions we've just worked out, and we subtract that vector (times some scalar η) from our guess. <br></p><p    >Hopefully, repeating this process a number of times in small steps will directly follow the loss surface down to a (local) minimum.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-067">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-067">link here</a>
            <img src="12.Linear1.key-stage-0067.png" class="slide-image" />

            <figcaption>
            <p    >Here is the result on our dataset. Note how the iteration converges directly to the minimum. Note also that we have no rejections: the algorithm is fully deterministic: it computes the optimal step, and takes it. There is no trial and error anymore.<br></p><p    >Note also that the gradient gives us a direction and a <strong>step size</strong>. As we get closer to the minimum, the function <em>flattens out</em> and the magnitude of the gradient decreases. The effect is that as we approach the minimum the algorithm automatically takes smaller and smaller steps, preventing us overshooting the optimum.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-068">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-068">link here</a>
            <img src="12.Linear1.key-stage-0068.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what it looks like in feature space.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-069">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-069">link here</a>
            <img src="12.Linear1.key-stage-0069.svg" class="slide-image" />

            <figcaption>
            <p    ><a href="https://bit.ly/36r66Qh"><strong class="blue">https://bit.ly/36r66Qh</strong></a><br></p><p    >Here is a very helpful little browser app that we’ll return to a few times during the course. It contains a few things that that we haven't discussed yet, but if you remove all hidden layers, and set the target to regression, you'll get a linear classifier of the kind that we've been discussing.<br></p><p    >The output for the data is indicated by the color of the points, the output of the model is indicated by the colouring of the plane.<br></p><p    >Note that the page calls this model a neural network (which we won’t discuss for a few more weeks). Linear models are just a very simple neural network.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-070">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-070">link here</a>
            <img src="12.Linear1.key-stage-0070.png" class="slide-image" />

            <figcaption>
            <p    >If our function is non-convex, gradient descent doesn’t help us with the problem of local minima. As we see here, it heads straight for the nearest minimum and stays there. To make the algorithm more robust against this type of thing, we need to add a little randomness back in, preferably without destroying the behaviour of moving so cleanly to a minimum once one is found.<br></p><p    >We can also try multiple runs from different starts. Later we will see <em>stochastic</em> gradient descent, which computes the gradient only over subsets of the data (making the algorithm more efficient, and adding a little randomness at the same time).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-071">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-071">link here</a>
            <img src="12.Linear1.key-stage-0071.png" class="slide-image" />

            <figcaption>
            <p    >Here is a more fortunate run.<br></p><p    >NB: The point of convergence seems a little off in these images. The partial derivatives for this function are very complex (I used<a href="https://goo.gl/zbeidi"><strong class="blue"> Wolfram Alpha</strong></a> to find them), so most likely, the implementation has some numerical instability.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-072">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-072">link here</a>
            <img src="12.Linear1.key-stage-0072.png" class="slide-image" />

            <figcaption>
            <p    >Here, we see the effect of the learning rate. If we set if too high, the gradient descent jumps outof the first minimum it finds. A little lower and it stays in the neighborhood of the first minimum, but it sort of bounces from side to side, only very slowly moving towards the actual minimum.<br></p><p    >At 0.01, we find a sweet spot where it finds the local minimum pretty quickly. At 0.005 we see the same behavior, but we need to wait much longer, because the step sizes are so small.<br></p><p    >The best value of the learning rate is different for each dataset and each model. You'll usually have to find it by trial and error. We'll talk a little more about how this looks in practice in the next lecture.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-073">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-073">link here</a>
            <img src="12.Linear1.key-stage-0073.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-074">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-074">link here</a>
            <img src="12.Linear1.key-stage-0074.svg" class="slide-image" />

            <figcaption>
            <p    >It’s worth saying that for <strong>linear regression</strong>, although it makes a nice, simple illustration, none of this is actually necessary. For linear regression, we can set the derivatives equal to zero and solve explicitly for <strong>w</strong> and for <span class="blue">b</span>. This would give us the optimal solution  directly without searching.<br></p><p    >However, this trick will stop working very quickly once we start looking at more complicated models, so we won’t go down this route very much. Consult your linear algebra textbook to see what this analytical solution looks like.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-075">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-075">link here</a>
            <img src="12.Linear1.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-075">
           <a class="slide-link" href="mlvu.github.io/lecture02#video-75">link here</a>
           <iframe
                src="https://youtube.com/embed/LjhzJUy-wfk?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-076">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-076">link here</a>
            <img src="12.Linear1.key-stage-0076.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-077">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-077">link here</a>
            <img src="12.Linear1.key-stage-0077.svg" class="slide-image" />

            <figcaption>
            <p    >Now, let’s look at how this works for classification. <br></p><p    >The first question we need to answer is how do we <em>define</em> a linear classifier: that is, a classifier whose decision boundary is always a line (or hyperplane) in feature space.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-078">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-078">link here</a>
            <img src="12.Linear1.key-stage-0078.svg" class="slide-image" />

            <figcaption>
            <p    >To define a linear decision boundary, we take the same functional form we used for the linear regression: some weight vector <strong class="orange red">w</strong>, and a bias <span class="blue">b</span>. <br></p><p    >The way we define the decision boundary is a little different than the way we defined the regression line. Here, we say that if <strong>w</strong><sup>T</sup><strong>x</strong> + b is larger than 0, we call <strong>x </strong>one class, if  it is smaller than 0, we call it the other (we’ll stick to binary classification for now).<br></p><p    >Note that we are drawing a line in a different space: in the regression example we draw a line in the combined feature and output space (a function from the feature to the output). Here, we have two features, and we are trying to draw a line in only the feature space.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-079">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-079">link here</a>
            <img src="12.Linear1.key-stage-0079.svg" class="slide-image" />

            <figcaption>
            <p    >The actual line or hyperplane we are defining can be tought of as lying above and below the feature space. <br></p><p    >Here it is visualized for the case of one feature. We are defining a linear function from the feature to some output y. Wherever this line lies above the feature space (i.e. is positive), we classify things as the<span class="blue"> blue/circle class</span>, and wherever the line lies below the feature space (i.e. is negative) we classify them as the<span class="orange red"> red/diamond class</span>.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-080">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-080">link here</a>
            <img src="12.Linear1.key-stage-0080.svg" class="slide-image" />

            <figcaption>
            <p    >The function f(x) = <strong>w</strong><sup>T</sup><strong>x</strong> + b describes a linear function from our feature space to a single value. Here it is in 2D: a plane that intersects the feature space. The line of intersection is our decision boundary.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-081">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-081">link here</a>
            <img src="12.Linear1.key-stage-0081.svg" class="slide-image" />

            <figcaption>
            <p    >This also shows us how to interpret <strong>w</strong>. Since it is the direction of steepest ascent, it is the vector <strong>perpendicular to the decision boundary</strong>, pointing to the class we assigned to the case where  <strong>w</strong><sup>T</sup><strong>x</strong> + <span class="blue">b</span> is larger than 0 (the<span> blue</span> class in this case).<br></p><p    >We never want to "ascend" this plane like we do with the hyperplane approximating the loss landscape, but it's useful for our geometric intuition to know where <strong>w</strong> points, relative to our decision boundary. This is come one handy specifically when we start talking about classifiers that maximize the margin to the nearest data points.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-082">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-082">link here</a>
            <img src="12.Linear1.key-stage-0082.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a simple classification dataset, which we’ll use to illustrate the principle.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-083">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-083">link here</a>
            <img src="12.Linear1.key-stage-0083.svg" class="slide-image" />

            <figcaption>
            <p    >This gives us a model space, but how do we decide the quality of any particular model? What is our<strong> loss function</strong> for classification?<br></p><p    >The thing we are usually trying to minimise is the <strong>error</strong>: the number of misclassified examples. Sometimes we are looking for something else, but in the simplest classification problems, this is what we are ultimately interested in: a classifier that makes as few mistakes as possible. So let's start there: <em>can we use the error as a loss function?</em></p><p    ><em></em></p>
            </figcaption>
       </section>


       <section id="slide-084">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-084">link here</a>
            <img src="12.Linear1.key-stage-0084.svg" class="slide-image" />

            <figcaption>
            <p    >This is what our loss surface looks like for the error function on our simple dataset. Note that it consists almost entirely of flat regions. This is because changing a model a tiny bit will usually not change the number of misclassified examples. And if it does, the loss function will suddenly jump a lot.<br></p><p    >In these flat regions, random search would have to do a random walk, stumbling around until it finds a ridge by accident. <br></p><p    >Gradient descent would fare even worse: the gradient is zero everywhere in this picture, except exactly on the ridges, where it is undefined. Gradient descent would either crash, or simply never move.<br></p><p    >Note that our model now has three parameters <span class="orange red">w</span><sup class="orange red">1</sup>, <span class="orange red">w</span><sup class="orange red">2</sup> and <span>b</span>, so the loss surface is a function on a 3d space (a 4d "surface"). In order to plot it in two dimensions, we have fixed <span class="orange red">w</span><sup class="orange red">2</sup>=1.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-085">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-085">link here</a>
            <img src="12.Linear1.key-stage-0085.svg" class="slide-image" />

            <figcaption>
            <p    >This is an important lesson about loss functions. They serve two purposes: <br></p><p     class="list-item">To express what quantity we want to maximise in our search for a good model.<br></p><p     class="list-item">To provide <strong>a smooth loss surface</strong>, so that we can find a path from a bad model to a good one.<br></p><p    >For this reason, it’s common not to use the error as a loss function, even when it’s the thing we’re actually interested in minimizing. Instead, we’ll replace it by a loss function that has its minimum at (roughly) the same model, but that provides a smooth, differentiable loss surface.<br></p><p    >After we have trained a model we can still <em>evaluate</em> it with the function we're actually interested in (that is, we can still count how many mistakes it makes). We'll discuss evaluation in-depth in the next lecture.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-086">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-086">link here</a>
            <img src="12.Linear1.key-stage-0086.svg" class="slide-image" />

            <figcaption>
            <p    >In this course, we will investigate three common loss functions for classification. The first, least-squares loss, is just an application of MSE loss to classification, we will discuss that in the remainder of the lecture. It's not usually that good, but it gives you an idea of what a classification loss might look like.<br></p><p    >The others require a bit more background, so we’ll save them for later.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-086" class="anim">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-087">link here</a>
            <img src="12.Linear1.key-stage-0087anim0.svg" data-images="12.Linear1.key-stage-0087anim0.svg,12.Linear1.key-stage-0087anim1.svg,12.Linear1.key-stage-0087anim2.svg,12.Linear1.key-stage-0087anim3.svg" class="slide-image" />

            <figcaption>
            <p    >The least squares classifier essentially turns the classification problem into a regression problem: it assigns points in <span class="blue">one clas</span>s the numeric value +1 and points in the <span class="orange red">other class</span> the value -1, we then use a basic MSE loss that we saw before the break to train a regression model to predict these numeric values. <br></p><p    >Performing gradient descent with this loss function will result in a line that minimises the green residuals. Hopefully the points are far enough apart that the decision boundary (the <strong class="green">single point </strong>where the orange line crosses the x axis) separates the two classes.<br></p><p    >As you can see, we always get very big residuals whatever we do. That is because the points simply do not lie on a single line, so the linear model is not appropriate. Still, with a little luck, the best fitting line will be positive for the +1 class and negative for the -1 class. If so the classifier will make the right predictions, even if the model is way off as a regression model for the numeric labels we introduced.</p><p    ></p>
            </figcaption>

            <span class="hint">click image for animation
            </span>
       </section>



       <section id="slide-088">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-088">link here</a>
            <img src="12.Linear1.key-stage-0088.svg" class="slide-image" />

            <figcaption>
            <p    >With this loss function, we note that our loss surface is perfectly smooth.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-089">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-089">link here</a>
            <img src="12.Linear1.key-stage-0089.svg" class="slide-image" />

            <figcaption>
            <p    >And gradient descent has no problem finding a solution. <br></p><p    >Note, however that the optimum under this loss function may not perfectly separate the classes, even if they <em>are</em> linearly separable. It does in our case, but this result is not guaranteed.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-090">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-090">link here</a>
            <img src="12.Linear1.key-stage-0090.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the result in instance space, with the final decision boundary in orange.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-091">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-091">link here</a>
            <img src="12.Linear1.key-stage-0091.svg" class="slide-image" />

            <figcaption>
            <p    ><a href="https://bit.ly/2Me1fxU"><strong class="blue">https://bit.ly/2Me1fxU</strong></a><br></p><p    >The tensorflow playground also allows us to play around with linear classifiers. Note that only for one of the two datasets, the linear decision boundary is appropriate.<br></p><p    >This example actually uses a logarithmic loss, rather than a least squares loss. We’ll discuss this kind of loss in the first probability lecture.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-092">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-092">link here</a>
            <img src="12.Linear1.key-stage-0092.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-093">
            <a class="slide-link" href="mlvu.github.io/lecture02#slide-093">link here</a>
            <img src="12.Linear1.key-stage-0093.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

</article>
