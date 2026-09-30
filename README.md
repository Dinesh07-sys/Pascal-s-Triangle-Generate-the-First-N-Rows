# Pascal's Triangle

A Python program that generates the first `N` rows of Pascal's Triangle using the values from the previously generated row.

## Overview

Pascal's Triangle is built row by row. Every row begins and ends with `1`, while each inner value is calculated by adding the two values positioned directly above it.

This implementation starts with an empty triangle and constructs each new row from the row immediately before it.

## How It Works

The `generate()` method receives the number of rows:

```python id="u4a7p3"
def generate(self, numRows: int) -> list[list[int]]:
```

An empty list is created to store the completed rows:

```python id="m9v2kd"
triangle: list[list[int]] = []
```

The program then generates one row at a time:

```python id="g3k8qx"
for row in range(numRows):
    current: list[int] = [1] * (row + 1)
```

Every new row is initially filled with `1`s. This automatically handles the first and last elements of each row.

For rows containing inner elements, those positions are calculated using the previous row:

```python id="r7c1nz"
for col in range(1, row):
    current[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
```

The completed row is then added to the triangle:

```python id="p6w4hs"
triangle.append(current)
```

After all requested rows have been generated, the complete triangle is returned.

## Example

For:

```python id="d8k2mz"
numRows = 5
```

the generated triangle is:

```text id="a5f7qn"
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

Each inner number is obtained by adding the two numbers above it.

For example:

```text id="h2j9rx"
    1
   1 1
  1 2 1
```

The `2` comes from:

```text
1 + 1 = 2
```

The same process continues for every subsequent row.

## Example Used in the Program

The provided program generates:

```python id="w3s6kt"
numRows = 8
```

and passes that value directly to `generate()`.

The resulting output contains eight rows of Pascal's Triangle.

## Algorithm

1. Create an empty triangle.
2. Generate each row from `0` to `N - 1`.
3. Initialize the row with `1`s.
4. Calculate each inner value from the two elements above it.
5. Add the completed row to the triangle.
6. Return all generated rows.

## Complexity

For `N` generated rows:

| Metric | Complexity |
|---|---|
| Time | O(N²) |
| Space | O(N²) |

The program calculates every element of the triangle and stores all generated rows in `triangle`.

## Key Concepts

- Nested lists
- Dynamic row construction
- Previous-row dependency
- Nested loops
- Pascal's Triangle
- Basic combinatorial structure

The program prints the generated triangle as a list of lists.
