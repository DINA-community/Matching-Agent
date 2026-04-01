# Performance Measurement Report for the Matching Agent

*(based on `test_measure_matcher_resources.py`)*

---

## 1. Test Objective

The purpose of the benchmark documented here was to answer the following questions:

- How does the matching runtime scale as the number of comparison pairs increases?
- How heavily are CPU and memory utilized during matching?
- What impact does the distribution of assets and CSAF products have when the total number of pairs is the same?
- At what load level do the first meaningful matches appear?

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
These results represent reference values obtained on high-performance hardware. Correspondingly longer runtimes are to be expected on less powerful systems.

---

## 3. Test Methodology

### 3.1 Measured Metrics

For each run, the test script records the following metrics:

- Number of input comparison pairs
- Number of actually processed pairs
- Number of matches found
- Total runtime in seconds
- Average and maximum CPU utilization
- Average and maximum RAM usage (RSS)

CPU and RAM values are sampled at fixed intervals during execution. This means the benchmark captures not only final values but also the resource utilization behavior over the full runtime.

### 3.2 Generation of Comparison Pairs

For each test run, the loaded assets and CSAF products are combined using a Cartesian product. The total number of comparison pairs is therefore calculated as follows:

`Number of pairs = Number of assets × Number of CSAF products`

### 3.3 Test Series

Four test series were evaluated:

**Test Series A – constant CSAF volume, increasing number of assets**

- 5:30
- 10:30
- 15:30
- 20:30
- 25:30
- 30:30

**Test Series B – constant asset volume, increasing number of CSAF products**

- 30:5
- 30:10
- 30:15
- 30:20
- 30:25
- 30:30

**Test Series C – balanced growth on both sides**

- 5:5
- 10:10
- 15:15
- 20:20
- 25:25
- 30:30

**Test Series D – direct comparison of identical pair counts with different distributions**

- 5:30
- 10:30
- 15:30
- 30:5
- 30:10
- 30:15

---

## 4. Summary of Measurement Results

### 4.1 Key Observations

1. Runtime increases significantly as the number of pairs grows, following an overall clearly understandable and approximately proportional trend.
2. Memory consumption remains very stable across all test series. RAM usage increases only slightly between small and large runs.
3. CPU is the dominant resource factor. Peak utilization ranges from approximately 170% to over 220%, depending on the test series.
4. The distribution of input data has a measurable impact on runtime.
   - 150 pairs in a 5:30 distribution require approximately 2.1 s.
   - 150 pairs in a 30:5 distribution require approximately 3.9 s.
   - This means that, for the same number of pairs, the run with many assets and few CSAF products was slower in this benchmark.
5. Matches occur primarily with larger data volumes. Smaller runs generally produce no matches; at 30:30, all corresponding series produce 10 matches.

---

## 5. Detailed Analysis by Test Series

## 5.1 Test Series A – increasing number of assets with 30 CSAF products

| Combination | Pairs | Runtime (s) | CPU avg (%) | CPU max (%) | Matches | RAM avg (MB) | RAM max (MB) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5:30  | 150 | 2.1 | 75.6 | 148 | 0 | 136.0 | 139.0 |
| 10:30 | 300 | 6.3 | 92.5 | 163 | 0 | 139.8 | 139.9 |
| 15:30 | 450 | 6.8 | 103.0 | 225 | 0 | 140.3 | 140.5 |
| 20:30 | 600 | 8.8 | 109.0 | 187 | 0 | 140.9 | 141.0 |
| 25:30 | 750 | 10.6 | 109.0 | 203 | 0 | 141.1 | 141.3 |
| 30:30 | 900 | 12.8 | 116.0 | 187 | 10 | 141.4 | 141.6 |

**Interpretation:**

- Runtime increases clearly as the number of assets grows.
- From roughly 450 pairs onward, average CPU utilization remains above 100%.
- RAM usage stays practically constant.
- Matches only appear in the largest run.

## 5.2 Test Series B – increasing number of CSAF products with 30 assets

| Combination | Pairs | Runtime (s) | CPU avg (%) | CPU max (%) | Matches | RAM avg (MB) | RAM max (MB) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 30:5  | 150 | 2.2 | 78.0 | 194 | 0 | 136.2 | 139.3 |
| 30:10 | 300 | 4.3 | 92.0 | 194 | 0 | 139.9 | 140.0 |
| 30:15 | 450 | 8.1 | 99.0 | 195 | 0 | 140.3 | 140.4 |
| 30:20 | 600 | 9.1 | 105.0 | 194 | 2 | 140.7 | 140.8 |
| 30:25 | 750 | 10.9 | 108.0 | 171 | 8 | 141.1 | 141.3 |
| 30:30 | 900 | 13.0 | 109.0 | 171 | 10 | 141.5 | 141.7 |

**Interpretation:**

- Here as well, runtime increases as expected with the number of pairs.
- Compared with Test Series A, peak CPU usage is somewhat lower and more consistent.
- The first matches already appear at 600 pairs; after that, the number of matches increases significantly.

## 5.3 Test Series C – balanced growth on both sides

| Combination | Pairs | Runtime (s) | CPU avg (%) | CPU max (%) | Matches | RAM avg (MB) | RAM max (MB) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5:5   | 25  | 0.35 | 14 | 93  | 0 | 131.8 | 138.5 |
| 10:10 | 100 | 2.4  | 69 | 132 | 0 | 139.4 | 139.6 |
| 15:15 | 225 | 4.0  | 74 | 187 | 0 | 140.0 | 140.4 |
| 20:20 | 400 | 5.8  | 97 | 172 | 0 | 140.7 | 140.8 |
| 25:25 | 625 | 9.0  | 110 | 179 | 0 | 141.1 | 141.4 |
| 30:30 | 900 | 13.1 | 110 | 179 | 10 | 141.5 | 141.8 |

**Interpretation:**

- This series shows the most even scaling pattern.
- Small data volumes are processed very quickly.
- Here too, the increase in memory usage is minimal.
- The behavior indicates a robust baseline architecture without noticeable memory-side scaling effects.

## 5.4 Test Series D – identical pair counts, different distributions

This series is particularly relevant because it shows that not only the absolute number of comparison pairs, but also the structure of the input data affects performance.

### Comparison at 150 pairs

| Combination | Runtime (s) | CPU avg (%) | Matches |
|---|---:|---:|---:|
| 5:30  | 2.1 | 75.6 | 0 |
| 30:5  | 3.9 | 80.6 | 0 |

### Comparison at 300 pairs

| Combination | Runtime (s) | CPU avg (%) | Matches |
|---|---:|---:|---:|
| 10:30 | 4.3 | 89.0 | 0 |
| 30:10 | 5.1 | 79.0 | 0 |

### Comparison at 450 pairs

| Combination | Runtime (s) | CPU avg (%) | Matches |
|---|---:|---:|---:|
| 15:30 | 6.4 | 97.0 | 0 |
| 30:15 | 6.7 | 103.0 | 0 |

**Interpretation:**

- For the same number of pairs, the distribution between assets and CSAF products is relevant.
- In this benchmark, runs with many assets and fewer CSAF products tended to be slower.
- This suggests that processing is not fully symmetrical with respect to both input sides in terms of runtime.

---

## 6. Technical Assessment

### 6.1 Scalability

Up to 900 comparison pairs, the Matching Agent shows overall manageable runtime behavior. Measured runtimes of around 13 seconds in the largest test run are generally acceptable for batch-oriented or asynchronously executed matching processes.

### 6.2 CPU Behavior

CPU values above 100% indicate that the process utilizes more than one CPU core. This is positive, as it shows that available compute capacity is being actively used. At the same time, it is clearly evident that computation time — not memory — is the primary bottleneck.

### 6.3 Memory Behavior

Memory usage remains very stable. Across the entire test set, average memory consumption stays roughly within the range of 136 MB to 142 MB. For the customer, this means in particular:

- low main memory requirements,
- good predictability during operation,
- low risk of memory-related instability.

### 6.4 Match Results

The number of matches increases as the data volume grows. This is technically plausible, since a larger number of assets and CSAF products also increases the probability of actual matches. For a reliable assessment of match quality, additional precision/recall evaluations or a professionally validated reference dataset would be advisable.

---

## 7. Conclusions

The following conclusions can be drawn from the benchmark results:

1. The Matching Agent performs well for typical medium-sized data volumes.
2. The primary resource load is on the CPU, not on memory.
3. The system scales in a controlled manner without noticeable resource outliers.
4. The composition of the input data has a measurable impact on runtime. A rough estimate based solely on the number of pairs is therefore insufficient.
5. For productive operation, asynchronous or scheduled batch execution is recommended, especially for larger data sets or frequent re-runs.

---

## 8. Recommendations

### Short term

- Prefer asynchronous execution for matching runs with larger data volumes.
- Focus production monitoring on CPU runtime and throughput.
- Continue to persist results and configurations per run in a traceable manner to ensure reproducibility.

### Medium term

- Conduct additional benchmarks with larger and more realistic data volumes.
- Analyze the cause of runtime differences for identical pair counts in a targeted way.
- Evaluate match quality against a reference dataset from a functional perspective.

### Long term

- Assess whether pre-filtering, caching, or pre-indexing can reduce the number of pairs that actually need to be compared.
- Optionally carry out load tests with parallel matching runs in line with the planned pool size.

---

## 9. Final Assessment

The benchmark shows an overall convincing resource profile for the Matching Agent. Particularly positive aspects are the very stable memory consumption and the clearly understandable runtime scaling. Optimization potential exists primarily in the further analysis of CPU-dominated runtime behavior and in developing a better understanding of how different data distributions affect performance.

Within the tested scale, the Matching Agent is technically viable and shows no critical memory-related bottlenecks.
