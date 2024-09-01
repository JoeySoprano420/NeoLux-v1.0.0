Library/import numpy as np

class DP3:
    def __init__(self, initial_state_probabilities):
        self.state_probabilities = np.array(initial_state_probabilities)
        self.transition_matrix = np.zeros((len(initial_state_probabilities), len(initial_state_probabilities)))

    def update_transition_matrix(self, transitions):
        for (i, j), probability in transitions.items():
            self.transition_matrix[i, j] = probability

    def predict_next_state(self):
        return np.argmax(np.dot(self.state_probabilities, self.transition_matrix))

    def update_probabilities(self, observed_state):
        self.state_probabilities = np.dot(self.state_probabilities, self.transition_matrix)
        self.state_probabilities[observed_state] += 1  # Adjust probabilities based on observation
        self.state_probabilities /= np.sum(self.state_probabilities)  # Normalize

# Example usage
dp3 = DP3([0.2, 0.3, 0.5])
dp3.update_transition_matrix({(0, 1): 0.4, (1, 2): 0.6})
print(f"Predicted next state: {dp3.predict_next_state()}")
dp3.update_probabilities(1)
print(f"Updated probabilities: {dp3.state_probabilities}")
