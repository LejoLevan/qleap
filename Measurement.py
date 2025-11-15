from scipy.stats import rv_discrete
from typing import Collection

from Operation import Operation
from QState import QState

class Measurement(Operation):

    def __init__(self, targets: Collection[QState]):
        """
        targets: List of Qubit objects
        
        Creates a new Measurement object and assigns the qubits in targets as its arguments
        """

        super().__init__(targets)
        self.result = None

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