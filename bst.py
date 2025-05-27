from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Optional

@dataclass(frozen=True)
class Node:
    element: Any
    left: Optional[Node] = None
    right: Optional[Node] = None


BinTree = Optional[Node]

@dataclass(frozen=True)
class frozenBinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree = None

#return true if bst has no nodes
def is_empty(bst: frozenBinarySearchTree) -> bool:
    return bst.tree is None

#insert value into bst and return new tree
def insert(bst: frozenBinarySearchTree, value: Any) -> frozenBinarySearchTree:
    def _insert(node: BinTree) -> BinTree:
        if node is None:
            return Node(value)
        if bst.comes_before(value, node.element):
            return Node(node.element, _insert(node.left), node.right)
        else:
            return Node(node.element, node.left, _insert(node.right))
    return frozenBinarySearchTree(bst.comes_before, _insert(bst.tree))

#return true if value is found in bst
def lookup(bst: frozenBinarySearchTree, value: Any) -> bool:
    node = bst.tree
    while node:
        if not bst.comes_before(value, node.element) and not bst.comes_before(node.element, value):
            return True
        node = node.left if bst.comes_before(value, node.element) else node.right
    return False

#delete one occurrence of value from bst and return new tree
def delete(bst: frozenBinarySearchTree, value: Any) -> frozenBinarySearchTree:
    def _find_min(node: Node) -> Any:
        while node.left:
            node = node.left
        return node.element

    def _delete(node: BinTree) -> BinTree:
        if node is None:
            return None
        if not bst.comes_before(value, node.element) and not bst.comes_before(node.element, value):
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = _find_min(node.right)
            return Node(succ, node.left, _delete(node.right))
        if bst.comes_before(value, node.element):
            return Node(node.element, _delete(node.left), node.right)
        else:
            return Node(node.element, node.left, _delete(node.right))

    return frozenBinarySearchTree(bst.comes_before, _delete(bst.tree))
