---
title: "Lecture 8: Sequences"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 8: Sequences</li>
                <li><a href="#video-000">Markov models</a></li>
                <li><a href="#video-036">Deep learning on sequences</a></li>
                <li><a href="#video-068">Recurrent neural networks and LSTMs</a></li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/61.SequentialModels.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">

        <section class="video" id="video-000">
            <a class="slide-link" href="https://mlvu.github.io/sequences#video-0">link here</a>
               <iframe
                    src="https://www.youtube.com/embed/wf8D0QWe0hg"
                    title="YouTube video player"
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
               </iframe>
        </section>


       <section id="slide-001">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-001" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    >In this lecture we’ll look at data that naturally forms a sequence. Language, music, stock prices. All of these can be modelled most naturally as a sequence of tokens of information coming in one after the other. <br></p><p    >Before we look at how to model sequences, we’ll look at some basic things to take into account when interpreting such data.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-002">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-002" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0002.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-003">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-003" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0003.png" class="slide-image" />

            <figcaption>
            <p    >We’ll start by looking at the different types of sequential datasets we might encounter. <br></p><p    >As with the traditional setting (a table of independently sampled instances) we can divide our features into numeric and discrete. <br></p><p    >A single 1D sequence might look like this. We could this of a stock price over time, traffic  to a webserver, or atmospheric pressure over Amsterdam. <br></p><p    >In this case, the data shows the number of sunspots observed over time. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-004">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-004" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0004.png" class="slide-image" />

            <figcaption>
            <p    >Sequential numeric data can also be multidimensional. In this case, we see the closing index of the AEX and the FTSE100 over time. This data is a sequence of 2D vectors.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-005">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-005" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0005.svg" class="slide-image" />

            <figcaption>
            <p    >If the elements of our data are discrete (analogous to a categorical feature), it becomes a sequence of symbols. Language is a prime example. In fact, we can model language as a sequence in two different ways: as a sequence of <strong>words</strong>, or as a sequence of <strong>characters</strong>. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-006" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-006" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0006anim0.svg" data-images="61.SequentialData.1.key-stage-0006anim0.svg,61.SequentialData.1.key-stage-0006anim1.svg" class="slide-image" />

            <figcaption>
            <p    >We can also encounter sequences with multiple categorical features per timestamp.<br></p><p    >For instance. music, or tagged language. The more complex the sequence grows, the more difficult it can be to represent. We’ll stick with simple examples for this lecture.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-007">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-007" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0007.svg" class="slide-image" />

            <figcaption>
            <p    >Then there is the question of what we’re trying to predict.<br></p><p    >One possibility is that we have a normal classification or regression task, but the instances are not represented by feature vectors bu by sequences. Tis slide shows a simple example: email classification. Each email is a sequence (of words or or characters), and each carries one target label (ham or spam).<br></p><p    >Among the instances themselves, there is not any strong sequential ordering. Emails do have a timestamp, but this ordering is usually ignored. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-008">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-008" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0008.png" class="slide-image" />

            <figcaption>
            <p    >An entirely different setting is one where the dataset as a whole is a sequence, and the instances are the elements in the sequence. For instance, in our sunspot example, we may consider each point in our sequence as a single instance consisting of a single feature.<br></p><p    >In that case, we often want to predict the future values of the sequence based on what we’ve seen in the past. </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-009" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-009" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0009anim0.svg" data-images="61.SequentialData.1.key-stage-0009anim0.svg,61.SequentialData.1.key-stage-0009anim1.svg" class="slide-image" />

            <figcaption>
            <p    >One simple way to achieve this, is to translate it to a classic regression problem by representing each point by a fixed number of values before it; in this case the 3 preceding values. <br></p><p    >This gives us a table with a target label (the value at time t) and 3 features (the 3 preceding values). With this data in hand we can grab any standard regression model, train it, and use it on the values we’re currently observing, to give us a prediction for the future.<br></p><p    >Many other features are possible: the mean over the whole history. The mean over the last 10 points, the variance over the last 10 points, and so on. This is a great way to solve this kind of sequence prediction task by translating it to a known abstract task, rather than designing a whole new approach, specific to the sequence setting.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-010">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-010" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0010.svg" class="slide-image" />

            <figcaption>
            <p    >Remember our golden rule. The test set is a simulation of what you expect to see in production. In production you won’t have access to data from the future</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-011" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-011" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0011anim0.svg" data-images="61.SequentialData.1.key-stage-0011anim0.svg,61.SequentialData.1.key-stage-0011anim1.svg,61.SequentialData.1.key-stage-0011anim2.svg,61.SequentialData.1.key-stage-0011anim3.svg,61.SequentialData.1.key-stage-0011anim4.svg" class="slide-image" />

            <figcaption>
            <p    >To check your algorithm, to do cross validation.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-012">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-012" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0012.svg" class="slide-image" />

            <figcaption>
            <p    >However, remember what we said in lecture 3: when your data has a meaningful ordering in time, you should keep it ordering in that way when you make data splits. You don’t want to train on data that is in the future comopared to your test data. In production, you won’t have that luxury, so to make your test setting a good simulation of production, you should keep your data ordered by time.<br></p><p    >If you can expect to retrain you model periodically, then you can simulate this in your test split, by retraining after every batch of instances instances you’ve seen of the test set, and adding them to the training data. This is called walk forward validation.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-013">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-013" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0013.svg" class="slide-image" />

            <figcaption>
            <p    >In the rest of the lecture, we’ll cover with methods that deal with sequences natively, without the need for feature extraction.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-014">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-014" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0014.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-015">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-015" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0015.svg" class="slide-image" />

            <figcaption>
            <p    >The first method we will look at is Markov modelling.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-016" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-016" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0016anim0.svg" data-images="61.SequentialData.1.key-stage-0016anim0.svg,61.SequentialData.1.key-stage-0016anim1.svg,61.SequentialData.1.key-stage-0016anim2.svg" class="slide-image" />

            <figcaption>
            <p    >The fundamental idea, here, is that we want to model the probability of a sequence occurring.<br></p><p    >When modelling probability, we usually break the sequence up into its <strong>tokens </strong>(in this case the words of the sentence) and model each as a random variable. Note that these random variables are decidedly <em>not </em>independent: if the previous word is an article like “a”, you’re much more likely to see a noun like “prize” following it, than another article.<br></p><p    >This leaves us with a joint distribution over 6 variables, which we would somehow like to model and fit to a dataset. How do we use our dataset to estimate the probability that we’ll see this sentence in the future?<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-017">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-017" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0017.svg" class="slide-image" />

            <figcaption>
            <p    >One simple trick we’ve used in the past to estimate probabilities is to take the relative frequencies of occurrences in the data. <br></p><p    >We could collect a large amount of natural language data and simply count how often the sequence “congratulations you have won a prize” occurs in the data, and then divide it by the total number of 6 word sequences in the data. <br></p><p    >The problem is that we’d need an extremely large amount of data for all sequences of interest to have been seen, and if our sequences get longer, like full emails, we’ll have no chance of collecting a dataset where every email we’re interested in has been seen before.<br></p><p    >What we need to do, is break our sequence up into subsequences, estimate their probability and combine the probabilities of the subsequences, to give us the probabilty of the whole sequence.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-018">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-018" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0018.svg" class="slide-image" />

            <figcaption>
            <p    >To do so, we’ll use this rule (it’s explained in the preliminaries lecture). If we have a joint distribution, we can break it up into two factors: the marginal distribution on one of the variables, times the distribution with that variable in the conditional.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-019" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-019" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0019anim0.svg" data-images="61.SequentialData.1.key-stage-0019anim0.svg,61.SequentialData.1.key-stage-0019anim1.svg,61.SequentialData.1.key-stage-0019anim2.svg,61.SequentialData.1.key-stage-0019anim3.svg,61.SequentialData.1.key-stage-0019anim4.svg" class="slide-image" />

            <figcaption>
            <p    >This gives us the<strong> chain rule of probability</strong> (which has nothing to do with the the chain rule of  calculus). <br></p><p    >The chain rule allows us to break a joint distribution on many variables into a product of conditional distributions. In sequences, we often apply it so that each word becomes conditioned on the words before it. We could apply it in any order we like but it makes most sense to condition each word on its preceding tokens.<br></p><p    >This tells us that if we build a model that can estimate the probability p(<span class="blue">x</span>|<span>y</span>, <span class="red">z</span>) of a word <span class="blue">x</span> based on the words <span>y</span>, <span class="red">z</span> that precede it, we can then <em>chain</em> this estimator to give us the joint probability of the whole sentence <span class="blue">x</span>, <span>y</span>, <span class="red">z</span>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-020" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-020" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0020anim0.svg" data-images="61.SequentialData.1.key-stage-0020anim0.svg,61.SequentialData.1.key-stage-0020anim1.svg,61.SequentialData.1.key-stage-0020anim2.svg,61.SequentialData.1.key-stage-0020anim3.svg" class="slide-image" />

            <figcaption>
            <p    >In other words, we can rewrite the probability of a sentences as the product of the  probability of  each word, conditioned on its history. <br></p><p    >If we use the log probability, this product becomes a sum. This is helpful, because these probabilities get very small, and we don’t want them underflowing to zero.<br></p><p    >This  view solves part of our problem. If we can figure out how to estimate the probabilties of a particular word occurring, given all the words that precede it, we can chain these probabilities together to give us the probabilities of a whole sentence, or an even longer sequence of words (like a whole email).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-021" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-021" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0021anim0.svg" data-images="61.SequentialData.1.key-stage-0021anim0.svg,61.SequentialData.1.key-stage-0021anim1.svg,61.SequentialData.1.key-stage-0021anim2.svg,61.SequentialData.1.key-stage-0021anim3.svg,61.SequentialData.1.key-stage-0021anim4.svg,61.SequentialData.1.key-stage-0021anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Note that this is no easy task. <br></p><p    >A perfect language model would encompass everything we know about language: the grammar, the idiom and the physical reality it describes. For instance, it would give <span>window</span> a very high probability, since that is a very reasonable  way to complete the sentence. <span class="blue">Aquarium</span> is less likely, but still physically possible and grammatically correct. A very clever language model might know that falling out of a <span class="blue">pool </span>is not physically possible (except under unusual circumstances), so that should get a lower probability, and finally <span>cycling</span> is ungrammatical, so that should get very low probability (perhaps even zero).<br></p><p    >The problem is most sentences of this length will never have been seen before in their entirety. A simple way to get a basic model is<strong> to limit how far back we look in the sentence</strong>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-022">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-022" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0022.svg" class="slide-image" />

            <figcaption>
            <p    >This is called a <strong>Markov assumption</strong>. We just take the probability of a word given all the words that precede it, and we assume that it’s equal to the probability of the word conditioned only on the k words that precede it.<br></p><p    >This is a bit like the naive Bayes assumption: we know it’s incorrect, but it still yields a very usable model. The number of words we retain in the conditional is called the order of the Markov model: this is a Markov assumption for a second-order Markov model.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-023" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-023" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0023anim0.svg" data-images="61.SequentialData.1.key-stage-0023anim0.svg,61.SequentialData.1.key-stage-0023anim1.svg,61.SequentialData.1.key-stage-0023anim2.svg,61.SequentialData.1.key-stage-0023anim3.svg,61.SequentialData.1.key-stage-0023anim4.svg,61.SequentialData.1.key-stage-0023anim5.svg,61.SequentialData.1.key-stage-0023anim6.svg,61.SequentialData.1.key-stage-0023anim7.svg,61.SequentialData.1.key-stage-0023anim8.svg,61.SequentialData.1.key-stage-0023anim9.svg" class="slide-image" />

            <figcaption>
            <p    >Using the Markov assumption and the chain rule together, we can model a sequence as limited-memory conditional probabilities. These probabilities can then be very simply estimated from a large dataset of text (called <strong>a corpus</strong>). <br></p><p    >To estimate the probability of <span class="red">prize</span> given “<span>won</span><span> a</span>” we just count how often “won a prize” occurs as a proportion of the times “<span>won</span> <span>a</span>” occurs. In other words, how often “<span>won</span><span> a</span>” is followed by <span class="red">prize</span>.<br></p><p    >These n-word snippets are called <strong>n-grams</strong>. “<span>won</span> <span>a</span> <span class="red">prize</span>” is a <strong>trigram</strong>, and “<span>won</span> <span>a</span>” is a <strong>bigram</strong>.<br></p><p    >This type of language model is often called a <strong>Markov model</strong>, because of the Markov assumption of limited memory. The size of the memory is referred to as the <strong>order</strong> of the Markov model. The higher the order of your model, the more you can model, but the more data you’ll need, to make sure that you’ve seen all the n-grams you’re interested in often enough.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-024">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-024" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0024.svg" class="slide-image" />

            <figcaption>
            <p    >With the kind of datasets you can download and run yourself, you can estimate good statistics for bigrams and trigrams. If you have a larger corpus, like Google’s corpus of all books, you can easily go up to 5-grams.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-025" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-025" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0025anim0.svg" data-images="61.SequentialData.1.key-stage-0025anim0.svg,61.SequentialData.1.key-stage-0025anim1.svg,61.SequentialData.1.key-stage-0025anim2.svg" class="slide-image" />

            <figcaption>
            <p    >So, now that we have worked out a first way to approximate probabilities for sequences, what can we do with this?<br></p><p    >We can use this to tackle both the case where our data consists of a separate sequence per instance (like in our spam classification example), and the case where our data consists of a single sequence, and we’re trying to predict the next token.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-026">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-026" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0026.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll start with a sequence-per-instance example: the spam classification task. We’ll see how to approach this with a Markov model.<br></p><p    >Ultimately, what we want to know is the the probability of the class, given the contents of the message.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-027">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-027" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0027.svg" class="slide-image" />

            <figcaption>
            <p    >We model an email as a sequence of n random variables. For the time being we’ll assume that all emails have a fixed length. <br></p><p    >(We can achieve this by taking this to be the maximum length and padding all short emails with a special `null’ word).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-028">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-028" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0028.svg" class="slide-image" />

            <figcaption>
            <p    >We’ll train a generative classifier. First, we’ll use Bayes rule to flip around the probabilties. <br></p><p    >The marignal probability p(<span class="red">spam</span>) we can estimate as as the proportion of spam emails in our data set. For the probability of the message given the class, we’ll use our language model.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-029" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-029" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0029anim0.svg" data-images="61.SequentialData.1.key-stage-0029anim0.svg,61.SequentialData.1.key-stage-0029anim1.svg,61.SequentialData.1.key-stage-0029anim2.svg,61.SequentialData.1.key-stage-0029anim3.svg" class="slide-image" />

            <figcaption>
            <p    >We use the chain rule and the Markov assumption to define the probability that a message occurs. This is exactly as before, except that now, everything is also conditioned on the class <span class="red">spam</span>.<br></p><p    >We then estimate the different conditional probabilities by computing the relative frequencies of bigrams and trigrams, as before, but we compute them only over the <strong class="red">spam</strong> part of our data.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-030" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-030" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0030anim0.svg" data-images="61.SequentialData.1.key-stage-0030anim0.svg,61.SequentialData.1.key-stage-0030anim1.svg,61.SequentialData.1.key-stage-0030anim2.svg,61.SequentialData.1.key-stage-0030anim3.svg,61.SequentialData.1.key-stage-0030anim4.svg,61.SequentialData.1.key-stage-0030anim5.svg,61.SequentialData.1.key-stage-0030anim6.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the complete algorithm, for a classifier using a second order Markov model. First, we split our data by class. We will train a separate language model for each class.<br></p><p    >Then, in each of these subsets, we count all occurrences of all unigrams, bigrams and trigrams. This is all the “training” we do.<br></p><p    >Then, to classify a new sequence, we need to compute the probability of the sequence given the class, and multiply it by the class marginal probability. <br></p><p    >In practice, as noted before, we use log probabilities, to keep low probability values from underflowing.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-031" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-031" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0031anim0.svg" data-images="61.SequentialData.1.key-stage-0031anim0.svg,61.SequentialData.1.key-stage-0031anim1.svg" class="slide-image" />

            <figcaption>
            <p    >We can also use a Markov model on unlabelled data, to predict the future. In this case, all we need is simply a large amount of natural language text.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-032" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-032" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0032anim0.svg" data-images="61.SequentialData.1.key-stage-0032anim0.svg,61.SequentialData.1.key-stage-0032anim1.svg,61.SequentialData.1.key-stage-0032anim2.svg,61.SequentialData.1.key-stage-0032anim3.svg,61.SequentialData.1.key-stage-0032anim4.svg,61.SequentialData.1.key-stage-0032anim5.svg,61.SequentialData.1.key-stage-0032anim6.svg" class="slide-image" />

            <figcaption>
            <p    >One interesting thing we can do with such a Markov model, is to sample from it, step by step. We start with a seed of a few words, and then work out the probability distribution over the next word, given the last n words. We sample from this distribution, append the sample to our text and repeat the process. <br></p><p    >Note that with the Markov assumption, we only need the last n elements of the sequence to work out the probabilities.<br></p><p    ><strong>Sequential sampling</strong> is also known as <strong>autoregressive sampling</strong>. In the context of Markov models, the sampling process is often called a<strong> Markov chain</strong>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-033">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-033" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0033.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-034">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-034" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0034.svg" class="slide-image" />

            <figcaption>
            <p    >Here is is a bit of text sampled from a Markov model trained on the works of Shakespeare. Even with such a simple language model, we can see some quite realistic patterns appearing.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-035">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-035" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0035.svg" class="slide-image" />

            <figcaption>
            <p    >V is the vocabulary (the set of all n-grams to the language model). As before, we can give the pseudo observations a smaller weight than 1, to have less impact on the estimate.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-036">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-036" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0036.svg" class="slide-image" />

            <figcaption>
            <p    >Sequential sampling can lead to amusing, results, but it’s unlikely to fool a human reader for very long. If we apply <br></p><p    >In the remainder of the lecture, we’ll look at ways of dealing with sequences in a deep learning setting. </p><p    ></p>
            </figcaption>
       </section>



        <section class="video" id="video-036">
            <a class="slide-link" href="https://mlvu.github.io/sequences#video-36">link here</a>
               <iframe
                    src="https://www.youtube.com/embed/mnkJSiS3ooc"
                    title="YouTube video player"
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
               </iframe>
        </section>


       <section id="slide-037">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-037" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0037.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-038">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-038" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0038.svg" class="slide-image" />

            <figcaption>
            <p    >The basic idea of sequence models is very similar to other deep learning model. The main characteristic that we need to ensure is that the model can handle input sequences of <strong>different lengths</strong>.<br></p><p    >We feed the model with raw data, with no feature extraction, so that we don’t lose any information. We build our model out of sequence-to-sequence layers, of which we’ll see three examples in this lecture. These take a sequence of vectors as their input, and produce a sequence of vectors as their out<br></p><p    >And finally, we need to produce some output. We can either produce a sequence of the same length as the input, for instance if we want to predict the next token at each stage, or we can output a single vector to represent the whole sequence, for instance when we want to classify the sequence.<br></p><p    >We’ll look at each of these three stages in detail.<br></p><p    >As before, if you are actually implementing these things, you’ll need some details that we won’t discuss here. You can go to <a href="http://dlvu.github.io"><strong class="blue">dlvu.github.io</strong></a> to see our lectures for the MSc course deep learning, where we discuss the same subjects, but provide some of the fines details too.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-039">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-039" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >First, the <strong>input</strong>. As we’ve seen, when we want to do deep learning, our input should be represented as a tensor. Preferably in a way that retains all information (i.e. we want to be learning from the raw data, or something as close to it as possible).<br></p><p    >Here is an example: to encode a simple monophonic musical sequence, we just one-hot encode the notes, and encode the note sequence as a matrix: one dimension for time, one dimension for the notes. We can do the same thing for characters or even words in natural language sequences.<br></p><p    ><br></p><p    >source: <a href="https://violinsheetmusic.org"><strong class="blue">https://violinsheetmusic.org</strong></a></p><p    ><a href="https://violinsheetmusic.org"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>





       <section id="slide-040" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-040" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0040anim0.svg" data-images="61.SequentialData.1.key-stage-0040anim0.svg,61.SequentialData.1.key-stage-0040anim1.svg" class="slide-image" />

            <figcaption>
            <p    >One thing is different from what we’ve seen so far in deep learning data: if we have multiple sequences of different lengths, this leads to a data set of matrices of different sizes.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-041" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-041" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0041anim0.svg" data-images="61.SequentialData.1.key-stage-0041anim0.svg,61.SequentialData.1.key-stage-0041anim1.svg,61.SequentialData.1.key-stage-0041anim2.svg,61.SequentialData.1.key-stage-0041anim3.svg" class="slide-image" />

            <figcaption>
            <p    >In principle, this is not a problem, we want to build models that can deal with sequences of any length (and can generalise over sequences of variable lengths), so they should be able to handle this.<br></p><p    >However, within a batch it’s usually required that all sequences have the same length. One way to deal with this, is to sequences of similar length together (for instance by sorting the data by length) and then pad the shorter sequences with zero vectors, so that all sequences are the same length.<br></p><p    >At this point, we have translated a batch of input sequences into a 3-tensor, which can be consumed by any deep learning model.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-042" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-042" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0042anim0.svg" data-images="61.SequentialData.1.key-stage-0042anim0.svg,61.SequentialData.1.key-stage-0042anim1.svg,61.SequentialData.1.key-stage-0042anim2.svg" class="slide-image" />

            <figcaption>
            <p    >One-hot vectors are fine if if you have a small vocabulary of symbols (like seven notes), but if you want to model 100 000 words, you’re using a lot of memory that is mostly filled with zeros. <br></p><p    >An alternative method is to use <strong>embedding vectors</strong>. The idea here is that you assign each input symbol in your vocabulary a vector of random values. You then translate a symbolic input sequence into a sequence of vectors by mapping the input symbold to their corresponding embedding vectors. The dimensionality of the embedding vectors is a hyperparameter, but it’s usually set between 64 and 1024.<br></p><p    >The fundamental trick of embedding vectors is that we treat these vectors<strong> as parameters of the model</strong>. We feed this input sequence to the model (we’ll describe what that looks like later), compute the loss, backpropagate, and we get gradients on all parameters of the model, including these embedding vectors. As we train, these vectors become useful representations of our words in some high dimensional space.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-043">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-043" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0043.svg" class="slide-image" />

            <figcaption>
            <p    >Embedding vectors occur in many contexts, so let’s define them more broadly. In any setting where you have a large collection of discrete objects, and no features for these objects, you can represent them with embedding vectors. You assign a unique vector to each object in your set, and use these vectors to  represent the objects you want to learn over. If you are training on a sequence of objects, you turn this into a sequence of embedding vectors. <br></p><p    >Once you’ve computed your loss, you update the values of the embedding vectors by gradient descent, possibly using backpropagation to compute the gradients.<br></p><p    >We can think of the embeddings as learned features: we don’t have features for our objects, so we simply assign them some random features, and then tweak the values of these by gradient descent.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-044">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-044" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0044.svg" class="slide-image" />

            <figcaption>
            <p    >Because the input layer is just a matrix multiplication, and the input is just a one-hot vector, what we end up doing when we compute the embedding for word i, is just extracting the i-th column from <strong>W</strong>.<br></p><p    >In other words, we’re not really training a function that computes an embedding for each word, we are actually learning the embeddings directly: every element of every embedding vector is a separate parameter.<br></p><p    ><br></p><p    ><br></p><p    ><br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-045">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-045" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0045.svg" class="slide-image" />

            <figcaption>
            <p    >In addition to training embeddings together with the other parameters of our model, embeddings also provide a good opportunity for <strong>pre-training</strong>. If we have a large amount of unlabeled text available, and we can think of a cheap way to use it to train word embeddings, these can then be re-used in larger, more elaborate models.<br></p><p    >We’ll take a quick look at the Word2vec model as an example.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-046" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-046" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0046anim0.svg" data-images="61.SequentialData.1.key-stage-0046anim0.svg,61.SequentialData.1.key-stage-0046anim1.svg,61.SequentialData.1.key-stage-0046anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We start with a large corpus: a data set of natural language. From this we create a very simple dataset. We slide a window of, say, five words, along the text, and match every word to the words that appear in its context. The task is to predict, for a given input word, the distribution on the words appearing in the context.<br></p><p    >We model this very simply by creating embedding vectors for all words in our vocabulary. We then feed these to a single-layer neural network with one output for every word in our vocabulary and with a softmax output. If we have 100 000 words in our vocabulary, then we can think of this as a one-layer classification network with 100 000 classes, and the embedding as input features. We train both the embedding and the weight of the network in concert. <br></p><p    >If training is succesful, we know that our embedding vectors now contain the information about which words are likely to appear in their context. The basic idea is that this information captures a lot of their meaning (this is sometimes called the distributional hypothesis). <br></p><p    ><br></p><p    >The softmax activation over 100K outputs is very expensive to compute, and you need some clever tricks to make this feasible (called<em> hierarchical </em>softmax or negative sampling). We won’t go into them here.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-047">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-047" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    >To start with, we’ll represent words as atomic objects: in a single, very large one-hot vector.<br></p><p    >These are very big, but we can usually implement things in a clever way so that we won’t explicitly need to store these in memory.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-048">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-048" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0048.svg" class="slide-image" />

            <figcaption>
            <p    >After training, we discard the second layer, and use only the embeddings produced by the first layer.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-049" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-049" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0049anim0.svg" data-images="61.SequentialData.1.key-stage-0049anim0.svg,61.SequentialData.1.key-stage-0049anim1.svg,61.SequentialData.1.key-stage-0049anim2.svg" class="slide-image" />

            <figcaption>
            <p    >If we investigate what the Word2Vec embeddings look like after training, we can tease out some interesting properties. For instance, it seems like there is a direction in the resulting embedding space, that, if we move along this direction, pushes male words towards their female counterparts. What’s more, if we subtract the embedding of the word <span class="blue">woman</span> from the embedding of the word <span class="blue">man</span>, we we find roughly this direction.<br></p><p    >Compare this with the “smiling vector” we saw in the autoencoder lecture. Word2Vec isn’t an autoencoder, but we are learning a similar kind of latent space model.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-050">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-050" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0050.svg" class="slide-image" />

            <figcaption>
            <p    >So, these are the most important methods for representing input sequences so that deep learning models can understand them. We need to somehow translate our input to a sequence of vectors.<br></p><p    >If we have a symbolic input, we can do this by representing the symbols with <strong>one-hot vectors</strong> if the vocabulary is small, and with <strong>embedding vectors</strong> if the vocabulary is larger.<br></p><p    >Pre-training your embedding </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-051">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-051" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0051.svg" class="slide-image" />

            <figcaption>
            <p    >Now that we know how to represent our input, we need some layers that we can stack together to build a deep neural net for sequences.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-052">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-052" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0052.svg" class="slide-image" />

            <figcaption>
            <p    >The next ingredient we need is layers that we can stack on top of each other. These need to be <strong>sequence-to-sequence layers</strong>. These are layers that take sequence of vectors as input and produce a new sequence of vectors as output. The input and output <br></p><p    >The defining property of a sequence-to-sequence layer is that they can consume sequences of different lengths with the same set of weights. That is, in one iteration of gradient descent, we can feed the layer a sequence of 5 words, get a loss and update its weights, and the next iteration we can feed it a sequence of 15 words, and get a loss and a gradient<em> on the same weights</em>.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-053" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-053" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0053anim0.svg" data-images="61.SequentialData.1.key-stage-0053anim0.svg,61.SequentialData.1.key-stage-0053anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here is an example: imagine that we need a layer that consumes a sequence of five vectors with four elements each and produces another sequence of five vectors with four elements each.<br></p><p    >A fully connected layer would simply connect every input with every output, giving us 400 connections with a weight each. This is<em> not </em>a sequence-to-sequence layer. Why not? Imagine that the next instance has 6 vectors: we wouldn’t be able to feed it to this layer without adding extra weights.<br></p><p    >The version on the right also uses an MLP, but only applies it to each vector in isolation: this gives us 4x4=16 connections per vector and 80 in total. These eighty connection share only 16 unique weights, which are repeated at each step.<br></p><p    >This is a sequence-to-sequence layer. If the next instance has 6 vectors, we can simple repeat the same MLP again, we don’t need any extra weights. This is the basic idea of the sequence-to-sequence layer. If we see an input with a new length, we can take the layer, keep the weights the same, but configure the layer to accept a sequence of the required length.<br></p><p    >Of course, this second option may technically be a sequence-to-sequence layer, but it doesn’t actually learn over the time dimension. The value of vector 5 is in no way influenced by the values of input vectors 1 through 4, because there are no connections between them. Luckily, there is a layer that we’ve seen already, that is a sequence-to-sequence layer and allows for information to be propagated along the time dimension.<br></p><p    ><br></p><p    >NB: We call the sequence dimension “time”, but it doesn’t necessarily always represent time. </p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-054">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-054" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >This is the 1D convolution that we first saw in the deep learning lecture.<br></p><p    >Note that the number of (distinct) weights depends only on the size of the kernel and the number of input and output channels. If we see a longer or shorter sequence, we just repeat the same kernel more often, but we don’t need extra weights.<br></p><p    >All we need to do to fit our definition of a sequence to sequence layer is to add a little padding so that the input and output have the same length.<br></p><p    >Note that even though we are now allowing information to propagate from one position in the input to another position in the output, we’re only allowing this over a finite distance. This is a bit like the finite memory of the Markov model. We can use the history (and future) of the sequence but only a fixed, finite part of it.<br></p><p    >NB: Note that the MLP example from the last slide is equal to a 1d convolution with a kernel size of 1.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-055">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-055" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0055.svg" class="slide-image" />

            <figcaption>
            <p    >In many settings, it’s not reasonable to let the model look into the future. For instance when you only have this information for your training data, but you don’t expect to have it in production. In that case it’s important to wire up your sequence to sequence layer so that each output node only has connections to the corresponding input node and to ones before it. <br></p><p    >This is called <strong>causal sequence to sequence layer</strong>. And pictured here is a a <strong>causal convolution</strong>.<br></p><aside    >Note that this doesn’t imply that we’re performing causal inference: that is, we’re not making guaranteed distinctions between correlation and causation, as we discussed in the social impact videos. It’s simply a way of ensuring that the model can’t see “into the future.”</aside><aside    ></aside>
            </figcaption>
       </section>





       <section id="slide-056">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-056" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0056.svg" class="slide-image" />

            <figcaption>
            <p    >The convolution layer is hopefully enough to give you a concrete idea of what a sequence to sequence layer looks like. In the next video we’ll see another way of building seuqence to sequence layers.<br></p><p    >So, now we have an input format: a sequence of vectors, and a type of layer, which translates a sequence of vectors to another sequence of vectors. Finally, we need to give our network some output: something that allows it to compute a single loss, so that we can start our backpropagation.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-057">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-057" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0057.svg" class="slide-image" />

            <figcaption>
            <p    >There’s number of ways we can configure our model, depending on what we’re trying to achieve. <br></p><p    >Here are three basic configurations we may want to build.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-058" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-058" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0058anim0.svg" data-images="61.SequentialData.1.key-stage-0058anim0.svg,61.SequentialData.1.key-stage-0058anim1.svg,61.SequentialData.1.key-stage-0058anim2.svg,61.SequentialData.1.key-stage-0058anim3.svg" class="slide-image" />

            <figcaption>
            <p    >A sequence-to-sequence task is probably the simplest set-up. Our dataset consists of a set of <span>input</span> and <span>target </span>sequences. <br></p><p    >We simply create a model by stacking a bunch of sequence to sequence layers, and our loss is the difference between the target sequence and the output sequence.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-059" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-059" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0059anim0.svg" data-images="61.SequentialData.1.key-stage-0059anim0.svg,61.SequentialData.1.key-stage-0059anim1.svg,61.SequentialData.1.key-stage-0059anim2.svg,61.SequentialData.1.key-stage-0059anim3.svg,61.SequentialData.1.key-stage-0059anim4.svg,61.SequentialData.1.key-stage-0059anim5.svg" class="slide-image" />

            <figcaption>
            <p    >Here’s a simple example of a sequence to sequence task: tag each word in a sentence with its grammatical category. This is known as part-of-speech tagging. All we need is a large collection of sentences that have been tagged.<br></p><p    >For the embedding layer, we convert our input sequence to positive integers. We have to decide beforehand what the size of our vocabulary is. If we keep a vocabulary of 10 000 tokens, the embedding layer will create 10 000 embedding vectors for us. <br></p><p    >It then takes a sequence of positive integers and translates this to a sequence of the corresponding embedding vectors. These are fed to a stack of s2s layers, which produce a sequence of vectors with al many elements as output tokens. After applying a softmax activation to each vector in this sequence, we get a sequence of probabilities over the target tokens.<br></p><p    >In the rest of the lecture we will omit the embedding layer, assuming that some suitable input representation has been chosen.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-060" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-060" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0060anim0.svg" data-images="61.SequentialData.1.key-stage-0060anim0.svg,61.SequentialData.1.key-stage-0060anim1.svg,61.SequentialData.1.key-stage-0060anim2.svg" class="slide-image" />

            <figcaption>
            <p    >One interesting thing we can build with a sequence-to-sequence model is an <strong>autoregressive model</strong>.<br></p><p    >We feed some sequence, and to set the target as the same sequence, shifted one token to the left. We then feed the input through several causal layers, so that the network can only look backward in the sequence. And we produce a probability distribution on the output characters.<br></p><p    >This effectively trains the model to predict the next character in the sequence, but it does so for the whole sequence in parallel.<br></p><p    >Note that this only works with causal models, because non-causal models can just look ahead in the sequence to see the next character.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-061">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-061" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0061.svg" class="slide-image" />

            <figcaption>
            <p    >Each of these outputs gives us the probability of the next character in the sequence, given the preceding characters.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-062" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-062" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0062anim0.svg" data-images="61.SequentialData.1.key-stage-0062anim0.svg,61.SequentialData.1.key-stage-0062anim1.svg,61.SequentialData.1.key-stage-0062anim2.svg" class="slide-image" />

            <figcaption>
            <p    >After the network is trained, we can start with a small seed of tokens, and sequentially sample a likely sequence. This is exactly what we did with the Markov model, but now we have a potentially much more powerful model, with a potentially infinite memory.<br></p><p    >After training, we feed the model the whole seed each time and look only at its last output to give us a probability distribution on what the next token will be. The other outputs are only used during training.<br></p><p    ><br></p><p    >We’ll see some examples of data generated this way this after we’ve explained LSTM networks.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-063">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-063" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0063.svg" class="slide-image" />

            <figcaption>
            <p    >So that’s what we can do with sequence-to-sequence model. <br></p><p    >If we have a sequence labeling task, like the email spam classification example we saw earlier, We’ll need to construct a model that consumes sequences of variable lengths, but at some stages reduces them down to a single label (like a class promability vector).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-064" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-064" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0064anim0.svg" data-images="61.SequentialData.1.key-stage-0064anim0.svg,61.SequentialData.1.key-stage-0064anim1.svg,61.SequentialData.1.key-stage-0064anim2.svg,61.SequentialData.1.key-stage-0064anim3.svg,61.SequentialData.1.key-stage-0064anim4.svg,61.SequentialData.1.key-stage-0064anim5.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-065">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-065" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0065.svg" class="slide-image" />

            <figcaption>
            <p    >Another approach is to simply take one of the vectors in the output sequence, use that as the output vector and ignore the rest. If we train the neural network to classify only on this unit, it will hopefully learn to put the right information into this output vector.<br></p><p    >If you have causal s2s layers, it’s important that you use the last vector, since that’s the only one that gets to see the whole input sequence.<br></p><p    >For some layers (like recurrent ones), this kind of approach puts more weight on the end of the sequence, since the early nodes have to propagate through more intermediate steps in the s2s layer. For others (like self-attention), all inputs in the sequence are treated equally, and there is little difference between a global unit and a pooling layer.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-066">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-066" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0066.svg" class="slide-image" />

            <figcaption>
            <p    >Finally, if we want to train a generative model on sequences, we may want to start with a label, for instance a latent vector, or a representation of the type of thing we want to sample, and map that to a sequence.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-067">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-067" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0067.svg" class="slide-image" />

            <figcaption>
            <p    >The simplest way to achieve this, is just to take your input vector and to repeat it into a sequence of the same vector over and over again.<br></p><p    >For some layers, like recurrent ones, there are other ways to feed a single vector in addition to the input sequence, but we won’t detail that here.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-068">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-068" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0068.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>



        <section class="video" id="video-068">
            <a class="slide-link" href="https://mlvu.github.io/sequences#video-68">link here</a>
               <iframe
                    src="https://www.youtube.com/embed/KUjsy7Hp8fE"
                    title="YouTube video player"
                    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
               </iframe>
        </section>


       <section id="slide-069">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-069" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0069.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-070">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-070" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0070.svg" class="slide-image" />

            <figcaption>
            <p    >One of the most popular neural networks for sequences is the<strong> recurrent neural network</strong>. This is a generic name for any neural network with cycles in it.<br></p><p    >The figure shows a popular configuration. It’s a basic fully connected network, except that its input x is extended by three nodes to which the hidden layer is copied.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-071">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-071" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0071.svg" class="slide-image" />

            <figcaption>
            <p    >To keep things clear we will adopt this visual shorthand: a rectangle represents a vector of nodes, and an arrow feeding into such a rectangle annotated with a weight matrix represents a fully connected transformation.<br></p><p    >We will assume bias nodes are included without drawing them.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-072" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-072" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0072anim0.svg" data-images="61.SequentialData.1.key-stage-0072anim0.svg,61.SequentialData.1.key-stage-0072anim1.svg" class="slide-image" />

            <figcaption>
            <p    >A line with no weight matrix represents a copy of the input vector. When two lines flow into each other, we concatenate their vectors. <br></p><p    >Here, the added line copies<span> h</span>, concatenates it to <span class="blue">x</span>, and applies weight matrix <span>W</span>.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-073">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-073" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0073.svg" class="slide-image" />

            <figcaption>
            <p    >We can now apply this neural network to a sequence. We feed it the first input, <span class="blue">x</span><sub class="blue">1</sub>, result in a first value for the hidden layer, <span>h</span><sub>1</sub>, and retrieve the first output y<sub>1</sub>.<br></p><p    >The hidden nodes are initialise to zero, so at first the network behaves just like a fully connected network.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-074">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-074" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0074.svg" class="slide-image" />

            <figcaption>
            <p    >We then feed the second input in the sequence, <span class="blue">x</span><sub class="blue">1</sub>. We now receive the <em>previous </em>hidden layer, <span>h</span><sub>1</sub>, concatenate it to the input, and multiply it by <span>W</span>, to produce the second hidden layer <span>h</span><sub>2</sub>. This is multiplied by <span>V</span> to produce the second output.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-075">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-075" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    >And so on.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-076">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-076" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0076.svg" class="slide-image" />

            <figcaption>
            <p    >We will assume bias nodes are included</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-077">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-077" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0077.svg" class="slide-image" />

            <figcaption>
            <p    >In principle, we </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-078" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-078" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0078anim0.svg" data-images="61.SequentialData.1.key-stage-0078anim0.svg,61.SequentialData.1.key-stage-0078anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Instead of visualising a single small network, applied at every time step, we can <strong>unroll</strong> the network. Every step in the sequence is applied in parallel to a copy of the network, and the recurrent connection flows from the previous copy to the next.<br></p><p    >Now the whole network is just one big, complicated<strong> feedforward net</strong>, that is, a network<em> without </em>cycles. Note that we have a lot of shared weights, but we know how to deal with those.<br></p><p    >The hidden layer is initialised to the zero vector.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-079">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-079" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0079.svg" class="slide-image" />

            <figcaption>
            <p    >Now the whole network is just one big, complicated feedforward net. Note that we have a lot of shared weights, but we know how to deal with those.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-080">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-080" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0080.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-081">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-081" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0081.svg" class="slide-image" />

            <figcaption>
            <p    >Basic RNNs work pretty well, but they do not learn to remember information for very long. Technically they can, but the gradient vanished too quickly over the timesteps.<br></p><p    >You can’t have a long term memory for everything. You need to be selective, and you need to learn to select words to be stored for the long term when you first see them. <br></p><p    >In order to remember things long term you need to forget many other things.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-082">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-082" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0082.svg" class="slide-image" />

            <figcaption>
            <p    >One of the reasons that neural networks don remember too well is that the weights between an input long ago and the current output get a gradient that has to travel through a lot of layers in our network. If these are sigmoid activated layers, these gradients will vanish much more strongly than the gradients between input 6 and output 6, so the network will always learn more from short term correlations between the input and the output than from long term correlations.<br></p><p    >We could fix this with ReLU activations and other tricks, but in the late 1990s most of this tricks weren’t available yet. Instead the LSTM was invented, which solved this problem, by moving the activations out of the way of the gradient travelling backwards in time.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-083">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-083" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0083.svg" class="slide-image" />

            <figcaption>
            <p    >An enduring solution to the problem are LSTMs. LSTMs have a complex mechanism, which we’ll go through step by step. To do so, we’ll first set up a visual notation.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-084">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-084" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0084.svg" class="slide-image" />

            <figcaption>
            <p    >Here is our visual notation.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-085" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-085" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0085anim0.svg" data-images="61.SequentialData.1.key-stage-0085anim0.svg,61.SequentialData.1.key-stage-0085anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The basic operation of the LSTM is called a cell (the orange square, which we’ll detail later). Between cells, there are two recurrent connections, y, the current output, and C the <strong>cell state</strong>.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-086">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-086" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0086.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what happens inside the cell. It looks complicated, but we’ll go through all the elements step by step.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-087">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-087" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0087.svg" class="slide-image" />

            <figcaption>
            <p    >The first is the “conveyor belt”. It passes the previous cell state to the next cell. Along the way, the current input can be used to manipulate it. <br></p><p    ><br></p><p    >Note that the connection from the previous cell to the next has <em>no activations</em>. This means that along this path, gradients do not decay. It’s also very easy for an LSTM cell  to ignore the current information and just pass the information along the conveyor belt.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-088">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-088" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0088.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the first manipulation of the conveyor belt. This is called the <strong>forget gate</strong>.<br></p><p    >It looks at the current <span class="blue">input</span>, concatenated with the previous <span>output</span>, and applies an element-wise scaling to the current value in the conveyor belt. Outputting all 1s will keep the current value on the belt what it is, and outputting all values near 0, will decay the values (forgetting what we’ve seen so far, and allowing it to be replaces by our new values in the next step).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-089">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-089" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0089.svg" class="slide-image" />

            <figcaption>
            <p    >in the next step, we pass the current input into two transformations that yield two vectors one sigmoid activated (between 0 and 1) and one <span>tanh</span> activated (between -1 and 1). There are element-wise multiplied and added to the conveyor belt.<br></p><p    >This is called a <strong>gating mechanism</strong>, and it essentially decides for each dimension what should be added to the conveyor belt (the tanh-ed vector) and <em>how much</em> of it should be added (the sigmoided vector). You can think of the sigmoided vector as a kind of "soft mask" over the tanh-ed vector.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-090">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-090" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0090.svg" class="slide-image" />

            <figcaption>
            <p    >The gating mechanism takes a single input vector, projects it to two different vectors, one using a sigmoid and one using a  a tanh activation. <br></p><p    >The gate is best understand as producing an additive value: we want to figure out how much of the input to add to some other vector, in this case the one on the converyor belt. If the current input is important  we want to add most of it, at the risk of forgetting what we have in memory, and it the current input is unimportant, we want to ignore it.<br></p><p    >The tanh should be though of as a mapping of the input to the range [-1, 1]. This is the value we will add to the conveyor belt. <br></p><p    >The sigmoid acts as a selection or attention vector. For elements of the input that are important, it outputs 1,  retaining all the input in the addition vector. For elements of the input that are not important, it outputs 0, so that they are zeroed out. The sigmoid and tanh vectors are element-wise multiplied.<br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-091">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-091" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0091.svg" class="slide-image" />

            <figcaption>
            <p    >Finally, we need to decide what to output now. We take the current value of the conveyor belt, tanh it to rescale, and element-wise multiply it by another sigmoid activated layer. This layer is sent out as the current output, and sent to the next cell along the second recurrent connection.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-092">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-092" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0092.png" class="slide-image" />

            <figcaption>
            <p    >Now, when we look at all the paths that the gradients take back down the network, we see that there are many of them, in <span>purple</span> that cross activations, and these will likely die out over a few cells, and never contribute to learning long range dependencies.<br></p><p    >However, there are also paths for the gradient, in <span>green</span>, that travel over the conveyor belt and only encounter linear operations. This means that these gradients are perfectly preserved as they travel back through time, and can be used to pick up on long range dependencies. This is where the name comes from. The conveyor belt functions as a long term memory preserving good gradients, and the rest of the functions as a short term memory, making nonlinear projections of the input and using them to manipulate the output and the contents of the conveyor belt.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-093" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-093" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0093anim0.svg" data-images="61.SequentialData.1.key-stage-0093anim0.svg,61.SequentialData.1.key-stage-0093anim1.svg" class="slide-image" />

            <figcaption>
            <p    >That’s a lot of complexity. Let’s see what it buys us. The best way, by far, to illustrate the power of LSTMs is to apply the sequential sampling trick.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-094">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-094" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0094.svg" class="slide-image" />

            <figcaption>
            <p    >So, now that we have a powerful, recurrent sequence-to-sequence layer, let’s see what it can do. We’ll train a languange model autoregressively, as we did with the markov model, but this time we’ll train it at character-level.<br></p><p    >We cut a corpus of text into large chunks of character sequences, and we feed these to our model, teaching it to predict the next character at each position in the sequence.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-095">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-095" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0095.svg" class="slide-image" />

            <figcaption>
            <p    >Then for the sequential sampling, we proceed as before. We start with a small seed, and sample the characters one at a time, appending them to the seed.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-096">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-096" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0096.svg" class="slide-image" />

            <figcaption>
            <p    >After training, we start with a small seed of characters, and we sample sequentially. Note that this time we have no Markov assumption, so we keep feeding the whole sequence to the network very time we sample.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-097">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-097" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0097.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-098">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-098" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0098.svg" class="slide-image" />

            <figcaption>
            <p    >Remember, this is a <strong>character level</strong> language model.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-099">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-099" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0099.svg" class="slide-image" />

            <figcaption>
            <p    >Note that not only is the language natural, the wikipedia markup is also correct (link brackets are closed properly, and contain key concepts).</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-100">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-100" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0100.svg" class="slide-image" />

            <figcaption>
            <p    >The network can even learn to generate valid (looking) URLs for external links.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-101">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-101" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0101.svg" class="slide-image" />

            <figcaption>
            <p    >Sometimes wikipedia text contains bits of XML for structured information. The model can generate these flawlessly.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-102">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-102" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0102.png" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>





       <section id="slide-103">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-103" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0103.svg" class="slide-image" />

            <figcaption>
            <p    ><a href="https://twitter.com/deepdrumpf?lang=en"><strong class="blue">https://twitter.com/deepdrumpf?lang=en</strong></a><br></p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-104">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-104" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0104.svg" class="slide-image" />

            <figcaption>
            <p    >Another way to train a model to generate sequences is to use the generator network that we saw previously. We sample a <em>single</em> vector from a standard normal distribution and feed it to a sequence-to-sequence network</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-105">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-105" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0105.svg" class="slide-image" />

            <figcaption>
            <p    >In the previous video we saw that we could achieve this by repeating the input vector into a sequence, but when we use RNNs, there is another option. We can feed the latent vector to the network as the initial hidden state. We canthen set the input sequence to zero, or as we will see later, use it for something else.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-106">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-106" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0106.svg" class="slide-image" />

            <figcaption>
            <p    >Of course, if we want to train a generator network we’ll need either a discriminator or an encoder. <br></p><p    >For an autoencoder we can simply use a sequence-to-label network as our encoder, and interpret the last vector of the output as the latent vector representing the whole input.</p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-107">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-107" title="Link to this slide.">link here</a>
            <iframe
                src="https://www.youtube.com/embed/G5JT16flZwM"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>

            <figcaption>
            <p    >Here's an example of such a sequence VAE trained on small snippets of MIDI music. The starting and end snippets (A and B) are two very different styles of music. The video shows an interpolation between the two. It shows that at each step, a realistic sample of music is produced. If we do this interpolation in the data space rather than the latent space (see the link below for an example), most of the intermediate samples are much less musical.<br></p><p    ><br></p><p    >source: <a href="https://magenta.tensorflow.org/music-vae"><strong class="blue">https://magenta.tensorflow.org/music-vae</strong></a></p><p    ><a href="https://magenta.tensorflow.org/music-vae"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>





       <section id="slide-108" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-108" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0108anim0.svg" data-images="61.SequentialData.1.key-stage-0108anim0.svg,61.SequentialData.1.key-stage-0108anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This works well for music but we’ve lost the fine touch of the sequential/autoregressive sampling, where we could build up a sentence character by character, finetuning the details one at a time. <br></p><p    >Instead a single small latent vector now needs to represent all information in the sequence: this is great to capture the global pattern, but not for deciding on the finer details. This is similar to what we saw with images: the VAE reconstructions we recognizable people but the finer details of the image had been washed out.<br></p><p    >Here, we can combine the best of both worlds, in a method called <strong>teacher forcing</strong>. Since we’d left the input sequence to the decoder blank, we can feed the decoder a character-shifted version of the input <strong>as well as the latent vector</strong>. This way, we are training a decoder that gets global information from the latent vector, and generates the finer details by autoregressive sampling.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>





       <section id="slide-109">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-109" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0109.svg" class="slide-image" />

            <figcaption>
            <p    >The example we saw in the autoencoder lecture was also trained in this way: using a variational autoencoder with teacher forcing.<br></p><p    ><br></p><aside    >source: Generating Sentences from a Continuous Space by Samuel R. Bowman, Luke Vilnis, Oriol Vinyals, Andrew M. Dai, Rafal Jozefowicz, Samy Bengio<br></aside><aside    >https://arxiv.org/abs/1511.06349<br></aside><p    ></p>
            </figcaption>
       </section>





       <section id="slide-110">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-110" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0110.png" class="slide-image" />

            <figcaption>
            <p    >Here is another sequence-to-sequence autoencoder. To gather data, Google <a href="https://quickdraw.withgoogle.com/"><strong class="blue">set up a website</strong></a>, where it challenged users to quickly draw a sketch of something using their mouse. The drawing was captured as a<em> sequence</em> of points in the plane.<br></p><p    >Researchers then trained a variational sequence-to-sequence autoencoder with teacher forcing and a mixture density output at each step of the sequence. In short, quite a complex model. The result, however was worth it. Here, we see two interpolation grids from the latent space of this model, smoothly interpolating between vairous ways of drawing cats and various ways of drawing owls.<br></p><p    >source: <a href="https://arxiv.org/abs/1704.03477"><strong class="blue">A Neural Representation of Sketch Drawings</strong></a>, Ha and Eck (2017) </p><p    ></p>
            </figcaption>
       </section>





       <section id="slide-111">
            <a class="slide-link" href="https://mlvu.github.io/sequences#slide-111" title="Link to this slide.">link here</a>
            <img src="61.SequentialData.1.key-stage-0111.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


</article>
