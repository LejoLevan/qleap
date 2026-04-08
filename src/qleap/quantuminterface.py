from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFT
from qiskit.quantum_info import DensityMatrix, Statevector
from qiskit.exceptions import QiskitError
from qiskit_aer import AerSimulator
from qiskit.qasm3 import dumps
from .simresult import SimResult

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
    
    def toffoli(self, control1, control2, target):
        self._qc.ccx(control_qubit1=control1, control_qubit2=control2, target_qubit=target) # type: ignore

    def x(self, start, end):
        self._qc.x(range(start, end)) # type: ignore

    def z(self, start, end):
        self._qc.z(range(start, end))

    def QFT(self, start, end):
        self._qc.compose(QFT(end - start), qubits=range(start, end), inplace=True)

    def invQFT(self, start, end):
        self._qc.compose(QFT(end - start, inverse=True), qubits=range(start, end), inplace=True)

    def swap(self, first, second):
        self._qc.swap(first, second)

    def cswap(self, control, first, second):
        self._qc.cswap(control, first, second)
    
    def measure(self, start, end):
        self._qc.measure(range(start, end), range(start, end)) # type: ignore
    
    def barrier(self, start, end):
        self._qc.barrier(range(start, end)) # type: ignore

    def draw(self):
        print(self._qc)

    def simulate(self, shots):
        """
        Simulates this quantum circuit locally

        Output: counts of the results
        """
        sim = AerSimulator()
        qc_transpiled = transpile(self._qc, sim)

        result = AerSimulator().run(qc_transpiled, shots=shots).result()
        qppResult = SimResult()

        try:
            counts = result.get_counts()
            
            # Fix the order of qubits in the result
            reversed_counts = dict()
            for outcome in counts:
                reversed_counts[outcome[::-1]] = counts[outcome] 

            qppResult.counts = reversed_counts
        except QiskitError:
            pass

        return qppResult
    
    def evolve_density_matrix(self, dmat):
        """
        Evolves density matrix unitarily (no measurements are allowed here)
        """

        rho = DensityMatrix(dmat)
        return rho.evolve(self._qc).data
    
    def evolve_vector(self, vec):
        """
        Evolves statevector unitarily (no measurements are allowed here)
        """

        statevec = Statevector(vec)
        return statevec.evolve(self._qc).data
    
    def measure_vector(self, vec):
        """
        Measures the vector
        """

        statevec = Statevector(vec)
        outcome, result_state = statevec.measure()
        return outcome, result_state.data

    def toQASM(self):
        """
        Generates OPENQASM 3.0 code
        """

        qasm_code = dumps(self._qc)
        return qasm_code