from scipy.stats import rv_discrete
from typing import override

from Operation import Operation
from QState import QState

class Measurement(Operation):

    def __init__(self, *args: QState):
        """
        targets: List of Qubit objects
        
        Creates a new Measurement object and assigns the qubits in targets as its arguments
        """

        super().__init__(args)
        self.result = None
    
    @override
    def _apply(self, qi):
        
        for target in self._targets:
            qi.measure(
                start=target._start, 
                end=target._end
            )

        # maybe anticipate some kind of return assigned to result??

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