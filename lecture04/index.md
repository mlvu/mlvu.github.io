---
title: "Lecture 4: Probabilistic models"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 4: Probabilistic models</li>
            <li><a href="#video-000">What is probability?</a></li>
            <li><a href="#video-036">Learning with probability</a></li>
            <li><a href="#video-054">(Naive) Bayes classifiers</a></li>
            <li><a href="#video-074">Logistic regression</a></li>
            <li><a href="#video-102">Information theory</a></li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/31.ProbabilisticModels1.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">
       <section class="video" id="video-000">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-0">link here</a>
           <iframe
                src="https://www.youtube.com/embed/9rWoBVnVuLQ?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-001">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-001" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0001.svg" class="slide-image" />

            <figcaption>
            <p    >Probability is an important tool in Machine Learning. We expect that you have been taught probability theory already, but since it’s a subtle concept, with complicated foundations, we’ll go over the basics again in this first video.<br></p><p    >If you have never done <em>any</em> probability before, please consult the homework exercises and the recommended reading to brush up first.<br></p><p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-002">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-002" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0002.svg" class="slide-image" />

            <figcaption>
            <p    >To start, let’s look at the way we use probability <em>informally</em>.<br></p><p    >Let’s say you are a concerned parent, you read this headline and you are shocked by it. You turn to your partner, and you say “that means that the probability that our son is gambling online is 12.5%”. Your partner disagrees, you have a good handle on your son’s behaviour and his spending. Unless he has a credit card you don’t know about, and the probability of that is much lower.<br></p><p    >Well, then the probability that Josh, his closest friend, gambles online must be 12.5%. If one in eight teenage boys is gambling, they must be hiding <em>somewhere</em>. Your partner disagrees again: probability doesn’t enter in to it. Josh is either gambling or he isn’t.<br></p><p    >Clearly, we need to look at what we mean when we say that a probability of something is such-and-so. There are two commonly accepted ways of looking at it: objective and subjective probability. We’ll start with <strong>objective probability</strong>. <br></p><p    >image source: <a href="https://www.theguardian.com/society/2016/sep/20/one-in-eight-european-teenage-boys-gamble-online-says-survey"><strong class="blue">https://www.theguardian.com/society/2016/sep/20/one-in-eight-european-teenage-boys-gamble-online-says-survey</strong></a></p><p    ><a href="https://www.theguardian.com/society/2016/sep/20/one-in-eight-european-teenage-boys-gamble-online-says-survey"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-003">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-003" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0003.svg" class="slide-image" />

            <figcaption>
            <p    >In <strong>objective probability</strong>, “the probability that X is the case” represents an<em> objective truth</em>: whatever a probability is, it must be the same for everybody. You and I may disagree over a probability, but only because one of us is wrong. There is one true probability. An example is the probability that a coin-toss will land heads. If nothing unusual is going on, everybody should agree that the outcome is uncertain and that the probability will be 50%. We can't have a situation  where one person thinks it's 10% and the other thinks it's 90%<em> and they're both right</em>.<br></p><p    >The most common form of objective probability is<strong> frequentism</strong>. Under the frequentist definition, probability is a property of a (hypothetical) repeated experiment.  For instance, take the statement “the probability of rolling 6 with a fair die, is one in six.” <br></p><p    >The experiment is rolling a die. The outcome we are discussing is the roll resulting in a 6. If we were to repeat the experiment a large number of times, N, then the proportion of times we observe the discussed outcome is close to 1 in 6. More precisely, as N grows, the proportion <em>converges</em> to 1 in 6.<br></p><p    >Under a frequentist interpretation, saying “the probability is one in six", is equivalent to saying “if I roll the die repeatedly, the relative frequency of sixes will converge to 1 in 6 as the number of rolls grows.”<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-004">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-004" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0004.svg" class="slide-image" />

            <figcaption>
            <p    >Under objective probability the statement “the probability that Josh is gambling is 12.5%” is indeed nonsense. There is no experiment we can imagine where Josh “turns out" to be a gambler one in 8 times. He either gambles or he doesn’t.<br></p><p    >What we <em>can</em> say is that the probability that a teenage boy drawn randomly from the European population gambles online is 12.5%. This is an experiment we can repeat, and at every repetition, we choose a different boy, so we get a different outcome.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-005">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-005" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0005.svg" class="slide-image" />

            <figcaption>
            <p    >The alternative to objectivism is <strong>subjectivism</strong>. It states that probability expresses our uncertainty. If X is a boolean variable, one that is true or not true, and we are uncertain whether X is true, we can assign a probability to X being true. A probability of 0.5 means we are entirely ambivalent, a probability of 0.75 means we think X is pretty likely, and a probability of 1 means we’re entirely sure that X is true. <br></p><p    >In this case, different people can have different probabilities for the same thing being true. You and I may "assign" different probabilities to something being true and both be right. If you have information I don’t have, your probability may be closer to certainty than mine.<br></p><p    ><strong>Bayesianism</strong> is the main form of subjective probability. It builds on Bayes’ rule, which we will discuss later, to tell us how we should use observations to <em>update</em> our beliefs.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-006">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-006" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0006.svg" class="slide-image" />

            <figcaption>
            <p    >Under subjectivism, we <em>can</em> say “the probability that our son is gambling is 12.5%” We don’t know precisely what he gets up to, so even though there is a definite objective answer, <em>we</em> are uncertain. If we know only this headline, we may well pick 12.5% as our belief that our son is gambling. Of course, as noted before we have a lot more knowledge about <em>our </em>son than about other teenage boys. We know he goes to bed on time, we know where gets his money,  and we know he probably doesn’t have a secret credit card. So even though the probability for a random teenage boy would be 12.5%, the probability for our son is actually much lower, because we have extra information.<br></p><p    >This is the fundamental difference between the two views: under frequentism, probability is defined as an objective property of the world. The probability of X is the same for all people regardless of what we know or don’t know. Under Bayesianism, probability is an expression of a subjective property: it can change from one person to the next, and if we learn new information, it can change from one moment to the next. If we find out that our son <em>does </em>have a secret credit card, the probability that he is gambler, suddenly jumps up dramatically, even though nothing about him has changed, only our knowledge about him.<br></p><p    >Note that Bayesianism, in a sense encompasses frequentism. If we define probability as the outcome of a repeated experiment, then before we do the experiment we are uncertain about its outcome. If we understand the experiment perfectly, then the Bayesian probability we assign to the outcomes will coincide with the frequentist probabilities of the outcomes.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-007">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-007" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0007.svg" class="slide-image" />

            <figcaption>
            <p    >So, at heart subjectivism and objectivism are disambiguations. The word probability is ambiguous, and these allow you to make precise what you mean.<br></p><p    >Note that you don’t have to commit to one view or another. At heart subjective and objective probability are just ways to be more precise about what the word probability actually means. You can use the subjective definition one day and the objective definition the next (especially in informal settings).<br></p><p    >However, once you start doing statistics, the two definitions lead to fundamentally different approaches (which we’ll see in more detail later). And in the statistical community there are definitely two camps: the frequentists and the Bayesians, and arguments between the two can get very heated.<br></p><p    >Since machine learning is often seen as another form of statistics, you may ask whether it is usually seen as using subjective or objective probability. I can’t give you a commonly accepted answer, I think opinions differ.<br></p><aside    >My view (which is definitely not shared by everyone) is that Machine Learning, while being statistical in nature, is not fundamentally probabilistic. The fundamental principles of machine learning can be defined and explained without recourse to probability theory (and indeed, we have done so for most of the start of the course). The fundamental goal of (offline) machine learning is to minimise test set loss given only a training set, and some hint as to the relation between the two datasets. This definition does not require probability.<br></aside><aside    >Of course, even if machine learning is not fundamentally probabilistic, probability has proven to be a very powerful tool (much like linear algebra and calculus), in helping us solve this problem. The consequence, is that we can borrow whatever methods are most helpful to us at the time. We’ll use the frequentist methods when we need them, and the Bayesian methods when they prove most helpful. We’ll even happily mix the two in a single model.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-008">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-008" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0008.svg" class="slide-image" />

            <figcaption>
            <p    >All that was about the<em> interpretation</em> of probabilities. This is what the field of <strong>statistics</strong> is about. We have frequentist statistics and Bayesian statistics.<br></p><p    >The<em> mathematical </em>definition of probability, studied in the field of <strong>probability theory</strong>, which is very different from statistics,<strong> </strong>is entirely distinct from the question of how probability applies to the real world. Both frequentists and Bayesians use the same mathematical framework to express probability as a number between 0 and 1. The only difference between them is in what this number is taken to represent.<br></p><p    >We’ll go through the basic ingredients of probability theory quickly. This is a complex field, and a complete basis is too technical for this course. We'll handwave some of the details, and you can hopefully get by with a little bit of intuition.<br></p><aside    >If you plan to make machine learning your main expertise, should probably  resolve to return to the fundamentals of probability theory at some point and learn how everything is properly defined.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-008" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-009" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0009anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0009anim0.svg,31.ProbabilisticModels1.key-stage-0009anim1.png" class="slide-image" />

            <figcaption>
            <p    >First the <strong>sample space</strong>. These are the single outcomes or truths that we wish to model. If we flip a coin, our sample space is the set of the two outcomes <em>heads</em> and <em>tails</em>.<br></p><p    >We can have discrete sample spaces or continuous ones. In a continuous space, you can imagine that in between any two values there is always another value (like when we measure someone's height very precisely). In a discrete sample space this isn't usually the case.*<br></p><p    >A discrete sample space can also be infinite: consider flipping a coin and counting how many flips it takes to see tails. In this case any number of flips is possible, so the sample space is the  natural numbers (although any number larger than 20 will get an astronomically small probability).<br></p><aside    >* <span>As we said before, this is not a proper </span>definition<span> of a continuous space, and there are some odd exceptions, but it should be enough to tell the most common continuous and discrete spaces apart. The proper definition is a bit too technical at this point.</span></aside><aside    ><span></span></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-010">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-010" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0010.svg" class="slide-image" />

            <figcaption>
            <p    >From the sample space, we construct the <strong>event space</strong>. Events are those things that can have probabilities. These include the elements of the sample space, like the probability of rolling a six with a die, but they also include sets of multiple elements of the sample space, like the event of "rolling  a one or a six" and the event of "rolling an even number". Even the empty set and the set of all six numbers are events. As we will see, these will get probabilities 0 and 1 respectively.<br></p><p    >The events containing only one element of the sample space, like "rolling a 1", are called <strong>atomic events</strong>.<br></p><p    >How the event space is constructed is a technical business. For our purposes, we can simply say that if the sample space is discrete then the event space is the powerset of the sample space: the set of all possible subsets we can make.<br></p><p    >For continuous sample spaces, not every subset can be an event. We need to make sure that our event space is a thing called a “sigma algebra.” We won’t need to worry about this in this course. We can simply trust that if we don't try to assign probability to any particularly unusual subsets of the sample space, everything will work: these will be in the sigma algebra, so they will be events, and we can assign a probability to them.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-011">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-011" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0011.svg" class="slide-image" />

            <figcaption>
            <p    >Random variables have a confusing and convoluted definition, so we’ll just give you the intuitive interpretation. <br></p><p    ><strong>Random variables</strong> help us to describe events. We can think of a random variable D as something that takes the values in the sample space, so that we can use it to describe events: instead of describing an event like "rolling a number larger than three" in natural language, we can describe it symbolically using the random variable D as "<span class="blue">D</span> &gt; 3". This usually makes our notation more concise and precise. <br></p><p    >We usually use capital, non-bold letters for random variables, and lowercase letters for traditional variables. A statement like "<span class="blue">D</span>=d" refers to the event that the random variable takes the value that the normal variable d currently represents.<br></p><p    >Once we have a way to describe the events we are interested in, we can assign a probability to each event. We do this  with a <strong>probability function p. </strong>This function must satisfy several constraints, but we’ll take those as read for now, and just say that it takes an event, and maps it to a value between 0 and 1 (inclusive).<br></p><p    >In probabilistic machine learning, it’s common to model features, target labels, and sometimes even model parameters as random variables. If we are referring to a dataset of multiple instances, we model each as a separate random variable with the same distribution. We'll see some examples later in this lecture.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-012">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-012" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0012.svg" class="slide-image" />

            <figcaption>
            <p    >Interpreting what a statement including a probability function means depends on whether all variables are “filled in.” <br></p><p    >In the first line, X=0 refers to a single, well-defined event, so p(X=0) refers to a single value between 0 and 1. In the second line we have a classical variable <span class="blue">x</span>, so the statement “X=<span class="blue">x</span>” can refer to different events, depending on what <span class="blue">x</span> is. In other words, here “p(X=<span class="blue">x</span>)” is a function of <span class="blue">x</span>. For example, if <span class="blue">x</span> can take one of two values, -1 or 1, then the function p(X=x) has a range of only two values as shown here. <br></p><p    >Note that this is is not the <em>complete </em>probability function p, since that also assigns probabilities to events like "X=-1 or X=1" and the empty event. <br></p><aside    >However, if X=-1 and X=1 are the only two members of the sample space, you can work out the complete probability function from the definition given here.<br></aside><p    ></p>
            </figcaption>
       </section>


       <section id="slide-013">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-013" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0013.svg" class="slide-image" />

            <figcaption>
            <p    >Since we usually know which outcomes belong to which random variables, p(X) and p(<span class="blue">x</span>) can both be used as shorthand for p(X=<span class="blue">x</span>).<br></p><p    >If we have a Boolean random variable, which takes values true or false, people often use a different shorthand, where p(X) represents the probability that X is true and p(¬X) represents the probability that it is false. <br></p><p    >All these conflicting shorthands may be a little confusing at times, but there is usually enough information in the context to figure out what the author means (and writing everything out in unambiguous notation usually leads to an unreadable mess).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-013" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-014" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0014anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0014anim0.svg,31.ProbabilisticModels1.key-stage-0014anim1.svg,31.ProbabilisticModels1.key-stage-0014anim2.svg" class="slide-image" />

            <figcaption>
            <p    >On both discrete and continuous sample spaces, <strong>the events we describe have probability</strong>. Where they differ, in an important way, is in whether a meaningful probability is assigned to the elements of the sample space. Here is how such probabilities are usually visualized: discrete on the left, continuous on the right. In both cases, we are look at the sample space.<br></p><p    >On the left, we are seeing the probabilities assigned to each element of the sample space. Using this, we can easily work out the probabilities of every event as well (just add up all the probabilities of all the atomic events in the event).<br></p><p    >However, when we look at a graph like the one on the right, describing a normal distribution, it’s important to realize that <strong>this function does not express a probability</strong>. If I ask you, under this distribution, which has the higher probability, 0 or 1, the answer is that <em>they both have probability 0</em>. This should make intuitive sense: What is the probability of meeting somebody who is exactly 2m tall? Surely, if you measure more and more precisely, the probability of getting <em>exactly</em> 2m goes further and further down.<br></p><p    >In short, when it comes to probability distributions on continuous spaces, the atomic events normally all have probability 0. The things that have nonzero probability are <em>ranges</em> of values. The probability of somebody being between 2.0m and 2.1m tall is more than 0, no matter how precisely you measure them. <br></p><p    >So what does this curve express? Not probability but probability <em>density</em>. The probabilities can be retrieved by integration. For instance, the probability of getting a sample between 0 and 1 from this distribution is equal to the area highlighted in the slide. The total area between -∞ and ∞ is exactly 1.<br></p><aside    >These integrals can usually not be worked out analytically so we use numeric approximations. In the old days, you'd look these up in tables, but nowadays, we usually let the computer do it for us on the fly.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-015">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-015" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0015.svg" class="slide-image" />

            <figcaption>
            <p    >Now that we have the basic language of probability theory in place, we can look at some of the most important concepts. We will quickly review these five.<br></p><p    >Note that even though we have multiple random variables, we still have a <em>single</em> sample space and event space, and the random variables <span class="blue">X</span> and <span class="blue">Y</span> will help us describe the events that we’re interested in. Think of the <em>single</em> sample space for rolling <em>two</em> dice. You could use <span class="blue">X</span> for the result of the first die, and <span class="blue">Y</span> for the result of the second to describe events in this situation.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-016">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-016" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0016.svg" class="slide-image" />

            <figcaption>
            <p    >We will use the following running example: we sample a random person from the Dutch population and we check<span class="green"> their age</span> and <span class="orange red">the health of their teeth</span> (binning the results into three categories for each variable).<br></p><p    >We want to ask questions like:<br></p><p     class="list-item">what is the probability of seeing an old person?<br></p><p     class="list-item">what is the probability that a young person has fake teeth?<br></p><p     class="list-item">does a person’s age influence the health of their teeth, or is there no relation?<br></p><p    >The sample space is the set of the nine different pairs of values we can observe, and the event space is the powerset of that. The random variables <span>Age</span> and <span>Teeth</span> will help us describe these events.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-017">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-017" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0017.svg" class="slide-image" />

            <figcaption>
            <p    >The joint distribution is the most important distribution. It tells us the probability of each <strong>atomic event</strong>: each event that contains a single element in our sample space. <br></p><p    >Since we have two random variables in our example, which together capture the whole sample space, we can specify the joint distribution in a small table. The probabilities of all these events sum to one.<br></p><p    >Note that p(<span class="green">Age = old</span> &amp; <span class="orange red">Teeth = healthy</span>) refers to a single value (1/18), because we have specified the event. p(<span class="green">Age</span>, <span class="orange red">Teeth</span>) does not refer to a single value, because the variables are not instantiated, it represents <em>a function of two variables, </em>i.e. the whole table.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-017" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-018" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0018anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0018anim0.svg,31.ProbabilisticModels1.key-stage-0018anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If we want to focus on just one random variable, all we need to do is sum over the rows or columns. <br></p><p    >For instance, the probability that <span class="green">Age=old</span>, regardless of the value of <span class="orange red">Teeth</span>, is the probability of the event {(<span class="green">o</span>,<span class="orange red">h</span>), (<span class="green">o</span>,<span class="orange red">u</span>), (<span class="green">o</span>,<span class="orange red">f</span>)}. Because we can write these sums in the <em>margins</em> of our joint probability table, this process of “getting rid” of a variable is also called <strong>maginalizing out</strong> (as in “we marginalize out the variable <span class="orange red">Teeth</span>”). The resulting distribution over the remaining variable(s) is called a <strong>marginal distribution</strong>.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-018" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-019" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0019anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0019anim0.svg,31.ProbabilisticModels1.key-stage-0019anim1.svg,31.ProbabilisticModels1.key-stage-0019anim2.svg,31.ProbabilisticModels1.key-stage-0019anim3.svg" class="slide-image" />

            <figcaption>
            <p    >This is what marginalizing looks like in symbols: we sum the joint probabilities for all values of one of the random variables, keeping the value of the other fixed.<br></p><p    >Remember that p(X) and P(x) are both shorthand for p(X=x).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-020">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-020" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0020.svg" class="slide-image" />

            <figcaption>
            <p    >If we know that somebody is <span class="green">young</span>, we know that the probability of them having <span>false teeth</span> must be much lower. This is called<strong> conditional probability</strong>, our knowledge of one random variable, given that some other variable takes some specific value. This is expressed with a vertical bar, with the known part, the <strong>conditional</strong> on the right.<br></p><p    >The conditional probability p(X=x|Y=y) is computed taking the joint probability of (x, y) and normalising by the sum of the probabilities in the row or column corresponding to the part that’s given in the conditional.<br></p><p    >Imagine we’re throwing darts at this table, and the probability of hitting a certain cell is the joint probability indicated in the cell. The conditional probability p(<span class="orange red">T=f</span>|<span class="green">A=y</span>) is the probability that the dart hits the (<span class="green">y</span>, <span class="orange red">f</span>) cell, given that it’s hit the <span class="green">y</span> row.<br></p><p    >Note that  a statement about conditional probability tells us nothing about <strong>causality</strong>. In our example age causes bad teeth, but het can express both the probability that somebody has bad teeth given that they are old (in the causal direction), and the probability that somebody is old given that they have bad teeth (in the opposite direction).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-020" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-021" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0021anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0021anim0.svg,31.ProbabilisticModels1.key-stage-0021anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what conditional probability looks like in abstract, symbolic terms. Note that the denominator is just the marginal probability</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-022">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-022" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0022.svg" class="slide-image" />

            <figcaption>
            <p    >If we re-arrange the factors in the definition of the conditional probabilty, we get this equation, showing a kind of <em>decomposition</em> of the joint probability. This comes up <strong>a lot</strong>, so make a note of it.<br></p><p    >For a specific example, the probability of seeing an<span class="green"> old person</span> with <span class="orange red">false teeth</span>, is the probability that an old would have false teeth, times the probability of seeing a old person at all. The probability that an old person has false teeth may be very high, but if the probability of seeing an old person is very small, there's still a very small probability of seeing an old person with false teeth.<br></p><p    >Note that the same decomposition works with the reverse conditional, the probability that someone with <span class="orange red">false teeth</span> would be <span class="green">old</span>. Try it.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-023">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-023" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0023.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what these concepts look like with <em>continuous </em>random variables (a bivariate normal distribution in this case). The joint probability distribution is represented by the point cloud in the middle. These are the values of X and Y that are likely.<br></p><p    ><strong>Marginalizing </strong>out either variable results in a univariate normal (the red and blue distributions), the projection of the multivariate distribution onto the X and Y axes.<br></p><p    >The<strong> conditional distribution </strong>corresponds to a vertical or horizontal <em>slice </em>through the joint distribution (and also results in a univariate normal).<br></p><p    >image source: By IkamusumeFan - Own work, CC BY-SA 3.0, <a href="https://commons.wikimedia.org/w/index.php?curid=30432580"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=30432580</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-024">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-024" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0024.svg" class="slide-image" />

            <figcaption>
            <p    >If two variables <span class="blue">X</span> and <span class="orange">Y</span> are <strong>independent</strong>, then knowing <span class="orange">Y</span> will not change what we know about <span class="blue">X</span>. More formally, the conditional distribution p(<span class="blue">X</span>|<span class="orange">Y</span>) is the same as the distribution P(<span class="blue">X</span>): knowing the value of <span class="orange">Y</span> doesn't affect our knowledge of the value of <span class="blue">X</span>. <br></p><p    >If we fill in the definition of conditional probability and re-arrange the factors, we see that this implies that the joint probability of <span class="blue">X</span> and <span class="orange">Y</span> is just the product of the marginal probabilities p(<span class="blue">X</span>) and p(<span class="orange">Y</span>). Have a look at the joint probability of the <span class="green">age</span>/<span class="orange red">teeth</span> example. Are these independent random variables? What would it mean for the example if they were?<br></p><p    ><strong>Conditional independence </strong>means that the two variables<em> can</em> be<em> </em>dependent, but their dependence is entirely explained by a third variable Z. If we condition on Z, the variables become dependent.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-025">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-025" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0025.svg" class="slide-image" />

            <figcaption>
            <p    >Conditional independence comes up a lot, and it can be tricky to wrap your head around at first, so here’s an example.<br></p><p    >Imagine two people who work in different areas of a very big city. In principle, they work so far apart that whether or not they arrive home in time for dinner is completely independent. Knowing whether or not Alice is late for dinner tells you nothing about whether Bob is home in time for dinner. No aspect of their lives (weather, traffic) intersect in a meaningful way, except one. <br></p><p    >Very rarely, a large monster attacks the city. In that case, all traffic shuts down and everybody is late for dinner. That means that if we know that Bob is late for dinner, there is a slight chance that it’s because of the monster, which should slightly raise the possibility that Alice is late for dinner. However, once we know whether or not the monster has attacked, knowing that Bob is late provides no additional information.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-026">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-026" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0026.svg" class="slide-image" />

            <figcaption>
            <p    >Here is another visualization, taken from Wikipedia. This one is more abstract, but sometimes, sitting down with an abstract example and trying to work through it can help a lot to train your brain to get used to complex concepts. <em>If you're in a hurry, you can skip this one.</em><br></p><p    >Imagine throwing a dart at the square on the right. We look at the probability of hitting a yellow, red or blue square (the purple ones are both red and blue). Describe these events by boolean random variables <span class="orange">Y</span>, <span class="orange red">R</span> and <span class="blue">B</span>.<br></p><p    >We have p(<span class="orange red">R</span>) = 16<span>/49</span> and p(<span class="blue">B</span>) = 18<span>/49</span>.  These probabilities are <strong>not independent</strong>. We can work this out by counting all the squares for the event (<span class="orange red">R</span>, <span class="blue">B</span>) (<span class="orange red">R</span>, <span class="blue">¬B</span>), (<span class="orange red">¬R</span>, <span class="blue">B</span>) and (<span class="orange red">¬R</span>, <span class="blue">¬B</span>) and seeing if they are the product of the marginal probabilities, but we can also tell directly by looking at the picture: if we know that we've hit a blue square, there is a certain probability that that blue square is purple (i.e. also a red square). If we know that we haven't hit a blue square, there is also a certain probability that that square is red. The proportion of red inside the blue region looks different to the proportion of reds inside the non-blue region, so knowing whether we are in a blue square tells us something about how likely we are to be in a red square.<br></p><p    >Now, let's condition on <span class="orange">Y</span>. Somebody tells us the dart landed in a yellow square. Now that we know this, does knowing whether the square is blue still tell us anything about whether the square is also red? <strong>Note that within the yellow block, the proportion of red within the blues is the same as the proportion of reds within the non-blues. </strong>Once we're inside the yellow block, it doesn't matter anymore whether the block is blue. The probability of red is the same either way. Conditional on the knowledge that <span class="orange">Y=true</span>, the probabilities of red and blue are independent.<br></p><p    >What about when we hear that the dart has landed outside the yellow block? It's harder to see, but the proportions are 4/12 for the blue blocks and 8/25 for the nonblue. Thus the probabilities of blue and red are<strong> not conditionally independent given that </strong><strong class="orange">Y=false</strong>.<br></p><p    >By AzaToth at English Wikipedia, CC BY-SA 3.0, <a href="https://commons.wikimedia.org/w/index.php?curid=3206668"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=3206668</strong></a></p><p    ><a href="https://commons.wikimedia.org/w/index.php?curid=3206668"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-027">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-027" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0027.svg" class="slide-image" />

            <figcaption>
            <p    >Now that we have a decent understanding of conditional probability, let's look at Bayes' rule, probably the most important application of conditional probabilities.<br></p><p    >Bayes' rule is a solution to the inversion problem. What usually happens is that we have some idea of the mechanics of the world, and we observe some outcome, that could have happened through these mechanics in different ways. We didn't observe how it happened: that's the part that is hidden, and the part that we'd like to reason about. It's usually easy to reason about the probabilities of the outcomes given the observables (because we know the mechanics of the world) but we'd like to reverse this.<br></p><p    >For example imagine that you call a restaurant to book a table, and nobody picks up. This is unusual, and you wonder if it means the restaurant has burned down. You can easily reason <strong>forward</strong>, from the cause to the effect. If the restaurant has burned down, you would be sure that nobody would pick up the phone. If it hasn't, you would be quite sure that somebody would pick up the phone, but not certain. This is how you would reason if you <em>observed</em> whether or not the restaurant burned down and had to guess whether or not the phone would be answer. You are reasoning in the causal direction, so you use your understanding of the mechanics of the world to arrive at an intuitive conclusion.<br></p><p    >The problem is that we usually want to do <strong>backward</strong> reasoning. We observe the <em>outcome</em> of some event and we don't observe the <em>cause</em>. What we want to figure out is how to assign probabilities to the different causes. In this case, given that we observe nobody answering the phone, what is the probability that the restaurant has burned down?<br></p><p    >In short, we need a way to “turn around” the conditional probability. If we know p(<span class="blue">X</span>|<span class="orange">Y</span>), how do we work out p(<span class="orange">Y</span>|<span class="blue">X</span>)?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-028">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-028" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0028.svg" class="slide-image" />

            <figcaption>
            <p    >To do this, we need some additional probabilities. This makes sense if you think about our example. If the restaurant has burned down, we are sure that the phone won't be answered, but if we observe that the phone wasn't answered, we can't be sure that the restaurant has burned down. We need to take into account the fact that it's very rare for a restaurant to burn down, even though it would definitely lead to this observation. We also need to take into account the probability that something else has caused the restaurant to burn down. <br></p><p    >If the cause and effect are labeled <span class="orange">Y</span> and <span class="blue">X</span>, then the marginal probabilities p(<span class="orange">Y</span>) and p(<span class="blue">X</span>) capture all this information. <br></p><p    >This equation is the way Bayes' rule is usually written. You can prove that this is true very simply by starting with the definition of conditional probability and using the equation in slide 22 to rewrite the numerator.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-029">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-029" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0029.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>


       <section id="slide-030">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-030" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0030.svg" class="slide-image" />

            <figcaption>
            <p    >To build an intuitive understanding of why this formula works, let's return to the example of the monster attack. We'll focus on Alice only, and forget about Bob. <br></p><p    >Let’s say that we observe that Alice is late for dinner (and we observe nothing else). Does this tell us anything about whether a monster has attacked the city? It doesn’t tell us much; it’s extremely rare that a monster attacks the city so it’s almost certain that Alice is late for other reasons. Still, if Alice were on time, we’d know that a monster couldn’t. have attacked the city, since that would certainly make her late. So we may not know much, but we know something.<br></p><p    >In this case it’s easy for us to work out the probability that Alice is late given the monster attack. This is because the conditional is the cause of the observable. The opposite is usually what we are interested in, since we have the observable and want to reason about its cause. This is where Bayes’ rule comes in.<br></p><p    >Say that we know the probability that we observe Alice being late, given that a monster attack happened, p(<span>a</span> | <span>m</span>), is somewhere near 1. Bayes’ rule tells us how to use this to calculate the opposite conditional p(<span>m</span> | <span>a</span>). This is<em> not</em> near 1, because we multiply it by the marginal probability of a monster attack p(<span>m</span>), which is really low. We then divide by the probability of Alice being late in general p(<span>a</span>): the more likely Alice is to be late due to other causes, the lower the probability that it is caused by a monster attack.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-031">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-031" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0031.svg" class="slide-image" />

            <figcaption>
            <p    >If there are three possible reasons for Alice to be late: traffic, <span>monster</span> or snowfall. Then we can see the denominator as a sum marginalizing out the cause for Alice’s lateness. The proportion of this sum  given by the middle term is the probability that Alice’s lateness is caused by a monster attack.<br></p><p    >Consider the situation where both traffic and snowfall are far more likely than a monster attack, so p(t) and p(s) are much higher than p(<span>m</span>), but neither traffic nor snowfall ever cause Alice to be late, perhaps  because she cycles home from work, and has a bike with good snow tires. In that case both the first and last term in the sum become zero, and despite the fact that monster attacks are really rare, we can still conclude that a monster has attacked if we notice that Alice is late for dinner.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-031" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-032" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0032anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0032anim0.svg,31.ProbabilisticModels1.key-stage-0032anim1.svg" class="slide-image" />

            <figcaption>
            <p    >To finish up, we'll look at some of the most common probability distributions we'll see throughout the course. Most of these you should know already, but we'll summarize them here briefly for the sake of completeness.<br></p><p    >The simplest is probably the Bernoulli distribution. It's any a distribution with two outcomes. You can think of it as modelling the outcome of a coin flip with a (possibly) bent coin, but the outcome could also be true/false, guilty/innocent or positive/negative.<br></p><p    >Every distribution like this, with its probabilties set to some pair of values summing to 1 is <em>a</em> Bernoulli distribution. To specify which Bernoulli distribution we are talking about we specify one of the probabilities by a number. The other probability is then also defined, since they must sum to one. <br></p><p    >The numbers we use to specify which specific distribution we are talking about in a family like the Bernoulli distributions, are called the <strong>parameters</strong>, and often indicated by the greek letter theta, θ.You can think of θ as a set of vector of numbers. In the case of the Bernoulli distribution theta is just a single number. </p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-033">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-033" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0033.svg" class="slide-image" />

            <figcaption>
            <p    >If we have more than two outcomes, but still a finite number, we can assign each a separate probability so that they sum to one. For instance, if we want to model the outcome of rolling a loaded die, it might look like this. This is called a <strong>categorical distribution</strong>. Other examples are modeling which team will win the next world cup, which child in a classroom will score the highest on a test, or what the hair color of a random person from Ireland is. <br></p><p    >To specify a categorical distribution with n outcomes we strictly need only n-1 probabilities. We can work out the n-th probability from the knowledge that all probabilities sum to one. However, this is usually more trouble than it's worth, and instead we tend to represent categorical distributions by the slightly redundant complete set of n probabilities.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-034">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-034" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0034.svg" class="slide-image" />

            <figcaption>
            <p    >The <strong>normal distribution</strong> or<strong> Gaussian</strong> is probably the most common distribution on a continuous sample space. It is defined by this complex looking function. Don't worry about the formula too much now, we'll dig into that later. For now just remember that the curve it describes is the probability <em>density</em>.<br></p><p    >Its parameters are the <span class="orange">mean μ</span>, which tells us where the peak is, and the <span class="blue">variance σ</span><sup class="blue">2</sup> or <span class="blue">standard deviation σ</span>, which tells us how widely spread out the normal distribution is. <br></p><p    >The<em> standard</em><strong> normal distribution</strong> is the specific distribution with mean 0 and variance/standard deviation 1.<br></p><p    >The normal distribution is particularly useful for anything that has a <em>definite scale</em>. Consider, for instance height: people have all kinds of different heights, but if we get far enough away from the average, the probability gets so low it may as well be zero. We can say with near certainty that there are no 4 meter tall people and no 10cm tall people. If there were a hundred times as many people, that would still be true.<br></p><p    >An example of an attribute that doesn't have such a definite scale is income. In a small population there may be millionaires but no billionaires, but if we zoom out to the population of a small country, we will see billionaires appear. In a large country will we see people with fortunes in the order of 10 billion dollars and in the whole world we will see fortunes of 100 billion dollars. In short, the largest grows exponentially with the population size. <br></p><p    >In such cases, as we've seen, the normal distribution is not a good choice. We won't discuss them in this course, but so called fat-tailed distributions like the log-normal, Zipf or power law distributions may be more suitable.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-035">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-035" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0035.png" class="slide-image" />

            <figcaption>
            <p    >If our sample space consists of multiple numbers, for instance when we have a dataset with multiple features, we can draw this as an n-dimensional Euclidean space, like the plane shown here. A distribution over such a space can be defined by a probability density function over it, which, in the 2D case looks like a surface over the plane.<br></p><p    >The <strong>multivariate normal distribution</strong><em> </em>is an extension of the normal distribution to multiple dimensions. It takes the shape of a kind of bell over our sample space. For higher dimensions it's harder to visualize, just think of an ellipsoidal region in space taking most of the probability mass, with the probability density decaying quickly in all directions.<br></p><p    >Again, don't worry too much about the complicated formula for the probability density. We'll see where that comes from and what all the parts mean later.<br></p><p    >Its parameters are<span class="orange"> the mean </span><strong class="orange">μ</strong>, a vector which provides the center, and the <span class="blue">covariance matrix </span><strong class="blue">Σ</strong>, which tells us how much the probability decays in each direction. <br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-035" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-036" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0036anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0036anim0.svg,31.ProbabilisticModels1.key-stage-0036anim1.png,31.ProbabilisticModels1.key-stage-0036anim2.png,31.ProbabilisticModels1.key-stage-0036anim3.png" class="slide-image" />

            <figcaption>
            <p    >Here is an illustration of the way the covariance matrix affects the data we get from a multivariate normal distribution. The mean is at (0, 0) in all four examples. <br></p><p    >If the covariance is<span class="green"> the identity matrix</span>, we get the standard normal distribution. This is called a spherical distribution, because the variance along all axes is the same, and there is no correlation between axes, giving the data roughly spherical shape. <br></p><aside    >More precisely the lines of equal probability density are circles in 2D and spherical surfaces in higher dimensions.<br></aside><p    >If we <span class="blue">change the values on the diagonal</span>, we stretch this sphere into an ellipse, but only along the axes. There is still no correlation: knowing the value along one axis tells us nothing about the value along the others. <br></p><p    >If <span class="orange red">we change the off-diagonal values to positive values</span> we get <strong>correlation</strong>. In this case having a high value along one axis makes it more likely that the value along the other axis is also high. Note that the coviarance matrix needs to be symmetric, so the value on one side of the diagonal must be the same as the value on the other side.<br></p><p    >If <span class="orange">the off-diagonal value is negative</span>, we get <strong>anti-correlation</strong>. A high positive value on one axis most likely corresponds to a high negative value along the other axis.<br></p><p    >If we have more than 2 dimensions, say n, then there are (n^2 - n)/2 possible pairs of axes between which we can define a correlation. This corresponds exactly to the number of values above the diagonal in an n x n matrix.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>


       <section class="video" id="video-036">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-36">link here</a>
           <iframe
                src="https://www.youtube.com/embed/IubHHpzM32Y?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-037">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-037" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0037.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we'll start to connect probability theory with machine learning. We will first focus on <em>model selection</em>. We will not yet worry about abstract tasks like classification or regression, we will simply look a the case where we see some data, and we use probability theory to select a <em>model</em> for that data. In the next video, we will see how this translates to the abstract tasks we already know.<br></p><p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-037" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-038" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0038anim0.png" data-images="31.ProbabilisticModels1.key-stage-0038anim0.png,31.ProbabilisticModels1.key-stage-0038anim1.png" class="slide-image" />

            <figcaption>
            <p    >Here is an analogy for the way probability is usually applied in statistics and machine learning. We assume some “machine” (which could be any process, the universe, or an actual machine) has <em>generated</em> our data, by a process that is partly deterministic and partly random. The configuration of this machine is determined by its <strong>parameters </strong>(theta). Theta could be a single number, several numbers or even a complicated data structure.<br></p><p    >We know how the machine works, so if we know theta, we know the probability of each dataset. The problem is that we only observe the data.<br></p><p    >In practice, the "machine" takes the form of a probability distribution, and the configuration of the machine is determined by its parameters θ.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-039">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-039" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0039.svg" class="slide-image" />

            <figcaption>
            <p    >In <strong>frequentist learning</strong>, we are given some data and our job is to guess the true model (out of a model class) that generated some data. In other words, pick the right parameters θ so that the probability distribution fits the data well.<br></p><p    >In the frequentist view of the world, the true model is not subject to probability. Which model generated the data doesn’t change if we repeat the experiment, so we shouldn’t apply probability to it. We just try to guess which one it is. We won;t be exactly right, but we can hopefully get close. This is typical of frequentist approaches: we build algorithms that gives us a <strong>point estimate</strong> for our model parameters. That is , they return <em>one </em>point in our model space. One guess for θ.<br></p><p    >One of the most common criterion is that we should guess the model for which the probability of seeing the data that we saw is highest. This is called the<em> </em><strong>maximum likelihood principle</strong>. Under the maximum likelihood principle, picking a model becomes an optimization problem.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-040">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-040" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0040.svg" class="slide-image" />

            <figcaption>
            <p    >To explain both maximum likelihood fitting, let’s look at a simple example. We have two coins, a bent one and a straight one. Flipping these coins gives us different probabilities of heads and tails. <br></p><p    >We ask a friend to pick a random coin once without showing us, and to flip it twelve times. The resulting sequence has more heads than tails, but not such a disparity that you would never expect it from a fair coin. If we had to guess which coin our friend had picked, which should we guess?<br></p><p    >image source: <a href="https://www.magictricks.com/bent.html"><strong class="blue">https://www.magictricks.com/bent.html</strong></a><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-041">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-041" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0041.svg" class="slide-image" />

            <figcaption>
            <p    >This is a simple version of a <strong>model selection</strong> problem. Our model class consists of two models (the two coins) and our data consists of 12 instances (the results of the coin flips).<br></p><p    >In more technical terms, the coins are Bernoulli distributions with parameter 1/2 and  and 4/5 respetively. We could also look at the model space of all Bernoulli distributions, but to simplify matters we are looking at just these two.<br></p><p    >Under the frequentist view, we cannot assign probability to which coin produced this specific data, we can only provide a best guess which coin we consider most likely.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-042">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-042" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0042.svg" class="slide-image" />

            <figcaption>
            <p    >The maximum likelihood principle tells us to pick the coin for which the likelihood is the greatest. There are other principles (called <em>estimators</em>), but the maximum likelihood is usually the first thing to try. We simply compute, for both coins, the probability of the data that we saw given the coin. The coin that gives us the highest value is the coin we choose.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-043">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-043" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0043.svg" class="slide-image" />

            <figcaption>
            <p    >Since the coin flips are independent, the probability over the whole sequence is just the product over the probabilities of the individual flips. There’s not much in it, but the likelihood for the <em>bent </em>coin is slightly higher, so that’s the preferred model under the maximum likelihood criterion.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-044">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-044" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0044.svg" class="slide-image" />

            <figcaption>
            <p    >When we do this kind of computation, we often take the logarithm of the likelihood, instead of the plain likelihood. The logarithm is a monotonic function (it gets bigger if the input gets bigger) so the likelihood and the log-likelihood have their maxima in the same place, but the log-likelihood is often easier to manipulate symbolically (see the first homework exercise). It can also provide a smoother loss landscape for methods like gradient descent.<br></p><p    >The log-likelihood of a probability distribution is a lot like the loss functions we’ve already encountered many times.<br></p><p    >In fact, if we want to fit a probability distribution with a gradient based method, we usually take the <em>negative</em> log-likelihood, so that we can do gradient <em>descent</em> to find the optimum. <br></p><aside    >We could also use gradient ascent on the log-likelihood, but it's nice to keep the convention that you always minimize functions, and as we will see at the end of the lecture, the negative logarithm of a probability actually has a very natural interpretation.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-045">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-045" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0045.svg" class="slide-image" />

            <figcaption>
            <p    >As a second example of maximum likelihood, let's look at the univariate (i.e. 1D) normal distribution. This is defined by a complicated probability density function, which we don't fully understand yet. What we want to show here is how much of this complexity disappear just by taking the logarithm.<br></p><p    >The probability density of our whole data, given some mean and standard deviation, is simply the product of all individual probability densities. This follows from the assumption that instance data is independently drawn from the same distribution.  <br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-045" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-046" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0046anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0046anim0.svg,31.ProbabilisticModels1.key-stage-0046anim1.svg,31.ProbabilisticModels1.key-stage-0046anim2.svg,31.ProbabilisticModels1.key-stage-0046anim3.svg,31.ProbabilisticModels1.key-stage-0046anim4.svg,31.ProbabilisticModels1.key-stage-0046anim5.svg" class="slide-image" />

            <figcaption>
            <p    >We assume that X is a list of single numbers. We want to find the parameters that maximize the log probability density of this data given the parameters. The probability density of the whole dataset is simply the product of the individual probability densities, if we assume that the data was independently drawn from the same distribution.<br></p><p    >Since there's a factor factor raised to the power of e inside this function, we'll use the natural logarithm (base e). With a bit of luck, these will cancel out.<br></p><p    >We can turn this product into a sum by moving the logarithm inside. <em>This is explained in detail in the first homework.</em><br></p><p    >We fill in the definition of the actual probability density function we’re using (line 3). This function is the product of two factors (the division and the exponent). Both of these become terms if we work them out of the logarithm. In the second term the exponent cancels against the logarithm. Already the function we are maximizing looks a lot simpler.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-047">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-047" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0047.svg" class="slide-image" />

            <figcaption>
            <p    >This is enough to show that with the log likelihood we have another “landscape” on top of our model space. If we didn’t want to work out the rest analytically, we could just find the optimum by gradient descent or even random search.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-047" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-048" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0048anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0048anim0.svg,31.ProbabilisticModels1.key-stage-0048anim1.svg,31.ProbabilisticModels1.key-stage-0048anim2.svg,31.ProbabilisticModels1.key-stage-0048anim3.svg,31.ProbabilisticModels1.key-stage-0048anim4.svg" class="slide-image" />

            <figcaption>
            <p    >If we look at each parameter individually, we can reduce the problem even more.<br></p><p    >We can remove the first term, since it doesn't contain the mean. The factor 1/(2σ<sup>2</sup>) can be moved outside the sum and then removed (since a positive mulitplicative factor won't affect where the maximum is).<br></p><p    >Maximizing a function is the same as minimizing the negative of that function, so we can remove the minus and turn the argmax into an argmin.<br></p><p    >This shows that the maximum likelihood solution for the mean is just the value that minimizes the sum of the squared distances between the mean and the values in the dataset. This is how assuming a normal distribution leads to a least squares loss. If you work this out analytically, as we'll do in the next lecture, you'll see that the minimum for this is the (arithmetic) of the data, as you'd normally compute it. <br></p><aside    >This connection between the normal distribution, the least squares loss and the artihmetic mean is a deep one. Don't worry if you don't quite get it yet, we'll come back to this a few more times. For instance we'll see that historically, the order was the other way around, Gauss started with the arithmetic mean which was a tried and tested approach, worked out that it implied the least squares principle, and then built the normal distribution on top of that. But that's for later. For now, just make sure that you understand the basic principle of maximizing the likelihood.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-048" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-049" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0049anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0049anim0.svg,31.ProbabilisticModels1.key-stage-0049anim1.svg,31.ProbabilisticModels1.key-stage-0049anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We'll finish up with a quick look at <strong>Bayesian learning</strong>. Here, we are free to talk about the probability of the true model parameters taking a particular value. We don’t know the true parameters, but the data gives us some idea, so we express that uncertainty a probability distribution <em>over the model space</em>.<br></p><p    >That is, we'd like to know the distribution p(<span class="blue">θ</span>|D): a distribution over all available models, given the data that we've observed. As usual, the distribution with the reverse conditional p(D|<span class="blue">θ</span>) is much easier to work out. So the first thing we do is apply Bayes' rule to relate the two conditionals to one another.<br></p><p    >The distribution we want to work out is called the <strong>posterior distribution</strong>. Posterior means "after", as in: this is our belief about the true model <em>after</em> we've seen the data.<br></p><p    >The three parts of the right-hand side have these names. The <strong>prior distribution</strong> is a name you’ll hear often. Prior means before, as in: this is our belief about the true model <em>before</em> we've seen the data. For instance if we do spam classification in a Bayesian way, we might have a prior belief about the probability of getting a spam email, which we then <strong>update</strong> by looking at the content of the email (the data). Our beliefs about the parameters after seeing the data, is expressed by the posterior distribution. <br></p><p    >Note that Bayesian learning does, in principle, not require us to search or optimize anything. If we can work out the function on the right hand side of this equation, we get the posterior distribution and that gives us everything we need. If we need a good model, we can pick the one to which p(<span class="blue">θ</span>|X) assigns the highest probability, or we can sample a model and get a good fit with high probability. We can also study other properties of the distribution: for instance the variance of this distribution is a good indication of how uncertain we still are about the parameters of the model. <br></p><p    >In some cases, like for normal distributions, we can work all of this out analytically. For more complicated models, it’s usually impossible to work out the posterior analytically, and we have to make do with a function that approximates it, or with a number of individual  <em>samples </em>from the posterior. At that point, working out the posterior usually starts to look a lot like the searching we have to do in frequentist method and general machine learning.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-049" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-050" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0050anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0050anim0.svg,31.ProbabilisticModels1.key-stage-0050anim1.svg" class="slide-image" />

            <figcaption>
            <p    >That may all sound a little abstract, so let's return to our coin example and see what a Bayesian approach would look like there.<br></p><p    >We first need to establish a prior. What is the probability of each coin in our model space? We said that we’d asked a friend to pick a coin at random. If we assume that he follows our instructions, then we believe each coin is equally likely so both get 0.5 probability. If we had two fair coins and one bent one, we could set the prior to 1/3 for bent and 2/3 for fair. Or if we expected our friend to have a preference for the bent coin, we might set our prior differently.<br></p><p    >This is an important thing to understand about choosing a prior: it allows us to encode our assumptions about the problem. As we will see again and again, encoding your assumptions is the most important part of designing machine learning models.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-050" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-051" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0051anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0051anim0.svg,31.ProbabilisticModels1.key-stage-0051anim1.svg,31.ProbabilisticModels1.key-stage-0051anim2.svg,31.ProbabilisticModels1.key-stage-0051anim3.svg" class="slide-image" />

            <figcaption>
            <p    >After the prior, we need to work out the model evidence p(D). This is the probability of the data with the model marginalized out. Independent of the model, how likely are we to see this data at all? We work this out by making the marginalization explicit, and replacing the joint probabilities by their conditionals.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-052">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-052" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0052.svg" class="slide-image" />

            <figcaption>
            <p    >Remember, the long form of Bayes' rule, with the denominator a long sum over all the causes, and the numerator one of the terms in this sum. That view applies here as well: we see the available models (bent and straight) as the two possible causes for our data. The marginal probability of seeing this data is the probability of picking straight and seeing it plus picking bent and seeing it. The proportion of the straight term in this sum is the probability of seeing straight given the data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-052" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-053" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0053anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0053anim0.svg,31.ProbabilisticModels1.key-stage-0053anim1.svg" class="slide-image" />

            <figcaption>
            <p    >If we choose a  uniform prior (each model gets the same probability), then the priors cancel out and we are just left with a function of the conditional data probabilities that we've worked out already for the frequentist example.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-054">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-054" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0054.svg" class="slide-image" />

            <figcaption>
            <p    >Filling these in gives us posterior probabilities for the <span class="orange red">straight</span> and the <span class="green">bent</span> coins.<br></p><p    >Note the difference with the maximum likelihood case. Both approaches prefer the <span class="green">bent</span> model as an explanation for the data.<br></p><p    >However, in the maximum likelihood case, even though the differences between the two likelihoods were small, we only provided<em> one </em>guess for the true model. In the Bayesian approach we get a <em>distribution</em> on the model space. It tells us not just that <span class="green">bent</span> is the more likely model, but also that<em> both models</em> are still quite likely. In this sense, getting a posterior distribution is a much more valuable result than getting a point estimate for your model.<br></p><p    >The downside of Bayesian analysis is that as the models get more complex, it gets more and more difficult to accurately approximate the posterior, and trying to do so is what has led to some of the most complicated material in machine learning. Working out the posterior for the mean of a normal distribution is already a bit too technical for this course, but it's a good exercise to try and imagine what it would involve.</p><p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-054">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-54">link here</a>
           <iframe
                src="https://www.youtube.com/embed/fK6dQYkeVqA?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-055">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-055" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0055.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we’ll try to connect this probability business to the abstract tasks of machine learning. <br></p><p    ><lnbr></lnbr></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-056">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-056" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0056.svg" class="slide-image" />

            <figcaption>
            <p    >We will focus on building <strong>probabilistic classifiers</strong>. These are classifiers that return not just a class for a given instance x (or a ranking) but a <em>probability over all classes</em>.<br></p><p    >This can be very useful. We can use the probabilities to extract a ranking (and plot an ROC curve) or we can use the probabilities to assess how certain the classifier is about its judgement. <br></p><p    >Note that a probabilistic classifier is also immediately a ranking classifier (if we rank by how likely the positive class is) and a regular classifier (if we pick the class with the highest probability).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-056" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-057" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0057anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0057anim0.svg,31.ProbabilisticModels1.key-stage-0057anim1.svg" class="slide-image" />

            <figcaption>
            <p    >There are two approaches to casting the classification problem in probabilistic terms. <br></p><p    >A <strong>generative classifier</strong> focuses on learning a distribution on the feature space given the class p(X|<span>Y</span>). This distribution is then combined with Bayes’ rule to get the probability over the classes, conditioned on the data.<br></p><p    >A<strong> discriminative classifier</strong> learns the function p(<span class="blue">Y</span>|X) directly with X as input and class probabilities as output. It functions as a kind of regression, mapping x to a vector of class probabilities.<br></p><p    > We’ll look at some simple generative classifiers in this video, and then we'll describe a discriminative classifier in the next video.<br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-058">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-058" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0058.svg" class="slide-image" />

            <figcaption>
            <p    >Here are three approaches, arranged from impractical but entirely correct to highly practical, but based on largely incorrect assumptions.<br></p><p    >We won’t discuss the Bayes optimal classifier in this course, but it’s worth knowing that it exists, and that it means something different than a (naive) Bayes classifier.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-059">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-059" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0059.svg" class="slide-image" />

            <figcaption>
            <p    >For the Bayes classifier, we start with the probability we’re interested in p(<span class="blue">Y</span>|X): the probability of the class given the data. We then rewrite this using Bayes’ rule. From the final form, we see that if we compute the probability functions p(X|<span class="blue">Y</span>), the data given the class and p(Y), the prior probability of the class, we can compute the probabilites we;re interested in: the class probabilities given the data.<br></p><p    >So the task becomes to learn functions for those two probabilties. The most important part will be P(X|<span class="blue">Y</span>). We can model this by separating the data by class and fitting a probability distribution to each subset individually.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-059" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-060" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0060anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0060anim0.svg,31.ProbabilisticModels1.key-stage-0060anim1.svg,31.ProbabilisticModels1.key-stage-0060anim2.svg,31.ProbabilisticModels1.key-stage-0060anim3.svg,31.ProbabilisticModels1.key-stage-0060anim4.svg,31.ProbabilisticModels1.key-stage-0060anim5.svg,31.ProbabilisticModels1.key-stage-0060anim6.svg" class="slide-image" />

            <figcaption>
            <p    >Here is the algorithm for a simple Bayes classifier. We choose a model class for P(X|Y), for instance multivariate normal distributions. <br></p><p    >We then separate the points by classes and fit a separate MVN to each of these subsets of the data. We use the maximum likelihood estimates to fit the MVNs to the instances. <br></p><aside    >Note that this make the Bayes classifier a bit of a Bayesian/frequentist chimera: we are using Bayes' rule to reverse the conditional, but we are using point esitmates to fit our distributions.<br></aside><p    >The <strong>class prior</strong> p(<span class="blue">Y</span>) is a simple categorical distribution over the classes. We can estimate this from the data, or use some kind of prior knowledge that we have about the domain.<br></p><p    >Strictly speaking, we are mixing probabilities and probability densities, but in this example that doesn't cause any problems. The resulting probability on the classes is a categorical distribution.<br></p><aside    >When we compute the class probabilities, we can compute the term p(x | class)p(class) once for each term, and then re-use them in the computation of each class probability. If we are only interested in the most probable class or in the ranking, we can omit the computation of the denominator.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-061">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-061" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0061.svg" class="slide-image" />

            <figcaption>
            <p    >Here is an example of what that looks like with 2 features. On the left we have two classes, blue and black. We fit a 2D normal distribution to each, represented by the blue and black ellipses. Then, for a new point, we see which assigns the new point the highest probability density, or compute the full probabilities.<br></p><p    >The red line provides the decision boundary: the points where the two probability densities are exactly equal.<br></p><p    ><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-062">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-062" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0062.svg" class="slide-image" />

            <figcaption>
            <p    >This works well for small numbers of features, but if we have many features, modelling the dependence between each pair of features gets very expensive. <br></p><p    >A crude, but very effective solution is <strong>Naive Bayes</strong>. This just assumes that all features are independent, conditional on the class (whatever the class).<br></p><p    >Note that <em>we do not assume that the features are independent</em>: it’s perfectly possible for one feature to be dependent on another feature, but they are <em>conditionally</em> independent. Informally, the dependency between the features is “caused” by the class and nothing else. Just like Alice and Bob in the first video: their lateness had only one possible shared cause, the monster, and once we’d isolated that, their lateness was independent.<br></p><p    >Since naive Bayes is often used with categorical features, we'll start with an example that uses these.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-063">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-063" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0063.svg" class="slide-image" />

            <figcaption>
            <p    >Here is an example dataset, with binary features. Each feature indicates whether a particular word occurs in that instance.<br></p><p    >We are bulding a generative classifier, so we should start by estimating the probability of the data given the class. The Naive Bayes assumption says that we can do this for each feature independently and just multiply the probabilities. <br></p><p    >We will estimate p(“pill”|<span class="orange red">spam</span>) as the relative frequency with which the “pill” feature was<span class="blue"> true</span> for <span class="orange red">spam</span> emails, and similar for the other feature.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-064">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-064" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0064.svg" class="slide-image" />

            <figcaption>
            <p    >Here's what those estimates look like.<br></p><aside    >Strictly speaking, we are modelling X<sub>1</sub> as a Bernoulli distribution whose parameter we estimate as 2/6. This estimation, using the relative frequency of outcome x as the probability of x, is the maximum likelihood estimate for the Bernoulli distribution. If that sounds too complicated, it hopefully also makes intuitive sense to estimate the probabilities this way.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-065">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-065" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0065.svg" class="slide-image" />

            <figcaption>
            <p    >We do the same for the <span class="orange red">spam</span> class and for the other feature.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-066">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-066" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0066.svg" class="slide-image" />

            <figcaption>
            <p    >This is the naive Bayes assumption formulaically. We simply factor p(X1,…Xn) into n separate, independent probabilities. That means we can take our estimates for the probability of each feature, and multiply them together to get the probability of the whole instance.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-066" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-067" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0067anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0067anim0.svg,31.ProbabilisticModels1.key-stage-0067anim1.svg,31.ProbabilisticModels1.key-stage-0067anim2.svg,31.ProbabilisticModels1.key-stage-0067anim3.svg" class="slide-image" />

            <figcaption>
            <p    >This gives us a probability for the whole instance space. Now, let's imagine a new email comes in, one which contains the words <em>pill</em> and <em>meeting</em>. What class do we think it is? <br></p><p    >The probability of it being ham is proportional to the probability of seeing a ham email with these characteristics times the probability of seeing a ham email at all. The first factor breaks up by the naive Bayes assumption, and we can simply fill in our three probability estimates. We do the same thing for spam and report wich class gets the high probability <br></p><aside    >Note that we are only computing the numerator of Bayes' rule. This is enough to work out which class gets the higher probability.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-067" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-068" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0068anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0068anim0.svg,31.ProbabilisticModels1.key-stage-0068anim1.svg,31.ProbabilisticModels1.key-stage-0068anim2.svg,31.ProbabilisticModels1.key-stage-0068anim3.svg" class="slide-image" />

            <figcaption>
            <p    >If we work out the probability of spam in the same way, we see that the Naive Bayes classifier assigns the class ham the most probability. If we want proper class probabilities all we have to do is normalize these values (that is, divide by (5/33) + (3/55)).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-069">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-069" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0069.svg" class="slide-image" />

            <figcaption>
            <p    >While Naive Bayes can work surprisingly well (given how strong and incorrect the assumption is), with these estimators, we do run into a problem if for some feature a particular value does not occur. In that case, we estimate the probability as 0.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-070">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-070" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0070.svg" class="slide-image" />

            <figcaption>
            <p    >Since the whole estimate of our probability is just a long product, if one of the factors becomes zero, <strong>the whole things collapses</strong>. Even if all the other features gave this class a very high probability, that information is lost.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-071">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-071" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0071.svg" class="slide-image" />

            <figcaption>
            <p    >To remedy this, we need to apply <strong>smoothing</strong>. The simplest waY to do that is to add pseudo-observations. For each possible value, we add one instance where all the features have that value. This may seem like we're ruining our data with fake examples, but if we have a large dataset the impact should be minimal (and we'll see a way to minimize the impact even further later).<br></p><p    >(We should do the same for the class <span class="green">ham</span>).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-071" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-072" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0072anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0072anim0.svg,31.ProbabilisticModels1.key-stage-0072anim1.svg" class="slide-image" />

            <figcaption>
            <p    >This changes our estimates as shown here. In practice, we don’t actually need to add the pseudo-observations, we just change our estimator.<br></p><p    >Here, v is the number of different values X<sub>1</sub> can take.<br></p><p    >If we are worried about the impact of the pseudo-observations we can reduce the weight they have among the observations. For all other observations the weight is 1 in all relative frequencies. By replacing 1 for the pseudo-observations with λ, and setting this to a low value like 0.01, we get the estimator shown. This makes the impact of the pseudo observations very small, but it still ensures that we will never see a zero.<br></p><aside    >If you do a Bayesian analysis, you can derive exactly this estimator by setting a particular prior. In fact, many common priors can be framed as pseudo-obervations. We won't dig into this in the course, but it is very neat.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-073">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-073" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0073.svg" class="slide-image" />

            <figcaption>
            <p    >Naive Bayes is commonly associated with categorical features (to which Bernoulli or Categorical distributions are fitted), but it can also be used with numerical features. If we use normal distributions, then the independence assumption means that we fit a univariate normal distribution to each feature independently. The distribution over the whole space for each class then becomes a multivariate normal whose covariance matrix is diagonal (all off-diagonal elements are zero). Visually, this means that the distribution looks like an ellipsoid that is stretched along the axes. <br></p><p    >The kind of ellipse shown on the bottom, which is stretched in an abitrary direction <em>is</em> a multivariate normal, but not one where the features are independent. So this kind of fit would only be allowed in a non-naive Bayes classifier. Note that this requires full covariance matrix to specify, so that the number of model parameters grows quadratically with the number of features, while the number of parameters for the Naive Bayes classifier only grows linearly.<br></p><p    >source: <a href="http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes"><strong class="blue">http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes</strong></a></p><p    ><a href="http://learning.cis.upenn.edu/cis520_fall2009/index.php?n=Lectures.NaiveBayes"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-074">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-074" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0074.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-074">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-74">link here</a>
           <iframe
                src="https://www.youtube.com/embed/EYhxR22Ta88?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-075">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-075" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0075.svg" class="slide-image" />

            <figcaption>
            <p    ><lnbr></lnbr><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-076">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-076" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0076.svg" class="slide-image" />

            <figcaption>
            <p    >In this video we’ll look at an example of a discriminative classifier: <strong>logistic regression</strong>. This is a classifier that learns to map the features directly to class probabilities, without using Bayes’ rule to reverse the conditional probability. <br></p><p    >This is basically a small extension of the linear classifier we've already seen. You can also think of it as a linear classifier with a specific loss function.<br></p><aside    >The name logistic <span>regression</span> is very confusing, but in the modern view it is a classifier, not a regression model.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-077">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-077" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0077.svg" class="slide-image" />

            <figcaption>
            <p    >Remember that we were still on the lookout for good loss functions for the classification problem. We’ll use the language of probability to define one for us.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-078">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-078" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0078.svg" class="slide-image" />

            <figcaption>
            <p    >This was our last attempt: the <em>least squares loss</em>.<br></p><p    >Our thinking was: the hyperplane classifier checks if <strong class="orange">w</strong><sup>T</sup><strong>x </strong>+ <span class="blue">b</span> is positive or negative, to decide whether to assign classes <span class="blue">positive</span> (blue discs) or <span class="orange red">negative </span>(red diamonds), respectively. Why not just give the classes some arbitrary positive and negative values (-1 and +1), and treat it as a regression problem?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-079">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-079" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0079.svg" class="slide-image" />

            <figcaption>
            <p    >Here is another option: instead of assigning the two classes arbitrary values, we assign them <em>probabilities</em>: specifically, <em>the probability of being positive.</em> This is 1 for allpoints in the <span class="blue">positive</span> class and 0 for all points in the <span class="orange red">negative</span> class. Compared to the least squares approach, we just assign the <span class="orange red">negative</span> class points the value 0 instead of -1.<br></p><p    >Does this give us a probabilistic classifier? Can we fit a linear regression line to these points and interpret the output as the probability of the feature being positive, conditioned on the feature value(s)? If we fit a line through these points, the picture, it doesn’t look substantially different to the previous slide, because our function <strong class="orange">w</strong><sup>T</sup><strong>x </strong>+ <span class="blue">b</span> still ranges from negative infinity to positive infinity. We'd like it to produce values between 0 and 1, so we can always interpret them as probabilities, but it only does that for a very narrow and arbitrary range.<br></p><p    >What we need, is a way to squeeze the whole infinite range of the linear function into the range [0, 1], so that the model will ever produce valid probabilities.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-079" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-080" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0080anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0080anim0.svg,31.ProbabilisticModels1.key-stage-0080anim1.svg" class="slide-image" />

            <figcaption>
            <p    >For this purpose, we will use the <strong>logistic sigmoid</strong> function shown here. A sigmoid function is a function that makes an s-shape like this: its domain is the entire real number line, its range is between two finite values, 0 and 1 in this case, and it increases monotonically. Informally, it squeezes the whole real number line into a finite interval in a smooth way. The<em> logistic</em> sigmoid shown here is just one of many sigmoid functions.<br></p><aside    >The second definition, in grey, is equal to the first. You can show this easily by multiplying both the numerator and the denominator by e<sup class="orange red">t</sup> in the first definition.<br></aside><p    >source: By Qef (talk) - Created from scratch with gnuplot, Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=4310325"><strong class="blue">https://commons.wikimedia.org/w/index.php?curid=4310325</strong></a><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-080" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-081" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0081anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0081anim0.svg,31.ProbabilisticModels1.key-stage-0081anim1.svg" class="slide-image" />

            <figcaption>
            <p    >We'll see a lot more of the logistic sigmoid as the course progresses, so make sure to remember it. The reason we like to use this specific sigmoid in machine learning settings is that it has a few nice properties that make analysis easier.<br></p><p    >The first is its <strong>symmetry</strong>: if you flip it upside down, or left to right, you get the same function, which is the sigmoid running in the opposite direction σ(-t). Basically the remainder between σ(t) and 1, is itself a sigmoid. We'll use this property later in this video.<br></p><p    >The second property is that the<strong> derivative</strong> of the sigmoid has a particularly simple form: it's equal to the sigmoid itself times one of these flipped sigmoids.<br></p><aside    >Both of these properties are easy enough to work out from the definition on the previous slide. We'll save you this to keep the lecture simple, but it's a good exercise if have the time to try.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-082">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-082" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0082.svg" class="slide-image" />

            <figcaption>
            <p    >With this, we can build our new classifier: we compute the linear function as before, but we apply the logistic sigmoid to its output , squeezing it into the interval [0, 1]. This means that we can interpret the output as the probability of the positive class. <br></p><p    >This may be a very accurate probability, or a very inaccurate one, depending on how we choose <strong class="orange">w</strong> and <span class="blue">b</span>, but it’s always a value between 0 and 1. Hopefully, if we choose the parameters w and b well, we'll get a probability distribution that assigns high probability to the<span class="blue"> blue</span> points and low probability to the<span class="orange red"> red </span>points.<br></p><p    >Now all we need is a<strong> loss function</strong> that tells us which probabilities match the data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-083">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-083" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0083.svg" class="slide-image" />

            <figcaption>
            <p    >For this we'll introduce the <strong>log(arithmic) loss</strong>. This is also know as the (binary) cross-entropy loss, for reasons we'll explain in the next video.<br></p><p    >At heart, this is just the maximum likelihood principle at work. We have some data, the class labels, and a model with some parameters, <strong class="orange">w</strong> and <span class="blue">b</span>. We are looking for the parameters that maximize the probability of the data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-084">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-084" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0084.svg" class="slide-image" />

            <figcaption>
            <p    >We assume that the instances in our data are independent, so that the probability of all class labels is just the probabilities of the individual class labels multiplied together. Since we have a discriminative classifier, we are not modeling the features. We take them as given and directly maximize the probility of the labels given the features.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-084" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-085" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0085anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0085anim0.svg,31.ProbabilisticModels1.key-stage-0085anim1.svg,31.ProbabilisticModels1.key-stage-0085anim2.svg,31.ProbabilisticModels1.key-stage-0085anim3.svg,31.ProbabilisticModels1.key-stage-0085anim4.svg" class="slide-image" />

            <figcaption>
            <p    >Since, as we've seen, the logarithm of the probability of often better behaved, we will maximize the log-probability of the class labels given the features. Since we like to minimize—we are looking for a<em> loss function</em> so lower should be better—we stick a minus in front of the log probability and change the argmax to an argmin.<br></p><p    >Then, the multiplication can be moved out of the logarithm, turning it into a sum. <br></p><p    >Finally, we separate the data into the positive and negative classes. Our loss function says that for the positive poitns we want to maximize the log probability the classifier assigned to the point being positive and for the negative classes we want to maximize the probability that the classifier assigns to the point being negative. Hopefully, this sounds intuitive so far.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-086">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-086" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0086.svg" class="slide-image" />

            <figcaption>
            <p    >Before we move on, let's try to visualize what we have so far.<br></p><p    >In the least-squares case, the loss function could be thought of in terms of the <em class="green">residuals</em><span class="green"> </span>between the prediction and the true values. They pull on the line like rubber bands.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-087">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-087" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0087.svg" class="slide-image" />

            <figcaption>
            <p    >For the logarithmic loss on the logistic classifier, we can imagine the residuals as the lines drawn here. The logarithmic loss tries to maximize the sum of their logarithm (or minimizetheir negative logarithm).<br></p><p    >You can think of them as little rods pushing up (for the blue rods) and down (for the red rods) on the sigmoid function to push it towards the relevant instances.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-088">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-088" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0088.svg" class="slide-image" />

            <figcaption>
            <p    >Remember that in the least squares loss we squared the residuals before summing them, to punish outliers. Taking the logarithm has a similar effect. For those instances where the probability is near the value it should be, we are taking the negative logarithm of a value very close to zero. That means that there points, which are far away from the decision boundary, contribute very little to the loss.<br></p><p    >The next question is how do we minimize this loss? We'll use gradient descent, which means that we need to work out the derivatives with respect to the parameters. <br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-089">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-089" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0089.svg" class="slide-image" />

            <figcaption>
            <p    >The next couple of slides show a (somewhat) complicated derivation. You should do your best to go through this step by step. There are a couple more of these coming up in the course, so if you don't take the time to get used to them, you'll struggle later on. If you do take the time, I promise it gets easier with a little practice.<br></p><p    >You don't, however, have to understand this <em>right away</em>. If you struggle to follow along,<em> just look at the start and end points</em>. Try to figure out what the derivation is trying to show and why this is important. Then, move on to the rest of the lecture and come back for the details later. <br></p><aside    >If you haven't done the second homework exercise yet, it may be better to do that first, and then come back to this part of the video. After that exercise, you should have a more practical understanding of what we're trying to do here.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-089" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-090" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0090anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0090anim0.svg,31.ProbabilisticModels1.key-stage-0090anim1.svg,31.ProbabilisticModels1.key-stage-0090anim2.svg,31.ProbabilisticModels1.key-stage-0090anim3.svg" class="slide-image" />

            <figcaption>
            <p    >What we need is the derivative of the loss with respect to every parameter of the model. We'll work it out for the weights <span class="orange">w</span><sub class="orange">i</sub> and take the bias <span class="blue">b</span> as read. <br></p><p    >We’ll show you the basics of working out the gradient for logistic regression. The first step is to break the loss apart in separate terms for the positive and negative points. We'll look at the positive term in detail (the negative term can be derived in a similar way).</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-090" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-091" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0091anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0091anim0.svg,31.ProbabilisticModels1.key-stage-0091anim1.svg,31.ProbabilisticModels1.key-stage-0091anim2.svg,31.ProbabilisticModels1.key-stage-0091anim3.svg,31.ProbabilisticModels1.key-stage-0091anim4.svg,31.ProbabilisticModels1.key-stage-0091anim5.svg,31.ProbabilisticModels1.key-stage-0091anim6.svg,31.ProbabilisticModels1.key-stage-0091anim7.svg,31.ProbabilisticModels1.key-stage-0091anim8.svg,31.ProbabilisticModels1.key-stage-0091anim9.svg" class="slide-image" />

            <figcaption>
            <p    >To simplify the derivation, we first take the output of the linear part of our model (before it goes into the sigmoid) and call it y. Not that the derivative of y with respect <span class="orange">w</span><sub class="orange">i</sub> is just xi, because the dot product is a simple sum of element-wise multiplications, so the only term that wi appears in is <span class="orange">w</span><sub class="orange">i </sub>x<sub>i</sub>.<br></p><p    >With this, we can work out the partial derivative with respect to <span class="orange">w</span><sub class="orange">i</sub> in a relatively clean and simple manner. We start (line 1) by filling in q<sub>x</sub>(<span class="blue">P</span>), the probability according to our current classfier that the point x is in the <span class="blue">positive</span> class (which it is). This is just the output <span class="orange red">y</span> of the linear function, passed through the logistic sigmoid σ.<br></p><p    >Next (line 2), we apply the chain rule twice. First to move out of the logarithm, and then to move out of the sigmoid. <br></p><p    >For each of these three factors, we can work out the derivative (line3). The derivative of log(x) is 1/x. That is, assuming we are using the natural logarithm. If we want to use a different logarithm (like base-2), then we get a constant multiplier, which we can ignore if we are using gradient descent (because we are scaling the gradient by η anyway). The derivative of the sigmoid wrt to <span class="orange red">y</span> is the sigmoid times the flipped sigmoid, and the derivative of <span class="orange red">y</span> wrt to <span class="orange">w</span><sub class="orange">i</sub> we have already worked out.<br></p><p    >The factor σ(<span class="orange red">y</span>) appears above and below the division line, so these cancel out (line 4), leaving us with just the flipped sigmoid times x<sub>i</sub>. We note that the flipped sigmoid is one minus the probability of the positive class (according to our classifier). since there are only two classes, this equals the probability of the negative class q<sub>x</sub>(<span class="orange red">N</span>). We fill this in, which provides our answer.<br></p><p    ><br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-092">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-092" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0092.svg" class="slide-image" />

            <figcaption>
            <p    >Note that despite the complicated business in the middle, the result is actually very simple. This is one of the pleasing properties of the logistic sigmoid, it tends to cancel itself out when the derivative is taken.<br></p><p    >In short, for this particular instance, and weight i, the derivative is the i-th feature times the probability (according to the current parameters) that this instance is negative.<br></p><p    >Consider what this means in a gradient descent setting: this value here is what we want to subtract from the current value of <span class="orange">w</span><sub class="orange">i</sub> to better fit the classifier to this particular point x.  Imagine that the classifier does badly at the moment: to this<span class="blue"> positive</span> point it assigns a large probability for the <span class="orange red">negative</span> class, so q<sub>x</sub>(<span class="orange red">N</span>) is large. <br></p><p    >If x<sub>i</sub> is a large positive value, then gradient descent subtracts a large negative number, - q<sub>x</sub>(<span class="orange red">N</span>)x<sub>i</sub>, from <span class="orange">w</span><sub class="orange">i</sub>. This makes it bigger, increasing the sum the sum <strong class="orange">w</strong><sup>T</sup><strong>x</strong> + <span class="blue">b</span> and reducing the probability σ(<strong class="orange">w</strong><sup>T</sup><strong>x</strong> + <span class="blue">b</span>) that the classifier assigns to the positive class. If x<sub>i</sub> is a large <em>negative</em> number, we go in the opposite direction.<br></p><p    >If, however, the classifier already does well, assigning this positive point a large <span class="blue">positive</span> probability, then q<sub>x</sub>(<span class="orange red">N</span>) is very close to 0, and this particular instance has very little influence on the gradient descent step (unless the magnitude of x<sub>i</sub> is so big that x<sub>i</sub>q<sub>x</sub>(<span class="orange red">N</span>) is still a substantial value).</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-093">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-093" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0095.svg" class="slide-image" />

            <figcaption>
            <p    >If we work out the derivative for the other term, we get a predictable result: the same form, but with q<sub>x</sub>(<span class="blue">P</span>) instead of q<sub>x</sub>(<span class="orange red">N</span>) and a minus instead of a plus.<br></p><p    >So there we have it: the gradient for a linear classifier, fed through a sigmoid function, producing a logarithmic loss.<br></p><aside    >For the bias <span class="blue">b</span>, we get the same result, but without the x<sub>i</sub> factors. The derivation is the same, except that in the second line of the derivation the third factor is 1 instead of x<sub>i</sub>.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-094">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-094" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0096.svg" class="slide-image" />

            <figcaption>
            <p    ><em>Regression</em> is a bit of misnomer, since we’re building a classifier. I suppose the confusing terminology comes from the fact that we’re fitting a (curved) line through the probability values in the data. Just one of the many confusing names in the field of machine learning, I'm afraid.<br></p><p    >Anyway, now that we have a gradient, we can apply gradient descent. Let's see the model in action.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-095">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-095" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0097.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a 2D dataset that shows a common failure case for the least squares classifier. The points at the top are so far away from the ideal decision boundary that they will have huge residuals under the least squares model.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-096">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-096" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0098.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what the least-square regression converges to. Clearly, this is not a satisfying solution for such an easily separable dataset. The blue points at the top are so far from the decision boundary.<br></p><p    >In the linear models 1 lecture, we fixed one of the parameters to 1, so that we could plot the loss surface. This time, we’re optimizing all three parameters.<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-097">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-097" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0099.svg" class="slide-image" />

            <figcaption>
            <p    >Here is a 1D view of a similar situation. The green bar is the decision boundary that we want, but any line that crosses the horizontal axis there has really big residuals for the far away points. These pull on the line with a quadratic strength, so the decision boundary will always be pulled toward them.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-097" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-098" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0100anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0100anim0.svg,31.ProbabilisticModels1.key-stage-0100anim1.svg" class="slide-image" />

            <figcaption>
            <p    >The logistic model doesn’t have this problem.If the model fits well around the ideal decision boundary, it doesn’t have to worry at all about points that are far away (if they’re on the right side of the boundary). The log loss for these points is very close to -log(1), so very close to 0.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-099">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-099" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0101.svg" class="slide-image" />

            <figcaption>
            <p    >Here is what the logistic regression chooses as a decision boundary. Unlike the least squares regression, the points are perfectly separated.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-100">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-100" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0102.svg" class="slide-image" />

            <figcaption>
            <p    ><br></p><p    >We can also plot the probability function usuing a color map (blue is high probability of <span class="blue">positive</span>, red is high probability of <span class="orange red">negative</span>). The white band in the middle is where the probability of positive is near 0.5. That is, in this region, the classifier is <em>uncertain</em>. <br></p><p    >Uncertainty in machine learning is a difficult problem, and models like these that that can express their certainty about a classification are usually much more certain than they should be, so be sure to take this with a grain of salt. Still, it's nice that the model can at least <em>express</em> its uncertainty.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-101">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-101" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0103.svg" class="slide-image" />

            <figcaption>
            <p    >Note that for such well-separable classes, there are many suitable decision boundaries, and logistic regression has little reason to prefer one over the other (all points are assigned the correct probability very close to 1). We’ll see a solution to this problem next lecture, when we meet our final loss function: the SVM loss.<br></p><aside    >If we want to stick with logistic regression we can solve this problem to some extent by widening the "region of uncertainty" as much as possible, without sacrificing too much of the log loss. One way to achieve this is by adding L2 regularization, which we will learn about in a later lecture.</aside><aside    ></aside>
            </figcaption>
       </section>


       <section id="slide-102">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-102" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0104.svg" class="slide-image" />

            <figcaption>
            <p    ></p>
            </figcaption>
       </section>

       <section class="video" id="video-102">
           <a class="slide-link" href="https://mlvu.github.io/lecture04#video-102">link here</a>
           <iframe
                src="https://www.youtube.com/embed/mSneVjDvzNQ?modestbranding=1&showinfo=0&rel=0"
                title="YouTube video player"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
           </iframe>

       </section>

       <section id="slide-103">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-103" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0105.svg" class="slide-image" />

            <figcaption>
            <p    >The last video was all about defining a probability p(x) and then taking the negative logarithm of that probability. We justified this by saying that the logarithm of the likelihood is easier to work with, and that as a convention we tend to minimize rather than maximize in machine learning  so we took the negative of the log likelihood. All very pragmatic.<br></p><p    >But actually, there is a very concrete meaning to the negative log likelihood of a probability, that can really help to deepen our understanding of what we are doing when we use probabilities in machine learning. To understand this, we need to dig briefly into the topic of <strong>information theory</strong>. This will not just help us understand probability from a new perspective, it will also provide us with the concept of <strong>entropy</strong>, which is an important tool we will use at different points in the course.<br></p><p    ><lnbr></lnbr><br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-104">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-104" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0106.svg" class="slide-image" />

            <figcaption>
            <p    >Imagine you’re on holiday, and you’ve brought your travel monopoly. Unfortunately, the dice have gone missing. You do however, have a coin with you. Can you use a coin flip to simulate the throw of a six sided  die?<br></p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-105">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-105" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0107.svg" class="slide-image" />

            <figcaption>
            <p    >For a four sided die, the solution is easy. We flip the coin twice, and assign a number to each possible outcome.<br></p><p    >source: <a href="http://www.midlamminiatures.co.uk/blackpolydice/D4Black.html"><strong class="blue">http://www.midlamminiatures.co.uk/blackpolydice/D4Black.html</strong></a></p><p    ><a href="http://www.midlamminiatures.co.uk/blackpolydice/D4Black.html"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>


       <section id="slide-106">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-106" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0108.svg" class="slide-image" />

            <figcaption>
            <p    >A six sided die is more tricky. We’ll show the solution for three “sides”. You can just add another coin flip to decide whether to interpret the result as picking between 1,2 and 3 or as picking between 4, 5 and 6.<br></p><p    >The trick is to assign the fourth outcome to a “reset”. If you throw two heads in a row, you just start again. Theoretically you could be coin flipping forever, but the probability of resetting more than five times is already less than one in one-thousand.<br></p><p    >With these kind of resets, it turns out that you can model any probability distribution you like. This will allow you to play your monopoly game.<br></p><p    >The downside is that you have to assign one outcome to multiple leaves in your tree. What if we restrict ourselves to trees where each leaf has a distinct outcome? In that case, we can't model the six-sided die perfectly with coin flips. What distributions can we still model?</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-107">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-107" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0109.svg" class="slide-image" />

            <figcaption>
            <p    >Here are two distributions on the natural numbers that we can model this way. One with an exponentially decaying tail, and one with a fatter tail. <br></p><p    >Note that both trees are infinite in size. This we don't mind. The only constraint we care about is that each leaf node has a unique label.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-108">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-108" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0110.svg" class="slide-image" />

            <figcaption>
            <p    >In probability distributions expressed like this, it's really simple to see the relation between probabilities and codes. We simply replace the <span class="orange red">heads</span> and <span class="green">tails</span> by <span class="orange red">zeros</span> and <span class="green">ones </span>and describe each outcome by the sequence of steps required to get from the root of the tree to that particular outcome.<br></p><p    ><strong><br></strong></p><p    ><strong></strong></p>
            </figcaption>
       </section>


       <section id="slide-108" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-109" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0111anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0111anim0.svg,31.ProbabilisticModels1.key-stage-0111anim1.svg" class="slide-image" />

            <figcaption>
            <p    >These kinds of trees are called<strong> prefix-free trees</strong>, and the resulting codes <strong>prefix -ree codes</strong>. The name comes from the fact that no codeword will be the prefix of any other code word. That is, the first k bits of one code will never be a codeword by themselves.<br></p><p    >The nice thing about prefix free codes is that if we want to encode a sequence of these outcomes, we can just stick the codes one after another and we won’t need any delimiters. A decoder that has access to the tree will know exactly where each codeword ends and the next begins.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-109" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-110" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0112anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0112anim0.svg,31.ProbabilisticModels1.key-stage-0112anim1.svg" class="slide-image" />

            <figcaption>
            <p    >Another nice property is that there is a direct relation between the length of the code we assign an outcome, and its probability: <strong>the more coinflips we require to get to a particular outcome, the lower the probability that we will get there, and the longer the code. </strong>In this tree here, if we generate outcomes by flipping coins randomly, the probability of getting a is the probability of flipping heads twice in a row: 1/4. The probability of getting b is the probability of flippinf head, tails, head: 1/8. <br></p><p    >This is expressed in the code lengths of a and b. b has a longer codelength and is therefore less likely.<br></p><p    >If the probabilities from this tree match the probabilities with which we expect to see the outcomes, then this is a very nice property for a code to have: when frequent outcomes have short codes, we end up with shorter messages overall.<br></p><p    >This was realized as early as the invention of Morse code. Samuel Morse explicitly assigned short codewords to letters like e and t, because he knew that they would occur frequently, so that the telegraph messages would be shorter.<br></p><aside    >Information theory didn't exist yet, so his codelengths were a little ad-hoc. He also didn't know about prefix-free codes, so Morse code does have a delimited code.<strong><br></strong></aside><p    ><strong><br></strong></p><p    ><strong></strong></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-110" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-111" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0113anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0113anim0.svg,31.ProbabilisticModels1.key-stage-0113anim1.svg,31.ProbabilisticModels1.key-stage-0113anim2.svg,31.ProbabilisticModels1.key-stage-0113anim3.svg" class="slide-image" />

            <figcaption>
            <p    >Let's make all this a little more precise. Let's start with an arbitrary tree, and assume that we sample from it by flipping a coin to decide our path from the root to the leaves. What probability distribution does this define? This is very simple: each coinflip multiplies the probability by 1/2, so if the length of the code for outcome <span class="green">b</span> is 3, then the outcome <span class="green">b</span> has probability (1/2)<sup>3</sup> = 1/8.<br></p><p    >In general the probability for an outcome x with a code of length L(x) is p(x) = 2<sup>-L(x)</sup>.<br></p><p    >With this equation in place, we can reverse the question. If we are given a probability distribution p(x), and we are assured that there is some prefix tree corresponding to it, what can we say about the codelengths that this probability tree describes? Rewriting the equation we have to isolate L(x), we get L(x) = -log<sub>2</sub>p(x)<br></p><p    >There it is! The negative logarithm of a probability. If we have a probability distribution that can be expressed by a prefix-free tree, the negative logarithm of its probabilities has a very concrete meaning: <strong>it's the codelengths of the outcomes under the corresponding codes</strong>.<br></p><aside    >The base 2 of the logarithm is a consequence of using bits to encode our data. If we used trits (0, 1, 2) we'd get a base-3 logarithm and if we used digits, we'd get a base-10 logarithm. You can even go the other way around and start with the natural logarithm, which will give you a unit for amount of information called "nats". These are a little more abstract; I can't imagine what a codeword written in nats looks like, but it still works to quantify the amount of information in the outcome of a sample from a probability distribution.<br></aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-112">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-112" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0114.svg" class="slide-image" />

            <figcaption>
            <p    >The only drawback with this view is that we are restricted to probability distributions that we can model as prefix-free codes with unique labels on the leaves. If we investigate closer, it turns out that this is not as much of a restriction as we may fear. We can show that for any probability distribution L we can find a prefix-free code so that the value -log p(x) and the code-length L(x) differ by no more than one bit for any outcome x.<br></p><p    >If we handwave this small difference, we can<strong> equate codes with probability distributions</strong>: every code gives us a distribution and every distribution gives us a code. And all of these codes have the nice property that the higher the probability of an outcome is, the shorter its codelength.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-112" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-113" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0115anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0115anim0.svg,31.ProbabilisticModels1.key-stage-0115anim1.svg,31.ProbabilisticModels1.key-stage-0115anim2.svg" class="slide-image" />

            <figcaption>
            <p    >We already noted that this is a nice property for a code to have, because it reduces the amount of bits we can expect to use. How much does it reduce it? If we know the things we are going to encode come from distribution x, then can we say something about whether using the corresponding code is in some sense the optimal choice?<br></p><p    >The simplest way to answer this question is to compute the expected number of bits we will have to use per outcome. This is simply the codelength of each outcome, multiplied by its probability, summed over all outcomes. This quantity is called the <strong>entropy</strong>. <br></p><p    >The entropy of a distribution is the expected codelength of an element sampled from that distribution.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-113" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-114" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0116anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0116anim0.svg,31.ProbabilisticModels1.key-stage-0116anim1.svg,31.ProbabilisticModels1.key-stage-0116anim2.svg" class="slide-image" />

            <figcaption>
            <p    >The entropy of a distribution is a very commonly used function, because it expresses in a single number how much uncertainty we have over the outcome. Or in other words, how uniformly spread out the probability mass is among the outcomes.<br></p><p    >The more uniform our distribution is, we less we know about what will happen, and the higher the entropy. <br></p><p    >On the left we see<span class="orange red"> a perfectly uniform distribution</span>. Each outcome has equal probability 1/4, so each outcome gets a 2-bit codewords, and the expected codelength is 2.<br></p><p    >In <span class="blue">the middle</span>, we know something more about our distribution, for instance that <span>a</span> is very likely, so we can make the codeword for "a" a little shorter, reducing the expected codelength to 1.75 bits. <br></p><p    >On the right, we see the extreme case of<span class="green"> perfect knowledge</span>. We are certain that outcome "a" will happen every time. We can label the root of our tree with "a". This is like having a single "empty" codeword. More practically if I had to sample an outcome from this distribution and send you a message saying what had happened, the best option would be no message at all: we both know the distribution, so I don't need to tell you what happened.<br></p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-114" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-115" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0117anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0117anim0.svg,31.ProbabilisticModels1.key-stage-0117anim1.svg" class="slide-image" />

            <figcaption>
            <p    >What if we don’t use the code that corresponds to the source of our data <span class="orange red">p</span> to encode our data, but some other code based on distribution <span class="blue">q</span>. What is our expected codelength then? This is called the<em> </em><strong>cross entropy</strong>.<br></p><p    >It can be shown that the cross entropy is minimal when <span class="orange red">p</span>=<span class="blue">q</span>. That is, when the cross entropy corresponds to the entropy.<br></p><p    >We can conclude two things:<br></p><p     class="list-item">The code corresponding to<span class="orange red"> p</span> provides the best expected codelength out of all possible prefix-free codes.<br></p><p     class="list-item">The cross entropy is a good way to <strong>quantify the distance between two distributions</strong> (because it’s minimal when the two are the same).<br></p><aside    >The proof that the cross entropy is always bigger than the entropy. If you're up for a challenge, wait until we've discussed Lagrange mulitpliers, and then apply them to the problem of minimizing the cross entropy for vector <strong class="blue">q</strong>, subject to the constraints that the elements of <strong class="blue">q</strong> are positive and sum to 1.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-116">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-116" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0118.svg" class="slide-image" />

            <figcaption>
            <p    >The cross-entropy is a nice measure, but it’s not zero when <span class="orange red">p</span> and <span class="blue">q</span> are equal. Instead, it’s equal to the entropy of <span class="orange red">p</span>.<br></p><p    >To get a measure that is zero when the two are equal, we can just subtract the the entropy of <span class="orange red">p</span>. This is called the Kullback-Leibler (KL) divergence. The KL divergence between two distributions is zero if and only if they are equal.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-117">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-117" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0119.svg" class="slide-image" />

            <figcaption>
            <p    >For probability distributions on continuous spaces, we can also define entropy and KL divergence. We lose the interpretation of prefix-free codes, and there are some technical hurdles here, but the long and short of it is that we replace the summation by an integration.<br></p><p    >To avoid this complexity, in the rest of the course we will often write the entropy and the KL divergence using the expectation notation. This automatically implies that we are summing for discrete sample spaces and integrating for continuous ones, and if we know the basic properties of the expectation (see homework 1), then we'll never need to open the expectation operator up anyway.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-117" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-118" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0120anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0120anim0.svg,31.ProbabilisticModels1.key-stage-0120anim1.svg,31.ProbabilisticModels1.key-stage-0120anim2.svg" class="slide-image" />

            <figcaption>
            <p    >Now that we have our interpretation of -log(x) as a codelength, let's see what it says about the places where we've used it. <br></p><p    >On such place was the log loss. One interpretation we now have is that if we minmize -q<sub>x</sub>(<span class="blue">P</span>) in logistic regression, we are minimizing the amount of bits we would need to transmit to say that x is of the postive class, if we assume that both the sender and receiver have access to the classifier and x, but not to the class label (more about this in a bit).<br></p><p    >Another interpretation comes from the fact that we characterized the cross entropy loss as the distance between two probability distributions. What if we see the labels in the dataset as one probability distribution p (with all probabilities 0 or 1), and the classifier as another distribution q? What happens if we explicitly try to minimize the cross entropy between p and q by changing the parameters of q?<br></p><p    >As you can see, with a little rewriting, we recover the logarithmic loss we already derived. For this reason log-loss is also known as cross-entropy loss. This is not just a mathematical curiosity. There may be cases, where the data provides class probabilities rather than explicit class labels. In such cases, the cross entropy view tells us exactly what to do, but the log-loss perspective becomes useless.<br></p><aside    >We can also do this with the KL divergence instead of the cross-entropy. In that case, we get a constant term - log p(x), which is independent of the parameters of q. This usually doesn't affect the gradient, but in some cases it does.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-119">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-119" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0121.svg" class="slide-image" />

            <figcaption>
            <p    >Just a little heads up: entropy is an important subject. It may feel a little abstract now, and it's fine if you don't quite get it, but we will see it in use a number of times throughout the course. <br></p><p    >We will practice it in the homework exercises, so you'll get another chance to get comfortable with it.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-120">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-120" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0122.svg" class="slide-image" />

            <figcaption>
            <p    >We'll finish up with a brief look at the field that aims to apply this coding perspective to problems of learning more rigorously. The set of method based on the principle of <strong>Minimum Description Length</strong>.<br></p><p    >The idea is very simple: compression is similar to learning. We look at some data and try to isolate recurring patterns in the data. Using the ideas of coding and entropy, we can make this idea rigorous.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-121">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-121" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0123.svg" class="slide-image" />

            <figcaption>
            <p    >The simplest way to think of MDL is in a <strong>sender and receiver framework</strong>. The sender is going to see some data, and is going to send it to the receiver. Before observing the data, the sender and receiver are allowed to come up with any scheme they like. But afterwards, the data must be sent using the scheme, and in a way that is perfectly decodable by the receiver without further communication. <br></p><p    >One way this is often done, called <strong>two-part coding</strong>, is that the sender and receiver agree on a family of models. Then, once the sender has seen the data, she picks a model, sends it to the receiver, and then used the model to encode the data. The receiver unpacks the model and then uses the model to decode the data.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-121" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-122" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0124anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0124anim0.svg,31.ProbabilisticModels1.key-stage-0124anim1.svg,31.ProbabilisticModels1.key-stage-0124anim2.svg,31.ProbabilisticModels1.key-stage-0124anim3.svg,31.ProbabilisticModels1.key-stage-0124anim4.svg" class="slide-image" />

            <figcaption>
            <p    >This principle is often used to solve the problem of over and under fitting. Without going into the technical details, here is the basic principle of two-part coding applied to a regression problem. <br></p><p    >In a regression (or classification) problems, we take the instances and their features as fixed: both the sender and receiver have access to them. The data that we want to send over the wire is the <em>target labels</em>; in this case the regression targets. How you encode a continuous value is a technical matter that requires some assumptions. For now we can just discretize the range of outputs, and assume that we are using a code that means that <strong>bigger numbers cost more bits</strong>. The same goes for the parameters of the model: these are also continuous values, but we’ll discretize them somehow. Here we only need to assume that using <strong>more parameters in your model takes more bits</strong>.<br></p><p    >Once we’ve chosen a model we can reconstruct the data by sending the <span class="blue">model parameters</span> and the <span class="green">residual values</span>. We see that if we pick a linear model we have many large residuals to transmit. On the other hand, our model is described by only two parameters, so we can transmit that part very cheaply. If we make our model a parabola, we require three numbers to transmit it, so that part of  our message gets bigger, but because the model fits so much better, the residuals are much smaller, and the overal length of our message gets much smaller.<br></p><p    >If we make our model a 15-th order polynomial, we get a slightly tighter fit, but not by much, and the price we pay in storing the 16 numbers required to describe our model means that our message length is bigger than for the parabola. So overall we prefer the model in  the middle, according to the minimum description length principle. </p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-122" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-123" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0125anim0.svg" data-images="31.ProbabilisticModels1.key-stage-0125anim0.svg,31.ProbabilisticModels1.key-stage-0125anim1.svg,31.ProbabilisticModels1.key-stage-0125anim2.svg,31.ProbabilisticModels1.key-stage-0125anim3.svg,31.ProbabilisticModels1.key-stage-0125anim4.svg,31.ProbabilisticModels1.key-stage-0125anim5.svg" class="slide-image" />

            <figcaption>
            <p    >There are many correspondences between using MDL and using Bayesian methods. In fact they are often perspectives on the same thing.<br></p><p    >Here is one example. Let's say we are picking a single model <span class="orange red">M</span> that maximizes the posterior probability  of the data (this requires us to maximize only the numerator of Bayes rule, since the denominator is constant).<br></p><aside    >A full Bayesian analysis would compute the entire posterior distribution, but sometimes we are only interested in its maximum.<br></aside><p    >As we've seen before, we can stick a logarithm in front of any probability without changing the maximum, and we can add a minus to change the maximum into a minimum.<br></p><p    >Then, using the basic properties of the logarithm, we find that we are minimizing the sum of two code-lengths: the cost of describing the model, and the cost of describing the data once the model is know. This is exactly what we do in two-part coding.</p><p    ></p>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>



       <section id="slide-124">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-124" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0126.svg" class="slide-image" />

            <figcaption>
            <p    >When we talked about the problem of induction and the no free lunch theorem, we noted that <em>some assumption</em> about the source of our data was necessary to make learning possible at all. Some aspects of our problem we need to assume before we start learning.<br></p><p    >You can think of MDL as encoding a simplicity assumption. We prefer simple solutions over complex ones, <strong>and we define a simple solution as one that compresses the data well</strong>. The assumption we make about the universe, is that it generates compressible data for us. Or, more precisely, that the compressible aspects of the data that we see are likely to carry over to the test set, and that the incompressible aspects of the data are likely random noise.</p><p    ></p>
            </figcaption>
       </section>


       <section id="slide-125">
            <a class="slide-link" href="https://mlvu.github.io/lecture04#slide-125" title="Link to this slide.">link here</a>
            <img src="31.ProbabilisticModels1.key-stage-0127.svg" class="slide-image" />

            <figcaption>
            <p    >source: <a href="https://xkcd.com/1236/"><strong class="blue">https://xkcd.com/1236/</strong></a></p><p    ><a href="https://xkcd.com/1236/"><strong class="blue"></strong></a></p>
            </figcaption>
       </section>

</article>
