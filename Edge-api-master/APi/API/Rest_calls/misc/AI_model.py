import random

import joblib
import pandas as pd
import os
from django.conf import settings

# Load the saved model from a file

def calculate_probabilities(batskill, bowlskill):
    
    #file_ = open(os.path.join(settings.BASE_DIR, 'filename'))
    #print(settings.BASE_DIR)
    file_path = settings.BASE_DIR / 'rest_calls' / 'misc' /'cricket_prediction_model.pkl'
    loaded_model = joblib.load(file_path)

    # Example usage: Predict probabilities for a new input
    new_input = pd.DataFrame({'batsman': [batskill], 'bowler': [bowlskill]})
    probabilities = loaded_model.predict_proba(new_input)
    #print(f"Probabilities: {probabilities}")
    return probabilities[0].tolist()


def calculate_outcome(probabilities):
    cumulative_probabilities = []
    cumulative_sum = 0

    # Calculate cumulative probabilities
    for prob in probabilities:
        cumulative_sum += prob
        cumulative_probabilities.append(cumulative_sum)

    # Generate a random number between 0 and 1
    random_num = random.random()

    # Find the index of the first cumulative probability greater than the random number
    for i, cumulative_prob in enumerate(cumulative_probabilities):
        if random_num < cumulative_prob:
            
            return i
        

    # If no outcome is found, return -1 (optional)
    return -1

# Example usage
