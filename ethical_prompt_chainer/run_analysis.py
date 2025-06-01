"""
Script to run ethical dilemma analysis one at a time.
This allows for cost-effective testing and review of individual dilemmas.
"""

from typing import Optional
from ethical_prompt_chainer import EthicalPromptChainer
from ethical_prompt_chainer.prompts import get_all_dilemmas, get_dilemma

def display_available_dilemmas() -> None:
    """Display all available dilemmas with their keys."""
    dilemmas = get_all_dilemmas()
    print("\nAvailable Ethical Dilemmas:")
    print("-" * 50)
    for key in dilemmas.keys():
        print(f"- {key}")
    print("-" * 50)

def get_user_choice() -> Optional[str]:
    """Get user's choice of dilemma to analyze."""
    while True:
        choice = input("\nEnter the key of the dilemma to analyze (or 'q' to quit): ").strip().lower()
        if choice == 'q':
            return None
        if choice in get_all_dilemmas():
            return choice
        print("Invalid choice. Please try again.")

def run_analysis() -> None:
    """Run the ethical dilemma analysis."""
    chainer = EthicalPromptChainer()
    
    while True:
        # Display available dilemmas
        display_available_dilemmas()
        
        # Get user's choice
        choice = get_user_choice()
        if choice is None:
            print("\nExiting analysis...")
            break
            
        # Get and display the chosen dilemma
        dilemma = get_dilemma(choice)
        print("\nAnalyzing the following dilemma:")
        print("-" * 50)
        print(dilemma)
        print("-" * 50)
        
        # Confirm before proceeding
        proceed = input("\nProceed with analysis? (y/n): ").strip().lower()
        if proceed != 'y':
            print("Skipping this dilemma...")
            continue
            
        # Run the analysis
        print("\nRunning analysis...")
        analysis = chainer.analyze_dilemma(dilemma)
        
        # Display the results
        print("\nAnalysis Results:")
        print("=" * 50)
        print(chainer.format_analysis(analysis))
        print("=" * 50)
        
        # Ask if user wants to continue
        continue_analysis = input("\nAnalyze another dilemma? (y/n): ").strip().lower()
        if continue_analysis != 'y':
            print("\nExiting analysis...")
            break

if __name__ == "__main__":
    print("Welcome to the Ethical Dilemma Analysis Tool")
    print("This tool will help you analyze ethical dilemmas one at a time.")
    run_analysis() 