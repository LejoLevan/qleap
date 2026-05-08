GitHub
======

This page provides basic description on what Developers should expect from 
the GitHub repository page.

https://github.com/LejoLevan/qleap

Advanced Documentaiton
----------------------

This website only contains API reference on public classes and methods. In order to understand the codebase in such a way that is needed
to be able to develop the language, the src\\qleap directory contains sourcee code that has everything docstringed. Use the Architecture page on this website
to understand the basic organization.

Navigation
----------

The GitHub repository is organized into several directories, each serving a specific purpose:

- The "dev" directory contains QLeap written code that was developed to experiment with the language and identify needed areas of improvement. Noteablely contains research level code that was adapted from Qiskit into QLeap in the research subdirectory.

- The "docs" directory contains sphinx related subdirectories that are used to generate documentation. It also contains files related to the language's UML diagram

- The "src" directory contains the language's source code.

- The "test" directory contains integration unit testing that are utilized by GitHub Action workflows.
