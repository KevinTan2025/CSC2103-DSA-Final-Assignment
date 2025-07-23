# CSC2103 Data Structures and Algorithms - Final Assignment

## 📚 Course Information

- **Course**: CSC2103 - Data Structures and Algorithms
- **Assignment**: Final Assignment
- **Academic Year**: 2025
- **Institution**: Sunway University

## 👥 Team Members

- **Tan Kok Feng** - Team Leader, UX Refinement & Problem 2 (Dijkstra's Algorithm)
- **Yeoh JinWei** - Problem 1 (Binary Search Tree)
- **Ch'ng Shen Ming** - Problem 2 (Dijkstra's Algorithm)
- **Ng Ji Yeung** - Problem 3 (Dynamic Programming)
- **Wong Yu Xuan** - Problem 3 (Dynamic Programming)
- **Wong Wen Ru** - Problem 3 (Dynamic Programming)

## 🎯 Project Overview

This repository contains the implementation of three fundamental data structure and algorithm problems, demonstrating comprehensive understanding of:

- **Tree Data Structures** (Binary Search Trees)
- **Graph Algorithms** (Dijkstra's Shortest Path)
- **Dynamic Programming** (Coin Change Problem)

Each problem is implemented with a focus on educational clarity, comprehensive testing, and user-friendly interfaces.

## 📁 Project Structure

```
CSC2103-DSA-Final-Assignment/
├── main.py                     # 🚀 Unified entry point for all problems
├── README.md                   # 📖 Project documentation
├── pyproject.toml             # 🔧 Python project configuration
├── .gitignore                 # 🚫 Git ignore rules
├── problem1/                  # 🌳 Binary Search Tree Implementation
│   └── main.py               # Complete BST with operations and visualization
├── problem2/                  # 🗺️ Dijkstra's Algorithm Visualization
│   ├── main.py               # Algorithm implementation with step-by-step visualization
│   └── graph_edges.csv       # Graph data for testing
└── problem3/                  # 💰 Dynamic Programming - Coin Change
    └── main.py               # Bottom-up tabulation with breakdown analysis
```

## 🚀 How to Run

### Prerequisites

- Python 3.8 or higher
- No external libraries required (all implementations use built-in Python only)

### Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/KevinTan2025/CSC2103-DSA-Final-Assignment.git
   cd CSC2103-DSA-Final-Assignment
   ```
2. Run the unified entry point:

   ```bash
   python main.py
   ```
3. Choose from the interactive menu:

   - **Option 1**: Binary Search Tree (BST) Implementation
   - **Option 2**: Dijkstra's Algorithm Visualization
   - **Option 3**: Dynamic Programming - Coin Change Problem
   - **Option 4**: View Problems Overview

### Running Individual Problems

You can also run each problem independently:

```bash
# Problem 1: Binary Search Tree
cd problem1 && python main.py

# Problem 2: Dijkstra's Algorithm
cd problem2 && python main.py

# Problem 3: Dynamic Programming
cd problem3 && python main.py
```

## 📋 Problems Detailed Description

### 🌳 Problem 1: Binary Search Tree (BST) Implementation

**Developer**: Yeoh JinWei
**UX Enhancement**: Tan Kok Feng

**Features**:

- Complete BST implementation with insert, delete, and search operations
- Multiple tree traversal methods (In-order, Pre-order, Post-order, Level-order)
- Tree visualization and comprehensive statistics
- Support for multiple data types (integers, floats, strings)
- Interactive command-line interface with comprehensive testing

**Key Algorithms**:

- BST insertion and deletion with proper tree balancing
- Recursive and iterative traversal implementations
- Tree height and node counting algorithms

### 🗺️ Problem 2: Dijkstra's Algorithm Visualization

**Developers**: Tan Kok Feng, Ch'ng Shen Ming

**Features**:

- Complete implementation of Dijkstra's shortest path algorithm
- Custom Min Heap implementation for priority queue functionality
- Step-by-step algorithm visualization showing the process
- Graph data loaded from CSV file for realistic testing
- Interactive path finding with detailed explanations

**Key Algorithms**:

- Dijkstra's shortest path algorithm with priority queue
- Custom Min Heap implementation (heapify, push, pop operations)
- Graph representation using adjacency lists
- Path reconstruction and visualization

### 💰 Problem 3: Dynamic Programming - Coin Change Problem

**Developers**: Ng Ji Yeung, Wong Yu Xuan, Wong Wen Ru
**UX Enhancement**: Tan Kok Feng

**Features**:

- Bottom-up tabulation approach for optimal solution
- Minimum coins calculation with detailed breakdown
- Parent tracking for solution reconstruction
- Comprehensive test cases and validation
- Support for custom coin denominations
- Real-world currency formatting and verification

**Key Algorithms**:

- Dynamic Programming with bottom-up tabulation
- Parent array tracking for solution reconstruction
- Optimal substructure and overlapping subproblems demonstration

## 🧪 Testing

Each problem includes comprehensive testing:

- **Problem 1**: Interactive BST operations with various data types and edge cases
- **Problem 2**: Multiple graph configurations with different shortest path scenarios
- **Problem 3**: Built-in test cases covering standard, edge, and impossible scenarios

All implementations include error handling and input validation for robust user experience.

## 🎨 Design Principles

### Code Quality

- **Clean Code**: Well-documented, readable implementations
- **No External Dependencies**: Pure Python implementations for educational clarity
- **Comprehensive Comments**: Detailed explanations of algorithms and data structures
- **Error Handling**: Robust input validation and exception management

### User Experience

- **Interactive Interfaces**: User-friendly command-line interfaces
- **Visual Feedback**: Progress indicators, formatting, and clear output
- **Educational Value**: Step-by-step explanations and algorithm visualization
- **Consistent Design**: Uniform UI/UX across all problems
