from __future__ import annotations
from typing import List, Optional
from .bst import BST
from .node import TrialNode


class HyperparamRegistry:
    """
    High-level interface around BST for managing hyperparameter trials.
    Provides range queries, top-k retrieval, pruning, and summaries.
    """

    def __init__(self) -> None:
        # TODO: create self._bst = BST() and self._history = []
        ...

    def add_trial(self, score: float, params: dict) -> None:
        """
        Record a new trial: insert into BST and append to history log.

        Collision handling: if a trial with this exact score already exists
        in the BST, the existing params are kept (first-inserted wins) and
        this call is ignored silently. Round scores to 6 decimals before
        calling this method to minimise accidental collisions from
        floating-point noise.
        """
        # TODO
        ...

    def best(self) -> Optional[TrialNode]:
        """Return the highest-scoring trial. Uses BST find_max()."""
        # TODO
        ...

    def worst(self) -> Optional[TrialNode]:
        """Return the lowest-scoring trial. Uses BST find_min()."""
        # TODO
        ...

    def top_k(self, k: int) -> List[TrialNode]:
        """
        Return the k highest-scoring trials in descending order.
        Hint: use a reverse in-order traversal (Right → Node → Left).
        Complexity: O(k + h).
        """
        # TODO: implement self._reverse_inorder and call it here
        ...

    def range_query(self, lo: float, hi: float) -> List[TrialNode]:
        """
        Return all trials with lo <= score <= hi, sorted ascending.
        Hint: use BST pruning — don't explore a subtree if it can't
        contain values in the range.
        Complexity: O(k + h) where k = number of results.
        """
        # TODO: implement self._range and call it here
        ...

    def prune_below(self, threshold: float) -> int:
        """
        Delete all trials with score < threshold.
        Returns the count of deleted nodes.
        Hint: first collect all scores to delete via inorder(),
        then delete them one by one.
        """
        # TODO
        ...

    def all_trials(self) -> List[TrialNode]:
        """Return all trials sorted ascending by score (in-order)."""
        # TODO
        ...

    def summary(self) -> dict:
        """
        Return a dict with: count, best score, worst score,
        mean score, tree height, is_balanced.
        """
        # TODO
        ...

    def _reverse_inorder(self, node, result, k):
        """
        Right → Node → Left traversal, stops when len(result) == k.
        """
        # TODO
        ...

    def _range(self, node, lo, hi, result):
        """
        Collect all nodes with lo <= score <= hi.
        Prune: only go left if node.score > lo;
               only go right if node.score < hi.
        """
        # TODO
        ...