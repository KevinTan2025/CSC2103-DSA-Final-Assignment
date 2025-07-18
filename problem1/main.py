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

    def _is_balanced(self) -> bool:
        # Check if tree is balanced (height difference <= 1)
        def check_balance(node: Optional[BSTNode]) -> Tuple[bool, int]:
            if node is None:
                return True, 0

            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0

            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0

            height_diff = abs(left_height - right_height)
            is_balanced = height_diff <= 1
            height = 1 + max(left_height, right_height)

            return is_balanced, height

        balanced, _ = check_balance(self.root)
        return balanced

    def visualize_tree(self) -> str:
        '''
        Create a visual representation of the tree
        Returns a formatted string showing tree structure
        '''
        if not self.root:
            return "Empty Tree"

        lines = []
        self._build_tree_string(self.root, 0, True, "", lines)
        return "\n".join(lines)

    def _build_tree_string(self, node: Optional[BSTNode], prefix_len: int,
                           is_tail: bool, prefix: str, lines: List[str]):
        # Helper method for tree visualization
        if node is None:
            return

        if node.right is not None:
            new_prefix = " " * prefix_len + ("    " if is_tail else "│   ")
            self._build_tree_string(node.right, len(new_prefix), False, "┌── ", lines)

        lines.append(" " * prefix_len + prefix + str(node.data))

        if node.left is not None:
            new_prefix = " " * prefix_len + ("    " if is_tail else "│   ")
            self._build_tree_string(node.left, len(new_prefix), True, "└── ", lines)

class BSTTester:
    '''
    Comprehensive testing module for BST operations
    Includes predefined test cases and validation
    '''

    @staticmethod
    def run_basic_tests() -> bool:
        # Run basic functionality tests
        print("=" * 50)
        print("RUNNING BASIC TESTS")
        print("=" * 50)

        bst = BinarySearchTree()
        test_data = [50, 30, 70, 20, 40, 60, 80]

        # Test insertions
        print("Testing insertions:")
        for data in test_data:
            result = bst.insert(data)
            print(f"  Insert {data}: {'Success' if result else 'Failed'}")

        # Test searches
        print("\nTesting searches:")
        for data in test_data:
            result = bst.search(data)
            print(f"  Search {data}: {'Found' if result else 'Not Found'}")

        # Test non-existent search
        result = bst.search(100)
        print(f"  Search 100: {'Found' if result else 'Not Found'}")

        # Test traversals
        print(f"\nInorder traversal: {bst.inorder_traversal()}")
        print(f"Preorder traversal: {bst.preorder_traversal()}")
        print(f"Postorder traversal: {bst.postorder_traversal()}")

        # Test tree visualization
        print("\nTree Structure:")
        print(bst.visualize_tree())

        # Test deletion
        print("\nTesting deletions:")
        delete_values = [20, 30, 50]
        for val in delete_values:
            result = bst.delete(val)
            print(f"  Delete {val}: {'Success' if result else 'Failed'}")
            print(f"  Inorder after deletion: {bst.inorder_traversal()}")

        return True

    @staticmethod
    def run_edge_case_tests() -> bool:
        # Run edge case tests
        print("\n" + "=" * 50)
        print("RUNNING EDGE CASE TESTS")
        print("=" * 50)

        # Test empty tree
        bst = BinarySearchTree()
        print(f"Empty tree search: {bst.search(10)}")
        print(f"Empty tree delete: {bst.delete(10)}")
        print(f"Empty tree height: {bst.get_height()}")

        # Test single node
        bst.insert(42)
        print(f"Single node tree height: {bst.get_height()}")
        print(f"Single node delete: {bst.delete(42)}")
        print(f"Tree size after deletion: {bst.size}")

        # Test duplicate insertions
        bst = BinarySearchTree()
        print(f"First insert 10: {bst.insert(10)}")
        print(f"Duplicate insert 10: {bst.insert(10)}")
        print(f"Tree size: {bst.size}")

        return True

    @staticmethod
    def run_type_tests() -> bool:
        # Test different data types
        print("\n" + "=" * 50)
        print("RUNNING DATA TYPE TESTS")
        print("=" * 50)

        # Test integers
        int_bst = BinarySearchTree()
        int_data = [5, 3, 7, 1, 9, 2, 8]
        for val in int_data:
            int_bst.insert(val)
        print(f"Integer BST inorder: {int_bst.inorder_traversal()}")

        # Test floats
        float_bst = BinarySearchTree()
        float_data = [5.1, 3.2, 7.4, 1.3, 9.9]
        for val in float_data:
            float_bst.insert(val)
        print(f"Float BST inorder: {float_bst.inorder_traversal()}")

        # Test strings
        str_bst = BinarySearchTree()
        str_data = ["university", "keyboard", "data", "sunway", "computer"]
        for val in str_data:
            str_bst.insert(val)
        print(f"String BST inorder: {str_bst.inorder_traversal()}")

        return True

def display_menu():
    # Display interactive menu options
    print("\n" + "=" * 60)
    print("BINARY SEARCH TREE OPERATIONS")
    print("=" * 60)
    print("Supported data types: integers, floats, strings")
    print("Note: Use only one data type per tree & don't use duplicate values")
    print("=" * 60)
    print("1.  Insert element")
    print("2.  Bulk insert from list")
    print("3.  Search element")
    print("4.  Delete element")
    print("5.  Display tree structure")
    print("6.  Show inorder traversal")
    print("7.  Show preorder traversal")
    print("8.  Show postorder traversal")
    print("9.  Find elements in range")
    print("10. Show tree statistics")
    print("11. Run automated test cases")
    print("12. Clear tree")
    print("0.  Exit")
    print("=" * 60)
