from Qubit import Qubit
from QPP import QuantumMemory

class QState:

    def __init__(self, length: int):
        """
        Creates a new QState object.

        length: int, how many qubits are in this quantum state.
        """

        self._len = length

        if self._len > 0:
            self._start = QuantumMemory._allocate(length)
            self._end = self._start + length

    def __len__(self):
        """
        Returns the number of qubits in this quantum state.
        """
        return self._len
    
    def __getitem__(self, index):
        """
        Returns a Qubit object for the given index.
        If a slice object is passed, returns a QState object instead.
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
            
            return Qubit(self, index)
    
    def show(self):
        """
        Shows a representation of this QState
        """

        #TODO: make a nice representation of this QState
