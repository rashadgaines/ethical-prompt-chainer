import unittest
from ..chainer import EthicalPromptChainer
from ..data_validator import DilemmaValidator
from ..prompts import EthicalPromptTemplates

class TestEnhancedFeatures(unittest.TestCase):
    def setUp(self):
        self.validator = DilemmaValidator()
        self.prompt_templates = EthicalPromptTemplates()
        self.chainer = EthicalPromptChainer(model_name="gpt-4")
    
    def test_dilemma_validation(self):
        # Test valid dilemma
        valid_dilemma = "Should universal basic income be implemented to reduce inequality, or should we maintain targeted welfare programs to avoid disincentivizing work?"
        is_valid, _ = self.validator.validate_dilemma_text(valid_dilemma)
        self.assertTrue(is_valid)
        
        # Test invalid dilemma (too short)
        invalid_dilemma = "UBI or welfare?"
        is_valid, error_msg = self.validator.validate_dilemma_text(invalid_dilemma)
        self.assertFalse(is_valid)
        self.assertIn("too short", error_msg)
        
        # Test invalid dilemma (not a question)
        invalid_dilemma = "Universal basic income versus targeted welfare programs."
        is_valid, error_msg = self.validator.validate_dilemma_text(invalid_dilemma)
        self.assertFalse(is_valid)
        self.assertIn("must be a question", error_msg)
    
    def test_context_identification(self):
        # Test economic context
        economic_dilemma = "Should we implement a carbon tax to reduce emissions, or keep energy costs low for consumers?"
        contexts = self.prompt_templates.identify_dilemma_context(economic_dilemma)
        self.assertIn('economic', contexts)
        
        # Test environmental context
        environmental_dilemma = "Should we ban single-use plastics to protect the environment, or allow their use to keep consumer goods affordable?"
        contexts = self.prompt_templates.identify_dilemma_context(environmental_dilemma)
        self.assertIn('environmental', contexts)
        
        # Test social context
        social_dilemma = "Should we implement universal healthcare to ensure equal access, or maintain private systems for faster service?"
        contexts = self.prompt_templates.identify_dilemma_context(social_dilemma)
        self.assertIn('social', contexts)
    
    def test_issue_extraction(self):
        # Test extraction with "versus"
        dilemma = "Universal basic income versus targeted welfare programs"
        issue_a, issue_b = self.chainer._extract_issues(dilemma)
        self.assertEqual(issue_a, "Universal basic income")
        self.assertEqual(issue_b, "targeted welfare programs")
        
        # Test extraction with "or"
        dilemma = "Should we implement UBI or maintain welfare programs?"
        issue_a, issue_b = self.chainer._extract_issues(dilemma)
        self.assertEqual(issue_a, "Should we implement UBI")
        self.assertEqual(issue_b, "maintain welfare programs?")
    
    def test_contextual_prompt_generation(self):
        # Test economic prompt
        economic_dilemma = "Should we implement a carbon tax to reduce emissions, or keep energy costs low for consumers?"
        issue_a, issue_b = self.chainer._extract_issues(economic_dilemma)
        prompt = self.prompt_templates.get_template("frame_dilemma", economic_dilemma, issue_a, issue_b)
        self.assertIn("economic impacts", prompt)
        
        # Test environmental prompt
        environmental_dilemma = "Should we ban single-use plastics to protect the environment, or allow their use to keep consumer goods affordable?"
        issue_a, issue_b = self.chainer._extract_issues(environmental_dilemma)
        prompt = self.prompt_templates.get_template("frame_dilemma", environmental_dilemma, issue_a, issue_b)
        self.assertIn("environmental sustainability", prompt)

if __name__ == '__main__':
    unittest.main() 