""" 
quantuminterface.py

This module provides the QuantumInterface class
This module should be the only place the QLeap references a backend (such as Qiskit.)
USERS SHOULD NOT INTERACT WITH THIS CLASS DIRECTLY.
"""

from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFT
from qiskit.quantum_info import DensityMatrix, Statevector
from qiskit.exceptions import QiskitError
from qiskit_aer import AerSimulator
from qiskit.qasm3 import dumps
from .simresult import SimResult

class QuantumInterface:
    """
    This module provides the quantuminterface class, which is the bridge between QLeap and the backend execution of the quantum program (this is currently in Qiskit). 
    This class should be the only place where Qiskit (or any other backend) is directly imported or interacted with by any QLeap file. This is to ensure separation of QLeap and the backend
    and to prevent overreliance on an outside library. Maintaining this practice also allows the backend to be swapped out easily.
    The methods in this class are wrappers for methods from the backend.
    To add another backend (such as Cirq, etc.), the recommnded procedure would be to create another abstract QuantumInterface class that both this and the new quantuminterface inherit from.
    The QuantumInterface used by Circuit can then be set by that class. 
    """
    
    def __init__(self):
        """
        Sets up by creating an empty quantum circuit.
        """
        self._qc = None
    
    def create_circuit(self, numQubits):
        """
        Creates a Qiskit quantum cirucit with the specified number of qubits. Each qubits receives a corresponding classical bit.
        """
        numClassicalBits = numQubits
        self._qc = QuantumCircuit(numQubits, numClassicalBits)
    
    def hadamard(self, start, end):
        """
        Applies a Qiskit Hadamard gate to the specified index ranges.
        """
        self._qc.h(range(start, end)) # type: ignore
    
    def cnot(self, control, target):
        """
        Applies a Qiskit CNOT gate to the specified indices.
        """
        self._qc.cx(control_qubit=control, target_qubit=target) # type: ignore
    
    def toffoli(self, control1, control2, target):
        """
        Applies a Qiskit Toffoli gate to the specified indices.
        """
        self._qc.ccx(control_qubit1=control1, control_qubit2=control2, target_qubit=target) # type: ignore

    def x(self, start, end):
        """
        Applies a Qiskit X gate to the specified indices.
        """
        self._qc.x(range(start, end)) # type: ignore

    def z(self, start, end):
        """
        Applies a Qiskit Z gate to the specified indices.
        """
        self._qc.z(range(start, end))

    def QFT(self, start, end):
        """
        Applies a Qiskit QFT gate to the specified indices.
        """
        self._qc.compose(QFT(end - start), qubits=range(start, end), inplace=True)

    def invQFT(self, start, end):
        """
        Applies a Qiskit Inverse QFT gate to the specified indices.
        """
        self._qc.compose(QFT(end - start, inverse=True), qubits=range(start, end), inplace=True)

    def swap(self, first, second):
        """
        Applies a Qiskit SWAP gate to the specified indices.
        """
        self._qc.swap(first, second)

    def cswap(self, control, first, second):
        """
        Applies a Qiskit CSWAP gate to the specified indices.
        """
        self._qc.cswap(control, first, second)
    
    def measure(self, start, end):
        """
        Applies a Qiskit measurement in the Z basis to the specified indices.
        """
        self._qc.measure(range(start, end), range(start, end)) # type: ignore
    
    def barrier(self, start, end):
        """
        Applies a Qiskit barrier to the specified indices.
        """
        self._qc.barrier(range(start, end)) # type: ignore

    def draw(self):
        """
        Wraps Qiskit draw method to print out the quantum circuit.
        """
        if self._qc is not None:
            print(self._qc)
        else:
            print("No quantum circuit created yet.")


    def simulate(self, shots):
        """
        Simulates this quantum circuit locally using Qiskit and AerSimulaor.

        Parameters
        ----------
        shots : int
            The nubmer of times to run the simulation.

        Returns
        -------
        SimResult
            The results of the simulation.
        """
        sim = AerSimulator()
        qc_transpiled = transpile(self._qc, sim)

        result = AerSimulator().run(qc_transpiled, shots=shots).result()
        qppResult = SimResult()

        try:
            counts = result.get_counts()
            
            # Fix the order of qubits in the result: not backwards like in Qiskit.
            reversed_counts = dict()
            for outcome in counts:
                reversed_counts[outcome[::-1]] = counts[outcome] 

            qppResult.counts = reversed_counts
        except QiskitError:
            pass

        return qppResult
    
    def evolve_density_matrix(self, dmat):
        """
        Evolves a density matrix unitarily according to the constructed circuit. The circuit must contain no measurements or an error will be raised.

        Parameters
        ----------
        dmat : DensityMatrix
            The intial state of the density matrix to evolve

        Returns
        -------
        DensityMatrix
            The evolved density matrix
        """

        rho = DensityMatrix(dmat)
        return rho.evolve(self._qc).data
    
    def evolve_vector(self, vec):
        """
        Evolves a statevector unitarily according to the constructed circuit. The circuit must contain no measurements or an error will be raised.

        Parameters
        ----------
        vec : array-like
            The intial state of the density matrix to evolve

        Returns
        -------
        ndarray
            The evolved statevector
        """

        statevec = Statevector(vec)
        return statevec.evolve(self._qc).data
    
    def measure_vector(self, vec):
        """
        Evolves a statevector unitarily according to the constructed circuit. The circuit must contain no measurements or an error will be raised.

        Parameters
        ----------
        vec : array-like
            The intial state of the density matrix to evolve

        Returns
        -------
        tuple
            the pair (outcome, state) where outcome is the measurement outcome (0, 1, et.c), and state is the collapsed post-measurement state of vec.
        """

        statevec = Statevector(vec)
        outcome, result_state = statevec.measure()
        return outcome, result_state.data

    def toQASM(self):
        """
        Generates OPENQASM 3.0 code

        Returns
        -------
        String
            OPENQASM 3.0 code representation of the QLeap program for porting to quantum hardware.
        """

        qasm_code = dumps(self._qc)
        return qasm_code