from Gate import Gate
from Measurement import Measurement
from RunArguments import RunArguments

class QPP:

    def __init__(self):
        """
        Internal class for handling QPP quantum circuits.
        Should not be instantiated by the user.
        """

        self.count = 0
        self.gates = []
        self.measurements = []

    def _allocate(self, count: int) -> int:
        """
        Allocates space for qubits.
        For internal use only.
        
        count: int, number of qubits created

        Returns: int, the starting index of the space allocated.
        """
        
        return_value = self.count
        self.count += count

        return return_value
    
    def _add_gate(self, gate: Gate):
        """
        Adds a gate to the Quantum program

        gate: Gate, a gate object to add
        """
        self.gates.append(gate)

    def _add_measurement(self, measurement: Measurement):
        """
        Adds a measurement to the Quantum program

        measurement: Measurement, a gate object to add
        """
        self.measurements.append(measurement)

    def run(self, args: RunArguments):
        """
        Runs the quantum program created through QPP
        """
        #TODO: convert this into a Qiskit circuit and execute

QuantumMemory = QPP()