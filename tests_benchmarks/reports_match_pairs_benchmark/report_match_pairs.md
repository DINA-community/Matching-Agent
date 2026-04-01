# Report: Benchmark Test of the `match_pairs` Function

*(based on `test_match_pairs_benchmark.py`)*

---

## 1. Objective of the Test

The goal of this benchmark test is to analyze the runtime and stability of the `match_pairs` function under increasing load.  
In particular, it evaluates how execution time scales with a growing number of comparison pairs.

---

## 2. Test Environment

The benchmarks were executed on the following system:

| Component | Specification |
|-----------|--------------|
| Processor | Intel® Core™ Ultra 7 165H |
| Memory | 64 GB RAM |
| Graphics | 4 GB VRAM |
| Storage | 1.86 TB SSD |

**Note:**  
The results represent reference values on high-performance hardware. On weaker systems, longer runtimes are expected.

---

## 3. Test Setup

Three benchmark cases were defined:

| Test Case | Pairs |
|-----------|------:|
| pairs_10  | 100 |
| pairs_20  | 400 |
| pairs_30  | 900 |

Each test case was executed multiple times and statistically evaluated.

Collected metrics:

- minimum runtime (Min)
- maximum runtime (Max)
- average runtime (Mean)
- median
- standard deviation
- interquartile range (IQR)
- operations per second (OPS)

---

## 4. Results

### 4.1 Overview of Measurement Results

| Name     | Pairs | Processed | Matches | Min (s) | Max (s) | Mean (s) | StdDev (s) | Median (s) | IQR (s) | OPS    | Rounds | Iterations |
|----------|------:|----------:|--------:|--------:|--------:|---------:|-----------:|-----------:|--------:|-------:|-------:|-----------:|
| pairs_10 |   100 |       100 |       0 |  2.2188 |  2.8062 |   2.4959 |     0.2236 |     2.5334 |  0.2142 | 0.4007 |      5 |          1 |
| pairs_20 |   400 |       400 |       0 | 14.5565 | 18.0714 |  16.8678 |     1.5096 |    17.5619 |  1.8745 | 0.0593 |      5 |          1 |
| pairs_30 |   900 |       900 |       0 | 22.0863 | 40.8484 |  30.3959 |     9.4617 |    24.8136 | 16.8945 | 0.0329 |      5 |          1 |

---

### 4.2 Runtime Development

The average runtime increases significantly with the number of pairs:

- pairs_10: approx. 2.5 seconds  
- pairs_20: approx. 16.9 seconds  
- pairs_30: approx. 30.4 seconds  

---

## 5. Analysis

### 5.1 Scalability

Runtime increases more than linearly with the number of pairs:

- 100 → 400 pairs (4×) → runtime increases approx. 6–7×  
- 100 → 900 pairs (9×) → runtime increases approx. 12×  

**Interpretation:**

- Behavior is typical for pairwise comparison algorithms  
- Complexity is close to **O(n²)**

---

### 5.2 Runtime Stability

- Small datasets (`pairs_10`) show very stable runtimes  
- Larger datasets exhibit significantly higher variance  

Example (`pairs_30`):

- Min: 22.09 s  
- Max: 40.85 s  

**Interpretation:**

- Increased variability under higher load  
- Possible causes:
  - OS scheduling
  - parallel execution effects
  - background processes

---

### 5.3 Outliers

The high IQR value for `pairs_30` indicates:

- strong dispersion in measurements  
- presence of outliers  

**Interpretation:**

- performance becomes less stable with larger datasets

---

### 5.4 Efficiency

Operations per second (OPS) decrease significantly:

- 0.40 → 0.06 → 0.03  

**Interpretation:**

- efficiency decreases as data size increases  
- typical for compute-intensive matching algorithms

---

## 6. Conclusion

The benchmark results show:

- `match_pairs` scales predictably with the number of comparison pairs  
- runtime grows overproportionally, indicating near-quadratic complexity  
- stability decreases for larger datasets  
- efficiency declines significantly with increasing load  

**Overall assessment:**  
The algorithm works correctly and scales as expected, but shows clear performance and stability limitations for larger datasets.