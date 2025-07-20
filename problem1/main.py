'''
CSC2103 Data Structures and Algorithms
Problem 1: Binary Search Tree (BST) Implementation
Author: Yeoh JinWei
UX Refinement: Tan Kok Feng

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

        return True # Placeholder to demonstrate program's ability

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

        return True # Placeholder to demonstrate program's ability

def display_menu():
    # Display interactive menu options
    print("\n" + "=" * 70)
    print("BINARY SEARCH TREE OPERATIONS - Interactive Demo")
    print("=" * 70)
    print("📝 Supported data types: integers, floats, strings")
    print("⚠️ Note: Use only ONE data type per tree | No duplicate values allowed")
    print("=" * 70)
    print("🌳 TREE BUILDING:")
    print("1.  Insert multiple nodes (guided input)")
    print("2.  Insert single element")
    print("")
    print("🔍 TREE OPERATIONS:")
    print("3.  Search for element")
    print("4.  Delete element")
    print("5.  Find elements in range")
    print("")
    print("📊 TREE VISUALIZATION & ANALYSIS:")
    print("6.  Display tree structure")
    print("7.  Show inorder traversal (sorted order)")
    print("8.  Show preorder traversal")
    print("9.  Show postorder traversal")
    print("10. Show tree statistics")
    print("")
    print("🧪 TESTING & UTILITIES:")
    print("11. Run automated test cases")
    print("12. Reset/Clear tree")
    print("0.  Exit program")
    print("=" * 70)

def parse_input(user_input: str) -> Any:
    '''
    Parse user input to appropriate data type
    Tries int, then float, then string
    '''
    user_input = user_input.strip()

    # Try integer
    try:
        return int(user_input)
    except ValueError:
        pass

    # Try float
    try:
        return float(user_input)
    except ValueError:
        pass

    # Return as string
    return user_input

def parse_list_input(user_input: str) -> List[Any]:
    # Parse comma-separated list input
    items = [item.strip() for item in user_input.split(',')]
    return [parse_input(item) for item in items if item]

def ask_continue_choice(additional_options: List[str] = None) -> str:
    """
    Unified continue choice function for better UX
    Returns: 'continue', 'home', 'exit', or additional option key
    """
    print("\n" + "=" * 50)
    print("Do you want to continue?")
    
    options = {}
    option_num = 1
    
    # Add additional options if provided
    if additional_options:
        for option in additional_options:
            print(f"{option_num}. {option}")
            options[str(option_num)] = f"option_{option_num}"
            option_num += 1
    
    # Add standard options
    print(f"{option_num}. Back to home")
    options[str(option_num)] = "home"
    option_num += 1
    
    print(f"{option_num}. Exit")
    options[str(option_num)] = "exit"
    
    while True:
        try:
            choice = input(f"\nEnter your choice (1-{len(options)}): ").strip()
            
            if choice in options:
                if options[choice] == "home":
                    return "home"
                elif options[choice] == "exit":
                    print("👋 Thank you for using our BST program!")
                    exit()
                else:
                    return options[choice]
            else:
                print(f"❌ Invalid choice. Please enter a number between 1 and {len(options)}.")
        except KeyboardInterrupt:
            print("\n❌ Operation cancelled. Returning to main menu...")
            return "home"

def guided_multiple_insert(bst: BinarySearchTree) -> None:
    """
    Guided insertion of multiple nodes with better UX
    """
    print("\n" + "=" * 50)
    print("🌳 GUIDED TREE BUILDING")
    print("=" * 50)
    print("This will help you build your tree step by step.")
    print("Examples:")
    print("  • Integers: 50, 30, 70, 20, 40, 60, 80")
    print("  • Floats: 5.5, 3.2, 7.8, 1.1, 9.9")
    print("  • Strings: apple, banana, cherry, date")
    
    # Show current tree state if not empty
    if bst.size > 0:
        print(f"\n📝 Current tree elements: {bst.inorder_traversal()}")
        print(f"🌳 Current tree size: {bst.size} nodes")
    else:
        print("\n🌳 Tree is currently empty")
    
    print("=" * 50)
    
    while True:
        try:
            num_nodes = input("How many nodes would you like to insert? (1-20): ").strip()
            num_nodes = int(num_nodes)
            if 1 <= num_nodes <= 20:
                break
            else:
                print("❌ Please enter a number between 1 and 20.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    print(f"\n📝 Please enter {num_nodes} values one by one:")
    print("💡 Tip: Keep data types consistent (all integers, all floats, or all strings)")
    
    inserted_count = 0
    failed_insertions = []
    
    for i in range(num_nodes):
        while True:
            try:
                value = input(f"  Node {i+1}/{num_nodes}: ").strip()
                if not value:
                    print("❌ Please enter a value.")
                    continue
                
                parsed_value = parse_input(value)
                result = bst.insert(parsed_value)
                
                if result:
                    print(f"  ✅ Successfully added: {parsed_value}")
                    inserted_count += 1
                    break
                else:
                    print(f"  ❌ Failed to add {parsed_value} (duplicate or type mismatch)")
                    failed_insertions.append(parsed_value)
                    
                    retry = input("  Would you like to try a different value? (y/n): ").lower()
                    if retry != 'y':
                        break
                        
            except KeyboardInterrupt:
                print("\n❌ Operation cancelled by user.")
                return
    
    # Summary
    print(f"\n📊 INSERTION SUMMARY:")
    print(f"  ✅ Successfully inserted: {inserted_count} nodes")
    if failed_insertions:
        print(f"  ❌ Failed insertions: {len(failed_insertions)} ({failed_insertions})")
    
    if inserted_count > 0:
        print(f"\n🌳 Current tree structure:")
        print(bst.visualize_tree())
        print(f"\n📝 Current tree (sorted): {bst.inorder_traversal()}")
    
    # Use unified continue choice function
    ask_continue_choice()

def main():
    '''
    Main program function with interactive menu
    Demonstrates all BST operations with user input
    '''
    print("BST Implementation - CSC2103 Data Structures Assignment")
    print("This program demonstrates a complete Binary Search Tree implementation")
    print("with comprehensive operations and visualizations.")

    bst = BinarySearchTree()

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (0-12): ").strip()

            if choice == '0':
                print("👋 Thank you for using our BST program!")
                break

            elif choice == '1':
                guided_multiple_insert(bst)

            elif choice == '2':
                while True:  # Add this loop to stay in single insert mode
                    print("\n🔸 SINGLE ELEMENT INSERTION")
                    print("Example inputs: 42, 3.14, hello")

                    # Show current tree state if not empty
                    if bst.size > 0:
                        print(f"\n📝 Current tree elements: {bst.inorder_traversal()}")
                        print(f"🌳 Tree size: {bst.size} nodes")
                    else:
                        print("\n🌳 Tree is currently empty")

                    value = input("\nEnter element to insert: ").strip()
                    if not value:
                        print("❌ Please enter a value.")
                        continue

                    parsed_value = parse_input(value)
                    result = bst.insert(parsed_value)
                    if result:
                        print(f"✅ Successfully inserted: {parsed_value}")
                        print(f"🌳 Tree size: {bst.size} nodes")

                        # Show current state
                        if bst.size > 1:
                            print(f"📝 Current tree (sorted): {bst.inorder_traversal()}")

                        # Use unified continue choice function with additional option
                        choice_result = ask_continue_choice(["Insert another element"])
                        if choice_result == "option_1":
                            continue  # Continue the while loop (insert again)
                        else:
                            break  # Exit the while loop and return to main menu
                    else:
                        print(f"❌ Failed to insert {parsed_value}")
                        print("💡 Possible reasons: duplicate value or data type mismatch")

                        retry_choice = input("Would you like to try again with a different value? (y/n): ").lower().strip()
                        if retry_choice == 'y':
                            continue  # Continue the while loop to try again
                        else:
                            break  # Exit the while loop and return to main menu

            elif choice == '3':
                while True:  # Add this loop to stay in search mode
                    if bst.size == 0:
                        print("❌ Tree is empty! Please insert some elements first.")
                        break

                    print(f"\n🔍 SEARCH IN TREE")
                    print(f"Current tree elements: {bst.inorder_traversal()}")
                    value = input("Enter element to search: ").strip()
                    if not value:
                        print("❌ Please enter a value.")
                        continue

                    parsed_value = parse_input(value)
                    result = bst.search(parsed_value)
                    if result:
                        print(f"✅ Element '{parsed_value}' FOUND in tree")
                    else:
                        print(f"❌ Element '{parsed_value}' NOT FOUND in tree")

                    # Use unified continue choice function
                    choice_result = ask_continue_choice(["Search another element"])
                    if choice_result == "option_1":
                        continue  # Continue the while loop (search again)
                    else:
                        break  # Exit the while loop and return to main menu

            elif choice == '4':
                while True:  # Add this loop to stay in delete mode
                    if bst.size == 0:
                        print("❌ Tree is empty! Nothing to delete.")
                        break

                    print(f"\n🗑️  DELETE ELEMENT")
                    print(f"Current tree elements: {bst.inorder_traversal()}")
                    value = input("Enter element to delete: ").strip()
                    if not value:
                        print("❌ Please enter a value.")
                        continue

                    parsed_value = parse_input(value)
                    result = bst.delete(parsed_value)
                    if result:
                        print(f"✅ Successfully deleted: {parsed_value}")
                        print(f"🌳 Remaining elements: {bst.inorder_traversal()}")
                    else:
                        print(f"❌ Failed to delete '{parsed_value}' (not found)")

                    # Use unified continue choice function
                    if bst.size > 0:  # Only offer to delete more if tree isn't empty
                        choice_result = ask_continue_choice(["Delete another element"])
                        if choice_result == "option_1":
                            continue  # Continue the while loop (delete again)
                        else:
                            break  # Exit the while loop and return to main menu
                    else:
                        print("🌳 Tree is now empty!")
                        ask_continue_choice()
                        break  # Exit since tree is empty

            elif choice == '5':
                while True:  # Add this loop to stay in range search mode
                    if bst.size == 0:
                        print("❌ Tree is empty! Please insert some elements first.")
                        break

                    print(f"\n🔍 RANGE SEARCH")
                    print(f"Current tree elements: {bst.inorder_traversal()}")
                    min_val = input("Enter minimum value: ").strip()
                    max_val = input("Enter maximum value: ").strip()

                    if not min_val or not max_val:
                        print("❌ Please enter both minimum and maximum values.")
                        continue

                    min_parsed = parse_input(min_val)
                    max_parsed = parse_input(max_val)
                    result = bst.find_range(min_parsed, max_parsed)
                    print(f"📊 Elements in range [{min_parsed}, {max_parsed}]: {result}")

                    # Use unified continue choice function
                    choice_result = ask_continue_choice(["Search another range"])
                    if choice_result == "option_1":
                        continue  # Continue the while loop (search another range)
                    else:
                        break  # Exit the while loop and return to main menu

            elif choice == '6':
                if bst.size == 0:
                    print("❌ Tree is empty! Please insert some elements first.")
                    continue
                print(f"\n🌳 TREE STRUCTURE VISUALIZATION:")
                print("=" * 40)
                print(bst.visualize_tree())
                print("=" * 40)
                
                # Use unified continue choice function
                ask_continue_choice()

            elif choice == '7':
                if bst.size == 0:
                    print("❌ Tree is empty! Please insert some elements first.")
                    continue
                result = bst.inorder_traversal()
                print(f"\n📊 Inorder traversal (sorted): {result}")
                print("💡 This shows elements in ascending order")
                
                # Use unified continue choice function
                ask_continue_choice()

            elif choice == '8':
                if bst.size == 0:
                    print("❌ Tree is empty! Please insert some elements first.")
                    continue
                result = bst.preorder_traversal()
                print(f"\n📊 Preorder traversal: {result}")
                print("💡 This shows: Root → Left → Right")
                
                # Use unified continue choice function
                ask_continue_choice()

            elif choice == '9':
                if bst.size == 0:
                    print("❌ Tree is empty! Please insert some elements first.")
                    continue
                result = bst.postorder_traversal()
                print(f"\n📊 Postorder traversal: {result}")
                print("💡 This shows: Left → Right → Root")
                
                # Use unified continue choice function
                ask_continue_choice()

            elif choice == '10':
                print(f"\n📊 TREE STATISTICS")
                stats = bst.get_statistics()
                print("=" * 40)
                print(f"  📏 Tree size: {stats['size']} nodes")
                print(f"  📐 Tree height: {stats['height']}")
                print(f"  ⚖️  Is balanced: {'Yes' if stats['is_balanced'] else 'No'}")
                print(f"  🔢 Operations performed: {stats['operations']}")
                if stats['size'] > 0:
                    print(f"  📉 Minimum value: {stats['min_value']}")
                    print(f"  📈 Maximum value: {stats['max_value']}")
                print("=" * 40)
                
                # Use unified continue choice function
                ask_continue_choice()

            elif choice == '11':
                print("\n🧪 RUNNING AUTOMATED TEST CASES")
                print("This will demonstrate various BST operations with predefined data...")
                input("Press Enter to continue...")
                BSTTester.run_basic_tests()
                BSTTester.run_edge_case_tests()
                BSTTester.run_type_tests()
                print("\n✅ All test cases completed!")
                
                # Use unified continue choice function
                ask_continue_choice()

            elif choice == '12':
                if bst.size == 0:
                    print("❌ Tree is already empty!")
                    ask_continue_choice()
                    continue
                    
                confirm = input(f"⚠️  Are you sure you want to clear the tree? ({bst.size} nodes will be lost) [y/n]: ").lower()
                if confirm == 'y':
                    bst = BinarySearchTree()
                    print("✅ Tree cleared successfully!")
                else:
                    print("❌ Operation cancelled.")
                
                # Use unified continue choice function
                ask_continue_choice()

            else:
                print("❌ Invalid choice. Please enter a number between 0 and 12.")

        except KeyboardInterrupt:
            print("\n\n⚠️  Program interrupted by user.")
            confirm = input("Do you want to exit? [y/n]: ").lower()
            if confirm == 'y':
                print("👋 Goodbye!")
                break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            print("💡 Please try again or restart the program.")

if __name__ == "__main__":
    main()