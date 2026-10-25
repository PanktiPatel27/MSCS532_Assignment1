"""# MSCS532 Assignment 1: Getting Started

## Overview

This project implements the Insertion Sort algorithm in Python.
The algorithm sorts a list of numbers in monotonically decreasing
order, from largest to smallest.

## Requirements

- Python 3.8 or higher

## Algorithm

The implementation follows the Insertion Sort approach described
in Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein.

The algorithm traverses the array and inserts each element into
its correct position in the already-sorted portion of the array.

For decreasing order, smaller elements are shifted to the right
when they precede the element currently being inserted.

## Example

Input:

[5, 2, 4, 6, 1, 3]

Output:

[6, 5, 4, 3, 2, 1]

## How to Run

Run the program using:

python3 insertion_sort.py

## How to Test

Run the automated tests using:

python3 -m unittest -v

## Complexity Analysis

- Best-case time complexity: O(n)
- Average-case time complexity: O(n^2)
- Worst-case time complexity: O(n^2)
- Auxiliary space complexity: O(1)

The implementation sorts the list in place.

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
Introduction to Algorithms (4th ed.). Random House Publishing Services.
"""