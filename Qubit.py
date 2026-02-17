from QState import QState
from SimResult import extract_counts

class Qubit(QState):

    def __init__(self, qState=None, index=0):
        """
        A QState instance with only a single qubit
        
        QState: optional argument, a QState to intitialzie this qubit from
        index:  optional argument, 0 by default. The index of qState to intialize from
        """
        if qState is not None:
            self._start = qState._start + index
            self._end = self._start + 1
            self._len = 1
            self._results = extract_counts(qState.get_results(), [index])
        else:
            super().__init__(1)

    def __getitem__(self, index):
        """
        Should not be used with Qubit
        """
        raise AttributeError("Qubit cannot be indexed")
