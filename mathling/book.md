---
title: "The Geometry of Grammar"
subtitle: "A Mathematical Journey Through Language — From Logic to Manifolds"
author: "SHUK<u>AI</u> HSIEH"
affiliation: "Graduate Institute of Linguistics,
National Taiwan University"
date: "Draft — February 2026"
---

<!-- ═══════════════════════════════════════════════════════
     HOW TO USE THIS FILE
     ═══════════════════════════════════════════════════════
     
     1. Edit this Markdown file in any editor (VS Code, Obsidian, Typora…)
     2. Run:  bash build.sh
     3. Open: geometry_of_grammar.html
     
     CONVENTIONS:
     - # = Part dividers (rendered as nav group labels, not in body)
     - ## = Chapter titles (each becomes a nav entry + chapter block)
     - ### = Section titles within chapters
     - LaTeX math: $inline$ and $$display$$
     - {.epigraph} after a blockquote = styled epigraph
     - {.example} after a blockquote = centered example sentence
     - {.deep-dive} or {.deep-dive: Title} after a blockquote = deep-dive box (multi‑para OK)
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


<!-- part: Part I · Discrete Foundations -->

# Chapter 1. Why Mathematics for Linguists? {#ch1}

> "Language is a process of free creation; its laws and principles are fixed, but the manner in which the principles of generation are used is free and infinitely varied."
> — Noam Chomsky
{.epigraph}

### 1.1 The Unreasonable Effectiveness of Mathematics in Linguistics

In 1960, the physicist Eugene Wigner published a celebrated essay on "The Unreasonable Effectiveness of Mathematics in the Natural Sciences." He marveled at the fact that mathematical structures, developed for their own internal beauty, repeatedly turned out to describe the physical world with uncanny precision. Linguistics presents a parallel puzzle. Why should the same mathematical structures that describe symmetry groups in physics or topological spaces in pure mathematics also illuminate the structure of human language?

One answer is that language, like the physical world, exhibits structure at multiple scales — phonological patterns, morphological regularities, syntactic hierarchies, semantic compositionality, discourse coherence — and mathematics is, at its core, the science of structure. But the deeper answer may be that language occupies a unique position at the intersection of the biological, the cognitive, and the social. It is a finite system that generates infinite variety, a discrete symbolic system that encodes continuous meaning, a local process (one word after another) that creates global coherence. These tensions — finite vs. infinite, discrete vs. continuous, local vs. global — are precisely the tensions that different branches of mathematics have been developed to address.

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

> "A set is a Many that allows itself to be thought of as a One."
> — Georg Cantor
{.epigraph}

### 2.1 The Language of Sets

The most fundamental mathematical framework applied to language is set theory. When Ferdinand de Saussure distinguished between *langue* (the abstract language system) and *parole* (actual speech), he was implicitly invoking set-theoretic thinking: *langue* is a set of signs, each defined as a pairing of a signifier and a signified. When a phonologist defines the vowel inventory of a language, they are specifying a set. When a morphologist lists the inflectional paradigm of a verb, they are constructing a function from a set of feature bundles to a set of forms.

Formally, a set is simply a collection of distinct objects, called elements or members. We write $a \in A$ to mean that $a$ is an element of set $A$. The power of set theory lies not in this simple definition but in the operations and relations we can define on sets: union ($\cup$), intersection ($\cap$), complement, Cartesian product ($\times$), and the critical notion of a function as a special kind of relation.

### 2.2 Phonological Feature Systems as Set Theory

One of the earliest and most elegant applications of set theory in linguistics is the distinctive feature theory of Jakobson, Fant, and Halle (1952), later refined by Chomsky and Halle (1968) in *The Sound Pattern of English*. In this framework, each phoneme is characterized by a set of binary features. For example, the English consonant /p/ can be described as:

$$\text{/p/} = \{[{+}\text{consonantal}],\; [{-}\text{sonorant}],\; [{-}\text{continuant}],\; [{-}\text{voiced}],\; [{+}\text{labial}]\}$$

The natural classes of phonology — the groups of sounds that behave alike in phonological rules — correspond to the intersections of feature sets. The class of voiceless stops $\{p, t, k\}$ is simply the intersection of sounds that are $[{-}\text{voiced}]$ and $[{-}\text{continuant}]$.

This set-theoretic perspective has profound consequences. It predicts that not all arbitrary groupings of phonemes should function as natural classes in phonological rules; only those groupings that can be defined by the intersection of feature specifications should do so. This prediction is largely confirmed by cross-linguistic data, which constitutes evidence that the feature system reflects something real about the cognitive representation of speech sounds.

### 2.3 Relations: From Paradigms to Hierarchies

A relation $R$ on a set $A$ is a subset of the Cartesian product $A \times A$. Different types of relations — reflexive, symmetric, transitive, antisymmetric — model different kinds of linguistic structure. Equivalence relations (reflexive, symmetric, transitive) partition a set into equivalence classes, which is exactly what paradigmatic relations do in morphology: the set of all noun forms in Latin can be partitioned into declension classes, where each class groups nouns that follow the same inflectional pattern.

Partial orders (reflexive, antisymmetric, transitive) model hierarchical structures. The hyponymy (is-a) relation in lexical semantics forms a partial order: "dog" is a hyponym of "animal," which is a hyponym of "living thing." This gives rise to a lattice structure that has been formalized in frameworks like WordNet (Miller, 1995). The feature geometry of phonology, in which features are organized into a hierarchical tree, is another linguistic instantiation of a partial order.

### 2.4 Functions and Compositionality

A function $f: A \to B$ assigns to each element of set $A$ exactly one element of set $B$. Functions are central to formal semantics, where the meaning of a complex expression is a function of the meanings of its parts. In Montague's framework, which we will explore in detail in Chapter 3, the meaning of a verb phrase like "runs quickly" is computed by applying the function denoted by the adverb "quickly" to the function denoted by "runs." The entire enterprise of compositional semantics rests on the mathematical notion of function composition.

The concept of a function also underlies the structuralist notion of paradigmatic substitution. Two expressions belong to the same syntactic category if they can substitute for each other in the same contexts — that is, if they have the same domain and range when viewed as functions from left contexts to right contexts. This insight, formalized by Zellig Harris and later by the categorial grammarians, connects set-theoretic function spaces directly to syntactic categories.

### 2.5 Limitations and the Road Ahead

Set theory provides a powerful vocabulary for describing the static architecture of language — its inventories, categories, and relations. But it says relatively little about the dynamic processes that operate over these structures: how sounds change in context, how sentences are generated, how meanings are computed. For this, we need the more expressive frameworks of logic and algebra, to which we turn in the next chapters. Nevertheless, set theory remains the lingua franca of all subsequent formalisms; every mathematical framework we encounter will be built on its foundations.


# Chapter 3. Logic and the Formal Semantics of Natural Language {#ch3}

> "The limits of my language mean the limits of my world."
> — Ludwig Wittgenstein
{.epigraph}

### 3.1 From Aristotle to Montague: Logic as the Language of Meaning

The application of logic to natural language has a pedigree stretching back to Aristotle's syllogistic. But the modern era begins with Gottlob Frege's *Begriffsschrift* (1879), which introduced predicate logic — a formal language powerful enough to express quantificational statements like "Every linguist admires some mathematician." Frege's insight was that natural language sentences have an internal logical structure that is obscured by their surface form. The sentence "Every linguist admires some mathematician" is ambiguous between two readings:

$$\forall x\bigl[\mathrm{Linguist}(x) \to \exists y[\mathrm{Mathematician}(y) \wedge \mathrm{Admires}(x,y)]\bigr]$$

$$\exists y\bigl[\mathrm{Mathematician}(y) \wedge \forall x[\mathrm{Linguist}(x) \to \mathrm{Admires}(x,y)]\bigr]$$

These differ in the relative scope of the universal and existential quantifiers — a distinction that has profound semantic consequences but is invisible in the surface syntax.

### 3.2 Propositional Logic: The Simplest Fragment

Propositional logic deals with sentences that are either true or false and the connectives that combine them: negation ($\lnot$), conjunction ($\wedge$), disjunction ($\vee$), implication ($\to$), and biconditional ($\leftrightarrow$). In natural language, these correspond (imperfectly) to "not," "and," "or," "if...then," and "if and only if." The imperfection of this correspondence has been one of the great generative puzzles of formal pragmatics. Natural language "or" is typically exclusive in conversational contexts ("You can have coffee or tea"), whereas logical $\vee$ is inclusive. Natural language "if...then" carries presuppositions and conversational implicatures that the material conditional $\to$ does not.

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

### 3.4 Lambda Calculus: The Glue of Compositionality

The lambda calculus, invented by Alonzo Church in the 1930s, provides a notation for defining and applying functions. In formal semantics, it serves as the "glue" that combines word meanings into phrase meanings. The transitive verb "loves" can be represented as $\lambda x.\lambda y.\,\mathrm{Loves}(y, x)$. To compute the meaning of "loves Mary," we perform $\beta$-reduction:

$$(\lambda x.\lambda y.\,\mathrm{Loves}(y, x))(\mathrm{Mary}) = \lambda y.\,\mathrm{Loves}(y, \mathrm{Mary})$$

This resulting expression, a function from individuals to truth values, is the meaning of the verb phrase "loves Mary."

Lambda abstraction also handles more complex phenomena like relative clauses. The relative clause "who loves Mary" denotes the set of individuals who love Mary, represented as $\lambda x.\,\mathrm{Loves}(x, \mathrm{Mary})$. When this combines with a common noun like "man," the result is the intersection of two sets:

$$\lambda x\bigl[\mathrm{Man}(x) \wedge \mathrm{Loves}(x, \mathrm{Mary})\bigr]$$

The mathematical elegance is striking: set intersection, function application, and variable binding conspire to produce the correct meanings for arbitrarily complex constructions.

### 3.5 Modal Logic and Possible Worlds

Natural language is saturated with modality: "must," "might," "can," "should," "necessarily," "possibly." Modal logic extends classical logic with operators $\Box$ (necessarily) and $\Diamond$ (possibly), interpreted over a set of possible worlds connected by an accessibility relation. The sentence "John might be a spy" is true in the actual world if there exists an accessible possible world in which John is a spy.

The possible-worlds framework has been enormously productive in formal semantics. It provides analyses of conditionals ("If kangaroos had no tails, they would topple over" requires evaluating a counterfactual scenario), attitude verbs ("John believes that it is raining" involves John's belief worlds), and tense ("John will arrive" involves quantification over future times). The mathematical structure — a Kripke frame $\langle W, R, V \rangle$ (Kripke, 1963) consisting of a set of worlds $W$, an accessibility relation $R \subseteq W \times W$, and a valuation function $V$ — is another instance of the relational structures introduced in Chapter 2.

### 3.6 Beyond First-Order Logic: Generalized Quantifiers

Natural language quantification goes far beyond "every" and "some." Determiners like "most," "few," "more than half," and "exactly three" cannot be expressed in first-order predicate logic. The theory of generalized quantifiers, developed by Barwise and Cooper (1981), treats determiners as relations between sets:

- **Every:** $\llbracket\text{every}\rrbracket(A)(B) = 1 \iff A \subseteq B$
- **Most:** $\llbracket\text{most}\rrbracket(A)(B) = 1 \iff |A \cap B| > |A \setminus B|$
- **No:** $\llbracket\text{no}\rrbracket(A)(B) = 1 \iff A \cap B = \varnothing$
- **Exactly $n$:** $\llbracket\text{exactly } n\rrbracket(A)(B) = 1 \iff |A \cap B| = n$

The generalized quantifier framework revealed a remarkable cross-linguistic universal: natural language determiners are **conservative**, meaning that $D(A)(B) \Leftrightarrow D(A)(A \cap B)$. This conservativity universal, which holds across all known languages, is a mathematical constraint on the space of possible human languages — one of the most striking examples of mathematics illuminating a linguistic universal.

### 3.7 Limitations of Logic-Based Approaches

For all its elegance, the logical approach to semantics faces persistent challenges. Vagueness ("John is tall"), gradience ("This sentence is grammatical"), context-dependence ("enough" for what purpose?), metaphor ("Time flies"), and the open-endedness of word meaning all sit uneasily within the crisp, binary framework of classical logic. These challenges have motivated extensions — fuzzy logic, degree semantics, dynamic semantics, situation semantics — but they have also motivated a fundamentally different mathematical approach: the geometric and probabilistic frameworks of Parts II and III. The tension between the compositional precision of logic and the flexible gradience of actual language use is, arguably, the central tension in the mathematical study of meaning.


# Chapter 4. Formal Languages, Automata, and the Chomsky Hierarchy {#ch4}

> "Colorless green ideas sleep furiously."
> — Noam Chomsky
{.epigraph}

### 4.1 The Generative Enterprise

In 1957, Noam Chomsky published *Syntactic Structures*, inaugurating a revolution in linguistics whose mathematical foundations remain central to the field. Chomsky's key insight was that a language can be defined as a set of strings generated by a formal grammar — a finite set of rules that recursively produce an infinite set of well-formed expressions. This perspective connects linguistics directly to the mathematical theory of computation developed by Turing, Post, and Kleene.

A formal grammar $G$ is a tuple $\langle V, \Sigma, R, S \rangle$ where $V$ is a finite set of non-terminal symbols, $\Sigma$ is a finite set of terminal symbols (the alphabet), $R$ is a finite set of production rules, and $S \in V$ is the start symbol. The language $L(G)$ generated by $G$ is the set of all strings of terminal symbols derivable from $S$ by repeated application of rules in $R$.

### 4.2 The Chomsky Hierarchy

The Chomsky hierarchy classifies formal grammars by the form of their production rules, yielding four types of increasing generative power. Type 3 (regular) grammars, equivalent to finite-state automata, generate languages like $a^n$. Type 2 (context-free) grammars, equivalent to pushdown automata, generate languages like $a^n b^n$ that require matching dependencies. Type 1 (context-sensitive) grammars and Type 0 (unrestricted) grammars are progressively more powerful, with Type 0 equivalent to Turing machines.

The burning question in mathematical linguistics has been: where does natural language fall in this hierarchy? Chomsky argued early on that natural languages are not regular — that is, they cannot be generated by finite-state grammars. His famous example involved center-embedding: English allows sentences like "The cat the dog the rat bit chased ran," which requires tracking nested dependencies (cat-ran, dog-chased, rat-bit) that a finite-state device cannot handle.

### 4.3 Beyond Context-Free: Mildly Context-Sensitive Languages

In 1985, Stuart Shieber (1985) demonstrated that the cross-serial dependencies found in Swiss German — where accusative and dative objects must be matched with their respective verbs in a crossing pattern — cannot be generated by any context-free grammar. This established that natural languages are at least mildly context-sensitive. The term was coined by Aravind Joshi to describe a class of grammars — including Tree-Adjoining Grammars (TAGs), Combinatory Categorial Grammars (CCGs), and Linear Indexed Grammars — that are slightly more powerful than context-free grammars but far less powerful than full context-sensitive grammars.

The mildly context-sensitive languages have several attractive properties: they can generate the cross-serial dependencies found in natural language, they have polynomial parsing complexity, and their structural descriptions are trees (or mildly enriched trees). Joshi conjectured that human languages are exactly the class of mildly context-sensitive languages — a mathematical hypothesis about the computational complexity of Universal Grammar.

### 4.4 Finite-State Methods in Phonology and Morphology

While syntax required context-free or mildly context-sensitive power, phonology and morphology turned out to be well-modeled by the weakest class in the hierarchy: regular languages and finite-state transducers. The insight, formalized by Ronald Kaplan and Martin Kay (1994), was that most phonological rules can be compiled into finite-state transducers — devices that read an input string and produce an output string, operating with bounded memory.

In morphology, finite-state methods proved extraordinarily successful. Kimmo Koskenniemi's two-level morphology (1983) modeled the relationship between underlying and surface forms of words as a set of parallel finite-state constraints. This approach could handle the complex morphological phenomena of agglutinative languages like Finnish and Turkish, and it led to the development of practical morphological analyzers for dozens of languages.

### 4.5 Automata as Cognitive Models

The connection between automata and cognition runs deeper than analogy. The finite-state hypothesis in psycholinguistics — that human sentence processing operates with finite memory and is thus fundamentally finite-state in nature — has been both defended and attacked. While the unbounded recursive power of human syntax argues against strict finite-state processing, psycholinguistic evidence shows that deeply center-embedded sentences are effectively unprocessable, suggesting that the human parser operates within a bounded region of the Chomsky hierarchy in practice.

This tension between competence (what the grammar can generate in principle) and performance (what the processor can handle in practice) maps directly onto the mathematical distinction between different levels of the hierarchy. It is a tension that will resurface throughout this book, particularly when we encounter neural network language models that are, in principle, finite-state machines (bounded by their parameter count) but that approximate the behavior of more powerful computational devices.


# Chapter 5. Graphs, Trees, and Linguistic Structure {#ch5}

> "The branching tree of possibilities is the deepest picture of reality."
> — David Deutsch
{.epigraph}

### 5.1 Trees: The Canonical Representation of Syntax

If there is a single mathematical object that symbolizes modern linguistics, it is the tree. From Chomsky's phrase structure trees to dependency trees, from phonological prosodic trees to semantic type-driven derivation trees, the tree diagram is ubiquitous. Mathematically, a tree is a connected acyclic graph — a set of nodes connected by edges such that there is exactly one path between any two nodes.

### 5.2 Dependency Graphs

An alternative to phrase structure is dependency grammar, whose mathematical formalization uses directed graphs rather than constituent trees. In a dependency tree, each word is a node, and directed edges connect heads to their dependents. Dependency trees and phrase structure trees are mathematically related but not equivalent. Dependency parsing has become dominant in computational linguistics, partly because dependency trees are easier to learn from data and partly because they generalize more naturally across typologically diverse languages.

### 5.3 Graphs Beyond Trees: Semantic and Discourse Structure

While syntax is largely tree-structured, other levels of linguistic analysis require the full generality of graphs. Semantic representations often involve directed acyclic graphs (DAGs) or even cyclic graphs. Abstract Meaning Representation (AMR; Banarescu et al., 2013) uses rooted DAGs to represent the meaning of sentences, allowing reentrancy — the same entity participating in multiple semantic roles.

### 5.4 Graph Properties and Linguistic Universals

The mathematical properties of linguistic graphs encode substantive linguistic claims. The projectivity of dependency trees — the requirement that dependency arcs do not cross when the words are laid out in linear order — corresponds to a constraint on word-order freedom. Graph-theoretic measures like average dependency length have been shown to correlate with processing difficulty. Dependency Length Minimization (Gildea & Jaeger, 2015), the tendency for languages to prefer shorter dependencies, has been documented across dozens of languages and appears to be a genuine universal, explicable as an optimization strategy for the human parser.


<!-- part: Part II · Probabilistic & Algebraic Turn -->

# Chapter 6. Probability, Information, and the Statistics of Language {#ch6}

> "Whenever I fire a linguist, the performance of the speech recognizer goes up."
> — Frederick Jelinek (attrib.)
{.epigraph}

### 6.1 The Probabilistic Turn

For much of the twentieth century, the dominant paradigm in theoretical linguistics was categorical: a sentence was either grammatical or ungrammatical. Chomsky famously argued that probabilistic models were inappropriate for natural language, observing that "Colorless green ideas sleep furiously" and "Furiously sleep ideas green colorless" are equally improbable, yet only the first is grammatical. The counter-revolution came from both computational linguistics and sociolinguistics.

### 6.2 Probability Distributions over Linguistic Objects

A probability distribution over a set $\Omega$ assigns a non-negative real number $P(\omega)$ to each element $\omega \in \Omega$ such that the probabilities sum to 1. In language modeling, $\Omega$ is the set of all possible sentences, and $P$ assigns to each sentence its probability of occurrence. The simplest language model is the $n$-gram model, which approximates the probability of a word given its entire history by conditioning only on the previous $n{-}1$ words:

$$P(w_i \mid w_1, \ldots, w_{i-1}) \approx P(w_i \mid w_{i-n+1}, \ldots, w_{i-1})$$

### 6.3 Information Theory and Language

Claude Shannon's information theory (1948) provides a mathematical framework for quantifying the information content of linguistic messages. The entropy of a random variable $X$ is defined as:

$$H(X) = -\sum_{x} P(x) \log_2 P(x)$$

This measures the average surprise associated with outcomes. The entropy of English is approximately 1.0 to 1.5 bits per character — meaning that each character carries about one bit of information, far less than the $\log_2(26) \approx 4.7$ bits that a uniformly random letter would carry. This redundancy provides robustness against noise and facilitates prediction.

### 6.4 Bayesian Approaches to Language

Bayes' theorem provides a principled framework for updating beliefs in light of evidence:

$$P(H \mid D) = \frac{P(D \mid H)\,P(H)}{P(D)}$$

Bayesian approaches have been applied to language acquisition, syntactic parsing, pragmatic reasoning (the Rational Speech Acts framework (Frank & Goodman, 2012)), and historical linguistics (Bayesian phylogenetics of language families).

### 6.5 Zipf's Law and the Statistics of the Lexicon

One of the most striking statistical regularities of language is Zipf's law (Zipf, 1949): if the words of a language are ranked by frequency, the frequency of the $r$th-ranked word is approximately proportional to $1/r$:

$$f(r) \propto \frac{1}{r^\alpha}, \quad \alpha \approx 1$$

This power-law distribution means that a small number of words ("the," "of," "and") account for a large fraction of all word tokens, while the vast majority of word types occur rarely. Zipf's law has been documented across all studied languages and extends to other linguistic units.


# Chapter 7. Linear Algebra: The Vector Space of Language {#ch7}

> "You shall know a word by the company it keeps."
> — J.R. Firth
{.epigraph}

### 7.1 The Distributional Hypothesis

The idea that the meaning of a word can be inferred from its patterns of co-occurrence — the distributional hypothesis — was articulated by Harris (1954) and Firth (1957) and has become one of the most productive ideas in computational linguistics. Its mathematical realization requires linear algebra: words become vectors, contexts become dimensions, and meaning becomes geometry.

### 7.2 Vectors, Matrices, and the Algebra of Meaning

A vector space $V$ over a field $F$ (typically $\mathbb{R}$) is a set equipped with two operations — vector addition and scalar multiplication — satisfying certain axioms. The key concepts for linguistic applications are:

- **Dot product:** $\langle \mathbf{u}, \mathbf{v} \rangle = \sum_i u_i\, v_i$ — measures alignment
- **Norm:** $\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$ — measures magnitude
- **Cosine similarity:** $\cos(\theta) = \dfrac{\langle \mathbf{u}, \mathbf{v} \rangle}{\|\mathbf{u}\| \cdot \|\mathbf{v}\|}$ — measures angle, independent of magnitude

In the word-vector space, cosine similarity becomes a measure of semantic similarity. The vectors for "dog" and "cat" will have high cosine similarity because they occur in similar contexts, while "dog" and "democracy" will have low cosine similarity. This is remarkable: a purely mathematical operation on co-occurrence counts recovers something that looks very much like human semantic intuition.

### 7.3 Dimensionality Reduction: SVD and the Latent Structure of Meaning

Raw word-context matrices are enormous and sparse. Singular Value Decomposition (SVD) provides a principled method for reducing their dimensionality while preserving the most important patterns. Given a matrix $M$ of rank $r$, SVD factorizes it as:

$$M = U \Sigma V^\top$$

where $U$ and $V$ are orthogonal matrices and $\Sigma = \mathrm{diag}(\sigma_1, \ldots, \sigma_r)$ is a diagonal matrix of singular values. By retaining only the $k$ largest singular values ($k \ll r$), we obtain a low-rank approximation $M_k = U_k \Sigma_k V_k^\top$ that captures the dominant latent structure. Latent Semantic Analysis (LSA), introduced by Landauer and Dumais (1997), applied SVD to word-document matrices and demonstrated that the resulting low-dimensional representations captured semantic relationships not present in the original counts.

### 7.4 Word Embeddings: From Counting to Prediction

Word2Vec (Mikolov et al., 2013) and GloVe (Pennington et al., 2014) learned word vectors by training neural networks to predict context. The resulting embeddings exhibited striking algebraic properties — vector arithmetic encoded semantic relationships:

$$\vec{v}_{\text{king}} - \vec{v}_{\text{man}} + \vec{v}_{\text{woman}} \approx \vec{v}_{\text{queen}}$$

This showed that vector offsets captured relational structure — different directions correspond to different semantic relations (gender, tense, plurality, etc.).

### 7.5 Tensor Products and Compositional Distributional Semantics

The Categorical Compositional Distributional (DisCoCat) framework of Coecke, Sadrzadeh, and Clark (2010) addresses compositionality by representing relational words as tensors. A transitive verb like "loves" is represented as a rank-3 tensor $\mathcal{T} \in V \otimes V \otimes V$. The meaning of "John loves Mary" is computed by tensor contraction:

$$\llbracket\text{John loves Mary}\rrbracket_k = \sum_{i,j} \mathcal{T}_{ijk} \cdot \vec{v}_{\text{John},\,i} \cdot \vec{v}_{\text{Mary},\,j}$$

This approach elegantly combines the compositional structure of formal semantics with the distributional content of vector space models.

### 7.6 Linear Algebra in Syntax: Spectral Methods

Linear algebra serves as a bridge between the discrete, symbolic representations of classical linguistics and the continuous, distributed representations of modern computational linguistics. A discrete grammar generates trees; these trees give rise to distributional statistics; these statistics live in a vector space; and the structure of that vector space reflects the structure of the underlying grammar. Linear algebra is the mathematical framework that makes this connection precise.


# Chapter 8. Neural Networks and the Mathematics of Learned Representations {#ch8}

> "What I cannot create, I do not understand."
> — Richard Feynman
{.epigraph}

### 8.1 From Perceptrons to Transformers

The neural network revolution in linguistics can be told as a mathematical story of progressive enrichment. Each architecture can be described precisely in linear-algebraic terms. A single Transformer attention head computes:

$$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V$$

where $Q = XW^Q$, $K = XW^K$, $V = XW^V$ are linear projections of the input $X$, and $d_k$ is the dimensionality of the key vectors. The entire Transformer is a composition of attention layers interspersed with position-wise feed-forward networks, layer normalization, and residual connections.

### 8.2 The Geometry of the Residual Stream

A key insight from mechanistic interpretability research is that the Transformer can be understood as performing successive geometric transformations on a high-dimensional vector representing each token. The residual stream — the sequence of vectors that flows through the network — can be thought of as a trajectory through a high-dimensional space. Different layers perform different kinds of operations: early layers encode local syntactic relationships, middle layers encode more global syntactic and semantic relationships, and late layers encode distributional information needed for prediction.

### 8.3 Attention as Soft Graph Construction

The attention mechanism has a beautiful interpretation in terms of graph theory. Each attention head defines a weighted directed graph over the tokens, where the edge weight from token $i$ to token $j$ is the attention weight $\alpha_{ij}$. Different heads learn to construct different graphs: some attend to the syntactically adjacent word, others to the head of the current phrase, others to the subject of the sentence. Transformers are, among other things, soft structure-learning machines.

### 8.4 Superposition and the Geometry of Features

Networks represent more features than they have dimensions, by encoding features as nearly orthogonal directions in a space that is too small to accommodate them all as exactly orthogonal dimensions. This phenomenon has deep connections to compressed sensing and the Johnson-Lindenstrauss lemma (Johnson & Lindenstrauss, 1984). The mathematics of superposition suggests that neural networks exploit the geometry of high-dimensional spaces — in particular, the fact that high-dimensional spaces admit exponentially many nearly orthogonal directions — to pack a vast amount of linguistic knowledge into a finite-dimensional representation.


<!-- part: Part III · The Geometric Turn -->

# Chapter 9. The Geometry of Meaning: Manifolds in Semantic Space {#ch9}

> "Geometry is the art of correct reasoning from incorrectly drawn figures."
> — Henri Poincaré
{.epigraph}

### 9.1 From Vector Spaces to Manifolds

The vector space models of Chapter 7 treat semantic space as flat — a Euclidean space where distances are measured with the familiar straight-line metric. But there are compelling reasons to believe that the geometry of meaning is curved. Consider the hierarchical structure of concepts: "animal" encompasses "mammal," which encompasses "dog," which encompasses "poodle." This tree-like structure cannot be faithfully embedded in Euclidean space without distortion, but it can be naturally embedded in hyperbolic space, where the volume of a ball grows exponentially with its radius — just as the number of nodes in a tree grows exponentially with depth.

A manifold is a topological space that locally resembles Euclidean space but may have a different global structure. The surface of the Earth is a two-dimensional manifold: locally, it looks flat (which is why flat maps work for small regions), but globally it is curved (which is why no flat map of the whole Earth can avoid distortion). The **manifold hypothesis** in machine learning proposes that high-dimensional data lies on or near a low-dimensional manifold embedded in the ambient high-dimensional space.

### 9.2 Hyperbolic Geometry and Lexical Hierarchies

Nickel and Kiela (2017) demonstrated that embedding the WordNet hierarchy in hyperbolic space produced far better representations than Euclidean embeddings of the same dimensionality. In just two hyperbolic dimensions, they could embed a hierarchy that required hundreds of Euclidean dimensions. The mathematical reason is elegant: a tree with branching factor $b$ has $O(b^n)$ nodes at depth $n$. The volume of a hyperbolic ball of radius $r$ also grows exponentially:

$$\mathrm{Vol}_{\mathbb{H}^d}(r) \propto e^{(d-1)\,r}$$

so there is a natural correspondence between tree depth and hyperbolic distance. In contrast, Euclidean volume grows only polynomially ($\propto r^d$), creating a mismatch with tree structure.

### 9.3 Poincaré Embeddings and Lexical Entailment

Hyperbolic embeddings have been extended to model lexical entailment — where the meaning of one word is contained in another. More broadly, the choice of geometric space becomes a modeling decision with linguistic content. Euclidean space $\mathbb{E}^n$ is appropriate for symmetric similarity. Hyperbolic space $\mathbb{H}^n$ is appropriate for hierarchies. Spherical space $\mathbb{S}^n$ may be appropriate for cyclical structures. And product spaces $\mathbb{H}^{n_1} \times \mathbb{S}^{n_2} \times \mathbb{E}^{n_3}$ may be needed for the complex mixture of relations found in natural language semantics.

### 9.4 The Manifold Hypothesis in Language Models

Recent work has shown that the token representations in Transformer models lie on manifolds whose intrinsic dimensionality is much lower than the ambient dimensionality. Different linguistic properties correspond to different geometric features: syntactic information tends to be encoded in linear subspace structure, while semantic information is encoded in nonlinear manifold geometry (curvature, topology). This distinction parallels the distinction between syntax and semantics in traditional linguistics.

### 9.5 Contextual Embeddings and the Geometry of Polysemy

Ethayarajh (2019) showed that contextual embeddings occupy a narrow cone in high-dimensional space. Different senses of a polysemous word occupy different regions of this cone, and the degree of separation varies across layers. In early layers, senses are close together; in middle layers, they are maximally separated; in later layers, they may reconverge. This layer-wise geometry of polysemy resolution is a window into how neural networks process lexical ambiguity.


# Chapter 10. Topology and the Shape of Linguistic Spaces {#ch10}

> "A topologist is a person who cannot distinguish a coffee cup from a doughnut."
> — Mathematical folklore
{.epigraph}


![](./figures/topology.png)


### 10.1 What Topology Offers Linguistics

Topology studies properties preserved under continuous deformation — stretching, bending, and twisting, but not tearing or gluing. While geometry cares about distances and angles, topology cares about connectivity, holes, and the overall "shape" of a space. For linguistics, topology offers tools for asking questions that geometry cannot: Does the space of word meanings have holes? Do the internal representations of language models have a characteristic topological signature?


### 10.2 Basic Topological Concepts

A linguistically intuitive example: consider the semantic space of color terms. In a language with basic color terms arranged around the color wheel, the topology has a characteristic one-dimensional hole — you can traverse the color terms (red → orange → yellow → green → blue → purple → red) and return to your starting point, forming a loop that cannot be contracted to a point. This loop is a topological feature that exists regardless of how we stretch or deform the space.


> 在語義學中，傳統的向量空間（幾何）告訴我們詞與詞之間的「距離」，但拓撲學（Topology）則揭示了語義結構的「連通性」與「形狀」。在加入拓撲學深度後，不僅涵蓋了語言的「量」（機率與向量），更觸及了語言的「質」與「結構」。
>
> 專題章節，深入探討**持久同調（Persistent Homology）與單體複形（Simplicial Complexes）**在語義空間中的數學意義，
{.deep-dive}
<!-- {.deep-dive: Deep Dive: The Topological Turn in Semantics} -->



- From Pairs to Simplices

In vector semantics, we focus on pairwise relationships (the edge between two words). However, language often involves higher-order dependencies. A "context" is not just a pair of words, but a group of words that together form a coherent meaning.

Mathematically, we represent this using a Simplicial Complex $K$.

  - A 0-simplex is a single word: $[w_i]$.
  
  - A 1-simplex is a relationship between two words: $[w_i, w_j]$.
  
  - A 2-simplex is a filled triangle representing a 3-way semantic coherence: $[w_i, w_j, w_k]$.

Linguistic Example:

Consider the words {Bank, River, Money, Interest}.

- {Bank, River} share a 1-simplex in a geographical context.
 
- {Bank, Money, Interest} share a 2-simplex in a financial context.
  
- Crucially, {River, Money} might not share an edge. This "missing edge" prevents the formation of a 3-way simplex, defining the boundaries of semantic domains.

- Homology and Lexical Gaps

Topology allows us to calculate Betti numbers ($\beta_n$), which count the "holes" in a space.

$\beta_0$: Number of connected components (isolated semantic clusters).

$\beta_1$: Number of 1-dimensional "tunnels" or cycles.

In a semantic manifold, a hole ($\beta_1 > 0$) represents a Lexical Gap. It is a conceptual region surrounded by words, yet empty at its center.

Example: Imagine words describing "warmth," "hot," and "burning," and another set describing "affection," "passion," and "desire." If these clusters circle around a central concept that the language has no specific word for (e.g., a specific type of spiritual heat), the topology of the lexicon will literally show a hole.

- Persistent Homology: The Evolution of Meaning

How do we know if a hole is "real" or just noise? We use Persistent Homology. We grow "balls" of radius $\epsilon$ around each word vector.

As $\epsilon$ increases, words connect to form edges, then triangles.
We track the "birth" and "death" of topological features (holes).

Linguistic Insight: Robust semantic structures "persist" over a long range of $\epsilon$, while accidental associations disappear quickly. This gives us a "barcode" of a language's conceptual DNA.

- Mathematical Derivation: The Boundary Operator
To find these holes, we define a boundary operator $\partial_n$:

$$\partial_n([v_0, \dots, v_n]) = \sum_{i=0}^{n} (-1)^i [v_0, \dots, \hat{v}_i, \dots, v_n]$$

The cycles that are not boundaries ($Z_n / B_n$) form the Homology Group $H_n$. For linguists, $H_n$ is the mathematical signature of what a language cannot say, or chooses not to group together.



### 10.3 Persistent Homology and Word Embedding Topology

Persistent homology tracks how topological features appear and disappear as we vary a scale parameter. Given a set of points (such as word embeddings), we build a family of simplicial complexes indexed by a distance threshold $\varepsilon$: at each threshold, we connect points that are within distance $\varepsilon$ of each other. As $\varepsilon$ increases from $0$ to $\infty$, topological features are "born" (when new connections create loops or voids) and "die" (when those features are filled in). The persistence diagram — which plots each feature's birth time $b_i$ and death time $d_i$ — summarizes the multi-scale topological structure. Features with high persistence $d_i - b_i$ represent robust topological structure. Word embedding spaces exhibit nontrivial persistent homology: stable loops that may correspond to semantic "circuits" — cyclic patterns of association (seasons, days of the week, stages of life).








### 10.4 Topological Data Analysis of Language Models

The persistent homology of activation vectors at different Transformer layers reveals that topological complexity varies systematically: early layers have simpler topology, middle layers exhibit maximum complexity, and later layers simplify again. Layers that encode rich syntactic structure tend to have higher Betti numbers $\beta_k = \mathrm{rank}\,H_k$, suggesting more complex topology.

### 10.5 Sheaf Theory and Discourse Coherence

Sheaf theory provides a mathematical framework for studying how local information can be consistently combined into global information. Abramsky and collaborators (Abramsky & Brandenburger, 2011) have used sheaf theory to model contextuality in language — connecting surprisingly to quantum mechanics, where sheaf-theoretic methods characterize non-classical correlations. The mathematical parallel between linguistic contextuality and quantum contextuality reflects a shared formal structure of context-dependence that may have deep cognitive implications.


# Chapter 11. Differential Geometry on the Landscape of Language {#ch11}

> "God created the integers; all the rest is the work of man."
> — Leopold Kronecker
{.epigraph}

### 11.1 Why Differential Geometry?

Differential geometry is the mathematical framework for studying curved spaces using the tools of calculus. If topology tells us the overall "shape" of a space, differential geometry tells us how the space curves and stretches locally — how distances, angles, and volumes vary from point to point. For language, differential geometry becomes essential when we recognize that the spaces in which linguistic objects are embedded — the parameter spaces of language models, the manifolds of word representations, the loss landscapes — are not flat but curved, and this curvature carries linguistic information.

### 11.2 Riemannian Manifolds: The Foundation

A Riemannian manifold is a smooth manifold $M$ equipped with a Riemannian metric — a smoothly varying inner product $g_p$ on each tangent space $T_pM$ that allows us to measure lengths, angles, and volumes. The length of a curve $\gamma: [a,b] \to M$ is:

$$L(\gamma) = \int_a^b \sqrt{g_{\gamma(t)}\!\bigl(\dot\gamma(t),\, \dot\gamma(t)\bigr)}\; dt$$

and the geodesic distance $d(p,q)$ between two points is the infimum of lengths over all curves connecting them. For the linguist, the key intuition is this: a Riemannian manifold is a space where the "ruler" for measuring distances changes from place to place. In linguistic terms, moving from one region of semantic space to another may involve different amounts of "semantic distance" per unit of geometric distance — the local metric reflects the local density and organization of meanings.

### 11.3 Curvature and the Local Structure of Semantic Space

The curvature of a Riemannian manifold measures how it deviates from flatness. Negative curvature (hyperbolic) means geodesics diverge and volumes grow faster than in flat space; positive curvature (spherical) means geodesics converge. Regions of high negative curvature in the representation manifold may correspond to hierarchical branching structures; regions of positive curvature may correspond to tightly clustered, cyclic structures. By measuring curvature at different points and layers, researchers can build a "curvature atlas" of linguistic information organization.

### 11.4 Geodesics and Semantic Trajectories

A geodesic is the shortest path between two points on a manifold — the generalization of a straight line to curved spaces. The geodesic from "puppy" to "dog" may pass through representations encoding maturation. The geodesic from "walk" to "run" may pass through representations encoding increasing speed. Geodesics on the representation manifold may encode conceptual pathways — the cognitive paths by which one concept is transformed into another.

### 11.5 The Fisher Information Metric

One of the deepest connections between differential geometry and language models comes through the Fisher information metric. For a family of probability distributions $p(x|\theta)$ parameterized by $\theta$, the Fisher information matrix defines a Riemannian metric on the parameter space:

$$F(\theta)_{ij} = \mathbb{E}_{x \sim p(\cdot|\theta)}\!\left[\frac{\partial \log p(x|\theta)}{\partial \theta_i} \cdot \frac{\partial \log p(x|\theta)}{\partial \theta_j}\right]$$

This metric measures how rapidly the probability distribution changes as the parameters vary. Flat directions (low Fisher information) correspond to redundant parameters; curved directions (high Fisher information) correspond to parameters that strongly influence linguistic behavior. This geometric perspective has implications for catastrophic forgetting and the effectiveness of low-rank adaptation methods like LoRA (Hu et al., 2022).

### 11.6 Fiber Bundles and the Architecture of Linguistic Representation

A fiber bundle is a topological space that locally looks like a product space $E \cong B \times F$ (with projection $\pi: E \to B$), but may have nontrivial global structure — the fibers may "twist" as one moves around the base space. In linguistic representation, the base space $B$ might represent syntactic structure, and the fiber $F_p = \pi^{-1}(p)$ at each node $p$ might represent semantic and morphological features. This connects to gauge equivariant neural networks, which use fiber bundles and connections to build networks that respect specified symmetries. If linguistic structure has gauge-like symmetries, gauge-equivariant architectures may be natural candidates for next-generation language models.


# Chapter 12. Category Theory: The Mathematics of Mathematical Linguistics {#ch12}

> "Category theory takes a bird's-eye view of mathematics."
> — Tom Leinster
{.epigraph}

### 12.1 Categories as a Unifying Language

Category theory provides a language for describing deep structural similarities between different mathematical frameworks. A category $\mathbf{C}$ consists of objects, morphisms between objects, and a composition operation. The category $\mathbf{Set}$ has sets and functions. The category $\mathbf{Vect}$ has vector spaces and linear maps. The category $\mathbf{Top}$ has topological spaces and continuous maps. By abstracting common structure, we can see what is preserved when translating between different mathematical representations of language.

### 12.2 Functors and Natural Transformations

A functor $F: \mathbf{C} \to \mathbf{D}$ is a structure-preserving map between categories. In linguistics, the passage from syntactic trees to semantic representations can be modeled as a functor. The embedding of words into vectors is a functor from a discrete linguistic category to the category of vector spaces. A natural transformation $\eta: F \Rightarrow G$ provides a systematic way of comparing two such translations while respecting structure.

### 12.3 The Categorical Approach to Compositionality

The DisCoCat framework models the syntax-semantics interface as a monoidal functor from a pregroup grammar (modeling syntax) to $\mathbf{FdVect}$ (finite-dimensional vector spaces, modeling semantics). This categorical perspective unifies the formal-semantic tradition of Montague and the distributional tradition — both can be expressed as functors from syntax to semantics. They differ in the target category ($\mathbf{Set}$ vs. $\mathbf{Vect}$) but share the same abstract principle. Category theory reveals that these approaches are not competitors but different instantiations of the same compositionality principle.

### 12.4 Enriched Categories and Graded Structures

In enriched categories, morphisms form objects in some other category — a metric space or vector space rather than a set. This is natural for linguistic applications where relationships are graded: the similarity between two words is a continuous measure, not binary. Enriching linguistic categories over metric spaces gives a framework in which graded linguistic relations are first-class citizens.


<!-- part: Part IV · Complex Systems & Reflection -->

# Chapter 13. Language as a Complex Adaptive System {#ch13}

> "More is different."
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

where $x \in [0,1]$ is the frequency of the innovative form, $\beta$ is the selection coefficient, and $\xi(t)$ is Gaussian noise, describes the S-shaped adoption curves documented across hundreds of language changes. The transition from $x \approx 0$ (old form dominant) to $x \approx 1$ (new form dominant) is a first-order phase transition: the fixed-point attractor at $x = 0$ becomes unstable and the attractor at $x = 1$ captures the system's trajectory. Blythe and Croft (2012) provide a comprehensive mathematical treatment of language change as a stochastic dynamical process, unifying sociolinguistic data with the mathematics of population dynamics.

### 13.4 Agent-Based Models and the Emergence of Linguistic Convention

A complementary mathematical approach models language as the outcome of interactions among many *agents*, each following simple local rules, from which global structure emerges. The paradigm example is Steels's (1995, 2011) *Language Game* framework.

In the Naming Game, a population of $N$ agents must converge on a shared lexicon for a set of objects without any central coordinator. The protocol is:

1. A *speaker* is selected at random and attempts to name a randomly chosen object, drawing from its inventory (or inventing a new word if empty).
2. A *hearer* attempts to parse the word. If successful, both agents reinforce that word and prune alternatives. If not, the hearer adds the new word to its inventory.

The mathematical analysis of this protocol reveals a phase transition from initial disorder (every agent uses different words) to global consensus (all agents converge on a single word per object) through a process of symmetry breaking. The convergence time scales as $O(N^{1.5})$, and the word frequency distribution follows a power law during the intermediate phase — another hallmark of criticality. The simulator at the end of this chapter allows you to observe these dynamics in real time.

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

The implication is both humbling and exciting: the full complexity of linguistic meaning is, in a precise sense, uncomputable. No finite formal system can capture it. This is not a counsel of despair — it is an invitation to take seriously the extra-formal dimensions of language: embodiment, sociality, history, and the irreducibly pragmatic.

### 13.8 Emergent Capabilities and the CAS View of Language Models

The CAS perspective also illuminates the behavior of large language models (LLMs). Wei et al. (2022) documented a striking phenomenon: as LLMs are scaled in parameters and training data, certain capabilities — multi-step arithmetic, chain-of-thought reasoning, language translation — appear to emerge *discontinuously*. Below a critical scale, a capability is absent; above it, the capability appears fully formed. This is a phase transition in the parameter-scale space.

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

> "The limits of formalization reveal the limits of understanding."
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

### 14.5 Future Directions

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

### Distributional Semantics and Lexical Resources

Harris, Z. "Distributional Structure." *Word*, 10(2–3):146–162, 1954.

Firth, J.R. *Papers in Linguistics 1934–1951.* Oxford University Press, 1957.

Miller, G.A. "WordNet: A Lexical Database for English." *Communications of the ACM*, 38(11):39–41, 1995.

Banarescu, L., Bonial, C., Cai, S., Georgescu, M., Griffitt, K., Hermjakob, U., Knight, K., Koehn, P., Palmer, M., and Schneider, N. "Abstract Meaning Representation for Sembanking." *Proceedings of the 7th Linguistic Annotation Workshop*, 178–186, 2013.

Gildea, D. and Jaeger, T.F. "Human Languages Order Information Efficiently." *Current Biology*, 25(9):R382–R385, 2015.

Landauer, T.K. and Dumais, S.T. "A Solution to Plato's Problem: The Latent Semantic Analysis Theory of Acquisition, Induction, and Representation of Knowledge." *Psychological Review*, 104(2):211–240, 1997.

Mikolov, T., Chen, K., Corrado, G., and Dean, J. "Efficient Estimation of Word Representations in Vector Space." arXiv:1301.3781, 2013.

Pennington, J., Socher, R., and Manning, C.D. "GloVe: Global Vectors for Word Representation." *Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 1532–1543, 2014.

Coecke, B., Sadrzadeh, M., and Clark, S. "Mathematical Foundations for a Compositional Distributional Model of Meaning." *Linguistic Analysis*, 36:345–384, 2010.

### Neural Networks and Transformers

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł., and Polosukhin, I. "Attention Is All You Need." *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.

Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., and Olah, C. "Toy Models of Superposition." *Transformer Circuits Thread*, Anthropic, 2022.

Hu, E.J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., and Chen, W. "LoRA: Low-Rank Adaptation of Large Language Models." *International Conference on Learning Representations (ICLR)*, 2022.

### Geometric and Topological Methods

Johnson, W.B. and Lindenstrauss, J. "Extensions of Lipschitz Mappings into a Hilbert Space." *Contemporary Mathematics*, 26:189–206, 1984.

Nickel, M. and Kiela, D. "Poincaré Embeddings for Learning Hierarchical Representations." *Advances in Neural Information Processing Systems (NeurIPS)*, 2017.

Abramsky, S. and Brandenburger, A. "The Sheaf-Theoretic Structure of Non-Locality and Contextuality." *New Journal of Physics*, 13:113036, 2011.

Ethayarajh, K. "How Contextual Are Contextualized Word Representations? Understanding the Geometry of Hidden States." *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2019.

Amari, S. *Information Geometry and Its Applications.* Springer, 2016.

### Category Theory and Linguistics

Lambek, J. "The Mathematics of Sentence Structure." *American Mathematical Monthly*, 65(3):154–170, 1958.

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

### Linear Algebra

Vectors in bold ($\mathbf{v}$), matrices in capitals ($M$), scalars in lowercase ($a$). $\langle \mathbf{u}, \mathbf{v} \rangle$ inner product, $\|\mathbf{v}\|$ norm, $M^\top$ transpose, $M^{-1}$ inverse, $\det(M)$ determinant, $\mathrm{tr}(M)$ trace, $\lambda_i$ eigenvalues, $\sigma_i$ singular values.

### Topology and Geometry

$M$ manifold, $T_pM$ tangent space at $p$, $g$ Riemannian metric, $R_{ijkl}$ Riemann curvature tensor, $H_k(X)$ $k$th homology group, $\beta_k$ $k$th Betti number, $\gamma$ curve/geodesic, $\nabla$ connection/covariant derivative.
