"""
circuit.py

This module provides the Circuit class, which serves as the main interface for constructing and running quantum circuits using the Circuit framework. 
The Circuit class collects operations, manages qubit allocation, and handles the execution of quantum programs, either through simulation or 
by generating a trace of the program's execution.

"""

from .trace import Trace
from .quantuminterface import QuantumInterface
from .simresult import extract_counts
from .runarguments import RunArguments

class Circuit:
    """Circuit is the main class for running quantum circuits.

    The Circuit class collects operations, manages qubit allocation, and handles the execution of quantum programs, either through simulation or by generating a trace of the program's execution.
    The Circuit class is designed to be used in conjunction with the Operation, QState, and Qubit classes, which are used to construct quantum circuits. 
    When an Operation is created, it is added to the list of operations in the Circuit class. When a QState or Qubit is created, qubits are allocated for it using the private allocate method in the Circuit class.
    """
    
    _operation_count = 0
    _qubit_count = 0

    _operations = []
    _qi = QuantumInterface()
    _results = None

    _measured = set()
    
    _built = False

    @classmethod
    def _add_operation(cls, operation):
        """Private method to add an operation to the list of operations. This is used by the Operation class when an operation is created. Sets _built flag to False to notify that the circuit needs to be rebuilt.

        Parameters
        ----------
        operation : Operation
            The operation to be added to the list of operations.
        """

        cls._operations.append(operation)
        cls._built = False

    @classmethod
    def _allocate(cls, count: int) -> int:
        """Private method to allocate qubits for a QState or Qubit instance. This is used by the QState and Qubit classes when they are created.

        Parameters
        ----------
        count : int
            The number of qubits to allocate.
        
        Returns
        -------
        int
            The starting index of the allocated qubits.
        """
        
        return_value = cls._qubit_count
        cls._qubit_count += count

        return return_value

    @classmethod
    def _record_measurement(cls, qs):
        """Records a QState instance that was measured. This is used by the QState class when a QState instance is measured to keep track of which QState instances to distribute results to when the run() method is called.

        Parameters
        ----------
        qs : QState
            The QState instance that was measured.
        """

        cls._measured.add(qs)

    @classmethod
    def get_results(cls):
        """Gets the results of the most recent simulation. This is used by the QState class to distribute results to the QState instances that were measured.

        Returns
        -------
        simResult
            The results of the most recent simulation, stored as an instance of the SimResult class.
        """

        return cls._results

    @classmethod
    def _build(cls):
        """Builds the quantum circuit that has been constructed through creating qstates and applying operations to them. Sets the _built flag to true to record that the circuit is built.
        """
        cls._qi.create_circuit(numQubits=cls._qubit_count)

        for op in cls._operations:
            op._apply(cls._qi)

        cls._built = True

    @classmethod
    def draw(cls):
        """Draws the quantum circuit that has been constructed by the Circuit class.

        Returns
        -------
        string
            The string representation of the quantum circuit.
        """

        if not cls._built:
            cls._build()

        return cls._qi.draw()

    @classmethod
    def run(cls, args: RunArguments | None = None):
        """Runs the quantum program that has been constructed by the Circuit class. 
        This method simulates the quantum program and distributes results to the QState instances that were measured. 
        If the trace flag is set in the RunArguments, this method generates a trace of the quantum program instead of simulating it.

        Parameters
        ----------
        args : RunArguments, optional
            The arguments for running the quantum program, by default None.

        Returns
        -------
        simResult or Trace
            The results of the simulation as an instance of the SimResult class, or a trace of the quantum program as an instance of the Trace class if the trace flag is set in the RunArguments.
        """
        result = None

        if args is None:
            args = RunArguments()

        result = None
        if args.trace:
            result = cls._run_trace(args)
        else:
            result = cls._run_sim(args)
        
        # Wipe the circuit if needed
        if args.clear:
            cls.clear()

        return result

    @classmethod
    def _run_sim(cls, args):
        """Simulates the quantum program that has been constructed by the Circuit class and distributes results to the QState instances that were measured.

        Parameters
        ----------
        args : RunArguments
             The arguments for running the quantum program, including the number of shots to simulate and whether to generate a trace instead of simulating.

        Returns
        -------
        simResult
            The results of the simulation as an instance of the SimResult class.
        """

        if not cls._built:
            cls._build()

        cls._results = cls._qi.simulate(args.shots)
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
        if len(cls._measured) > 0:
            cls._results.counts = extract_counts(counts, kept_counts)

        return cls._results

    @classmethod
    def _run_trace(cls, args):
        """Generates a trace of the quantum program that has been constructed by the Circuit class. Note: This method requires that no measurements are made in the quantum program.

        Parameters
        ----------
        args : RunArguments
            The arguments for running the quantum program, including the number of shots to simulate and whether to generate a trace instead of simulating.

        Returns
        -------
        Trace
            A trace of the quantum program as an instance of the Trace class.
        """

        cur_state = [0] * (2 ** cls._qubit_count)
        cur_state[0] = 1

        return Trace(cls._operations, cur_state)
    
    @classmethod
    def clear(cls):
        """Clears the state of the Circuit class, including the list of operations, the quantum interface, and the results. This is used to reset the Circuit class after a simulation or trace has been generated. This method does not affect any QState or Qubit objects, just operations.
        """

        cls._operation_count = 0
        cls._qubit_count = 0
        cls._operations.clear()
        cls._measured.clear()
        cls._built = False

    @classmethod
    def toQASM(cls):
        """Converts the quantum program that has been constructed by the Circuit class to openQASM 3.0 code.

        Returns
        -------
        string
            The openQASM 3.0 code.
        """
        if not cls._built:
            cls._build()

        return cls._qi.toQASM()