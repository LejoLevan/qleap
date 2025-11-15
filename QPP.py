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
    
    @staticmethod
    def get_instance():
        """
        Gets the singleton instance of this class
        """
        if QPP._instance is None:
            QPP._instance = QPP()
        
        return QPP._instance

    @staticmethod
    def _add_operation(op: Operation):
        """
        Adds a gate to the Quantum program

        gate: Gate, a gate object to add
        """
        QPP._instance.gates.append(gate) # type: ignore

    @staticmethod
    def run(args: RunArguments):
        """
        Runs the quantum program created through QPP
        """
        #TODO: convert this into a Qiskit circuit and execute
        pass
