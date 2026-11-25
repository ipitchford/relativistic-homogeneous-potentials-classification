# Review summary (internal, AI-assisted)

This file records the internal checking of this candidate before release, without any ratings. It is not peer review,
independent reproduction or formal verification. All review steps were carried out by AI systems (Claude) under the
Evidence Press publication protocol; no external referee has seen the paper.

## What was done (24 November 2026)

1. **Combined five-role review panel** (editor, methodology, domain, perspective and devil's-advocate roles, run as
   one combined Claude pass because the source draft was short). The panel re-derived the load-bearing algebra
   (variational equations from the flow, the pullback, the Kimura case analysis, the jet and polar identities, the
   residue computations of Section 7), recomputed parts of it with SymPy and re-ran the original script. It found no
   mathematical error. Its objections concerned attribution, the rigour of one citation step and exposition.
2. **Independent proof audit** of the whole argument: every load-bearing computation reproduced, every cited external
   theorem checked against its source (Kimura's paper pp. 274–277, the Morales-Ruiz–Ramis–Simó author manuscript, the
   2023 paper eqs. (29)–(30) and Proposition 2, the 2025 paper Section 3.1 and Theorem 3). Verdict: proof complete,
   six minor items (justifications stated too briefly, wording).
3. **One revision round** (listed below), with extensions: Theorem B for complex coefficients, Corollary C, the local
   version Theorem 6.1, and the new script `code/check_complex.py`.
4. **Re-review** of the revised paper and a **second proof audit** of the new or rewritten proofs. Neither found a
   mathematical error. Their items were applied (see "Round-2 changes").
5. **Clean replay** of both scripts from a fresh copy, with and without `-O`, outputs byte-identical to `results/`;
   **negative control**: flipping the sign of the expected residue sum in `check_complex.py` makes it exit 1 under `-O`.
6. No Astra/Codex review took place for this candidate.

## Main objections and how they were resolved

- **Attribution to the 2023 paper (major).** The draft understated what Przybylska, Szumiński and Maciejewski had
  proved. Resolved: their Theorem 3 (a sparse integer set of admissible eigenvalues for rational integrals) is now
  stated in the Introduction and after Proposition 3.1, which is described as weaker but valid for meromorphic
  integrals; their Section V conclusion for degrees three to five and their non-integrability proofs for the Cartesian
  and parabolic separable families are credited; Theorem A is framed as new for k ≥ 6 and uniform for all k ≥ 3.
- **Generic potentials (major).** Corollary C proves the stated consequence of the 2023 Section VI conjecture
  (generic potentials are non-integrable); the arithmetic question on integer solutions stays open and is said so.
- **Method precedents.** Combot's degree −1 classification (2016) is named as the closest precedent (extremal
  direction, Lemma 3.1; rigidity, Theorem B and Lemma 4.5); Combot (2013) for the period determinant and the
  eigenvalue-one alternative; Duval–Maciejewski (2015) for higher variational equations. The paper does not claim the
  proof architecture or the period-determinant mechanism as new.
- **Citation step from MRS07 to the energy-surface holonomy (rigour).** New Lemma 2.4 (normal holonomy) shows that the
  jets of the holonomy on a transversal in the energy surface are a homomorphic image of the jets in MRS07
  Corollary 2(ii), and records the hypothesis (integrals not necessarily independent on the curve itself).
- **Smaller rigour items.** Passage from the variational to the normal variational equation; irreducibility of the
  phase curves; the identity g′/h = λ − 1 proved before use (Lemma 7.1(b)); the isotropic residue in one line
  (Lemma 7.1(d)); the use of x as time; the sharp range of Lemma 4.2; Kimura's theorem stated in Appendix A and checked
  against the original scan.
- **Readability.** New title naming the result; context-first abstract; Introduction with the problem, why it
  matters, what was known, what is new, the proof idea and a roadmap; purpose sentences for every section; notation
  defined before use.

## Round-2 changes

- The abstract and the Introduction state Theorem B's hypothesis δ > 0 (a nonisotropic linear factor).
- Lemma 7.1(f) bounds the number of nonisotropic Darboux directions for all isotropic multiplicities, so Corollary C
  does not depend on them; Corollary C says "nonradial".
- "Exactly two families undecided" became "the method leaves two families undecided in general".
- The Darboux-point relation and the multiplicity counts are credited to Maciejewski and Przybylska (2005) at the
  points of use; Lemma 7.1 re-derives what is used.
- Notation clashes removed; a short glossary added in Section 2.3; locators for the 2025 paper, MRS07 and Kimura
  corrected (Kimura: journal year 1969, issue dated 1970).

## What remains open or unchecked

- Isotropic monomials (a ≠ b) and the exact-half multiplicity case (Section 7).
- Curved-space and position-dependent-mass versions; three or more degrees of freedom; the arithmetic question of the
  2023 paper.
- Prior-art searches were of limited scope (Semantic Scholar citations of the 2023 paper, web searches and the cited
  sources); this is not a proof of priority.
- No external specialist has checked the proofs.
