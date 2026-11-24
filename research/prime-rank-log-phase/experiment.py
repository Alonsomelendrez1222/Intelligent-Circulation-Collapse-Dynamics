"""Compare two-mode conditioning at primes and at shuffled-gap controls."""
import cmath
import math
import random
from statistics import median

ZEROS = (complex(0.5, 14.134725), complex(0.5, 21.022040))

def condition(x):
    columns = []
    for zero in ZEROS:
        phase = zero.imag * math.log(x) - cmath.phase(zero)
        columns.append((math.sin(phase) / abs(zero),
                        math.cos(phase) * zero.imag / (abs(zero) * ZEROS[1].imag)))
    (a, c), (b, d) = columns
    det = abs(a*d - b*c)
    trace = a*a + b*b + c*c + d*d
    largest_squared = (trace + math.sqrt(max(0, trace**2 - 4*det**2))) / 2
    return largest_squared / det if det else math.inf

def main():
    primes = [n for n in range(2, 1001)
              if all(n % k for k in range(2, math.isqrt(n) + 1))]
    gaps = [b-a for a, b in zip(primes, primes[1:])]
    rng = random.Random(2026)
    controls = []
    for _ in range(200):
        rng.shuffle(gaps)
        positions = [primes[0]]
        for gap in gaps:
            positions.append(positions[-1] + gap)
        controls.append(median(map(condition, positions)))
    print("Prime sample median:", median(map(condition, primes)))
    print("Shuffle medians (min, median, max):", min(controls), median(controls), max(controls))

if __name__ == "__main__":
    main()
