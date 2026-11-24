# Prime rank, logarithmic phase, and local observability
**José Alonso Melendrez Hurtado · Working research note · 24 November 2026**

This independent number-theory project asks how sampling at primes affects the ability to distinguish two oscillatory contributions associated with zeros of the Riemann zeta function. The proposed contribution is a reproducible comparison of sampling coordinates. The zero phases and the inverse function theorem are established ingredients. Priority and empirical performance remain open.

## Two coordinates for one event
For the nth prime p_n, retain both n and p_n. The step from 7 to 11 advances the rank by one and the integer coordinate by four. In logarithmic coordinates u_n = log(p_n), the same step has length log(11/7). For a zero ρ_j = 1/2 + iγ_j on the critical line, define θ_j(u) = γ_j u − arg(ρ_j). Its unwrapped phase increment between consecutive primes is exactly γ_j log(p_{n+1}/p_n). This identity also holds for any positive increasing sequence after substituting its events. Evidence for prime-specific structure therefore requires a control sequence.

## A two-mode calculation
Use the first two positive zero ordinates, approximately 14.134725 and 21.022040. Write b_j = 1/|ρ_j| and define the normalized displacement F = −Σ b_j cos θ_j and its logarithmic slope G = dF/du = Σ b_j γ_j sin θ_j. These are two selected modes of an explicit-formula oscillation. They omit the other zeros and terms required to reconstruct a prime-counting function.

The phase-to-observation Jacobian of (F,G) has column j equal to (b_j sin θ_j, b_j γ_j cos θ_j). Its determinant is

D = b₁b₂(γ₂ sin θ₁ cos θ₂ − γ₁ cos θ₁ sin θ₂).

D ≠ 0 permits local recovery of two independently perturbed phases from the two observations. Varying u alone traces a one-dimensional curve through this phase plane. If the displacement is restored to W = 2 exp(u/2) F, the product rule gives dW/du = W/2 + 2 exp(u/2) G. Omitting W/2 changes the observable.

## Experiment
Run `python experiment.py` from this directory to compare the median local condition number at primes with its distribution under shuffled prime gaps. Shuffling preserves the endpoints and exact gap counts while disrupting gap order. The condition number uses the Euclidean norm with G divided by γ₂ to state a fixed relative scale for the two measurements. It measures worst-direction local sensitivity. The shuffle distribution is a descriptive control. Vary the sample size and test other null models before drawing conclusions about primes.

For the 168 primes through 1000, the median was 2.9413. Across 200 seeded shuffles the medians ranged from 2.5455 to 3.8562, with median 3.0419. The observed value lies inside that range.

## Generalized window criterion and a falsifiable next-prime test

### Can the observables distinguish the candidate gaps?

Let $\mathbf y(x)$ be the chosen measurements, for example normalized wave displacement and slope. Let $J_x$ be their Jacobian with respect to the phase vector. A cutoff such as $\kappa_2(J_x)<10$ describes relative sensitivity across directions. Even $J=0.001I$ has condition number one, so a condition-number cutoff alone gives no minimum detectable change.

Specify a set $\mathcal D_x$ of perturbations at the smallest scientifically relevant size in each direction of interest. Choose a positive-definite uncertainty matrix $\Sigma_x$ for the measurements and a separation threshold $\tau>0$. A local observability window satisfies

$
\inf_{\delta\in\mathcal D_x}\left\|\Sigma_x^{-1/2}J_x\delta\right\|_2\geq\tau .
$

State how the uncertainty scale was chosen. In deterministic calculations, declared tolerances for displacement and slope can supply the diagonal standard deviations. The threshold then expresses separation in tolerance units.

Starting at a prime $p$, each proposed gap $h$ advances the phases together by $\log(1+h/p)(\gamma_1,\ldots,\gamma_m)$. For finite candidate gaps $a,b$, use their actual measurement difference, which also detects similar signatures after phase wrapping:

$
d_p(a,b)=\left\|\Sigma_p^{-1/2}\big[\mathbf y(p+a)-\mathbf y(p+b)\big]\right\|_2 .
$

For example, at $p=101$, compare offsets 2 and 6 by evaluating the same observables at 103 and 107. If their distance exceeds $\tau$, the signatures are distinguishable. The distance is symmetric, so it gives no preference between the candidates. A prediction requires a separate ranking rule.

### Does the phase information help locate the next prime?

1. Specify an earlier training range and a disjoint, later evaluation range. On the earlier range choose a search horizon, candidate exclusions, frequencies, scaling, threshold, scoring rule, tie rule, and guess budget $K$. Freeze these choices before evaluation.
2. At each evaluation prime $p_n$, rank candidate offsets using only information available through $p_n$ and features computable at proposed locations without testing their primality. One reproducible comparison is to learn next-gap frequencies by offset on the training range, then test whether adding candidate phase features to that same baseline improves its ranking.
3. Give both methods the same horizon, exclusions and budget. Record their top $K$ guesses before revealing $p_{n+1}$. Count gaps beyond the horizon as misses. If the window permits abstention, score the baseline on the same issued cases and also report results over all eligible cases, counting abstentions as misses.
4. Report the evaluation bounds, number of cases, coverage, hit rates, paired hit-rate difference, and uncertainty estimate with its assumptions. Publish misses alongside hits. A zero or negative difference fails to support a predictive advantage for the tested configuration. Changes motivated by the results require a fresh evaluation range.

The existing Python experiment compares conditioning at known primes with shuffled-gap controls. The forward test above is an open protocol. Readers extending it can change one element at a time and share the exact configuration, code, and held-out results.

## Possible extension to neural electrical signals
For a spike train, pair each spike's event index with its recorded time. A separate experiment could compare phase-recovery error on synthetic spike trains with known generating phases, then compare recorded spike trains with interval-shuffled controls. Time units, phase frequencies, and a positive reference time for logarithms must be defined for those data. No neural recordings were analyzed here. Whether such coordinates capture anything about information transfer between neurons remains an open question.

## Sources and reuse
Numerical and theoretical background: [NIST DLMF, zeros of the Riemann zeta function](https://dlmf.nist.gov/25.10).

© 2026 José Alonso Melendrez Hurtado. This note and the accompanying example are offered under [Creative Commons Attribution–NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/). You are welcome to reproduce the calculations, share adaptations, and report counterexamples under those terms.

Developed from the author's research dialogue with AI assistants. This first edition presents a selected derivation and experiment from the longer working draft.
