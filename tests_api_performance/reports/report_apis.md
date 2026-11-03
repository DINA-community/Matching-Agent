# Test Report – API Load Test with Increasing Number of Users

*(based on `common.py`)*

---

## 1. Test Objective

The objective of the load test was to evaluate the system behavior under increasing concurrent usage. For this purpose, four load levels were analyzed: 10, 30, 50, and 100 users. The following aspects were examined in particular:

- Number of successfully processed requests
- Error rate
- Average response time
- Median
- 95th and 99th percentile
- Overall throughput

The reports show that no requests failed in any of the four test runs.

The following APIs were tested:

- Asset Synchronizer (`assetsync`)
  - Default API: <http://0.0.0.0:8992>
- CSAF Synchronizer (`csafsync`)
  - Default API: <http://0.0.0.0:8991>
- Matcher
  - Default API: <http://0.0.0.0:8998>

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

## 3. Summary of Measured Results

| Load Level | Total Requests | Errors | Avg. Response Time | Median | P95 | P99 | Max | Overall Throughput |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 Users | 428 | 0 | 578.82 ms | 9 ms | 640 ms | 5,900 ms | 66,655 ms | 4.03 RPS |
| 30 Users | 682 | 0 | 180.52 ms | 13 ms | 900 ms | 3,000 ms | 4,257 ms | 11.67 RPS |
| 50 Users | 897 | 0 | 235.70 ms | 18 ms | 1,000 ms | 4,400 ms | 4,868 ms | 14.73 RPS |
| 100 Users | 2,912 | 0 | 433.44 ms | 25 ms | 2,300 ms | 6,400 ms | 9,990 ms | 25.46 RPS |

These values are based on the aggregated Locust statistics from the four HTML reports.

## 4. Evaluation of the Results

The tests demonstrate stable system behavior under load, as no errors occurred in any of the four runs. This is the most important positive outcome: even with 100 concurrent users, all requests were processed successfully.

As expected, throughput increases with the number of users. It rises from 4.03 requests per second with 10 users to 25.46 requests per second with 100 users. At the same time, the total number of processed requests increases significantly from 428 to 2,912. This indicates that the system is fundamentally capable of handling additional load.

The response times show a differentiated picture. The run with 30 users achieved the best average value at 180.52 ms. With 50 users, the average increased moderately to 235.70 ms, and with 100 users to 433.44 ms. At the same time, the higher percentiles also increased significantly: the 95th percentile rose from 640 ms at 10 users to 2,300 ms at 100 users, while the 99th percentile increased from 5,900 ms to 6,400 ms. This shows that the system remains stable, but produces more slow outliers under higher load.

A noticeable result appears in the 10-user run: despite the relatively low load, the average response time of 578.82 ms is higher than in the 30-user and 50-user runs, and the maximum value reaches 66,655 ms. This is not typical scaling behavior. In this report, the request `csafsync_api: /token` in particular stands out, with an average response time of around 63.6 seconds, which explains the significantly elevated average value in this test run.

## 5. Critical Endpoints Under Higher Load

In the test with **100 users**, the following endpoints were particularly critical in terms of response time:

- `matcher_api: /matches/` with an average of **1,840 ms** and P95 of **5,200 ms**
- `matcher_api: /matches/ (for id lookup)` with an average of **1,783 ms** and P95 of **6,000 ms**
- `csafsync_api: /task/status` with an average of **940 ms** and P95 of **4,900 ms**
- `csafsync_api: /task/stop` with an average of **953 ms** and P95 of **6,300 ms**

These endpoints represent the greatest response-time risks in the 100-user test.

## 6. Overall Conclusion

The tested system showed robust and error-free behavior across all four load levels, as not a single request failed. The application is therefore functionally resilient even under increased load.

As the number of users increases, throughput rises significantly, but response times also increase, especially in the higher percentiles. Up to 50 users, the overall behavior remains well manageable. With 100 users, the system still remains stable, but with noticeably higher response times and individual slow requests in the range of several seconds.

Particular attention should be paid to the anomaly in the 10-user test, which is not caused by general overload but by a single very slow request. For further optimization, special focus should therefore be placed on the endpoints around `/matches/` as well as the CSAF synchronization paths.

## 7. Brief Assessment

The system operates without errors at all tested load levels. Scaling up to 100 concurrent users is fundamentally possible. Under high load, however, response times increase, especially for matching and synchronization operations. Targeted performance optimization of these endpoints is recommended in order to further stabilize response times at higher load levels.
