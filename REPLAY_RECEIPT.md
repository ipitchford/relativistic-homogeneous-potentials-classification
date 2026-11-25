# Replay receipt (0.1.0-candidate, 25 November 2026)

**Environment.** macOS arm64. Commands as in the publish brief, from fresh copies of the approved candidate, cwd = package
root, `PYTHONDONTWRITEBYTECODE=1`; standard output went to a separate directory, never over the shipped results. The
interpreter was printed inside the run: `uv run --no-project --python 3.12 --with sympy==1.14.0 python3` built an
ephemeral environment on CPython 3.12.11 with SymPy 1.14.0.

| Command | Exit | Time | Result |
|---|---|---|---|
| `python3 -I -B code/verify_physics.py` | 0 | 1 s | PASS (spectral lists for k = 3, 4, 5 and every identity) |
| `python3 -I -B code/check_complex.py` | 0 | 2 s | PASS (Lemma 7.1(b), (d), identity (7.4), ten example potentials) |
| `python3 -I -B -O code/verify_physics.py` | 0 | 1 s | identical output |
| `python3 -I -B -O code/check_complex.py` | 0 | 1 s | identical output |

Every output, with and without `-O`, was byte-identical to the shipped file in `results/`; every standard-error stream was
empty.

**Negative control (under -O).** In a third fresh copy the expected residue sum in `code/check_complex.py` had its sign
flipped (`expected = S.Rational(kk * d, ...)` instead of `-S.Rational(...)`); the script stopped with
`RuntimeError: residue sum != -k d/((k-2a)(k-2b))`, exit 1.

**After the replay** only the title-page DOI line of `manuscript.tex`, the rebuilt PDF (three pdflatex passes, 16 pages;
a word-level text comparison with the approved PDF shows only the DOI line, with a float moved by one page) and the
release records changed; the scripts, recorded results and `requirements.txt` are byte-identical to the replayed
candidate.

**Cross-platform policy** (declared before tagging; see ENVIRONMENT.txt): fresh outputs must equal the recorded files byte
for byte. The outputs contain only exact text and exact rationals; the 60-digit numerical root checks inside
`check_complex.py` use a declared internal tolerance of 1e-40 and do not print floating-point values. No output contains
an interpreter or platform version. The GitHub Actions workflow `.github/workflows/replay.yml` checks the manifest, reruns
both scripts under `python -O` on Linux, compares byte for byte and runs the negative control (one blocking job).

**Scope.** The scripts check algebra (the variational equations, exponent differences, spectral lists, jet and polar
identities, the residue lemma and identity) and explicit examples. The proofs carry the general theorems.
