"""
Problem Set 2 - Master Script
Run all problems at once
"""

import subprocess
import sys
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

print("="*80)
print("PROBLEM SET 2 - GLOBAL BUSINESS ENVIRONMENT")
print("Exchange Rates, Forward Rates, Options, and Money Demand")
print("="*80)
print()

problems = [
    ("Problem 1, Part 1: Exchange Rate Risk Analysis", "problem1_part1_analysis.py"),
    ("Problem 1, Part 2: Switzerland Exchange Rate Data", "problem1_part2_switzerland.py"),
    ("Problem 2: Forward Exchange Rate Analysis", "problem2_forward_rate.py"),
    ("Problem 3: Put Option Analysis", "problem3_put_option.py"),
    ("Problem 4: Domestic Money Demand", "problem4_money_demand.py")
]

def run_problem(name, filename):
    """Run a single problem script"""
    print("\n" + "="*80)
    print(f"RUNNING: {name}")
    print("="*80)
    print()
    
    filepath = os.path.join(script_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"❌ ERROR: File not found: {filepath}")
        return False
    
    try:
        result = subprocess.run(
            [sys.executable, filepath],
            cwd=script_dir,
            capture_output=False,
            text=True
        )
        
        if result.returncode == 0:
            print()
            print(f"✓ {name} completed successfully")
            return True
        else:
            print(f"❌ {name} failed with return code {result.returncode}")
            return False
            
    except Exception as e:
        print(f"❌ Error running {name}: {e}")
        return False

def main():
    """Run all problem scripts"""
    print("This script will run all problem solutions in sequence.")
    print()
    
    response = input("Do you want to run all problems? (y/n): ").strip().lower()
    
    if response != 'y':
        print("\nYou can run individual problems using:")
        for name, filename in problems:
            print(f"  python {filename}")
        return
    
    print("\nStarting problem set execution...")
    print()
    
    results = {}
    
    for name, filename in problems:
        success = run_problem(name, filename)
        results[name] = success
        
        # Add a pause between problems
        if filename != problems[-1][1]:  # Not the last problem
            print("\n" + "-"*80)
            input("Press Enter to continue to next problem...")
    
    # Summary
    print("\n" + "="*80)
    print("EXECUTION SUMMARY")
    print("="*80)
    print()
    
    for name, success in results.items():
        status = "✓ COMPLETED" if success else "❌ FAILED"
        print(f"{status}: {name}")
    
    total = len(results)
    successful = sum(1 for s in results.values() if s)
    
    print()
    print(f"Total: {successful}/{total} problems completed successfully")
    print()
    
    if successful == total:
        print("🎉 All problems completed successfully!")
    else:
        print("⚠️  Some problems encountered errors. Please review the output above.")
    
    print()
    print("="*80)
    print("FILES CREATED:")
    print("="*80)
    print()
    print("Python Scripts:")
    for _, filename in problems:
        print(f"  • {filename}")
    print()
    print("Generated Outputs:")
    print("  • switzerland_exchange_rate.png")
    print("  • problem3_put_option_diagrams.png")
    print("  • problem4_part4_initial.png")
    print("  • problem4_part4_no_accommodation.png")
    print("  • problem4_part6_accommodation.png")
    print()
    print("="*80)

if __name__ == "__main__":
    main()
