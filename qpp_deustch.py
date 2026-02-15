from Qubit import Qubit
from Hadamard import Hadamard
from Measurement import Measurement
from X import X
from QPP import QPP
from Cnot import Cnot

input_wire = Qubit()
output_wire = Qubit()

def deutsch_function(case: int):
    if case not in [1, 2, 3, 4]:
        raise ValueError("`case` must be 1, 2, 3, or 4.")

    if case in [2, 3]:
        Cnot(input_wire, output_wire)
    if case in [3, 4]:
        X(output_wire)

def compile_circuit(case: int):
    X(output_wire)
    Hadamard(input_wire, output_wire)

    deutsch_function(case)

    Hadamard(input_wire)
    Measurement(input_wire)

def deutsch_algorithm(case: int):
    compile_circuit(case)
    QPP.run()

deutsch_algorithm(4)