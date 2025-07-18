'''
CSC2103 Data Structures and Algorithms
Problem 1: Binary Search Tree (BST) Implementation
Author: Yeoh JinWei

This program implements a comprehensive Binary Search Tree with various operations
and visualization capabilities. No built-in libraries are used for core BST operations.
'''

from typing import List, Optional, Any, Tuple # For code documentation and type checking

class BSTNode:
    '''
    Node class for Binary Search Tree
    Each node contains data and pointers to left and right children
    '''
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

    def __str__(self):
        return str(self.data)
