from qleap import QState, Qubit, X, Hadamard, Cnot, Measurement, Circuit

def test_deutsch_jozsa():
    Circuit.clear()
    Circuit._qubit_count = 0

    qin = QState(3)
    qout = Qubit()

    # Check that the qubits were added to the circuit and assigned the correct indices
    assert qin._start == 0
    assert qin._end == 3
    assert qout._start == 3
    assert qout._end == 4

    # Apply the Deutsch-Jozsa algorithm to a balanced function
    X(qout)
    Hadamard(qin, qout)
    Cnot(qin[0], qout)
    Cnot(qin[1], qout)
    Cnot(qin[2], qout)
    Hadamard(qin)
    Measurement(qin)

    # Check that the operations were added to the circuit
    assert len(Circuit._operations) == 7

    # Check that the targets of the operations are correct
    assert isinstance(Circuit._operations[0], X)
    assert Circuit._operations[0]._targets[0]._start == 3
    assert Circuit._operations[0]._targets[0]._end == 4

    assert isinstance(Circuit._operations[1], Hadamard)
    assert Circuit._operations[1]._targets[0]._start == 0
    assert Circuit._operations[1]._targets[0]._end == 3
    assert Circuit._operations[1]._targets[1]._start == 3
    assert Circuit._operations[1]._targets[1]._end == 4  

    assert isinstance(Circuit._operations[2], Cnot)
    assert Circuit._operations[2]._control._start == 0
    assert Circuit._operations[2]._control._end == 1
    assert Circuit._operations[2]._targets[0]._start == 3
    assert Circuit._operations[2]._targets[0]._end == 4

    assert isinstance(Circuit._operations[3], Cnot)
    assert Circuit._operations[3]._control._start == 1
    assert Circuit._operations[3]._control._end == 2
    assert Circuit._operations[3]._targets[0]._start == 3
    assert Circuit._operations[3]._targets[0]._end == 4

    assert isinstance(Circuit._operations[4], Cnot)
    assert Circuit._operations[4]._control._start == 2
    assert Circuit._operations[4]._control._end == 3
    assert Circuit._operations[4]._targets[0]._start == 3
    assert Circuit._operations[4]._targets[0]._end == 4

    assert isinstance(Circuit._operations[5], Hadamard)
    assert Circuit._operations[5]._targets[0]._start == 0
    assert Circuit._operations[5]._targets[0]._end == 3

    assert isinstance(Circuit._operations[6], Measurement)
    assert Circuit._operations[6]._targets[0]._start == 0
    assert Circuit._operations[6]._targets[0]._end == 3

    # Run the quantum program
    result = Circuit.run()

    # Check that the measurement was recorded correctly
    assert len(Circuit._measured) == 1
    assert any(q._start == 0 for q in Circuit._measured)
    assert any(q._end == 3 for q in Circuit._measured)

    # Check that the results were recorded correctly
    assert result is not None
    assert result.counts == {'111': 1024}


