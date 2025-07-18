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

    def delete(self, data: Any) -> bool:
        '''
        Delete data from BST maintaining BST property
        Returns True if deletion successful, False if not found
        '''
        self.operation_count += 1
        initial_size = self.size
        self.root = self._delete_recursive(self.root, data)
        if self.size < initial_size:
            return True
        return False

    def _delete_recursive(self, node: Optional[BSTNode], data: Any) -> Optional[BSTNode]:
        # Helper method for recursive deletion
        if node is None:
            return None

        try:
            if data < node.data:
                node.left = self._delete_recursive(node.left, data)
            elif data > node.data:
                node.right = self._delete_recursive(node.right, data)
            else:
                # Node to be deleted found
                self.size -= 1

                # Case 1: Node with no children
                if node.left is None and node.right is None:
                    return None

                # Case 2: Node with one child
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Case 3: Node with two children
                else:
                    # Find inorder successor (smallest in right subtree)
                    successor = self._find_min(node.right)
                    node.data = successor.data
                    node.right = self._delete_recursive(node.right, successor.data)
                    self.size += 1  # Adjust since we'll decrement again

            return node
        except TypeError:
            return node

    def _find_min(self, node: BSTNode) -> BSTNode:
        # Find minimum value node in subtree
        while node.left is not None:
            node = node.left
        return node

    def _find_max(self, node: BSTNode) -> BSTNode:
        # Find maximum value node in subtree
        while node.right is not None:
            node = node.right
        return node

    def inorder_traversal(self) -> List[Any]:
        # Return inorder traversal (sorted order)
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[BSTNode], result: List[Any]):
        # Helper method for inorder traversal
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self) -> List[Any]:
        # Return preorder traversal
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[BSTNode], result: List[Any]):
        # Helper method for preorder traversal
        if node is not None:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self) -> List[Any]:
        # Return postorder traversal
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[BSTNode], result: List[Any]):
        # Helper method for postorder traversal
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

    def get_height(self) -> int:
        # Calculate height of the tree
        return self._height_recursive(self.root)

    def _height_recursive(self, node: Optional[BSTNode]) -> int:
        # Helper method for height calculation
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left),
                       self._height_recursive(node.right))

    def find_range(self, min_val: Any, max_val: Any) -> List[Any]:
        # Find all values in given range [min_val, max_val]
        result = []
        self._range_search(self.root, min_val, max_val, result)
        return result

    def _range_search(self, node: Optional[BSTNode], min_val: Any, max_val: Any, result: List[Any]):
        # Helper method for range search
        if node is None:
            return

        try:
            if min_val <= node.data <= max_val:
                result.append(node.data)

            if node.data > min_val:
                self._range_search(node.left, min_val, max_val, result)

            if node.data < max_val:
                self._range_search(node.right, min_val, max_val, result)
        except TypeError:
            pass

    def get_statistics(self) -> dict:
        # Get comprehensive tree statistics
        if not self.root:
            return {"size": 0, "height": 0, "operations": self.operation_count}

        return {
            "size": self.size,
            "height": self.get_height(),
            "operations": self.operation_count,
            "is_balanced": self._is_balanced(),
            "min_value": self._find_min(self.root).data if self.root else None,
            "max_value": self._find_max(self.root).data if self.root else None,
        }
