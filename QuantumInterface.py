from qiskit import QuantumCircuit

class QuantumInterface:
    def __init__(self):
        self._qc = None
    
    def create_circuit(self, numQubits):
        numClassicalBits = numQubits
        self._qc = QuantumCircuit(numQubits, numClassicalBits)
    
    def hadamard(self, start, end):
        self.qc.h(range(start, end))
    
    def measure(self, start, end):
        self.qc.measure(range(start, end), range(start, end))
        # maybe have some return??