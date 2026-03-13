from .quantuminterface import QuantumInterface

from math import log2

class Trace:
   
    def __init__(self, steps, start_state):
        """
        Tracethrough of a quantum program

        steps: Collection of arrays representing statevectors, each timestep of the execution
        """

        self.current_time = 0

        self._start_state = start_state
        self.cur_state = start_state

        self.outcomes = list()
        self._premeasured = list()
        self.operations = steps
        
        self._qubit_count = log2(len(start_state))

        self._qi = QuantumInterface()

    def step_forward(self):
        """
        Moves one step forward in the execution
        """
        if self.current_time == len(self.operations):
            return
        
        op = self.operations[self.current_time]
        if op.has_measurement():
            # Do a single measurement, random collapse
            self._premeasured.append(self.cur_state)
            outcome, self.cur_state = self._qi.measure_vector(self.cur_state)
            self.outcomes.append(outcome)

        else:

            # Evolve the state
            self._qi.create_circuit(self._qubit_count)
            op._apply(self._qi)
            self.cur_state = self._qi.evolve_vector(self.cur_state)
        
        self.current_time += 1

    def step_back(self):
        """
        Moves one step back in the execution
        """

        if self.current_time == 0:
            return

        self.current_time -= 1

        op = self.operations[self.current_time]
        if op.has_measurement():
            # Do a single measurement, random collapse
            self.outcomes.pop()
            self.cur_state = self._premeasured.pop()

        else:

            # Evolve the state
            self._qi.create_circuit(self._qubit_count)
            op._apply_inverse(self._qi)
            self.cur_state = self._qi.evolve_vector(self.cur_state)

    def run_to_end(self):
        """
        Runs to the end of the program
        """
        while self.current_time < len(self) - 1:
            self.step_forward()

    def reset(self):
        """
        Restarts the program
        """
        self.current_time = 0
        self.cur_state = self._start_state
        self._premeasured.clear()
        self.outcomes.clear()

    def show_state(self):
        """
        Shows the state at the current time
        """

        #TODO: output the current state nicely
        print(self.cur_state)
        print(f'Measurements: {self.outcomes}')

    def __len__(self):
        """
        The number of steps in this trace
        """
        return len(self.operations) + 1