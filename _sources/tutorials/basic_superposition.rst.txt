Basic Superposition
===================

In this tutorial, we will learn how to create basic superposition using the Hadamard gate. The Hadamard gate is a fundamental quantum gate that transforms a qubit from the computational basis to the Hadamard basis. 
When the Hadamard gate is applied to a qubit in the :math:`\ket{0}` state, which is a common use case, it evolves into :math:`\ket{+} = \frac{1}{\sqrt{2}}(\ket{0} + \ket{1})`, which is a equal superposition of the :math:`\ket{0}` and :math:`\ket{1}` states.
We know that they are equally likely to be measured as either :math:`\ket{0}` or :math:`\ket{1}` by squaring the amplitudes.

To create a qubit in superposition using the Hadamard gate, we begin with the following code:

.. code-block:: python

    from qleap import Qleap, Qubit, Hadamard, Measurement

    # Create a Qleap instance
    qleap = Qleap()

    # Create a qubit
    q = Qubit()

    # Apply the Hadamard gate to put the qubit in superposition
    Hadamard(q)

    # Measure the qubit
    Measurement(q)

    # Run the quantum program
    qleap.run()

    # Print the measurement result
    print(f'Measurement result: {qleap.get_results()}')

In this code, we first import the necessary classes from the Qleap library. We create an instance of the Qleap class, which serves as the main interface for building and running quantum programs.
Next, we create a qubit using the Qubit class. By default, the qubit is initialized in the :math:`\ket{0}` state. We then apply the Hadamard gate to the qubit, which puts it into a superposition state.
After applying the Hadamard gate, we measure the qubit using the Measurement class. This collapses the superposition state back to either :math:`\ket{0}` or :math:`\ket{1}` with equal probability.
Finally, we run the quantum program using the `run()` method of the Qleap instance and print the measurement result.

When you run this code, you should see that the measurement result is either 0 or 1, demonstrating that the qubit was in a superposition state before measurement.