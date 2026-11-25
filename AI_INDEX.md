# AI index: Relativity leaves only the symmetric potentials integrable (v0.1.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with [README.md](README.md) ("What
this is about") and the paper [manuscript.pdf](manuscript.pdf) (source [manuscript.tex](manuscript.tex); Section 1 is
a plain introduction with what was known, what is new, the proof idea and a roadmap). DOI 10.5281/zenodo.24523290
(concept 10.5281/zenodo.24523289). Status: unrefereed candidate; internal AI-assisted review only.

## Normalisation

H = √(1 + p1² + p2²) + V(q1, q2) on the connected complex phase space M = {(q, p, u) ∈ C⁵ : u² − p1² − p2² = 1, u ≠ 0},
H = u + V. V ∈ C[q1, q2] homogeneous of degree k ≥ 3. "Integrable" = a second first integral meromorphic on M (or near
named phase curves) and functionally independent of H. Darboux direction [d]: ∇V(d) = γ d; proper if γ ≠ 0;
nonisotropic if d·d ≠ 0. Transverse eigenvalue λ: the scaled Hessian eigenvalue on the vector orthogonal to d.
ℓ± = q1 ± i q2 (isotropic linear forms); V = ℓ+^α ℓ−^β U with δ = deg U. Homothetic phase curves Γ_s at energies
s = 0, 1. Reference keys as in [refs.bib](refs.bib): PSM23 = Przybylska–Szumiński–Maciejewski, Chaos 33 (2023) 063156,
doi:10.1063/5.0140633; MP05 = Maciejewski–Przybylska, J. Math. Phys. 46 (2005) 062901, doi:10.1063/1.1917311;
Combot16 = Ann. Inst. Fourier 66 (2016), doi:10.5802/aif.3063; MRS07 = Morales-Ruiz–Ramis–Simó, doi:10.1016/j.ansens.2007.09.002.

## Claims and where they are proved

| ID | Claim | Location | Status / credit |
|---|---|---|---|
| A (main) | Real V, nonzero, homogeneous, k ≥ 3: meromorphically integrable on M ⇔ rationally integrable ⇔ after a real rotation V = c q1^k, or k even and V = c (q1² + q2²)^(k/2); integrals p2 and q1p2 − q2p1 | Theorem A, Section 6 | written proof; new for k ≥ 6; for k = 3, 4, 5 PSM23 Sec. V reached the real conclusion by another route (their Thm 3 plus classical lists) |
| A-local | Non-integrability already fails near Γ0 or Γ1 attached to a real direction where \|V\| is maximal on the unit circle | Theorem 6.1 | written proof |
| 1 | Spectral restriction: λ = (n+1)(kn+1), n ∈ Z, hence λ ∈ {0,1} ∪ [2k−1, ∞), for meromorphic integrals near Γ0 and Γ1 | Proposition 3.1 | written proof via SP25 reductions and Kimura's theorem (Appendix A); weaker than PSM23 Thm 3 (rational integrals) |
| 2 | Zero-eigenvalue rigidity: λ = 0 at a nonisotropic proper Darboux direction forces V = a x^k (aligned coordinates) | Theorem 4.1, Lemma 4.2 | written proof; mechanism: independent periods of dx/ψ and x^(2k−m)dx/ψ on ψ² = a²x^(2k) − 1 make a finite jet of the normal holonomy non-commutative (MRS07 Cor. 2(ii) via Lemma 2.4) |
| 3 | Eigenvalue-one rigidity: λ = 1 forces k even and V = c (q1² + q2²)^(k/2) | Theorem 5.1 | written proof; conclusion also follows from PSM23 Prop. 1 with Combot13 Thm 1 |
| 4 | Normal holonomy lemma linking MRS07 to transversal jets in the energy surface | Lemma 2.4 | written proof |
| B | Complex V with δ > 0, α ≠ k/2, β ≠ k/2: integrable ⇔ α = β = 0 and V is a power of one nonisotropic linear form | Theorem B, Section 7, Lemma 7.1 | written proof; uses the residue relation of MP05 Thm 2.3 (eq. (2.42)), which Lemma 7.1 re-derives |
| C | No isotropic factor: integrable ⇔ V = c L^k, L nonisotropic; generic potentials (k distinct nonisotropic proper Darboux directions, nonradial) are non-integrable | Corollary C | written proof; proves the stated consequence of the PSM23 Sec. VI conjecture; its arithmetic part stays open |
| 5 | Open: isotropic monomials ℓ+^α ℓ−^β (α ≠ β, α, β ≥ 1) and δ > 0 with an isotropic multiplicity exactly k/2 | end of Section 7, Section 8 | open (individual members can sometimes be decided) |

## Evidence

| Check | Script | Output | Scope |
|---|---|---|---|
| NVE (3.2) from the flow; pullback (3.3); exponent differences (3.4)–(3.5) incl. infinity; A = 2Δ − k² + 2 and the factorisation behind (3.1); spectral lists for k = 3, 4, 5 (k = 3: 0, 1, 5, 8, 16, ...; smallest value other than 0, 1 is 2k − 1); flat specialisation of SP25 eqs. (31)–(34); jet coefficient (4.10)–(4.11) for symbolic N; first transverse term (4.6) and force for 3 ≤ m ≤ k ≤ 8; degree and leading coefficient in (4.12); polar identities behind (5.5) | [code/verify_physics.py](code/verify_physics.py) | [results/verify_physics.txt](results/verify_physics.txt) | exact SymPy |
| Lemma 7.1(b) g′ = (λ − 1)h and the radial eigenvalue k − 1; Lemma 7.1(d) residue α/(k − 2α) (symbolic); identity (7.4); ten potentials (k = 3..8) with residue sums against Hessian eigenvalues | [code/check_complex.py](code/check_complex.py) | [results/check_complex.txt](results/check_complex.txt) | exact SymPy; examples with 60-digit roots, internal tolerance 1e-40, seed 20261124; printed output exact |

Both scripts raise RuntimeError on failure (checks stay active under python -O). Output comparison: byte-exact. Negative
control: sign flip of the expected residue sum in check_complex.py exits 1 under -O (release replay and CI).

Numbers quoted on the release page and in the audio: degree at least three; eigenvalue 0 or 1; degrees three to five
(2023 paper); the 2023 admissible set for degree three begins 0, 1, 5, 40, 176. All are stated in the paper or its
sources and bound in the review record.

## Limits

Integrability is complex-meromorphic on M (or near two phase curves); smooth or real-region integrals, single energy
levels and chaos are not addressed. Degrees one and two, non-homogeneous potentials and n ≥ 3 degrees of freedom are
outside the statements. Two complex families are undecided in general (claim 5). The scripts check algebra and
examples; the proofs carry the general claims. Prior-art searches were of limited scope (see
[RESEARCH_GATES.json](RESEARCH_GATES.json)).

## Records

[REVIEW_SUMMARY.md](REVIEW_SUMMARY.md) (rating-free internal review record), [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md),
[ENVIRONMENT.txt](ENVIRONMENT.txt), [RESEARCH_GATES.json](RESEARCH_GATES.json), [refs.bib](refs.bib),
[CITATION.cff](CITATION.cff), [LICENSE.md](LICENSE.md), [MANIFEST.sha256](MANIFEST.sha256),
[.github/workflows/replay.yml](.github/workflows/replay.yml).
