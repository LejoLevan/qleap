from scipy.stats import rv_discrete

from QState import QState
from QPP import QuantumMemory

class Measurement():

    def __init__(self, target: QState):
        """
        targets: List of Qubit objects
        
        Creates a new Gate object and assigns the qubits in targets as its arguments
        """

        self.target = target
        self.result = None
        QuantumMemory._add_measurement(self)

    def measure(self): 
        """
        Measures the target state and determines a random outcome based on the wavefunction
        """
        pass

    def get_distribution(self):
        """
        Returns a probability distribution of measurments outcomes
        """
        
        pass