from QuantumInterface import QuantumInterface
from SimResult import extract_counts

class QPP:
    
    _operation_count = 0
    _qubit_count = 0

    _operations = []
    _qi = QuantumInterface()
    _results = None

    _measured = set()

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
    def record_measurement(cls, qs):
        """
        Records measurement of the given QState
        """
        cls._measured.add(qs)

    @classmethod
    def get_results(cls):
        """
        Returns the results of the most recent simulation, in a dict of {result: count} pairs
        """

        return cls._results

    @classmethod
    def draw(cls):
        """
        Draws the constructed circuit that has already run
        """

        return cls._qi.draw()

    @classmethod
    def run(cls, args=None):
        """
        Runs the quantum program created through QPP

        args: RunArugments object, modifies the run parameters. If omitted,
            uses default arguments.
        """
        cls._qi.create_circuit(numQubits=cls._qubit_count)
        
        for op in cls._operations:
             op._apply(cls._qi)

        cls._results = cls._qi.simulate()
        counts = cls._results.counts

        kept_counts = set()

        # Distribute the results into the qstates
        for qs in cls._measured:

            extract_range = range(qs._start, qs._end)
            kept_counts.update(extract_range)

            extracted_counts = extract_counts(counts, extract_range)

            for count in extracted_counts:
                qs._add_result(count, extracted_counts[count])

        # filter out unmeasured qubits
        cls._results.counts = extract_counts(counts, kept_counts)

        return cls._results

    @classmethod
    def clear(cls):
        """
        Resets the quantum program
        """

        cls._operation_count = 0
        cls._qubit_count = 0
        cls._operations.clear()
        cls._measured.clear()
        cls._results = None