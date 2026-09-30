# Revision notes — September 2026

## How to publish
1. Copy `book.md`, `book.zh.md`, `build.py`, `template.html`, `publish.sh` into `mathling/` in the repo.
2. `bash publish.sh` → builds `temp/book.html` (EN) + `temp/book-zh.html` (中文) and syncs both to `docs/mathling/`.
3. `git add docs/mathling/book.html docs/mathling/book-zh.html` and push.

The EN/中文 switch sits in the top bar. Chapter and section ids (`#ch7`, `#sec-7-3`) match across the two languages, so switching keeps the reader in the same section.

## Build / template changes
- Fenced code blocks can now contain blank lines. The t-SNE code in §7.3 had been breaking out of its block.
- Raw `<figure>`, `<table>`, and `<svg>` blocks pass through unchanged. `####` sub-headings are supported.
- New `{.intuition}` box; boxes accept a custom title, e.g. `{.deep-dive: Title}`; multi-paragraph boxes work.
- Epigraphs no longer get doubled quotation marks (Preface, Ch. 10).
- Chinese typography: Noto Serif TC / Noto Sans TC, upright (non-italic) epigraphs.

## Content fixes
- Ch. 1 epigraph: a Poincaré line had been merged into the Chomsky quote. Removed.
- §9.1: fixed the LaTeX-style quotes and the full-width colon; turned the bullet-as-heading layout into `####` sub-sections.
- §10.2: the English edition had a Chinese paragraph in the middle of the text. Replaced it with an English deep-dive and restructured the section.
- Bibliography: Gildea & Jaeger (2015) is an arXiv paper, not *Current Biology*. Added Futrell et al. (2015, PNAS), the standard DLM citation. Also added the references the new material cites (van der Maaten & Hinton was already cited but missing from the list).
- §13.3: softened "first-order phase transition" for the logistic S-curve.
- §13.7: added a caution box saying the MIP* = RE argument is an analogy, not a theorem.
- §13.8: added Schaeffer et al. (2023), who argue some "emergent abilities" come from the choice of metric.

## New material (concept first, then formula)
- 1.5 How to read the mathematics
- Ch. 2: sets and Cartesian products; Venn figure for natural classes; table of relation properties; functions, syncretism, and non-injectivity
- Ch. 3: scope figure; scalar implicature; types as plugs and sockets; λ-terms as forms with blanks; possible worlds as a stack of maps; the conservativity intuition (*nall*)
- Ch. 4: worked derivation; hierarchy figure and memory analogy; pumping lemma; nested vs cross-serial figure; 4.6 weak vs strong generative capacity
- Ch. 5: constituency vs dependency figure; dominance and c-command; the head function; a worked dependency-length example; 5.5 adjacency matrices as the bridge to attention
- Ch. 6: why probability; chain rule and bigrams; surprisal and surprisal theory; cross-entropy, perplexity, KL divergence, PMI; a worked Bayes example with *bank*; Zipf figure
- Ch. 7: toy co-occurrence table; cosine figure; SVD as hidden dials; Levy & Goldberg (2014); a caution about analogies; the verb tensor as a machine; spectral learning (the old §7.6 had a title but no content on spectral methods)
- Ch. 8: neurons, loss, gradient descent; attention as a library search; reading the formula piece by piece; the residual stream as a whiteboard; attention figure; superposition and the JL lemma; 8.5 probing (Hewitt & Manning, 2019)
- Ch. 9: intrinsic dimension; the order-dependence picture of curvature; hyperbolic space "making room"; anisotropy
- Ch. 10: simplices as a construction kit; Betti numbers and Euler's formula; filtration and barcode figure; boundary operator worked through; sheaves as witness testimony
- Ch. 11: the metric as a hiking map; triangle-curvature figure; a worked Fisher example with a Bernoulli parameter; KL ↔ Fisher and natural gradient; fiber bundle intuition
- Ch. 12: categories as a transit map; functors as subway maps; commutative-square figure; pregroup derivation of *John loves Mary*; 12.5 costs and benefits
- Ch. 13: S-curve figure and rumour analogy; Baronchelli et al. citation for N^1.5
- Ch. 14: 14.5 "One word, many mathematics" (*bank* across all frameworks); Future Directions renumbered to 14.6
- Appendix A: probability and information notation. Chinese edition only: Appendix B, a Chinese–English glossary.

## Please check
- Ch. 5 epigraph (Deutsch) and Ch. 14 epigraph ("attributed to Gödel"): I could not verify either one.
- The simulator in §13.9 is still English-only.
- The front-matter `affiliation` field is still not rendered; the old build ignored it too.
