"""
Collection of ethical dilemmas for training the reasoning chain.
Each dilemma is structured to test different aspects of ethical reasoning.
"""

ETHICAL_DILEMMAS = {
    "ai_workplace": """
    A tech company has developed an AI system that can predict employee performance and likelihood of leaving. 
    The system uses data from work patterns, communication styles, and even social media activity. 
    Should the company use this system to make decisions about promotions, raises, and retention efforts?
    """,

    "self_driving_car": """
    A self-driving car is approaching a crosswalk where a pedestrian has started to cross. 
    The car can either:
    1. Continue straight and hit the pedestrian
    2. Swerve left and hit a cyclist
    3. Swerve right and hit a barrier, potentially injuring the passenger
    
    What should the car do?
    """,

    "medical_triage": """
    A hospital has limited ventilators during a pandemic. Three patients need immediate ventilation:
    1. A 75-year-old with multiple pre-existing conditions
    2. A 35-year-old healthcare worker with no pre-existing conditions
    3. A 5-year-old child with a rare condition that has a 50% chance of recovery with ventilation

    Who should receive the ventilator?
    """,

    "ai_content_moderation": """
    A social media platform is using AI to detect and remove harmful content. The system has a 95% accuracy rate 
    but occasionally flags legitimate content as harmful. This can affect users' ability to share important 
    information, especially in regions with limited internet access. Should the platform continue using this 
    system, and if so, how should it handle false positives?
    """,

    "data_privacy": """
    A healthcare company has developed an AI that can predict patient health outcomes with 85% accuracy 
    using data from wearable devices. The data includes sensitive information like sleep patterns, 
    exercise habits, and social interactions. Should the company share this data with insurance 
    companies to help them set premiums, even if it could lead to higher costs for high-risk patients?
    """,

    "autonomous_weapons": """
    A military contractor has developed an autonomous drone system that can identify and engage targets 
    without human intervention. The system has a 99% accuracy rate in target identification and can 
    reduce civilian casualties compared to human operators. Should this system be deployed in conflict zones?
    """,

    "ai_art": """
    An AI system has created a piece of art that closely resembles the style of a famous artist. 
    The artwork is being sold for a high price, with no credit given to the original artist's style. 
    Is this ethical? Should there be regulations on AI-generated art that mimics specific artists' styles?
    """,

    "algorithmic_bias": """
    A bank is using an AI system to evaluate loan applications. The system has been trained on historical 
    data and shows a tendency to approve loans for certain demographic groups more than others. 
    However, the bank argues that the system is more accurate than human loan officers. 
    Should the bank continue using this system?
    """,

    "surveillance_society": """
    A city is implementing an AI-powered surveillance system that can detect suspicious behavior 
    in public spaces. The system has reduced crime rates by 30% but has also led to increased 
    monitoring of ordinary citizens. Should the city continue using this system?
    """,

    "ai_education": """
    A school district is considering replacing human teachers with AI tutors for certain subjects. 
    The AI system can provide personalized learning and has shown better test results than traditional 
    teaching methods. However, it may reduce human interaction and emotional support for students. 
    Should the school district implement this system?
    """
}

def get_dilemma(key: str) -> str:
    """
    Get a specific ethical dilemma by key.
    
    Args:
        key: The key of the dilemma to retrieve
        
    Returns:
        The ethical dilemma text
    """
    return ETHICAL_DILEMMAS.get(key, "Dilemma not found")

def get_all_dilemmas() -> dict:
    """
    Get all available ethical dilemmas.
    
    Returns:
        Dictionary of all ethical dilemmas
    """
    return ETHICAL_DILEMMAS.copy()

def add_dilemma(key: str, dilemma: str) -> None:
    """
    Add a new ethical dilemma to the collection.
    
    Args:
        key: Unique identifier for the dilemma
        dilemma: The ethical dilemma text
    """
    ETHICAL_DILEMMAS[key] = dilemma 