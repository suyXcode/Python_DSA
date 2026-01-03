# Guide: How to Measure Time Complexity

This guide helps you quickly analyze time complexity by recognizing common patterns in code.

---

## 1. Loop-Based Patterns

| Pattern | Code Example | Time Complexity |
|--------|--------------|-----------------|
| Single Loop | `for (int i = 0; i < n; i++)` | O(n) |
| Nested Loops | Two loops from 0 to n | O(n²) |
| Triple Nested Loops | Three loops from 0 to n | O(n³) |
| Loop with Increment | `for (int i = 1; i < n; i *= 2)` | O(log n) |
| Loop with Decrement | `for (int i = n; i > 0; i /= 2)` | O(log n) |

---

## 2. Recursive Patterns

| Pattern | Recurrence Relation | Time Complexity |
|--------|---------------------|-----------------|
| Linear Recursion | T(n) = T(n−1) + O(1) | O(n) |
| Binary Recursion | T(n) = 2T(n/2) + O(1) | O(n) |
| Divide & Conquer | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Exponential Recursion | T(n) = T(n−1) + T(n−2) | O(2ⁿ) |

---

## 3. Divide and Conquer Algorithms

| Algorithm | Recurrence | Complexity |
|-----------|------------|------------|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort (Avg) | T(n) = T(n/2) + O(n) | O(n log n) |
| Quick Sort (Worst) | T(n) = T(n−1) + O(n) | O(n²) |

---

## 4. Dynamic Programming

| Pattern | Example | Time Complexity |
|---------|----------|-----------------|
| Memoization | Fibonacci | O(n) |
| Bottom-Up DP | Knapsack, LIS | O(n²) / O(n³) |
| Matrix Chain Multiplication | — | O(n³) |

---

## 5. Graph Algorithms

| Algorithm | Complexity |
|-----------|------------|
| BFS / DFS | O(V + E) |
| Dijkstra (Heap) | O((V + E) log V) |
| Bellman-Ford | O(VE) |
| Floyd Warshall | O(V³) |
| Prim / Kruskal MST | O(E log V) |

---

## 6. Sorting Algorithms

| Algorithm | Best Case | Worst Case |
|-----------|-----------|------------|
| Bubble / Insertion Sort | O(n) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) |

---

## 7. Logarithmic and Amortized Complexities

| Pattern | Example | Complexity |
|---------|----------|------------|
| Binary Search | Sorted array | O(log n) |
| Heap Operations | Priority Queue | O(log n) |
| Balanced BST | AVL / Red-Black | O(log n) |
| Union-Find | DSU | O(α(n)) |

---

## 8. Special Cases

| Case | Complexity |
|------|------------|
| All Subsets | O(2ⁿ) |
| All Permutations | O(n!) |
| All Pairs | O(n²) |

---
