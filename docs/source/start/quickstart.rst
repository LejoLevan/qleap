Quickstart
==========

This example creates a qubit in superposition using the Hadamard gate, then measures the qubit to collapse it back to a classical state. 
The results of the measurement are printed to the console.

.. code-block:: python

    from qleap import Circuit, Qubit, Hadamard, Measurement

    # Create a qubit
    q = Qubit()

    # Apply the Hadamard gate to put the qubit in superposition
    Hadamard(q)

    # Measure the qubit
    Measurement(q)

    # Run the quantum program
    Circuit.run()

    # Print the measurement result
    print(f'Measurement result: {Circuit.get_results()}')

For a more detailed explanation of superposition and the Hadamard gate, see the :doc:`../tutorials/basic_superposition` tutorial.