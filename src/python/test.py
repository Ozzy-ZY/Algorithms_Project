import random
import time
import copy
import sys
from tabulate import tabulate # type: ignore
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Import the sorting algorithms
# You'll need to adjust this import statement to match your file structure
# If the sorting algorithms are in a file called 'sorting_algorithms.py':
try:
    from main import (
        insertion_sort_iterative,
        insertion_sort_recursive,
        merge_sort_iterative,
        merge_sort_recursive,
        bubble_sort_iterative,
        bubble_sort_recursive
    )
    print(f"{Fore.GREEN}Successfully imported sorting algorithms.{Style.RESET_ALL}")
except ImportError:
    print(f"{Fore.RED}Error importing sorting algorithms. Make sure the file exists and is in the correct location.")
    print(f"{Fore.YELLOW}If your sorting algorithms are in a different file, adjust the import statement.{Style.RESET_ALL}")
    sys.exit(1)

def generate_random_array(size, min_val=-1000, max_val=1000):
    """Generate a random array of integers within the specified range."""
    return [random.randint(min_val, max_val) for _ in range(size)]

def is_sorted(array):
    """Check if an array is sorted in ascending order."""
    return all(array[i] <= array[i+1] for i in range(len(array)-1))

def test_sorting_algorithm(algorithm, array, algorithm_name):
    """Test a sorting algorithm and return execution time and correctness."""
    # Make a copy of the array to avoid modifying the original
    test_array = copy.deepcopy(array)
    
    # Time the algorithm
    start_time = time.time()
    algorithm(test_array)
    end_time = time.time()
    
    # Check if the array is correctly sorted
    correctly_sorted = is_sorted(test_array)
    
    # Also verify against Python's built-in sort
    verification_array = copy.deepcopy(array)
    verification_array.sort()
    matches_builtin = test_array == verification_array
    
    execution_time = end_time - start_time
    
    return {
        "algorithm": algorithm_name,
        "execution_time": execution_time,
        "correctly_sorted": correctly_sorted,
        "matches_builtin": matches_builtin
    }

def run_sorting_tests(array_sizes=[10, 100, 1000]):
    """Run tests on all sorting algorithms with different array sizes."""
    # Dictionary mapping algorithm functions to their names
    algorithms = {
        insertion_sort_iterative: "Insertion Sort (Iterative)",
        insertion_sort_recursive: "Insertion Sort (Recursive)",
        merge_sort_iterative: "Merge Sort (Iterative)",
        merge_sort_recursive: "Merge Sort (Recursive)",
        bubble_sort_iterative: "Bubble Sort (Iterative)",
        bubble_sort_recursive: "Bubble Sort (Recursive)"
    }
    
    all_results = []
    
    # Test each array size
    for size in array_sizes:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Testing with array size: {size}{Style.RESET_ALL}")
        
        # Generate a random array
        test_array = generate_random_array(size)
        
        # Test each algorithm
        size_results = []
        for algorithm, name in algorithms.items():
            # Skip recursive algorithms for large arrays to prevent stack overflow
            if "Recursive" in name and size > 1000:
                print(f"{Fore.YELLOW}Skipping {name} for size {size} to prevent stack overflow.{Style.RESET_ALL}")
                continue
                
            try:
                print(f"{Fore.BLUE}Testing {name}...{Style.RESET_ALL}")
                result = test_sorting_algorithm(algorithm, test_array, name)
                result["array_size"] = size
                size_results.append(result)
                
                # Color based on performance (faster = greener)
                time_color = Fore.GREEN if result["execution_time"] < 0.1 else Fore.YELLOW if result["execution_time"] < 1.0 else Fore.RED
                
                print(f"  {Fore.GREEN}✓{Style.RESET_ALL} {name} took {time_color}{result['execution_time']:.6f}{Style.RESET_ALL} seconds")
                
                if not result["correctly_sorted"] or not result["matches_builtin"]:
                    print(f"  {Fore.RED}⚠️ WARNING: Sorting may be incorrect!{Style.RESET_ALL}")
            except Exception as e:
                print(f"  {Fore.RED}✗ Error testing {name}: {str(e)}{Style.RESET_ALL}")
                size_results.append({
                    "algorithm": name,
                    "array_size": size,
                    "execution_time": float('inf'),
                    "correctly_sorted": False,
                    "matches_builtin": False,
                    "error": str(e)
                })
        
        # Compare with Python's built-in sort
        builtin_array = copy.deepcopy(test_array)
        start_time = time.time()
        builtin_array.sort()
        end_time = time.time()
        builtin_time = end_time - start_time
        
        size_results.append({
            "algorithm": "Python Built-in sort()",
            "array_size": size,
            "execution_time": builtin_time,
            "correctly_sorted": True,
            "matches_builtin": True
        })
        
        time_color = Fore.GREEN if builtin_time < 0.1 else Fore.YELLOW if builtin_time < 1.0 else Fore.RED
        print(f"  {Fore.GREEN}✓{Style.RESET_ALL} Python Built-in sort() took {time_color}{builtin_time:.6f}{Style.RESET_ALL} seconds")
        
        all_results.extend(size_results)
    
    return all_results

def colored_cell(text, is_correct=True, is_time=False, value=None):
    """Format a cell with appropriate color"""
    if is_time and value is not None:
        if value < 0.01:
            return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
        elif value < 0.1:
            return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
        elif value < 1.0:
            return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
        else:
            return f"{Fore.RED}{text}{Style.RESET_ALL}"
    elif not is_correct:
        return f"{Fore.RED}{text}{Style.RESET_ALL}"
    else:
        return text

def print_results_table(results):
    """Print the test results in a nice table format with colors."""
    # Group results by array size
    results_by_size = {}
    for result in results:
        size = result["array_size"]
        if size not in results_by_size:
            results_by_size[size] = []
        results_by_size[size].append(result)
    
    # Print a table for each array size
    for size, size_results in sorted(results_by_size.items()):
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Results for array size {size}:{Style.RESET_ALL}")
        
        # Sort algorithms by execution time
        size_results.sort(key=lambda x: x["execution_time"])
        
        # Prepare table data with colors
        table_data = []
        headers = [f"{Fore.WHITE}{Style.BRIGHT}Algorithm{Style.RESET_ALL}", 
                  f"{Fore.WHITE}{Style.BRIGHT}Time{Style.RESET_ALL}", 
                  f"{Fore.WHITE}{Style.BRIGHT}Correct{Style.RESET_ALL}"]
        
        for result in size_results:
            is_correct = result["correctly_sorted"] and result["matches_builtin"]
            status = f"{Fore.GREEN}✓{Style.RESET_ALL}" if is_correct else f"{Fore.RED}✗{Style.RESET_ALL}"
            
            # Highlight the fastest algorithm
            if result == size_results[0]:  # First result is the fastest after sorting
                algo_name = f"{Fore.GREEN}{Style.BRIGHT}{result['algorithm']}{Style.RESET_ALL}"
            else:
                algo_name = result["algorithm"]
                
            time_str = colored_cell(f"{result['execution_time']:.6f} s", True, True, result['execution_time'])
            
            table_data.append([algo_name, time_str, status])
        
        # Print the table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

def main():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== Sorting Algorithm Test Suite ==={Style.RESET_ALL}")
    print("This script will test various sorting algorithms on random arrays of different sizes.")
    print("The results will be compared to Python's built-in sort function.")
    
    # Default array sizes
    default_sizes = [10, 100, 1000]
    
    # Allow custom array sizes from command line
    if len(sys.argv) > 1:
        try:
            sizes = [int(arg) for arg in sys.argv[1:]]
            print(f"{Fore.BLUE}Using custom array sizes: {sizes}{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.YELLOW}Invalid size arguments. Using default sizes: {default_sizes}{Style.RESET_ALL}")
            sizes = default_sizes
    else:
        print(f"{Fore.BLUE}Using default array sizes: {default_sizes}{Style.RESET_ALL}")
        sizes = default_sizes
    
    # Run the tests
    results = run_sorting_tests(sizes)
    
    # Print the results
    print_results_table(results)
    
    print(f"\n{Fore.GREEN}{Style.BRIGHT}Testing complete!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()