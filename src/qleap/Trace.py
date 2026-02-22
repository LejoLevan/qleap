from typing import Collection

from .QState import QState

class Trace:
   
    def __init__(self, steps: Collection[QState], measure_results):
        """
        Tracethrough of a quantum program

        steps: Collection of QState, each timestep of the execution
        measure_results: the results of the measurements 
        """

        self.current_time = 0
        self.steps = steps

    def step_forward(self):
        """
        Moves one step forward in the execution
        """
        self.current_time += 1

    def step_back(self):
        """
        Moves one step back in the execution
        """
        self.current_time -= 1

    def run_to_end(self):
        """
        Runs to the end of the program
        """
        self.current_time = len(self)

    def restart(self):
        """
        Restarts the program
        """
        self.current_time = 0

    def show_state(self):
        """
        Shows the state at the current time
        """

        #TODO: output the current state nicely

    def __len__(self):
        """
        The number of steps in this trace
        """
        return len(self.steps)