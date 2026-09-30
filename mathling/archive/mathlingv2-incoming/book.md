---
title: "The Geometry of Grammar"
subtitle: "A Mathematical Journey Through Language — From Logic to Manifolds"
author: "SHUK<u>AI</u> HSIEH"
affiliation: "Graduate Institute of Linguistics,
National Taiwan University"
date: "Draft — February 2026"
---

<!-- ═══════════════════════════════════════════════════════
     HOW TO 
     ═══════════════════════════════════════════════════════
     
     1. Edit this Markdown file (book.md)
     2. Run:  bash build.sh > index.html
     3. Open: index.html
     4. Deploy: bash deploy.sh ..  (loperntu.github.io/mathling/)
     

     
     CONVENTIONS:
     - # = Part dividers (rendered as nav group labels, not in body)
     - ## = Chapter titles (each becomes a nav entry + chapter block)
     - ### = Section titles within chapters
     - LaTeX math: $inline$ and $$display$$
     - {.epigraph} after a blockquote = styled epigraph
     - {.example}

after a blockquote = centered example sentence
     - {.deep-dive}

or {.deep-dive: Title}

after a blockquote = deep-dive box (multi‑para OK)
     - {.math-block} or {.def-block} after a div = special box
     - affiliation: use a new line in the quoted value, or \\n or <br>, for line breaks
     - Lines starting with <!-- part: ...  = sidebar group labels
     ═══════════════════════════════════════════════════════ -->


# Preface {.unnumbered}

> "The book of nature is written in the language of mathematics."
> — Galileo Galilei
{.epigraph}

This book tells a story that has been unfolding for over a century: the story of how mathematics has shaped our understanding of human language, and how language, in turn, has inspired new branches of mathematics. It is written for linguists who sense that mathematical tools are increasingly indispensable to their field but who may feel daunted by the sheer variety of mathematical frameworks now in play. It is also written for mathematicians and computer scientists who are curious about why natural language — that most human of phenomena — keeps generating such rich mathematical problems.

The narrative arc of this book traces a remarkable intellectual migration. For most of the twentieth century, the mathematics of language was fundamentally discrete: sets, relations, logical formulas, trees, and automata. Language was carved into categories, parsed into hierarchical structures, and analyzed through the lens of formal logic. This discrete paradigm produced extraordinary achievements — generative grammar, formal semantics, computational complexity theory of parsing — and it remains deeply relevant today.

But beginning in the 1990s and accelerating dramatically in the 2010s, a new mathematical vocabulary began to pervade linguistics and natural language processing: vectors, matrices, tensors, probability distributions, and ultimately manifolds, curvature, and topology. The rise of distributional semantics, word embeddings, and finally large language models has not merely added new tools to the linguist's kit; it has fundamentally altered what it means to "represent" a linguistic object. A word is no longer just a node in a tree or an entry in a lexicon — it is a point in a high-dimensional space, and the relationships between words are geometric relationships: distances, angles, projections, and curved paths.

This book aims to make this entire trajectory visible and comprehensible. Each mathematical framework is introduced not in the abstract but through the linguistic phenomena that motivated it. Every definition is accompanied by a linguistic example. Every theorem is contextualized by the question it helps answer about language. The goal is not to produce mathematicians, but to produce linguists who can read the primary literature across all eras of mathematical linguistics with genuine comprehension.

A special emphasis of this book is on the geometric turn: the ways in which the internal representations of modern language models exhibit geometric structure — manifolds, fiber bundles, curvature — that connects to deep questions in both mathematics and cognitive science. This is the frontier, and it is where linguistics, mathematics, and philosophy converge most provocatively.

The book can be read linearly as a historical narrative, or individual chapters can be consulted as self-contained introductions to particular mathematical frameworks. Throughout, I have tried to honor the spirit captured by Leibniz: *Calculemus* — let us calculate. But I have also tried to honor the complementary insight that language is not merely a formal object but a living, embodied, social phenomenon whose mathematical shadows, however beautiful, are always partial.


### 1.5 How to Read the Mathematics in This Book

Every formula in this book is an answer to a question someone asked about language. A useful habit is to read each one in three passes. First, the **picture**: what shape, space, or process is being described? Second, the **sentence**: say the formula aloud in plain words ("the probability of the next word, given the words so far"). Only third, the **symbols**: check how each piece of notation encodes a piece of that sentence.

> Think of a formula as a tightly compressed paragraph. You would not read a dense paragraph of a philosophy paper by staring at individual letters; you look for its subject, its verb, and its claim. A formula has the same parts: the thing being defined (left of the $=$), the operation (the verbs: sum, apply, compose), and the constraint (what must hold). If you can paraphrase it, you understand it.
{.intuition}

For this reason, each chapter introduces a concept first — often through an analogy or a diagram — and only then gives the formal statement. Analogies are scaffolding, not proofs: each one is chosen to be *right about the thing that matters*, and where an analogy breaks down, the text says so. Boxes marked **Intuition** give the picture; boxes marked **Deep dive** give optional technical detail that can be skipped on first reading.

<!-- part: Part I · Discrete Foundations -->

# Chapter 1. Why Mathematics for Linguists? {#ch1}

> Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied.
> — Noam Chomsky
{.epigraph}

### 1.1 The Unreasonable Effectiveness of Mathematics in Linguistics

Let's start with what **the Linguist's Problem** is: *Language Is Too Structured to Be Described, Too Variable to Be Memorized*.

Linguistics has been a field that lives between two temptations. The first is to treat language as an inventory of facts — lists of words, constructions, and exceptions. The second is to treat language as pure abstraction—rules, grammars, and logical systems. Neither temptation is sufficient. Language is both discrete and adaptive: it has hard constraints (ungrammaticality exists) and soft gradients (usage shifts, meanings drift, norms evolve).

In 1960, the physicist Eugene Wigner published a celebrated essay on "The Unreasonable Effectiveness of Mathematics in the Natural Sciences." He marveled at the fact that mathematical structures, developed for their own internal beauty, repeatedly turned out to describe the physical world with uncanny precision. Linguistics presents a parallel puzzle. Why should the same mathematical structures that describe symmetry groups in physics or topological spaces in pure mathematics also illuminate the structure of human language?

One answer is that language, like the physical world, exhibits structure at multiple scales — phonological patterns, morphological regularities, syntactic hierarchies, semantic compositionality, discourse coherence — and mathematics is, at its core, the science of structure. But the deeper answer may be that language occupies a unique position at the intersection of the biological, the cognitive, and the social. 

It is a finite system that generates infinite variety, a discrete symbolic system that encodes continuous meaning, a local process (one word after another) that creates global coherence. These tensions — finite vs. infinite, discrete vs. continuous, local vs. global — are precisely the tensions that different branches of mathematics have been developed to address.

Mathematics enters precisely when we ask questions that force us to be explicit about (i) what counts as an object of analysis, (ii) what counts as sameness, and (iii) what operations we allow. Those three choices—objects, equivalences, operations—quietly determine what kinds of explanations become possible.

- **Objects.** What are we studying? Strings, trees, feature bundles, meanings, discourse moves, or learned representations?

- **Equivalences.** When are two objects “the same for our purpose”?
  A phonologist may treat two phones as “the same phoneme.” A semanticist may treat two expressions as “the same meaning” (by mutual entailment). A discourse analyst may treat two utterances as “the same move” (same update effect). Each choice creates a partition of the messy world into equivalence classes. This is not bookkeeping; it is theory.

- **Operations.** How do objects combine and transform?
  `concatenation, merge, feature unification, function application, update, inference`, and — crucially in the modern era— `smooth transformations` in representation space.

This triad is the reason mathematics keeps returning: once you commit to objects/equivalences/operations, you are already in the land of structures.


> Consider the English form bank. 
It can denote a financial institution or the side of a river. If we treat “word meaning” as a single object per wordform, bank becomes a problem. If we treat meaning as a distribution over context-conditioned senses, bank becomes a structured object (a family of points, or a mixture, or a graph of usages).
This book will repeatedly return to bank, not because it is special, but because it forces us to choose what “a meaning” is.
{.example: A running example we will revisit: bank}



### 1.2 A Map of the Territory







The mathematical frameworks that have been applied to language can be organized along several axes. One axis runs from the **discrete** to the **continuous**. On the discrete end we find set theory, logic, formal language theory, and graph theory; on the continuous end we find calculus, differential geometry, and topology. Another axis runs from the **algebraic** to the **geometric**: algebra emphasizes operations and transformations, while geometry emphasizes spaces and distances. A third axis runs from the **deterministic** to the **probabilistic**. The history of mathematical linguistics can be read as a gradual movement along all three axes — from discrete-algebraic-deterministic toward continuous-geometric-probabilistic — though each earlier framework retains its relevance.

This movement is not merely a matter of fashion. It reflects genuine discoveries about the nature of language. The discrete frameworks captured the combinatorial and compositional aspects of language with extraordinary precision. But they struggled with gradience, ambiguity, context-dependence, and the sheer messiness of language in use. The probabilistic and geometric frameworks address these challenges more naturally, at the cost of a different kind of precision.


### 1.3 The Linguistic Motivation: What Are We Trying to Represent?

Before diving into mathematics, it is worth pausing to ask: what aspects of language do we want our mathematical representations to capture? Consider a seemingly simple English sentence:

> *The bank by the river collapsed after the flood.*
{.example}

Even this unremarkable sentence involves a cascade of linguistic phenomena, each of which has been the target of mathematical modeling. At the **phonological** level, the sentence is a sequence of sound segments organized into syllables, feet, and intonational phrases — a structure that can be modeled with autosegmental representations and metrical grids. At the **morphological** level, words like "collapsed" exhibit internal structure (collapse + -ed) amenable to finite-state analysis. At the **syntactic** level, the sentence has a hierarchical phrase structure that determines the scope of modifiers ("by the river" modifies "bank," not "collapsed"). At the **semantic** level, "bank" is ambiguous between a financial institution and a riverbank, and the phrase "by the river" helps disambiguate. At the **pragmatic** level, the temporal adverbial "after the flood" presupposes that a flood occurred. Each level of analysis invites different mathematical tools.

### 1.4 The Plan of This Book

**Part I** (Chapters 2–5) covers the classical discrete foundations: set theory and relations, formal logic, formal language theory and automata, and graph theory. **Part II** (Chapters 6–8) introduces the probabilistic and algebraic turn: probability and information theory, and the linear algebra that underlies modern computational approaches. **Part III** (Chapters 9–12) is devoted to the geometric turn: vector space semantics, the geometry of neural language models, topological methods, and differential geometry on linguistic manifolds. **Part IV** (Chapters 13–14) ventures into complexity and reflection. Chapter 13 treats language as a *Complex Adaptive System*, drawing on dynamical systems theory, agent-based models, network topology, and the quantum complexity result $\text{MIP}^* = \text{RE}$ to show that language is not a static structure but a self-organizing, emergent, and irreducibly complex phenomenon. Chapter 14 steps back to offer a philosophical reflection on what the entire succession of mathematical framings reveals about the nature of language itself.

Each chapter follows a common pattern: we begin with the linguistic problem that motivates the mathematical framework, introduce the necessary mathematical concepts with linguistic examples, show how the framework has been applied, and conclude with its limitations and the questions that led to the next framework.


# Chapter 2. Sets, Relations, and the Architecture of Language {#ch2}

> A set is a Many that allows itself to be thought of as a One.
> — Georg Cantor
{.epigraph}

### 2.1 The Language of Sets

The most fundamental mathematical framework applied to language is set theory. When Ferdinand de Saussure distinguished between *langue* (the abstract language system) and *parole* (actual speech), he was implicitly invoking set-theoretic thinking: *langue* is a set of signs, each defined as a pairing of a signifier and a signified. When a phonologist defines the vowel inventory of a language, they are specifying a set. When a morphologist lists the inflectional paradigm of a verb, they are constructing a function from a set of feature bundles to a set of forms.

Formally, a set is simply a collection of distinct objects, called elements or members. We write $a \in A$ to mean that $a$ is an element of set $A$. The power of set theory lies not in this simple definition but in the operations and relations we can define on sets: union ($\cup$), intersection ($\cap$), complement, Cartesian product ($\times$), and the critical notion of a function as a special kind of relation.

> A set is like a bouncer with a guest list. The bouncer does not care about the order in which guests arrive, or how many times a name is written on the list; the only question it can answer is "Are you in, or not?" That austerity is the point. By refusing to encode order, repetition, or internal structure, a set lets us isolate the one thing we want to talk about: *membership*. Everything richer — sequences, trees, functions — is built later by adding structure on top.
{.intuition}

The Cartesian product $A \times B$ deserves a picture of its own: it is the grid of *every possible pairing*, like a menu that lists every combination of one starter from column $A$ with one main from column $B$. Most of linguistics lives inside such grids. A lexicon pairs forms with meanings; a paradigm pairs feature bundles with word forms; a grammar rule pairs a category with its possible expansions. The interesting claims are always about *which* cells of the grid are actually used.

### 2.2 Phonological Feature Systems as Set Theory

One of the earliest and most elegant applications of set theory in linguistics is the distinctive feature theory of Jakobson, Fant, and Halle (1952), later refined by Chomsky and Halle (1968) in *The Sound Pattern of English*. In this framework, each phoneme is characterized by a set of binary features. For example, the English consonant /p/ can be described as:

$$\text{/p/} = \{[{+}\text{consonantal}],\; [{-}\text{sonorant}],\; [{-}\text{continuant}],\; [{-}\text{voiced}],\; [{+}\text{labial}]\}$$

The natural classes of phonology — the groups of sounds that behave alike in phonological rules — correspond to the intersections of feature sets. The class of voiceless stops $\{p, t, k\}$ is simply the intersection of sounds that are $[{-}\text{voiced}]$ and $[{-}\text{continuant}]$.

<figure class="fig">
<svg viewBox="0 0 520 250" width="520" role="img" aria-label="Natural class as intersection of feature sets">
<ellipse cx="200" cy="125" rx="150" ry="100" fill="#B08968" fill-opacity="0.12" stroke="#B08968" stroke-width="1.5"/>
<ellipse cx="320" cy="125" rx="150" ry="100" fill="#7A9CC6" fill-opacity="0.12" stroke="#7A9CC6" stroke-width="1.5"/>
<text x="110" y="42" font-size="14" fill="#6B4C3B" font-weight="600">[−voiced]</text>
<text x="350" y="42" font-size="14" fill="#4A6E9A" font-weight="600">[−continuant]</text>
<text x="105" y="120" font-size="16" fill="#2C2825">f  s  ʃ</text><text x="118" y="146" font-size="16" fill="#2C2825">θ  h</text>
<text x="372" y="120" font-size="16" fill="#2C2825">b  d  g</text><text x="385" y="146" font-size="16" fill="#2C2825">m  n</text>
<text x="222" y="132" font-size="20" fill="#2C2825" font-weight="600">p  t  k</text>
<text x="260" y="240" font-size="12" fill="#6B635A" text-anchor="middle">voiceless stops = [−voiced] ∩ [−continuant]</text>
</svg>
<figcaption><b>Figure 2.1.</b> A natural class is an intersection. Each feature value picks out a set of segments; the voiceless stops are exactly the segments that fall inside both circles. A grouping such as {p, s, g} cannot be carved out by intersecting feature sets — and indeed it rarely patterns together in phonological rules.</figcaption>
</figure>

This set-theoretic perspective has profound consequences. It predicts that not all arbitrary groupings of phonemes should function as natural classes in phonological rules; only those groupings that can be defined by the intersection of feature specifications should do so. This prediction is largely confirmed by cross-linguistic data, which constitutes evidence that the feature system reflects something real about the cognitive representation of speech sounds.

### 2.3 Relations: From Paradigms to Hierarchies

A relation $R$ on a set $A$ is a subset of the Cartesian product $A \times A$. Different types of relations — reflexive, symmetric, transitive, antisymmetric — model different kinds of linguistic structure. Equivalence relations (reflexive, symmetric, transitive) partition a set into equivalence classes, which is exactly what paradigmatic relations do in morphology: the set of all noun forms in Latin can be partitioned into declension classes, where each class groups nouns that follow the same inflectional pattern.

It helps to see the properties side by side, each tested against a familiar linguistic relation:

<table class="tbl">
<tr><th>Property</th><th>Plain-language test</th><th>Linguistic relation that has it</th><th>…and one that fails it</th></tr>
<tr><td>Reflexive</td><td>Everything relates to itself</td><td>"is in the same declension class as"</td><td>"precedes" (no word precedes itself)</td></tr>
<tr><td>Symmetric</td><td>If $a$ relates to $b$, then $b$ relates to $a$</td><td>"rhymes with"</td><td>"is a hyponym of"</td></tr>
<tr><td>Transitive</td><td>Relations chain: $a \to b \to c$ gives $a \to c$</td><td>"dominates" in a tree</td><td>"is a near-synonym of" (chains drift: <em>big → large → generous</em>)</td></tr>
<tr><td>Antisymmetric</td><td>Mutual relation only between identicals</td><td>"is a hyponym of or identical to"</td><td>"co-occurs with"</td></tr>
</table>

The failure of transitivity for near-synonymy is worth pausing on. It is an early warning that meaning is *graded* and *local*: similarity holds between neighbours but does not propagate indefinitely. We will meet the same phenomenon again as a geometric fact in Chapters 7 and 9, where "near" in meaning space is a matter of distance, and distances do not simply add up along chains.

Partial orders (reflexive, antisymmetric, transitive) model hierarchical structures. The hyponymy (is-a) relation in lexical semantics forms a partial order: "dog" is a hyponym of "animal," which is a hyponym of "living thing." This gives rise to a lattice structure that has been formalized in frameworks like WordNet (Miller, 1995). The feature geometry of phonology, in which features are organized into a hierarchical tree, is another linguistic instantiation of a partial order.

### 2.4 Functions and Compositionality

A function $f: A \to B$ assigns to each element of set $A$ exactly one element of set $B$. Functions are central to formal semantics, where the meaning of a complex expression is a function of the meanings of its parts. In Montague's framework, which we will explore in detail in Chapter 3, the meaning of a verb phrase like "runs quickly" is computed by applying the function denoted by the adverb "quickly" to the function denoted by "runs." The entire enterprise of compositional semantics rests on the mathematical notion of function composition.

> A function is a vending machine. Press a button (an input) and exactly one item drops out (the output). Two different buttons may deliver the same snack — that is allowed. What is never allowed is one button delivering two different snacks at random. This "exactly one output" condition is what makes composition reliable: if every step is a vending machine, a chain of steps is also a vending machine.
{.intuition}

The picture immediately illuminates a morphological phenomenon. An inflectional paradigm is a function from feature bundles to forms, for instance $f(\langle \text{1sg}, \text{pres} \rangle) = \textit{amō}$ for Latin *amāre* "to love". **Syncretism** — when distinct cells share a form, as English *put* serves as present, past, and participle — is simply the observation that this function is *not injective*: several buttons deliver the same snack. Conversely, **overabundance** (*dreamed* / *dreamt*) is a place where the paradigm fails to be a function at all, and a linguist must decide whether to enrich the output (a set of forms) or split the input (register, dialect).

The concept of a function also underlies the structuralist notion of paradigmatic substitution. Two expressions belong to the same syntactic category if they can substitute for each other in the same contexts — that is, if they have the same domain and range when viewed as functions from left contexts to right contexts. This insight, formalized by Zellig Harris and later by the categorial grammarians, connects set-theoretic function spaces directly to syntactic categories.

### 2.5 Limitations and the Road Ahead

Set theory provides a powerful vocabulary for describing the static architecture of language — its inventories, categories, and relations. But it says relatively little about the dynamic processes that operate over these structures: how sounds change in context, how sentences are generated, how meanings are computed. For this, we need the more expressive frameworks of logic and algebra, to which we turn in the next chapters. Nevertheless, set theory remains the lingua franca of all subsequent formalisms; every mathematical framework we encounter will be built on its foundations.


# Chapter 3. Logic and the Formal Semantics of Natural Language {#ch3}

> The limits of my language mean the limits of my world.
> — Ludwig Wittgenstein
{.epigraph}

### 3.1 From Aristotle to Montague: Logic as the Language of Meaning

The application of logic to natural language has a pedigree stretching back to Aristotle's syllogistic. But the modern era begins with Gottlob Frege's *Begriffsschrift* (1879), which introduced predicate logic — a formal language powerful enough to express quantificational statements like "Every linguist admires some mathematician." Frege's insight was that natural language sentences have an internal logical structure that is obscured by their surface form. The sentence "Every linguist admires some mathematician" is ambiguous between two readings:

$$\forall x\bigl[\mathrm{Linguist}(x) \to \exists y[\mathrm{Mathematician}(y) \wedge \mathrm{Admires}(x,y)]\bigr]$$

$$\exists y\bigl[\mathrm{Mathematician}(y) \wedge \forall x[\mathrm{Linguist}(x) \to \mathrm{Admires}(x,y)]\bigr]$$

These differ in the relative scope of the universal and existential quantifiers — a distinction that has profound semantic consequences but is invisible in the surface syntax.

<figure class="fig">
<svg viewBox="0 0 560 220" width="560" role="img" aria-label="Two scope readings">
<text x="140" y="22" font-size="13" fill="#6B4C3B" font-weight="600" text-anchor="middle">∀ > ∃ (surface scope)</text>
<text x="420" y="22" font-size="13" fill="#6B4C3B" font-weight="600" text-anchor="middle">∃ > ∀ (inverse scope)</text>
<circle cx="80" cy="70" r="6" fill="#B08968"/><text x="66" y="74" font-size="12" fill="#2C2825" text-anchor="end">L1</text><circle cx="80" cy="120" r="6" fill="#B08968"/><text x="66" y="124" font-size="12" fill="#2C2825" text-anchor="end">L2</text><circle cx="80" cy="170" r="6" fill="#B08968"/><text x="66" y="174" font-size="12" fill="#2C2825" text-anchor="end">L3</text><circle cx="200" cy="70" r="6" fill="#7A9CC6"/><text x="214" y="74" font-size="12" fill="#2C2825" text-anchor="start">M1</text><circle cx="200" cy="120" r="6" fill="#7A9CC6"/><text x="214" y="124" font-size="12" fill="#2C2825" text-anchor="start">M2</text><circle cx="200" cy="170" r="6" fill="#7A9CC6"/><text x="214" y="174" font-size="12" fill="#2C2825" text-anchor="start">M3</text>
<g stroke="#6B4C3B" stroke-width="1.4" fill="none"><line x1="86" y1="70" x2="192" y2="120"/><line x1="86" y1="120" x2="192" y2="170"/><line x1="86" y1="170" x2="192" y2="70"/></g>
<circle cx="360" cy="70" r="6" fill="#B08968"/><text x="346" y="74" font-size="12" fill="#2C2825" text-anchor="end">L1</text><circle cx="360" cy="120" r="6" fill="#B08968"/><text x="346" y="124" font-size="12" fill="#2C2825" text-anchor="end">L2</text><circle cx="360" cy="170" r="6" fill="#B08968"/><text x="346" y="174" font-size="12" fill="#2C2825" text-anchor="end">L3</text><circle cx="480" cy="120" r="6" fill="#7A9CC6"/><text x="494" y="124" font-size="12" fill="#2C2825">M</text>
<g stroke="#6B4C3B" stroke-width="1.4" fill="none"><line x1="366" y1="70" x2="473" y2="118"/><line x1="366" y1="120" x2="473" y2="120"/><line x1="366" y1="170" x2="473" y2="122"/></g>
<text x="140" y="208" font-size="12" fill="#6B635A" text-anchor="middle">each linguist picks their own</text>
<text x="420" y="208" font-size="12" fill="#6B635A" text-anchor="middle">one mathematician for everyone</text>
<line x1="280" y1="40" x2="280" y2="190" stroke="#E2DBD1"/>
</svg>
<figcaption><b>Figure 3.1.</b> Scope as "who chooses first". On the left, the universal quantifier chooses first: for each linguist (L), we are then free to pick a possibly different admired mathematician (M). On the right, the existential chooses first: one mathematician is fixed, and every linguist must admire that same person. The right-hand situation entails the left-hand one, but not vice versa.</figcaption>
</figure>

> A useful way to hear the difference: quantifier scope is a game with an order of moves. In $\forall x\,\exists y$, a challenger first names any linguist, and only then do you get to name a mathematician — so your answer may depend on the linguist. In $\exists y\,\forall x$, you must commit to a mathematician *before* seeing any linguist. Moving second is easier; that is why the inverse-scope reading is logically stronger.
{.intuition}

### 3.2 Propositional Logic: The Simplest Fragment

Propositional logic deals with sentences that are either true or false and the connectives that combine them: negation ($\lnot$), conjunction ($\wedge$), disjunction ($\vee$), implication ($\to$), and biconditional ($\leftrightarrow$). In natural language, these correspond (imperfectly) to "not," "and," "or," "if...then," and "if and only if." The imperfection of this correspondence has been one of the great generative puzzles of formal pragmatics. Natural language "or" is typically exclusive in conversational contexts ("You can have coffee or tea"), whereas logical $\vee$ is inclusive. Natural language "if...then" carries presuppositions and conversational implicatures that the material conditional $\to$ does not.

The standard modern resolution is Grice's (1975): the *semantics* of "or" is inclusive, and exclusivity is a *pragmatic* inference. If the speaker had meant "both," the stronger word "and" was available; by choosing the weaker "or," the speaker invites the hearer to infer "not both." This is a **scalar implicature**, and it can be cancelled ("You can have coffee or tea — or both, if you like"), which a truth-conditional entailment cannot. The division of labour between a crisp logical core and a flexible inferential layer is a recurring design pattern in this book.

Despite these mismatches, propositional logic provides the foundation for understanding the truth-conditional core of sentence meaning. The truth table for a compound sentence defines the set of possible worlds in which it is true — a set-theoretic object that connects logic back to the framework of Chapter 2.

### 3.3 Predicate Logic and Natural Language Semantics

First-order predicate logic extends propositional logic with variables, predicates, quantifiers ($\forall$ and $\exists$), and the apparatus of variable binding. This is the mathematical language that Richard Montague used in his landmark papers of the early 1970s to argue that natural language could be treated with the same mathematical rigor as formal languages. Montague's "The Proper Treatment of Quantification in Ordinary English" (1973) demonstrated that a fragment of English could be given a fully compositional model-theoretic semantics using typed lambda calculus and intensional logic.

The key move in Montague grammar is the use of typed functions. Each syntactic category is assigned a semantic type:

$$\begin{aligned}
\text{Proper names} &: e \quad \text{(entities)} \\
\text{Sentences} &: t \quad \text{(truth values)} \\
\text{Intransitive VPs} &: \langle e, t \rangle \quad \text{(functions: entities} \to \text{truth values)} \\
\text{Transitive verbs} &: \langle e, \langle e, t \rangle \rangle
\end{aligned}$$

The meaning of "John walks" is computed by applying the function $\llbracket \text{walks} \rrbracket$ (of type $\langle e, t \rangle$) to the individual $\llbracket \text{John} \rrbracket$ (of type $e$), yielding a truth value. This type-driven composition is one of the most elegant applications of mathematical function theory to language.

> Semantic types behave like the shapes of plugs and sockets. An expression of type $\langle e, t \rangle$ is a socket waiting for an $e$-shaped plug; once plugged, it delivers a $t$. A transitive verb $\langle e, \langle e, t \rangle \rangle$ is a socket that takes one plug and turns into another socket. Composition succeeds only when shapes match — which is why type mismatches are a diagnostic tool: if nothing fits, the semantics must posit a hidden operation (type shifting) or the sentence is uninterpretable.
{.intuition}

### 3.4 Lambda Calculus: The Glue of Compositionality

The lambda calculus, invented by Alonzo Church in the 1930s, provides a notation for defining and applying functions. In formal semantics, it serves as the "glue" that combines word meanings into phrase meanings. The transitive verb "loves" can be represented as $\lambda x.\lambda y.\,\mathrm{Loves}(y, x)$. To compute the meaning of "loves Mary," we perform $\beta$-reduction:

$$(\lambda x.\lambda y.\,\mathrm{Loves}(y, x))(\mathrm{Mary}) = \lambda y.\,\mathrm{Loves}(y, \mathrm{Mary})$$

This resulting expression, a function from individuals to truth values, is the meaning of the verb phrase "loves Mary."

> A lambda term is a form with a blank. $\lambda x.\,\mathrm{Loves}(x, \mathrm{Mary})$ reads: "___ loves Mary." The $\lambda x$ announces which blank is fillable, and $\beta$-reduction is simply the act of writing a name into the blank. Nothing more mysterious is going on; the notation just keeps track of *which* blank is filled when there are several.
{.intuition}

Lambda abstraction also handles more complex phenomena like relative clauses. The relative clause "who loves Mary" denotes the set of individuals who love Mary, represented as $\lambda x.\,\mathrm{Loves}(x, \mathrm{Mary})$. When this combines with a common noun like "man," the result is the intersection of two sets:

$$\lambda x\bigl[\mathrm{Man}(x) \wedge \mathrm{Loves}(x, \mathrm{Mary})\bigr]$$

The mathematical elegance is striking: set intersection, function application, and variable binding conspire to produce the correct meanings for arbitrarily complex constructions.

### 3.5 Modal Logic and Possible Worlds

Natural language is saturated with modality: "must," "might," "can," "should," "necessarily," "possibly." Modal logic extends classical logic with operators $\Box$ (necessarily) and $\Diamond$ (possibly), interpreted over a set of possible worlds connected by an accessibility relation. The sentence "John might be a spy" is true in the actual world if there exists an accessible possible world in which John is a spy.

> Picture a stack of transparent maps, each showing one way the world could be. The accessibility relation tells you which maps you are allowed to consult from where you stand. "Must $p$" ($\Box p$) says that $p$ holds on *every* map you may consult; "might $p$" ($\Diamond p$) says it holds on *at least one*. Different flavours of modality are different rules for which maps are admissible: *epistemic* "must" consults maps compatible with what you know; *deontic* "must" consults maps in which the rules are obeyed. The same logical skeleton, with a different accessibility relation, yields a different modal meaning.
{.intuition}

The possible-worlds framework has been enormously productive in formal semantics. It provides analyses of conditionals ("If kangaroos had no tails, they would topple over" requires evaluating a counterfactual scenario), attitude verbs ("John believes that it is raining" involves John's belief worlds), and tense ("John will arrive" involves quantification over future times). The mathematical structure — a Kripke frame $\langle W, R, V \rangle$ (Kripke, 1963) consisting of a set of worlds $W$, an accessibility relation $R \subseteq W \times W$, and a valuation function $V$ — is another instance of the relational structures introduced in Chapter 2.

### 3.6 Beyond First-Order Logic: Generalized Quantifiers

Natural language quantification goes far beyond "every" and "some." Determiners like "most," "few," "more than half," and "exactly three" cannot be expressed in first-order predicate logic. The theory of generalized quantifiers, developed by Barwise and Cooper (1981), treats determiners as relations between sets:

- **Every:** $\llbracket\text{every}\rrbracket(A)(B) = 1 \iff A \subseteq B$
- **Most:** $\llbracket\text{most}\rrbracket(A)(B) = 1 \iff |A \cap B| > |A \setminus B|$
- **No:** $\llbracket\text{no}\rrbracket(A)(B) = 1 \iff A \cap B = \varnothing$
- **Exactly $n$:** $\llbracket\text{exactly } n\rrbracket(A)(B) = 1 \iff |A \cap B| = n$

The generalized quantifier framework revealed a remarkable cross-linguistic universal: natural language determiners are **conservative**, meaning that $D(A)(B) \Leftrightarrow D(A)(A \cap B)$. This conservativity universal, which holds across all known languages, is a mathematical constraint on the space of possible human languages — one of the most striking examples of mathematics illuminating a linguistic universal.

> Conservativity has a simple intuition: to decide whether "Every student smokes" is true, you only need to look at the students. The non-students — smokers or not — are irrelevant. Formally, $D(A)(B)$ depends only on $A$ and the part of $B$ inside $A$. To appreciate how strong this is, imagine a hypothetical determiner *nall* such that "Nall students smoke" means "everyone who is *not* a student smokes." It is perfectly definable as a relation between sets, yet no human language has such a word (Keenan & Stavi, 1986). The mathematics describes a much larger space of possible meanings than languages actually use — and the universal is a claim about which region they occupy.
{.intuition}

### 3.7 Limitations of Logic-Based Approaches

For all its elegance, the logical approach to semantics faces persistent challenges. Vagueness ("John is tall"), gradience ("This sentence is grammatical"), context-dependence ("enough" for what purpose?), metaphor ("Time flies"), and the open-endedness of word meaning all sit uneasily within the crisp, binary framework of classical logic. These challenges have motivated extensions — fuzzy logic, degree semantics, dynamic semantics, situation semantics — but they have also motivated a fundamentally different mathematical approach: the geometric and probabilistic frameworks of Parts II and III. The tension between the compositional precision of logic and the flexible gradience of actual language use is, arguably, the central tension in the mathematical study of meaning.


# Chapter 4. Formal Languages, Automata, and the Chomsky Hierarchy {#ch4}

> Colorless green ideas sleep furiously.
> — Noam Chomsky
{.epigraph}

### 4.1 The Generative Enterprise

In 1957, Noam Chomsky published *Syntactic Structures*, inaugurating a revolution in linguistics whose mathematical foundations remain central to the field. Chomsky's key insight was that a language can be defined as a set of strings generated by a formal grammar — a finite set of rules that recursively produce an infinite set of well-formed expressions. This perspective connects linguistics directly to the mathematical theory of computation developed by Turing, Post, and Kleene.

A formal grammar $G$ is a tuple $\langle V, \Sigma, R, S \rangle$ where $V$ is a finite set of non-terminal symbols, $\Sigma$ is a finite set of terminal symbols (the alphabet), $R$ is a finite set of production rules, and $S \in V$ is the start symbol. The language $L(G)$ generated by $G$ is the set of all strings of terminal symbols derivable from $S$ by repeated application of rules in $R$.

A tiny grammar makes this concrete. With rules $S \to NP\ VP$, $NP \to \textit{Det}\ N$, $VP \to V$, and lexical rules $\textit{Det} \to \text{the}$, $N \to \text{dog}$, $V \to \text{barks}$, the derivation

$$S \Rightarrow NP\ VP \Rightarrow \textit{Det}\ N\ VP \Rightarrow \text{the}\ N\ VP \Rightarrow \text{the dog}\ VP \Rightarrow \text{the dog barks}$$

rewrites one symbol at a time until only words remain. A grammar is a recipe; a derivation is one particular cooking of it. Recursion enters as soon as a rule can reintroduce its own left-hand side, e.g. $NP \to NP\ PP$: a finite recipe book then describes infinitely many dishes.

### 4.2 The Chomsky Hierarchy

The Chomsky hierarchy classifies formal grammars by the form of their production rules, yielding four types of increasing generative power. Type 3 (regular) grammars, equivalent to finite-state automata, generate languages like $a^n$. Type 2 (context-free) grammars, equivalent to pushdown automata, generate languages like $a^n b^n$ that require matching dependencies. Type 1 (context-sensitive) grammars and Type 0 (unrestricted) grammars are progressively more powerful, with Type 0 equivalent to Turing machines.

<figure class="fig">
<svg viewBox="0 0 560 300" width="560" role="img" aria-label="Chomsky hierarchy">
<rect x="10" y="10" width="540" height="280" rx="18" fill="#F7F3EC" stroke="#9E958A"/>
<rect x="40" y="48" width="480" height="234" rx="16" fill="#F5EDE3" stroke="#B08968"/>
<rect x="70" y="86" width="420" height="188" rx="14" fill="#EDE3D6" stroke="#B08968" stroke-dasharray="5 4"/>
<rect x="100" y="124" width="360" height="142" rx="12" fill="#E6EDF4" stroke="#7A9CC6"/>
<rect x="130" y="172" width="300" height="86" rx="10" fill="#E3EEE8" stroke="#8CB4A0"/>
<text x="24" y="32" font-size="12.5" fill="#2C2825" font-weight="600">Type 0 · recursively enumerable — Turing machine</text>
<text x="54" y="70" font-size="12.5" fill="#2C2825" font-weight="600">Type 1 · context-sensitive — linear-bounded automaton</text>
<text x="84" y="108" font-size="12.5" fill="#6B4C3B" font-weight="600">Mildly context-sensitive — TAG, CCG  (natural-language syntax?)</text>
<text x="114" y="146" font-size="12.5" fill="#2C2825" font-weight="600">Type 2 · context-free — pushdown automaton (stack)</text>
<text x="144" y="194" font-size="12.5" fill="#2C2825" font-weight="600">Type 3 · regular — finite-state automaton</text>
<text x="144" y="214" font-size="11.5" fill="#6B635A">e.g. aⁿ, (ab)*, most phonological rules</text>
<text x="144" y="232" font-size="11.5" fill="#6B635A">memory: a fixed number of states</text>
<text x="114" y="164" font-size="11.5" fill="#6B635A">e.g. aⁿbⁿ, nested embedding</text>
</svg>
<figcaption><b>Figure 4.1.</b> The Chomsky hierarchy as nested classes. Each ring can do everything the inner rings can, plus more — and the "more" is always a matter of memory. The dashed ring marks Joshi's mildly context-sensitive class, the current best guess for where natural-language syntax lives.</figcaption>
</figure>

> The hierarchy is best understood as a ladder of **memory**. A finite-state automaton is like a person who can only remember which room of a house they are standing in: it can follow patterns, but it cannot count without limit. A pushdown automaton adds a stack of plates: it can put a plate down for each opening bracket and take one off for each closing bracket, so it can check $a^n b^n$ — but only in last-in, first-out order. A linear-bounded automaton may reread and rewrite its whole input, and a Turing machine has unbounded scratch paper. Asking "where does language sit?" is asking "how much, and what shape of, memory does grammar require?"
{.intuition}

The burning question in mathematical linguistics has been: where does natural language fall in this hierarchy? Chomsky argued early on that natural languages are not regular — that is, they cannot be generated by finite-state grammars. His famous example involved center-embedding: English allows sentences like "The cat the dog the rat bit chased ran," which requires tracking nested dependencies (cat-ran, dog-chased, rat-bit) that a finite-state device cannot handle.

> How can one *prove* that a language is not regular? The key is the **pumping lemma**, and its idea is the pigeonhole principle. A finite-state machine with $p$ states, reading a string longer than $p$ symbols, must visit some state twice — it has gone round a loop. Whatever it read along that loop can be repeated ("pumped") any number of times, and the machine will not notice. Formally: if $L$ is regular, there is a $p$ such that every $w \in L$ with $|w| \ge p$ splits as $w = xyz$ with $|xy| \le p$, $|y| \ge 1$, and $xy^iz \in L$ for all $i \ge 0$. Pumping the $a$'s in $a^n b^n$ breaks the balance with the $b$'s, so $a^n b^n$ is not regular — and neither is any language with unboundedly deep centre-embedding.
{.deep-dive: Deep dive: the pumping lemma}

### 4.3 Beyond Context-Free: Mildly Context-Sensitive Languages

In 1985, Stuart Shieber (1985) demonstrated that the cross-serial dependencies found in Swiss German — where accusative and dative objects must be matched with their respective verbs in a crossing pattern — cannot be generated by any context-free grammar. This established that natural languages are at least mildly context-sensitive. The term was coined by Aravind Joshi to describe a class of grammars — including Tree-Adjoining Grammars (TAGs), Combinatory Categorial Grammars (CCGs), and Linear Indexed Grammars — that are slightly more powerful than context-free grammars but far less powerful than full context-sensitive grammars.

<figure class="fig">
<svg viewBox="0 0 520 250" width="520" role="img" aria-label="Nested versus cross-serial dependencies">
<text x="10" y="20" font-size="12.5" fill="#6B4C3B" font-weight="600">Nested (English centre-embedding): stack order works</text>
<g transform="translate(20,0)"><text x="40" y="118" font-size="12.5" fill="#2C2825" text-anchor="middle">cat</text><text x="120" y="118" font-size="12.5" fill="#2C2825" text-anchor="middle">dog</text><text x="200" y="118" font-size="12.5" fill="#2C2825" text-anchor="middle">rat</text><text x="280" y="118" font-size="12.5" fill="#2C2825" text-anchor="middle">bit</text><text x="360" y="118" font-size="12.5" fill="#2C2825" text-anchor="middle">chased</text><text x="440" y="118" font-size="12.5" fill="#2C2825" text-anchor="middle">ran</text><path d="M40 100 A200 70 0 0 1 440 100" fill="none" stroke="#B08968" stroke-width="1.6"/><path d="M120 100 A120 70 0 0 1 360 100" fill="none" stroke="#B08968" stroke-width="1.6"/><path d="M200 100 A40 40 0 0 1 280 100" fill="none" stroke="#B08968" stroke-width="1.6"/></g>
<text x="10" y="148" font-size="12.5" fill="#4A6E9A" font-weight="600">Cross-serial (Swiss German): arcs cross — a stack is not enough</text>
<g transform="translate(20,0)"><text x="40" y="244" font-size="12.5" fill="#2C2825" text-anchor="middle">d'chind</text><text x="120" y="244" font-size="12.5" fill="#2C2825" text-anchor="middle">em Hans</text><text x="200" y="244" font-size="12.5" fill="#2C2825" text-anchor="middle">es huus</text><text x="280" y="244" font-size="12.5" fill="#2C2825" text-anchor="middle">lönd</text><text x="360" y="244" font-size="12.5" fill="#2C2825" text-anchor="middle">hälfe</text><text x="440" y="244" font-size="12.5" fill="#2C2825" text-anchor="middle">aastriiche</text><path d="M40 226 A120 70 0 0 1 280 226" fill="none" stroke="#7A9CC6" stroke-width="1.6"/><path d="M120 226 A120 70 0 0 1 360 226" fill="none" stroke="#7A9CC6" stroke-width="1.6"/><path d="M200 226 A120 70 0 0 1 440 226" fill="none" stroke="#7A9CC6" stroke-width="1.6"/></g>
</svg>
<figcaption><b>Figure 4.2.</b> Why the shape of dependencies matters. Nested arcs close in reverse order of opening, which is exactly what a stack provides. In the Swiss German clause "(…that we) let the children help Hans paint the house", each noun phrase is case-matched with its verb in the <em>same</em> order, so the arcs cross. Handling unboundedly many crossings takes more than a single stack.</figcaption>
</figure>

The mildly context-sensitive languages have several attractive properties: they can generate the cross-serial dependencies found in natural language, they have polynomial parsing complexity, and their structural descriptions are trees (or mildly enriched trees). Joshi conjectured that human languages are exactly the class of mildly context-sensitive languages — a mathematical hypothesis about the computational complexity of Universal Grammar.

### 4.4 Finite-State Methods in Phonology and Morphology

While syntax required context-free or mildly context-sensitive power, phonology and morphology turned out to be well-modeled by the weakest class in the hierarchy: regular languages and finite-state transducers. The insight, formalized by Ronald Kaplan and Martin Kay (1994), was that most phonological rules can be compiled into finite-state transducers — devices that read an input string and produce an output string, operating with bounded memory.

In morphology, finite-state methods proved extraordinarily successful. Kimmo Koskenniemi's two-level morphology (1983) modeled the relationship between underlying and surface forms of words as a set of parallel finite-state constraints. This approach could handle the complex morphological phenomena of agglutinative languages like Finnish and Turkish, and it led to the development of practical morphological analyzers for dozens of languages.

### 4.5 Automata as Cognitive Models

The connection between automata and cognition runs deeper than analogy. The finite-state hypothesis in psycholinguistics — that human sentence processing operates with finite memory and is thus fundamentally finite-state in nature — has been both defended and attacked. While the unbounded recursive power of human syntax argues against strict finite-state processing, psycholinguistic evidence shows that deeply center-embedded sentences are effectively unprocessable, suggesting that the human parser operates within a bounded region of the Chomsky hierarchy in practice.

This tension between competence (what the grammar can generate in principle) and performance (what the processor can handle in practice) maps directly onto the mathematical distinction between different levels of the hierarchy. It is a tension that will resurface throughout this book, particularly when we encounter neural network language models that are, in principle, finite-state machines (bounded by their parameter count) but that approximate the behavior of more powerful computational devices.


### 4.6 Limitations and the Road Ahead

The Chomsky hierarchy measures **weak generative capacity**: which *sets of strings* a grammar can produce. Linguists usually care about more — **strong generative capacity**, the *structures* assigned to those strings. Two grammars may generate the same strings while assigning different trees, and only one of them may support the right semantics. This is why the next chapter turns from strings to the structures themselves: trees and graphs. And because the hierarchy is categorical — a string is in the language or it is not — it has nothing to say about the gradient judgments and frequency effects that Part II will take up.

# Chapter 5. Graphs, Trees, and Linguistic Structure {#ch5}

> The branching tree of possibilities is the deepest picture of reality.
> — David Deutsch
{.epigraph}

### 5.1 Trees: The Canonical Representation of Syntax

If there is a single mathematical object that symbolizes modern linguistics, it is the tree. From Chomsky's phrase structure trees to dependency trees, from phonological prosodic trees to semantic type-driven derivation trees, the tree diagram is ubiquitous. Mathematically, a tree is a connected acyclic graph — a set of nodes connected by edges such that there is exactly one path between any two nodes.

<figure class="fig">
<svg viewBox="0 0 500 340" width="500" role="img" aria-label="Constituency tree and dependency tree">
<defs><marker id="ah" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#7A9CC6"/></marker></defs>
<text x="0" y="14" font-size="12" fill="#6B635A">Constituency (phrase-structure) tree</text>
<text x="275" y="34" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">S</text><text x="120" y="68" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">NP</text><text x="430" y="98" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">VP</text><text x="237" y="98" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">PP</text><text x="285" y="128" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">NP</text>
<text x="50" y="160" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">Det</text><text x="120" y="160" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">N</text><text x="190" y="160" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">P</text><text x="250" y="160" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">Det</text><text x="320" y="160" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">N</text><text x="430" y="160" font-size="12" fill="#6B4C3B" text-anchor="middle" font-weight="600">V</text>
<line x1="275" y1="38" x2="120" y2="55" stroke="#B08968" stroke-width="1.2"/><line x1="275" y1="38" x2="430" y2="85" stroke="#B08968" stroke-width="1.2"/><line x1="120" y1="72" x2="50" y2="147" stroke="#B08968" stroke-width="1.2"/><line x1="120" y1="72" x2="120" y2="147" stroke="#B08968" stroke-width="1.2"/><line x1="120" y1="72" x2="237" y2="85" stroke="#B08968" stroke-width="1.2"/><line x1="237" y1="102" x2="190" y2="147" stroke="#B08968" stroke-width="1.2"/><line x1="237" y1="102" x2="285" y2="115" stroke="#B08968" stroke-width="1.2"/><line x1="285" y1="132" x2="250" y2="147" stroke="#B08968" stroke-width="1.2"/><line x1="285" y1="132" x2="320" y2="147" stroke="#B08968" stroke-width="1.2"/><line x1="430" y1="102" x2="430" y2="147" stroke="#B08968" stroke-width="1.2"/>
<text x="50" y="186" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">The</text><text x="120" y="186" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">bank</text><text x="190" y="186" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">by</text><text x="250" y="186" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">the</text><text x="320" y="186" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">river</text><text x="430" y="186" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">collapsed</text>
<line x1="0" y1="206" x2="500" y2="206" stroke="#E2DBD1"/>
<text x="0" y="226" font-size="12" fill="#6B635A">Dependency tree (Universal Dependencies style)</text>
<path d="M430 300 A155 58 0 0 0 120 300" fill="none" stroke="#7A9CC6" stroke-width="1.5" marker-end="url(#ah)"/><text x="275" y="238" font-size="10.5" fill="#4A6E9A" text-anchor="middle">nsubj</text><path d="M120 300 A35 35 0 0 0 50 300" fill="none" stroke="#7A9CC6" stroke-width="1.5" marker-end="url(#ah)"/><text x="85" y="261" font-size="10.5" fill="#4A6E9A" text-anchor="middle">det</text><path d="M120 300 A100 58 0 0 1 320 300" fill="none" stroke="#7A9CC6" stroke-width="1.5" marker-end="url(#ah)"/><text x="220" y="238" font-size="10.5" fill="#4A6E9A" text-anchor="middle">nmod</text><path d="M320 300 A65 58 0 0 0 190 300" fill="none" stroke="#7A9CC6" stroke-width="1.5" marker-end="url(#ah)"/><text x="255" y="238" font-size="10.5" fill="#4A6E9A" text-anchor="middle">case</text><path d="M320 300 A35 35 0 0 0 250 300" fill="none" stroke="#7A9CC6" stroke-width="1.5" marker-end="url(#ah)"/><text x="285" y="261" font-size="10.5" fill="#4A6E9A" text-anchor="middle">det</text>
<line x1="430" y1="236" x2="430" y2="296" stroke="#7A9CC6" stroke-width="1.5" marker-end="url(#ah)"/><text x="436" y="246" font-size="10.5" fill="#4A6E9A">root</text>
<text x="50" y="318" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">The</text><text x="120" y="318" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">bank</text><text x="190" y="318" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">by</text><text x="250" y="318" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">the</text><text x="320" y="318" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">river</text><text x="430" y="318" font-size="13" fill="#2C2825" text-anchor="middle" font-style="italic">collapsed</text>
</svg>
<figcaption><b>Figure 5.1.</b> Two graphs for one sentence. The constituency tree groups words into nested phrases; its internal nodes are categories. The dependency tree has no phrasal nodes at all: every arc links a head to a dependent, and the structure is carried entirely by who depends on whom. Note that "by the river" attaches to <em>bank</em>, not to <em>collapsed</em>, in both pictures.</figcaption>
</figure>

> A syntactic tree works like an organisational chart. Every employee except the director has exactly one immediate boss (one mother node); bosses may have several reports (daughters); and nobody can be their own boss's boss (no cycles). Two useful relations fall out of the chart. **Dominance** — "is somewhere above, in the same chain of command" — is a partial order of exactly the kind met in Chapter 2. **C-command** — a node c-commands its sisters and everything below them — captures who can "see" whom, and it constrains binding: in *John's mother admires himself*, *John* does not c-command *himself*, and the sentence fails.
{.intuition}

### 5.2 Dependency Graphs

An alternative to phrase structure is dependency grammar, whose mathematical formalization uses directed graphs rather than constituent trees. In a dependency tree, each word is a node, and directed edges connect heads to their dependents. Dependency trees and phrase structure trees are mathematically related but not equivalent. Dependency parsing has become dominant in computational linguistics, partly because dependency trees are easier to learn from data and partly because they generalize more naturally across typologically diverse languages.

A simple but useful count follows from the definition: a dependency tree over $n$ words has exactly $n-1$ arcs, because every word except the root has exactly one head. The whole analysis of a sentence can therefore be written as a function $h: \{1,\ldots,n\} \to \{0,1,\ldots,n\}$ assigning each word its head (with $0$ standing for the root) — once again, a function in the sense of §2.4, subject to the constraint that following heads upward never loops.

### 5.3 Graphs Beyond Trees: Semantic and Discourse Structure

While syntax is largely tree-structured, other levels of linguistic analysis require the full generality of graphs. Semantic representations often involve directed acyclic graphs (DAGs) or even cyclic graphs. Abstract Meaning Representation (AMR; Banarescu et al., 2013) uses rooted DAGs to represent the meaning of sentences, allowing reentrancy — the same entity participating in multiple semantic roles.

### 5.4 Graph Properties and Linguistic Universals

The mathematical properties of linguistic graphs encode substantive linguistic claims. The projectivity of dependency trees — the requirement that dependency arcs do not cross when the words are laid out in linear order — corresponds to a constraint on word-order freedom. Graph-theoretic measures like average dependency length have been shown to correlate with processing difficulty. Dependency Length Minimization (Gildea & Jaeger, 2015; Futrell, Mahowald & Gibson, 2015), the tendency for languages to prefer shorter dependencies, has been documented across dozens of languages and appears to be a genuine universal, explicable as an optimization strategy for the human parser.

The measure itself is disarmingly simple. If word $i$ has head $h(i)$, the total dependency length of a sentence is

$$\mathrm{DL} = \sum_{i \ne \text{root}} |\,i - h(i)\,|,$$

the total distance that every dependent must "reach" to its head. Compare two orders of a phrasal verb:

> *John threw out the old trash* (DL = 9) vs. *John threw the old trash out* (DL = 11)
{.example}

In the first order, *out* sits next to *threw* (distance 1) while *trash* is at distance 4; in the second, *trash* comes one step closer (3) but *out* is pushed to distance 4, so the total rises from 9 to 11. As the object grows heavier, the gap widens, and speakers increasingly prefer to put the particle first. What looks like a stylistic preference is, from the graph's point of view, a minimisation of total wire length.

> Imagine each dependency as a piece of string that must be held in working memory until its head arrives. Long strings are costly to hold; many long strings at once are costlier still. Dependency Length Minimisation says that languages — and speakers choosing among word orders — tend to keep the strings short. **Projectivity** is the related requirement that the strings, drawn above the sentence, never cross (compare Figure 4.2).
{.intuition}

### 5.5 From Graphs to Matrices: A Bridge to Part II

Any graph over $n$ nodes can be written down as an $n \times n$ table, its **adjacency matrix** $A$, with $A_{ij} = 1$ if there is an arc from $i$ to $j$ and $0$ otherwise. This seemingly clerical step is a bridge. Once a graph is a matrix, the tools of linear algebra apply: powers of $A$ count paths ($(A^2)_{ij}$ is the number of two-step paths from $i$ to $j$), and eigenvectors of $A$ identify the most central nodes. Replace the 0s and 1s by real-valued weights, let the weights be *learned* rather than annotated, and you have — as Chapter 8 will show — exactly what a Transformer attention head computes. The discrete trees of this chapter and the continuous matrices of Part II are two views of the same object.


<!-- part: Part II · Probabilistic & Algebraic Turn -->

# Chapter 6. Probability, Information, and the Statistics of Language {#ch6}

> Whenever I fire a linguist, the performance of the speech recognizer goes up.
> — Frederick Jelinek (attrib.)
{.epigraph}

### 6.1 The Probabilistic Turn

For much of the twentieth century, the dominant paradigm in theoretical linguistics was categorical: a sentence was either grammatical or ungrammatical. Chomsky famously argued that probabilistic models were inappropriate for natural language, observing that "Colorless green ideas sleep furiously" and "Furiously sleep ideas green colorless" are equally improbable, yet only the first is grammatical. The counter-revolution came from both computational linguistics and sociolinguistics.

Chomsky's example is a good argument against one particular probabilistic model — counting whole sentences — but not against probability as such. A model that assigns probabilities to *structures*, or that smooths over word classes, readily prefers *Colorless green ideas sleep furiously* to its reversal. Meanwhile, three bodies of evidence made probability hard to ignore. Sociolinguists found that variable rules (Labov's *-t/-d* deletion, for instance) apply with stable, conditioned *rates* rather than categorically. Psycholinguists found that reading times track how *predictable* a word is. And acceptability judgments, collected carefully, turn out to be *gradient* rather than binary. Probability is the natural mathematics for all three.

### 6.2 Probability Distributions over Linguistic Objects

A probability distribution over a set $\Omega$ assigns a non-negative real number $P(\omega)$ to each element $\omega \in \Omega$ such that the probabilities sum to 1. In language modeling, $\Omega$ is the set of all possible sentences, and $P$ assigns to each sentence its probability of occurrence. The simplest language model is the $n$-gram model, which approximates the probability of a word given its entire history by conditioning only on the previous $n{-}1$ words:

$$P(w_i \mid w_1, \ldots, w_{i-1}) \approx P(w_i \mid w_{i-n+1}, \ldots, w_{i-1})$$

> Think of a language model as a seasoned bettor at a racetrack where the horses are words. Before each word is revealed, the bettor spreads a fixed budget of chips (total probability 1) across all possible next words. Conditioning on the history narrows the field: after *Please pass the*, most chips go on *salt*, *butter*, and *ball*, and almost none on *democracy*. A good model is one that, over many races, keeps putting a lot of chips on the horse that actually wins.
{.intuition}

The formula above is an approximation of an exact identity. By the **chain rule** of probability, any sentence probability factors into a product of next-word predictions:

$$P(w_1, \ldots, w_n) = \prod_{i=1}^{n} P(w_i \mid w_1, \ldots, w_{i-1}).$$

The $n$-gram model simply truncates the history. A bigram model estimates each factor from counts, $P(w_i \mid w_{i-1}) \approx C(w_{i-1} w_i) / C(w_{i-1})$: if *the* occurs 1,000 times in a corpus and *the bank* 12 times, then $P(\text{bank} \mid \text{the}) \approx 0.012$. Every modern language model, including a Transformer, is still estimating the same factors — it just uses the whole history rather than the last $n-1$ words.

### 6.3 Information Theory and Language

Claude Shannon's information theory (1948) provides a mathematical framework for quantifying the information content of linguistic messages. The entropy of a random variable $X$ is defined as:

$$H(X) = -\sum_{x} P(x) \log_2 P(x)$$

This measures the average surprise associated with outcomes.

The building block is the **surprisal** of a single outcome, $s(x) = -\log_2 P(x)$. The intuition is news value: a headline announcing that the sun rose this morning carries almost no information; one announcing that it did not would carry a great deal. Surprisal turns probabilities into additive "bits of news": a certain event ($P=1$) has surprisal $0$, a fair coin flip has $1$ bit, and an event with probability $1/8$ has $3$ bits — as much news as three coin flips. Entropy is then just surprisal *averaged* over outcomes. A fair coin has $H = 1$ bit; a coin that lands heads 90% of the time has only $H = -(0.9\log_2 0.9 + 0.1\log_2 0.1) \approx 0.47$ bits, because most of its flips are unsurprising.

Surprisal has become one of the most successful bridges between probability and the mind. **Surprisal theory** (Hale, 2001; Levy, 2008) proposes that the processing difficulty of a word is proportional to its surprisal in context, and large-scale reading-time studies confirm a roughly linear relation between reading time and $-\log P(w_i \mid \text{context})$ (Smith & Levy, 2013). Garden-path sentences such as *The horse raced past the barn fell* are, in this view, sentences in which one word — *fell* — carries an enormous, unexpected load of bits.

The entropy of English is approximately 1.0 to 1.5 bits per character — meaning that each character carries about one bit of information, far less than the $\log_2(26) \approx 4.7$ bits that a uniformly random letter would carry. This redundancy provides robustness against noise and facilitates prediction.

#### Cross-entropy, perplexity, and KL divergence

Three further quantities appear throughout the rest of the book. If the true distribution is $P$ but we predict with a model $Q$, the average surprisal we actually experience is the **cross-entropy**

$$H(P, Q) = -\sum_x P(x) \log_2 Q(x) \;\ge\; H(P).$$

Language models are trained precisely to minimise this quantity on text. Its exponential, the **perplexity** $\mathrm{PP} = 2^{H(P,Q)}$, has a vivid reading: it is the *effective number of equally likely choices* the model is torn between at each step. A perplexity of 20 means the model is, on average, as uncertain as if it were choosing uniformly among 20 words. The gap between the two, the **Kullback–Leibler divergence**

$$\mathrm{KL}(P \,\|\, Q) = H(P, Q) - H(P) = \sum_x P(x) \log_2 \frac{P(x)}{Q(x)} \;\ge\; 0,$$

is the number of *extra* bits paid for using the wrong codebook. It is zero only when $Q = P$, and it is not symmetric — being surprised by a rare event you thought impossible is far costlier than the reverse. KL divergence will return in t-SNE (§7.3) and, in its infinitesimal form, as the Fisher metric of §11.5.

Finally, **pointwise mutual information** measures how much more often two words co-occur than chance would predict:

$$\mathrm{PMI}(w, c) = \log_2 \frac{P(w, c)}{P(w)\,P(c)}.$$

*Strong tea* has high PMI; *powerful tea* does not, even though the adjectives are near-synonyms. PMI is the quantity that turns raw co-occurrence counts into the word vectors of Chapter 7.

### 6.4 Bayesian Approaches to Language

Bayes' theorem provides a principled framework for updating beliefs in light of evidence:

$$P(H \mid D) = \frac{P(D \mid H)\,P(H)}{P(D)}$$

Bayesian approaches have been applied to language acquisition, syntactic parsing, pragmatic reasoning (the Rational Speech Acts framework (Frank & Goodman, 2012)), and historical linguistics (Bayesian phylogenetics of language families).

> Bayes' theorem is the arithmetic of a detective. The **prior** $P(H)$ is how plausible a suspect was before the new clue; the **likelihood** $P(D \mid H)$ is how well the clue fits that suspect; and the **posterior** $P(H \mid D)$ is the updated suspicion. The denominator merely rescales so that suspicions across all suspects add up to one.
{.intuition}

Return to *bank*. Suppose that, in general text, the financial sense is more common: $P(\text{fin}) = 0.7$, $P(\text{river}) = 0.3$. Now the word *fishing* appears nearby, with $P(\textit{fishing} \mid \text{fin}) = 0.01$ and $P(\textit{fishing} \mid \text{river}) = 0.2$. Then

$$P(\text{river} \mid \textit{fishing}) = \frac{0.2 \times 0.3}{0.2 \times 0.3 + 0.01 \times 0.7} = \frac{0.06}{0.067} \approx 0.90.$$

A single contextual clue has overturned a 70–30 prior into a 90–10 posterior in the other direction. Word-sense disambiguation, in this light, is evidence accumulation.

### 6.5 Zipf's Law and the Statistics of the Lexicon

One of the most striking statistical regularities of language is Zipf's law (Zipf, 1949): if the words of a language are ranked by frequency, the frequency of the $r$th-ranked word is approximately proportional to $1/r$:

$$f(r) \propto \frac{1}{r^\alpha}, \quad \alpha \approx 1$$

<figure class="fig">
<svg viewBox="0 0 520 280" width="520" role="img" aria-label="Zipf's law on log-log axes">
<line x1="60" y1="230" x2="490" y2="230" stroke="#6B635A"/><line x1="60" y1="20" x2="60" y2="230" stroke="#6B635A"/>
<text x="60" y="248" font-size="11" fill="#6B635A" text-anchor="middle">10⁰</text><text x="165" y="248" font-size="11" fill="#6B635A" text-anchor="middle">10¹</text><text x="270" y="248" font-size="11" fill="#6B635A" text-anchor="middle">10²</text><text x="375" y="248" font-size="11" fill="#6B635A" text-anchor="middle">10³</text><text x="480" y="248" font-size="11" fill="#6B635A" text-anchor="middle">10⁴</text>
<text x="52" y="234" font-size="11" fill="#6B635A" text-anchor="end">10⁰</text><text x="52" y="192" font-size="11" fill="#6B635A" text-anchor="end">10¹</text><text x="52" y="150" font-size="11" fill="#6B635A" text-anchor="end">10²</text><text x="52" y="108" font-size="11" fill="#6B635A" text-anchor="end">10³</text><text x="52" y="66" font-size="11" fill="#6B635A" text-anchor="end">10⁴</text><text x="52" y="24" font-size="11" fill="#6B635A" text-anchor="end">10⁵</text>
<line x1="60" y1="20" x2="480" y2="188" stroke="#B08968" stroke-width="1.2" stroke-dasharray="5 4"/>
<circle cx="60.0" cy="20.0" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="70.5" cy="20.9" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="81.0" cy="29.3" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="91.5" cy="35.7" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="102.0" cy="35.1" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="112.5" cy="38.3" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="123.0" cy="47.6" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="133.5" cy="51.5" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="144.0" cy="50.7" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="154.5" cy="56.5" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="165.0" cy="65.2" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="175.5" cy="66.7" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="186.0" cy="67.0" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="196.5" cy="75.0" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="207.0" cy="82.1" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="217.5" cy="81.8" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="228.0" cy="84.2" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="238.5" cy="93.4" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="249.0" cy="98.0" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="259.5" cy="97.2" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="270.0" cy="102.2" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="280.5" cy="111.3" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="291.0" cy="113.4" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="301.5" cy="113.3" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="312.0" cy="120.7" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="322.5" cy="128.3" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="333.0" cy="128.5" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="343.5" cy="130.2" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="354.0" cy="139.1" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="364.5" cy="144.6" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="375.0" cy="143.7" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="385.5" cy="148.0" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="396.0" cy="157.2" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="406.5" cy="160.1" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="417.0" cy="159.6" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="427.5" cy="166.4" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="438.0" cy="174.6" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="448.5" cy="175.2" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="459.0" cy="176.3" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="469.5" cy="184.9" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/><circle cx="480.0" cy="191.0" r="3.2" fill="#6B4C3B" fill-opacity="0.75"/>
<text x="70" y="26" font-size="11.5" fill="#2C2825">the</text><text x="100" y="46" font-size="11.5" fill="#2C2825">of</text><text x="130" y="60" font-size="11.5" fill="#2C2825">and</text>
<text x="340" y="110" font-size="12" fill="#6B4C3B">slope ≈ −1</text>
<text x="275" y="272" font-size="12" fill="#2C2825" text-anchor="middle">rank r (log scale)</text>
<text x="16" y="125" font-size="12" fill="#2C2825" text-anchor="middle" transform="rotate(-90 16 125)">frequency f (log scale)</text>
</svg>
<figcaption><b>Figure 6.1.</b> On ordinary axes, Zipf's law is a steep curve that hugs both axes. On logarithmic axes it becomes a straight line, because $\log f = \text{const} - \alpha \log r$. The slope is $-\alpha$; for word frequencies it is close to $-1$.</figcaption>
</figure>

This power-law distribution means that a small number of words ("the," "of," "and") account for a large fraction of all word tokens, while the vast majority of word types occur rarely. Zipf's law has been documented across all studied languages and extends to other linguistic units.

> A power law is the signature of a "rich get richer" world. City sizes, citation counts, and word frequencies share it: a few giants, a long tail of the obscure, and no characteristic "typical" size. Why language should look like this remains debated. Zipf himself proposed a **principle of least effort** — speakers would prefer one all-purpose word, hearers would prefer one word per meaning, and the compromise is a power law. Other explanations invoke preferential reuse of already-frequent words (a mechanism we meet again in §13.5), and some point out that even random typing produces Zipf-like curves. What the law does establish beyond doubt is practical: most word *types* are rare, so any model of language must generalise to words it has barely seen.
{.intuition}


# Chapter 7. Linear Algebra: The Vector Space of Language {#ch7}

> You shall know a word by the company it keeps.
> — J.R. Firth
{.epigraph}

### 7.1 The Distributional Hypothesis

The idea that the meaning of a word can be inferred from its patterns of co-occurrence — the distributional hypothesis — was articulated by Harris (1954) and Firth (1957) and has become one of the most productive ideas in computational linguistics. Its mathematical realization requires linear algebra: words become vectors, contexts become dimensions, and meaning becomes geometry.

> "You shall know a word by the company it keeps" can be taken literally. Imagine describing each person at a party only by the list of people they talk to. You would never learn anyone's name or job — yet two people with heavily overlapping lists are probably similar (colleagues, or members of the same family). The distributional hypothesis bets that words are like that: their *social life in text* reveals their meaning.
{.intuition}

A toy co-occurrence table shows the idea. Each row is a word; each column counts how often a context word appeared nearby in some corpus:

<table class="tbl">
<tr><th></th><th>bark</th><th>pet</th><th>feed</th><th>vote</th><th>law</th></tr>
<tr><td>dog</td><td>9</td><td>7</td><td>6</td><td>0</td><td>1</td></tr>
<tr><td>cat</td><td>0</td><td>8</td><td>7</td><td>0</td><td>0</td></tr>
<tr><td>democracy</td><td>0</td><td>0</td><td>0</td><td>9</td><td>7</td></tr>
</table>

Each row is now a list of five numbers — a **vector** — and a word is a point (or an arrow from the origin) in a five-dimensional space. *Dog* and *cat* point in similar directions; *democracy* points somewhere else entirely. Everything that follows in this chapter is a way of making that observation precise, and of scaling it from five columns to hundreds of thousands.

### 7.2 Vectors, Matrices, and the Algebra of Meaning

A vector space $V$ over a field $F$ (typically $\mathbb{R}$) is a set equipped with two operations — vector addition and scalar multiplication — satisfying certain axioms. The key concepts for linguistic applications are:

- **Dot product:** $\langle \mathbf{u}, \mathbf{v} \rangle = \sum_i u_i\, v_i$ — measures alignment
- **Norm:** $\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$ — measures magnitude
- **Cosine similarity:** $\cos(\theta) = \dfrac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\| \cdot \|\mathbf{v}\|}$ — measures angle, independent of magnitude

<figure class="fig">
<svg viewBox="0 0 460 250" width="460" role="img" aria-label="Cosine similarity as angle between word vectors">
<defs><marker id="va6B4C3B" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#6B4C3B"/></marker><marker id="vaB08968" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#B08968"/></marker><marker id="va7A9CC6" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#7A9CC6"/></marker></defs>
<line x1="60" y1="230" x2="440" y2="230" stroke="#E2DBD1"/><line x1="60" y1="20" x2="60" y2="230" stroke="#E2DBD1"/>
<line x1="60" y1="230" x2="338.2" y2="117.6" stroke="#6B4C3B" stroke-width="2.2" marker-end="url(#va6B4C3B)"/><text x="344.2" y="113.6" font-size="13" fill="#6B4C3B" font-weight="600">dog</text><line x1="60" y1="230" x2="187.2" y2="150.5" stroke="#B08968" stroke-width="2.2" marker-end="url(#vaB08968)"/><text x="193.2" y="146.5" font-size="13" fill="#B08968" font-weight="600">cat</text><line x1="60" y1="230" x2="99.5" y2="44.2" stroke="#7A9CC6" stroke-width="2.2" marker-end="url(#va7A9CC6)"/><text x="105.5" y="40.2" font-size="13" fill="#7A9CC6" font-weight="600">democracy</text>
<path d="M124.9 203.8 A70 70 0 0 0 119.4 192.9" fill="none" stroke="#2C2825" stroke-width="1"/>
<text x="138" y="196" font-size="12" fill="#2C2825">small θ</text>
<path d="M102.4 203.5 A50 50 0 0 0 70.4 181.1" fill="none" stroke="#9E958A" stroke-width="1" stroke-dasharray="3 3"/>
<text x="92" y="160" font-size="12" fill="#6B635A">large θ</text>
</svg>
<figcaption><b>Figure 7.1.</b> Cosine similarity measures the angle between arrows, not their length. <em>Dog</em> is drawn longer than <em>cat</em> — as a more frequent word's count vector would be — yet the two are near-parallel and so highly similar. <em>Democracy</em> points in a different direction. Ignoring length is deliberate: frequency inflates length without changing meaning.</figcaption>
</figure>

In the word-vector space, cosine similarity becomes a measure of semantic similarity. The vectors for "dog" and "cat" will have high cosine similarity because they occur in similar contexts, while "dog" and "democracy" will have low cosine similarity. This is remarkable: a purely mathematical operation on co-occurrence counts recovers something that looks very much like human semantic intuition.

### 7.3 Dimensionality Reduction: SVD and the Latent Structure of Meaning

> Imagine summarising a video-streaming service's giant table of users × films. You could describe every film by thousands of individual ratings — or notice that a handful of hidden "dials" explain most of the ratings: how much action, how much romance, how much of a cult following. SVD finds such dials automatically. It says that any matrix can be decomposed into three simple steps — *rotate* into the dial coordinates, *stretch* each dial by its importance, *rotate* back — and that keeping only the few most important dials loses surprisingly little. For a word-context matrix, the dials are latent semantic dimensions: topics, registers, domains.
{.intuition}

Raw word-context matrices are enormous and sparse. Singular Value Decomposition (SVD) provides a principled method for reducing their dimensionality while preserving the most important patterns. Given a matrix $M$ of rank $r$, SVD factorizes it as:

$$M = U \Sigma V^\top$$

where $U$ and $V$ are orthogonal matrices and $\Sigma = \mathrm{diag}(\sigma_1, \ldots, \sigma_r)$ is a diagonal matrix of singular values. By retaining only the $k$ largest singular values ($k \ll r$), we obtain a low-rank approximation $M_k = U_k \Sigma_k V_k^\top$ that captures the dominant latent structure. Latent Semantic Analysis (LSA), introduced by Landauer and Dumais (1997), applied SVD to word-document matrices and demonstrated that the resulting low-dimensional representations captured semantic relationships not present in the original counts.

**t-SNE: Nonlinear visualization for embeddings (intuition and applications).**

SVD is a **linear** method: it compresses a matrix by preserving global variance structure in a low-rank subspace. In practice, we often also want a tool for **exploratory visualization** of high-dimensional representations (word/sentence embeddings, or the token states from a specific Transformer layer). A widely used method is **t-SNE** (t-distributed Stochastic Neighbor Embedding; van der Maaten & Hinton, 2008). Its goal is not to preserve global geometry, but to preserve **local neighborhoods**: points that are close in the original space should remain close in 2D/3D.

t-SNE converts distances into probabilities. For each point $x_i$, it defines conditional neighbor probabilities with a Gaussian kernel:

$$p_{j\mid i} \propto \exp\!\left(-\frac{\|x_i-x_j\|^2}{2\sigma_i^2}\right),\quad p_{i\mid i}=0,$$

and chooses $\sigma_i$ so that the entropy of $\{p_{j\mid i}\}_j$ matches a user-chosen **perplexity** (intuitively, an "effective number of neighbors"; typical values are roughly 5–50). These conditionals are then symmetrized into a joint distribution, e.g.

$$p_{ij}=\frac{p_{j\mid i}+p_{i\mid j}}{2n}.$$

In the low-dimensional map $y_i$, t-SNE uses a heavy-tailed Student-$t$ kernel:

$$q_{ij} \propto \left(1+\|y_i-y_j\|^2\right)^{-1},\quad q_{ii}=0,$$

and minimizes a KL divergence

$$\mathrm{KL}(P\|Q)=\sum_{i\ne j} p_{ij}\log\frac{p_{ij}}{q_{ij}}.$$

The heavy tail helps mitigate the "crowding problem", making it easier for distinct local clusters to separate in 2D.

Typical language-oriented uses include:

- **Embedding sanity checks**: visualize a selected vocabulary to see whether synonyms, topics, or domains form coherent local neighborhoods, and to spot outliers.
- **Polysemy and context clustering**: apply t-SNE to *contextual* embeddings of the same word type to see whether different senses form distinct "islands".
- **Model/layer comparison**: compare neighborhood structure across models or across layers (e.g., whether syntactic distinctions appear more cleanly in some layers).

**A concrete language example (polysemy: "bank").** Take multiple sentences that contain the word *bank* in different senses (financial vs river). Extract the contextual embedding of the *bank* token from a fixed layer of a Transformer, then run t-SNE and inspect whether the two senses separate locally.

```python
from transformers import AutoTokenizer, AutoModel
from sklearn.manifold import TSNE
import numpy as np, torch, matplotlib.pyplot as plt

S = [
  "I deposited cash at the bank.",
  "The bank approved the loan.",
  "We sat on the river bank at dusk.",
  "The boat reached the bank.",
]

tok = AutoTokenizer.from_pretrained("bert-base-uncased")
m = AutoModel.from_pretrained("bert-base-uncased", output_hidden_states=True).eval()
L = 8

@torch.no_grad()
def v(s):
  e = tok(s, return_tensors="pt")
  hs = m(**e).hidden_states[L][0]
  toks = tok.convert_ids_to_tokens(e["input_ids"][0])
  idx = [i for i,t in enumerate(toks) if t == "bank"]
  return hs[idx].mean(0).cpu().numpy()

Y = TSNE(2, perplexity=2, init="pca", random_state=0).fit_transform(np.stack([v(s) for s in S]))
plt.scatter(Y[:,0], Y[:,1]); [plt.text(Y[i,0], Y[i,1], i, fontsize=9) for i in range(len(S))]
plt.title('t-SNE of contextual "bank" embeddings'); plt.tight_layout(); plt.show()
```

A critical caveat: the **relative positions, inter-cluster distances, and cluster sizes** in a t-SNE plot generally do *not* have a reliable global geometric meaning. Results can change with perplexity, learning rate, initialization, and random seed. A common workflow is to first reduce to 30–100 dimensions with PCA/SVD, then run t-SNE, and to repeat with multiple seeds to avoid over-interpreting a single visualization.




### 7.4 Word Embeddings: From Counting to Prediction

Word2Vec (Mikolov et al., 2013) and GloVe (Pennington et al., 2014) learned word vectors by training neural networks to predict context. The resulting embeddings exhibited striking algebraic properties — vector arithmetic encoded semantic relationships:

$$\vec{v}_{\text{king}} - \vec{v}_{\text{man}} + \vec{v}_{\text{woman}} \approx \vec{v}_{\text{queen}}$$

This showed that vector offsets captured relational structure — different directions correspond to different semantic relations (gender, tense, plurality, etc.).

The training objective itself is a fill-in-the-blank game. The *skip-gram* model sees a word and must guess which words appear around it; with **negative sampling**, it learns to tell true neighbours from random impostors. Each successful guess nudges the vectors of words that share neighbours closer together. It therefore came as a satisfying unification when Levy and Goldberg (2014) proved that skip-gram with negative sampling is implicitly **factorising a matrix** — the PMI matrix of §6.3, shifted by a constant. "Counting" (Chapter 6 and §7.3) and "predicting" (neural embeddings) turn out to be two routes to nearly the same geometry.

> The parallelogram picture of *king − man + woman ≈ queen* is memorable but fragile. In the standard evaluation, the input words themselves are excluded from the answer set; without this exclusion, the nearest vector to *king − man + woman* is usually *king* itself (Linzen, 2016). Many "analogies" also succeed simply because the target is a close neighbour of one input. The safer conclusion is modest: *some* relations are encoded as roughly consistent directions, and this is exactly the "local linear factor" idea that Chapter 9 tests more carefully.
{.deep-dive: A caution about analogies}

### 7.5 Tensor Products and Compositional Distributional Semantics

The Categorical Compositional Distributional (DisCoCat) framework of Coecke, Sadrzadeh, and Clark (2010) addresses compositionality by representing relational words as tensors. A transitive verb like "loves" is represented as a rank-3 tensor $\mathcal{T} \in V \otimes V \otimes V$. The meaning of "John loves Mary" is computed by tensor contraction:

$$\llbracket\text{John loves Mary}\rrbracket_k = \sum_{i,j} \mathcal{T}_{ijk} \cdot \vec{v}_{\text{John},\,i} \cdot \vec{v}_{\text{Mary},\,j}$$

> Think of a transitive verb as a machine with two input slots and one output chute. A noun, being a single vector, is a list of numbers. The verb must say, for *every* combination of subject-feature $i$ and object-feature $j$, how much each output feature $k$ is activated — a three-dimensional table of numbers, $\mathcal{T}_{ijk}$. Feeding in *John* and *Mary* and summing over $i$ and $j$ is exactly the contraction above. The price is size: with $d$-dimensional nouns, a verb needs $d^3$ numbers, which is why practical systems compress or factorise these tensors.
{.intuition}

This approach elegantly combines the compositional structure of formal semantics with the distributional content of vector space models.

### 7.6 Linear Algebra in Syntax: Spectral Methods

A concrete example of this bridge is **spectral learning**. A hidden Markov model or a latent-variable PCFG is a discrete, symbolic device, and fitting one to data traditionally requires iterative search (the EM algorithm), which can get stuck. Hsu, Kakade, and Zhang (2012) and Cohen et al. (2012) showed that the parameters can instead be recovered, up to a change of basis, from the singular value decomposition of matrices of observable co-occurrence statistics — for instance, how often word triples occur in sequence. The hidden grammar leaves a low-rank fingerprint on the statistics; SVD reads it off.

Linear algebra serves as a bridge between the discrete, symbolic representations of classical linguistics and the continuous, distributed representations of modern computational linguistics. A discrete grammar generates trees; these trees give rise to distributional statistics; these statistics live in a vector space; and the structure of that vector space reflects the structure of the underlying grammar. Linear algebra is the mathematical framework that makes this connection precise.


# Chapter 8. Neural Networks and the Mathematics of Learned Representations {#ch8}

> What I cannot create, I do not understand.
> — Richard Feynman
{.epigraph}

### 8.1 From Perceptrons to Transformers

The neural network revolution in linguistics can be told as a mathematical story of progressive enrichment. Each architecture can be described precisely in linear-algebraic terms.

The basic unit is modest. An artificial **neuron** takes a weighted vote over its inputs and passes the result through a nonlinearity: $y = \sigma(\mathbf{w}^\top \mathbf{x} + b)$. A **layer** is many neurons at once, $\mathbf{y} = \sigma(W\mathbf{x} + \mathbf{b})$ — a matrix multiplication (Chapter 7) followed by a bend. Without the bend, stacking layers would be pointless, since a product of matrices is just another matrix; the nonlinearity is what lets depth build genuinely new features.

> Training a network is like walking downhill in thick fog. You cannot see the valley; you can only feel the slope under your feet. The **loss** is your altitude — for a language model, the cross-entropy of §6.3, i.e. how surprised the model is by the real next word. The **gradient** is the local slope, computed for every one of millions of parameters at once by *backpropagation* (the chain rule of calculus, applied systematically). **Gradient descent** takes a small step downhill, re-measures, and repeats. Nothing in this procedure knows any linguistics; whatever grammar the network ends up encoding, it has found because grammar lowers the altitude.
{.intuition}

The architecture that now dominates is the Transformer (Vaswani et al., 2017), and its signature component is **attention**.

> Attention works like a library search. Each word writes a **query** ("what am I looking for?"), and every word also carries a **key** (the label on its spine) and a **value** (its contents). A word compares its query with every key; the better the match, the more of that word's value it borrows. For the token *bank* in *The bank by the river collapsed*, a query that asks "is there anything about water or money nearby?" will match the key of *river* strongly, and the representation of *bank* will absorb some of *river*'s value — nudging it towards the riverbank sense.
{.intuition}

A single Transformer attention head computes:

$$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

where $Q = XW^Q$, $K = XW^K$, $V = XW^V$ are linear projections of the input $X$, and $d_k$ is the dimensionality of the key vectors. The entire Transformer is a composition of attention layers interspersed with position-wise feed-forward networks, layer normalization, and residual connections.

Each piece of the formula now has a plain reading. $QK^\top$ is a table of match scores between every query and every key. The **softmax** turns each row of scores into shares of attention that are positive and sum to 1 — it is a "soft" version of picking the maximum, where higher scores get exponentially larger shares. Dividing by $\sqrt{d_k}$ keeps the scores from growing with dimension, which would make the softmax so spiky that each word attends to only one other. Multiplying by $V$ finally mixes the values according to those shares. Since attention by itself ignores order, Transformers add a **positional encoding** to each token vector, so that "the dog bit the man" and "the man bit the dog" do not look identical.

### 8.2 The Geometry of the Residual Stream

A key insight from mechanistic interpretability research is that the Transformer can be understood as performing successive geometric transformations on a high-dimensional vector representing each token. The residual stream — the sequence of vectors that flows through the network — can be thought of as a trajectory through a high-dimensional space.

> Think of the residual stream as a shared whiteboard attached to each token. Every layer reads what is currently on the board, computes something, and *adds* its note without erasing anything: $\mathbf{x}_{\ell+1} = \mathbf{x}_\ell + f_\ell(\mathbf{x}_\ell)$. Because contributions are added, later layers can read off earlier notes directly, and researchers can ask which layer wrote which "direction" onto the board (Elhage et al., 2021). The final board is then read by an output layer that turns it into a probability distribution over the next word.
{.intuition}

Different layers perform different kinds of operations: early layers encode local syntactic relationships, middle layers encode more global syntactic and semantic relationships, and late layers encode distributional information needed for prediction.

### 8.3 Attention as Soft Graph Construction

The attention mechanism has a beautiful interpretation in terms of graph theory. Each attention head defines a weighted directed graph over the tokens, where the edge weight from token $i$ to token $j$ is the attention weight $\alpha_{ij}$. Different heads learn to construct different graphs: some attend to the syntactically adjacent word, others to the head of the current phrase, others to the subject of the sentence. Transformers are, among other things, soft structure-learning machines.

<figure class="fig">
<svg viewBox="0 0 470 170" width="470" role="img" aria-label="Attention weights as a weighted graph">
<text x="40" y="150" font-size="13" fill="#2C2825" font-weight="400" text-anchor="middle" font-style="italic">The</text><text x="110" y="150" font-size="13" fill="#6B4C3B" font-weight="700" text-anchor="middle" font-style="italic">bank</text><text x="180" y="150" font-size="13" fill="#2C2825" font-weight="400" text-anchor="middle" font-style="italic">by</text><text x="245" y="150" font-size="13" fill="#2C2825" font-weight="400" text-anchor="middle" font-style="italic">the</text><text x="320" y="150" font-size="13" fill="#2C2825" font-weight="400" text-anchor="middle" font-style="italic">river</text><text x="420" y="150" font-size="13" fill="#2C2825" font-weight="400" text-anchor="middle" font-style="italic">collapsed</text>
<path d="M110 132 A0 0 0 0 0 110 132" fill="none" stroke="#7A9CC6" stroke-opacity="0.45" stroke-width="2.3"/><text x="110" y="126" font-size="11" fill="#4A6E9A" text-anchor="middle">0.15</text><path d="M110 132 A105 80 0 0 1 320 132" fill="none" stroke="#7A9CC6" stroke-opacity="0.85" stroke-width="6.0"/><text x="215" y="46" font-size="11" fill="#4A6E9A" text-anchor="middle">0.55</text><path d="M110 132 A35 35 0 0 0 40 132" fill="none" stroke="#7A9CC6" stroke-opacity="0.50" stroke-width="2.8"/><text x="75" y="91" font-size="11" fill="#4A6E9A" text-anchor="middle">0.20</text><path d="M110 132 A35 35 0 0 1 180 132" fill="none" stroke="#7A9CC6" stroke-opacity="0.40" stroke-width="1.9"/><text x="145" y="91" font-size="11" fill="#4A6E9A" text-anchor="middle">0.10</text>
<text x="235" y="20" font-size="12" fill="#6B635A" text-anchor="middle">attention from “bank” (one head; weights sum to 1)</text>
</svg>
<figcaption><b>Figure 8.1.</b> One row of an attention matrix drawn as a graph. Arc thickness is the attention weight from <em>bank</em> to each other token (self-attention and small weights omitted). Compare Figure 5.1: an annotated dependency tree is a graph with weights of exactly 0 or 1; an attention head is a graph whose weights are real numbers, learned from data, and recomputed for every sentence.</figcaption>
</figure>

### 8.4 Superposition and the Geometry of Features

Networks represent more features than they have dimensions, by encoding features as nearly orthogonal directions in a space that is too small to accommodate them all as exactly orthogonal dimensions. This phenomenon has deep connections to compressed sensing and the Johnson-Lindenstrauss lemma (Johnson & Lindenstrauss, 1984). The mathematics of superposition suggests that neural networks exploit the geometry of high-dimensional spaces — in particular, the fact that high-dimensional spaces admit exponentially many nearly orthogonal directions — to pack a vast amount of linguistic knowledge into a finite-dimensional representation.

> Superposition resembles fitting more radio stations into a band than there are clean frequencies, by tolerating a little crosstalk. It works because most features are **sparse**: any given sentence mentions only a few of the thousands of things a network can represent, so rarely-co-active features can share nearly-overlapping directions without garbling each other. The Johnson–Lindenstrauss lemma quantifies the room available: $n$ points can be placed in only $k = O(\log n / \varepsilon^2)$ dimensions while distorting all pairwise distances by at most a factor of $1 \pm \varepsilon$. The number of "almost perpendicular" directions grows exponentially with dimension (Elhage et al., 2022).
{.intuition}

### 8.5 Probing: Finding Trees Inside Vectors

If neural networks learn linguistic structure, where is it? A **probe** is a small, deliberately simple model trained to read a linguistic property off the hidden vectors. If even a *linear* probe succeeds, the property is written in the geometry in an easily accessible form.

The most striking example is the **structural probe** of Hewitt and Manning (2019). They looked for a single linear map $B$ such that, for every pair of words $i, j$ in a sentence, the squared distance between their transformed vectors approximates their distance in the dependency tree:

$$\|B(\mathbf{h}_i - \mathbf{h}_j)\|^2 \approx d_T(i, j),$$

where $d_T(i,j)$ is the number of arcs on the path between $i$ and $j$ in a tree like the lower one in Figure 5.1. Such a $B$ exists, and it works across sentences: in a suitable linear subspace of BERT's representations, the dependency tree is present *as a geometry*. Chapters 2–5 described syntax with discrete objects; this result shows those objects reappearing, approximately, as distances. It is a natural doorway into Part III.

> Probing results need care: a sufficiently powerful probe can "find" almost anything by learning the task itself. Good practice compares against control tasks and random baselines, and prefers the simplest probe that works — the goal is to discover what is *easily readable* from the representation, not what can be computed from it with enough effort.
{.deep-dive: A caution about probes}


<!-- part: Part III · The Geometric Turn -->

# Chapter 9. The Geometry of Meaning: Manifolds in Semantic Space {#ch9}

> Mathematics is the art of correct reasoning from incorrectly drawn figures.
> — Henri Poincaré
{.epigraph}

### 9.1 Why “Flat” Semantic Space Is Not Enough: From Vector Spaces to Manifolds

The vector-space semantic models of Chapter 7 begin with a convenient idealization: meanings live in a Euclidean space where distances are measured with a single global ruler. This is a powerful starting point, but language gives us reasons to doubt that assumption. Polysemy, hierarchy, and compositional interaction all suggest that “semantic distance per unit move” depends on where you are in meaning space. In other words, the geometry of meaning is plausibly curved.

Consider the hierarchical structure of concepts: "animal" encompasses "mammal," which encompasses "dog," which encompasses "poodle." This tree-like structure cannot be faithfully embedded in Euclidean space without distortion, but it can be naturally embedded in hyperbolic space, where the volume of a ball grows exponentially with its radius — just as the number of nodes in a tree grows exponentially with depth.

A **manifold** is a space that is locally Euclidean but globally may be curved or twisted. The Earth is the canonical example: locally flat enough to build roads, globally curved enough to make flat maps distort.

> Picture a sheet of paper crumpled into a ball and floating in a room. The room is three-dimensional, but an ant living on the paper experiences only two dimensions: forward–back and left–right. Two points on the paper may be close *through the air* yet far apart *along the paper*. High-dimensional representations are believed to behave similarly: vectors live in a space of, say, 768 dimensions, but the linguistically meaningful states occupy a much thinner, crumpled surface inside it. The number of directions the ant can move in is the **intrinsic dimension**; the size of the room is the **ambient dimension**.
{.intuition}

The **manifold hypothesis** in representation learning proposes that linguistic data — words in contexts, constructions, discourse moves — occupies a structured subset $\mathcal{M}$ of an ambient high-dimensional space. For linguists, the key reinterpretation is:

- The ambient space is the representational space (embedding space, hidden-state space).
- The manifold $\mathcal{M}$ is the set of “plausible linguistic states” shaped by grammar, meaning, and usage.
- “Ungrammatical” or “infelicitous” objects are naturally modeled as off-manifold.

This does not replace symbolic grammar. It provides a complementary view: grammar as constraints that carve out a region of representational space.

#### Local linearity and linguistic minimal pairs

Manifolds are locally linear — zoom in far enough on the crumpled paper and it looks flat. That matters because linguistic analysis thrives on minimal pairs.

If a linguistic factor behaves smoothly (style, politeness, gradual semantic drift), then small controlled edits should produce locally consistent representation shifts. If a factor behaves categorically (idioms, scope flips), we expect discontinuities — large representational changes triggered by small surface cues.

**Worked example: a “politeness direction” test.** Take a set of content-controlled pairs:

- $s$: “Open the window.”
- $E(s)$: “Could you please open the window?”

Let $v(\cdot)$ be a sentence embedding and define the edit vector $\Delta_E(s)=v(E(s))-v(s)$. Test whether $\Delta_E(s)$ is approximately parallel across many base sentences $s$ (for instance, by the average cosine between edit vectors).

- If yes: politeness behaves like a stable local factor — a **tangent direction** that can be followed from many starting points.
- If no: politeness is highly interaction-dependent (curved or entangled with content).

This is differential-geometry thinking before we introduce formal differential geometry.

#### Curvature as an interaction signature

In linguistics, interactions are the rule, not the exception: negation interacts with quantifiers; aspect interacts with telicity; honorifics interact with social roles.

Geometrically, a clean diagnostic is additivity. Compare the effect of two edits $E_1$ and $E_2$. If

$$\Delta_{E_1\circ E_2}(s)\approx \Delta_{E_1}(s)+\Delta_{E_2}(s),$$

then effects are locally additive — the space behaves as if flat around $s$. Systematic failure suggests curvature-like interaction: order and context matter.

> On a flat floor, walking 3 m north then 4 m east lands you at the same spot as walking 4 m east then 3 m north. On a curved surface such as a sphere, the two routes end at slightly different places, and the discrepancy grows with the size of the loop. That order-dependence *is* curvature. When "make it polite" followed by "negate it" lands somewhere different from "negate it" followed by "make it polite", the representation space is telling us that the two factors interact.
{.intuition}

### 9.2 Hyperbolic Geometry and Lexical Hierarchies

> Hyperbolic space is a space that keeps making more room the farther out you go. Frilly lettuce leaves and crocheted coral models are physical approximations: their edges ruffle because there is more edge than a flat disc can hold. A family tree has the same problem — each generation doubles — and in a flat plane the leaves quickly run out of space and crowd together. In hyperbolic space the circumference of a circle grows like $2\pi \sinh r \approx \pi e^{r}$ rather than $2\pi r$, so there is always room for the next generation.
{.intuition}

Nickel and Kiela (2017) demonstrated that embedding the WordNet hierarchy in hyperbolic space produced far better representations than Euclidean embeddings of the same dimensionality. In just two hyperbolic dimensions, they could embed a hierarchy that required hundreds of Euclidean dimensions. The mathematical reason is elegant: a tree with branching factor $b$ has $O(b^n)$ nodes at depth $n$. The volume of a hyperbolic ball of radius $r$ also grows exponentially:

$$\mathrm{Vol}_{\mathbb{H}^d}(r) \propto e^{(d-1)\,r}$$

so there is a natural correspondence between tree depth and hyperbolic distance. In contrast, Euclidean volume grows only polynomially ($\propto r^d$), creating a mismatch with tree structure.

### 9.3 Poincaré Embeddings and Lexical Entailment

The Poincaré disk model maps the entire infinite hyperbolic plane onto the interior of a unit circle. The key insight is that distance in this model is not uniform: moving a fixed Euclidean distance near the boundary corresponds to a much larger hyperbolic distance than the same Euclidean step near the centre. Formally, the distance between two points $\mathbf{u}, \mathbf{v}$ in the Poincaré ball is:

$$d(\mathbf{u}, \mathbf{v}) = \mathrm{arcosh}\!\left(1 + \frac{2\,\|\mathbf{u} - \mathbf{v}\|^2}{(1 - \|\mathbf{u}\|^2)(1 - \|\mathbf{v}\|^2)}\right)$$

Notice the denominator: as either point approaches the boundary ($\|\mathbf{u}\| \to 1$), the factor $(1 - \|\mathbf{u}\|^2) \to 0$, which sends the distance to infinity. This is exactly what makes the Poincaré disk a natural home for hierarchies. The root of a taxonomy sits near the origin; each successive level of specialization pushes nodes outward, and the exponentially growing "room" near the boundary accommodates the exponentially branching leaves.

For lexical entailment, this geometric property has a clean semantic interpretation: if concept $A$ entails concept $B$ (i.e., $A$ is more specific), then $A$ should be embedded farther from the origin than $B$, and the geodesic from $A$ to $B$ should point inward. Nickel and Kiela (2017) showed that a simple constraint — $\|\mathbf{v}_{\text{hypernym}}\| < \|\mathbf{v}_{\text{hyponym}}\|$ — captures the is-a relation with high accuracy in just 2 dimensions.

The interactive simulation below lets you experience this directly. Drag any word toward the boundary and watch the hyperbolic distances explode — even though the Euclidean displacement is small. Click two nodes to compare their distances. Toggle the geodesic view to see the curved shortest path.

<div class="interactive-widget" id="poincare-widget">
<style>
.pw-container {
  background: linear-gradient(145deg, #1a1814 0%, #2a2520 100%);
  border-radius: 12px;
  padding: 1.5rem;
  margin: 2rem 0;
  border: 1px solid #3d3630;
  font-family: 'Source Sans 3', sans-serif;
  color: #e8e0d6;
}
.pw-header {
  display: flex; align-items: baseline; gap: 0.8rem; margin-bottom: 0.3rem;
}
.pw-header h4 {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.15rem; font-weight: 600; color: #E8CBA8; margin: 0;
}
.pw-header .pw-badge {
  font-size: 0.62rem; letter-spacing: 0.1em; text-transform: uppercase;
  background: rgba(176,137,104,0.2); color: #B08968; padding: 0.15em 0.6em;
  border-radius: 3px; font-weight: 600;
}
.pw-desc {
  font-size: 0.82rem; color: #9e958a; margin-bottom: 1rem; line-height: 1.5;
}
.pw-layout {
  display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap;
}
.pw-canvas-wrap { position: relative; flex: 0 0 auto; }
.pw-canvas-wrap canvas {
  border-radius: 50%; cursor: grab;
  box-shadow: 0 0 30px rgba(176,137,104,0.1), inset 0 0 60px rgba(0,0,0,0.3);
}
.pw-canvas-wrap canvas:active { cursor: grabbing; }
.pw-panel { flex: 1; min-width: 220px; }
.pw-info-box {
  background: rgba(255,255,255,0.04); border-radius: 8px;
  padding: 0.9rem 1rem; margin-bottom: 0.8rem;
  border: 1px solid rgba(255,255,255,0.06);
}
.pw-info-box .pw-label {
  font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.1em;
  color: #8a8279; margin-bottom: 0.3rem;
}
.pw-info-box .pw-value {
  font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; color: #E8CBA8;
}
.pw-info-box .pw-explain {
  font-size: 0.75rem; color: #7a7268; margin-top: 0.25rem; line-height: 1.4;
}
.pw-controls { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.6rem; }
.pw-btn {
  background: rgba(176,137,104,0.15); border: 1px solid rgba(176,137,104,0.3);
  color: #B08968; padding: 0.35em 0.8em; border-radius: 5px; cursor: pointer;
  font-size: 0.75rem; font-family: inherit; transition: all 0.2s;
}
.pw-btn:hover { background: rgba(176,137,104,0.3); color: #E8CBA8; }
.pw-btn.active { background: rgba(176,137,104,0.4); color: #fff; border-color: #B08968; }
.pw-legend {
  font-size: 0.72rem; color: #7a7268; margin-top: 0.8rem; line-height: 1.6;
}
.pw-legend span { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 4px; vertical-align: -1px; }
@media (max-width: 700px) {
  .pw-layout { flex-direction: column; align-items: center; }
  .pw-panel { min-width: 100%; }
}
</style>
<div class="pw-container">
  <div class="pw-header">
    <h4>Interactive: Poincaré Disk Model</h4>
    <span class="pw-badge">drag to explore</span>
  </div>
  <p class="pw-desc">
    The Poincaré disk maps the infinite hyperbolic plane onto a finite circle.
    Points near the centre are "general" concepts (high in the hierarchy); points near the boundary are "specific" (deep leaves).
    <strong>Drag any word</strong> to feel how hyperbolic distance grows exponentially near the edge.
    <strong>Click two nodes</strong> to compare distances.
  </p>
  <div class="pw-layout">
    <div class="pw-canvas-wrap">
      <canvas id="poincareCanvas" width="420" height="420"></canvas>
    </div>
    <div class="pw-panel">
      <div class="pw-info-box">
        <div class="pw-label">Selected pair</div>
        <div class="pw-value" id="pwPair">click two nodes</div>
      </div>
      <div class="pw-info-box">
        <div class="pw-label">Hyperbolic distance d(u,v)</div>
        <div class="pw-value" id="pwDist">—</div>
        <div class="pw-explain" id="pwDistExplain"></div>
      </div>
      <div class="pw-info-box">
        <div class="pw-label">Euclidean distance ‖u−v‖</div>
        <div class="pw-value" id="pwEuclid">—</div>
        <div class="pw-explain" id="pwEuclidExplain"></div>
      </div>
      <div class="pw-info-box">
        <div class="pw-label">Distance formula (Poincaré ball)</div>
        <div class="pw-value" style="font-size:0.78rem; color:#9e958a;">
          d(u,v) = arcosh(1 + 2‖u−v‖² / ((1−‖u‖²)(1−‖v‖²)))
        </div>
      </div>
      <div class="pw-controls">
        <button class="pw-btn" onclick="pwReset()">Reset</button>
        <button class="pw-btn" id="pwGeodesicBtn" onclick="pwToggleGeodesic()">Geodesic</button>
        <button class="pw-btn" id="pwGridBtn" onclick="pwToggleGrid()">Grid</button>
      </div>
      <div class="pw-legend">
        <span style="background:#E8CBA8;"></span> Root &nbsp;
        <span style="background:#8CB4A0;"></span> Mid &nbsp;
        <span style="background:#7A9CC6;"></span> Leaf &nbsp;
        <span style="background:#C97A7A;"></span> Leaf (alt)
      </div>
    </div>
  </div>
</div>
<script>
(function(){
  const canvas = document.getElementById('poincareCanvas');
  const ctx = canvas.getContext('2d');
  const W = canvas.width, H = canvas.height, R = W/2 - 15, cx = W/2, cy = H/2;
  const nodes = [
    { label: 'entity',    x: 0.00, y: 0.00, color: '#E8CBA8', depth: 0 },
    { label: 'organism',  x:-0.18, y:-0.22, color: '#8CB4A0', depth: 1 },
    { label: 'artifact',  x: 0.22, y:-0.15, color: '#8CB4A0', depth: 1 },
    { label: 'substance', x: 0.05, y: 0.25, color: '#8CB4A0', depth: 1 },
    { label: 'animal',    x:-0.38, y:-0.45, color: '#7A9CC6', depth: 2 },
    { label: 'plant',     x: 0.05, y:-0.50, color: '#7A9CC6', depth: 2 },
    { label: 'vehicle',   x: 0.50, y:-0.30, color: '#7A9CC6', depth: 2 },
    { label: 'food',      x: 0.20, y: 0.50, color: '#7A9CC6', depth: 2 },
    { label: 'dog',       x:-0.55, y:-0.68, color: '#C97A7A', depth: 3 },
    { label: 'cat',       x:-0.20, y:-0.72, color: '#C97A7A', depth: 3 },
    { label: 'oak',       x: 0.15, y:-0.73, color: '#C97A7A', depth: 3 },
    { label: 'car',       x: 0.70, y:-0.45, color: '#C97A7A', depth: 3 },
    { label: 'boat',      x: 0.68, y:-0.15, color: '#C97A7A', depth: 3 },
    { label: 'bread',     x: 0.10, y: 0.72, color: '#C97A7A', depth: 3 },
    { label: 'rice',      x: 0.35, y: 0.65, color: '#C97A7A', depth: 3 },
  ];
  const edges = [[0,1],[0,2],[0,3],[1,4],[1,5],[2,6],[3,7],[4,8],[4,9],[5,10],[6,11],[6,12],[7,13],[7,14]];
  let origPos = nodes.map(n => ({x:n.x, y:n.y}));
  let lastPair = [null, null], showGeodesic = false, showGrid = false;
  let dragging = null, dragOff = {x:0,y:0};

  function pd(u,v) {
    const dx=u.x-v.x, dy=u.y-v.y, num=dx*dx+dy*dy;
    const nu=u.x*u.x+u.y*u.y, nv=v.x*v.x+v.y*v.y;
    const den=(1-nu)*(1-nv); if(den<=0)return Infinity;
    return Math.acosh(Math.max(1,1+2*num/den));
  }
  function ed(u,v){return Math.sqrt((u.x-v.x)**2+(u.y-v.y)**2);}
  function toS(p){return{x:cx+p.x*R,y:cy+p.y*R};}
  function toP(s){return{x:(s.x-cx)/R,y:(s.y-cy)/R};}

  function draw() {
    ctx.clearRect(0,0,W,H);
    const g=ctx.createRadialGradient(cx,cy,0,cx,cy,R);
    g.addColorStop(0,'#2a2520');g.addColorStop(0.85,'#1f1b17');g.addColorStop(1,'#151210');
    ctx.beginPath();ctx.arc(cx,cy,R,0,Math.PI*2);ctx.fillStyle=g;ctx.fill();
    ctx.strokeStyle='rgba(176,137,104,0.3)';ctx.lineWidth=1.5;ctx.stroke();
    if(showGrid){for(let r=0.2;r<1;r+=0.2){ctx.beginPath();ctx.arc(cx,cy,r*R,0,Math.PI*2);ctx.strokeStyle='rgba(176,137,104,0.08)';ctx.lineWidth=1;ctx.stroke();}for(let a=0;a<Math.PI;a+=Math.PI/6){ctx.beginPath();ctx.moveTo(cx+R*Math.cos(a),cy+R*Math.sin(a));ctx.lineTo(cx-R*Math.cos(a),cy-R*Math.sin(a));ctx.strokeStyle='rgba(176,137,104,0.06)';ctx.lineWidth=1;ctx.stroke();}}
    edges.forEach(([i,j])=>{const a=toS(nodes[i]),b=toS(nodes[j]);ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.strokeStyle='rgba(176,137,104,0.15)';ctx.lineWidth=1;ctx.stroke();});
    if(showGeodesic&&lastPair[0]!==null&&lastPair[1]!==null){const u=nodes[lastPair[0]],v=nodes[lastPair[1]];const sp=toS(u),ep=toS(v);const mx=(u.x+v.x)/2,my=(u.y+v.y)/2,mn=Math.sqrt(mx*mx+my*my),pull=0.3*(1-mn);const cp=toS({x:mx*(1-pull),y:my*(1-pull)});ctx.beginPath();ctx.moveTo(sp.x,sp.y);ctx.quadraticCurveTo(cp.x,cp.y,ep.x,ep.y);ctx.strokeStyle='rgba(232,203,168,0.6)';ctx.lineWidth=2;ctx.setLineDash([5,4]);ctx.stroke();ctx.setLineDash([]);}
    nodes.forEach((n,i)=>{const s=toS(n);const r=n.depth===0?7:n.depth===1?6:n.depth===2?5:4.5;ctx.beginPath();ctx.arc(s.x,s.y,r+4,0,Math.PI*2);ctx.fillStyle=n.color+'18';ctx.fill();ctx.beginPath();ctx.arc(s.x,s.y,r,0,Math.PI*2);ctx.fillStyle=n.color;if(lastPair.includes(i)){ctx.fillStyle='#fff';ctx.shadowColor=n.color;ctx.shadowBlur=12;}ctx.fill();ctx.shadowBlur=0;ctx.fillStyle='#c8c0b6';ctx.font=(lastPair.includes(i)?'bold ':'')+'11px "Source Sans 3",sans-serif';ctx.textAlign='center';ctx.fillText(n.label,s.x,s.y-r-5);});
  }

  function info() {
    if(lastPair[0]!==null&&lastPair[1]!==null){
      const a=nodes[lastPair[0]],b=nodes[lastPair[1]];
      const hd=pd(a,b),eu=ed(a,b),ratio=hd/Math.max(eu,0.001);
      document.getElementById('pwPair').textContent=a.label+' ↔ '+b.label;
      document.getElementById('pwDist').textContent=hd===Infinity?'∞':hd.toFixed(3);
      document.getElementById('pwEuclid').textContent=eu.toFixed(3);
      document.getElementById('pwDistExplain').textContent=hd>4?'Very far — different hierarchy branches.':hd>2?'Moderate — several levels apart.':'Close — nearby in hierarchy.';
      document.getElementById('pwEuclidExplain').textContent='Ratio: '+ratio.toFixed(1)+'× — '+(ratio>3?'boundary distortion amplifies true distance!':'near center, distances are similar.');
    }
  }

  canvas.addEventListener('mousedown',e=>{const rect=canvas.getBoundingClientRect();const mx=e.clientX-rect.left,my=e.clientY-rect.top;let best=-1,bd=20;nodes.forEach((n,i)=>{const s=toS(n);const d=Math.sqrt((mx-s.x)**2+(my-s.y)**2);if(d<bd){bd=d;best=i;}});if(best>=0){dragging=best;const s=toS(nodes[best]);dragOff={x:mx-s.x,y:my-s.y};if(lastPair[0]===null){lastPair[0]=best;}else if(lastPair[1]===null&&lastPair[0]!==best){lastPair[1]=best;}else{lastPair=[best,null];}info();draw();}});
  canvas.addEventListener('mousemove',e=>{if(dragging===null)return;const rect=canvas.getBoundingClientRect();const p=toP({x:e.clientX-rect.left-dragOff.x,y:e.clientY-rect.top-dragOff.y});const norm=Math.sqrt(p.x*p.x+p.y*p.y),mx=0.92;if(norm>mx){p.x*=mx/norm;p.y*=mx/norm;}nodes[dragging].x=p.x;nodes[dragging].y=p.y;info();draw();});
  canvas.addEventListener('mouseup',()=>{dragging=null;});
  canvas.addEventListener('mouseleave',()=>{dragging=null;});
  canvas.addEventListener('touchstart',e=>{e.preventDefault();const t=e.touches[0];canvas.dispatchEvent(new MouseEvent('mousedown',{clientX:t.clientX,clientY:t.clientY}));},{passive:false});
  canvas.addEventListener('touchmove',e=>{e.preventDefault();const t=e.touches[0];canvas.dispatchEvent(new MouseEvent('mousemove',{clientX:t.clientX,clientY:t.clientY}));},{passive:false});
  canvas.addEventListener('touchend',()=>{dragging=null;});

  window.pwReset=function(){origPos.forEach((p,i)=>{nodes[i].x=p.x;nodes[i].y=p.y;});lastPair=[null,null];document.getElementById('pwPair').textContent='click two nodes';document.getElementById('pwDist').textContent='—';document.getElementById('pwEuclid').textContent='—';document.getElementById('pwDistExplain').textContent='';document.getElementById('pwEuclidExplain').textContent='';draw();};
  window.pwToggleGeodesic=function(){showGeodesic=!showGeodesic;document.getElementById('pwGeodesicBtn').classList.toggle('active',showGeodesic);draw();};
  window.pwToggleGrid=function(){showGrid=!showGrid;document.getElementById('pwGridBtn').classList.toggle('active',showGrid);draw();};
  draw();
})();
</script>
</div>

More broadly, the choice of geometric space becomes a modeling decision with linguistic content. Euclidean space $\mathbb{E}^n$ is appropriate for symmetric similarity. Hyperbolic space $\mathbb{H}^n$ is appropriate for hierarchies. Spherical space $\mathbb{S}^n$ may be appropriate for cyclical structures (colour terms, days of the week, seasonal vocabulary). And product spaces $\mathbb{H}^{n_1} \times \mathbb{S}^{n_2} \times \mathbb{E}^{n_3}$ may be needed for the complex mixture of relations found in natural language semantics — where hierarchical, cyclical, and flat similarity relations coexist.

### 9.4 The Manifold Hypothesis in Language Models

Recent work has shown that the token representations in Transformer models lie on manifolds whose intrinsic dimensionality is much lower than the ambient dimensionality. Different linguistic properties correspond to different geometric features: syntactic information tends to be encoded in linear subspace structure, while semantic information is encoded in nonlinear manifold geometry (curvature, topology). This distinction parallels the distinction between syntax and semantics in traditional linguistics.

### 9.5 Contextual Embeddings and the Geometry of Polysemy

Ethayarajh (2019) showed that contextual embeddings occupy a narrow cone in high-dimensional space. Different senses of a polysemous word occupy different regions of this cone, and the degree of separation varies across layers. In early layers, senses are close together; in middle layers, they are maximally separated; in later layers, they may reconverge. This layer-wise geometry of polysemy resolution is a window into how neural networks process lexical ambiguity.

> The "narrow cone" finding has a practical moral. If every vector points roughly the same way — like beams from torches all aimed at the same wall — then any two words have a high raw cosine similarity, and cosine stops being informative. This property, called **anisotropy**, is why careful studies subtract the mean vector, standardise dimensions, or compare similarities against a baseline of random word pairs before interpreting them.
{.intuition}


# Chapter 10. Topology and the Shape of Linguistic Spaces {#ch10}

> "A topologist is a person who cannot distinguish a coffee cup from a doughnut."
> — Mathematical folklore
{.epigraph}


![](./figures/topology.png)


### 10.1 What Topology Offers Linguistics

Topology studies properties preserved under continuous deformation — stretching, bending, and twisting, but not tearing or gluing. While geometry cares about distances and angles, topology cares about connectivity, holes, and the overall "shape" of a space. For linguistics, topology offers tools for asking questions that geometry cannot: Does the space of word meanings have holes? Do the internal representations of language models have a characteristic topological signature?


### 10.2 Basic Topological Concepts

A linguistically intuitive example: consider the semantic space of color terms. In a language with basic color terms arranged around the color wheel, the topology has a characteristic one-dimensional hole — you can traverse the color terms (red → orange → yellow → green → blue → purple → red) and return to your starting point, forming a loop that cannot be contracted to a point. This loop is a topological feature that exists regardless of how we stretch or deform the space.


> Classical vector semantics (geometry) tells us the *distance* between words. Topology asks a different question: how is the space *connected*, and what is its *shape*? Adding topology to our toolkit extends the analysis from the quantitative (probabilities and vectors) to the qualitative and structural. The rest of this section introduces the two central tools — **simplicial complexes** and **persistent homology** — and what they might mean for semantic space.
{.deep-dive: Deep dive: the topological turn in semantics}

#### From pairs to simplices

In vector semantics, we focus on pairwise relationships (the edge between two words). However, language often involves higher-order dependencies. A "context" is not just a pair of words, but a group of words that together form a coherent meaning.

Mathematically, we represent this using a **simplicial complex** $K$ — a set of "filled-in" shapes glued along shared faces:

- A 0-simplex is a single word: $[w_i]$.
- A 1-simplex is a relationship between two words: $[w_i, w_j]$.
- A 2-simplex is a filled triangle representing a 3-way semantic coherence: $[w_i, w_j, w_k]$.

> A simplicial complex is a construction kit of dots, sticks, and triangular tiles. Dots are words; a stick joins two words that belong together; a tile fills in a triangle when three words cohere *as a group*, not merely pairwise. The difference between three sticks and a tile is the difference between "each pair is related" and "the three form one context" — the kind of distinction that pairwise similarity alone cannot express.
{.intuition}

**Linguistic example.** Consider the words {*bank*, *river*, *money*, *interest*}.

- {*bank*, *river*} share a 1-simplex in a geographical context.
- {*bank*, *money*, *interest*} share a 2-simplex in a financial context.
- Crucially, {*river*, *money*} might not share an edge. This "missing edge" prevents the formation of a 3-way simplex, defining the boundaries of semantic domains.

#### Homology and lexical gaps

Topology allows us to calculate **Betti numbers** $\beta_n$, which count the "holes" in a space:

- $\beta_0$: the number of connected components (isolated semantic clusters);
- $\beta_1$: the number of one-dimensional loops that enclose empty space;
- $\beta_2$: the number of enclosed cavities, like the inside of a hollow ball.

The smallest example makes the idea concrete. Three words joined pairwise by three sticks, with no tile, form a hollow triangle: one component and one loop, so $\beta_0 = 1, \beta_1 = 1$. Add the tile and the loop is filled: $\beta_1 = 0$. A useful check is Euler's formula — (vertices) − (edges) + (faces) equals $\beta_0 - \beta_1 + \beta_2$: for the hollow triangle, $3 - 3 + 0 = 0 = 1 - 1$; for the filled one, $3 - 3 + 1 = 1 = 1 - 0$.

In a semantic space, a hole ($\beta_1 > 0$) is a candidate **lexical gap**: a conceptual region surrounded by words, yet empty at its center.

Example: imagine words describing "warmth," "hot," and "burning," and another set describing "affection," "passion," and "desire." If these clusters circle around a central concept for which the language has no specific word (e.g., a specific type of spiritual heat), the topology of the lexicon will literally show a hole. This remains a hypothesis to be tested, not an established result — holes can also arise from sparse sampling of vocabulary.

#### Persistent homology: which holes are real?

How do we know if a hole is "real" or just noise? We use **persistent homology**. We grow "balls" of radius $\epsilon$ around each word vector.

As $\epsilon$ increases, words connect to form edges, then triangles. We track the "birth" and "death" of topological features (components, holes).

<figure class="fig">
<svg viewBox="0 0 540 350" width="540" role="img" aria-label="Filtration and persistence barcode">
<g transform="translate(90,92)"><circle cx="40.1" cy="13.4" r="8" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="9.9" cy="39.9" r="8" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-28.4" cy="26.7" r="8" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-42.0" cy="-13.2" r="8" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-9.5" cy="-41.8" r="8" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="28.7" cy="-26.3" r="8" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="40.1" cy="13.4" r="3.5" fill="#6B4C3B"/><circle cx="9.9" cy="39.9" r="3.5" fill="#6B4C3B"/><circle cx="-28.4" cy="26.7" r="3.5" fill="#6B4C3B"/><circle cx="-42.0" cy="-13.2" r="3.5" fill="#6B4C3B"/><circle cx="-9.5" cy="-41.8" r="3.5" fill="#6B4C3B"/><circle cx="28.7" cy="-26.3" r="3.5" fill="#6B4C3B"/></g><text x="90" y="198" font-size="12" fill="#2C2825" text-anchor="middle">small ε: six separate words</text><g transform="translate(270,92)"><circle cx="40.1" cy="13.4" r="24" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="9.9" cy="39.9" r="24" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-28.4" cy="26.7" r="24" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-42.0" cy="-13.2" r="24" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-9.5" cy="-41.8" r="24" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="28.7" cy="-26.3" r="24" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><line x1="40.1" y1="13.4" x2="9.9" y2="39.9" stroke="#6B4C3B" stroke-width="1.5"/><line x1="9.9" y1="39.9" x2="-28.4" y2="26.7" stroke="#6B4C3B" stroke-width="1.5"/><line x1="-28.4" y1="26.7" x2="-42.0" y2="-13.2" stroke="#6B4C3B" stroke-width="1.5"/><line x1="-42.0" y1="-13.2" x2="-9.5" y2="-41.8" stroke="#6B4C3B" stroke-width="1.5"/><line x1="-9.5" y1="-41.8" x2="28.7" y2="-26.3" stroke="#6B4C3B" stroke-width="1.5"/><line x1="28.7" y1="-26.3" x2="40.1" y2="13.4" stroke="#6B4C3B" stroke-width="1.5"/><circle cx="40.1" cy="13.4" r="3.5" fill="#6B4C3B"/><circle cx="9.9" cy="39.9" r="3.5" fill="#6B4C3B"/><circle cx="-28.4" cy="26.7" r="3.5" fill="#6B4C3B"/><circle cx="-42.0" cy="-13.2" r="3.5" fill="#6B4C3B"/><circle cx="-9.5" cy="-41.8" r="3.5" fill="#6B4C3B"/><circle cx="28.7" cy="-26.3" r="3.5" fill="#6B4C3B"/></g><text x="270" y="198" font-size="12" fill="#2C2825" text-anchor="middle">medium ε: a loop is born</text><g transform="translate(450,92)"><circle cx="40.1" cy="13.4" r="44" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="9.9" cy="39.9" r="44" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-28.4" cy="26.7" r="44" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-42.0" cy="-13.2" r="44" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="-9.5" cy="-41.8" r="44" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><circle cx="28.7" cy="-26.3" r="44" fill="#B08968" fill-opacity="0.13" stroke="#B08968" stroke-opacity="0.35"/><polygon points="40.1,13.4 9.9,39.9 -28.4,26.7 -42.0,-13.2 -9.5,-41.8 28.7,-26.3" fill="#8CB4A0" fill-opacity="0.4"/><line x1="40.1" y1="13.4" x2="9.9" y2="39.9" stroke="#6B4C3B" stroke-width="1.5"/><line x1="9.9" y1="39.9" x2="-28.4" y2="26.7" stroke="#6B4C3B" stroke-width="1.5"/><line x1="-28.4" y1="26.7" x2="-42.0" y2="-13.2" stroke="#6B4C3B" stroke-width="1.5"/><line x1="-42.0" y1="-13.2" x2="-9.5" y2="-41.8" stroke="#6B4C3B" stroke-width="1.5"/><line x1="-9.5" y1="-41.8" x2="28.7" y2="-26.3" stroke="#6B4C3B" stroke-width="1.5"/><line x1="28.7" y1="-26.3" x2="40.1" y2="13.4" stroke="#6B4C3B" stroke-width="1.5"/><circle cx="40.1" cy="13.4" r="3.5" fill="#6B4C3B"/><circle cx="9.9" cy="39.9" r="3.5" fill="#6B4C3B"/><circle cx="-28.4" cy="26.7" r="3.5" fill="#6B4C3B"/><circle cx="-42.0" cy="-13.2" r="3.5" fill="#6B4C3B"/><circle cx="-9.5" cy="-41.8" r="3.5" fill="#6B4C3B"/><circle cx="28.7" cy="-26.3" r="3.5" fill="#6B4C3B"/></g><text x="450" y="198" font-size="12" fill="#2C2825" text-anchor="middle">large ε: the loop is filled (dies)</text>
<g transform="translate(0,222)">
<text x="10" y="0" font-size="12" fill="#6B635A">Barcode: each bar is one feature, drawn from its birth to its death</text>
<line x1="60" y1="110" x2="520" y2="110" stroke="#6B635A"/><text x="524" y="114" font-size="12" fill="#2C2825">ε</text>
<line x1="210" y1="14" x2="210" y2="114" stroke="#E2DBD1" stroke-dasharray="3 3"/><line x1="390" y1="14" x2="390" y2="114" stroke="#E2DBD1" stroke-dasharray="3 3"/>
<text x="10" y="42" font-size="12" fill="#6B4C3B" font-weight="600">β₀</text>
<line x1="60" y1="18" x2="200" y2="18" stroke="#6B4C3B" stroke-width="3"/><line x1="60" y1="25" x2="203" y2="25" stroke="#6B4C3B" stroke-width="3"/><line x1="60" y1="32" x2="206" y2="32" stroke="#6B4C3B" stroke-width="3"/><line x1="60" y1="39" x2="209" y2="39" stroke="#6B4C3B" stroke-width="3"/><line x1="60" y1="46" x2="212" y2="46" stroke="#6B4C3B" stroke-width="3"/>
<line x1="60" y1="53" x2="515" y2="53" stroke="#6B4C3B" stroke-width="3"/>
<text x="10" y="86" font-size="12" fill="#4A6E9A" font-weight="600">β₁</text>
<line x1="214" y1="82" x2="386" y2="82" stroke="#7A9CC6" stroke-width="5"/>
</g>
</svg>
<figcaption><b>Figure 10.1.</b> A filtration and its barcode. As the balls around six word-points grow, separate components merge (the short $\beta_0$ bars end) and a loop appears; as they grow further, triangles fill the loop in and it dies. Long bars are robust structure; short bars are noise.</figcaption>
</figure>

> Persistent homology is like watching ink blots spread on wet paper. At first each drop is separate; then neighbouring drops touch and merge; sometimes a ring of drops encloses a dry patch in the middle, which survives for a while before the ink finally floods it. A dry patch that survives a long time is a genuine feature of the arrangement; one that is flooded almost immediately was an accident of spacing.
{.intuition}

**Linguistic insight.** Robust semantic structures "persist" over a long range of $\epsilon$, while accidental associations disappear quickly. This gives us a "barcode" of a language's conceptual structure.

#### The boundary operator

To find holes algebraically, we define a **boundary operator** $\partial_n$ that maps each simplex to the signed sum of its faces:

$$\partial_n([v_0, \dots, v_n]) = \sum_{i=0}^{n} (-1)^i [v_0, \dots, \hat{v}_i, \dots, v_n]$$

where $\hat{v}_i$ means "omit $v_i$". For a triangle, $\partial_2[a,b,c] = [b,c] - [a,c] + [a,b]$: its three edges, oriented to go round the loop. A chain whose boundary is zero is a **cycle** (it closes up); a cycle that is itself the boundary of something filled is a "trivial" loop. The holes are the cycles that are *not* boundaries: formally, the quotient $H_n = Z_n / B_n$ of cycles $Z_n = \ker \partial_n$ by boundaries $B_n = \mathrm{im}\, \partial_{n+1}$, and $\beta_n = \mathrm{rank}\, H_n$. For linguists, $H_n$ is a mathematical signature of what a lexicon leaves unfilled — what a language cannot say, or chooses not to group together.

### 10.3 Persistent Homology and Word Embedding Topology

Persistent homology tracks how topological features appear and disappear as we vary a scale parameter. Given a set of points (such as word embeddings), we build a family of simplicial complexes indexed by a distance threshold $\varepsilon$: at each threshold, we connect points that are within distance $\varepsilon$ of each other. As $\varepsilon$ increases from $0$ to $\infty$, topological features are "born" (when new connections create loops or voids) and "die" (when those features are filled in). The persistence diagram — which plots each feature's birth time $b_i$ and death time $d_i$ — summarizes the multi-scale topological structure. Features with high persistence $d_i - b_i$ represent robust topological structure. Word embedding spaces exhibit nontrivial persistent homology: stable loops that may correspond to semantic "circuits" — cyclic patterns of association (seasons, days of the week, stages of life).








### 10.4 Topological Data Analysis of Language Models

The persistent homology of activation vectors at different Transformer layers reveals that topological complexity varies systematically: early layers have simpler topology, middle layers exhibit maximum complexity, and later layers simplify again. Layers that encode rich syntactic structure tend to have higher Betti numbers $\beta_k = \mathrm{rank}\,H_k$, suggesting more complex topology.

### 10.5 Sheaf Theory and Discourse Coherence

Sheaf theory provides a mathematical framework for studying how local information can be consistently combined into global information.

> Think of several witnesses to an event, each of whom saw only part of it. Each testimony is locally coherent. A consistent global story exists only if the testimonies *agree wherever they overlap* — if two witnesses both saw the getaway car, they must agree on its colour. A sheaf formalises exactly this: data attached to local regions, plus a **gluing condition** saying when local data assemble into a global whole. Discourse is similar: each sentence is interpreted in its local context, and a coherent text is one whose local interpretations glue together; a failure to glue is a contradiction or an unresolved ambiguity.
{.intuition}

Abramsky and collaborators (Abramsky & Brandenburger, 2011) have used sheaf theory to model contextuality in language — connecting surprisingly to quantum mechanics, where sheaf-theoretic methods characterize non-classical correlations. The mathematical parallel between linguistic contextuality and quantum contextuality reflects a shared formal structure of context-dependence that may have deep cognitive implications.


# Chapter 11. Differential Geometry on the Landscape of Language {#ch11}

> God created the integers; all the rest is the work of man.
> — Leopold Kronecker
{.epigraph}

### 11.1 Why Differential Geometry?

Differential geometry is the mathematical framework for studying curved spaces using the tools of calculus. If topology tells us the overall "shape" of a space, differential geometry tells us how the space curves and stretches locally — how distances, angles, and volumes vary from point to point. For language, differential geometry becomes essential when we recognize that the spaces in which linguistic objects are embedded — the parameter spaces of language models, the manifolds of word representations, the loss landscapes — are not flat but curved, and this curvature carries linguistic information.

### 11.2 Riemannian Manifolds: The Foundation

A Riemannian manifold is a smooth manifold $M$ equipped with a Riemannian metric — a smoothly varying inner product $g_p$ on each tangent space $T_pM$ that allows us to measure lengths, angles, and volumes. The length of a curve $\gamma: [a,b] \to M$ is:

$$L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}\!\bigl(\dot\gamma(t),\, \dot\gamma(t)\bigr)}\; dt$$

and the geodesic distance $d(p,q)$ between two points is the infimum of lengths over all curves connecting them. For the linguist, the key intuition is this: a Riemannian manifold is a space where the "ruler" for measuring distances changes from place to place.

> Imagine a hiking map on which every square kilometre carries its own note: "flat meadow — easy walking" or "steep scree — every metre costs ten". The **metric** $g$ is that note: at each point, it says how much effort a small step in each direction costs. The length formula above just walks along a route $\gamma$, measures each tiny step $\dot\gamma(t)\,dt$ with the local rule, and adds up the costs. The **geodesic** is the cheapest route — which, in rough terrain, is rarely the straight line on the map.
{.intuition}

In linguistic terms, moving from one region of semantic space to another may involve different amounts of "semantic distance" per unit of geometric distance — the local metric reflects the local density and organization of meanings.

### 11.3 Curvature and the Local Structure of Semantic Space

<figure class="fig">
<svg viewBox="0 0 540 205" width="540" role="img" aria-label="Triangles in flat, spherical and hyperbolic geometry">
<g transform="translate(90,90)"><path d="M0 -55 Q-30.0 -5.0 -60 45 Q0.0 45.0 60 45 Q30.0 -5.0 0 -55 Z" fill="#6B4C3B" fill-opacity="0.18" stroke="#6B4C3B" stroke-width="1.8"/><text x="0" y="82" font-size="12.5" fill="#2C2825" text-anchor="middle" font-weight="600">flat (K = 0)</text><text x="0" y="100" font-size="12" fill="#6B635A" text-anchor="middle">angles sum to 180°</text></g><g transform="translate(270,90)"><path d="M0 -55 Q-46.5 -5.0 -60 45 Q0.0 72.5 60 45 Q46.5 -5.0 0 -55 Z" fill="#8CB4A0" fill-opacity="0.18" stroke="#8CB4A0" stroke-width="1.8"/><text x="0" y="82" font-size="12.5" fill="#2C2825" text-anchor="middle" font-weight="600">spherical (K > 0)</text><text x="0" y="100" font-size="12" fill="#6B635A" text-anchor="middle">angles sum to more than 180°</text></g><g transform="translate(450,90)"><path d="M0 -55 Q-13.5 -5.0 -60 45 Q0.0 17.5 60 45 Q13.5 -5.0 0 -55 Z" fill="#7A9CC6" fill-opacity="0.18" stroke="#7A9CC6" stroke-width="1.8"/><text x="0" y="82" font-size="12.5" fill="#2C2825" text-anchor="middle" font-weight="600">hyperbolic (K < 0)</text><text x="0" y="100" font-size="12" fill="#6B635A" text-anchor="middle">angles sum to less than 180°</text></g>
</svg>
<figcaption><b>Figure 11.1.</b> Curvature seen from the inside. An inhabitant who cannot leave the surface can still detect curvature by drawing a triangle out of shortest paths and adding its angles. On a sphere the sides bulge outwards; on a saddle-shaped (hyperbolic) surface they are pinched inwards.</figcaption>
</figure>

The curvature of a Riemannian manifold measures how it deviates from flatness. Negative curvature (hyperbolic) means geodesics diverge and volumes grow faster than in flat space; positive curvature (spherical) means geodesics converge. Regions of high negative curvature in the representation manifold may correspond to hierarchical branching structures; regions of positive curvature may correspond to tightly clustered, cyclic structures. By measuring curvature at different points and layers, researchers can build a "curvature atlas" of linguistic information organization.

### 11.4 Geodesics and Semantic Trajectories

A geodesic is the shortest path between two points on a manifold — the generalization of a straight line to curved spaces. The geodesic from "puppy" to "dog" may pass through representations encoding maturation. The geodesic from "walk" to "run" may pass through representations encoding increasing speed. Geodesics on the representation manifold may encode conceptual pathways — the cognitive paths by which one concept is transformed into another.

### 11.5 The Fisher Information Metric

One of the deepest connections between differential geometry and language models comes through the Fisher information metric. For a family of probability distributions $p(x|\theta)$ parameterized by $\theta$, the Fisher information matrix defines a Riemannian metric on the parameter space:

$$F(\theta)_{ij} = \mathbb{E}_{x \sim p(\cdot|\theta)}\!\left[\frac{\partial \log p(x|\theta)}{\partial \theta_i} \cdot \frac{\partial \log p(x|\theta)}{\partial \theta_j}\right]$$

This metric measures how rapidly the probability distribution changes as the parameters vary. Flat directions (low Fisher information) correspond to redundant parameters; curved directions (high Fisher information) correspond to parameters that strongly influence linguistic behavior. This geometric perspective has implications for catastrophic forgetting and the effectiveness of low-rank adaptation methods like LoRA (Hu et al., 2022).

> The Fisher metric answers the question: "if I nudge the model's parameters slightly, how *distinguishable* are the old and new predictions?" Two settings are far apart in this geometry not when their numbers differ a lot, but when they would produce noticeably different text. It is the distance a listener would perceive, not the distance an accountant would compute.
{.intuition}

The simplest case shows why this matters. Let a single parameter $p$ be the probability that some word occurs (a Bernoulli distribution). Its Fisher information is

$$F(p) = \frac{1}{p(1-p)}.$$

At $p = 0.5$, $F = 4$; at $p = 0.01$, $F \approx 101$. Raising a common word's probability from 50% to 51% barely changes what we observe, but raising a rare word's probability from 1% to 2% *doubles* how often it appears — the same Euclidean step of $0.01$ is several times longer in Fisher distance (which scales as $\sqrt{F}$). The geometry of probability space is therefore genuinely curved: it stretches near the edges, where rare events live — a pattern reminiscent of the Poincaré disk of §9.3. Formally, the Fisher metric is the infinitesimal form of the KL divergence of §6.3:

$$\mathrm{KL}\bigl(p_\theta \,\|\, p_{\theta + d\theta}\bigr) \approx \tfrac{1}{2}\, d\theta^\top F(\theta)\, d\theta,$$

and **natural gradient** methods (Amari, 2016) exploit this by taking optimisation steps of fixed *Fisher* length rather than fixed Euclidean length.

### 11.6 Fiber Bundles and the Architecture of Linguistic Representation

A fiber bundle is a topological space that locally looks like a product space $E \cong B \times F$ (with projection $\pi: E \to B$), but may have nontrivial global structure — the fibers may "twist" as one moves around the base space. In linguistic representation, the base space $B$ might represent syntactic structure, and the fiber $F_p = \pi^{-1}(p)$ at each node $p$ might represent semantic and morphological features. This connects to gauge equivariant neural networks, which use fiber bundles and connections to build networks that respect specified symmetries. If linguistic structure has gauge-like symmetries, gauge-equivariant architectures may be natural candidates for next-generation language models.

> A fiber bundle is a space in which every point of a "base" carries its own small attached space — like every point on a scalp carrying a hair, or every town on a map carrying its own local timetable. Locally, it is just "base × fiber". The interesting case is when the attachment *twists* globally: a Möbius strip is a circle (base) with a line segment (fiber) attached at each point, but going once around flips the segment over. For language, the proposal is that grammatical position is the base and the space of possible fillers at that position is the fiber. How fibers are "connected" as one moves through the structure would then describe how features propagate — agreement, for example. This remains a research programme rather than an established result.
{.intuition}


# Chapter 12. Category Theory: The Mathematics of Mathematical Linguistics {#ch12}

> Category theory takes a bird's-eye view of mathematics.
> — Tom Leinster
{.epigraph}

### 12.1 Categories as a Unifying Language

Category theory provides a language for describing deep structural similarities between different mathematical frameworks. A category $\mathbf{C}$ consists of objects, morphisms between objects, and a composition operation. The category $\mathbf{Set}$ has sets and functions. The category $\mathbf{Vect}$ has vector spaces and linear maps. The category $\mathbf{Top}$ has topological spaces and continuous maps. By abstracting common structure, we can see what is preserved when translating between different mathematical representations of language.

> A category is like a transit map. The **objects** are stations; the **morphisms** are routes from one station to another; **composition** is making a transfer — a route from A to B followed by a route from B to C is itself a route from A to C. Every station has a trivial "stay where you are" route (the **identity**), and it does not matter how you bracket a journey with several transfers (**associativity**). That is the entire definition. What makes it powerful is how little it assumes: sets and functions, vector spaces and linear maps, and syntactic types and derivations all satisfy it.
{.intuition}

A linguistic category, in the tradition of Lambek (1958), takes *syntactic types* as objects (e.g. $n$ for noun phrases, $s$ for sentences) and *derivations* as morphisms: there is a morphism $a \to b$ whenever an expression of type $a$ can be shown to have type $b$. Composition is chaining derivations; the identity is the trivial derivation.

### 12.2 Functors and Natural Transformations

A functor $F: \mathbf{C} \to \mathbf{D}$ is a structure-preserving map between categories. In linguistics, the passage from syntactic trees to semantic representations can be modeled as a functor. The embedding of words into vectors is a functor from a discrete linguistic category to the category of vector spaces. A natural transformation $\eta: F \Rightarrow G$ provides a systematic way of comparing two such translations while respecting structure.

> A functor is a translation that preserves connections. A subway map is a functor from the city: it sends each station to a dot and each route to a line, and it guarantees that if two routes connect in the city, their lines connect on the map. It forgets a great deal (distances, streets, scenery) but never breaks a connection. The defining law, $F(g \circ f) = F(g) \circ F(f)$, says: translating a combined journey gives the same result as translating each leg and combining the translations.
{.intuition}

<figure class="fig">
<svg viewBox="0 0 520 230" width="520" role="img" aria-label="Compositionality as a commutative square">
<defs><marker id="ca" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#6B4C3B"/></marker></defs>
<rect x="20" y="30" width="170" height="44" rx="6" fill="#F7F3EC" stroke="#B08968"/><text x="105" y="57" font-size="12.5" fill="#2C2825" text-anchor="middle">John · loves · Mary</text>
<rect x="330" y="30" width="170" height="44" rx="6" fill="#F7F3EC" stroke="#B08968"/><text x="415" y="57" font-size="12.5" fill="#2C2825" text-anchor="middle">John loves Mary</text>
<rect x="20" y="160" width="170" height="44" rx="6" fill="#E6EDF4" stroke="#7A9CC6"/><text x="105" y="187" font-size="12.5" fill="#2C2825" text-anchor="middle">⟦John⟧, ⟦loves⟧, ⟦Mary⟧</text>
<rect x="330" y="160" width="170" height="44" rx="6" fill="#E6EDF4" stroke="#7A9CC6"/><text x="415" y="187" font-size="12.5" fill="#2C2825" text-anchor="middle">⟦John loves Mary⟧</text>
<line x1="192" y1="52" x2="326" y2="52" stroke="#6B4C3B" stroke-width="1.5" marker-end="url(#ca)"/><text x="260" y="44" font-size="12" fill="#6B4C3B" text-anchor="middle">syntactic composition</text>
<line x1="192" y1="182" x2="326" y2="182" stroke="#6B4C3B" stroke-width="1.5" marker-end="url(#ca)"/><text x="260" y="174" font-size="12" fill="#6B4C3B" text-anchor="middle">semantic composition</text>
<line x1="105" y1="76" x2="105" y2="156" stroke="#6B4C3B" stroke-width="1.5" marker-end="url(#ca)"/><text x="115" y="121" font-size="13" fill="#6B4C3B" font-style="italic">F</text>
<line x1="415" y1="76" x2="415" y2="156" stroke="#6B4C3B" stroke-width="1.5" marker-end="url(#ca)"/><text x="425" y="121" font-size="13" fill="#6B4C3B" font-style="italic">F</text>
<text x="260" y="121" font-size="12" fill="#6B635A" text-anchor="middle">the two paths agree</text>
</svg>
<figcaption><b>Figure 12.1.</b> Compositionality as a commutative square. Going right-then-down (build the sentence, then interpret it) and going down-then-right (interpret the words, then combine the meanings) must give the same answer. Saying that interpretation $F$ is a functor is saying exactly that this square commutes — Frege's principle, stated as a diagram.</figcaption>
</figure>

### 12.3 The Categorical Approach to Compositionality

The DisCoCat framework models the syntax-semantics interface as a monoidal functor from a pregroup grammar (modeling syntax) to $\mathbf{FdVect}$ (finite-dimensional vector spaces, modeling semantics). This categorical perspective unifies the formal-semantic tradition of Montague and the distributional tradition — both can be expressed as functors from syntax to semantics. They differ in the target category ($\mathbf{Set}$ vs. $\mathbf{Vect}$) but share the same abstract principle. Category theory reveals that these approaches are not competitors but different instantiations of the same compositionality principle.

A **pregroup grammar** (Lambek, 1999) makes the syntactic side concrete. Each basic type $a$ has a left adjoint $a^l$ and a right adjoint $a^r$, which cancel against it: $a^l \cdot a \to 1$ and $a \cdot a^r \to 1$. Think of $a^r$ as "I need an $a$ on my left" and $a^l$ as "I need an $a$ on my right". A transitive verb has type $n^r\, s\, n^l$: it needs a noun phrase on each side and yields a sentence. For *John loves Mary*:

$$n \cdot (n^r\, s\, n^l) \cdot n \;\to\; (n \cdot n^r)\; s\; (n^l \cdot n) \;\to\; 1 \cdot s \cdot 1 = s.$$

The cancellations are the grammatical "wiring". DisCoCat's insight is that the *same wiring* can be read in $\mathbf{FdVect}$, where each cancellation becomes a tensor contraction — precisely the sum over $i$ and $j$ in §7.5.

### 12.4 Enriched Categories and Graded Structures

In enriched categories, morphisms form objects in some other category — a metric space or vector space rather than a set. This is natural for linguistic applications where relationships are graded: the similarity between two words is a continuous measure, not binary. Enriching linguistic categories over metric spaces gives a framework in which graded linguistic relations are first-class citizens.


### 12.5 What Category Theory Buys — and What It Costs

The payoff of the categorical view is *transfer*: once two frameworks are shown to be instances of the same structure, results, proofs, and even software can move between them. It also makes design choices explicit — choosing a target category is choosing what kind of meaning you believe in (truth values, vectors, probability distributions). The cost is abstraction: category theory rarely tells you anything about a specific sentence that the concrete framework could not. It is best read not as a new theory of language but as a theory of *theories* of language, a map of the maps drawn in the preceding chapters.

<!-- part: Part IV · Complex Systems & Reflection -->

# Chapter 13. Language as a Complex Adaptive System {#ch13}

> More is different.
> — Philip Anderson
{.epigraph}

### 13.1 The Complex Turn in Linguistics

The frameworks explored in Parts I–III share a common assumption: that language can be analyzed in terms of stable structures — grammars, vector spaces, manifolds, categories. Yet language, as it actually exists in communities of speakers spread across time, is none of these things alone. It is messy, dynamic, historically contingent, and perpetually incomplete. The scientific tradition that takes these properties seriously, rather than bracketing them as noise, is the study of *complex adaptive systems* (CAS).

The landmark statement of this program for linguistics is the manifesto published by the Five Graces Group (Beckner, Blythe, Bybee, Christiansen, Croft, Ellis, Holland, Ke, Larsen-Freeman, and Schoenemann, 2009), simply titled "Language is a complex adaptive system." Drawing on work in complexity science, evolutionary biology, and cognitive science, Beckner et al. argue that language — simultaneously a cognitive system, a social institution, and a historical artifact — exhibits all the hallmarks of a CAS: it is distributed across a population of interacting agents, it evolves without central control, it exhibits emergent properties at the level of the system that are not present at the level of individual agents, and it perpetually adapts to new communicative pressures.

This is not a metaphor. The mathematical tools of complexity science — dynamical systems theory, agent-based models, network theory, and information-theoretic measures of self-organization — have been brought to bear on language with concrete and testable results.

### 13.2 Properties of a Complex Adaptive System

What makes a system *complex adaptive*? Drawing on Holland (1995) and Mitchell (2009), we can enumerate the key properties and map them onto linguistic phenomena.

**Distributed control and emergence.** No central authority governs language evolution. Sound changes, grammaticalization processes, and the spread of new constructions arise from the local interactions of millions of speakers. The grammatical patterns of Modern English are not the design of any planner; they are the emergent result of countless speech acts across centuries. Croft (2000) formalizes this in the theory of *utterance selection*: linguistic variants compete in a population, and the outcome of this competition — the differential replication of forms — produces the directional patterns we call language change.

**Intrinsic diversity and non-stationarity.** A CAS maintains internal variation as a resource. Linguistic communities are never homogeneous: regional dialects, social registers, age-graded variation, and idiolectal differences create a perpetual pool of variation from which selection can operate. The sociolinguistic literature documents this diversity in meticulous quantitative detail.

**Non-linearity and phase transitions.** In a CAS, small perturbations can trigger large-scale reorganizations. The history of language is punctuated by rapid reorganizations — the Great Vowel Shift in English, the emergence of analytic word order from synthetic — that do not appear proportionate to their triggers. This non-linearity is a hallmark of dynamical systems operating near *critical points*, as we discuss in §13.6.

**Sensitive dependence on network structure.** How rapidly a linguistic innovation spreads depends critically on the topology of the social network through which speakers interact (Barabási & Albert, 1999). Scale-free networks — where a few highly connected hubs interact with many peripheral nodes — produce different diffusion dynamics from small-world or regular lattice networks.

**Adaptation through amplification and competition.** Linguistic forms are in constant competition for communicative niches. Forms that serve communicative functions efficiently get amplified; redundant or inefficient forms get pruned. The result is a continuously adapting system that is neither random nor rigidly determined.

### 13.3 Dynamical Systems: Attractors, Phase Transitions, and the Grammar of Change

The mathematical backbone of complexity science is *dynamical systems theory*. A dynamical system is a tuple $(\mathcal{X}, \Phi^t)$ where $\mathcal{X}$ is the state space and $\Phi^t: \mathcal{X} \to \mathcal{X}$ is the flow map giving the state of the system at time $t$ given its initial state. For a continuous-time system governed by a differential equation $\dot{x} = f(x)$, the flow solves the initial value problem.

The key objects of interest are the *attractors* of the flow:

- **Fixed-point attractors:** The system converges to a stable equilibrium $x^* = f^{-1}(0)$. In linguistics, a fully conventionalized form — a phoneme that has categorically shifted — represents a fixed-point attractor.
- **Limit cycles:** The system oscillates periodically. Some models of linguistic rhythm and prosodic organization exhibit limit-cycle behavior.
- **Strange attractors:** For chaotic systems, the attractor has fractal geometry. While linguistic systems are unlikely to be fully chaotic, sensitivity to initial conditions may manifest locally near critical points.

*Phase transitions* occur when a control parameter crosses a critical threshold, causing the system to reorganize from one attractor basin to another. The logistic (S-curve) model of language change,

$$\frac{dx}{dt} = \beta\, x(1-x) + \sigma\, \xi(t)$$

where $x \in [0,1]$ is the frequency of the innovative form, $\beta$ is the selection coefficient, and $\xi(t)$ is Gaussian noise, describes the S-shaped adoption curves documented across hundreds of language changes. The transition from $x \approx 0$ (old form dominant) to $x \approx 1$ (new form dominant) is a shift between attractors: for $\beta > 0$ the fixed point at $x = 0$ is unstable, so any small seed of the innovation grows, and the fixed point at $x = 1$ captures the system's trajectory. (Strictly, the term *phase transition* is reserved for a qualitative change as a control parameter crosses a threshold — here, $\beta$ changing sign — but the S-curve itself is the visible signature of that instability.)

<figure class="fig">
<svg viewBox="0 0 520 270" width="520" role="img" aria-label="S-curve of language change">
<line x1="60" y1="220" x2="490" y2="220" stroke="#6B635A"/><line x1="60" y1="30" x2="60" y2="220" stroke="#6B635A"/>
<text x="52" y="224" font-size="11" fill="#6B635A" text-anchor="end">0</text><text x="52" y="44" font-size="11" fill="#6B635A" text-anchor="end">1</text>
<line x1="60" y1="40" x2="490" y2="40" stroke="#E2DBD1" stroke-dasharray="3 3"/>
<path d="M60.0 219.6 L67.0 219.5 L74.0 219.3 L81.0 219.2 L88.0 219.0 L95.0 218.8 L102.0 218.5 L109.0 218.2 L116.0 217.8 L123.0 217.3 L130.0 216.8 L137.0 216.1 L144.0 215.2 L151.0 214.2 L158.0 213.0 L165.0 211.5 L172.0 209.7 L179.0 207.6 L186.0 205.0 L193.0 202.0 L200.0 198.5 L207.0 194.5 L214.0 189.8 L221.0 184.4 L228.0 178.3 L235.0 171.6 L242.0 164.2 L249.0 156.2 L256.0 147.8 L263.0 139.0 L270.0 130.0 L277.0 121.0 L284.0 112.2 L291.0 103.8 L298.0 95.8 L305.0 88.4 L312.0 81.7 L319.0 75.6 L326.0 70.2 L333.0 65.5 L340.0 61.5 L347.0 58.0 L354.0 55.0 L361.0 52.4 L368.0 50.3 L375.0 48.5 L382.0 47.0 L389.0 45.8 L396.0 44.8 L403.0 43.9 L410.0 43.2 L417.0 42.7 L424.0 42.2 L431.0 41.8 L438.0 41.5 L445.0 41.2 L452.0 41.0 L459.0 40.8 L466.0 40.7 L473.0 40.5 L480.0 40.4 " fill="none" stroke="#6B4C3B" stroke-width="2.4"/>
<text x="110" y="205" font-size="12" fill="#6B635A" text-anchor="middle">slow start</text>
<text x="300" y="120" font-size="12" fill="#6B4C3B">rapid spread</text>
<text x="440" y="60" font-size="12" fill="#6B635A" text-anchor="middle">saturation</text>
<text x="275" y="252" font-size="12" fill="#2C2825" text-anchor="middle">time</text>
<text x="18" y="125" font-size="12" fill="#2C2825" text-anchor="middle" transform="rotate(-90 18 125)">share of new form x</text>
</svg>
<figcaption><b>Figure 13.1.</b> The logistic S-curve. Change begins slowly (few speakers to copy from), accelerates in the middle (many innovators, many conservatives to convert), and slows at the end (few holdouts left). Its steepest point is at $x = 1/2$, where the growth rate $\beta x(1-x)$ is maximal.</figcaption>
</figure>

> An S-curve is how a rumour spreads through a school. At first, only a few pupils know it, so it spreads slowly. Once many know it, every conversation is a chance to pass it on, and it spreads explosively. At the end, almost everyone has heard it, and there is no one left to tell. The term $x(1-x)$ is exactly this logic: growth needs both people who have the new form ($x$) and people who do not yet ($1-x$).
{.intuition}

Blythe and Croft (2012) provide a comprehensive mathematical treatment of language change as a stochastic dynamical process, unifying sociolinguistic data with the mathematics of population dynamics.

### 13.4 Agent-Based Models and the Emergence of Linguistic Convention

A complementary mathematical approach models language as the outcome of interactions among many *agents*, each following simple local rules, from which global structure emerges. The paradigm example is Steels's (1995, 2011) *Language Game* framework.

In the Naming Game, a population of $N$ agents must converge on a shared lexicon for a set of objects without any central coordinator. The protocol is:

1. A *speaker* is selected at random and attempts to name a randomly chosen object, drawing from its inventory (or inventing a new word if empty).
2. A *hearer* attempts to parse the word. If successful, both agents reinforce that word and prune alternatives. If not, the hearer adds the new word to its inventory.

The mathematical analysis of this protocol reveals a phase transition from initial disorder (every agent uses different words) to global consensus (all agents converge on a single word per object) through a process of symmetry breaking. The convergence time scales as $O(N^{1.5})$ (Baronchelli et al., 2006), and the word frequency distribution follows a power law during the intermediate phase — another hallmark of criticality. The simulator at the end of this chapter allows you to observe these dynamics in real time.

### 13.5 Construction Grammar as a Complex Network

The grammatical system itself, viewed from a CAS perspective, is not a set of categorical rules but a *network of constructions* — form-meaning pairings that range from fully lexically specified idioms ("by and large") to schematic patterns ("the Xer the Yer"). This is the perspective of *Construction Grammar* (Goldberg, 1995; Croft, 2001; Tomasello, 2003).

What makes the constructional view compatible with complexity science is that the network of constructions has the topological properties of a *complex network*: a scale-free degree distribution (a few very general, highly connected schemas coexist with many specific, weakly connected idioms) and small-world properties (any two constructions are connected by a short path of inheritance or similarity links). Barabási and Albert (1999) showed that scale-free networks arise from *preferential attachment*: new constructions are more likely to inherit from and extend constructions that are already well entrenched.

Entrenchment — Langacker's (1987) term for the cognitive strength of a linguistic unit — is, mathematically, the activation level of a node in a spreading-activation network. The weight $w_{ij}$ of the link from construction $i$ to construction $j$ reflects their functional and formal similarity. Spreading activation,

$$a_j(t+1) = (1-d)\sum_i \frac{w_{ij}}{\sum_k w_{ik}} \cdot a_i(t) + d \cdot s_j$$

where $d$ is a decay factor and $s_j$ is the external stimulus, models how priming one construction activates related constructions (Collins & Loftus, 1975). The network topology determines which constructions are most central (high betweenness centrality), most reachable (low mean shortest path), and most vulnerable to perturbation.

### 13.6 Self-Organization and the Edge of Chaos

A striking property of many CAS is that they spontaneously organize into a critical state — neither fully ordered nor fully random — without any external tuning. This phenomenon, termed *self-organized criticality* (SOC) by Bak, Tang, and Wiesenfeld (1987), is marked by power-law distributions, $1/f$ noise, and scale-invariant fluctuations.

Kello et al. (2010) provide systematic evidence that linguistic behavior — reading times, response latencies, phoneme durations — exhibits $1/f$ fluctuations consistent with SOC. Zipf's law itself (§6.5) — the power-law frequency distribution of words — is now understood as a hallmark of linguistic criticality: a system at the edge of chaos, balanced between the order needed for communication and the disorder needed for expressive flexibility.

The mathematical signature of SOC is a power-law distribution:

$$P(s) \propto s^{-\tau}$$

where $s$ is the size of a fluctuation (a word's rank, a parsing time, a syntactic dependency length) and $\tau$ is the critical exponent. The fact that linguistic observables cluster around similar exponents across languages and speakers suggests that language actively self-organizes to maintain the critical state. From a cognitive perspective, operating at the edge of chaos is computationally optimal: the system is maximally sensitive to inputs while remaining stable enough to maintain coherent representations.

### 13.7 Complexity Beyond Computability: Interactive Proofs, Entanglement, and Meaning Verification

The relationship between complexity theory and language runs deeper than the Chomsky hierarchy of Chapter 4. Recent work at the intersection of quantum information theory and computational complexity has revealed a result of profound implications for the limits of formal systems: the proof by Ji, Natarajan, Vidick, Wright, and Yuen (2021) that $\text{MIP}^* = \text{RE}$.

To unpack this: $\text{MIP}^*$ (multi-prover interactive proof with quantum entanglement) is the class of problems that can be verified by a classical polynomial-time verifier interacting with multiple quantum-entangled provers. $\text{RE}$ (recursively enumerable) is the class of all problems whose yes-instances can be verified by a Turing machine — the broadest class in the classical hierarchy. The equality $\text{MIP}^* = \text{RE}$ means that quantum entanglement, shared between non-communicating provers, gives a polynomial-time verifier the power to verify any recursively enumerable problem. Since the halting problem is in $\text{RE}$ but undecidable, the verification protocol for $\text{MIP}^*$ is itself not computable.

Why does this matter for linguistics? **Communicative interaction is, in its idealized form, a multi-prover interactive proof.** Two interlocutors — speaker and hearer — are provers; the communicative act is a protocol; the meaning verified is the proposition conveyed. Classical communication theory (Shannon, 1948) assumes non-entangled provers. But the pragmatic literature (Grice, 1975; Sperber & Wilson, 1986; Frank & Goodman, 2012) has long recognized that human communication relies on *shared context*, *mutual knowledge*, and *common ground* in ways that go far beyond classical channel-passing.

Translating into complexity-theoretic terms: the shared cognitive context between interlocutors — the vast implicit knowledge of the world, the language, and conversational history — functions as a form of *pragmatic entanglement*. With full pragmatic entanglement, the class of propositions verifiable through communication becomes $\text{MIP}^*$ — that is, all of $\text{RE}$. But $\text{RE}$ includes the halting problem, which is undecidable. This implies that there exist communicative propositions whose verification through pragmatic reasoning is, in principle, undecidable.

This connects to Wittgenstein's insight (*Philosophical Investigations*) that "meaning is use" implies the space of meanings is as complex as the space of human practices — at least as complex as $\text{RE}$. Gödel's incompleteness theorem (1931) showed that formal arithmetic cannot be complete; the $\text{MIP}^* = \text{RE}$ result extends this incompleteness to the interactive verification of meaning. Yuen's broader program connects these results to the geometry of Chapters 9–11: the quantum correlations that make $\text{MIP}^*$ so powerful are described by operators in infinite-dimensional Hilbert space, and characterizing achievable strategies reduces to a geometric question about the topology of non-commutative convex bodies.

> The argument of this section is an **analogy**, and it should be read as one. $\text{MIP}^* = \text{RE}$ is a theorem about provers who share *quantum* entanglement and a verifier who runs a specific kind of protocol; "pragmatic entanglement" between interlocutors is a metaphor for shared context, not a quantum resource, and human conversation is not literally an interactive proof system. What the analogy legitimately suggests is a research question — *how much can shared background, rather than transmitted signal, expand what a conversation can establish?* — and a caution against assuming that meaning must be fully capturable by any single finite formal system. It does not by itself prove that linguistic meaning is uncomputable.
{.deep-dive: A note of caution}

The implication, if the analogy holds, is both humbling and exciting: the full complexity of linguistic meaning may be, in a precise sense, uncomputable. No finite formal system can capture it. This is not a counsel of despair — it is an invitation to take seriously the extra-formal dimensions of language: embodiment, sociality, history, and the irreducibly pragmatic.

### 13.8 Emergent Capabilities and the CAS View of Language Models

The CAS perspective also illuminates the behavior of large language models (LLMs). Wei et al. (2022) documented a striking phenomenon: as LLMs are scaled in parameters and training data, certain capabilities — multi-step arithmetic, chain-of-thought reasoning, language translation — appear to emerge *discontinuously*. Below a critical scale, a capability is absent; above it, the capability appears fully formed. This is a phase transition in the parameter-scale space. (Schaeffer, Miranda, and Koyejo (2023) caution that part of this apparent discontinuity is created by the choice of evaluation metric: all-or-nothing scores such as exact-match accuracy can turn smooth underlying improvement into a sudden jump. Which emergent abilities are genuine phase transitions remains an open question.)

From the Fisher information metric (§11.5), such phase transitions can be characterized geometrically: the loss landscape develops a new basin of attraction as scale increases, and the model's trajectory during training crosses a threshold where the representation manifold undergoes a topological phase transition in the sense of Chapter 10. The emergent capability corresponds to a new attractor in the high-dimensional representational space.

From a CAS perspective, this is exactly what we would expect. An LLM is a complex system — not in the biological or social sense, but in the mathematical sense: many interacting components, non-linear dynamics, and a high-dimensional state space. Like linguistic communities, it can exhibit critical phenomena. The "language" learned by an LLM is a CAS in miniature: a self-organized system of distributed representations that has adapted to the statistical structure of human language through a process analogous to evolutionary selection. This does not mean that LLMs understand language in the full pragmatic sense outlined in §13.7. The point is rather that attractors, phase transitions, critical exponents, and network topology provide a richer vocabulary for understanding LLM behavior than the classical computational framework alone.

**Bridge to Chapter 14.** The CAS perspective does not replace the logical, geometric, and categorical frameworks of the preceding chapters — it situates them within a larger story. The formal grammars of Chapter 4 are not the language; they are attractors in a dynamical system of language use. The manifolds of Chapters 9–11 are not static; they are momentary snapshots of a self-organizing process. The category theory of Chapter 12 provides the abstract skeleton; complexity science provides the flesh. In Chapter 14, we step back from all these frameworks to ask the philosophical question they collectively raise: what does it mean to give a mathematical account of something as deeply, irreducibly human as language?

### 13.9 Interactive Simulator: Exploring Language as a Complex System

The three-tab simulator below allows you to explore the core mathematical models introduced in this chapter. **Tab 1 (Agent-Based Model)** implements the Naming Game (Steels, 1995): watch lexical conventions emerge from the interactions of simple agents, and observe the S-shaped convergence curve and the power-law intermediate phase. **Tab 2 (Dynamics)** implements replicator dynamics with stochastic noise (Blythe & Croft, 2012): adjust the selection coefficient and noise level to see how they govern the transition from old to new linguistic forms. **Tab 3 (Construction Network)** implements a spreading-activation construction network (Goldberg, 1995) using Mandarin Chinese X-*shénme*-X constructions as a case study: activate a construction and watch entrenchment and activation spread through the network.

<div class="simulator-embed" style="width:100%;height:720px;border-radius:16px;overflow:hidden;margin:2.5rem 0;border:1px solid rgba(255,255,255,0.08);">
<iframe src="language_complexity_simulator.html" style="width:100%;height:100%;border:none;" loading="lazy" title="Language Complexity Simulator"></iframe>
</div>

*The simulator is fully interactive and runs in your browser. All computations are performed locally; no data is transmitted.*


# Chapter 14. Philosophical Reflections: What Does the Mathematics Tell Us About Language? {#ch14}

> The limits of formalization reveal the limits of understanding.
> — attributed to Gödel
{.epigraph}

### 14.1 The Plurality of Mathematical Representations

We have traversed a remarkable landscape: from set theory and logic, through probability and information theory, to linear algebra, geometry, and topology. Each framework captures some aspects of language brilliantly while remaining silent about others. This plurality is not a defect but a feature. Language itself is multi-faceted — simultaneously a biological capacity, a cognitive system, a social institution, and a formal structure.

### 14.2 The Discrete-Continuous Dialectic

Perhaps the deepest tension is between discrete and continuous representations. Language has both discrete aspects (phonemes, morphemes, syntactic categories, truth values) and continuous aspects (phonetic variation, semantic gradience, probabilistic expectation). The Transformer architecture is, arguably, the most successful bridge yet constructed: it takes discrete inputs (tokens) and processes them through continuous transformations that implicitly encode discrete structures. Understanding how discrete linguistic structure emerges from continuous neural computation is one of the great open problems.

### 14.3 Meaning as Geometry: A Philosophical Assessment

If the meaning of a word is a point in a high-dimensional space, and the meaning of a sentence is a trajectory through that space, what kind of "meaning" is this? It is not referential meaning (Frege) nor truth-conditional meaning (Tarski, Montague). It is something new: a relational, geometric meaning, defined not by what a word refers to but by how it relates to every other word. This has striking parallels with Wittgenstein's later philosophy — meaning as use. But the formalization also reveals limits: geometric proximity captures similarity of use, but not the grounding of meaning in embodied experience, social practice, and the physical world.

### 14.4 The Chinese Room, Revisited Geometrically

Searle's Chinese Room argument takes on new complexion when the "symbols" are not discrete tokens but points in a continuous geometric space. In the Chinese Room, relationships between symbols are purely syntactic. In a geometric language model, relationships are substantive — defined by distances, angles, and curvature that encode semantic content. Whether this geometric richness constitutes "understanding" is debatable, but it shows that internal representations are far richer than the discrete symbol strings Searle envisioned.

### 14.5 One Word, Many Mathematics

It is worth ending where the book began, with the English form *bank*. Each framework we have met gives it a different mathematical identity, and each identity makes a different question answerable:

<table class="tbl">
<tr><th>Framework</th><th>What <em>bank</em> becomes</th><th>The question it answers</th></tr>
<tr><td>Sets (Ch. 2)</td><td>Two lexical entries, or one form mapped to a set of senses</td><td>Is this one word or two?</td></tr>
<tr><td>Logic (Ch. 3)</td><td>Two predicates, $\mathrm{Bank}_1(x)$ and $\mathrm{Bank}_2(x)$</td><td>Under which reading is the sentence true?</td></tr>
<tr><td>Automata (Ch. 4)</td><td>A terminal symbol; ambiguity is two paths through the grammar</td><td>Which strings are well formed?</td></tr>
<tr><td>Graphs (Ch. 5)</td><td>A node whose attachments (<em>by the river</em>) select the sense</td><td>What depends on what?</td></tr>
<tr><td>Probability (Ch. 6)</td><td>A distribution over senses, updated by context</td><td>How likely is each reading here?</td></tr>
<tr><td>Vectors (Ch. 7–8)</td><td>A point, or a cloud of contextual points</td><td>Which words are similar, and how?</td></tr>
<tr><td>Geometry (Ch. 9, 11)</td><td>A region on a curved manifold, with sense "islands"</td><td>How far apart are the senses, and along what path?</td></tr>
<tr><td>Topology (Ch. 10)</td><td>A vertex bridging two otherwise separate components</td><td>How is the semantic space connected?</td></tr>
<tr><td>Categories (Ch. 12)</td><td>An object whose image under different functors differs</td><td>What is preserved across representations?</td></tr>
<tr><td>Complex systems (Ch. 13)</td><td>A form whose sense distribution drifts in a population</td><td>How did this come to be, and where is it going?</td></tr>
</table>

None of these identities is *the* meaning of *bank*. Together, they suggest that "meaning" names not a single mathematical object but a family of structures, each answering to a different practice of asking.

### 14.6 Future Directions

The CAS perspective of Chapter 13 reminds us that the mathematical frameworks surveyed in this book are not endpoints but attractors — stable patterns that emerge from the ongoing, self-organizing process of scientific inquiry, subject to the same phase transitions and emergent reorganizations that they describe. Several directions seem especially promising at this moment of convergence. Geometric and topological methods for analyzing LLM internals stand to benefit from the criticality framework of §13.6: measuring topological phase transitions at scale thresholds may make the emergence results of Wei et al. (2022) mathematically precise. Category-theoretic unification of formal and distributional semantics, cross-linguistic curvature and topology of representation spaces as windows into language universals, and information geometry of training dynamics all remain active frontiers. As new mathematical tools are developed and as language models become more interpretable, we can expect new chapters in this story — chapters that will deepen our understanding of both the mathematics of structure and the structure of human language.


<!-- part: Back Matter -->

# Selected Bibliography {#bibliography .unnumbered}

### Mathematical Background

Wigner, E.P. "The Unreasonable Effectiveness of Mathematics in the Natural Sciences." *Communications in Pure and Applied Mathematics*, 13(1):1–14, 1960.

### Foundational Texts

Partee, B.H., ter Meulen, A., and Wall, R.E. *Mathematical Methods in Linguistics.* Kluwer, 1990.

Kornai, A. *Mathematical Linguistics.* Springer, 2008.

Winter, Y. *Elements of Formal Semantics.* Edinburgh University Press, 2016.

### Logic and Formal Semantics

Frege, G. *Begriffsschrift, eine der arithmetischen nachgebildete Formelsprache des reinen Denkens.* Halle: Louis Nebert, 1879.

Montague, R. "The Proper Treatment of Quantification in Ordinary English." In Hintikka, J. et al. (eds.), *Approaches to Natural Language*, 221–242. Reidel, 1973.

Barwise, J. and Cooper, R. "Generalized Quantifiers and Natural Language." *Linguistics and Philosophy*, 4(2):159–219, 1981.

Kripke, S.A. "Semantic Considerations on Modal Logic." *Acta Philosophica Fennica*, 16:83–94, 1963.

Heim, I. and Kratzer, A. *Semantics in Generative Grammar.* Blackwell, 1998.

Grice, H.P. "Logic and Conversation." In Cole, P. and Morgan, J.L. (eds.), *Syntax and Semantics 3: Speech Acts*, 41–58. Academic Press, 1975.

Keenan, E.L. and Stavi, J. "A Semantic Characterization of Natural Language Determiners." *Linguistics and Philosophy*, 9(3):253–326, 1986.

### Phonology and Morphology

Jakobson, R., Fant, C.G.M., and Halle, M. *Preliminaries to Speech Analysis: The Distinctive Features and Their Correlates.* MIT Press, 1952.

Chomsky, N. and Halle, M. *The Sound Pattern of English.* Harper & Row, 1968.

Koskenniemi, K. *Two-Level Morphology: A General Computational Model for Word-Form Recognition and Production.* Ph.D. thesis, University of Helsinki, 1983.

### Formal Language Theory

Chomsky, N. *Syntactic Structures.* Mouton, 1957.

Shieber, S.M. "Evidence Against the Context-Freeness of Natural Language." *Linguistics and Philosophy*, 8(3):333–343, 1985.

Joshi, A.K. "Tree Adjoining Grammars." In Dowty, D.R. et al. (eds.), *Natural Language Parsing*, 206–250. Cambridge University Press, 1985.

Kaplan, R.M. and Kay, M. "Regular Models of Phonological Rule Systems." *Computational Linguistics*, 20(3):331–378, 1994.

### Probability and Information Theory

Zipf, G.K. *Human Behavior and the Principle of Least Effort.* Addison-Wesley, 1949.

Shannon, C.E. "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27:379–423, 1948.

Manning, C.D. and Schütze, H. *Foundations of Statistical Natural Language Processing.* MIT Press, 1999.

Frank, M.C. and Goodman, N.D. "Predicting Pragmatic Reasoning in Language Games." *Science*, 336(6084):998, 2012.

Cover, T.M. and Thomas, J.A. *Elements of Information Theory.* 2nd ed. Wiley, 2006.

Hale, J. "A Probabilistic Earley Parser as a Psycholinguistic Model." *Proceedings of NAACL*, 159–166, 2001.

Levy, R. "Expectation-Based Syntactic Comprehension." *Cognition*, 106(3):1126–1177, 2008.

Smith, N.J. and Levy, R. "The Effect of Word Predictability on Reading Time Is Logarithmic." *Cognition*, 128(3):302–319, 2013.

### Distributional Semantics and Lexical Resources

Harris, Z. "Distributional Structure." *Word*, 10(2–3):146–162, 1954.

Firth, J.R. *Papers in Linguistics 1934–1951.* Oxford University Press, 1957.

Miller, G.A. "WordNet: A Lexical Database for English." *Communications of the ACM*, 38(11):39–41, 1995.

Banarescu, L., Bonial, C., Cai, S., Georgescu, M., Griffitt, K., Hermjakob, U., Knight, K., Koehn, P., Palmer, M., and Schneider, N. "Abstract Meaning Representation for Sembanking." *Proceedings of the 7th Linguistic Annotation Workshop*, 178–186, 2013.

Gildea, D. and Jaeger, T.F. "Human Languages Order Information Efficiently." arXiv:1510.02823, 2015.

Futrell, R., Mahowald, K., and Gibson, E. "Large-Scale Evidence of Dependency Length Minimization in 37 Languages." *Proceedings of the National Academy of Sciences*, 112(33):10336–10341, 2015.

Levy, O. and Goldberg, Y. "Neural Word Embedding as Implicit Matrix Factorization." *Advances in Neural Information Processing Systems (NeurIPS)*, 2014.

Linzen, T. "Issues in Evaluating Semantic Spaces Using Word Analogies." *Proceedings of the 1st Workshop on Evaluating Vector-Space Representations for NLP*, 13–18, 2016.

van der Maaten, L. and Hinton, G. "Visualizing Data Using t-SNE." *Journal of Machine Learning Research*, 9:2579–2605, 2008.

Hsu, D., Kakade, S.M., and Zhang, T. "A Spectral Algorithm for Learning Hidden Markov Models." *Journal of Computer and System Sciences*, 78(5):1460–1480, 2012.

Cohen, S.B., Stratos, K., Collins, M., Foster, D.P., and Ungar, L. "Spectral Learning of Latent-Variable PCFGs." *Proceedings of the 50th Annual Meeting of the ACL*, 223–231, 2012.

Landauer, T.K. and Dumais, S.T. "A Solution to Plato's Problem: The Latent Semantic Analysis Theory of Acquisition, Induction, and Representation of Knowledge." *Psychological Review*, 104(2):211–240, 1997.

Mikolov, T., Chen, K., Corrado, G., and Dean, J. "Efficient Estimation of Word Representations in Vector Space." arXiv:1301.3781, 2013.

Pennington, J., Socher, R., and Manning, C.D. "GloVe: Global Vectors for Word Representation." *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 1532–1543, 2014.

Coecke, B., Sadrzadeh, M., and Clark, S. "Mathematical Foundations for a Compositional Distributional Model of Meaning." *Linguistic Analysis*, 36:345–384, 2010.

### Neural Networks and Transformers

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., and Polosukhin, I. "Attention Is All You Need." *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.

Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., and Olah, C. "Toy Models of Superposition." *Transformer Circuits Thread*, Anthropic, 2022.

Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., and Chen, W. "LoRA: Low-Rank Adaptation of Large Language Models." *International Conference on Learning Representations (ICLR)*, 2022.

Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., et al. "A Mathematical Framework for Transformer Circuits." *Transformer Circuits Thread*, Anthropic, 2021.

Hewitt, J. and Manning, C.D. "A Structural Probe for Finding Syntax in Word Representations." *Proceedings of NAACL-HLT*, 4129–4138, 2019.

Schaeffer, R., Miranda, B., and Koyejo, S. "Are Emergent Abilities of Large Language Models a Mirage?" *Advances in Neural Information Processing Systems (NeurIPS)*, 2023.

### Geometric and Topological Methods

Johnson, W.B. and Lindenstrauss, J. "Extensions of Lipschitz Mappings into a Hilbert Space." *Contemporary Mathematics*, 26:189–206, 1984.

Nickel, M. and Kiela, D. "Poincaré Embeddings for Learning Hierarchical Representations." *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.

Abramsky, S. and Brandenburger, A. "The Sheaf-Theoretic Structure of Non-Locality and Contextuality." *New Journal of Physics*, 13:113036, 2011.

Ethayarajh, K. "How Contextual Are Contextualized Word Representations? Understanding the Geometry of Hidden States." *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2019.

Amari, S. *Information Geometry and Its Applications.* Springer, 2016.

Carlsson, G. "Topology and Data." *Bulletin of the American Mathematical Society*, 46(2):255–308, 2009.

### Category Theory and Linguistics

Lambek, J. "The Mathematics of Sentence Structure." *American Mathematical Monthly*, 65(3):154–170, 1958.

Lambek, J. "Type Grammar Revisited." In Lecomte, A. et al. (eds.), *Logical Aspects of Computational Linguistics*, LNCS 1582, 1–27. Springer, 1999.

Coecke, B. and Kissinger, A. *Picturing Quantum Processes: A First Course in Quantum Theory and Diagrammatic Reasoning.* Cambridge University Press, 2017.

### Complex Adaptive Systems and Language Dynamics

Beckner, C., Blythe, R., Bybee, J., Christiansen, M.H., Croft, W., Ellis, N.C., Holland, J., Ke, J., Larsen-Freeman, D., and Schoenemann, T. "Language Is a Complex Adaptive System: Position Paper." *Language Learning*, 59(S1):1–26, 2009.

Holland, J.H. *Hidden Order: How Adaptation Builds Complexity.* Addison-Wesley, 1995.

Mitchell, M. *Complexity: A Guided Tour.* Oxford University Press, 2009.

Croft, W. *Explaining Language Change: An Evolutionary Approach.* Longman, 2000.

Croft, W. *Radical Construction Grammar: Syntactic Theory in Typological Perspective.* Oxford University Press, 2001.

Goldberg, A.E. *Constructions: A Construction Grammar Approach to Argument Structure.* University of Chicago Press, 1995.

Tomasello, M. *Constructing a Language: A Usage-Based Theory of Language Acquisition.* Harvard University Press, 2003.

Langacker, R.W. *Foundations of Cognitive Grammar, Vol. 1: Theoretical Prerequisites.* Stanford University Press, 1987.

Collins, A.M. and Loftus, E.F. "A Spreading-Activation Theory of Semantic Processing." *Psychological Review*, 82(6):407–428, 1975.

Steels, L. "A Self-Organizing Spatial Vocabulary." *Artificial Life*, 2(3):319–332, 1995.

Baronchelli, A., Felici, M., Loreto, V., Caglioti, E., and Steels, L. "Sharp Transition Towards Shared Vocabularies in Multi-Agent Systems." *Journal of Statistical Mechanics*, P06014, 2006.

Steels, L. "Modeling the Cultural Evolution of Language." *Physics of Life Reviews*, 8(4):339–356, 2011.

Blythe, R.A. and Croft, W. "S-curves and the Mechanisms of Propagation in Language Change." *Language*, 88(2):269–304, 2012.

Bak, P., Tang, C., and Wiesenfeld, K. "Self-Organized Criticality: An Explanation of the 1/f Noise." *Physical Review Letters*, 59(4):381–384, 1987.

Barabási, A.-L. and Albert, R. "Emergence of Scaling in Random Networks." *Science*, 286(5439):509–512, 1999.

Kello, C.T., Brown, G.D.A., Ferrer-i-Cancho, R., Holden, J.G., Linkenkaer-Hansen, K., Rhodes, T., and Van Orden, G.C. "Scaling Laws in Cognitive Sciences." *Trends in Cognitive Sciences*, 14(5):223–232, 2010.

Ji, Z., Natarajan, A., Vidick, T., Wright, J., and Yuen, H. "MIP* = RE." *Communications of the ACM*, 64(11):131–138, 2021.

Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Narang, S., Chowdhery, A., Roberts, A., Barham, P., Dean, J., Petrov, S., and Le, Q.V. "Emergent Abilities of Large Language Models." *Transactions on Machine Learning Research*, 2022.

Lund, H., Basso Fossali, P., Mazur, J., and Ollagnier-Beldame, M. (eds.) *Language Is a Complex Adaptive System: Explorations and Evidence.* Language Science Press, 2022.


# Appendix A. Mathematical Notation and Conventions {#appendix .unnumbered}

### Set Theory

$\in$ (element of), $\subseteq$ (subset), $\cup$ (union), $\cap$ (intersection), $\times$ (Cartesian product), $\varnothing$ (empty set), $|A|$ (cardinality), $\mathcal{P}(A)$ (power set), $f: A \to B$ (function from $A$ to $B$), $f \circ g$ (composition).

### Logic

$\lnot$ (negation), $\wedge$ (conjunction), $\vee$ (disjunction), $\to$ (implication), $\forall$ (universal quantifier), $\exists$ (existential quantifier), $\lambda$ (lambda abstraction), $\llbracket\cdot\rrbracket$ (semantic interpretation brackets).

### Probability and Information

$P(A)$ probability, $P(A \mid B)$ conditional probability, $\mathbb{E}[X]$ expectation, $H(X)$ entropy, $H(P,Q)$ cross-entropy, $\mathrm{KL}(P\|Q)$ Kullback–Leibler divergence, $\mathrm{PMI}(w,c)$ pointwise mutual information, $-\log_2 P(x)$ surprisal (bits).

### Linear Algebra

Vectors in bold ($\mathbf{v}$), matrices in capitals ($M$), scalars in lowercase ($a$). $\langle \mathbf{u}, \mathbf{v} \rangle$ inner product, $\|\mathbf{v}\|$ norm, $M^\top$ transpose, $M^{-1}$ inverse, $\det(M)$ determinant, $\mathrm{tr}(M)$ trace, $\lambda_i$ eigenvalues, $\sigma_i$ singular values.

### Topology and Geometry

$M$ manifold, $T_pM$ tangent space at $p$, $g$ Riemannian metric, $R_{ijkl}$ Riemann curvature tensor, $H_k(X)$ $k$th homology group, $\beta_k$ $k$th Betti number, $\gamma$ curve/geodesic, $\nabla$ connection/covariant derivative.
