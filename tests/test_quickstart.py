from qleap import Circuit, Qubit, Hadamard, Measurement

def test_quickstart():
    Circuit.clear()
    Circuit._qubit_count = 0

    q = Qubit()
    Hadamard(q)
    Measurement(q)

    # Check that the operations were added to the circuit 
    assert len(Circuit._operations) == 2
    assert isinstance(Circuit._operations[0], Hadamard)
    assert isinstance(Circuit._operations[1], Measurement)

    # Check that the targets of the operations are correct
    assert Circuit._operations[0]._targets[0]._start == 0
    assert Circuit._operations[0]._targets[0]._end == 1
    assert Circuit._operations[1]._targets[0]._start == 0
    assert Circuit._operations[1]._targets[0]._end == 1

    assert Circuit._qubit_count == 1
    assert Circuit._results is None

    # Run the quantum program
    Circuit.run()

    # Check that the measurement was recorded correctly
    assert len(Circuit._measured) == 1
    assert any(q._start == 0 for q in Circuit._measured)
    assert any(q._end == 1 for q in Circuit._measured)

    # Check that the results were recorded correctly
    assert Circuit._results is not None
    