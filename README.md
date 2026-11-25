# Relativity leaves only the symmetric potentials integrable

A classification of homogeneous polynomial potentials for the additive relativistic Hamiltonian.

Version 0.1.0-candidate. DOI [10.5281/zenodo.24523290](https://doi.org/10.5281/zenodo.24523290) (all versions:
[10.5281/zenodo.24523289](https://doi.org/10.5281/zenodo.24523289)). Release page:
https://evidencepress.org/releases/relativistic-homogeneous-potentials-classification/

**Status: unrefereed research candidate.** The proofs have had internal AI-assisted review only (see
[REVIEW_SUMMARY.md](REVIEW_SUMMARY.md)); this is not peer review, independent reproduction or formal verification.

## What this is about

Think of a particle sliding in a plane under a force field. The field is described by a potential V(q1, q2), and the
total energy is kinetic energy plus V. The motion is called **integrable** when, besides the energy, there is a second
conserved quantity. Integrable motion is regular and predictable; without a second conserved quantity the motion can
be chaotic.

For potentials that are **homogeneous polynomials** (every term has the same degree k, as in x³, x⁴ − y⁴ or
(x² + y²)²), classical mechanics has a rich list of integrable cases: potentials depending on one coordinate, radial
potentials, separable ones such as x^k + y^k, and several sporadic families.

Now replace the classical kinetic energy ½|p|² by Einstein's relativistic one, √(1 + |p|²) (unit mass, unit speed of
light). The Hamiltonian becomes

    H = √(1 + p1² + p2²) + V(q1, q2).

Which potentials are still integrable?

## What was known

Przybylska, Szumiński and Maciejewski (*Chaos*, 2023) found that relativity is "destructive": almost all classical
integrable cases lose integrability. They suggested that only potentials depending on one coordinate, or radial ones,
survive. They proved a strong necessary condition for rational first integrals, used it with the known classical lists
to settle degrees three, four and five, proved the Cartesian and parabolic separable families non-integrable for all
degrees, and conjectured that generic potentials are all non-integrable, while calling a general conjecture premature.
Maciejewski and Przybylska (2005) gave the relation between the eigenvalues at the special directions of a generic
potential and the multiplicity counts used here for complex potentials.

## What is new

1. **Theorem A (real potentials, every degree k ≥ 3).** A nonzero real homogeneous polynomial potential of degree k ≥ 3
   has a second first integral, meromorphic on the natural complex phase space and independent of H, **if and only if**,
   after a rotation,

       V = c·q1^k   or   (k even)   V = c·(q1² + q2²)^(k/2).

   In plain words: only potentials with a continuous symmetry survive (sliding along a line, or rotating), and their
   conserved quantity is the corresponding momentum or angular momentum. The result is new for k ≥ 6; for k = 3, 4, 5
   the 2023 paper reached the same real conclusion by another route, and the proof here is uniform in k. A local
   version (Theorem 6.1) needs integrability only near two explicit complex phase curves.
2. **Theorem 4.1 (zero-eigenvalue rigidity).** If a special direction has transverse eigenvalue 0, the potential must
   be a pure power of one coordinate. This has no classical counterpart in positive degree: classically x^k + y^k has
   eigenvalue 0 and is integrable.
3. **Theorem B and Corollary C (complex coefficients).** Take a complex-coefficient potential that has a nonisotropic
   linear factor and whose isotropic factors q1 ± i q2 do not occur with multiplicity exactly k/2. It is integrable if
   and only if it is a power c·L^k of a single nonisotropic linear form L. In particular, for potentials with no
   isotropic factor, every generic homogeneous polynomial potential is non-integrable. This proves the stated consequence of the 2023 conjecture; the arithmetic
   question posed there remains open.

## Idea of the proof

Find the direction where |V| is largest on the unit circle. Straight-line motions along it exist, and the small motions
across it are governed by one number λ (the transverse eigenvalue). At this extremal direction λ ≤ 1, and two
hypergeometric reductions of the linearised equations, together with Kimura's classification of solvable
hypergeometric equations, force λ = 0 or λ = 1.

If λ = 0, look at the first term of V that depends on the sideways coordinate. Following nearby orbits once around a
loop of the phase curve ψ² = a²x^(2k) − 1 gives a map (the normal holonomy). Its linear part and its first nonlinear
part involve two periods on this hyperelliptic curve, and the two periods are independent; so two such loop maps fail
to commute. The Morales–Ramis–Simó theory forbids this for an integrable system, so the sideways term cannot exist and
V = c·x^k. The case λ = 1 is the same argument in polar coordinates and gives the radial power. Classically the
corresponding second period collapses, which is why the classical separable x^k + y^k survives classically but not
relativistically.

## Credit

The question and the strongest prior results are due to Przybylska, Szumiński and Maciejewski (2023); Szumiński and
Przybylska (2025) supply the hypergeometric reductions used in the spectral step. Maciejewski and Przybylska (2005) give
the Darboux-point relation and the multiplicity counts behind Theorem B. The proof architecture (an extremal direction
plus rigidity at small eigenvalues) follows Combot's classical classification of degree −1 potentials (2016), and the
eigenvalue-one case also follows from published results (2023 paper, Proposition 1, with Combot 2013, Theorem 1). The
tool that turns the holonomy computation into an obstruction is the theorem of Morales-Ruiz, Ramis and Simó (2007).

## Limits

- Integrability here means a first integral meromorphic on the complex phase space. Smooth conserved quantities on a
  restricted real region or on one energy level are not excluded, and chaos is not proved.
- Degrees one and two, non-homogeneous potentials and three or more degrees of freedom are outside the statements.
- For complex coefficients the method leaves two families undecided in general: isotropic monomials
  (q1 + i q2)^a (q1 − i q2)^b with a ≠ b and a, b ≥ 1, and potentials with a nonisotropic factor in which one isotropic
  factor has multiplicity exactly k/2. Real potentials never fall into either family.
- Unrefereed candidate. The scripts check algebra and examples; the proofs carry the general claims.

## Contents

| Path | What it is |
|---|---|
| `manuscript.pdf`, `manuscript.tex` | The paper (16 pages; self-contained LaTeX source, no figures) |
| `code/verify_physics.py` | Exact SymPy checks: the normal variational equation from the flow, the pullback, the exponent differences, the spectral lists for k = 3, 4, 5, the flat specialisation of the 2025 reductions, the jet-composition coefficient (symbolic N), the first transverse term and its force for 3 ≤ m ≤ k ≤ 8, the polynomial-primitive degree and the polar identities |
| `code/check_complex.py` | Lemma 7.1(b) and (d), identity (7.4), and ten example potentials (k = 3..8) whose residue sums are compared with eigenvalues computed directly from the Hessian |
| `results/` | Recorded outputs of both scripts |
| `requirements.txt` | sympy==1.14.0 |
| `refs.bib`, `AI_INDEX.md`, `RESEARCH_GATES.json`, `REVIEW_SUMMARY.md`, `REPLAY_RECEIPT.md`, `ENVIRONMENT.txt`, `MANIFEST.sha256` | Records |
| `.github/workflows/replay.yml` | CI: manifest, both scripts under python -O, exact comparison with `results/`, negative control |

## Replay

From the package root:

    python3 -m pip install -r requirements.txt
    python3 -I -B -O code/verify_physics.py   # compare with results/verify_physics.txt
    python3 -I -B -O code/check_complex.py    # compare with results/check_complex.txt

Each script takes a few seconds and raises an exception on any failed check (no bare `assert`), so the checks stay
active under `python -O`. Comparison policy: both outputs contain only exact text and exact rationals and must match
the recorded files **byte for byte**, on any platform. Inside `check_complex.py` the ten example potentials use
60-digit numerical roots with a declared tolerance of 1e-40 and a fixed random seed (20261124); the printed results are
exact rationals, so no output tolerance is needed. Neither output prints an interpreter or platform version. A
negative control (flipping the sign of the expected residue sum in `check_complex.py`) makes the script exit 1 under
`-O`; CI repeats it on every push.

## Licence and citation

Text, paper, recorded outputs and records: CC0-1.0. Code: MIT. See [LICENSE.md](LICENSE.md) and
[CITATION.cff](CITATION.cff). Creator: Anonymous.

Cite as: Anonymous (2026). *Relativity leaves only the symmetric potentials integrable: a classification of
homogeneous polynomial potentials for the additive relativistic Hamiltonian*. Version 0.1.0-candidate. Evidence Press.
https://doi.org/10.5281/zenodo.24523290
