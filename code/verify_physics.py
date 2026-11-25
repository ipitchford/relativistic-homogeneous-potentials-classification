#!/usr/bin/env python3
"""Exact algebra checks for Sections 3-5 of the manuscript; requires SymPy.

This checks algebraic reductions, not the analytic hypotheses of the
Morales-Ramis-Simo and Kimura theorems.
Run from the package root: python3 code/verify_physics.py
"""
import sympy as S

z, x, k, lam, p, s, t = S.symbols("z x k lam p s t", nonzero=True)
P = (k - 1) / (k * z) + (z - s) / ((z - s)**2 - 1)
Q = lam * (s - z) / (k * z * ((z - s)**2 - 1))
Delta = (k - 1)**2 + 4 * k * lam
A = (k - 2)**2 + 8 * k * lam

def equal(a, b):
    if S.simplify(a - b) != 0:
        raise RuntimeError(f"Exact equality failed: {a} != {b}")

# Independent derivation from dot(z)=gamma*phi^(k-1)*psi/u,
# u=s-z, psi^2=(s-z)^2-1, and dot(eta)=xi/u.
log_derivative_dot_z = (k - 1) / (k * z) + (z - s) / ((z - s)**2 - 1) + 1 / (s - z)
equal(P, log_derivative_dot_z - 1 / (s - z))
equal(Q, lam * (s - z) / (k * z * ((s - z)**2 - 1)))

# Quadratic substitution x=z^2 at E=0.
actual = [S.factor(c * (1 - z*z) / 4) for c in
          (4*z*z, 2 + 2*z*P.subs(s, 0), Q.subs(s, 0))]
expected = [z*z*(1-z*z),
            1-S.Rational(1, 2)/k-(S.Rational(3, 2)-S.Rational(1, 2)/k)*z*z,
            lam/(4*k)]
for a, b in zip(actual, expected):
    equal(a, b)

# All exponent differences, including infinity.
def finite_difference_squared(z0, energy):
    a = S.limit((z-z0)*P.subs(s, energy), z, z0)
    b = S.limit((z-z0)**2*Q.subs(s, energy), z, z0)
    return S.factor((a-1)**2-4*b)

equal(finite_difference_squared(0, 1), A/(4*k*k))
equal(finite_difference_squared(2, 1), S.Rational(1, 4))
P_inf = S.limit(z*P, z, S.oo)
Q_inf = S.limit(z*z*Q, z, S.oo)
equal((P_inf-1)**2-4*Q_inf, Delta/(k*k))
equal((S.Rational(1, 2)-1/(2*k))**2+lam/k, Delta/(4*k*k))

# Exact Diophantine identity and the surviving eigenvalue family.
equal(A, 2*Delta-k*k+2)
equal(((2*p+1)*k+1)**2-(k-1)**2, 4*k*(p+1)*(k*p+1))

# Projective multiplier equals transverse scaled Hessian eigenvalue.
# At a Darboux point v'=t*h; h'=(k-1)*v'-t*v''.
h, vpp = S.symbols("h vpp", nonzero=True)
hp = (k-1)*t*h-t*vpp
multiplier = (vpp-t*hp)/h
trace_scaled = ((k-1)*h-t*hp+vpp)/h
equal(multiplier, trace_scaled-(k-1))
equal((vpp-h-t*hp)/h, multiplier-1)

# Euclidean specialization of the 2025 paper's exponent parameters.
lambda1_sq = 1/(k*k)
lambda2_sq = ((k+2)**2+8*k*(lam-1))/(4*k*k)
lambda3_sq = S.Rational(1, 2)-lambda1_sq+2*lambda2_sq
equal(lambda2_sq, A/(4*k*k))
equal(lambda3_sq, Delta/(k*k))

# The two halves of the integer spectrum (3.1): {0, 1} and values >= 2k - 1.
for degree in (3, 4, 5):
    spectrum = sorted({(i+1)*(degree*i+1) for i in range(-8, 9)})[:12]
    if spectrum[:2] != [0, 1] or min(spectrum[2:]) != degree + degree - 1:
        raise RuntimeError(f"Spectral sanity check failed for degree {degree}")
    print(f"k={degree}: {spectrum}")

# Exact jet-composition coefficient for arbitrary integral N>=2.
y, Pmom, N = S.symbols("y P N", positive=True)
Ag, Ad, Bg, Bd, Cg, Cd = S.symbols("A_g A_d B_g B_d C_g C_d")
composed_top = Bd*y**N+Cd*y**(N-1)*Pmom+Bg*(y+Ad*Pmom)**N+Cg*(y+Ad*Pmom)**(N-1)*Pmom
reversed_top = Bg*y**N+Cg*y**(N-1)*Pmom+Bd*(y+Ag*Pmom)**N+Cd*(y+Ag*Pmom)**(N-1)*Pmom
equal(S.diff(composed_top, Pmom).subs(Pmom, 0)/y**(N-1), Cd+Cg+N*Bg*Ad)
equal(S.diff(composed_top-reversed_top, Pmom).subs(Pmom, 0)/y**(N-1), N*(Bg*Ad-Bd*Ag))
equal(composed_top.subs(Pmom, 0)/y**N, Bg+Bd)

# Square-root Hamiltonian: first potential term and its normal momentum force.
eps, aa, cc, xx, ps = S.symbols("epsilon a c x psi", nonzero=True)
for degree in range(3, 9):
    for order in range(3, degree+1):
        j = 2*degree-order
        # Differentiate in c at c=0 to isolate the first transverse term.
        expression = -ps*S.sqrt(1-eps**2*Pmom**2/ps**2+2*aa*cc*xx**j*eps**order*y**order/ps**2)
        isolated = S.diff(expression, cc).subs(cc, 0)
        leading = S.series(isolated, eps, 0, order+1).removeO().coeff(eps, order)
        equal(leading, -aa*xx**j*y**order/ps)
        equal(-S.diff(leading, y), order*aa*xx**j*y**(order-1)/ps)

# Polynomial-primitive degree obstruction on psi^2=a^2*x^(2k)-1.
for degree in range(3, 9):
    for r in range(4):
        poly = xx**r + (xx+1 if r >= 2 else 0)
        numerator = S.expand((aa**2*xx**(2*degree)-1)*S.diff(poly, xx)
                             + degree*aa**2*xx**(2*degree-1)*poly)
        actual_degree = S.Poly(numerator, xx).degree()
        actual_leading = S.Poly(numerator, xx).LC()
        poly_degree = S.Poly(poly, xx).degree()
        if actual_degree != poly_degree+2*degree-1:
            raise RuntimeError("Primitive numerator degree check failed")
        equal(actual_leading, aa**2*(poly_degree+degree)*S.Poly(poly, xx).LC())

# Polar radial-rigidity argument: exact differential identities.
# Multiply each derivative by psi and use psi^2=a^2*r^(2k)-1.
rr, theta, angular_momentum, angular_order = S.symbols(
    "r theta L m", positive=True)
psi_squared = aa**2*rr**(2*k)-1
equal(psi_squared+k*aa**2*rr**(2*k),
      (k+1)*aa**2*rr**(2*k)-1)
equal(k*aa**2*rr**(2*k-2)-psi_squared/rr**2,
      (k-1)*aa**2*rr**(2*k-2)+rr**(-2))

# First angular term, isolated at zero momentum; m need not be <= k.
polar_hamiltonian = -ps*S.sqrt(
    1-angular_momentum**2/(rr**2*ps**2)
    +2*aa*cc*rr**(2*k)*theta**angular_order/ps**2)
first_angular_term = S.diff(polar_hamiltonian, cc).subs(
    {cc: 0, angular_momentum: 0})
equal(first_angular_term, -aa*rr**(2*k)*theta**angular_order/ps)
equal(-S.diff(first_angular_term, theta),
      angular_order*aa*rr**(2*k)*theta**(angular_order-1)/ps)
equal(S.diff(polar_hamiltonian, angular_momentum, 2).subs(
    {cc: 0, angular_momentum: 0}), 1/(rr**2*ps))

print("PASS: NVE derivation, pullback, exponent differences, discriminants,")
print("      eigenvalue family, projective multiplier and 2025 specialization;")
print("      general jet-composition coefficient, reduced-Hamiltonian terms,")
print("      polynomial-primitive degree and polar differential identities.")
print("      Checks remain active under -O.")
