from Operation import Operation

class Gate(Operation):
    def __init__(self, target):
        """
        targets: List of Qubit objects
        
        Creates a new Gate object and assigns the qubits in targets as its arguments
        """
        super().__init__(target)