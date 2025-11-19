from QuantumInterface import QuantumInterface

class QPP:
    
    _operation_count = 0
    _qubit_count = 0

    _operations = []
    _qi = QuantumInterface()
    
    @classmethod
    def _add_operation(cls, operation):

        """
        Adds an operation to the Quantum program

        gate: Gate, a gate object to add
        """
        cls._operations.append(operation)

    @classmethod
    def _allocate(cls, count: int) -> int:
        """
        Allocates space for qubits.
        For internal use only.
        
        count: int, number of qubits created

        Returns: int, the starting index of the space allocated.
        """
        
        return_value = cls._qubit_count
        cls._qubit_count += count

        return return_value

    @classmethod
    def run(cls, args=None):
        """
        Runs the quantum program created through QPP

        args: RunArugments object, modifies the run parameters. If omitted,
            uses default arguments.
        """
        #TODO: convert this into a Qiskit circuit and execute
        cls._qi.create_circuit(numQubits=cls._qubit_count)
        
        for op in cls._operations:
             op._apply(cls._qi)

        cls._qi.draw()
        print(cls._qi.simulate())

        print("done running")