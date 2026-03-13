.. qleap documentation master file, created by
   sphinx-quickstart on Wed Mar 11 00:37:50 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

qleap documentation
===================

Qleap is a new quantum programming language developed by our team. The goal of Qleap is to fill the
role of a quantum programming language which is simple, readable, and easy to use. 
Our team designed QLeap with the intention that it is both accessible to newcomers and viable for professional and research applications. 

Quantum computers utilize quantum physics to perform operations that are impossible on
classical computers. With new capabilities, they need new programming languages. 
While several quantum programming languages already exist, such as Qiskit, Qleap focuses on ease of use over performance or synergy with a particular hardware design. Qleap is primarily based on Qiskit, and the backend of Qleap even runs it. 
However, Qleap is designed to beindependent, and its backend may migrate away from Qiskit in a future version. Qleap is not a standalone language, but packaged as a Python library. 
The code can be executed in two ways: simulating the result locally, or exporting to compiled code ready to run on a quantum machine.


.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   installation
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: Tutorials

   tutorials/index

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/index

