from __future__ import annotations
from typing import List, Callable, Tuple
from .registry import HyperparamRegistry
from .node import TrialNode
import random


def rebuild_naive(registry: HyperparamRegistry,
                  evaluate_fn: Callable,
                  new_dataset) -> HyperparamRegistry:
    """
    Strategy 1 — Re-score every trial and insert one by one.

    WARNING: all_trials() returns nodes in sorted (ascending) order.
    Inserting a sorted sequence into a BST produces a degenerate tree
    (like a linked list), giving O(n²) total time instead of O(n log n).
    This is intentional — you will measure and demonstrate this problem.
    """
    # TODO:
    # 1. Iterate over registry.all_trials()
    # 2. For each node, call evaluate_fn(node.params, new_dataset)
    # 3. Insert into a new HyperparamRegistry
    # 4. Return the new registry
    ...


def rebuild_shuffled(registry: HyperparamRegistry,
                     evaluate_fn: Callable,
                     new_dataset) -> HyperparamRegistry:
    """
    Strategy 2 — Shuffle trials before re-inserting.

    Breaking the sorted order prevents degenerate insertion.
    Expected O(n log n) but the resulting tree is not guaranteed balanced.
    """
    # TODO:
    # 1. Get all trials and shuffle them (random.shuffle)
    # 2. Re-score and insert into a new registry
    ...


def rebuild_balanced(registry: HyperparamRegistry,
                     evaluate_fn: Callable,
                     new_dataset) -> HyperparamRegistry:
    """
    Strategy 3 — Build a perfectly balanced BST using divide & conquer.

    Steps:
    1. Re-score all trials.
    2. Sort by new score — O(n log n).
    3. Call _build_from_sorted() — O(n), guarantees height = floor(log2 n).

    This is the recommended strategy for Phase 2.
    """
    # TODO
    ...


def _build_from_sorted(sorted_trials: List[Tuple[float, dict]]):
    """
    Recursively build a balanced BST from a sorted list of (score, params).

    Algorithm (Divide & Conquer — same structure as merge sort):
    - Base case: empty list → return None
    - Find the middle element → make it the root
    - Recurse on the left half  → left subtree
    - Recurse on the right half → right subtree

    Complexity: O(n) time, O(log n) stack space.
    """
    # TODO
    ...