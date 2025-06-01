from ethical_prompt_chainer import EthicalPromptChainer
from ethical_prompt_chainer.analyzers.example import ExampleAnalyzer

def main():
    # Initialize the chainer with default settings
    chainer = EthicalPromptChainer()
    
    # Create an example dilemma
    dilemma = """
    Should we implement AI-based hiring systems that could improve efficiency
    but might introduce bias in the selection process?
    """
    
    # Define relevant contexts
    contexts = ["technology", "employment", "fairness"]
    
    # Perform the analysis
    analysis = chainer.analyze_dilemma(
        dilemma=dilemma,
        context=contexts
    )
    
    # Print the formatted results
    print("\nEthical Analysis Results:")
    print("=" * 50)
    print(chainer.format_analysis(analysis))
    
    # Demonstrate using a custom analyzer
    print("\nCustom Analyzer Results:")
    print("=" * 50)
    custom_analyzer = ExampleAnalyzer()
    custom_result = custom_analyzer.analyze(dilemma, contexts)
    print(custom_analyzer.format_result(custom_result))

if __name__ == "__main__":
    main() 