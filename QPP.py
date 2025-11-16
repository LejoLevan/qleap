from Operation import Operation
from QuantumInterface import QuantumInterface
from RunArguments import RunArguments

class QPP:
    
    _instance = None
    
    @staticmethod
    def get_instance():
        """
        Gets the singleton instance of this class
        """
        if QPP._instance is None:
            QPP._instance = QPP()
        
        return QPP._instance

    def __init__(self):
        """
        Internal class for handling QPP quantum circuits.
        Should not be instantiated by the user.
        """

        if QPP._instance is not None:
            raise RuntimeError("QPP is a singleton class.")
        QPP._instance = self

        self.operation_count = 0
        self._qubit_count = 0

        self._operations = []
        self._qi = QuantumInterface()

    
    def _add_operation(self, operation: Operation):

        """
        Adds an operation to the Quantum program

        gate: Gate, a gate object to add
        """
        self._operations.append(operation)

    def run(self, args: RunArguments):
        """
        Runs the quantum program created through QPP
        """
        #TODO: convert this into a Qiskit circuit and execute
        self._qi.create_circuit(numQubits=self._qubit_count)
        
        for op in self._operations:
             op._apply(self._qi)