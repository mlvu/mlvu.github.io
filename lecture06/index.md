---
title: "Lecture 6: Beyond linear models"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 6: Beyond linear models</li>
                <li><a href="#video-000">Neural networks</a></li>
                <li><a href="#video-017">Backpropagation</a></li>
                <li><a href="#video-039">Support vector machines</a></li>
                <li><a href="#video-073">Lagrange multipliers</a></li>
                <li><a href="#video-105">The kernel trick</a></li>
                <li><a href="#slide-131">KKT conditions and the SVM dual*</a></li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/32.LinearModels2.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">


       <section class="video" id="video-000">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-0">link here</a>
           <iframe
                src="https://www.youtube.com/embed/DeQ4STHYT3g?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-001">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-001" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-002">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-002" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0002.png" class="slide-image" />

            <figcaption>
            <p    >This lecture is a little on the heavy side. We generally pack a lot into the lectures, but this is probably the most dense one in the series. This is mostly to make the story complete and self-contained. We've tried to indicate where you can skip parts to make it easier to get through the whole thing. The aim is to give you a general idea the first time around, but to also ensure that if you do ever find yourself needing to use kernel methods or Lagrange multipliers, you can come back to this lecture and work through the details.<br></p><p    >Don't worry if you don't understand all the details in the time you have. If you're struggling with this one, we recommend skimming everything quickly, and then trying the relevant homework exercise. This should tell you which parts to come back to.<br></p><p    >The following subjects may appear on the exam as application questions, so these are important to fully understand:<br></p><p     class="list-item">Backpropagation<br></p><p     class="list-item">Lagrange multipliers<br></p><p     class="list-item">The kernel trick <br></p><p    >Things like the unconstrained SVM loss and the derivation of the SVM dual objective are good to know but they won't be on the exam as application questions, so you can skip them if you're struggling to find the time to wrap your head around the whole lecture.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-003">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-003" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0003.png" class="slide-image" />

            <figcaption>
            <p    >A few lectures ago, we saw how we could make a linear model more powerful, and able to learn nonlinear decision boundaries by just <strong>expanding our features</strong>: we add new features derived from the old ones, and depending on which combinations we add, we can learn new, non-linear decision boundaries or regression functions.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-004">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-004" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0004.svg" class="slide-image" />

            <figcaption>
            <p    >Both models we will see today, <strong>neural networks </strong>and<strong> support vector machines</strong>, take this idea and build on it. Neural networks are a big family, but the simplest type, the <strong>two-layer feedforward network</strong>, functions as a feature extractor followed by a linear model. In this case, we don’t choose the extended features but we <em>learn</em> them, together with the weights of the linear model.<br></p><p    >The support vector machine doesn’t learn the expanded features (we still have to choose them manually), but it uses a<strong> kernel function</strong> to allow us to fit a linear model in a <em>very</em> high-dimensional feature without  having to pay for actually computing all these expanded features.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-005">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-005" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0005.svg" class="slide-image" />

            <figcaption>
            <p    >The layout of today’s lecture will be largely chronological. We will focus on <strong>neural networks</strong>, which were very popular in the late eighties and early nineties. <br></p><p    >Then, towards the end of the nineties, interest in neural networks died down a little and <strong>support vector machines</strong> became much more popular.<br></p><p    >In the next lecture, we’ll focus on Deep Learning, which sees neural networks make a comeback in a big way.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-006">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-006" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0006.svg" class="slide-image" />

            <figcaption>
            <p    >In this video, we’ll start with the basics of neural networks. <br></p><p    ><br></p><p    >In the very early days of AI (the late 1950s), researchers decided to try a simple approach: the brain is the only truly intelligent system we know, so let’s see what it’s made of, and whether that provides some inspiration for intelligent (and learning) computer systems.<br></p><p    ><br></p><p    >They started with a single brain cell: a neuron. A neuron receives multiple different input signals from other cells through connections called <strong>dendrites</strong>. It processes these in a relatively simple way, deriving a single new signal, which it sends out through its single <strong>axon</strong>. The axon branches out so that this single output signal can reach different cells.<br></p><p    ><br></p><p    >image source: <a href="http://www.sciencealert.com/scientists-build-an-artificial-neuron-that-fully-mimics-a-human-brain-cell"><strong class="blue">http://www.sciencealert.com/scientists-build-an-artificial-neuron-that-fully-mimics-a-human-brain-cell</strong></a><br></p><aside    ><br></aside><p    ></p>
            </figcaption>
       </section>





       <section id="slide-007">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-007" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0007.svg" class="slide-image" />

            <figcaption>
            <p    >These ideas needed to be radically simplified to work with computers of that age, but the basic idea was still there: multiple inputs, one output. Doing this yielded one of the first successful machine learning systems: the <strong>perceptron</strong>. This was the model we saw in action in the video in the the first lecture.<br></p><p    >The perceptron has a number of inputs, the <em>features</em> in modern parlance, each of which is multiplied by a <span class="orange">weight</span>. The result is summed, together with a <span class="blue">bias</span> parameter, and the sign of this result is used as the classification.<br></p><p    >Of course, we’ve seen this classifier already: it’s just our basic linear classifier. The training algorithm was a little different from gradient descent, but the basic principle was the same. <br></p><p    >Note that when we draw the perceptron this way, as a mini network, the <span class="blue">bias</span> can be represented as just another input that we fix to always be 1. This is called a <strong>bias node</strong>.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-008" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-008" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0008anim0.svg" data-images="32.Linear.key-stage-0008anim0.svg,32.Linear.key-stage-0008anim1.svg,32.Linear.key-stage-0008anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Of course the brain’s power does not come from the fact that a single neuron is such a powerful mechanism by itself: it’s the<em> composition</em> of many simple parts that allows it to do what it does. We make the output of one neuron the input of another, and build networks of billions of neurons.<br></p><p    >And this is where the perceptron turns out to be too simple an abstraction. Because<strong> composing perceptrons doesn’t make them more powerful</strong>. Consider the graph on the left, with multiple perceptrons composed together.<br></p><p    >Writing down the function that this graph represents, we see that we get a simple function, with the first two perceptrons in brackets. If we then multiply out the brackets, we see that the result is a linear function. This means that we can represent this function also as a single perceptron with four inputs. This is always true. No matter how many perceptrons you chain together, the result will never be anything more than a simple linear function over your inputs: a single perceptron.<br></p><aside    >We’ve removed the bias node here for simplicity, but the conclusion is the same with a bias node included.<br></aside><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-009" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-009" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0009anim0.svg" data-images="32.Linear.key-stage-0009anim0.svg,32.Linear.key-stage-0009anim1.svg,32.Linear.key-stage-0009anim2.svg,32.Linear.key-stage-0009anim3.svg" class="slide-image" />

            <figcaption>
            <p    >To create perceptrons that we can chain together in such a way that the result will be more expressive than any single perceptron could be, the simplest trick is to include a<strong> non-linearity</strong>, also called an <strong>activation function</strong>.<br></p><p    >After all the weighted inputs have been combined, we pass the resulting scalar through a simple non-linear scalar function to produce the output. One popular option, especially in the early days of neural networks, was the<strong> logistic sigmoid</strong>, which we’ve seen already. Applying a sigmoid means that the sum of the inputs can range from negative infinity to positive infinity, but the output is always in the interval [0, 1]. <br></p><p    >Another, more recent non-linearity is the linear rectifier, or<strong> ReLU</strong> nonlinearity. This function just sets every negative input to zero, and keeps everything else the same.<br></p><p    >Not using an activation function is also called using a <strong>linear activation</strong>.<br></p><aside    >It's difficult to provide an intuition here for quite how these nonlinearities operate in the larger model. For now, the only point we want to make is that adding nonlinearities stops a network of perceptrons from collapsing into a single nonlinear function. We'll trust that these functions allow the network to learn some useful functions. We'll see a little more intuition in later lectures.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-010">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-010" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0010.svg" class="slide-image" />

            <figcaption>
            <p    >Using these nonlinearities, we can arrange single perceptrons into <strong>neural networks</strong>. Any arrangement of perceptrons makes a neural network, but for ease of training, this arrangement seen here was the most popular for a long time. It’s called the<strong> feedforward network </strong>or <strong>multilayer perceptron (MLP)</strong>. We arrange a layer of <strong>hidden units</strong> in the middle, each of which acts as a perceptron with a nonlinearity, connecting to all input nodes. Then we have one or more output nodes, connecting to all hidden units. Note the following points.<br></p><p     class="list-item">There are no cycles, the network feeds forward from input to output.<br></p><p     class="list-item">Nodes in the same layer are not connected to  each other, or to any other layer than the next and the previous one.<br></p><p     class="list-item">Each layer is<strong> fully connected</strong> to the previous layer, every node in one layer connects to every node in the layer before it.<br></p><p    >In the 80s and 90s these networks usually had just one hidden layer, because we hadn’t figured out how to train deeper networks. <br></p><aside    >Nowadays it's common to find feedforward networks with as many as 12 hidden layers, often used as part of a much larger network also employing different types of layers.<br></aside><p    >Note that every line in this picture represents one distinct parameter of the model. The <span class="blue">blue lines</span> (those connected to bias nodes) represent biases, and the rest represent <span class="orange">weights</span>.<br></p><p    >We can use networks like these to do classification or regression.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-011" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-011" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0011anim0.svg" data-images="32.Linear.key-stage-0011anim0.svg,32.Linear.key-stage-0011anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To build a <strong>regression model</strong>, all we need is one output node without an activation. This means that our network as a whole, describes a function from the feature space to the real number line.<br></p><p    >We can think of the first layer of our network as computing a <em>feature expansion</em>: the same thing we did in the fourth lecture to enable our linear regression to learn non-linear patterns, but this time, we don’t have to come up with the feature expansion ourselves, we simply learn it. The second layer is then just a linear regression in this expanded feature space.<br></p><p    >The number of hidden nodes is a hyperparameter. More nodes makes the network more powerful (that is, able to represent more different functions), but also more likely to overfit, more expensive to compute and potentially more difficult to train. The only real advice we can give is that whenever possible, your hidden layer should be wider than the input layer.<br></p><p    >After we've computed the output, we can apply any regression loss function we like, such as least-squares loss.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-012" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-012" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0012anim0.svg" data-images="32.Linear.key-stage-0012anim0.svg,32.Linear.key-stage-0012anim1.svg,32.Linear.key-stage-0012anim2.svg" class="slide-image" />

            <figcaption>
            <p    >To build a <strong>binary classifier</strong>, we could do what the perceptron did: use the <em>sign</em> of the output as the class. This would be a bit like using our least squares classifier from the second lecture, except with a feature expansion layer below it. <br></p><p    >These days, however, it’s much more common to take inspiration from the<em> logistic regression</em>. We apply the logistic sigmoid to the output and interpret the resulting value as the probability that the given input (x) is of the <span class="blue">positive class</span>. <br></p><p    >The logarithmic loss that we use for logistic regression, can then be applied here as well.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-013" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-013" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0013anim0.svg" data-images="32.Linear.key-stage-0013anim0.svg,32.Linear.key-stage-0013anim1.svg,32.Linear.key-stage-0013anim2.svg,32.Linear.key-stage-0013anim3.svg" class="slide-image" />

            <figcaption>
            <p    >For multiclass classification, we can use something called a <strong>softmax activation</strong>. We create a single output node for each class, and then ensure that <strong>they are all positive and that together they sum to one</strong>. This allows us to interpret them as <strong>class probabilities</strong>. <br></p><p    >The softmax function is one way to ensure this property. It simply passes each output node through the exponential function, to ensure that they are all positive, and then divides each by the sum total, to ensure that all outputs together sum to one.<br></p><p    >After the softmax we can interpret the value of node y<sub>3</sub> as the probability that <strong>x</strong> has class 3. Given these probabilities, we can apply a simple log loss: the aim is to maximize the logarithm of the probability of the true class. <br></p><aside    >The softmax is slightly unusual among activations in that it exchanges information between the nodes of the output layer. This allows us to look at just one output, and still provide a learning signal for all output nodes. For instance, imagine that the probability of class3 is low, but it should be high. This means that the value of y<sub>3</sub> should increase, but because the three nodes are required to sum to one, it automatically means that the values of y<sub>1</sub> and y<sub>2</sub> should decrease. We will see in the next video how this is achieved.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-014">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-014" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0014.svg" class="slide-image" />

            <figcaption>
            <p    >Because neural networks can be expensive to compute we tend to use <em>stochastic</em><strong> gradient descent</strong> to train them.<br></p><p    >Stochastic gradient descent is very similar to the gradient descent we’ve seen already, but we define the loss function over a<strong> single example</strong> instead of summing over the whole dataset: just use the same loss function, but pretend your data set consists of only one instance. We then loop over all instances, and perform a small gradient descent step for each one based on only the loss for that instance.<br></p><p    >Stochastic gradient descent has many advantages, including:<br></p><p     class="list-item">Using a new instance each time adds some noise to the process, since the gradient will be slightly different for each instance, which can help to escape local minima.<br></p><p     class="list-item">Gradient descent works fine if the gradient is not perfect, but still good on average (over many instances). This means that taking many small inaccurate steps is often much better than taking one very accurate big step. <br></p><p     class="list-item">Computing the loss over the whole dataset is expensive. By computing the loss over one instance at a time, we get N steps of stochastic gradient descent for the price of one step of regular gradient descent.<br></p><aside    >The most common approach these days is a compromise between stochastic and regular gradient descent, where we actually compute the loss for a small<strong> batch</strong> of instances (say 32 of them), and take a single step of gradient descent for each batch. This is called<strong> minibatch gradient descent,</strong> which we’ll look at more closely next lecture.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-015">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-015" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0015.svg" class="slide-image" />

            <figcaption>
            <p    >Apart from this exception, the training of a neural network proceeds in much the same way as the training of linear classifiers we've seen already.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-016">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-016" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0016.svg" class="slide-image" />

            <figcaption>
            <p    >Before we dig into the details, we can get a sense of what neural network training looks like in the <a href="http://playground.tensorflow.org/#activation=sigmoid&amp;batchSize=10&amp;dataset=circle&amp;regDataset=reg-plane&amp;learningRate=0.03&amp;regularizationRate=0&amp;noise=0&amp;networkShape=7&amp;seed=0.76686&amp;showTestData=false&amp;discretize=true&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=false&amp;xSquared=false&amp;ySquared=false&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=false&amp;problem=classification&amp;initZero=false&amp;hideText=false&amp;noise_hide=false&amp;activation_hide=false&amp;regularization_hide=true"><strong class="blue">tensorflow playground</strong></a>. We suggest you play around a bit with the different datasets,  different activations, and try to change the shape of the network.<br></p><p     class="list-item">Note how the shape of the decision boundary changes based on the activation functions we choose (curvy for sigmoid, piecewise linear for ReLU)<br></p><p     class="list-item">Note that adding another layer makes the network much more difficult to train (especially with sigmoid activations).<br></p><p     class="list-item">Try the linear activation (i.e. no activations on the hidden nodes). Note that all you get is a linear decision boundary, not matter how many layers you try.<br></p><p     class="list-item">Try a network on the circular dataset, with hidden layers with 2 units. It should not be possible so solve the circular dataset this way. It can be shown that to create a closed shape like a circle as a decision boundary, at least one hidden layer needs to be strictly bigger than your input layer.</p><p     class="list-item"></p>
            </figcaption>
       </section>





       <section id="slide-017">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-017" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0017.svg" class="slide-image" />

            <figcaption>
            <p    >That’s the basic idea of neural networks. So far, it’s hopefully a pretty simple idea. The complexity of neural networks lies in computing the gradients. For such complex models, sitting down at the kitchen table with pen and paper, and working out a symbolic expression for the gradient is no longer feasible. If we manage it at all, we get horrible convoluted expressions that no longer reduce to nice, simple functions, as they did in the case of linear regression and logistic regression.<br></p><p    >To help us out, we need the <strong>backpropagation</strong> algorithm, which we’ll discuss in the next video.</p><p    ></p>
            </figcaption>
       </section>




       <section class="video" id="video-017">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-17">link here</a>
           <iframe
                src="https://www.youtube.com/embed/IZ4w-aG50nU?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-018">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-018" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0018.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-019">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-019" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0019.svg" class="slide-image" />

            <figcaption>
            <p    >In the last video, we saw what the structure of a very basic neural network was, and we ended on this question. <strong>How do we work out the gradient?</strong><br></p><p    >For neural networks, the gradients quickly get too complex to work out by hand, so we need to automate this process.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-020" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-020" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0020anim0.svg" data-images="32.Linear.key-stage-0020anim0.svg,32.Linear.key-stage-0020anim1.svg,32.Linear.key-stage-0020anim2.svg,32.Linear.key-stage-0020anim3.svg,32.Linear.key-stage-0020anim4.svg,32.Linear.key-stage-0020anim5.svg" class="slide-image" />

            <figcaption>
            <p    >There are three basic flavors of working out derivatives and gradients automatically.<br></p><p    >The first is to do it<strong> symbolically</strong>, What we do on pen and paper, when we work out a derivative, is a pretty mechanical process. It’s not too difficult to program this process out and let the computer do it for us. This, is what happens, when you as Wolfram alpha to work out a derivative, for instance. It has its uses, cartainly, but it won;t work for us. The symbolic expression of the gradient of a function grows exponentiall with the complexity of the original function. That means that as we build bigger and bigger networks the expression of the gradient would soon grow too big to store in memory, let alone to compute.<br></p><p    >An alternative approach is to forget the symbolic form of the function, and just <strong>estimate the gradien</strong>t for a specific input <strong>x</strong>. We could, for instance, pick some points close to <strong>x</strong> and and fit a hyperplane through the outputs. This would be a pretty good approximation of the tangent hyperplane, so we could just read out the gradient. The problem is that this is a pretty unstable business. It’s quite difficult to be sure that the answer is accurate. It’s also expensive: the more dimensions in your model space, the more points you need to get an accurate estimate of your gradient, and each point requires you to recompute your model for a new input.<br></p><p    ><strong>Backpropagation</strong> is a middle ground: it does part of the work symbolically, and part of the work numerically. We get a very accurate computation of the gradient, and the cost of computation is usually only twice as expensive as computing the output for one input.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-021">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-021" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0022.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s the three steps required to implement backpropagation for a given function.<br></p><aside    >Don't worry if this seems abstract, it should become clearer when we look at an example.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-022" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-022" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0023anim0.svg" data-images="32.Linear.key-stage-0023anim0.svg,32.Linear.key-stage-0023anim1.svg,32.Linear.key-stage-0023anim2.svg,32.Linear.key-stage-0023anim3.svg" class="slide-image" />

            <figcaption>
            <p    >To show that backpropagation is a<em> generic </em>algorithm for working out gradients, not just a method for neural networks, we’ll first show how it works for some arbitrary scalar function: f(x) = 2/sin(e<sup>-x</sup>).<br></p><aside    >There is no special meaning to this function. I just chained together a few operations for which the derivatives are simple.<br></aside><p    >First we take our function f, and we break it up into a chain of smaller functions, the output of each feeding into the next. Defining the functions <span>a</span>, <span>b</span>, <span>c</span>, and <span>d</span> as shown, we can write f(<span class="blue">x</span>) = <span class="orange">d</span>(<span class="orange">c</span>(<span>b</span>(<span class="green">a</span>(<span class="blue">x</span>)))). <br></p><p    >The graph on the right is a called a <strong>computation graph</strong>: each node represents a small computer program that receives an input, computes an output and passes it on to another module.<br></p><aside    >Normally, we wouldn’t break a function up in such small modules: this is just a simple example to illustrate the principle.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-023" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-023" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0024anim0.svg" data-images="32.Linear.key-stage-0024anim0.svg,32.Linear.key-stage-0024anim1.svg,32.Linear.key-stage-0024anim2.svg,32.Linear.key-stage-0024anim3.svg,32.Linear.key-stage-0024anim4.svg,32.Linear.key-stage-0024anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Because we’ve described our function as a composition of modules, we can work out the derivative purely by repeatedly applying the chain rule.<br></p><aside    >Since we know for each function what the argument is, we’ll leave the arguments out to keep the notation clean.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-024" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-024" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0025anim0.svg" data-images="32.Linear.key-stage-0025anim0.svg,32.Linear.key-stage-0025anim1.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll call the derivative of the whole function with respect to input x the <strong class="blue">global derivative</strong>, and the derivative of each module with respect to its input we will call a<strong class="orange"> local derivative</strong>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-025" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-025" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0026anim0.svg" data-images="32.Linear.key-stage-0026anim0.svg,32.Linear.key-stage-0026anim1.svg,32.Linear.key-stage-0026anim2.svg,32.Linear.key-stage-0026anim3.svg,32.Linear.key-stage-0026anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The next step is to work out the local derivatives symbolically, using the rules we know. <br></p><p    >The difference from what we normally do is that <strong>we stop</strong> when we have the derivatives of the output of a module in terms of the input. For instance, the derivative <span>∂</span><span class="orange">c</span>/ <span>∂</span><span>b</span> is cos <span>b</span>. Normally, we would fill in the definition of <span>b</span> and see if we could simplify any further. Here we stop once we know the derivative in terms of <span>b</span>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-026" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-026" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0027anim0.svg" data-images="32.Linear.key-stage-0027anim0.svg,32.Linear.key-stage-0027anim1.svg,32.Linear.key-stage-0027anim2.svg,32.Linear.key-stage-0027anim3.svg,32.Linear.key-stage-0027anim4.svg,32.Linear.key-stage-0027anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Then, once all the local derivatives are known, in symbolic form, we switch to <strong>numeric computation</strong>. We will take a <em>specific</em> input, in this case -4.499 and compute the gradient only for that.<br></p><p    >First we compute the output of the function f given this input. We do this simply by following the computation graph: the input is fed to the first module, and its output is fed to the second module, and so on. This is known as the <strong>forward pass</strong>. During our computation, we also retain our intermediate values <span class="green">a</span>, <span>b</span>, <span class="orange">c</span> and <span class="orange red">d</span>. These will be useful later on.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-027" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-027" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0028anim0.svg" data-images="32.Linear.key-stage-0028anim0.svg,32.Linear.key-stage-0028anim1.svg,32.Linear.key-stage-0028anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Next up is the <strong>backward pass</strong>. We take the chain-rule derived form of the derivative, and we fill in the intermediate values <span>a</span>, <span>b</span>, <span>c</span> and <span>d</span>. <br></p><p    >This gives us a function with no variables, so we can compute the output. The result is that the derivative of this function, for the specific input -4.499, is 0.<br></p><p    >Note that we have stopped doing symbolic computations: we fill in the numeric values and work out the numeric result (accepting a small amount of inaccuracy due to floating point imprecisions).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-028">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-028" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0029.svg" class="slide-image" />

            <figcaption>
            <p    >If you're still struggling to see the difference between these three options, consider whether the answer you get is specific to a particular input x, or whether you get an answer that applies to the variable x, regardless of its value.<br></p><p    >When we worked out the gradient for least squares regression or for logistic regression, the result was not specific to a particular input. We didn't get a specific vector filled with numbers, we got a symbolic function that told us how to compute the gradient for <em>any</em> model and dataset. In short, if you can do it without knowing what the specific numbers of the input are, it's symbolic computation.<br></p><p    >With numeric computation, you don't get this function. You specify the particular dataset and the current model, and you get an estimate of the gradient as a single vector filled with specific numbers. If you change the model or the dataset, you have to do the whole gradient estimation again. If you need to know the specific numbers of the input before you can start, it's numeric computation.<br></p><p    >Backpropagation is, as we've said a middle ground. It works out the derivatives of the modules with respect to their inputs symbolically. You can do this without knowing the specific input we want the gradient for, so this part is symbolic. We then switch to numeric computation. This part can only start if we know the specific input we are computing the gradient for, so this part is numeric.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-029">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-029" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0030.svg" class="slide-image" />

            <figcaption>
            <p    >More fine-grained modules make the local derivatives easier to work out, but may increase the numeric instability. Less fine grained modules usually result in more accurate gradients, but if we make them too big, we end up with the problem that the symbolic expression of the gradient grows too complex.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-030" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-030" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0031anim0.svg" data-images="32.Linear.key-stage-0031anim0.svg,32.Linear.key-stage-0031anim1.svg,32.Linear.key-stage-0031anim2.svg,32.Linear.key-stage-0031anim3.svg,32.Linear.key-stage-0031anim4.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s now see how this works for a neural net. <br></p><p    >It’s important to remember that we <em>don’t</em> care about the derivative of the output y with respect tot he inputs  <strong>x</strong>. The function we’re computing the gradient for is <em>the loss</em>, and the variables we want to compute the gradient for are the <em>parameters </em>of the network. <strong>x</strong> does end up in our computation, because it’s part of the loss, but only as a constant.<br></p><p    >We'll work out what the gradient descent update will look like for the weights in the first and second layer.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-031" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-031" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0032anim0.svg" data-images="32.Linear.key-stage-0032anim0.svg,32.Linear.key-stage-0032anim1.svg,32.Linear.key-stage-0032anim2.svg,32.Linear.key-stage-0032anim3.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s what the local gradients look like for the weight <span class="orange">v</span><sub class="orange">2</sub>. <br></p><p    >The line on the bottom shows how we update <span class="orange">v</span><sub class="orange">2 </sub>when we apply a single step of stochastic gradient descent for x (x may not appear in the gradient, but the values y and h2 were computed using x).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-032">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-032" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0033.png" class="slide-image" />

            <figcaption>
            <p    >To see what this update rule means, we can use an analogy. Think of the neural network as a hierarchical structure like a government trying to make a decision. The output node is the prime minister: he provides the final decision (for instance what the tax on cigarettes should be). <br></p><p    >To make this decision, he listens to his ministers. His ministers don’t tell him what to do, they just shout. The louder they shout, the higher they want him to make the output.<br></p><p    >If he trusts a particular minister, he will <span class="orange">weigh</span> their advice positively, and follow their advice. If he distrusts the minister, he will do the opposite of what the minister says. The ministers each listen to a bank of civil servants and weigh their opinions in the same way the prime minister weight theirs. All ministers listen to the same civil servants, but they have their own <span class="orange">level of trust</span> for each.<br></p><aside    >We haven’t drawn the bias, but you can think of the bias as the prime minister’s own opinion; how strong the opinions of the ministers need to be to change his mind.<br></aside><p    ><br></p><p    >image sources: <a href="https://www.government.nl/government/members-of-cabinet/mark-rutte"><strong class="blue">https://www.government.nl/government/members-of-cabinet/mark-rutte</strong></a>, <a href="https://www.government.nl/government/members-of-cabinet/ingrid-van-engelshoven"><strong class="blue">https://www.government.nl/government/members-of-cabinet/ingrid-van-engelshoven</strong></a>, <a href="https://www.rijksoverheid.nl/regering/bewindspersonen/kajsa-ollongren"><strong class="blue">https://www.rijksoverheid.nl/regering/bewindspersonen/kajsa-ollongren</strong></a><br></p><p    >Door Photo: Yordan Simeonov (EU2018BG) - Dit bestand is afgeleid van: Informal JHA meeting (Justice) Arrivals (26031834658).jpg, CC BY-SA 2.0, <a href="https://commons.wikimedia.org/w/index.php?curid=70324317"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=70324317</strong></a><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-033">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-033" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0034.png" class="slide-image" />

            <figcaption>
            <p    >So let’s say the network has produced an output. The prime minister has set a tax on cigarettes <span class="orange red">y</span>, and based on the consequences realises that he should actually have set a tax of t. He’s now going to adjust his level of trust in each of his subordinates.<br></p><p    >Looking at the update rule for weight <span class="orange">v</span><sub class="orange">2</sub>, we can see that he takes two things into account: the error (<span class="orange red">y</span>-t), how wrong he was, and what minister<span> h</span><sub>2</sub> told him to do.<br></p><p     class="list-item">If  the error is positive, he set <span class="orange red">y</span> too high. If <span>h</span><sub>2</sub> shouted loudly, he will lower his trust in her. <br></p><p     class="list-item">If the error is negative, he set <span class="orange red">y</span> too low. If <span>h</span><sub>2</sub> shouted loudly, he will increase his trust in her. <br></p><p    >If we use a sigmoid activation, the ministers can only provide values between 0 and 1. If we use an activation that allows h2 to be negative, we see that the minister takes the sign into account: if h2 was negative and the error was negative too, the trust in the minister increases (because the PM should’ve listened to her).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-034">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-034" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0035.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-035" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-035" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0036anim0.svg" data-images="32.Linear.key-stage-0036anim0.svg,32.Linear.key-stage-0036anim1.svg,32.Linear.key-stage-0036anim2.svg,32.Linear.key-stage-0036anim3.svg,32.Linear.key-stage-0036anim4.svg,32.Linear.key-stage-0036anim5.svg,32.Linear.key-stage-0036anim6.svg" class="slide-image" />

            <figcaption>
            <p    >So far, this is no different from gradient descent on a linear model. The real power of the backpropagation algorithm shows when we look at how the error propagates back down the network (hence the name) and is used to update the weights. Lets look at the derivative for weight w12</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-036" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-036" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0037anim0.png" data-images="32.Linear.key-stage-0037anim0.png,32.Linear.key-stage-0037anim1.png,32.Linear.key-stage-0037anim2.png,32.Linear.key-stage-0037anim3.png" class="slide-image" />

            <figcaption>
            <p    >To see how much minister <span>h</span><sub>2</sub> needs to adjust her trust in x<sub>1</sub>, she first looks at the <em>global error</em>. To see how much she contributed to that global error, and whether she contributed negatively or positively, she multiplies by <span>v</span><sub>2</sub>, her level of influence over the decision. Then she looks at how much the input from all her subordinates influenced the decision, considering the activation function (that is, if the input was very high, she’ll need a bigger adjustment to make a meaningful difference). Finally she multiplies by x<sub>1</sub>, to isolate the effect that we trust in x<sub>1</sub> had on her decision.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-037">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-037" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0038.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-038">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-038" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >These weren’t just reasons not to use neural nets in production. They also slowed down the research on neural nets. SVM researchers were (probably) able to more faster, because once they’d designed a kernel, they could compute the optimal model performance and know, without ambiguity, whether it worked or not. Neural net researchers could design an architecture and spend months tuning the training algorithm without ever knowing whether the architecture would eventually perform.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-039" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-039" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0040anim0.svg" data-images="32.Linear.key-stage-0040anim0.svg,32.Linear.key-stage-0040anim1.svg,32.Linear.key-stage-0040anim2.svg,32.Linear.key-stage-0040anim3.svg,32.Linear.key-stage-0040anim4.svg,32.Linear.key-stage-0040anim5.svg" class="slide-image" />

            <figcaption>
            <p    >One important part of building such a framework is to recognise that all of this can easily be described as matrix multiplication/addition, together with the occasional element-wise non-linear operation. This allows us to write down the operation of a neural network very elegantly. <br></p><p    >In order to make proper use of this, we should also work out how to do the backpropagation part in terms of matrix multiplications. That’s where we’ll pick up next week in the first <strong>deep learning</strong> lecture.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>




       <section class="video" id="video-039">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-39">link here</a>
           <iframe
                src="https://www.youtube.com/embed/-PvsRdlISls?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-040">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-040" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0041.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-041">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-041" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0042.svg" class="slide-image" />

            <figcaption>
            <p    >In lecture 5, we introduced the logistic regression model, with the logarithmic loss. We saw that it performed very well, but it had one problem: when the data are very well separable, it didn’t have any basis to choose between two models like this: both separate the training data very well. Yet, they’re very different models.<br></p><p    >There are some tricks we can add to the logistic regression to deal with this problem, but today we'll look at a loss function that takes this problem as its starting point: the maximum margin hyperplane classifier.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-042" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-042" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0043anim0.svg" data-images="32.Linear.key-stage-0043anim0.svg,32.Linear.key-stage-0043anim1.svg,32.Linear.key-stage-0043anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Here is an extreme example of the problem. We have two linearly separable classes and a <span class="orange">decision boundary</span> that separates the data perfectly. And yet, if I see a new instance that is very similar to the rightmost <span class="orange red">red diamond</span>, but with a slightly higher x<sub>1</sub> value, it is suddenly classified as a<span class="blue"> blue disc</span>.<br></p><p    >This illustrates the intuition behind the loss function we will introduce in this video. <strong>If we see new points</strong><em> near</em><strong> our existing points, they should be classified the same as the existing points. </strong>One way to accomplish this is to look at the distance from the <span class="orange">decision boundary</span> to the nearest <span class="orange red">red</span> diamond and <span class="blue">blue</span> disc, and to <em>maximize</em> that.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-043">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-043" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0044.svg" class="slide-image" />

            <figcaption>
            <p    >What we are looking for is the hyperplane that separates the classes and has a maximal distance to the nearest <span class="blue">positive point </span>and nearest <span class="orange red">negative point</span>. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-044">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-044" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0045.svg" class="slide-image" />

            <figcaption>
            <p    >We measure the distance m at a right angle to the decision boundary. For the <span class="blue">positive</span> class, there is only one point nearest the margin, but for the <span class="orange red">negative </span>class, there are two the same distance away.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-045">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-045" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0046.svg" class="slide-image" />

            <figcaption>
            <p    >The points closest to the decision boundary are called the <strong>support vectors</strong>. This name comes from the fact that the support vectors alone, are enough to describe the model. If I give you the support vectors, you can work out the hyperplane without seeing the rest of the data.<strong><br></strong></p><p    >The distance to the support vectors is called the <strong>margin</strong>. We’ll assume that the decision boundary is chosen so that the margin is the same on both sides.<br></p><aside    >Or, alternatively, you can imagine we are drawing parallel lines through the support vectors, and putting the decision boundary halfway between these lines.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-046">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-046" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    >So, given a dataset, how do we work out which hyperplane maximizes the margin? <br></p><p    >This is a tricky problem, because the support vectors aren’t <em>fixed</em>. If we move the hyperplane around to maximize the distance to one set of support vectors, we may move too close to other points, making <em>them</em> the support vectors. <br></p><p    >Surprisingly, there is a way to phrase the maximum margin hyperplane objective as a relatively simple optimization problem.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-047" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-047" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0048anim0.svg" data-images="32.Linear.key-stage-0048anim0.svg,32.Linear.key-stage-0048anim1.svg,32.Linear.key-stage-0048anim2.svg,32.Linear.key-stage-0048anim3.svg" class="slide-image" />

            <figcaption>
            <p    >To work this out, let’s first review how we use a hyperplane to define a linear decision boundary. Here is the 1D case. We have a single feature and we first define a linear function from the feature space to a scalar y. <br></p><p    >If the function is positive we assign the positive class, if it is negative, we assign the negative class. Where this function is equal to 0, where it “intersects” the feature space, is the decision boundary (which in this case is just a single point).<br></p><p    >Note that by defining the decision boundary this way, we have given ourselves an extra degree of freedom: the same decision boundary can be defined by infinitely many hyperplanes. We’ll use this extra degree to help us define a single hyperplane to optimize.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-048">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-048" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0049.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s the picture for a two dimensional feature space. The decision boundary is the<span class="orange"> dotted line</span> where the hyperplane intersects the (x<sub>1</sub>, x<sub>2</sub>) plane. If we rotate the hyperplane about that dotted line, we get a <em>different</em>  hyperplane defining<em> the same</em> decision boundary.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-049" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-049" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0050anim0.svg" data-images="32.Linear.key-stage-0050anim0.svg,32.Linear.key-stage-0050anim1.svg,32.Linear.key-stage-0050anim2.svg,32.Linear.key-stage-0050anim3.svg,32.Linear.key-stage-0050anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The hyperplane <span>h</span> we will choose is the one that produces y=1 for the positive support vectors and y=-1 for the negative support vectors. Or rather, we will<em> define</em> the support vectors as those points for which the line produces 1 and -1.<br></p><aside    >There's no guarantee that this happens at points that are in the dataset, but we will see later that this must be the case for an optimal choice of <span class="orange">h</span>.<br></aside><p    >For all other negative points, <span>h</span> should produce values below -1 and for all other positive points, <span>h</span> should produce values <em>above</em> 1.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-050">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-050" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0051.svg" class="slide-image" />

            <figcaption>
            <p    >This is the picture we want to end up with in 2 dimensions. The linear function evaluates to -1 for the <span class="orange red">negative support vectors</span>, and to a lower value for all other negative points. It evaluates to 1 for the <span class="blue">positive support vectors</span> and to a higher value for all other positive points.<br></p><p    >The trick we use to achieve this is to optimize<strong> with a constraint</strong>. We first define the margin as the distance from the decision boundary, where <span class="orange">h</span> evaluates to zero, to the line where <span class="orange">h</span> evaluates to 1, and on the other side to the line where h evaluates to -1. Then we set the constraint that all points should be on the correct side of their respective margins.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-051">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-051" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0052.svg" class="slide-image" />

            <figcaption>
            <p    >Here is our objective, written as precisely as we can manage at the moment. We will make this more precise as we move on.<br></p><p    >The quantity that we want to maximize is "2 times the margin": the width of the band separating the negative from the positive support vectors (between the two dotted lines in the previous slide).<br></p><p    >The constraints define the support vectors: all positive points should evaluate to 1 or higher. All negative points should evaluate to -1 or lower. Note that if we have N instances in our data, this gives us a problem with N constraints.<br></p><p    ><strong>Note that this automatically ensures that the support vectors end up at -1 and 1.</strong> Why?</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-052">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-052" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0053.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a picture of a case where all negative points are strictly less than -1, and all positive points are strictly larger than 1. The constraints are satisfied, but there are no points on the edges of the margin: we have no support vectors.<br></p><p    >In this case, we can easily make the margin bigger, pushing it out to coincide with the nearest points. Therefore, we have not hit the maximum yet. This is not an optimal solution to our optimization problem.<br></p><p    >Thus, any hyperplane with a maximal margin, that satisfies the constraints. must have points on the edges of its margin. These points are the support vectors.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-053">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-053" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the picture in 3D. Just like the hyperplane crosses the plane where y=0 to make the decision boundary, it crosses the y=1 plane to make the <span class="blue">positive margin</span>, and it crosses the y=-1 plane to make the <span class="orange red">negative margin</span>. <br></p><p    >Imagine finding a hyperplane that separates the classes, and then angling it so that he margins hit the nearest points.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-054" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-054" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0055anim0.svg" data-images="32.Linear.key-stage-0055anim0.svg,32.Linear.key-stage-0055anim1.svg,32.Linear.key-stage-0055anim2.svg,32.Linear.key-stage-0055anim3.svg,32.Linear.key-stage-0055anim4.svg,32.Linear.key-stage-0055anim5.svg,32.Linear.key-stage-0055anim6.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the picture for a single feature. We want to maximize the distance between the point where the hyperplane hits -1 and where it hits 1, while keeping the <span>negatives</span> below -1 and the <span>positives </span>above 1.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-055" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-055" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0056anim0.svg" data-images="32.Linear.key-stage-0056anim0.svg,32.Linear.key-stage-0056anim1.svg" class="slide-image" />

            <figcaption>
            <p    >So, how do we work this into a practical optimization objective that we can actually solve?<br></p><p    >The first thing we’ll do, is to simplify the two constraints for the two classes into a single constraint.<br></p><p    >We introduce  a label y<sub>i</sub> for each point x<sub>i</sub> which is -1 for <span class="orange red">negative points</span> and +1 for <span class="blue">positive points</span>. Multiplying the left-hand side of the constraint by y<sub>i</sub> keeps it the same for <span class="blue">positive points </span>and takes the negative for<span class="orange red"> negative points</span>. This means that in both case, the left hand side should now be larger than or equal to one. <br></p><aside    >This label y<sub>i</sub> is the same label we introduced to define the least squares loss, but now we're using it in a different way. Instead of trying to map each point to its label y<sub>i</sub>, we are fitting points to values <span class="blue">above</span> or <span class="orange red">below</span> y<sub>i</sub>.<br></aside><p    >We now have a problem with the same constraint for every instance in the data.<br></p><p    >Next, we need to make the phrase "<span class="orange">2x the size of the margin</span>" more precise. We know that our hyperplane, whichever hyperplane we choose, is defined by parameters <strong class="orange">w</strong> and <span class="blue">b</span>. Looking at the parameters of a particular hyperplane (good or bad), can we tell what the size of the margin is?</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-056">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-056" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0057.svg" class="slide-image" />

            <figcaption>
            <p    >First, let's recall what the parameters mean geometrically. Remember that in the equation <strong>w</strong><sup>T</sup><strong>x</strong> + <span>b</span>, <strong>w</strong> is the vector pointing orthogonally to the decision boundary. <span class="blue">b</span> is how high the hyperplane is at the origin.<br></p><aside    >Note that the hyperplane we have drawn here is not a solution to our problem, since it does not satisfy the constraints.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-057">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-057" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0058.svg" class="slide-image" />

            <figcaption>
            <p    >This is the value we’re interested in expressing. Twice the margin.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-058" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-058" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0059anim0.svg" data-images="32.Linear.key-stage-0059anim0.svg,32.Linear.key-stage-0059anim1.svg,32.Linear.key-stage-0059anim2.svg" class="slide-image" />

            <figcaption>
            <p    >To make the math easier, let’s move the axes around so that the lower dotted line (belonging to the negative support vectors) crosses the origin. Doing this doesn’t change the size of the margin.<br></p><p    >We can now imagine a vector from the origin to the <span class="blue">upper dotted line</span>, at a right angle. Call this vector <strong>a</strong>. The length of <strong>a</strong> is exactly the quantity we’re interested in.<br></p><p    >Remember also that the vector <strong>w</strong> points in the same direction as <strong>a</strong>, because both are perpendicular to the decision boundary.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-059" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-059" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0060anim0.svg" data-images="32.Linear.key-stage-0060anim0.svg,32.Linear.key-stage-0060anim1.svg,32.Linear.key-stage-0060anim2.svg,32.Linear.key-stage-0060anim3.svg" class="slide-image" />

            <figcaption>
            <p    >Because of the way we’ve moved the hyperplane, we know that the origin (<strong>0</strong>) hits the negative margin, so evaluates to -1. We also know that <strong class="orange">a</strong> hits the positive margin, so evaluates to +1.<br></p><p    >Subtracting the first from the second, we find that the dot product of <strong>a</strong> and <strong class="orange">w</strong> must be equal to two. <br></p><aside    >The dot product of anything with the zero vector is always 0.<br></aside><p    >Since <strong>a</strong> and <strong class="orange">w</strong> point in the same direction (cos α = 1), their dot product is just the product of their magnitudes (see the geometric definition of the dot product on the right).<br></p><p    >Re-arranging, we find that the length of <strong>a</strong> is 2 over that of <strong class="orange">w</strong>.<br></p><p    ><br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-060">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-060" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0061.svg" class="slide-image" />

            <figcaption>
            <p    >So, the thing we actually want to maximise is 2/||<strong class="orange">w</strong>||. This gives us a precise optimization objective.<br></p><p    >Note that almost all the complexity of the loss is in the constraints. Without them we could just let all elements of <strong class="orange">w</strong> go to zero However, the constraints require the output of our model to be larger than 1 for all positive points and smaller than -1 for all negative points. This will automatically push the margin up to the support vectors, but no further.<br></p><aside    >Consider what it would mean for the elements of <strong class="orange">w</strong> to go to zero. <strong class="orange">w</strong> is the gradient of our hyperplane. It points in the direction of steepest ascent, and its magnitude indicates how steep that ascent is. The smaller <strong class="orange">w</strong> is, the more flat the hyperplane lies. This is what the objective says: subject to the constraint that all points are on the correct side of their respective margins, we want a hyperplane that lies as flat as possible. If you think back to the 3D picture, you should be able to imagine how this ensures as wide a margin as possible.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-061">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-061" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0062.svg" class="slide-image" />

            <figcaption>
            <p    >Since we prefer to minimize instead of maximize, we take the inverse of this objective, and minimize that. The resulting classifier is called a “<strong>hard margin</strong>” <strong>support vector machine</strong> (SVM), since no points are allowed to violate the constraint and end up inside the margin.<br></p><aside    >In previous lectures we usually took the negative of the objective to turn maximization into minimization. In SVMs taking the inverse is more common, since the objective looks nicer this way.<br></aside><p    >The hard margin SVM is nice, but it doesn’t work well when:<br></p><p     class="list-item">We have data that is not linearly separable<br></p><p     class="list-item">We could have a very nice decision boundary if we just ignored a few misclassified points. For instance, when there is a little noise, or a few outliers.<br></p><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-062" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-062" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0063anim0.svg" data-images="32.Linear.key-stage-0063anim0.svg,32.Linear.key-stage-0063anim1.svg" class="slide-image" />

            <figcaption>
            <p    >A common alternative is to replace the norm of <strong class="orange">w</strong> by the dot product of <strong class="orange">w</strong> with itself. This is just a question of removing the square from the norm, so it doesn't change the location of the minimum. <br></p><aside    >This is because the square is a monotonic function: if the input gets bigger, the output gets bigger.<br></aside><p    >This form is easier to work with if we want to work out the gradient explicitly.<br></p><aside    >This objective is also sometimes written as <span>½||</span><strong class="orange">w</strong><span>||</span><sup>2</sup>, which means the same thing.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-063">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-063" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0064.svg" class="slide-image" />

            <figcaption>
            <p    >To deal with such situations, we can allow a <strong>soft margin</strong>. In a soft margin, we allow a few points to be on the wrong side of the margin, if it helps us achieve a better fit on the rest of the points. That is, we can trade off a few violations of the constraints against a bigger margin.<br></p><aside    >These points can even be on the wrong side of the decision boundary.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-064">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-064" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0065.svg" class="slide-image" />

            <figcaption>
            <p    >To achieve this, we introduce a <strong>slack parameter</strong> <span>p</span><sub>i</sub><span class="green"> </span>for each point <strong>x</strong><sub>i</sub>. This parameter indicates the extent to the constraint on <strong>x</strong><sub>i</sub> is <em>relaxed</em><strong>.</strong> Our learning algorithm can set <span class="green">p</span><sub class="green">i</sub> to whatever it likes. If it sets <span>p</span><sub>i</sub> to zero, the constraint is the same as it was for the hard margin classifier. If it sets <span>p</span><sub>i</sub> higher than zero, the constraint is relaxed and the point <strong>x</strong><sub>i</sub> can fall inside the margin. <br></p><p    >The price we pay is that <span>p</span><sub>i</sub> is added to our minimization objective, so the value we reach there becomes higher if we use more nonzero slack parameters.<br></p><p    >Our search algorithm, which we will detail later, does the rest. It automatically makes the tradeoff between how much we want to violate the original constraints and how big we want the margin to be.<br></p><p    ><span class="orange red">C</span> is a hyperparameter, indicating how to balance the tradeoff.<br></p><aside    >The value of <span class="orange red">C</span> is positive, and we usually try values  on a logarithmic scale like 0.001, 0.01, 0.1, 1.0, 10 and 100. As <span class="orange red">C</span> goes to infinity, we recover the hard margin SVM, where violating the constraints is “infinitely bad” and this never happens.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-065" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-065" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0066anim0.svg" data-images="32.Linear.key-stage-0066anim0.svg,32.Linear.key-stage-0066anim1.svg,32.Linear.key-stage-0066anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what that looks like in 1D. The open points are the support vectors, and for each class, we have one point on the wrong side of the decision boundary, requiring us to pay the residual <span>p</span><sub>i</sub> as a penalty.<br></p><p    >So, the objective function has a penalty added to it, but without this penalty, we would not have been able to satisfy the objective at all, since the two classes are not separable<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-066">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-066" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0067.svg" class="slide-image" />

            <figcaption>
            <p    >However, even if the classes <em>are</em> linearly separable, it can be good to allow a little slack. <br></p><p    >Here, the two points that would be the support vectors of the hard margin objective leave a very narrow margin. By allowing a little slack, we can get a much wider margin that provides a decision boundary that may be more likely to generalise to unseen data. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-067">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-067" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0068.svg" class="slide-image" />

            <figcaption>
            <p    >So, now that we have made our objective precise, how do we find a good solution? We haven’t discussed constrained optimization much yet. It turns out, we don't necessarily <em>need </em>to use constrained optimization methods, although there is a benefit to using them. We'll look at both options.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-068" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-068" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0069anim0.svg" data-images="32.Linear.key-stage-0069anim0.svg,32.Linear.key-stage-0069anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The first oiption allows us to use the old familiar gradient descent, without having to worry about constraints. <br></p><p    >The other requires us to delve into constrained optimization, which we start to do in the next video. The payoff for that is that it opens the door to the <strong>kernel trick</strong>.<br></p><p    >In the rest of this video, we will work out option one.<br></p><p    >If you're in a hurry, and you just want to know the parts that are important for the course, you can skim the rest of this video and focus on the next two. </p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-069" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-069" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0070anim0.svg" data-images="32.Linear.key-stage-0070anim0.svg,32.Linear.key-stage-0070anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To get rid of the constraints, let’s look at what we know about the value of <span class="green">p</span><sub class="green">i</sub>.<br></p><p    >If the constraint for <strong>x</strong><sub>i</sub> is violated, we can see that <span class="green">p</span><sub class="green">i</sub> makes up the difference between what y<sup>i</sup>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sup>i</sup>+ <span class="blue">b</span>) should be (1) and what it is.<br></p><p    >If the constraint is not violated, <span class="green">p</span><sub class="green">i</sub> becomes zero, and the value we computed above becomes negative.<br></p><p    >We can summarise these two conclusions in a single definition for <span class="green">p</span><sub class="green">i</sub>:it is is 1 - y<sup>i</sup>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sup>i</sup>+ <span class="blue">b</span>) if the constraint is violated and 0 otherwise. This is equal to the value max(0, 1- y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>)) in both cases.<br></p><p    >Since this value is always equal to <span class="green">p</span><sub class="green">i</sub>, we can replace <span class="green">p</span><sub class="green">i</sub> by it everywhere it occurs in the optimization objective</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-070">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-070" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0071.svg" class="slide-image" />

            <figcaption>
            <p    >Doing this, we get a new objective function. <br></p><p    >The new constraints are now always true. For the second one, this is easy to see, since the maximum of 0 and something is always larger than or equal to 0. <br></p><p    >For the first, note that we worked out max(0, 1- y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>)) as how far below 1 the value y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) was. If we move it to the the other side, we get <br></p><p    >y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) + max(0, 1- y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>))<br></p><p    >which must therefore be exactly equal to 1 if y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) is below 1, or larger if y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) is larger than 1.<br></p><p    >Since the constraints are always true, we can remove them.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-071" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-071" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0072anim0.svg" data-images="32.Linear.key-stage-0072anim0.svg,32.Linear.key-stage-0072anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This gives us an <strong>unconstrained loss function</strong> we can directly apply to any model. For instance when training a neural network to classify, this makes a solid alternative to logarithmic loss. This is sometimes called the <strong>L1-SVM</strong> (loss). <br></p><aside    >There is also the L2-SVM loss where a square is applied to the <span class="green">p</span><sub class="green">i</sub> function, to increase the weight of outliers.<br></aside><p    >We can think of the first term as a<strong> regularizer</strong>. It doesn’t enforce anything about how well the plane should fit the data. It just ensures that the parameters of the plane don’t grow too big. We'll see more regularization in the next lecture, but this form, where we add the norm of the parameter vector to the loss function, is very common.<br></p><p    >The highlighted part of the second term functions as a kind of error (just as we used in least squares classification, but without the square). It computes how far the model output  y<sub>i</sub>(<strong class="orange">w</strong><sup>T</sup><strong>x</strong><sub>i</sub>+ <span class="blue">b</span>) is away from the desired value (1). <br></p><p    >However, unlike the least squares classifier, we <em>only</em> compute this error for points that are sufficiently close to the decision boundary. For any points far from the boundary (i.e. outside the margin), we do not compute any error at all. This is achieved by cutting off any negative values. If the data is linearly separable, we could easily shrink the margin enough to make the error zero for all points, but this usually requires a <strong>w</strong> with a very high norm, so then the regulariser kicks in and start increasing so much that we prefer some points inside the margin.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-072">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-072" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0073.svg" class="slide-image" />

            <figcaption>
            <p    >And with that, we have discussed our final classification loss. Let’s review.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-073">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-073" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0074.svg" class="slide-image" />

            <figcaption>
            <p    >Here are all our loss functions in one handy slide.<br></p><p    >The <strong>error</strong>, also known as zero one loss, is imply the number or proportion of misclasssified examples. It’s usually what we’re interested in, but it doesn’t give us a loss surface that is suitable for searching.<br></p><p    >The<strong> least-squares loss</strong> we introduced as a simple illustration of the principle of a proxy loss for the error. In practice it doesn't usually work very well, and is rarely used.<br></p><p    >The <strong>log loss </strong>requires a sigmoid function to be added to the output of the linear function. It assumes that he result is the probability of the positive class applying to the instance, and it maximizes the log likelihood of the classes given the model parameters. Practically this boils down to minimizing the negative log likelihood of the correct class. This can also be derived from the cross-entropy between the true class distribution given by the data and the class distribution given by the model.<br></p><p    >Finally, the <strong>soft margin SVM loss</strong>, which we've introduced today attempts to maximize the margin between the positive and negative points. It's also know as a maximum margin loss, or the <strong>hinge loss</strong> (since the error is fed through a maximum function, which looks like a hinge).<br></p><p    ></p>
            </figcaption>
       </section>




       <section class="video" id="video-073">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-73">link here</a>
           <iframe
                src="https://www.youtube.com/embed/cPbsqPg-s2Y?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-074">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-074" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-075" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-075" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0076anim0.svg" data-images="32.Linear.key-stage-0076anim0.svg,32.Linear.key-stage-0076anim1.svg" class="slide-image" />

            <figcaption>
            <p    >In the previous video we introduced the maximum margin loss objective. This was a <strong>constrained optimization</strong> problem which we hadn't learned how to solve yet. We sidestepped that issue by rewriting it into an unconstrained optimization problem, so that we could solve it with plain gradient descent.<br></p><p    >In this video, we will learn a relatively simple trick for attacking constrained optimization problems: the method of <strong>Lagrange multipliers</strong>. In the next video, we will see what happens if we apply this method to the SVM objective function.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-076">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-076" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0077.svg" class="slide-image" />

            <figcaption>
            <p    >So we start with <strong>optimization under constraints</strong>.<br></p><p    >First let’s make it a little more intuitive what optimization under constraints looks like. Here, we have a simple constrained optimization problem. We are trying to find the lowest point on <span class="orange red">some surface</span>, but there is <span class="green">a constraint</span> that we also need to satisfy.  <br></p><p    >In this case, the constraint specifies that the solution must lie on the unit circle (that is, x and y together must make a unit vector).  Within that set of points, we want to find the points x and y that result in the lowest value <span class="orange red">f(x, y)</span>.<br></p><p    >This is what is called an <strong>equality constraint</strong>. We have some function of our parameters that needs to be exactly equal to some value for any solution that we will return.<br></p><aside    >If you have a function of the parameters that needs to be greater than or less than some value, this is called an inequality constraint. We will discuss this in the optional 6th video.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-077">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-077" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0078.png" class="slide-image" />

            <figcaption>
            <p    >We can now draw the surface of <span class="orange red">f</span>. In this case, <span class="orange red">f </span>is a two-dimensional parabola. We see that if we ignore the constraint, the lowest point is somewhere towards the bottom right. If we move to that point, however, we violate<span class="green"> the constraint</span>.<br></p><p    >To figure out how low we can get while satisfying the constraint, we project the constraint region (the unit circle) onto the function, giving us a deformed circle. The constrained optimization problem asks what the lowest point on this deformed circle is.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-078" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-078" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0079anim0.svg" data-images="32.Linear.key-stage-0079anim0.svg,32.Linear.key-stage-0079anim1.svg,32.Linear.key-stage-0079anim2.svg" class="slide-image" />

            <figcaption>
            <p    >The method of  <strong>Lagrange multipliers</strong> is a popular way of dealing with these kinds of problems. <br></p><p    >To give you an idea of where we're going, we will describe the recipe first, with no derivation or intuition. We'll just show you the steps you need to follow to arrive at an answer, and we'll walk through a few examples. Then, we will look at why this recipe actually works.<br></p><p    >First, we need to rewrite the constraint so that it is equal to zero. This is easily done by just moving everything to the left hand side. We call the objective function (the one we want to minimize) <span class="orange red">f</span> and the left hand side of this constraint <span class="green">g</span>.<br></p><p    >Then, we create a new function L, <strong>the Lagrangian</strong>. This function has the same parameters as <span class="orange red">f</span>, plus an additional parameter α. It consists of the function <span class="orange red">f</span> plus or minus the constraint function <span class="green">g</span> times α. The end result will be the same whether we add or subtract <span class="green">g</span>. The parameter α is called a <strong>Lagrange multiplier</strong>. <br></p><p    >We now take the partial derivative of L with respect to all of its arguments (including α), i.e. we compute its gradient, and we set them all equal to 0. The resulting system of equations describes the solution to the constrained optimization problem. If we're lucky, that system of equations can be solved. <br></p><aside    >As always when we optimize by setting the derivative equal to zero, the solutions may be maxima, minima, saddlepoints or even flat regions that aren't optima (plateaus). Once we've found our solutions, we'll need to use a little common sense to work out which is which.<br></aside><p    >Again, there is no reason you should understand from this description why this should work at all. Let's first see the method in action, and then look at why it works.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-079" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-079" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0080anim0.png" data-images="32.Linear.key-stage-0080anim0.png,32.Linear.key-stage-0080anim1.png,32.Linear.key-stage-0080anim2.png,32.Linear.key-stage-0080anim3.png" class="slide-image" />

            <figcaption>
            <p    >This is our example problem with the constraint rewritten to be equal to 0.<br></p><p    >The first thing we do is to define our L-function. This is a function in three variables: the x and y from <span class="green">f</span> and the Lagrange multiplier α we've introduced.<br></p><p    >Next we take the three partial derivatives of L with respect to its arguments. We set all of these equal to zero which gives us a system of equations. If we manage to solve this, we work out where the solutions to our problem are.<br></p><aside    >Note that setting the derivative for the Lagrange multiplier equal to zero recovers <span class="green">the constraint</span>. This is always the case.<br></aside><p    >There's no exact recipe for how to work this out in terms of x and y. Here are a few tricks to look out for:<br></p><p     class="list-item">You can often rewrite the x and y equations to isolate the Lagrange multiplier on the left hand side and then set the right hand sides equal to each other. We'll use this trick in the next slide.<br></p><p     class="list-item">Often, the constraint is the simplest function. Rewrite this to isolate one of the variables, and then look for another equation where you can easily isolate a variable.<br></p><p     class="list-item">If you have access to Wolfram Alpha (e.g. if you're not doing an exam) it's a good idea to put<a href="https://www.wolframalpha.com/input/?i=solve+x+-+1+-+2xa+=+0,+y+-+4+-2ya+=+0,+x%5E2+++y%5E2+=1+"><strong class="blue"> the system of equations</strong></a> in, as well as <a href="https://www.wolframalpha.com/input/?i=optimize+(1/2)x%5E2+-x+++(1/2)y%5E2+-4y+++4+on+the+unit+circle"><strong class="blue">the minimization as a whole</strong></a>, to see if the solution looks like one that is easy to solve by hand. Often, Alpha will give you a mess of squares and constants, suggesting that the analytic solution is not pretty, and you might as well solve it numerically. There is no guarantee that this method yields an easily solvable system of equations (unless you're doing a homework problem).</p><p     class="list-item"></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-080" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-080" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0081anim0.svg" data-images="32.Linear.key-stage-0081anim0.svg,32.Linear.key-stage-0081anim1.svg,32.Linear.key-stage-0081anim2.svg,32.Linear.key-stage-0081anim3.svg,32.Linear.key-stage-0081anim4.svg,32.Linear.key-stage-0081anim5.svg" class="slide-image" />

            <figcaption>
            <p    >We are left with the three equations on the top left. It's not always guaranteed that the Lagrangian method leads to a system of equations that can be neatly solved, but in this case it can. Finding such a solution isn't a purely mechanical process, we can't give you a set of steps that always works, but a good place to start is to rewrite the equations for the parameters to isolate the Lagrange multiplier α on the left hand side.<br></p><p    >We then set the right hand sides equal to each other. Moving both denominators to the other sides, we see that the terms 2xy on both sides cancel out. And we are left with y=4x as a condition for our solution.<br></p><aside    >This example was carefully constructed so that this would happen. Without this bit of luck, the analytical solution becomes very complicated.<br></aside><p    >We now use the constraint <span class="green">x</span><sup class="green">2</sup><span class="green"> + y</span><sup class="green">2</sup><span class="green"> = 1</span> to finish the solution. We put 4x in place of y to give us an equation with only xs to solve, and we put 1/4y in place of x to give us an equation with only ys to solve. <br></p><p    >In both cases, the square means that we get a positive and a negative answer. This gives us four possible solutions. We can check the value of f(x, y) for each to see which is the minimum, or we can look at the plot. The latter option shows that the minimum has a positive x and a negative y, so that must be the solution.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-081" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-081" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0082anim0.svg" data-images="32.Linear.key-stage-0082anim0.svg,32.Linear.key-stage-0082anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Before we see why this works, we'll look at one more example.<br></p><p    >Imagine you are given two investment opportunities by a bank. You can use <span class="orange">plan A</span> or <span class="blue">plan B</span>. Both plans are guaranteed to make money after a year, but the more money you invest, the less you make proportionally (imagine there's a very strict tax system). The curves for the interest you get are shown top right.<br></p><p    >Both are clearly profitable investments, but sadly you don't have any money. What you can do however, is act as a bank yourself. You offer one of the schemes to somebody else. You take their money, and incur a debt. After a year, you'll have to pay them back with the interest, but in the mean time, you can use their money in the other scheme. All we need to do is figure out a point where one scheme makes more money than the other.<br></p><p    >We model this trick by saying you can invest positive or a negative amount in either of the schemes. In that case, the debt you incur is the negative investment, minus the interest. This is why the curve is mirrored for negative investments: you grow your debt by offering an investment to others.<br></p><p    >We'll label your investments as <span class="orange">a</span> dollars in scheme <span class="orange">A</span> and <span class="blue">b</span> dollars in scheme <span class="blue">B</span>. Since you have no money of your own, our constraint is that <span class="orange">a</span> + <span class="blue">b</span> = 0. Everything you get from the person investing with you, you put into the other plan. We want to maximize the amount of money you make after a year, which is the sum of the investments and the interests.<br></p><p    >From the plot, it's clear that <span class="blue">plan B</span> always pays more than <span class="orange">plan A</span> everywhere (this is necessary for a clean solution), so you should probably use <span class="blue">plan B</span> yourself, and offer <span class="orange">plan A</span> to somebody else. But how much should invest? The amount you make is proportional to how much you invest, but it also decays, so it's not as simple as just investing as much as you can.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-082" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-082" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0083anim0.svg" data-images="32.Linear.key-stage-0083anim0.svg,32.Linear.key-stage-0083anim1.svg,32.Linear.key-stage-0083anim2.svg,32.Linear.key-stage-0083anim3.svg,32.Linear.key-stage-0083anim4.svg,32.Linear.key-stage-0083anim5.svg" class="slide-image" />

            <figcaption>
            <p    >First, we write down our Lagrangian, which is simply the objective function, plus the constraint function times α.<br></p><p    >We work out the partial derivatives and set them equal to zero. Remember that the derivative of the absolute function |x| is the sign function sign(x). <br></p><p    >We find a solution, again, by isolating the Lagrange multipliers on the left hand side, and setting the right hand sides equal to one another. Then, the constraint tells us very simply that <span class="blue">b</span> should be equal to -<span class="orange">a</span>, so we fill that in to get an expression in terms of only <span class="orange">a</span>, which we can solve. This tells us that |<span class="orange">a</span>| = 1, which means we get solutions at <span class="orange">a</span> = 1 and <span class="orange">a</span> = -1. We can tell from the plot which is the minimum and which is the maximum.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-083">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-083" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0084.svg" class="slide-image" />

            <figcaption>
            <p    >If we make the interest curves cross, the problem becomes a bit more interesting: which plan is better depends on how much we put in. We don't know beforehand which plan to choose and which to offer. <br></p><p    >We can also attack this problem with the method of Lagrange multipliers. If you do this, you'll likely get stuck at the equation shown below. This tells us the solution, but it doesn't simplify in a straightforward way to a simple answer. This is often the case with more realistic problems. <br></p><p    >Note that this doesn't make the method of Lagrange multipliers useless for such problems. We've still found a solution, we just can't express it better than this. We can easily solve this equation numerically, which would probably give us a much more accurate answer, more quickly than if we'd solved the constrained optimization problem by numerical means in its original form.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-084">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-084" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0085.png" class="slide-image" />

            <figcaption>
            <p    >This has hopefully given you a good sense of <em>how</em> the method works. If you trust us, you can now just apply it, and with a little common sense, you can usually find your way to a solution.<br></p><p    >Still, we haven't discussed why this works. Let's see if we can add a little intuition. To illustrate, we'll return to the parabola we started with.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-085" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-085" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0086anim0.png" data-images="32.Linear.key-stage-0086anim0.png,32.Linear.key-stage-0086anim1.png,32.Linear.key-stage-0086anim2.png,32.Linear.key-stage-0086anim3.png,32.Linear.key-stage-0086anim4.png,32.Linear.key-stage-0086anim5.png,32.Linear.key-stage-0086anim6.png" class="slide-image" />

            <figcaption>
            <p    >One way to help us visualize what's happening is to draw <strong>contours</strong> for the function f. These are lines on our function where the output is the same value. For any given value k, we can highlight all the points where <span class="orange red">f(x, y)</span> = k, resulting in a curved line on the surface of our function. <br></p><p    >If we look down onto the xy plane from above, the z axis disappears, and we get a 2D plot, where the contour lines give us an idea of the height of the function. Note that the function f gets lower towards the top right corner. <br></p><aside    >This principle is often used in terrain maps to indicate elevation where they are called isolines.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-086" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-086" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0087anim0.svg" data-images="32.Linear.key-stage-0087anim0.svg,32.Linear.key-stage-0087anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Each contour line indicates a constant output value for <span class="orange red">f</span>. We can tell by this plot what we can achieve while sticking to the constraint..<br></p><p    >The output value<span> </span><span class="orange red">k</span><sub class="orange red">1</sub> is very low (the fourth lowest of the contour lines in this plot), so it would make a good solution, but it never meets <span class="green">the circle representing our constraints</span>. That means that we can’t get the output as low as <span class="orange red">k</span><sub class="orange red">1</sub> <em>and</em> satisfy the constraints.<br></p><p    >The next lowest contour we've drawn, with value <span class="orange red">k</span><sub class="orange red">2</sub>, does give us a contour line that hits the circle representing our constraints. Therefore, we can satisfy our constraints and get at least as low as <span class="orange red">k</span><sub class="orange red">2</sub>. However, the fact that it <em>crosses</em> the circle of our constrains, means that we can also get <em>lower</em> than <span class="orange red">k</span><sub class="orange red">2</sub>. This makes sense if you look at the plot: if we drew more contours, we could have one between <span class="orange red">k</span><sub class="orange red">1</sub> and <span class="orange red">k</span><sub class="orange red">2</sub> that hits the green circle. If we try and get lower and lower without leaving the circle, we see that we would probably end up with the contour that doesn't<em> cross </em>the circle, but just <em>touches</em> it at one point only. A bit like a tangent line, but curved.<br></p><p    >So, for this picture we have three conclusions:<br></p><p     class="list-item">Any contour line that doesn't meet the constraint region represents a value that we cannot achieve while satisfying the constraints.<br></p><p     class="list-item">Any contour line that crosses the constraint region represents a value we can achieve, but that isn't the optimum.<br></p><p     class="list-item">Any contour line that just touches the constraint region is a possible optimum.<br></p><p    >These certainly seem true here. We can use some basic calculus to show that this is true in general.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-087" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-087" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0088anim0.svg" data-images="32.Linear.key-stage-0088anim0.svg,32.Linear.key-stage-0088anim1.svg,32.Linear.key-stage-0088anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We'll work out how these ideas look in hyperplanes, and then translate them to general functions. We can always approximate our functions locally with a hyperplane, so the translation should be simple.<br></p><p    >If we have a hyperplane defined by <strong class="orange">w</strong><sup>T</sup><strong>x</strong> + <span class="blue">b</span>, then we know that<span class="orange"> </span><strong class="orange">w</strong> is the direction of steepest ascent, and -<strong class="orange">w</strong> is the direction of steepest <em>de</em>scent. <strong>This tells us that the direction orthogonal to the line of </strong><strong class="orange">w</strong><strong> is the direction in which the value of the plane doesn’t change</strong>: the direction <strong>of equal value</strong>. If we drew contours on a hyperplane, they would all be lines orthogonal to <strong class="orange">w</strong>.<br></p><p    >This means that if we take any point on our function <span class="orange red">f</span> and work out the tangent hyperplane of <span class="orange red">f</span> at that point, that is, compute the gradient, <strong>the direction orthogonal to the gradient points along the contour line</strong>. <br></p><aside    >The contour line is a curve, so to keep constant value, a straight line is not enough, but if we zoom in close enough, the tangent hyperplane is a close approximation, and the contour line will be a straight line orthogonal to the gradient.<br></aside><p    >In this case, since our contour line <em>crosses</em> the circle of the constraints, the direction of equal value doesn’t point along the circle for the constraints, and we can conclude that the value of f decreases in one direction along<span class="green"> the circle</span> and increases in one direction. Put simply, we are not at a minimum.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-088" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-088" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0089anim0.svg" data-images="32.Linear.key-stage-0089anim0.svg,32.Linear.key-stage-0089anim1.svg,32.Linear.key-stage-0089anim2.svg" class="slide-image" />

            <figcaption>
            <p    >By this logic, the only time we can be sure that there is no lower to go along <span class="green">the circle</span> is when the direction of equal value points along the circle. In other words, <strong>when the contour line is tangent to the circle</strong>: when it touches it only at one point without crossing it. <br></p><p    >How do we work out where this point is? By recognizing that <strong>the circle for our constraints is </strong><em>also</em><strong> a contour line</strong>. A contour of the function <span class="green">x</span><sup class="green">2</sup><span class="green"> + y</span><sup class="green">2</sup>, for the constant value <span class="green">1</span>. <br></p><p    >When the gradient of <span class="green">x</span><sup class="green">2</sup><span class="green"> + y</span><sup class="green">2</sup> points in the same or opposite direction as that of f, then so do the vectors orthogonal to them, which are the directions of equal value for <span class="orange red">f</span> and for <span class="green">g</span> respectively. And when that happens we have a minimum or maximum for our objective.<br></p><aside    >In this picture we've matched the steepest descent direction of <span class="green">the constraint</span> with the steepest ascent direction of <span class="orange red">the objective function</span>. This makes for a clearer picture, but the method also works if we match up the steepest ascent directions of both. Only when we start looking at inequality constraints do we need to be more careful about this.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-089" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-089" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0090anim0.svg" data-images="32.Linear.key-stage-0090anim0.svg,32.Linear.key-stage-0090anim1.svg" class="slide-image" />

            <figcaption>
            <p    >These are the two basic insights we've just discussed. We look at the contour lines of <span class="orange red">f</span> and <span class="green">g</span>, and note that the the constraint region is just the contour line of <span class="green">g</span> for the value 0.<br></p><p    >At any point where they cross, we've shown there can't be a minimum. At any point where they don't touch at all, we're outside the constraint region. The only other option is that they are <em>tangent</em>: that is, they just touch.<br></p><p    >To work out where two curves just touch, we note that the vectors that point along the curve must lie on the same line. These are the directions of equal value of <span class="orange red">f</span> and <span class="green">g</span> respectively, which are the vectors orthogonal to the gradients of <span class="orange red">f</span> and <span class="green">g</span>. So instead of looking for where the directions of equal value point in the same direction, we can just <strong>look where the gradients point in the same direction</strong>. This is something that we can write down symbolically.<br></p><aside    >There may be other points where this condition is also true, like maxima and saddle points, but these are usually easy to eliminate in practice.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-090" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-090" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0091anim0.svg" data-images="32.Linear.key-stage-0091anim0.svg,32.Linear.key-stage-0091anim1.svg,32.Linear.key-stage-0091anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We are looking for gradients pointing in the same (or opposite) direction, <strong>but not necessarily of the same size</strong>. To state this formally, we say that there must be some value α, such that the gradient of <span class="orange red">f</span> is equal to the gradient of <span class="green">g</span> <em>times α</em>.<br></p><p    >We rewrite to get something that must be equal to zero. By moving the gradient symbol out in front (the opposite of what we usually do with gradients), we see that what we’re looking for is the point where the gradient of some function is equal to zero. This function, of course, is the Lagrangian.<br></p><p    >What we see here is that at the optimum, the derivative of the Lagrangian wrt to the parameters <strong>x</strong>, is zero. This shows why we want to take the derivative of the Lagrangian wrt <strong>x</strong>, and set it to zero. It doesn't yet tell us why we also take the derivative with respect to α, and set that equal to zero as well.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-091">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-091" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0092.svg" class="slide-image" />

            <figcaption>
            <p    >All we need to do now is to figure out what α is. What we've seen is that at the optimum, α is the ratio of the size of the gradient of <span class="orange red">f</span> to the size of the gradient of <span class="green">g</span>,<br></p><p    >The recipe we've already seen just takes the derivative of L wrt α, same as we do wrt to <strong>x</strong>, and sets it equal to zero. It's not immediately intuitive that this is the right thing to do. <br></p><p    >You may think that by setting L <span>∂</span>L/<span>∂</span>α = 0, we are choosing α to optimize the value of L. But L expresses the difference between <span class="orange red">f(x)</span> and α<span class="green">g(x)</span>, not the difference between their gradients. There is no intuitive reason why we'd want <span class="orange red">f(x)</span> and α<span class="green">g(x)</span> to be close together in value, we only want their gradients to match. Our problem statement says that <span class="green">g(x)</span> should be 0, and that the gradients of <span class="orange red">f</span> and <span class="green">g</span> should be the same.<br></p><p    >What's more, we could also have <em>added</em> <span class="orange red">f(x)</span> and α<span class="green">g(x)</span>, according to the recipe, and got the same result. So why does setting <span>∂</span>L/<span>∂</span>α = 0 give us the correct α?<br></p><p    >One way to look at this is that this simply <strong>recovers the constraint</strong>. The multiplier α only appears in front of <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> so taking the derivative w.r.t. α just isolates <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> and sets it equal to zero. This also shows why we can add or subtract the Lagrange multiplier: -<span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> = 0 and <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> = 0 have the same solution.<br></p><p    >This should be enough to convince us that we are doing the right thing, but it's worth investigating what this function L actually looks like.<br></p><p    >We can ask ourselves, if we fix <strong>x</strong>, and find the zero of <span>∂</span>L/<span>∂</span>α this way, aren't we somehow optimizing L? This becomes even more mysterious when we realize that as a function of α, L is simply a 1D linear function (<span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span> and <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> are constant scalars if we take this to be a function of α). The maxima and minima of a linear function are off to positive and negative infinity respectively, so how can we be optimizing a linear function? <br></p><p    >The answer is that when the constraint is satisfied we know that <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> = 0. This means that L = <span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span> - α<span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> = <span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span>, and L becomes constant function: a flat horizontal line.<br></p><p    > In other words, if the constraint isn't satisfied L = <span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span> - α<span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> is a linear function, with no optima, so <span>∂</span>L/<span>∂</span>α = 0 has no solutions. If and only if the constraint is satisfied does <span>∂</span>L/<span>∂</span>α = 0 have a solution, so requiring that <span>∂</span>L/<span>∂</span>α = 0, is the same as requiring that the constraint is satisfied.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-092">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-092" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0093.png" class="slide-image" />

            <figcaption>
            <p    >This is a slightly complex and subtle point to understand about the shape of the Lagrangian function. Where its gradient is 0, it forms a <strong>saddlepoint</strong> (a minimum in one direction and a maximum in another), but that's not necessarily because we are minimizing over <strong>x</strong> and maximizing over α. It's more correct to say that at the optimum for <strong>x</strong>, L as a function of α <em>is constant </em>(it has the same value for all α). When <strong>x</strong> is not at its optimum, L is a linear function of α.<br></p><p    >On the left we've plotted L as a function of α at and near the optimal values of x and y for our example function. When we move x slightly away from the optimum, the function <span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span> - α<span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> becomes some linear function of α. Only when <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> = 0, do we get a constant function.<br></p><p    >On the right, we see the same picture in 3D. We've fixed y at the optimal value and varied x and α. The lines from the plot on the left are highlighted. The solution to the problem is in the exact center of the plot. Note that we have a saddlepoint solution, but it doesn't necessarily have its minimum over x and its maximum over α.<br></p><p    >This is also why we can't find the Lagrangian solution with gradient descent. Gradient descent can be used to find minima, but it doesn't settle on saddlepoints like these. <br></p><aside    >In the methods we use for inequality constraints, we can arrange things so that we are always minimizing over x and maximizing over α. This allows some tricks that don't quite work in this simpler setting.<br></aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-093" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-093" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0094anim0.svg" data-images="32.Linear.key-stage-0094anim0.svg,32.Linear.key-stage-0094anim1.svg,32.Linear.key-stage-0094anim2.svg" class="slide-image" />

            <figcaption>
            <p    >And with that, we have the method of Lagrange multipliers.<br></p><p    >We rewrite the problem so that he constraints are some function that needs to be equal to zero. Then we create a new function L, which consists of <span class="orange red">f</span> with α times <span class="green">g</span> subtracted (or added). For this new function <strong>x</strong> and α are both parameters. Then, we solve for both <strong>x</strong> and α.<br></p><p    >This new function L has an optimum where the original function is minimal within the constraints. The new optimum is a <strong>saddlepoint</strong>. This means we can’t solve it easily by basic gradient descent, we have to set its gradient equal to zero, and solve <em>analytically</em>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-094" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-094" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0095anim0.svg" data-images="32.Linear.key-stage-0095anim0.svg,32.Linear.key-stage-0095anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To deepen our understanding, and to set up some things that are coming up, we can ask ourselves what happens when we have an <em>inactive</em> constraint. What if the global minimum is inside the constraint region, so the solution would be the same with and without the constraint? Ideally, the Lagrangian method should still work, and give us the global minimum.<br></p><p    >In such a case, the gradient of <span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span> will be the zero vector, since it's at a global minimum. The gradient of <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> <em>won't </em>be the zero vector, since we're at a contour of <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span>. Is this an optimum if the gradients aren't pointing in the same direction?<br></p><p    ><br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-095">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-095" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0096.svg" class="slide-image" />

            <figcaption>
            <p    >They are, if we set α to 0. Then the term  α∇<span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> is reduced to the zero vector and it's equal to ∇<span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span> which is equal to the zero vector.<br></p><p    >So why doesn't this always work, even when we have an active constraint? Why can't we always set α=0 and collapse the gradient of the constraint function, so that it's always pointing in all directions at once? The answer is that if we set α equal to zero, we are forcing ∇<span class="orange red">f(</span><strong class="orange red">x</strong><span class="orange red">)</span> to the zero vector, so to its global minimum, which is normally outside the constraint. If we then attempt to solve <span>∂</span>L/<span>∂</span>α = 0, we will not find a solution.<br></p><aside    >If these questions make little sense to you the answer won't either. In that case, it's probably best to just try the basic recipe of Lagrange multipliers a few times on the homework exercises and exam questions and to come back to these questions later to develop your understanding of what's happening.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-096">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-096" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0097.svg" class="slide-image" />

            <figcaption>
            <p    >Finally, If we have <strong>multiple constraints</strong>, the method extends very naturally. With two constraints, we get three gradients: one for the objective function and two for the constraints.We want all all three to be pointing in the same direction, so we add all gradients together, with separate mulitpliers for each constraint. This sum should be equal to zero.<br></p><aside    >In this picture, the constraints by themselves already form a system of equations with only two point solutions. We still find these if we solve the Lagrangian, but at the solution the gradients don't point in the same direction. For a system with multiple constraints where the gradients come in, we need an active constraint region that is larger than a few individual points, which is difficult to do wityh equality constraints in 2 dimensions. </aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-097">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-097" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0098.svg" class="slide-image" />

            <figcaption>
            <p    >Here's what that looks like for two constraints. We end up adding a term to the Lagrangian for each constraint, each with a new multiplier.<br></p><p    >Note that if any of these constraints happens to be inactive, we will simply end up setting their multiplier to zero, and we will very naturally recover the problem with only the active constraints.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-098">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-098" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0099.svg" class="slide-image" />

            <figcaption>
            <p    >Sometimes a problem is too complex to solve use the Lagrangian method. In such cases, you can often still use the method, but instead of solving the problem, you turn one optimization into another one. This second problem is called the <strong>dual problem</strong> of the first. Under the right conditions, the solution to the dual problem also gives you the solution to the original problem.<br></p><p    >This is why the Lagrangian method is relevant to the subject of SVMs: we can't solve the SVM problem analytically, but we<em> can</em> rewrite it into a different problem.<br></p><p    >To illustrate the principle in its most basic form on this very simple problem. To see how it works in detail, and most importantly when it does and doesn't work, you'll have to watch the sixth video.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-099">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-099" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0100.svg" class="slide-image" />

            <figcaption>
            <p    >Here's our start and end points. This problem is very easy to solve explicitly of course, but we'll show you how to translate it to give you a sense of the principle. That way, when we make this step with SVMs, you'll hopefully  understand the basic idea of what's happening, even if you skip the full derivation.<br></p><p    >Note that in the dual problem, the x and y have disappeared and been replaced with α's. These are the Lagrange multipliers: the basic idea is that we set up the Lagrangian, set its derivative equal to zero, and then <strong>rewrite everything in terms of the Lagrange multipliers</strong>, getting rid of all other constraints.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-100" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-100" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0101anim0.svg" data-images="32.Linear.key-stage-0101anim0.svg,32.Linear.key-stage-0101anim1.svg,32.Linear.key-stage-0101anim2.svg,32.Linear.key-stage-0101anim3.svg" class="slide-image" />

            <figcaption>
            <p    >The first step is the same as before: we set up the Lagrangian, and set its derivative equal to zero.<br></p><p    >We then deviate from the standard approach by rewriting these equations to isolate x and y on the left-hand side. We express both as equations of α only (note that we need to be a bit lucky with our problem to be able to do this).<br></p><p    >The derivative with respect to α, <strong>we don't fill in</strong>. We will hold on to this, and use it in a different way.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-101" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-101" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0102anim0.svg" data-images="32.Linear.key-stage-0102anim0.svg,32.Linear.key-stage-0102anim1.svg,32.Linear.key-stage-0102anim2.svg,32.Linear.key-stage-0102anim3.svg" class="slide-image" />

            <figcaption>
            <p    >What we can now do is fill these back into the original Lagrangian. Whatever x and y are at the optimum, the Lagrangian should take this value in terms of the Lagrange multipliers α.<br></p><p    >Now, we require a bit of mental gymnastics. We still have the unused bit of knowledge that at the optimum, the derivative of the Lagrangian should be equal to zero. That's still true of this Lagrangian. In this case, we know how to work that out explicitly, <strong>but imagine that this was too complicated to do</strong> either because the function is too complex, or because there are more constraints active that make things complicated.<br></p><p    >Another route we can take is to recognize that the equation <span>∂</span>L/<span>∂</span>α = 0 <strong>describes an optimum of L</strong>. We saw earlier that in the 3D space of (x, y, α) that ∇L is always <strong>0</strong> at a saddle-point. It turns out, that if we rewrite it like this, expressed in terms of only α, and we get a bit lucky, the optimum corresponds to a minimum or a maximum in α. In this case, L is a second order polynomial in α, so it must have only one minimum or maximum.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-102">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-102" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0103.svg" class="slide-image" />

            <figcaption>
            <p    >Here's the trick in a nutshell. We rewrite the Lagrangian to express it in α. We are assuming the conditions that hold at the optimum, so this form only holds for the optimal x and y. Then we add the assumption that <span>∂</span>L/<span>∂</span>α = 0, and we treat this as an optimization objective.<br></p><p    >We are essentially doing the opposite of what we normally do. We normally start with an optimization objective and set the function's derivative equal to zero. Here we work out a function, assume it's derivative is equal and suppose that this corresponds to the solution to an optimization objective. <br></p><p    >At this point, we don't know whether we'll get a maximum or a minimum, or even a plateau or a saddlepoint. We'll just have to check by hand and hope for the best. In this case, it turns out we get a rather neat maximum, but then this was a particularly simple problem.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-103" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-103" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0104anim0.svg" data-images="32.Linear.key-stage-0104anim0.svg,32.Linear.key-stage-0104anim1.svg,32.Linear.key-stage-0104anim2.svg" class="slide-image" />

            <figcaption>
            <p    >And with that, we have our dual problem. A different optimization problem, that we can use to solve the first. We just optimize for α, and use the relations we worked out earlier to translate the optimal α back to the optimal x and y.<br></p><p    >This is all a bit handwavy, and if you work out a dual problem in this way, you should always keep your eyes wide open and double check that everything works out as you'd hoped. <strong>None of this is guaranteed to work, if you do it like this</strong>.<strong><br></strong></p><p    >If you want a more grounded and formal approach, we need to work out the dual problem slightly differently. This is a bit too much for a BSc level course, but we've included the basics in the sixth video for the sake of completeness.<br></p><aside    >In general, if you want to work out dual problems, it's best to dig a little deeper in to the matter so you get stronger guarantees that what you're doing is correct. The only thing we hope to achieve here is to show the basic principle of working out dual problems, so you get a sense of what's happening when we apply this trick to SVMs.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-104">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-104" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0105.png" class="slide-image" />

            <figcaption>
            <p    >Equality constraints are relatively rare. It's more often the case that you'll run into a an<strong> </strong><em>in</em><strong>equality constraint</strong>: some quantity that is allowed to be equal to or larger than 0, for instance. In such cases, the constraint region becomes a filled-in area in which the solution is allowed to lie.<br></p><p    >Optimization with inequality constraints is not part of the exam, but it is necessary to derive SVMs. If you're not interested in the details, just remember that it's basically the same approach, except we need a little extra administration. If you want to know the details, you can check out part 6 of this lecture.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-105">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-105" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0106.svg" class="slide-image" />

            <figcaption>
            <p    >In the next video, we will return to our constrained optimization objective and apply the KKT method to work out the Lagrangian dual. As we will see, this will allow us to get rid of all parameters except the KKT multipliers</p><p    ></p>
            </figcaption>
       </section>




       <section class="video" id="video-105">
           <a class="slide-link" href="https://mlvu.github.io/lecture06#video-105">link here</a>
           <iframe
                src="https://www.youtube.com/embed/rILXgY0IHxA?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>



       <section id="slide-106">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-106" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0107.svg" class="slide-image" />

            <figcaption>
            <p    >Errata: in the video, the optimization objective for the dual is a minimization objective when it should be a maximization objective. In the notes below, we take the negative of this objective.<br></p><p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-107">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-107" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0108.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the original optimization objective again, before we started rewriting. We will use the method of Lagrange multipliers to rewrite this objective to its<strong> dual problem</strong>.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-108">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-108" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0109.svg" class="slide-image" />

            <figcaption>
            <p    >First, we rewrite the objective function and the constraints a little to make things easier down the line. We turn the norm of <strong class="orange">w</strong> into its dot product. This is just a question of removing the square root so it doesn't change the location of the minimum.<br></p><p    >In the constraints, we move everything to the right, so that all constraints are "greater than or equal to 0."</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-109">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-109" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0110.svg" class="slide-image" />

            <figcaption>
            <p    >As we announced already, the SVM view follows from working out the dual problem to the soft margin SVM problem. <br></p><p    >We've seen this done for a simple problem already: (1) we work out the Lagrangian, set its partial derivatives equal to zero, (2) we use these equations to rewrite the Lagrangian to eliminate all variables except the Lagrange mulitpliers, (2) we cast the solution back to an optimization problem, optimizing only over the multipliers.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-110">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-110" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0111.svg" class="slide-image" />

            <figcaption>
            <p    >Here, we will skip a step. This derivation is simply too long and complicated for a BSc course. We will just show you the optimization problem at the top, and tell you that if you set up the Lagrangian and work out the dual problem, and do a little rewriting, you end up with the objective at the bottom. <br></p><p    ><br></p><p    >There's an optional sixth video, for if you really want or need to know how this works, but if you don't, you can take my word for it: these two problems lead to the same solution, which is the maximum margin hyperplane.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-111">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-111" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0112.svg" class="slide-image" />

            <figcaption>
            <p    >You may need to stare at the dual problem a little bit to see what you are looking at.<br></p><p    ><br></p><p    >Note the following:<br></p><p     class="list-item">The α's are the Lagrange multipliers that were introduced for the first constraint of each point. That is, we are assigning each instance in the data a number alpha. Remember from the previous video that at the optimum, these are 0 if the constraint is inactive, and nonzero if the constraint is active.<br></p><p     class="list-item">The α's are the only <em>parameters</em> of the problem. The <strong>x</strong>'s and y's are simply values from the data.<br></p><p     class="list-item">The second constraint also received a multiplier, β<sub>i</sub>, but this was removed from the optimization in rewriting.<br></p><p     class="list-item">The first problem sums once over the dataset. The second sums twice, with indices i and j. This means we are essentially looking at two nested loops, looking at all pairs of instances over the data.<br></p><p     class="list-item">For each pair, of any two instances, we compute the product of their multipliers α<sub>i</sub>α<sub>j</sub>, the product of their labels y<sub>i</sub>yj and their dot product. Summing these all up, we get the quantity that we want to minimize.<br></p><p     class="list-item">Because we started with a problem with inequality constraints, we don't end up with a problem without constraints. Instead we get a problem with constraints over the multipliers.<br></p><p     class="list-item">There is also a kind of penalty term keeping the sum of all alphas down.<br></p><p     class="list-item">The slack parameter <span class="orange red">C</span> now functions to keep the alphas in a fixed range.<br></p><p     class="list-item">The final line says that the sum of all the alphas on the positive examples must equal the sum of all the alphas on the negative examples.<br></p><p     class="list-item"><br></p><p    >Finally, note that unlike in the Lagrangian examples, we haven't ended up with anything we can solve analytically. We've just turned one constrained optimization problem into another one. We'll still need a solver that can handle constrained optimization problems. We won't go into the details, but the <a href="https://en.wikipedia.org/wiki/Sequential_minimal_optimization"><strong class="blue">SMO algorithm</strong></a> is a popular choice for SVMs.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-112" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-112" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0113anim0.svg" data-images="32.Linear.key-stage-0113anim0.svg,32.Linear.key-stage-0113anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Of course the solution means nothing to us in terms of the Lagrange multipliers, since these are variables that we introduced ourselves. Once we've found the optimal multipliers, we need to translate them back to a form that allows us to make classifications.<br></p><p    >The simplest thing to do is to translate them back to the hyperplane parameters <strong class="orange">w</strong> and <span class="blue">b</span>. As we saw in the previous video, the relation between the multipliers and the parameters of the original problem usually emerges from setting the Lagrangian derivative equal to zero. From this, we see that the vector <strong>w</strong> is a weighted sum over the support vectors, each multiplied by its label.<br></p><p    >This makes sense if you remember that <strong class="orange">w</strong> is the direction in which the hyperplane ascends the quickest. That is, it's the direction in which our model thinks the the points become most likely to be positive. In this sum, we are adding together all the positive support vectors, weighted by their Lagrange multiplier, and subtracting the same sum for the negative support vectors.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-113" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-113" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0114anim0.svg" data-images="32.Linear.key-stage-0114anim0.svg,32.Linear.key-stage-0114anim1.svg,32.Linear.key-stage-0114anim2.svg,32.Linear.key-stage-0114anim3.svg,32.Linear.key-stage-0114anim4.svg,32.Linear.key-stage-0114anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Here's a visualization of how the different Lagrange multipliers combine to define <strong class="orange">w</strong>. We have two support vectors for the negative class, and one for the positive class. The weights for both classes need to sum to the same value (the second constraint in the dual problem), so the weights for the negative vectors need to be half that of the weight for the positive vector.<br></p><p    >The second term in the objective function tells us that we'd like the multipliers to be as big as possible, and the first constraint suggests that the largest multiplier can be no bigger than C. Assuming we've set C=1, we get the multiplier values shown here.<br></p><p    >The relation in the previous slide now tells us that at the optimum, <strong class="orange">w</strong> is the weighted sum of all suppoort vectors, with the negative ones subtracted and the positive ones added.<br></p><p    >If we scale the support vectors by the multipliers, we can draw a simple vector addition to show how we arrive at <strong class="orange">w</strong>.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-114" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-114" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0115anim0.svg" data-images="32.Linear.key-stage-0115anim0.svg,32.Linear.key-stage-0115anim1.svg,32.Linear.key-stage-0115anim2.svg,32.Linear.key-stage-0115anim3.svg" class="slide-image" />

            <figcaption>
            <p    >Once we have our solution in terms of the Lagrange multipliers, we need to use them somehow to work out what class to assign to a new point that we haven't seen before.<br></p><p    >The first option is simply to compute <strong>w</strong> from the Lagrange multipliers and use w and b as you normally do in a linear classifier. However, this doesn't work with the method coming up. There, we never want to compute <strong>w</strong> explicitly because it might be too big. Instead, we can take the definition of w in terms of the multipliers, and fill it into our classification objective. <br></p><p    >What we see is that by computing a weighted sum over the dot products of the new instance x<sub>new</sub> with all instances in the data. Or rather, with all support vectors, since the multipliers are zero for the non-support vectors.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-115">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-115" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0117.svg" class="slide-image" />

            <figcaption>
            <p    >So why did we do all this if we still need to <em>search</em> for a solution? We had a version that worked with gradient descent, and now we have a version that requires constrained optimization. <strong>What have we gained?</strong><br></p><p    >The main results here are twofold:<br></p><p    >First, notice that the hyperplane parameters <strong class="orange">w</strong> and <span class="blue">b</span> have <em>disappeared</em> entirely from the objective and its constraints. The only parameters that remain are one α<sub>i</sub> per instance i in our data, and the hyperparameter <span class="orange red">C</span>. The alphas function as an encoding of the support vectors: <strong>any instance for which the corresponding alpha is not zero is a support vector</strong>. Remember that nonzero Lagrange multipliers correspond to inactive constraints. Only the constraints for the support vectors are active.<br></p><aside    >We could use this to reduce the data to only its support vectors. For the purposes of the classifier, these instances define the decision boundary, and the rest can be deleted.<br></aside><p    >Second, note that the algorithm only operates on the <strong>dot products</strong> of pairs of instances. In other words, if you didn’t have access to the data, but I <em>did</em> give you the full matrix of all dot products of all pairs of instances, you would still be able to find the optimal support vectors. This allows us to use a very special trick.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-116">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-116" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0118.svg" class="slide-image" />

            <figcaption>
            <p    >What if I didn’t give you the actual dot products, but instead gave you a different matrix of values, that <em>behaved </em>like a matrix of dot products.<br></p><p    >A <strong>kernel function</strong> is a function of two vectors that behaves like a dot product, but in a higher dimensional feature space. This will take a bit of effort to wrap your head around, so we'll start at the beginning.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-117">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-117" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0119.png" class="slide-image" />

            <figcaption>
            <p    >Remember, by adding features that are derived from the original features, we can make linear models more powerful. If the number of features we add grows very quickly (like if we add all 5-way cross products), this can becomes a little expensive (both memory and time wise).<br></p><p    >The kernel trick is basically a souped-up version of this idea.<br></p><p    >It turns out that for some feature expansions,<strong> we can compute the dot product between two instances in the expanded features space without explicitly computing all expanded features</strong>.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-118">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-118" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0120.svg" class="slide-image" />

            <figcaption>
            <p    >Let’s look at an example. The simplest way we saw to extend the feature space was to add <strong>all cross-products</strong>. This turns a 2D dataset into a 5D dataset. Let's se if we can do this, or something similar, without computing the 5D vectors.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-119" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-119" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0121anim0.svg" data-images="32.Linear.key-stage-0121anim0.svg,32.Linear.key-stage-0121anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here are two 2D feature vectors. What if, instead of computing their dot product, we computed the <em>square</em> of their dot product. <br></p><p    >It turns out that this is equal to the dot product of two other 3D vectors <strong>a’</strong> and <strong>b’</strong>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-120" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-120" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0122anim0.svg" data-images="32.Linear.key-stage-0122anim0.svg,32.Linear.key-stage-0122anim1.svg,32.Linear.key-stage-0122anim2.svg,32.Linear.key-stage-0122anim3.svg,32.Linear.key-stage-0122anim4.svg" class="slide-image" />

            <figcaption>
            <p    >The square of the dot product in the 2D feature space, is equivalent to the regular dot product in a 3D feature space. The new features in this 3D space can all be derived from the original features. They're the three cross products, with a small multiplier on the a<sub>1</sub>a<sub>2</sub> cross product.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-121" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-121" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0123anim0.svg" data-images="32.Linear.key-stage-0123anim0.svg,32.Linear.key-stage-0123anim1.svg,32.Linear.key-stage-0123anim2.svg,32.Linear.key-stage-0123anim3.svg" class="slide-image" />

            <figcaption>
            <p    >That is, this kernel function <span class="orange">k</span> doesn't compute the dot product between two instances, but it does compute the dot product in a feature space of <em>expanded</em> features. We could do this already, but before we had to actually <em>compute</em> the new features. <strong>Now, all we have to do is compute the dot product in the original feature space and square it.</strong></p><p    ><strong></strong></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-122">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-122" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0124.svg" class="slide-image" />

            <figcaption>
            <p    >Since the solution to the SVM is expressed purely in terms of the dot product, we can replace the dot product this <span class="orange">kernel function</span>. We are now fitting a line in a higher-dimensional space, without computing any extra features explicitly.<br></p><p    >Note that this only works because we rewrote the optimization objective to get rid of <strong class="orange">w</strong> and<span class="blue"> b</span>. Since <strong class="orange">w</strong> and<span class="blue"> b</span> have the same dimensionality as the features, keeping them in means using explicit features.<br></p><p    >Saving the trouble of computing a few extra features may not sound like a big saving, but by choosing our kernel function cleverly we can push things a lot further.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-123">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-123" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0125.svg" class="slide-image" />

            <figcaption>
            <p    >For some expansions to a higher feature space, we can compute the dot product between two vectors, <strong>without explicitly expanding the features</strong>. This is called a <strong>kernel function</strong>.<br></p><p    >There are many functions that compute the dot product of two vectors in a highly expanded feature space, but don’t actually require you to expand the features.<br></p><aside    >There are some straightforward conditions for when a given function of two vectors is a kernel. We won't worry about that now, and just look at some commonly used kernels, assuming that others have done the work to show that these actually are kernels.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-124">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-124" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0126.svg" class="slide-image" />

            <figcaption>
            <p    >Taking just the square of the dot product, as we did in our example, we lose the original features. If we take the square of the dot product<strong> plus one</strong>, it turns out that we retain the original features, <em>and</em> get all cross products. <br></p><aside    >You'll show how this works in the homework.<br></aside><p    >If we increase the exponent to <span class="orange red">d</span> we get all <span class="orange red">d</span>-way cross products. Here we can see the benefit of the kernel trick. Imagine setting <span class="orange red">d</span>=10 for a dataset with a modest 10 features. Expanding all 10-way cross-products of all features would give each instance<em> 10 trillion</em> expanded features. We wouldn't even be able to fit one instance into memory.<br></p><p    >However, if we use the kernel trick, all we need to do is to compute the dot product in the original feature space, add a 1, and raise it to the power of 10.<br></p><aside    ><span class="orange red">d</span> is a hyperparameter: increasing it does not make the algorithm much more expensive, but it does increase your (implicit) feature space so much that you risk overfitting, so you'll need to tune it to your data.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-125" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-125" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0127anim0.svg" data-images="32.Linear.key-stage-0127anim0.svg,32.Linear.key-stage-0127anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If ten trillion expanded features sounded like a lot, here is a kernel that corresponds to an infinite-dimensional expanded feature space. We can only approximate this kernel with a finite number of expanded features, getting closer as we add more. Nevertheless, the kernel function itself is very simple to compute.<br></p><p    >Gamma is another hyperparameter.<br></p><p    >Because this is such a powerful kernel, it is prone to overfitting.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-126">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-126" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0128.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s a plot for the dataset from the first lecture. As you can tell, the RBF kernel massively overfits for these hyperparameters, but it does give us a very nonlinear fit.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-127">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-127" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0129.svg" class="slide-image" />

            <figcaption>
            <p    >One of the most interesting application areas of kernel methods is places where you can turn a distance metric in your data space directly into a kernel, <strong>without first extracting any features at all</strong>.<br></p><p    >For instance for an email classifier, you don't need to extract word frequencies, as we’ve done so far, you can just design a kernel that operates directly on strings (usually based on the edit distance).Put simply, the fewer operations we need to turn one email into another, the closer we put them together. If you make sure that such a function behaves like a dot product, you can stick it in the SVM optimizer as a kernel. <strong>You never need to deal with any features at all.</strong> Just the raw data, and their dot products in some feature space that you never compute.<br></p><aside    >This approach has often been used to analyze DNA and protein sequences in bioinformatics.<br></aside><p    >If you’re classifying graphs, there are distance metrics like the Weisfeiler-Lehman algorithm that you can use to define kernels.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-128">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-128" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0130.svg" class="slide-image" />

            <figcaption>
            <p    >Kernel SVMs are complicated beasts to understand, but they're easy to use with the right libraries. Here's a simple recipe for fitting an SVM with an RBF kernel in sklearn.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-129">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-129" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0131.svg" class="slide-image" />

            <figcaption>
            <p    >Neural nets require a lot of passes over the data, so it takes a big dataset before kN becomes smaller than N<sup>2</sup>, but eventually, we got there. At that point, it became more efficient to train models by gradient descent, and the kernel trick lost its luster.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-130">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-130" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0132.svg" class="slide-image" />

            <figcaption>
            <p    >And when neural networks did come back, they caused a revolution. That’s where we’ll pick things up next lecture.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-131" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-131" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0133anim0.svg" data-images="32.Linear.key-stage-0133anim0.svg,32.Linear.key-stage-0133anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To make the story complete, we need to know two things that we've skipped over. How to solve problems with inequality constraints, and how to use this method to work out the dual problem for the SVM. <br></p><p    ><strong>These are explicitly not exam material. </strong>We've separated them into this video so that you can watch them if you need the whole story, or if you want to get a sense of what the missing steps look like, but you are entirely free to skip this video.<br></p><p    ></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-132">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-132" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0134.png" class="slide-image" />

            <figcaption>
            <p    >To start with, let's look at the details of how to handle inequality constraints. For instance, if you want you solution to lie anywhere within the unit circle, instead of on the unit circle.<br></p><p    >This method, called the method of KKT multipliers is necessary to understand how we derive the kernel trick in the next video. It won't, however, be an exam or homework question, so you're free to skim the rest of this video if you've reached your limit of math.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-133" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-133" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0135anim0.svg" data-images="32.Linear.key-stage-0135anim0.svg,32.Linear.key-stage-0135anim1.png" class="slide-image" />

            <figcaption>
            <p    >Lagrange multipliers work great, and are very useful, but so far we've only seen what to do if the constraint is an equality: if some quantity needs to stay exactly equal to some other quantity. It's more often the case that we have an inequality constraint: for instance, the amount of money we spend needs to stay within our budget.<br></p><p    >If the constraint in our problem is not an equality constraint, but an <em>in</em>equality constraint, the same method applies, but we need to keep a few more things in mind.<br></p><p    >Here is an example. This time we are not looking for a solution on the unit circle, we are looking for the lowest point anywhere <em>outside</em> the unit circle.<br></p><p    >This means that our constraint is <strong>inactive</strong>. The simplest approach for a particular problem is just to check manually if the constrain tis active. If it isn't, you can just solve the unconstrained problem, and if it is, the solution must be on the boundary of the constraint region, so the problem basically reduces to the standard Lagrangian method.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-134" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-134" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0136anim0.png" data-images="32.Linear.key-stage-0136anim0.png,32.Linear.key-stage-0136anim1.png" class="slide-image" />

            <figcaption>
            <p    >For this problem, if we search only<em> inside</em> the unit circle, the constraint is <strong>active</strong>. It stops us from going where we want to go, and we end up on the boundary, just like we would if the constraint were an equality constraint. This means that if we know that we have an active constraint, our solution should coincide with the equivalent problem with an equality constraint. For this reason, we can use almost the same approach. We just have to set it up a little bit more carefully, so that we restrict the allowed solutions a bit more.<br></p><p    >We first set the convention that all constraints are rewritten to be “greater than” inequalities, with zero on the right hand side. This doesn’t change the region we’re constrained to, but note that the function on left of the inequality sign had a “bowl” shape before, and now has a “hill” shape. In other words, the gradients of this function now point in the opposite direction. <br></p><p    >The drawings indicate the 1D equivalent. The places where the two functions intersect (the boundary of our constraint region) are the same, but the constraint function is flipped around. This means that its gradient (the direction of steepest ascent) now points in the opposite direction.<br></p><p    >We now know two things: the inequality is always a "greater than" inequality (by convention), and the constraint function is always a "hill" shape and never a "bowl" shape (if it were a bowl shape with a greater than constraint, the constraint would be inactive in this case).<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-135">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-135" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0137.png" class="slide-image" />

            <figcaption>
            <p    >If we are <strong>minimizing</strong>, we need to make sure that the gradient points<strong> into</strong> the constrained region, so that the direction of steepest descent points outside. If the direction of steepest descent pointed into the region, we could find a lower point somewhere inside, away from the boundary. Since the gradient for the constraint function points inside the region, we need to make sure that the gradients of the <span class="orange red">objective function</span> point in the same direction.<br></p><p    >If we are <strong>maximizing</strong>, by the same logic, we need to make sure that the gradients point in opposite directions. We want to direction of greatest ascent to point outside the constraint region.<br></p><p    >Contrast this with case of equality constraints. There, we just needed to make sure that the gradients were on the same line, either pointing in the same direction or in opposite directions. Since the constraint was a 1D curve, the gradients and negative gradients always point outside of the constraint region. Now, we need to be a bit more careful. Since we tend to minimize in machine learning, we'll show that version in detail.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-136" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-136" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0138anim0.svg" data-images="32.Linear.key-stage-0138anim0.svg,32.Linear.key-stage-0138anim1.svg,32.Linear.key-stage-0138anim2.svg" class="slide-image" />

            <figcaption>
            <p    >This makes the derivation the inequality method a little more complicated than the version with an equality constraint: we again set the gradient of the<span class="orange red"> objective function</span> equal to that of <span class="green">the constraint</span>, again with an α to account for the differences in size between the two gradients, but this time around, we need to make sure that <strong>α remains positive</strong>, since a negative α would cause the gradient of the constraint to point in the wrong direction.<br></p><aside    >We assume we're minimizing. If we are maximizing, we set the gradient of f equation to the negative gradient of g times α.<br></aside><p    >Even though we’ve not removed the constraint, we’ve simplified it a lot: it is now a linear function, even a constant one, instead of a nonlinear function. Linear constraints are much easier to handle, for instance using methods like linear programming, or gradient descent with projection. If you're lucky, you may even be able to solve it analytically still.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-137">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-137" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0139.svg" class="slide-image" />

            <figcaption>
            <p    >All this only works if we check manually whether a constraint is active. Sometimes this isn't practical: we may have too many constraints, or we may want to work out a solution independent of the specifics. For instance, in the SVM problem, we can only check which constraints are active once we know the data. If we want to work out a solution that holds for any dataset (with the data represented by uninstantiated variables), we can't check manually which constraints are active.<br></p><p    >Instead, we can work the activity checking into the optimization problem using a condition called <strong>complementary slackness</strong>.<br></p><p    >Remember what we saw for the Lagrangian case: if the constraint is inactive, we can simply set the multiplier to 0 and the problem reduces to the unconstrained problem.<br></p><p    >However, if we don't set the multiplier to zero, we need to make sure that the constraint is active, and stays on the boundary. We can achieve this by requiring that <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> is exactly 0 rather than larger than or equal to zero.<br></p><p    >In short either α is exactly zero, or <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> is.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-138">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-138" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0140.svg" class="slide-image" />

            <figcaption>
            <p    >We can summarize this requirement by saying that the product of the multiplier and the constraint function should be exactly zero. This condition is called<strong> complementary slackness</strong>.<br></p><p    >If we allow the solution to move away from the constraint boundary to the interior of the constraint region, <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> will become nonzero (because the boundary is where it is zero), so the α should be zero to satisfy complementary slackness. This will effectively remove the <span class="green">g</span> term from the Lagrangian, forcing us to find the global minimum of <span class="orange red">f</span>.<br></p><p    >If <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> is on the boundary and so equal to zero, we are allowing α to be <em>non</em>zero, this means that the <span class="green">g</span> term in the Lagrangian will be active, and we don't need to find the global minimum of f , where its gradient is zero, only the constrained minimum, where its gradient is equal to α∇<span class="green">g(</span><strong class="green">x</strong><span class="green">)</span>.<br></p><aside    >Complimentary slackness can be a little confusing to wrap your head around. For me, the key is viewing the term we add to the Lagrangian as a <span>relaxation</span> of the problem. It allows us to move away from the global optimum to a constrained optimum. To allow this we need to make the multiplier α non-zero, and the price we pay to do that is to make <span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> equal to zero.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-139">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-139" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0141.svg" class="slide-image" />

            <figcaption>
            <p    >Here's what the general solution looks like. We start with an optimization objective. We construct a Lagrangian-like function as before, but this time, we don't require that its whole gradient is equal to zero, just the objective functions and the constraint terms. In other words,<strong> we don't require that the derivative with respect to the multiplier is zero</strong>. <br></p><aside    >You can still start with the Lagrangian. You just don't set all of its partial derivatives equal to zero.<br></aside><p    >This is because the constraint may not be active: in that case the multiplier itself is zero and the gradient can take any value.<br></p><p    >This equation may have many solutions, not all of which will be solutions to the optimization problem. The Karush-Kuhn-Tucker (KKT) conditions then tell us which of these solutions also solve the optimization problem. <br></p><p    >It may seem a little counter-intuitive that this is actually a step forward. We had a simple minimization objective with a single constraint, and now we have to solve an equation under several constraint, including the original. Are we really better off? There are two answers. In some rare cases, you can actually solve the problem analytically. We'll see an example of that next. In other cases, you can use the KKT conditions to formulate a<strong> dual problem</strong>. We'll dig into that after the example.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-140">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-140" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0142.svg" class="slide-image" />

            <figcaption>
            <p    >If we have multiple inequality constraints, we just repeat the procedure with fresh multipliers for each. Each constraint gets its own set of three KKT conditions.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-141" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-141" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0143anim0.svg" data-images="32.Linear.key-stage-0143anim0.svg,32.Linear.key-stage-0143anim1.svg,32.Linear.key-stage-0143anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We can also mix equality and inequality constraints. In this case, we just treat the equality constraint the same as we did before. We set the KKT conditions for the inequality constraint(s) and for the equality constraint, we only set the condition that the original equality is true. As we saw before, this is equivalent to constructing the Lagrangian and requiring that its derivative with respect to the multiplier of the equality constraint is zero.<br></p><aside    >You can do it both ways, but since you are already including the original inequality constraint as one of the KKT conditions, you may as well include the original equality constraint as well.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-142">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-142" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0144.svg" class="slide-image" />

            <figcaption>
            <p    >Here's an example of when you can solve a KKT problem analytically.<br></p><p    >When we introduced entropy, we noted that the cross entropy of a function with itself was the lowest that the cross entropy could get. The implication was that the average codelength is minimized if we choose a code that corresponds to the source distribution of the elements we are trying to transmit.<br></p><p    >For a finite space of outcomes, we can now prove this with the Lagrangian method. Here's how we set up the problem. We will assume that we have n outcomes over which the probabilities are defined. The source the outcomes are drawn from is called <span class="orange red">p</span>, and it assigns probabilities <span class="orange red">p</span><sub>1</sub> through <span class="orange red">p</span><sub>n</sub>. We encode messages using a code corresponding to distributions <span class="blue">q</span>, which assigns probabilities <span class="blue">q</span><sub>1</sub> though <span class="blue">q</span><sub>n</sub>, and thus uses codewords of lengths - log <span class="blue">q</span><sub>1</sub> though -log <span class="blue">q</span><sub>n</sub>.<br></p><p    >The expected codelength under this scheme is the cross-entropy between <span class="orange red">p</span> and <span class="blue">q</span>. What we want to show is that setting <span class="blue">q</span>=<span class="orange red">p</span> will minimize the expected codelength.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-143" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-143" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0145anim0.svg" data-images="32.Linear.key-stage-0145anim0.svg,32.Linear.key-stage-0145anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here's how that looks as a minimization problem. We want to find the n values for <span class="blue">q</span><sub>i</sub> for which the corss entropy is minimized. The values of <span class="orange red">p</span><sub>i</sub> are given (we treat them as a constant).<br></p><p    >The constraints essentially state that the <span class="blue">q</span><sub>i</sub> values put together are <em>probabilities</em>. They should be non-negative and they should collectively sum to 1. This gives us n inequality constraints and one equality constraints.<br></p><p    >The only thing we need to do to put the constraint into the correct form is to move the 1 to the left hand side.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-144">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-144" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0146.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the Lagrangian we get. Note that it has 2n + 1 parameters: the original n parameters <span class="blue">q</span><sub>i</sub>, the multipliers of the inequalities α<sub>i</sub> and one more for the multiplier of the equality β.<br></p><p    >The additional constraints are only on the multipliers for the inequalities. They tell us that both the α<sub>i</sub> multipliers and the <span class="blue">q</span><sub>i</sub> parameters should be positive, and that at least one of them should be zero. <br></p><p    >Remember that we won't be working out the whole gradient of the Lagrangian, only the gradient with respect to the original parameters and the equality constraints.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-145">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-145" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0147.svg" class="slide-image" />

            <figcaption>
            <p    >We start by working out the relvant partial derivatives of the Lagrangian and setting them equal to zero.<br></p><p    >On the left we have the equations resulting from this: n equations for the original parameters, and one for the equality constraint. Again, for the multipliers corresponding to inequality constraints, we don't set the derivative equal to zero: for those we rely on the KKT conditions instead.<br></p><p    >At this point, there's no standard, mehcanical way to proceed. We need to look at what these equations and inequalities are telling us. If we're lucky, there's a way to solve the problem, and if we're even luckier, we're clever enough to find it.<br></p><p    >We can start with the following observations:<br></p><p     class="list-item">The parameters <span class="blue">q</span><sub>i</sub> must be positive and sum to zero. This means that they can't all be zero.<br></p><p     class="list-item">For those that are nonzero, α<sub>i</sub> must be zero, due to complementary slackness. So for the nonzero <span class="blue">q</span><sub>i</sub>, we have <span class="orange red">p</span><sub>i</sub>/<span class="blue">q</span><sub>i</sub> = - β and thus <span class="blue">q</span><sub>i</sub> = - <span class="orange red">p</span><sub>i</sub>/β.<br></p><p     class="list-item">All nonzero <span class="blue">q</span><sub>i</sub> should sum to one, so we have -(1/β)Σ<span class="orange red">p</span><sub>i</sub> = 1 (with the sum over those i's corresponding to nonzero <span class="blue">q</span><sub>i</sub>)<br></p><p    >At this point, we run into a snag. We need to know something about those <span class="blue">q</span><sub>i</sub>'s that are zero, but in that case, the first term of the first inequality, -<span class="orange red">p</span><sub>i</sub>/<span class="blue">q</span><sub>i</sub>, becomes undefined. The main thing to note is that this is a problem with our domain, not with the Lagrangian/KKT method. Note that in the entropy, we have a factor log <span class="blue">q</span><sub>i</sub> which goes to negative infinity as <span class="blue">q</span><sub>i</sub> goes to zero. The entropy isn't really properly defined for zero probabilities, so it's no surprise that we run into difficulty with the Lagrangian/KKT method for zero probabilities.<br></p><p    >The way we deal with this in entropy is to say that the length of the code word for i, - log <span class="blue">q</span><sub>i</sub>, goes to infinity as the probability goes to zero. If we are absolutely sure that the outcome i won't happen, we can assign it an "inifinitely long codeword" by setting <span class="blue">q</span><sub>i</sub>=0 (allowing us to make the other codewords shorter, by giving them more probability mass). We do, however, have to be<em> absolutely sure</em> that the i will never happen, that it that <span class="orange red">p</span><sub>i</sub> is also 0. If pi is anywhere above 0, no matter how small, and <span class="blue">q</span><sub>i</sub>=0 the expected codelength (the cross entropy) becomes infinite, because there is a non-zero probability that we'll need to transmit an infinitely long codeword.<br></p><p    >The conclusion of all of this is that if any of our <span class="blue">q</span><sub>i</sub> are 0 and the corresponding <span class="orange red">p</span><sub>i</sub> aren't, the objective function is infinite and we are as far from our minimum as we can be. Thus, we may conclude that if <span class="blue">q</span><sub>i</sub> is zero at an optimum, then <span class="orange red">p</span><sub>i</sub> is also zero. Conversely, if <span class="orange red">p</span><sub>i</sub> is zero and <span class="blue">q</span><sub>i</sub> isn't, we know we can't be at an optimum, because we could move probability mass away from qi to outcomes that have nonzero probabilty.<br></p><p    >All this should convince you that at the optimum, the nonzero <span class="blue">q</span><sub>i</sub>'s correspond exactly to the nonzero <span class="orange red">p</span><sub>i</sub>'s. This means that -(1/β)Σ<span class="orange red">p</span><sub>i</sub> = 1 = Σ<span class="orange red">p</span><sub>i</sub>, so β must be -1, and we have <span class="blue">q</span><sub>i </sub>= <span class="orange red">p</span><sub>i</sub> for all i.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-146">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-146" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0148.svg" class="slide-image" />

            <figcaption>
            <p    >The other approach we saw in the earlier video, is not to <em>solve</em> the optimization problem, but to turn it into a different problem: the so called dual problem of the first. We were a bit handwavy in our first explanation, skipping a lot of the details, and being vague about when it works and why. Now, in the context of optimization under inequality constraints, we can be more clear about exactly what we're doing.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-147" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-147" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0149anim0.svg" data-images="32.Linear.key-stage-0149anim0.svg,32.Linear.key-stage-0149anim1.svg,32.Linear.key-stage-0149anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We'll explain this first in the context of a basic minimization problem with a single inequality constraint. The approach of dual problems makes most sense in the context on inequality constraints, so now that we have the machinery for this, we can give it a proper treatment.<br></p><p    >We know that for any solution that satisfies the KKT conditions, the term α<span class="green">g(</span><strong class="green">x</strong><span class="green">)</span> must be positive. This means that whenever <strong>x</strong> satisfies the KKT conditions, we know that the Lagrangian at <strong>x</strong> is always strictly<em> less </em>than the the objective function <span class="orange red">f</span> at <strong>x</strong>.<br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-148" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-148" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0150anim0.svg" data-images="32.Linear.key-stage-0150anim0.svg,32.Linear.key-stage-0150anim1.svg,32.Linear.key-stage-0150anim2.svg" class="slide-image" />

            <figcaption>
            <p    >For all nonnegative a, and x satisfying the constraint, this tells us that the Lagrangian is less than the objective function. This includes the x for which L is minimal (under the constraints). <br></p><p    >Since this is always true, regardless of our value of a, we can now choose a to <em>maximize</em> this function. </p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-149" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-149" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0151anim0.svg" data-images="32.Linear.key-stage-0151anim0.svg,32.Linear.key-stage-0151anim1.svg,32.Linear.key-stage-0151anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Here's a visualization. We are looking for the minimum on the red line f(<strong>x</strong>), within the region where the green line g(<strong>x</strong>)is larger than 0.<br></p><p    >If we construct L, and pick some positive value a, we get a line that within the constrain region lies below f(<strong>x</strong>). If we keep <strong>x</strong> fixed and change a to a' in such a way that L(x, a') is bigger than L(x, a), we move the minimum closer to the optimal value.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-150">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-150" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0152.svg" class="slide-image" />

            <figcaption>
            <p    >Here are the proper definitions of the primal and dual problem. "primal" is just the opposite of dual, the problem we started out with.<br></p><p    >What we have done is to remove <strong>x</strong> as a variable, by setting it to the value it has at the minimum within in the constraint region. This leaves the Lagrange multipliers as the only free variable to maximize over. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-151">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-151" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0153.svg" class="slide-image" />

            <figcaption>
            <p    >We have not shown that the value we get for the dual problem is actually the same as the one we get for the dual. Only that it is less than or equal. This is called <strong>weak duality</strong>: the dual serves as a lower bound for the primal. This is always true.<br></p><p    >If they are exactly equal, we say that <strong>strong duality</strong> holds. It can be shown that this is true if and only if all three KKT conditions holds for the solution. Two of them are already included in the dual problem.We're just missing complimentary slackness. We can either define the problem with complimentary slackness added, or we can figure out the dual without complimentary slackness, and then check whether it holds for the solution.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-152">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-152" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0154.svg" class="slide-image" />

            <figcaption>
            <p    >Before we use these principles to work out the dual for the SVM problem, let's see it in action on a slightly simpler problem. We'll use the problem from the fourth part, but with an inequality constraint instead of an equality constraint.<br></p><p    >The constraint is active, so the solution will be the same as before, but we'll take you through the formal steps of formulating the dual problem. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-153">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-153" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0155.svg" class="slide-image" />

            <figcaption>
            <p    >As before, we set up the Lagrangian, but this time, we start by setting up the dual function f', which halp alpha as an argument and contains a minimization over x and y.<br></p><aside    >Note that the minimization is over values of x and y that satisfy the original constraints.<br></aside><p    >We then maximize this value of f subject to the KKT conditions. To make this practical, we need to rewrite the dual function to eliminate all references to x and y. We do this by making the assumption that x and y are at the optimum: <strong>the derivative of the Lagrangian is zero for them</strong>.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-154" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-154" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0156anim0.svg" data-images="32.Linear.key-stage-0156anim0.svg,32.Linear.key-stage-0156anim1.svg,32.Linear.key-stage-0156anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We worked this out already in slide 100. Under this assumption, we can express x and y in terms of the value of alpha.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-155">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-155" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0157.svg" class="slide-image" />

            <figcaption>
            <p    >As we saw before, filling in these derivatives gives us an objective function that is a simple parabola in α. The parabola has it's maximum at α=1, so we get weak duality at that value. do we also get strong duality? We should check the KKT conditions to find out.<br></p><p    >The first says that α should be nonnegative, and the second says that it should be larger or equal to 1. We can ignore the first, but either way our solution satisfies them both.<br></p><p    >The complementary slackness is an equation with two solutions α=0 and α=1. The second corresponds to our solution, so we do indeed have strong duality. <br></p><p    >Filling α=1 into the equations we derived before will tell us where in the x, y plane we will find this solution.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-156">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-156" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0158.svg" class="slide-image" />

            <figcaption>
            <p    >We are now ready to begin our attack on the SVM objective. This is a much more complicated beast than the problems we've seen so far, but so long as we stick to the plan, and work step by step, we should be fine.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-157" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-157" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0159anim0.svg" data-images="32.Linear.key-stage-0159anim0.svg,32.Linear.key-stage-0159anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here are the start and end points of our journey. The objective at the bottom is the dual problem of the one at the top.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-158" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-158" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0160anim0.svg" data-images="32.Linear.key-stage-0160anim0.svg,32.Linear.key-stage-0160anim1.svg,32.Linear.key-stage-0160anim2.svg,32.Linear.key-stage-0160anim3.svg,32.Linear.key-stage-0160anim4.svg" class="slide-image" />

            <figcaption>
            <p    >First, we define our Lagrangian. We introduce two sets of multipliers: α's for the first type of constraint, and β's for the second type of constraint. If our datasets has n instances, we add n α's and n β's.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-159" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-159" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0161anim0.svg" data-images="32.Linear.key-stage-0161anim0.svg,32.Linear.key-stage-0161anim1.svg,32.Linear.key-stage-0161anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Next, we'll rewrite the Lagrangian a little bit to isolate the terms we will be taking the derivative over. Remember we'll only do this over the parameters of the original problem <strong class="orange">w</strong>, <span class="blue">b</span> and <span class="green">p</span><sub class="green">i</sub>.<br></p><p    >In this form, the derivatives with respect to these variables should be straightforward to work out.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-160">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-160" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0162.svg" class="slide-image" />

            <figcaption>
            <p    >That makes this our dual function. Before we set up the dual problem, we can rewrite this by finding the minimum, expressing each variable in terms of the multipliers and filling them in to this function.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-161">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-161" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0163.svg" class="slide-image" />

            <figcaption>
            <p    >So, let's take the derivative with respect to the parameters, and set them equal to zero. We'll collect our findings in the box on the right.<br></p><p    >We haven’t discussed taking derivatives with respect to vectors, but here we’ll just use two rules that are analogous to the way we multiply scalars.<br></p><p     class="list-item">The derivative <strong>w</strong><sup>T</sup><strong>w</strong>, with respect to <strong>w</strong> is 2 times<strong> w</strong>. This is analogous to the derivative of the square for scalars.<br></p><p     class="list-item">The derivative of <strong>w</strong> times some constant vector (wrt to w) is just that constant. This is similar to the constant multiplier rule for scalars.<br></p><aside    >You can also work this out by looking at the scalar derivatives for each <span class="orange">w</span><sub>i</sub>, but to shorten the derivation, we'll take these two rules as given.<br></aside><p    >This gives us an expression for <strong>w</strong> at the optimum, in terms of alpha, y and <strong>x</strong>.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-162">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-162" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0164.svg" class="slide-image" />

            <figcaption>
            <p    >If we take the derivative with respect to <span class="blue">b</span>, we find a simple constraint: that at the optimum, the sum of all α values, multiplied by their corresponding y’s, should be zero.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-163" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-163" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0165anim0.svg" data-images="32.Linear.key-stage-0165anim0.svg,32.Linear.key-stage-0165anim1.svg,32.Linear.key-stage-0165anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Finally, we take the derivative for <span class="green">p</span><sub class="green">i</sub> and set that equal to zero.<br></p><p    >The result essentially tells us that for any given instance i, the alpha plus the beta must equal <span class="orange red">C</span>. <br></p><p    >If we assume that alpha is between 0 and <span class="orange red">C</span>, then we can just take beta to be the remainder.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-164" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-164" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0166anim0.svg" data-images="32.Linear.key-stage-0166anim0.svg,32.Linear.key-stage-0166anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This (in the orange box) is what we have figured out so far about our function at the optimum. <br></p><p    >If we fill in the three equalities, our function simplifies a lot. This function describes the optimum, subject to the constraints on the right. These are constraints of variables in our final form, so we need to remember these.<br></p><p    >We've eliminated almost all original variables, except <strong class="orange">w</strong>. We have a good expression for w in terms of the α's, so we can just fill this in, and rewrite.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-165" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-165" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0167anim0.svg" data-images="32.Linear.key-stage-0167anim0.svg,32.Linear.key-stage-0167anim1.svg,32.Linear.key-stage-0167anim2.svg,32.Linear.key-stage-0167anim3.svg" class="slide-image" />

            <figcaption>
            <p    >We first replace one of the sums in the first line with <strong class="orange">w</strong>. This is going in the wrong direction, but it allows us to reduce the number of <strong class="orange">w</strong>'s in the equation.<br></p><p    >Then, we replace the final two occurrences of <strong class="orange">w</strong>, with the sum. This gives us a function purely in terms of alpha, with no reference to <strong class="orange">w</strong> or <span class="blue">b</span>. All we need to do is simplify it a little bit.<br></p><p    >Note that the square brackets here are just brackets, they have no special meaning.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-166" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-166" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0168anim0.svg" data-images="32.Linear.key-stage-0168anim0.svg,32.Linear.key-stage-0168anim1.svg,32.Linear.key-stage-0168anim2.svg,32.Linear.key-stage-0168anim3.svg,32.Linear.key-stage-0168anim4.svg" class="slide-image" />

            <figcaption>
            <p    >To simplify, we distribute all dot products over the sums. Note that the dot product distributed over sums the same way as scalar multiplication: (a + b + c)<sup>T</sup>d -&gt; (a<sup>T</sup>d  + b<sup>T</sup>d  + c<sup>T</sup>d). <br></p><p    >It looks a little intimidating with the capital sigma notation, but it’s the same thing as you see on the right, except with dot products instead of of scalar multiplication.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-167">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-167" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0169.svg" class="slide-image" />

            <figcaption>
            <p    >Here's what all that gives us for the dual problem. We've simplified the objective function to have only α's, and we've received some constraints in return.<br></p><p    >Note that these constraints <strong>are not the KKT conditions</strong>. They are requirements for the Lagrangian to be at a minimum in the original parameters. All we have so far is weak duality. To get strong duality, we need to either prove that the KKT conditions hold for all solutions like these, or add some of them to the list of constraints. It turns out we can do the former: all KKT conditions hold already for this form of the problem, so we have strong duality.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-168">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-168" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0170.svg" class="slide-image" />

            <figcaption>
            <p    >Here they are for our problem. If we take a solution to our dual problem (a set of alphas), use the expressions for w, b and pi in terms of alpha, and fill them in here, these six statements should hold.<br></p><p    >This is easiest to do with the help of the original form of the Lagrangian, reproduced at the bottom of the slide. Note that we may assume that the original parameters are chosen so that this function is at a minimum, and the alphas are chosen to maximize over that.<br></p><p    >We don't have an expression for pi in terms of the alphas. This is because when (C -ai- bi) = 0, which is true at the optimum, the Langrangian is constant irrespective of p<sub>i</sub>. In some sense, we can set pi to whatever value we like. If we find one value that causes the KKT conditions to be satisfied, we have strong duality. We'll see that this is the case when we set pi to the originally intended value: where necessary, it makes up the difference between the output of the linear function and the edges of the margin.<br></p><p    >From top to bottom:<br></p><p     class="list-item">α<sub>i</sub> is explicitly constrained to be larger than zero in the dual problem<br></p><p     class="list-item">βi is the remainder between α<sub>i</sub> and <span class="orange red">C</span>, so must also be positive.<br></p><p     class="list-item">As noted, we are free to set and interpret p<sub>i</sub> however we like. It must be positive to satisfy the next condition. The original definition states that pi was zero if the first term was 1 or larger and makes up the (positive) difference if not. For this value of pi, the third and fourth constraints are satisfied.<br></p><p     class="list-item">See above.<br></p><p     class="list-item">The complementary slackness states that either ai is zero or the corresponding constraint is.If we use the slack variable pi, the constraint becomes exactly zero so complementary slackness is satisfied. If we don't use the slack variable (and pi is zero), the left hand side of the constraint may be nonzero, and we should show that that ai is zero. Assume that it isn't, and look at the second term of the Lagrangian. This now consists of two positive factors. If ai is nonzero, we could increase L by reducing it to zero, which tell us that ai must be zero, since ai is chosen to maximize L.<br></p><p     class="list-item">The same argument as in the previous point can be used here.<br></p><p    >Therefore, the KKT conditions are satisfied by any solution to the dual problem, and we have strong duality.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-169">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-169" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0171.svg" class="slide-image" />

            <figcaption>
            <p    >The argument we used to prove complementary slackness also tells us <strong>what the Lagrange multipliers mean</strong>. This is usually a fruitful area of investigation. The multipliers almost always have a meaningful intepretation in the problem domain. <br></p><p    >In this case, the alphas are a kind of complement to the slack parameters pi. Where the alphas are zero, the slack parameters aren't used, and so the point xi is on the correct side of the margin. Where alpha is nonzero, the slack parameters are active and we are dealing with points inside the margin.<br></p><aside    >A special case are the support vectors that are exactly on the margin. We can find these by checking for points where both the constraint and the multiplier are zero.</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-170">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-170" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0172.svg" class="slide-image" />

            <figcaption>
            <p    >And there we have the dual problem for SVMs. Note that the dual always gives us a maximization over the Lagrange multilpliers (if we start with inqeuality constraints), but here we've flipped the sign to change it back to a minimization problem.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-171">
            <a class="slide-link" href="https://mlvu.github.io/lecture06#slide-171" title="Link to this slide.">link here</a>
            <img src="32.Linear.key-stage-0173.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


</article>
