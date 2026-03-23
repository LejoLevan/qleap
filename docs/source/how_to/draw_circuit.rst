How To: Draw Quantum Circuits
=============================

QLeap provides a convenient way to visualize quantum circuits using the `draw()` method. 
This method generates a visual representation of the quantum circuit, showing the qubits, gates, and measurements in a clear and intuitive way.

.. code-block:: python

    from qleap import QLeap, QState, Hadamard, Measurement

    # Create a quantum register with 2 qubits
    qreg = QState(2)

    # Apply gates to the qubits
    Hadamard(qreg[0])
    Hadamard(qreg[1])

    # Measure the qubits
    Measurement(qreg)

    # Run the quantum program
    QLeap.run()

    # Draw the quantum circuit
    QLeap.draw()

In this code, we first create a quantum register with 2 qubits using the `QState` class. We then apply the Hadamard gate to both qubits in the register, putting them into a superposition state. Next, we measure the qubits and run the quantum program.
Finally, we call the `draw()` method of the `QLeap` class to visualize the quantum circuit. The resulting diagram will show the two qubits, the Hadamard gates applied to each qubit, and the measurement operation at the end of the circuit.
The `draw()` method provides a clear and intuitive visualization of the quantum circuit, making it easier to understand the sequence of operations and the structure of the circuit. This can be especially helpful for debugging and for communicating quantum algorithms to others.
