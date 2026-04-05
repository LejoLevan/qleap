"""
qubit.py

This module provides the Qubit class, which represents a single qubit in the QLeap framework.
"""

from .qstate import QState
from .simresult import extract_counts

class Qubit(QState):
    """Qubit is a class that represents a single qubit in the QLeap framework.
    """

    def __init__(self, qState=None, index=0):
        """Creates a Qubit instance. This constructor can be used in two ways:
        1. If a QState instance is provided, this constructor creates a Qubit instance that represents the qubit at the given index in the provided QState instance. This is used when a Qubit instance is created by indexing a QState instance.
        2. If no QState instance is provided, this constructor creates a new Qubit instance that allocates a new qubit using the private allocate method in the Circuit class. This is used when a Qubit instance is created independently of a QState instance.

        Parameters
        ----------
        qState : QState, optional
            The QState instance from which to initialize this qubit, by default None
        index : int, optional
            The index of the qubit within the QState instance, by default 0
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
