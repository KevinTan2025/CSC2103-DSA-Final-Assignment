'''
CSC2103 Data Structures and Algorithms - Final Assignment
Unified Entry Point for All Problems

Team Members:
- Tan Kok Feng (Team Leader, UX Refinement & Problem 2 - Dijkstra's Algorithm)
- Yeoh JinWei (Problem 1 - Binary Search Tree)
- Ch'ng Shen Ming (Problem 2 - Dijkstra's Algorithm)
- Ng Ji Yeung (Problem 3 - Dynamic Programming)
- Wong Yu Xuan (Problem 3 - Dynamic Programming)  
- Wong Wen Ru (Problem 3 - Dynamic Programming)


Course: CSC2103 - Data Structures and Algorithms
Assignment: Final Assignment
Academic Year: 2025
'''

import os
import sys
import subprocess

def display_header():
    """Display the main program header with team information"""
    print("\n" + "="*80)
    print(" CSC2103 DATA STRUCTURES AND ALGORITHMS - FINAL ASSIGNMENT")
    print("="*80)
    print("🎓 Course: CSC2103 - Data Structures and Algorithms")
    print("📚 Assignment: Final Assignment (Academic Year 2025)")
    print("\n👥 Team Members:")
    print("   • Tan Kok Feng      - Team Leader, UX Refinement & Problem 2 (Dijkstra's Algorithm)")
    print("   • Yeoh JinWei      - Problem 1 (Binary Search Tree)")
    print("   • Ch'ng Shen Ming   - Problem 2 (Dijkstra's Algorithm)")
    print("   • Ng Ji Yeung       - Problem 3 (Dynamic Programming)")
    print("   • Wong Yu Xuan      - Problem 3 (Dynamic Programming)")
    print("   • Wong Wen Ru       - Problem 3 (Dynamic Programming)")
    print("="*80)

def display_problems_overview():
    """Display overview of all problems"""
    print("\n📋 PROBLEMS OVERVIEW:")
    print("="*80)
    
    print("\n🌳 Problem 1: Binary Search Tree (BST) Implementation")
    print("   • Complete BST with insert, delete, search operations")
    print("   • Tree traversal methods (In-order, Pre-order, Post-order)")
    print("   • Tree visualization and statistics")
    print("   • Support for integers, floats, and strings")
    
    print("\n🗺️  Problem 2: Dijkstra's Algorithm Visualization") 
    print("   • Shortest path algorithm implementation")
    print("   • Custom Min Heap for priority queue")
    print("   • Step-by-step algorithm visualization")
    print("   • Graph data loaded from CSV file")
    
    print("\n💰 Problem 3: Dynamic Programming - Coin Change Problem")
    print("   • Bottom-up tabulation approach")
    print("   • Minimum coins calculation with breakdown")
    print("   • Parent tracking for solution reconstruction")
    print("   • Comprehensive test cases and validation")
    
    print("="*80)

def run_problem(problem_num):
    """Run the specified problem's main program"""
    try:
        problem_path = os.path.join(os.path.dirname(__file__), f"problem{problem_num}")
        
        # Define the actual filenames for each problem
        problem_files = {
            1: "problem1_binarySearchTree.py",
            2: "problem2_dijkstra.py", 
            3: "problem3_dynamicProgramming.py"
        }
        
        if problem_num not in problem_files:
            print(f"❌ Error: Problem {problem_num} not found!")
            return False
            
        main_file = os.path.join(problem_path, problem_files[problem_num])
        
        if not os.path.exists(main_file):
            print(f"❌ Error: {problem_files[problem_num]} not found in problem{problem_num} directory!")
            return False
        
        print(f"\n🚀 Launching Problem {problem_num}...")
        print("="*50)
        
        # Change to the problem directory and run the specific problem file
        original_cwd = os.getcwd()
        os.chdir(problem_path)
        
        # Execute the problem's Python file
        result = subprocess.run([sys.executable, problem_files[problem_num]], 
                              capture_output=False, 
                              text=True)
        
        # Change back to original directory
        os.chdir(original_cwd)
        
        if result.returncode != 0:
            print(f"\n⚠️  Problem {problem_num} exited with return code {result.returncode}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error running Problem {problem_num}: {str(e)}")
        return False

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("📚 MAIN MENU - Choose a Problem to Run:")
    print("="*50)
    print("1. 🌳 Problem 1 - Binary Search Tree (BST)")
    print("2. 🗺️  Problem 2 - Dijkstra's Algorithm")
    print("3. 💰 Problem 3 - Dynamic Programming (Coin Change)")
    print("4. 📋 View Problems Overview")
    print("0. 👋 Exit Program")
    print("="*50)

def main():
    """Main program loop"""
    try:
        # Display header information
        display_header()
        display_problems_overview()
        
        while True:
            display_menu()
            
            try:
                choice = input("Enter your choice (0-4): ").strip()
                
                if choice == '0':
                    print("\n" + "="*50)
                    print("👋 Thank you for exploring our DSA Final Assignment!")
                    print("   Created by: CSC2103 Team")
                    print("   Course: Data Structures and Algorithms")
                    print("="*50)
                    break
                
                elif choice in ['1', '2', '3']:
                    problem_num = int(choice)
                    success = run_problem(problem_num)
                    
                    if success:
                        print(f"\n✅ Problem {problem_num} completed successfully!")
                    
                    input("\nPress Enter to return to main menu...")
                
                elif choice == '4':
                    display_problems_overview()
                    input("\nPress Enter to return to main menu...")
                
                else:
                    print("❌ Invalid choice. Please enter 0, 1, 2, 3, or 4.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Program interrupted by user. Goodbye!")
                break
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
            except Exception as e:
                print(f"❌ An error occurred: {str(e)}")
                
    except KeyboardInterrupt:
        print("\n\n👋 谢谢使用我们的 DSA Final Assignment，再见！")
        print("Thank you for using our DSA Final Assignment, goodbye!")

if __name__ == "__main__":
    main()
