from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


class QuantumInterface:
    def __init__(self):
        self._qc = None
    
    def create_circuit(self, numQubits):
        numClassicalBits = numQubits
        self._qc = QuantumCircuit(numQubits, numClassicalBits)
    
    def hadamard(self, start, end):
        self._qc.h(range(start, end)) # type: ignore
    
    def measure(self, start, end):
        self._qc.measure(range(start, end), range(start, end)) # type: ignore
        # maybe have some return??

    def draw(self):
        print(self._qc)

    def simulate(self):
        """
        Simulates this quantum circuit locally

        Output: counts of the results
        """
        return AerSimulator().run(self._qc).result().get_counts()