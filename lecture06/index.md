---
title: "Lecture 6: Beyond linear models"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 6: Beyond linear models</li>
                <li><a href="#video-000">Neural networks</a></li>
                <li><a href="#video-016">Backpropagation</a></li>
                <li><a href="#video-038">Support vector machines</a></li>
                <li><a href="#slide-074">Support vector machines*<br></a></li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/32.LinearModels2.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">


       <section class="video" id="video-000">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-0">link here</a>
           <iframe
                src="https://www.youtube.com/embed/DeQ4STHYT3g"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-001">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-001" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-002">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-002" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0003.png" class="slide-image" />

            <figcaption>
            <p    >A few lectures ago, we saw how we could make a linear model more powerful, and able to learn nonlinear decision boundaries by just <strong>expanding our features</strong>: we add new features derived from the old ones, and depending on which combinations we add, we can learn new, non-linear decision boundaries or regression functions.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-003">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-003" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0004.svg" class="slide-image" />

            <figcaption>
            <p    >Both models we will see today, <strong>neural networks </strong>and<strong> support vector machines</strong>, take this idea and build on it. Neural networks are a big family, but the simplest type, the <strong>two-layer feedforward network</strong>, functions as a feature extractor followed by a linear model. In this case, we don’t choose the extended features but we <em>learn</em> them, together with the weights of the linear model.<br></p><p    >The support vector machine doesn’t learn the expanded features (we still have to choose them manually), but it uses a<strong> kernel function</strong> to allow us to fit a linear model in a <em>very</em> high-dimensional feature without  having to pay for actually computing all these expanded features.<br></p><aside    >Using the SVM in this way is becoming less popular. Their loss function (the maximum margin loss) is still used, but the feature expansion trick is exceedingly rare. For this reason, we have made this part of the lecture <span>optional</span>. We suggest you have at least a quick look at the basic idea, but the material covered in the fourth part of this lecture won’t appear on the exam.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-004">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-004" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0005.svg" class="slide-image" />

            <figcaption>
            <p    >The layout of today’s lecture will be largely chronological. We will focus on <strong>neural networks</strong>, which were very popular in the late eighties and early nineties. <br></p><p    >Then, towards the end of the nineties, interest in neural networks died down a little and <strong>support vector machines</strong> became much more popular.<br></p><p    >In the next lecture, we’ll focus on Deep Learning, which sees neural networks make a comeback in a big way.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-005">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-005" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0006.svg" class="slide-image" />

            <figcaption>
            <p    >In this video, we’ll start with the basics of neural networks. <br></p><p    ><br></p><p    >In the very early days of AI (the late 1950s), researchers decided to try a simple approach: the brain is the only truly intelligent system we know, so let’s see what it’s made of, and whether that provides some inspiration for intelligent (and learning) computer systems.<br></p><p    ><br></p><p    >They started with a single brain cell: a neuron. A neuron receives multiple different input signals from other cells through connections called <strong>dendrites</strong>. It processes these in a relatively simple way, deriving a single new signal, which it sends out through its single <strong>axon</strong>. The axon branches out so that this single output signal can reach different cells.<br></p><p    ><br></p><p    >image source: <a href="http://www.sciencealert.com/scientists-build-an-artificial-neuron-that-fully-mimics-a-human-brain-cell"><strong class="blue">http://www.sciencealert.com/scientists-build-an-artificial-neuron-that-fully-mimics-a-human-brain-cell</strong></a><br></p><aside    ><br></aside><p    ></p>
            </figcaption>
       </section>





       <section id="slide-006">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-006" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0007.svg" class="slide-image" />

            <figcaption>
            <p    >These ideas needed to be radically simplified to work with computers of that age, but the basic idea was still there: multiple inputs, one output. Doing this yielded one of the first successful machine learning systems: the <strong>perceptron</strong>. This was the model we saw in action in the video in the the first lecture.<br></p><p    >The perceptron has a number of inputs, the <em>features</em> in modern parlance, each of which is multiplied by a <span class="orange">weight</span>. The result is summed, together with a <span class="blue">bias</span> parameter, and the sign of this result is used as the classification.<br></p><p    >Of course, we’ve seen this classifier already: it’s just our basic linear classifier. The training algorithm was a little different from gradient descent, but the basic principle was the same. <br></p><p    >Note that when we draw the perceptron this way, as a mini network, the <span class="blue">bias</span> can be represented as just another input that we fix to always be 1. This is called a <strong>bias node</strong>.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-007" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-007" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0008anim0.svg" data-images="32.Linear.key-stage-0008anim0.svg,32.Linear.key-stage-0008anim1.svg,32.Linear.key-stage-0008anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Of course the brain’s power does not come from the fact that a single neuron is such a powerful mechanism by itself: it’s the<em> composition</em> of many simple parts that allows it to do what it does. We make the output of one neuron the input of another, and build networks of billions of neurons.<br></p><p    >And this is where the perceptron turns out to be too simple an abstraction. Because<strong> composing perceptrons doesn’t make them more powerful</strong>. Consider the graph on the left, with multiple perceptrons composed together.<br></p><p    >Writing down the function that this graph represents, we see that we get a simple function, with the first two perceptrons in brackets. If we then multiply out the brackets, we see that the result is a linear function. This means that we can represent this function also as a single perceptron with four inputs. This is always true. No matter how many perceptrons you chain together, the result will never be anything more than a simple linear function over your inputs: a single perceptron.<br></p><aside    >We’ve removed the bias node here for simplicity, but the conclusion is the same with a bias node included.<br></aside><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-008" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-008" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0009anim0.svg" data-images="32.Linear.key-stage-0009anim0.svg,32.Linear.key-stage-0009anim1.svg,32.Linear.key-stage-0009anim2.svg,32.Linear.key-stage-0009anim3.svg" class="slide-image" />

            <figcaption>
            <p    >To create perceptrons that we can chain together in such a way that the result will be more expressive than any single perceptron could be, the simplest trick is to include a<strong> non-linearity</strong>, also called an <strong>activation function</strong>.<br></p><p    >After all the weighted inputs have been combined, we pass the resulting scalar through a simple non-linear scalar function to produce the output. One popular option, especially in the early days of neural networks, was the<strong> logistic sigmoid</strong>, which we’ve seen already. Applying a sigmoid means that the sum of the inputs can range from negative infinity to positive infinity, but the output is always in the interval [0, 1]. <br></p><p    >Another, more recent non-linearity is the linear rectifier, or<strong> ReLU</strong> nonlinearity. This function just sets every negative input to zero, and keeps everything else the same.<br></p><p    >Not using an activation function is also called using a <strong>linear activation</strong>.<br></p><aside    >It's difficult to provide an intuition here for quite how these nonlinearities operate in the larger model. For now, the only point we want to make is that adding nonlinearities stops a network of perceptrons from collapsing into a single nonlinear function. We'll trust that these functions allow the network to learn some useful functions. We'll see a little more intuition in later lectures.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-009">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-009" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0010.svg" class="slide-image" />

            <figcaption>
            <p    >Using these nonlinearities, we can arrange single perceptrons into <strong>neural networks</strong>. Any arrangement of perceptrons makes a neural network, but for ease of training, this arrangement seen here was the most popular for a long time. It’s called the<strong> feedforward network </strong>or <strong>multilayer perceptron (MLP)</strong>. We arrange a layer of <strong>hidden units</strong> in the middle, each of which acts as a perceptron with a nonlinearity, connecting to all input nodes. Then we have one or more output nodes, connecting to all hidden units. Note the following points.<br></p><p     class="list-item">There are no cycles, the network feeds forward from input to output.<br></p><p     class="list-item">Nodes in the same layer are not connected to  each other, or to any other layer than the next and the previous one.<br></p><p     class="list-item">Each layer is<strong> fully connected</strong> to the previous layer, every node in one layer connects to every node in the layer before it.<br></p><p    >In the 80s and 90s these networks usually had just one hidden layer, because we hadn’t figured out how to train deeper networks. <br></p><aside    >Nowadays it's common to find feedforward networks with as many as 12 hidden layers, often used as part of a much larger network also employing different types of layers.<br></aside><p    >Note that every line in this picture represents one distinct parameter of the model. The <span class="blue">blue lines</span> (those connected to bias nodes) represent biases, and the rest represent <span class="orange">weights</span>.<br></p><p    >We can use networks like these to do classification or regression.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-010" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-010" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0011anim0.svg" data-images="32.Linear.key-stage-0011anim0.svg,32.Linear.key-stage-0011anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To build a <strong>regression model</strong>, all we need is one output node without an activation. This means that our network as a whole, describes a function from the feature space to the real number line.<br></p><p    >We can think of the first layer of our network as computing a <em>feature expansion</em>: the same thing we did in the fourth lecture to enable our linear regression to learn non-linear patterns, but this time, we don’t have to come up with the feature expansion ourselves, we simply learn it. The second layer is then just a linear regression in this expanded feature space.<br></p><p    >The number of hidden nodes is a hyperparameter. More nodes makes the network more powerful (that is, able to represent more different functions), but also more likely to overfit, more expensive to compute and potentially more difficult to train. The only real advice we can give is that whenever possible, your hidden layer should be wider than the input layer.<br></p><p    >After we've computed the output, we can apply any regression loss function we like, such as least-squares loss.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-011" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-011" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0012anim0.svg" data-images="32.Linear.key-stage-0012anim0.svg,32.Linear.key-stage-0012anim1.svg,32.Linear.key-stage-0012anim2.svg" class="slide-image" />

            <figcaption>
            <p    >To build a <strong>binary classifier</strong>, we could do what the perceptron did: use the <em>sign</em> of the output as the class. This would be a bit like using our least squares classifier from the second lecture, except with a feature expansion layer below it. <br></p><p    >These days, however, it’s much more common to take inspiration from the<em> logistic regression</em>. We apply the logistic sigmoid to the output and interpret the resulting value as the probability that the given input (x) is of the <span class="blue">positive class</span>. <br></p><p    >The logarithmic loss that we use for logistic regression, can then be applied here as well.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-012" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-012" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0013anim0.svg" data-images="32.Linear.key-stage-0013anim0.svg,32.Linear.key-stage-0013anim1.svg,32.Linear.key-stage-0013anim2.svg,32.Linear.key-stage-0013anim3.svg" class="slide-image" />

            <figcaption>
            <p    >For multiclass classification, we can use something called a <strong>softmax activation</strong>. We create a single output node for each class, and then ensure that <strong>they are all positive and that together they sum to one</strong>. This allows us to interpret them as <strong>class probabilities</strong>. <br></p><p    >The softmax function is one way to ensure this property. It simply passes each output node through the exponential function, to ensure that they are all positive, and then divides each by the sum total, to ensure that all outputs together sum to one.<br></p><p    >After the softmax we can interpret the value of node y<sub>3</sub> as the probability that <strong>x</strong> has class 3. Given these probabilities, we can apply a simple log loss: the aim is to maximize the logarithm of the probability of the true class. <br></p><aside    >The softmax is slightly unusual among activations in that it exchanges information between the nodes of the output layer. This allows us to look at just one output, and still provide a learning signal for all output nodes. For instance, imagine that the probability of class3 is low, but it should be high. This means that the value of y<sub>3</sub> should increase, but because the three nodes are required to sum to one, it automatically means that the values of y<sub>1</sub> and y<sub>2</sub> should decrease. We will see in the next video how this is achieved.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-013">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-013" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0014.svg" class="slide-image" />

            <figcaption>
            <p    >Because neural networks can be expensive to compute we tend to use <em>stochastic</em><strong> gradient descent</strong> to train them.<br></p><p    >Stochastic gradient descent is very similar to the gradient descent we’ve seen already, but we define the loss function over a<strong> single example</strong> instead of summing over the whole dataset: just use the same loss function, but pretend your data set consists of only one instance. We then loop over all instances, and perform a small gradient descent step for each one based on only the loss for that instance.<br></p><p    >Stochastic gradient descent has many advantages, including:<br></p><p     class="list-item">Using a new instance each time adds some noise to the process, since the gradient will be slightly different for each instance, which can help to escape local minima.<br></p><p     class="list-item">Gradient descent works fine if the gradient is not perfect, but still good on average (over many instances). This means that taking many small inaccurate steps is often much better than taking one very accurate big step. <br></p><p     class="list-item">Computing the loss over the whole dataset is expensive. By computing the loss over one instance at a time, we get N steps of stochastic gradient descent for the price of one step of regular gradient descent.<br></p><aside    >The most common approach these days is a compromise between stochastic and regular gradient descent, where we actually compute the loss for a small<strong> batch</strong> of instances (say 32 of them), and take a single step of gradient descent for each batch. This is called<strong> minibatch gradient descent,</strong> which we’ll look at more closely next lecture.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-014">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-014" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0015.svg" class="slide-image" />

            <figcaption>
            <p    >Apart from this exception, the training of a neural network proceeds in much the same way as the training of linear classifiers we've seen already.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-015">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-015" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0016.svg" class="slide-image" />

            <figcaption>
            <p    >Before we dig into the details, we can get a sense of what neural network training looks like in the <a href="http://playground.tensorflow.org/#activation=sigmoid&amp;batchSize=10&amp;dataset=circle&amp;regDataset=reg-plane&amp;learningRate=0.03&amp;regularizationRate=0&amp;noise=0&amp;networkShape=7&amp;seed=0.76686&amp;showTestData=false&amp;discretize=true&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=false&amp;xSquared=false&amp;ySquared=false&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=false&amp;problem=classification&amp;initZero=false&amp;hideText=false&amp;noise_hide=false&amp;activation_hide=false&amp;regularization_hide=true"><strong class="blue">tensorflow playground</strong></a>. We suggest you play around a bit with the different datasets,  different activations, and try to change the shape of the network.<br></p><p     class="list-item">Note how the shape of the decision boundary changes based on the activation functions we choose (curvy for sigmoid, piecewise linear for ReLU)<br></p><p     class="list-item">Note that adding another layer makes the network much more difficult to train (especially with sigmoid activations).<br></p><p     class="list-item">Try the linear activation (i.e. no activations on the hidden nodes). Note that all you get is a linear decision boundary, not matter how many layers you try.<br></p><p     class="list-item">Try a network on the circular dataset, with hidden layers with 2 units. It should not be possible so solve the circular dataset this way. It can be shown that to create a closed shape like a circle as a decision boundary, at least one hidden layer needs to be strictly bigger than your input layer.</p><p     class="list-item"></p>
            </figcaption>
       </section>





       <section id="slide-016">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-016" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0017.svg" class="slide-image" />

            <figcaption>
            <p    >That’s the basic idea of neural networks. So far, it’s hopefully a pretty simple idea. The complexity of neural networks lies in computing the gradients. For such complex models, sitting down at the kitchen table with pen and paper, and working out a symbolic expression for the gradient is no longer feasible. If we manage it at all, we get horrible convoluted expressions that no longer reduce to nice, simple functions, as they did in the case of linear regression and logistic regression.<br></p><p    >To help us out, we need the <strong>backpropagation</strong> algorithm, which we’ll discuss in the next video.</p><p    ></p>
            </figcaption>
       </section>




       <section class="video" id="video-016">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-16">link here</a>
           <iframe
                src="https://www.youtube.com/embed/IZ4w-aG50nU"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-017">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-017" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0018.svg" class="slide-image" />

            <figcaption>
            <p    ><br><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-018">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-018" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0019.svg" class="slide-image" />

            <figcaption>
            <p    >In the last video, we saw what the structure of a very basic neural network was, and we ended on this question. <strong>How do we work out the gradient?</strong><br></p><p    >For neural networks, the gradients quickly get too complex to work out by hand, so we need to automate this process.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-019" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-019" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0020anim0.svg" data-images="32.Linear.key-stage-0020anim0.svg,32.Linear.key-stage-0020anim1.svg,32.Linear.key-stage-0020anim2.svg,32.Linear.key-stage-0020anim3.svg,32.Linear.key-stage-0020anim4.svg,32.Linear.key-stage-0020anim5.svg" class="slide-image" />

            <figcaption>
            <p    >There are three basic flavors of working out derivatives and gradients automatically.<br></p><p    >The first is to do it<strong> symbolically</strong>, What we do on pen and paper, when we work out a derivative, is a pretty mechanical process. It’s not too difficult to program this process out and let the computer do it for us. This, is what happens, when you as Wolfram alpha to work out a derivative, for instance. It has its uses, cartainly, but it won;t work for us. The symbolic expression of the gradient of a function grows exponentiall with the complexity of the original function. That means that as we build bigger and bigger networks the expression of the gradient would soon grow too big to store in memory, let alone to compute.<br></p><p    >An alternative approach is to forget the symbolic form of the function, and just <strong>estimate the gradien</strong>t for a specific input <strong>x</strong>. We could, for instance, pick some points close to <strong>x</strong> and and fit a hyperplane through the outputs. This would be a pretty good approximation of the tangent hyperplane, so we could just read out the gradient. The problem is that this is a pretty unstable business. It’s quite difficult to be sure that the answer is accurate. It’s also expensive: the more dimensions in your model space, the more points you need to get an accurate estimate of your gradient, and each point requires you to recompute your model for a new input.<br></p><p    ><strong>Backpropagation</strong> is a middle ground: it does part of the work symbolically, and part of the work numerically. We get a very accurate computation of the gradient, and the cost of computation is usually only twice as expensive as computing the output for one input.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-020">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-020" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0022.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s the three steps required to implement backpropagation for a given function.<br></p><aside    >Don't worry if this seems abstract, it should become clearer when we look at an example.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-021" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-021" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0023anim0.svg" data-images="32.Linear.key-stage-0023anim0.svg,32.Linear.key-stage-0023anim1.svg,32.Linear.key-stage-0023anim2.svg,32.Linear.key-stage-0023anim3.svg" class="slide-image" />

            <figcaption>
            <p    >To show that backpropagation is a<em> generic </em>algorithm for working out gradients, not just a method for neural networks, we’ll first show how it works for some arbitrary scalar function: f(x) = 2/sin(e<sup>-x</sup>).<br></p><aside    >There is no special meaning to this function. I just chained together a few operations for which the derivatives are simple.<br></aside><p    >First we take our function f, and we break it up into a chain of smaller functions, the output of each feeding into the next. Defining the functions <span>a</span>, <span>b</span>, <span>c</span>, and <span>d</span> as shown, we can write f(<span class="blue">x</span>) = <span class="orange">d</span>(<span class="orange">c</span>(<span>b</span>(<span class="green">a</span>(<span class="blue">x</span>)))). <br></p><p    >The graph on the right is a called a <strong>computation graph</strong>: each node represents a small computer program that receives an input, computes an output and passes it on to another module.<br></p><aside    >Normally, we wouldn’t break a function up in such small modules: this is just a simple example to illustrate the principle.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-022" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-022" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0024anim0.svg" data-images="32.Linear.key-stage-0024anim0.svg,32.Linear.key-stage-0024anim1.svg,32.Linear.key-stage-0024anim2.svg,32.Linear.key-stage-0024anim3.svg,32.Linear.key-stage-0024anim4.svg,32.Linear.key-stage-0024anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Because we’ve described our function as a composition of modules, we can work out the derivative purely by repeatedly applying the chain rule.<br></p><aside    >Since we know for each function what the argument is, we’ll leave the arguments out to keep the notation clean.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-023" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-023" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0025anim0.svg" data-images="32.Linear.key-stage-0025anim0.svg,32.Linear.key-stage-0025anim1.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll call the derivative of the whole function with respect to input x the <strong class="blue">global derivative</strong>, and the derivative of each module with respect to its input we will call a<strong class="orange"> local derivative</strong>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-024" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-024" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0026anim0.svg" data-images="32.Linear.key-stage-0026anim0.svg,32.Linear.key-stage-0026anim1.svg,32.Linear.key-stage-0026anim2.svg,32.Linear.key-stage-0026anim3.svg,32.Linear.key-stage-0026anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The next step is to work out the local derivatives symbolically, using the rules we know. <br></p><p    >The difference from what we normally do is that <strong>we stop</strong> when we have the derivatives of the output of a module in terms of the input. For instance, the derivative <span>∂</span><span class="orange">c</span>/ <span>∂</span><span>b</span> is cos <span>b</span>. Normally, we would fill in the definition of <span>b</span> and see if we could simplify any further. Here we stop once we know the derivative in terms of <span>b</span>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-025" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-025" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0027anim0.svg" data-images="32.Linear.key-stage-0027anim0.svg,32.Linear.key-stage-0027anim1.svg,32.Linear.key-stage-0027anim2.svg,32.Linear.key-stage-0027anim3.svg,32.Linear.key-stage-0027anim4.svg,32.Linear.key-stage-0027anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Then, once all the local derivatives are known, in symbolic form, we switch to <strong>numeric computation</strong>. We will take a <em>specific</em> input, in this case -4.499 and compute the gradient only for that.<br></p><p    >First we compute the output of the function f given this input. We do this simply by following the computation graph: the input is fed to the first module, and its output is fed to the second module, and so on. This is known as the <strong>forward pass</strong>. During our computation, we also retain our intermediate values <span class="green">a</span>, <span>b</span>, <span class="orange">c</span> and <span class="red">d</span>. These will be useful later on.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-026" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-026" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0028anim0.svg" data-images="32.Linear.key-stage-0028anim0.svg,32.Linear.key-stage-0028anim1.svg,32.Linear.key-stage-0028anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Next up is the <strong>backward pass</strong>. We take the chain-rule derived form of the derivative, and we fill in the intermediate values <span>a</span>, <span>b</span>, <span>c</span> and <span>d</span>. <br></p><p    >This gives us a function with no variables, so we can compute the output. The result is that the derivative of this function, for the specific input -4.499, is 0.<br></p><p    >Note that we have stopped doing symbolic computations: we fill in the numeric values and work out the numeric result (accepting a small amount of inaccuracy due to floating point imprecisions).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-027">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-027" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0029.svg" class="slide-image" />

            <figcaption>
            <p    >If you're still struggling to see the difference between these three options, consider whether the answer you get is specific to a particular input x, or whether you get an answer that applies to the variable x, regardless of its value.<br></p><p    >When we worked out the gradient for least squares regression or for logistic regression, the result was not specific to a particular input. We didn't get a specific vector filled with numbers, we got a symbolic function that told us how to compute the gradient for <em>any</em> model and dataset. In short, if you can do it without knowing what the specific numbers of the input are, it's symbolic computation.<br></p><p    >With numeric computation, you don't get this function. You specify the particular dataset and the current model, and you get an estimate of the gradient as a single vector filled with specific numbers. If you change the model or the dataset, you have to do the whole gradient estimation again. If you need to know the specific numbers of the input before you can start, it's numeric computation.<br></p><p    >Backpropagation is, as we've said a middle ground. It works out the derivatives of the modules with respect to their inputs symbolically. You can do this without knowing the specific input we want the gradient for, so this part is symbolic. We then switch to numeric computation. This part can only start if we know the specific input we are computing the gradient for, so this part is numeric.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-028">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-028" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0030.svg" class="slide-image" />

            <figcaption>
            <p    >More fine-grained modules make the local derivatives easier to work out, but may increase the numeric instability. Less fine grained modules usually result in more accurate gradients, but if we make them too big, we end up with the problem that the symbolic expression of the gradient grows too complex.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-029" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-029" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0031anim0.svg" data-images="32.Linear.key-stage-0031anim0.svg,32.Linear.key-stage-0031anim1.svg,32.Linear.key-stage-0031anim2.svg,32.Linear.key-stage-0031anim3.svg,32.Linear.key-stage-0031anim4.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s now see how this works for a neural net. <br></p><p    >It’s important to remember that we <em>don’t</em> care about the derivative of the output y with respect tot he inputs  <strong>x</strong>. The function we’re computing the gradient for is <em>the loss</em>, and the variables we want to compute the gradient for are the <em>parameters </em>of the network. <strong>x</strong> does end up in our computation, because it’s part of the loss, but only as a constant.<br></p><p    >We'll work out what the gradient descent update will look like for the weights in the first and second layer.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-030" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-030" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0032anim0.svg" data-images="32.Linear.key-stage-0032anim0.svg,32.Linear.key-stage-0032anim1.svg,32.Linear.key-stage-0032anim2.svg,32.Linear.key-stage-0032anim3.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s what the local gradients look like for the weight <span class="orange">v</span><sub class="orange">2</sub>. <br></p><p    >The line on the bottom shows how we update <span class="orange">v</span><sub class="orange">2 </sub>when we apply a single step of stochastic gradient descent for x (x may not appear in the gradient, but the values y and h2 were computed using x).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-031">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-031" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0033.png" class="slide-image" />

            <figcaption>
            <p    >To see what this update rule means, we can use an analogy. Think of the neural network as a hierarchical structure like a government trying to make a decision. The output node is the prime minister: he provides the final decision (for instance what the tax on cigarettes should be). <br></p><p    >To make this decision, he listens to his ministers. His ministers don’t tell him what to do, they just shout. The louder they shout, the higher they want him to make the output.<br></p><p    >If he trusts a particular minister, he will <span class="orange">weigh</span> their advice positively, and follow their advice. If he distrusts the minister, he will do the opposite of what the minister says. The ministers each listen to a bank of civil servants and weigh their opinions in the same way the prime minister weight theirs. All ministers listen to the same civil servants, but they have their own <span class="orange">level of trust</span> for each.<br></p><aside    >We haven’t drawn the bias, but you can think of the bias as the prime minister’s own opinion; how strong the opinions of the ministers need to be to change his mind.<br></aside><p    ><br></p><p    >image sources: <a href="https://www.government.nl/government/members-of-cabinet/mark-rutte"><strong class="blue">https://www.government.nl/government/members-of-cabinet/mark-rutte</strong></a>, <a href="https://www.government.nl/government/members-of-cabinet/ingrid-van-engelshoven"><strong class="blue">https://www.government.nl/government/members-of-cabinet/ingrid-van-engelshoven</strong></a>, <a href="https://www.rijksoverheid.nl/regering/bewindspersonen/kajsa-ollongren"><strong class="blue">https://www.rijksoverheid.nl/regering/bewindspersonen/kajsa-ollongren</strong></a><br></p><p    >Door Photo: Yordan Simeonov (EU2018BG) - Dit bestand is afgeleid van: Informal JHA meeting (Justice) Arrivals (26031834658).jpg, CC BY-SA 2.0, <a href="https://commons.wikimedia.org/w/index.php?curid=70324317"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=70324317</strong></a><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-032">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-032" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0034.png" class="slide-image" />

            <figcaption>
            <p    >So let’s say the network has produced an output. The prime minister has set a tax on cigarettes <span class="red">y</span>, and based on the consequences realises that he should actually have set a tax of t. He’s now going to adjust his level of trust in each of his subordinates.<br></p><p    >Looking at the update rule for weight <span class="orange">v</span><sub class="orange">2</sub>, we can see that he takes two things into account: the error (<span class="red">y</span>-t), how wrong he was, and what minister<span> h</span><sub>2</sub> told him to do.<br></p><p     class="list-item">If  the error is positive, he set <span class="red">y</span> too high. If <span>h</span><sub>2</sub> shouted loudly, he will lower his trust in her. <br></p><p     class="list-item">If the error is negative, he set <span class="red">y</span> too low. If <span>h</span><sub>2</sub> shouted loudly, he will increase his trust in her. <br></p><p    >If we use a sigmoid activation, the ministers can only provide values between 0 and 1. If we use an activation that allows h2 to be negative, we see that the minister takes the sign into account: if h2 was negative and the error was negative too, the trust in the minister increases (because the PM should’ve listened to her).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-033">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-033" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0035.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-034" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-034" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0036anim0.svg" data-images="32.Linear.key-stage-0036anim0.svg,32.Linear.key-stage-0036anim1.svg,32.Linear.key-stage-0036anim2.svg,32.Linear.key-stage-0036anim3.svg,32.Linear.key-stage-0036anim4.svg,32.Linear.key-stage-0036anim5.svg,32.Linear.key-stage-0036anim6.svg" class="slide-image" />

            <figcaption>
            <p    >So far, this is no different from gradient descent on a linear model. The real power of the backpropagation algorithm shows when we look at how the error propagates back down the network (hence the name) and is used to update the weights. Lets look at the derivative for weight w12</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-035" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-035" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0037anim0.png" data-images="32.Linear.key-stage-0037anim0.png,32.Linear.key-stage-0037anim1.png,32.Linear.key-stage-0037anim2.png,32.Linear.key-stage-0037anim3.png" class="slide-image" />

            <figcaption>
            <p    >To see how much minister <span>h</span><sub>2</sub> needs to adjust her trust in x<sub>1</sub>, she first looks at the <em>global error</em>. To see how much she contributed to that global error, and whether she contributed negatively or positively, she multiplies by <span>v</span><sub>2</sub>, her level of influence over the decision. Then she looks at how much the input from all her subordinates influenced the decision, considering the activation function (that is, if the input was very high, she’ll need a bigger adjustment to make a meaningful difference). Finally she multiplies by x<sub>1</sub>, to isolate the effect that we trust in x<sub>1</sub> had on her decision.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-036">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-036" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0038.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-037">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-037" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >These weren’t just reasons not to use neural nets in production. They also slowed down the research on neural nets. SVM researchers were (probably) able to more faster, because once they’d designed a kernel, they could compute the optimal model performance and know, without ambiguity, whether it worked or not. Neural net researchers could design an architecture and spend months tuning the training algorithm without ever knowing whether the architecture would eventually perform.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-038" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-038" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0040anim0.svg" data-images="32.Linear.key-stage-0040anim0.svg,32.Linear.key-stage-0040anim1.svg,32.Linear.key-stage-0040anim2.svg,32.Linear.key-stage-0040anim3.svg,32.Linear.key-stage-0040anim4.svg,32.Linear.key-stage-0040anim5.svg" class="slide-image" />

            <figcaption>
            <p    >One important part of building such a framework is to recognise that all of this can easily be described as matrix multiplication/addition, together with the occasional element-wise non-linear operation. This allows us to write down the operation of a neural network very elegantly. <br></p><p    >In order to make proper use of this, we should also work out how to do the backpropagation part in terms of matrix multiplications. That’s where we’ll pick up next week in the first <strong>deep learning</strong> lecture.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>




       <section class="video" id="video-038">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-38">link here</a>
           <iframe
                src="https://www.youtube.com/embed/-PvsRdlISls"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-039">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-039" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0041.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-040">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-040" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0042.svg" class="slide-image" />

            <figcaption>
            <p    >In lecture 5, we introduced the logistic regression model, with the logarithmic loss. We saw that it performed very well, but it had one problem: when the data are very well separable, it didn’t have any basis to choose between two models like this: both separate the training data very well. Yet, they’re very different models.<br></p><p    >There are some tricks we can add to the logistic regression to deal with this problem, but today we'll look at a loss function that takes this problem as its starting point: the maximum margin hyperplane classifier.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-041" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-041" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0043anim0.svg" data-images="32.Linear.key-stage-0043anim0.svg,32.Linear.key-stage-0043anim1.svg,32.Linear.key-stage-0043anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Here is an extreme example of the problem. We have two linearly separable classes and a <span class="orange">decision boundary</span> that separates the data perfectly. And yet, if I see a new instance that is very similar to the rightmost <span class="red">red diamond</span>, but with a slightly higher x<sub>1</sub> value, it is suddenly classified as a<span class="blue"> blue disc</span>.<br></p><p    >This illustrates the intuition behind the loss function we will introduce in this video. <strong>If we see new points</strong><em> near</em><strong> our existing points, they should be classified the same as the existing points. </strong>One way to accomplish this is to look at the distance from the <span class="orange">decision boundary</span> to the nearest <span class="red">red</span> diamond and <span class="blue">blue</span> disc, and to <em>maximize</em> that.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-042">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-042" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0044.svg" class="slide-image" />

            <figcaption>
            <p    >What we are looking for is the hyperplane that separates the classes and has a maximal distance to the nearest <span class="blue">positive point </span>and nearest <span class="red">negative point</span>. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-043">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-043" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0045.svg" class="slide-image" />

            <figcaption>
            <p    >We measure the distance m at a right angle to the decision boundary. For the <span class="blue">positive</span> class, there is only one point nearest the margin, but for the <span class="red">negative </span>class, there are two the same distance away.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-044">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-044" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0046.svg" class="slide-image" />

            <figcaption>
            <p    >The points closest to the decision boundary are called the <strong>support vectors</strong>. This name comes from the fact that the support vectors alone, are enough to describe the model. If I give you the support vectors, you can work out the hyperplane without seeing the rest of the data.<strong><br></strong></p><p    >The distance to the support vectors is called the <strong>margin</strong>. We’ll assume that the decision boundary is chosen so that the margin is the same on both sides.<br></p><aside    >Or, alternatively, you can imagine we are drawing parallel lines through the support vectors, and putting the decision boundary halfway between these lines.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-045">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-045" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    >This idea goes by many names. These all mean the same thing, but they are used in different contexts. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-046">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-046" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0048.svg" class="slide-image" />

            <figcaption>
            <p    >So, given a dataset, how do we work out which hyperplane maximizes the margin? <br></p><p    >This is a tricky problem, because the support vectors aren’t <em>fixed</em>. If we move the hyperplane around to maximize the distance to one set of support vectors, we may move too close to other points, making <em>them</em> the support vectors. <br></p><p    >Surprisingly, there is a way to phrase the maximum margin hyperplane objective as a relatively simple optimization problem.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-047" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-047" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0049anim0.svg" data-images="32.Linear.key-stage-0049anim0.svg,32.Linear.key-stage-0049anim1.svg,32.Linear.key-stage-0049anim2.svg,32.Linear.key-stage-0049anim3.svg" class="slide-image" />

            <figcaption>
            <p    >To work this out, let’s first review how we use a hyperplane to define a linear decision boundary. Here is the 1D case. We have a single feature and we first define a linear function from the feature space to a scalar y. <br></p><p    >If the function is positive we assign the positive class, if it is negative, we assign the negative class. Where this function is equal to 0, where it “intersects” the feature space, is the decision boundary (which in this case is just a single point).<br></p><p    >Note that by defining the decision boundary this way, we have given ourselves an extra degree of freedom: the same decision boundary can be defined by infinitely many hyperplanes. We’ll use this extra degree to help us define a single hyperplane to optimize.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-048">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-048" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0050.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s the picture for a two dimensional feature space. The decision boundary is the<span class="orange"> dotted line</span> where the hyperplane intersects the (x<sub>1</sub>, x<sub>2</sub>) plane. If we rotate the hyperplane about that dotted line, we get a <em>different</em>  hyperplane defining<em> the same</em> decision boundary.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-049" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-049" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0051anim0.svg" data-images="32.Linear.key-stage-0051anim0.svg,32.Linear.key-stage-0051anim1.svg,32.Linear.key-stage-0051anim2.svg,32.Linear.key-stage-0051anim3.svg,32.Linear.key-stage-0051anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The hyperplane <span>h</span> we will choose is the one that produces y=1 for the positive support vectors and y=-1 for the negative support vectors. Or rather, we will<em> define</em> the support vectors as those points for which the line produces 1 and -1.<br></p><aside    >There's no guarantee that this happens at points that are in the dataset, but we will see later that this must be the case for an optimal choice of <span class="orange">h</span>.<br></aside><p    >For all other negative points, <span>h</span> should produce values below -1 and for all other positive points, <span>h</span> should produce values <em>above</em> 1.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-050">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-050" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0052.svg" class="slide-image" />

            <figcaption>
            <p    >This is the picture we want to end up with in 2 dimensions. The linear function evaluates to -1 for the <span class="red">negative support vectors</span>, and to a lower value for all other negative points. It evaluates to 1 for the <span class="blue">positive support vectors</span> and to a higher value for all other positive points.<br></p><p    >The trick we use to achieve this is to optimize<strong> with a constraint</strong>. We first define the margin as the distance from the decision boundary, where <span class="orange">h</span> evaluates to zero, to the line where <span class="orange">h</span> evaluates to 1, and on the other side to the line where h evaluates to -1. Then we set the constraint that all points should be on the correct side of their respective margins.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-051">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-051" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0053.svg" class="slide-image" />

            <figcaption>
            <p    >Here is our objective, written as precisely as we can manage at the moment. We will make this more precise as we move on.<br></p><p    >The quantity that we want to maximize is "2 times the margin": the width of the band separating the negative from the positive support vectors (between the two dotted lines in the previous slide).<br></p><p    >The constraints define the support vectors: all positive points should evaluate to 1 or higher. All negative points should evaluate to -1 or lower. Note that if we have N instances in our data, this gives us a problem with N constraints.<br></p><p    ><strong>Note that this automatically ensures that the support vectors end up at -1 and 1.</strong> Why?</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-052">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-052" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a picture of a case where all negative points are strictly less than -1, and all positive points are strictly larger than 1. The constraints are satisfied, but there are no points on the edges of the margin: we have no support vectors.<br></p><p    >In this case, we can easily make the margin bigger, pushing it out to coincide with the nearest points. Therefore, we have not hit the maximum yet. This is not an optimal solution to our optimization problem.<br></p><p    >Thus, any hyperplane with a maximal margin, that satisfies the constraints. must have points on the edges of its margin. These points are the support vectors.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-053">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-053" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0055.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the picture in 3D. Just like the hyperplane crosses the plane where y=0 to make the decision boundary, it crosses the y=1 plane to make the <span class="blue">positive margin</span>, and it crosses the y=-1 plane to make the <span class="red">negative margin</span>. <br></p><p    >Imagine finding a hyperplane that separates the classes, and then angling it so that he margins hit the nearest points.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-054" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-054" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0056anim0.svg" data-images="32.Linear.key-stage-0056anim0.svg,32.Linear.key-stage-0056anim1.svg,32.Linear.key-stage-0056anim2.svg,32.Linear.key-stage-0056anim3.svg,32.Linear.key-stage-0056anim4.svg,32.Linear.key-stage-0056anim5.svg,32.Linear.key-stage-0056anim6.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the picture for a single feature. We want to maximize the distance between the point where the hyperplane hits -1 and where it hits 1, while keeping the <span>negatives</span> below -1 and the <span>positives </span>above 1.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-055" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-055" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0057anim0.svg" data-images="32.Linear.key-stage-0057anim0.svg,32.Linear.key-stage-0057anim1.svg" class="slide-image" />

            <figcaption>
            <p    >So, how do we work this into a practical optimization objective that we can actually solve?<br></p><p    >The first thing we’ll do, is to simplify the two constraints for the two classes into a single constraint.<br></p><p    >We introduce  a label y<sub>i</sub> for each point x<sub>i</sub> which is -1 for <span class="red">negative points</span> and +1 for <span class="blue">positive points</span>. Multiplying the left-hand side of the constraint by y<sub>i</sub> keeps it the same for <span class="blue">positive points </span>and takes the negative for<span class="red"> negative points</span>. This means that in both case, the left hand side should now be larger than or equal to one. <br></p><aside    >This label y<sub>i</sub> is the same label we introduced to define the least squares loss, but now we're using it in a different way. Instead of trying to map each point to its label y<sub>i</sub>, we are fitting points to values <span class="blue">above</span> or <span class="red">below</span> y<sub>i</sub>.<br></aside><p    >We now have a problem with the same constraint for every instance in the data.<br></p><p    >Next, we need to make the phrase "<span class="orange">2x the size of the margin</span>" more precise. We know that our hyperplane, whichever hyperplane we choose, is defined by parameters <strong class="orange">w</strong> and <span class="blue">b</span>. Looking at the parameters of a particular hyperplane (good or bad), can we tell what the size of the margin is?</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-056">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-056" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0058.svg" class="slide-image" />

            <figcaption>
            <p    >First, let's recall what the parameters mean geometrically. Remember that in the equation <strong>w</strong><sup>T</sup><strong>x</strong> + <span>b</span>, <strong>w</strong> is the vector pointing orthogonally to the decision boundary. <span class="blue">b</span> is how high the hyperplane is at the origin.<br></p><aside    >Note that the hyperplane we have drawn here is not a solution to our problem, since it does not satisfy the constraints.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-057">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-057" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0059.svg" class="slide-image" />

            <figcaption>
            <p    >This is the value we’re interested in expressing. Twice the margin.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-058" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-058" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0060anim0.svg" data-images="32.Linear.key-stage-0060anim0.svg,32.Linear.key-stage-0060anim1.svg,32.Linear.key-stage-0060anim2.svg" class="slide-image" />

            <figcaption>
            <p    >To make the math easier, let’s move the axes around so that the lower dotted line (belonging to the negative support vectors) crosses the origin. Doing this doesn’t change the size of the margin.<br></p><p    >We can now imagine a vector from the origin to the <span class="blue">upper dotted line</span>, at a right angle. Call this vector <strong>a</strong>. The length of <strong>a</strong> is exactly the quantity we’re interested in.<br></p><p    >Remember also that the vector <strong>w</strong> points in the same direction as <strong>a</strong>, because both are perpendicular to the decision boundary.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-059" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-059" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0061anim0.svg" data-images="32.Linear.key-stage-0061anim0.svg,32.Linear.key-stage-0061anim1.svg,32.Linear.key-stage-0061anim2.svg,32.Linear.key-stage-0061anim3.svg" class="slide-image" />

            <figcaption>
            <p    >Because of the way we’ve moved the hyperplane, we know that the origin (<strong>0</strong>) hits the negative margin, so evaluates to -1. We also know that <strong class="orange">a</strong> hits the positive margin, so evaluates to +1.<br></p><p    >Subtracting the first from the second, we find that the dot product of <strong>a</strong> and <strong class="orange">w</strong> must be equal to two. <br></p><aside    >The dot product of anything with the zero vector is always 0.<br></aside><p    >Since <strong>a</strong> and <strong class="orange">w</strong> point in the same direction (cos α = 1), their dot product is just the product of their magnitudes (see the geometric definition of the dot product on the right).<br></p><p    >Re-arranging, we find that the length of <strong>a</strong> is 2 over that of <strong class="orange">w</strong>.<br></p><p    ><br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-060">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-060" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0062.svg" class="slide-image" />

            <figcaption>
            <p    >So, the thing we actually want to maximise is 2/||<strong class="orange">w</strong>||. This gives us a precise optimization objective.<br></p><p    >Note that almost all the complexity of the loss is in the constraints. Without them we could just let all elements of <strong class="orange">w</strong> go to zero However, the constraints require the output of our model to be larger than 1 for all positive points and smaller than -1 for all negative points. This will automatically push the margin up to the support vectors, but no further.<br></p><aside    >Consider what it would mean for the elements of <strong class="orange">w</strong> to go to zero. <strong class="orange">w</strong> is the gradient of our hyperplane. It points in the direction of steepest ascent, and its magnitude indicates how steep that ascent is. The smaller <strong class="orange">w</strong> is, the more flat the hyperplane lies. This is what the objective says: subject to the constraint that all points are on the correct side of their respective margins, we want a hyperplane that lies as flat as possible. If you think back to the 3D picture, you should be able to imagine how this ensures as wide a margin as possible.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-061">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-061" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0063.svg" class="slide-image" />

            <figcaption>
            <p    >Since we prefer to minimize instead of maximize, we take the inverse of this objective, and minimize that. The resulting classifier is called a “<strong>hard margin</strong>” <strong>support vector machine</strong> (SVM), since no points are allowed to violate the constraint and end up inside the margin.<br></p><aside    >In previous lectures we usually took the negative of the objective to turn maximization into minimization. In SVMs taking the inverse is more common, since the objective looks nicer this way.<br></aside><p    >The hard margin SVM is nice, but it doesn’t work well when:<br></p><p     class="list-item">We have data that is not linearly separable<br></p><p     class="list-item">We could have a very nice decision boundary if we just ignored a few misclassified points. For instance, when there is a little noise, or a few outliers.<br></p><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-062" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-062" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0064anim0.svg" data-images="32.Linear.key-stage-0064anim0.svg,32.Linear.key-stage-0064anim1.svg" class="slide-image" />

            <figcaption>
            <p    >A common alternative is to replace the norm of <strong class="orange">w</strong> by the dot product of <strong class="orange">w</strong> with itself. This is just a question of removing the square from the norm, so it doesn't change the location of the minimum. <br></p><aside    >This is because the square is a monotonic function: if the input gets bigger, the output gets bigger.<br></aside><p    >This form is easier to work with if we want to work out the gradient explicitly.<br></p><aside    >This objective is also sometimes written as <span>½||</span><strong class="orange">w</strong><span>||</span><sup>2</sup>, which means the same thing.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-063">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-063" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0065.svg" class="slide-image" />

            <figcaption>
            <p    >To deal with such situations, we can allow a <strong>soft margin</strong>. In a soft margin, we allow a few points to be on the wrong side of the margin, if it helps us achieve a better fit on the rest of the points. That is, we can trade off a few violations of the constraints against a bigger margin.<br></p><aside    >These points can even be on the wrong side of the decision boundary.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-064">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-064" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0066.svg" class="slide-image" />

            <figcaption>
            <p    >To achieve this, we introduce a <strong>slack parameter</strong> <span>p</span><sub>i</sub><span class="green"> </span>for each point <strong>x</strong><sub>i</sub>. This parameter indicates the extent to the constraint on <strong>x</strong><sub>i</sub> is <em>relaxed</em><strong>.</strong> Our learning algorithm can set <span class="green">p</span><sub class="green">i</sub> to whatever it likes. If it sets <span>p</span><sub>i</sub> to zero, the constraint is the same as it was for the hard margin classifier. If it sets <span>p</span><sub>i</sub> higher than zero, the constraint is relaxed and the point <strong>x</strong><sub>i</sub> can fall inside the margin. <br></p><p    >The price we pay is that <span>p</span><sub>i</sub> is added to our minimization objective, so the value we reach there becomes higher if we use more nonzero slack parameters.<br></p><p    >Our search algorithm, which we will detail later, does the rest. It automatically makes the tradeoff between how much we want to violate the original constraints and how big we want the margin to be.<br></p><p    ><span class="red">C</span> is a hyperparameter, indicating how to balance the tradeoff.<br></p><aside    >The value of <span class="red">C</span> is positive, and we usually try values  on a logarithmic scale like 0.001, 0.01, 0.1, 1.0, 10 and 100. As <span class="red">C</span> goes to infinity, we recover the hard margin SVM, where violating the constraints is “infinitely bad” and this never happens.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-065" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-065" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0067anim0.svg" data-images="32.Linear.key-stage-0067anim0.svg,32.Linear.key-stage-0067anim1.svg,32.Linear.key-stage-0067anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what that looks like in 1D. The open points are the support vectors, and for each class, we have one point on the wrong side of the decision boundary, requiring us to pay the residual <span>p</span><sub>i</sub> as a penalty.<br></p><p    >So, the objective function has a penalty added to it, but without this penalty, we would not have been able to satisfy the objective at all, since the two classes are not separable<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-066">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-066" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0068.svg" class="slide-image" />

            <figcaption>
            <p    >However, even if the classes <em>are</em> linearly separable, it can be good to allow a little slack. <br></p><p    >Here, the two points that would be the support vectors of the hard margin objective leave a very narrow margin. By allowing a little slack, we can get a much wider margin that provides a decision boundary that may be more likely to generalise to unseen data. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-067">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-067" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0069.svg" class="slide-image" />

            <figcaption>
            <p    >So, now that we have made our objective precise, how do we find a good solution? We haven’t discussed constrained optimization much yet. It turns out, we don't necessarily <em>need </em>to use constrained optimization methods, although there is a benefit to using them. We'll look at both options.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-068" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-068" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0070anim0.svg" data-images="32.Linear.key-stage-0070anim0.svg,32.Linear.key-stage-0070anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The first oiption allows us to use the old familiar gradient descent, without having to worry about constraints. <br></p><p    >The other requires us to delve into constrained optimization, which we start to do in the next video. The payoff for that is that it opens the door to the <strong>kernel trick</strong>.<br></p><p    >In the rest of this video, we will work out option one.<br></p><p    >If you're in a hurry, and you just want to know the parts that are important for the course, you can skim the rest of this video and focus on the next two. </p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-069" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-069" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0071anim0.svg" data-images="32.Linear.key-stage-0071anim0.svg,32.Linear.key-stage-0071anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To get rid of the constraints, let’s look at what we know about the value of <span class="green">p</span><sub class="green">i</sub>.<br></p><p    >If the constraint for <strong>x</strong><sub>i</sub> is violated, we can see that <span class="green">p</span><sub class="green">i</sub> makes up the difference between what y<sup>i</sup>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sup>i</sup>+ <span class="blue">b</span>) should be (1) and what it is.<br></p><p    >If the constraint is not violated, <span class="green">p</span><sub class="green">i</sub> becomes zero, and the value we computed above becomes negative.<br></p><p    >We can summarise these two conclusions in a single definition for <span class="green">p</span><sub class="green">i</sub>:it is is 1 - y<sup>i</sup>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sup>i</sup>+ <span class="blue">b</span>) if the constraint is violated and 0 otherwise. This is equal to the value max(0, 1- y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>)) in both cases.<br></p><p    >Since this value is always equal to <span class="green">p</span><sub class="green">i</sub>, we can replace <span class="green">p</span><sub class="green">i</sub> by it everywhere it occurs in the optimization objective</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-070">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-070" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0072.svg" class="slide-image" />

            <figcaption>
            <p    >Doing this, we get a new objective function. <br></p><p    >The new constraints are now always true. For the second one, this is easy to see, since the maximum of 0 and something is always larger than or equal to 0. <br></p><p    >For the first, note that we worked out max(0, 1- y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>)) as how far below 1 the value y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) was. If we move it to the the other side, we get <br></p><p    >y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) + max(0, 1- y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>))<br></p><p    >which must therefore be exactly equal to 1 if y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) is below 1, or larger if y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) is larger than 1.<br></p><p    >Since the constraints are always true, we can remove them.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-071" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-071" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0073anim0.svg" data-images="32.Linear.key-stage-0073anim0.svg,32.Linear.key-stage-0073anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This gives us an <strong>unconstrained loss function</strong> we can directly apply to any model. For instance when training a neural network to classify, this makes a solid alternative to logarithmic loss. This is sometimes called the <strong>L1-SVM</strong> (loss). <br></p><aside    >There is also the L2-SVM loss where a square is applied to the <span class="green">p</span><sub class="green">i</sub> function, to increase the weight of outliers.<br></aside><p    >We can think of the first term as a<strong> regularizer</strong>. It doesn’t enforce anything about how well the plane should fit the data. It just ensures that the parameters of the plane don’t grow too big. We'll see more regularization in the next lecture, but this form, where we add the norm of the parameter vector to the loss function, is very common.<br></p><p    >The highlighted part of the second term functions as a kind of error (just as we used in least squares classification, but without the square). It computes how far the model output  y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) is away from the desired value (1). <br></p><p    >However, unlike the least squares classifier, we <em>only</em> compute this error for points that are sufficiently close to the decision boundary. For any points far from the boundary (i.e. outside the margin), we do not compute any error at all. This is achieved by cutting off any negative values. If the data is linearly separable, we could easily shrink the margin enough to make the error zero for all points, but this usually requires a <strong>w</strong> with a very high norm, so then the regulariser kicks in and start increasing so much that we prefer some points inside the margin.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-072">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-072" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0074.svg" class="slide-image" />

            <figcaption>
            <p    >And with that, we have discussed our final classification loss. Let’s review.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-073">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-073" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    >Here are all our loss functions in one handy slide.<br></p><p    >The <strong>error</strong>, also known as zero one loss, is imply the number or proportion of misclasssified examples. It’s usually what we’re interested in, but it doesn’t give us a loss surface that is suitable for searching.<br></p><p    >The<strong> least-squares loss</strong> we introduced as a simple illustration of the principle of a proxy loss for the error. In practice it doesn't usually work very well, and is rarely used.<br></p><p    >The <strong>log loss </strong>requires a sigmoid function to be added to the output of the linear function. It assumes that he result is the probability of the positive class applying to the instance, and it maximizes the log likelihood of the classes given the model parameters. Practically this boils down to minimizing the negative log likelihood of the correct class. This can also be derived from the cross-entropy between the true class distribution given by the data and the class distribution given by the model.<br></p><p    >Finally, the <strong>soft margin SVM loss</strong>, which we've introduced today attempts to maximize the margin between the positive and negative points. It's also know as a maximum margin loss, or the <strong>hinge loss</strong> (since the error is fed through a maximum function, which looks like a hinge).<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-074">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-074" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0076.svg" class="slide-image" />

            <figcaption>
            <p    >In this final part of the lecture, we will take a quick look at support vector machines that make use of the kernel trick. It’s not exam material, so you can skip it if you need to, but we recommend at least giving a skim, so that you have a broad idea what SVMs are in case you ever encounter them in the wild.<br></p><p    >We’re skipping a large amount of technical details in this part. If you really want to know how this works all the way down to the foundations, there is an extra lecture explaining them on the website.<br></p><p    >video| |</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-075">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-075" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0077.svg" class="slide-image" />

            <figcaption>
            <p    >In the previous video we introduced the maximum margin loss objective. This was a <strong>constrained optimization</strong> problem which we hadn't learned how to solve yet. We sidestepped that issue by rewriting it into an unconstrained optimization problem, so that we could solve it with plain gradient descent.<br></p><p    >In this video, we will learn a relatively simple trick for attacking constrained optimization problems: the method of <strong>Lagrange multipliers</strong>. In the next video, we will see what happens if we apply this method to the SVM objective function.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-076">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-076" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0078.svg" class="slide-image" />

            <figcaption>
            <p    >To avoid overloading this lecture, we will skip a lot of the technical details. We will give you a very high level view of what support vector machine can do. This should help you recognize what they are, and give you a sense of how they work, in case you ever need to apply them. <br></p><p    >If you ever need to understand them properly, all the technical details are available on the website in an extra lecture.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-077">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-077" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0079.svg" class="slide-image" />

            <figcaption>
            <p    >The key idea behind all this technical stuff is that we can rewrite our<em> maximum margin objective</em> from the previous slide into its<em> dual form</em>. This is what the KKT method does for us, it gives us a new minimization objective where some of the variables have disappeared. Under the right conditions, both objectives have the same solution.<br></p><p    >In return we also get some extra variables α<sub>i</sub>. You can think of these as weights, we get one for every instance <strong>x</strong><sub>i</sub>, y<sub>i</sub> in our data. The hyperplane parameters have disappeared and these αs are the only parameters of our problem now. <br></p><p    >There isn’t much more intuition we can give you. Without a whole lot of math, you’ll just have to take our word for it that these two problems are equivalent. We can find the optimal maxim-margin hyperplane loss using the problem at the top or the problem at the bottom.<br></p><p    >The reason this dual problem is so interesting is that the only thing we ever need to compute on our data <strong>is the dot product between every pair of instances in our data</strong>. That is, we don’t need the original features: if I give you all dot products between all pairs of instances in a dataset, you can fit an SVM to it without every seeing anything else of the data.<br></p><p    >This is the idea that leads to the <strong>kernel trick</strong>.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-078">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-078" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0080.svg" class="slide-image" />

            <figcaption>
            <p    >What if I didn’t give you the actual dot products, but instead gave you a different matrix of values, that <em>behaved </em>like a matrix of dot products.<br></p><p    >The idea is that it’s possible to design a high-dimensional feature space in such a way that that you can very cheaply compute dot products without ever having to compute the high dimensions vectors.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-079">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-079" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0081.png" class="slide-image" />

            <figcaption>
            <p    >Remember, by adding features that are derived from the original features, we can make linear models more powerful. If the number of features we add grows very quickly (like if we add all 5-way cross products), this can becomes a little expensive (both memory and time wise).<br></p><p    >The kernel trick is basically a souped-up version of this idea. We expand our features into a high dimensional space, except we never actually compute the feature expansion. We just compute the dot products in the expanded feature space directly.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-080">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-080" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0082.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s a plot for the dataset from the first lecture. As you can tell, the RBF kernel massively overfits for these hyperparameters, but it does give us a very nonlinear fit.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-081">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-081" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0083.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s look at an example. The simplest way we saw to extend the feature space was to add <strong>all cross-products</strong>. This turns a 2D dataset into a 5D dataset. It also more than doubles the amount of data we need to store our dataset, and the amount of time required to, for instance, compute a dot product in this space.<br></p><aside    >This is not usually a bottleneck, but we want to expand this idea to thousands or even millions of extra features.<br></aside><p    >Again, to fit an SVM, all we need is the dot products between pairs of instances in this 5D space. Let’s see if we can compute those, or something similar, without explicitly computing the 5D vectors.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-082" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-082" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0084anim0.svg" data-images="32.Linear.key-stage-0084anim0.svg,32.Linear.key-stage-0084anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here are two 2D feature vectors. What if, instead of computing their dot product, we computed the <em>square</em> of their dot product. <br></p><p    >It turns out that this is equal to the dot product of two other <em>3</em>D vectors <strong>a’</strong> and <strong>b’</strong>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-083" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-083" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0085anim0.svg" data-images="32.Linear.key-stage-0085anim0.svg,32.Linear.key-stage-0085anim1.svg,32.Linear.key-stage-0085anim2.svg,32.Linear.key-stage-0085anim3.svg,32.Linear.key-stage-0085anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The square of the dot product in the 2D feature space, is equivalent to the regular dot product in a 3D feature space. The new features in this 3D space can all be derived from the original features. They're the three cross products, with a small multiplier on the a<sub>1</sub>a<sub>2</sub> cross product.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-084" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-084" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0086anim0.svg" data-images="32.Linear.key-stage-0086anim0.svg,32.Linear.key-stage-0086anim1.svg,32.Linear.key-stage-0086anim2.svg,32.Linear.key-stage-0086anim3.svg" class="slide-image" />

            <figcaption>
            <p    >That is, this kernel function <span class="orange">k</span> doesn't compute the dot product between two instances, but it does compute the dot product in a feature space of <em>expanded</em> features. We could do this already, but before we had to actually <em>compute</em> the new features. <strong>Now, all we have to do is compute the dot product in the original feature space and square it.</strong></p><p    ><strong></strong></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-085">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-085" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0087.svg" class="slide-image" />

            <figcaption>
            <p    >Since the dual solution to the SVM is expressed purely in terms of the dot product, we can replace the dot product this <span class="orange">kernel function</span>. We are now fitting a line in a higher-dimensional space, without computing any extra features explicitly.<br></p><p    >Note that this only works because we rewrote the optimization objective to get rid of <strong class="orange">w</strong> and<span class="blue"> b</span>. Since <strong class="orange">w</strong> and<span class="blue"> b</span> have the same dimensionality as the features, keeping them in means using explicit features.<br></p><p    >Saving the trouble of computing a few extra features may not sound like a big saving, but by choosing our kernel function cleverly we can push things a lot further.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-086">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-086" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0088.svg" class="slide-image" />

            <figcaption>
            <p    >For some expansions to a higher feature space, we can compute the dot product between two vectors, <strong>without explicitly expanding the features</strong>. This is called a <strong>kernel function</strong>.<br></p><p    >There are many functions that compute the dot product of two vectors in a highly expanded feature space, but don’t actually require you to expand the features.<br></p><aside    >There are some straightforward conditions for when a given function of two vectors is a kernel. We won't worry about that now, and just look at some commonly used kernels, assuming that others have done the work to show that these actually are kernels.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-087">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-087" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0089.svg" class="slide-image" />

            <figcaption>
            <p    >Taking just the square of the dot product, as we did in our example, we lose the original features. If we take the square of the dot product<strong> plus one</strong>, it turns out that we retain the original features, <em>and</em> get all cross products. <br></p><aside    >You'll show how this works in the homework.<br></aside><p    >If we increase the exponent to <span class="red">d</span> we get all <span class="red">d</span>-way cross products. Here we can see the benefit of the kernel trick. Imagine setting <span class="red">d</span>=10 for a dataset with a modest 10 features. Expanding all 10-way cross-products of all features would give each instance<em> 10 trillion</em> expanded features. We wouldn't even be able to fit one instance into memory.<br></p><p    >However, if we use the kernel trick, all we need to do is to compute the dot product in the original feature space, add a 1, and raise it to the power of 10.<br></p><aside    ><span class="red">d</span> is a hyperparameter: increasing it does not make the algorithm much more expensive, but it does increase your (implicit) feature space so much that you risk overfitting, so you'll need to tune it to your data.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-088" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-088" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0090anim0.svg" data-images="32.Linear.key-stage-0090anim0.svg,32.Linear.key-stage-0090anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If ten trillion expanded features sounded like a lot, here is a kernel that corresponds to an infinite-dimensional expanded feature space. We can only approximate this kernel with a finite number of expanded features, getting closer as we add more. Nevertheless, the kernel function itself is very simple to compute.<br></p><p    >Gamma is another hyperparameter.<br></p><p    >Because this is such a powerful kernel, it is prone to overfitting.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-089">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-089" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0091.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s a plot of the SVM decision boundary with a poly kernel and an RBF kernel, on some simple dataset.<br></p><p    >As you can tell, the RBF kernel massively overfits for these hyperparameters, but it does give us a very <em>nonlinear</em> fit.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-090">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-090" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0092.svg" class="slide-image" />

            <figcaption>
            <p    >One of the most interesting application areas of kernel methods is places where you can turn a distance metric in your data space directly into a kernel, <strong>without first extracting any features at all</strong>.<br></p><p    >For instance for an email classifier, you don't need to extract word frequencies, as we’ve done so far, you can just design a kernel that operates directly on strings (usually based on the edit distance).Put simply, the fewer operations we need to turn one email into another, the closer we put them together. If you make sure that such a function behaves like a dot product, you can stick it in the SVM optimizer as a kernel. <strong>You never need to deal with any features at all.</strong> Just the raw data, and their dot products in some feature space that you never compute.<br></p><aside    >This approach has often been used to analyze DNA and protein sequences in bioinformatics.<br></aside><p    >If you’re classifying graphs, there are distance metrics like the Weisfeiler-Lehman algorithm that you can use to define kernels.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-091">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-091" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0093.svg" class="slide-image" />

            <figcaption>
            <p    >Kernel SVMs are complicated beasts to understand, but they're easy to use with the right libraries. Here's a simple recipe for fitting an SVM with an RBF kernel in sklearn.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-092">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-092" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0094.svg" class="slide-image" />

            <figcaption>
            <p    >Neural nets require a lot of passes over the data, so it takes a big dataset before kN becomes smaller than N<sup>2</sup>, but eventually, we got there. At that point, it became more efficient to train models by gradient descent, and the kernel trick lost its luster.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-093">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-093" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0095.svg" class="slide-image" />

            <figcaption>
            <p    >And when neural networks did come back, they caused a revolution. That’s where we’ll pick things up next lecture.</p><p    ></p>
            </figcaption>
       </section>


</article>
