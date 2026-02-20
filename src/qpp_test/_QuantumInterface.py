from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from .SimResult import SimResult

class QuantumInterface:
    def __init__(self):
        self._qc = None
    
    def create_circuit(self, numQubits):
        numClassicalBits = numQubits
        self._qc = QuantumCircuit(numQubits, numClassicalBits)
    
    def hadamard(self, start, end):
        self._qc.h(range(start, end)) # type: ignore
    
    def cnot(self, control, target):
        self._qc.cx(control_qubit=control, target_qubit=target) # type: ignore

    def x(self, start, end):
        self._qc.x(range(start, end)) # type: ignore
    
    def measure(self, start, end):
        self._qc.measure(range(start, end), range(start, end)) # type: ignore

    def draw(self):
        print(self._qc)

    def simulate(self):
        """
        Simulates this quantum circuit locally

        Output: counts of the results
        """
        result = AerSimulator().run(self._qc).result()
        counts = result.get_counts()
        
        # Fix the order of qubits in the result
        reversed_counts = dict()
        for outcome in counts:
            reversed_counts[outcome[::-1]] = counts[outcome] 

        qppResult = SimResult()
        qppResult.counts = reversed_counts

        return qppResult
