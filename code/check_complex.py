#!/usr/bin/env python3
"""Exact checks for Section 7 (complex coefficients) of the manuscript; requires SymPy.

Checks Lemma 7.1(b) (g' = (lambda-1) h at a Darboux root), Lemma 7.1(d) (isotropic
residue a/(k-2a)), the residue-sum identity (7.4), and explicit examples in which
the residue sum is compared with eigenvalues computed directly from the Hessian.
Algebra only: the analytic theorems are proved in the text.
Failures raise RuntimeError, so the checks stay active under python -O.
Run from the package root: python3 code/check_complex.py
"""
import random

import sympy as S


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def zero(expr, message):
    require(S.simplify(expr) == 0, message)


t, h, vpp, k = S.symbols("t h vpp k")

# Lemma 7.1(b): at a Darboux root v' = t h and k v = (1+t^2) h.
vp = t * h
hp = (k - 1) * vp - t * vpp          # (k-1) V_2 = V_12 + t V_22 with V_12 = h'
V11 = (k - 1) * h - t * hp           # V_11 + t V_12 = (k-1) V_1
e_V_e = t**2 * V11 - 2 * t * hp + vpp  # e = (-t, 1)
lam = e_V_e / (h * (1 + t**2))
g_prime = 2 * t * vp + (1 + t**2) * vpp - (1 + t**2) * h - k * t * vp
zero(g_prime / h - (lam - 1), "g'/h != lambda - 1")
d_V_d = V11 + 2 * t * hp + t**2 * vpp   # d = (1, t): radial eigenvalue k-1
zero(d_V_d - (k - 1) * h * (1 + t**2), "radial eigenvalue != k-1")
print("PASS Lemma 7.1(b): g'(t_i) = (lambda_i - 1) h(t_i); radial eigenvalue k-1")

# Lemma 7.1(d): residue at t = i for v = (t-i)^a w, symbolic a, k, generic w.
a, b, W0, W1 = S.symbols("a b W0 W1")
eps = S.symbols("epsilon")
# Laurent data of h/v and g/v near t = i (t = i + eps), with W = w'/w = W0 + W1 eps.
tt = S.I + eps
W = W0 + W1 * eps
h_over_v = k - tt * a / eps - tt * W
g_over_v = a * (tt + S.I) + (1 + tt**2) * W - k * tt
residue = S.limit(eps * h_over_v / g_over_v, eps, 0)
zero(residue - a / (k - 2 * a), "isotropic residue != a/(k-2a)")
print("PASS Lemma 7.1(d): residue a/(k-2a) at t = i (symbolic a, k, cofactor)")

# Identity (7.4).
zero(-1 - a / (k - 2 * a) - b / (k - 2 * b) + k * (k - a - b) / ((k - 2 * a) * (k - 2 * b)),
     "residue-sum identity failed")
print("PASS identity (7.4): -1 - a/(k-2a) - b/(k-2b) = -k d/((k-2a)(k-2b))")


def hessian_eigenvalue(V, q1, q2, root):
    """Transverse eigenvalue at Darboux direction (1, root), from the Hessian (numeric root)."""
    point = {q1: 1, q2: root}
    gamma = S.N(S.diff(V, q1).subs(point), 60)
    H = [[S.N(S.diff(V, x, y).subs(point), 60) for y in (q1, q2)] for x in (q1, q2)]
    e = (-root, 1)
    eVe = sum(e[i] * H[i][j] * e[j] for i in range(2) for j in range(2))
    return eVe / (gamma * (1 + root**2))


q1, q2 = S.symbols("q1 q2")
lp, lm = q1 + S.I * q2, q1 - S.I * q2
examples = [
    (q1 - 2 * q2) * (q1 + 3 * q2) * (2 * q1 + q2),
    (q1 - 2 * q2)**2 * (q1 + 3 * q2) * (2 * q1 + 7 * q2),
    lp * (q1 - 2 * q2) * (q1 + 3 * q2) * (2 * q1 - 5 * q2),
    lp**4 * lm * (q1 - 2 * q2) * (q1 + 3 * q2),
    lp**2 * lm**3 * (q1 - 2 * q2) * (q1 + 3 * q2) * (q1 + q2),
    lp * lm * (q1**3 - 2 * q2**3 + q1 * q2**2),
    lp**3 * (q1 - q2) * (q1 + 2 * q2),
]
rng = random.Random(20261124)
while len(examples) < 10:
    lin = [rng.choice([1, 2, 3]) * q1 + rng.randint(-5, 5) * q2 for _ in range(rng.randint(3, 4))]
    examples.append(S.prod(lin) * lp**rng.randint(0, 1))

TOL = S.Float("1e-40", 60)
for V in examples:
    V = S.expand(V)
    kk = S.Poly(V, q1, q2).total_degree()
    v = S.expand(V.subs({q1: 1, q2: t}))
    vroots = S.roots(S.Poly(v, t))
    a_m, b_m = vroots.get(S.I, 0), vroots.get(-S.I, 0)
    d = kk - a_m - b_m
    require(kk >= 3 and d > 0 and 2 * a_m != kk and 2 * b_m != kk, "example outside Theorem B hypotheses")
    hh = S.expand(kk * v - t * S.diff(v, t))
    gg = S.expand((1 + t**2) * S.diff(v, t) - kk * t * v)
    require(S.degree(gg, t) == kk, "direction (0,1) is a Darboux direction in this chart")
    common = S.gcd(v, S.diff(v, t))
    ghat = S.quo(gg, common, t)
    hhat = S.quo(hh, common, t)
    require(S.gcd(ghat, hhat).is_number, "reduced h, g not coprime")
    total = 0
    count = 0
    for r in S.Poly(ghat, t).nroots(n=60, maxsteps=200):
        if abs(S.N(S.expand(1 + r**2), 60)) < S.Float("1e-30"):
            continue  # isotropic pole
        lam_r = hessian_eigenvalue(V, q1, q2, r)
        res_r = S.N(hhat.subs(t, r) / S.diff(ghat, t).subs(t, r), 60)
        require(abs(S.N(S.expand(res_r - 1 / (lam_r - 1)), 60)) < TOL, "residue at Darboux root != 1/(lambda-1)")
        total += res_r
        count += 1
    expected = -S.Rational(kk * d, (kk - 2 * a_m) * (kk - 2 * b_m))
    require(abs(S.N(S.expand(total - expected), 60)) < TOL, "residue sum != -k d/((k-2a)(k-2b))")
    require(count <= d, "more nonisotropic Darboux directions than d")
    print(f"PASS k={kk}, a={a_m}, b={b_m}, d={d}, r={count}, sum={expected}")

print("PASS: complex-coefficient residue lemma and identity checks. Checks remain active under -O.")
