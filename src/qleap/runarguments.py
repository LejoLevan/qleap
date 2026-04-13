"""
runarguments.py

This module provides the RunArguments class, which represents the arguments for running a quantum program in the QLeap framework.
"""

class RunArguments:
    """
    RunArguments is a class that represents the arguments for running a quantum program in the QLeap framework. 
    """

    def __init__(self, shots=2**10, trace=False, clear=True):
        """Creates a RunArguments instance with the specified arguments for running a quantum program.

        Parameters
        ----------
        shots : int, optional
            The number of shots to run the quantum program for, by default 2**10
        trace : bool, optional
            Whether to generate a trace of the program's execution, by default False
        """
        self.shots = shots
        self.trace = trace
        self.clear = clear