""" 
qstate.py

This module provides the QState class, which represents a multiple qubit quantum state in the QLeap framework.
"""

from .circuit import Circuit

class QState:
    """QState is a class that represents a multiple qubit quantum state in the QLeap framework.
    """


    def __init__(self, length: int):
        """Creates a QState instance with the specified number of qubits. 
        
        This constructor allocates qubits for this QState instance using the private allocate method in the Circuit class.

        Parameters
        ----------
        length : int
            The number of qubits in this quantum state.
        """

        self._len = length

        self._results = dict()

        if self._len > 0:
            self._start = Circuit._allocate(length)
            self._end = self._start + length

    def __len__(self):
        """Returns the number of qubits in this quantum state.

        Returns
        -------
        int
            The number of qubits in this quantum state.
        """
        return self._len
    
    def __getitem__(self, index):
        """Returns either a QState or Qubit object for the given index.

        Parameters
        ----------
        index : int or slice
            If the index is an int, the index of the qubit to return. If the index is a slice, the slice of qubits to return as a new QState object.

        Returns
        -------
        Qubit or QState
            If the index is an int, a Qubit object representing the qubit at the given index is returned. If the index is a slice, a new QState object representing the slice of qubits specified by the index is returned.
        """

        
        if isinstance(index, slice):

            if slice.start >= len(self): # type: ignore
                return

            sliced_state = QState(0)
            sliced_state._start = self._start + index.start
            sliced_state._end = self._start + index.end # type: ignore
            sliced_state._len = sliced_state._end - sliced_state._start
            return sliced_state

        else:

            if index >= len(self):
                raise IndexError(f"Index {int} is out of bounds for QState of length {len(self)}")
            
            from .qubit import Qubit
            return Qubit(self, index)
    
    def _add_result(self, outcome, count):
        """Adds a measurement result to this QState instance. 
        
        This is used by the QState class when a QState instance is measured to keep track of the results of measuring this QState instance.

        Parameters
        ----------
        outcome : int
            The measurement outcome to add
        count : int
            The number of times this outcome occurred
        """

        if outcome not in self._results:
            self._results[outcome] = 0

        self._results[outcome] += count


    def get_results(self):
        """Gets the results of measuring this QState instance. 
        
        Returns
        -------
        dict[int, int]
            A dictionary mapping measurement outcomes to their frequencies.
        """
        return self._results