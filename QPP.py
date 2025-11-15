from Operation import Operation
from RunArguments import RunArguments

class QPP:

    _instance = None
    
    def __init__(self):
        """
        Internal class for handling QPP quantum circuits.
        Should not be instantiated by the user.
        """

        if QPP._instance is not None:
            raise RuntimeError("QPP is a singleton class.")
        QPP._instance = self

        self.count = 0
        self.gates = []

    def _add_operation(self, op: Operation):
        """
        Adds a gate to the Quantum program

        gate: Gate, a gate object to add
        """
        QPP._instance.gates.append(gate) # type: ignore

    def run(self, args: RunArguments):
        """
        Runs the quantum program created through QPP
        """
        #TODO: convert this into a Qiskit circuit and execute
        pass

    @staticmethod
    def get_instance():
        """
        Gets the singleton instance of this class
        """
        if QPP._instance is None:
            QPP._instance = QPP()
        
        return QPP._instance