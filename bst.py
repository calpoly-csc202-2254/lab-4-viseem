import sys
from typing import Any, Callable, Union
from dataclasses import dataclass

sys.setrecursionlimit(10**6)

BinTree = Union['Node', None]

@dataclass
class Node:
    element: Any
    left: BinTree = None
    right: BinTree = None

@dataclass(frozen=True)
class frozenBinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree = None

def is_empty(bst: frozenBinarySearchTree) -> bool:
    return bst.tree is None

#insert value into bst and return new tree
def insert(bst: frozenBinarySearchTree, value: Any) -> frozenBinarySearchTree:
    def insert_node(tree: BinTree) -> BinTree:
        if tree is None:
            return Node(value)
        if bst.comes_before(value, tree.element):
            return Node(tree.element, insert_node(tree.left), tree.right)
        else:
            return Node(tree.element, tree.left, insert_node(tree.right))
    return frozenBinarySearchTree(bst.comes_before, insert_node(bst.tree))

#return true if value is found in bst
def lookup(bst: frozenBinarySearchTree, value: Any) -> bool:
    tree = bst.tree
    while tree is not None:
        if not bst.comes_before(value, tree.element) and not bst.comes_before(tree.element, value):
            return True
        elif bst.comes_before(value, tree.element):
            tree = tree.left
        else:
            tree = tree.right
    return False

#delete one occurrence of value from bst and return new tree
def delete(bst: frozenBinarySearchTree, value: Any) -> frozenBinarySearchTree:
    def find_min(tree: BinTree) -> Any:
        while tree.left is not None:
            tree = tree.left
        return tree.element

    def delete_helper(tree: BinTree) -> BinTree:
        if tree is None:
            return None
        if not bst.comes_before(value, tree.element) and not bst.comes_before(tree.element, value):
            if tree.left is None:
                return tree.right
            elif tree.right is None:
                return tree.left
            else:
                successor = find_min(tree.right)
                return Node(successor, tree.left, delete_helper(tree.right))
        elif bst.comes_before(value, tree.element):
            return Node(tree.element, delete_helper(tree.left), tree.right)
        else:
            return Node(tree.element, tree.left, delete_helper(tree.right))

    return frozenBinarySearchTree(bst.comes_before, delete_helper(bst.tree))