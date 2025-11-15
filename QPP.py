from Operation import Operation
from QuantumInterface import QuantumInterface
from RunArguments import RunArguments

class QPP:
    _operation_count = 0
    _qubit_count = 0

    _operations = []
    _qi = QuantumInterface
    
    @classmethod
    def _add_operation(cls, operation: Operation):
        """
        Adds a gate to the Quantum program

        gate: Gate, a gate object to add
        """
        cls._operations.append(operation)

    @classmethod
    def run(cls, args: RunArguments):
        """
        Runs the quantum program created through QPP
        """
        #TODO: convert this into a Qiskit circuit and execute
        cls._qi.create_circuit(numQubits=cls._qubit_count)
