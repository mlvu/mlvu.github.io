---
title: "Lecture 10: Transformers"
slides: true
---
<nav class="menu">
    <ul>
        <li class="home"><a href="/">Home</a></li>
        <li class="name">Lecture 10: Transformers</li>
        <li class="pdf"><a href="https://mlvu.github.io/lectures/Transformers.annotated.pdf">PDF</a></li>
    </ul>
</nav>

<article class="slides">



       <section id="slide-001" class="anim">
            <a class="slide-link" href="https://mlvu.github.io/transformers#slide-001" title="Link to this slide.">link here</a>
            <img src="Transformers.key-stage-0005anim0.svg" data-images="Transformers.key-stage-0005anim0.svg,Transformers.key-stage-0005anim1.svg,Transformers.key-stage-0005anim2.svg" class="slide-image" />

            <figcaption>
            <p    >As we said before, self-attention is a <em>sequence-to-sequence layer</em>. That means it’s job is to consume <span class="blue">a sequence of vectors</span>, and to spit out <span>another sequence of vectors</span>. <br></p><p    >At heart, the operation that does this is very simple. Every <span>output</span> is simply a <em>weighted sum</em> over the <span class="blue">inputs</span>. We multiply each input by a<span> weight</span> and then sum them all up. So, when we’re computing output <strong>y</strong><sub>3</sub>, we have a weight <span>w</span><sub>3i</sub> for every input <strong class="blue">x</strong><sub>i</sub>. We then multiply each<span class="blue"> input vector </span>by its<span> weight</span> and sum all these products together. The result is <strong>y</strong><sub>3</sub>. In order to keep the magnitude of the of the output stable, we ensure that he weights are positive and that they sum to 1.<br></p><p    >This is not unlike the feedforward network we’ve seen already (except the inputs are now vectors instead of numbers). However, the fundamental trick of self-attention, is that the weights in this sum are<strong> not parameters</strong>. They are <em>derived</em> from the inputs.<br></p><aside    >Note that this means that the input and output dimensions of a self-attention layer are always the same. If we want to transform to a different dimension, we’ll need to add a projection layer.</aside><aside    ></aside>
            </figcaption>
            <span class="hint">click image for animation</span>
       </section>


</article>
