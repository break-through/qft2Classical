from quantum_field import QuantumField
from psi_function import PsiFunction
from probability_expectation import ProbabilityExpectation
from classical_field import ClassicalField

class Simulation:
    def __init__(self, visualizer):
        self.visualizer = visualizer

    def run_simulation(self, parameters):
        # Create a quantum field
        quantum_field = QuantumField('electron', parameters)
        
        # Create the psi function from the quantum field
        psi_function = PsiFunction([quantum_field])
        psi = psi_function.integrate_fields()
        
        # Calculate the probability expectation
        probability_expectation = ProbabilityExpectation(psi)
        probability = probability_expectation.calculate_expectation()
        
        # Convert to classical field
        classical_field = ClassicalField(probability)
        classical_wave = classical_field.to_classical()
        
        # Visualize the classical field
        self.visualizer.plot_field(classical_wave)