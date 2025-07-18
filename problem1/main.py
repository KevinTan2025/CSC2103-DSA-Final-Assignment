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

class BinarySearchTree:
    '''
    Complete Binary Search Tree implementation with comprehensive operations
    Supports integers, floats, and strings with proper comparison
    '''

    def __init__(self):
        self.root: Optional[BSTNode] = None
        self.size = 0
        self.operation_count = 0  # Track operations for analysis

    def insert(self, data: Any) -> bool:
        '''
        Insert data into BST maintaining BST property
        Returns True if insertion successful, False if duplicate
        '''
        self.operation_count += 1
        if self.root is None:
            self.root = BSTNode(data)
            self.size += 1
            return True
        else:
            result = self._insert_recursive(self.root, data)
            if result:
                self.size += 1
            return result

    def _insert_recursive(self, node: BSTNode, data: Any) -> bool:
        # Helper method for recursive insertion
        try:
            if data < node.data:
                if node.left is None:
                    node.left = BSTNode(data)
                    return True
                else:
                    return self._insert_recursive(node.left, data)
            elif data > node.data:
                if node.right is None:
                    node.right = BSTNode(data)
                    return True
                else:
                    return self._insert_recursive(node.right, data)
            else:
                return False  # Duplicate value
        except TypeError:
            print(f"Error: Cannot compare {type(data)} with {type(node.data)}. Please only use 1 data type per tree")
            return False

    def search(self, data: Any) -> bool:
        '''
        Search for data in BST
        Returns True if found, False otherwise
        '''
        self.operation_count += 1
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node: Optional[BSTNode], data: Any) -> bool:
        # Helper method for recursive search
        if node is None:
            return False

        try:
            if data == node.data:
                return True
            elif data < node.data:
                return self._search_recursive(node.left, data)
            else:
                return self._search_recursive(node.right, data)
        except TypeError:
            return False

    