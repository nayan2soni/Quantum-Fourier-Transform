# Quantum Fourier Transform (QFT) Implementation using Qiskit

This repository contains a Python implementation of the Quantum Fourier Transform (QFT) using Qiskit. The QFT is an essential algorithm in quantum computing, often used in quantum algorithms such as Shor's algorithm for factoring large integers.

## Implementation Details

In this implementation, we build our own gates for the QFT:

1. Single-Qubit Rotation Gate: This gate applies a phase rotation to a single qubit.
2. Controlled Rotation Gate: This gate applies a controlled phase rotation between two qubits.
3. Quantum Fourier Transform Gate: This gate applies the QFT to the entire quantum circuit.

# Requirements
Python 3.7+
Qiskit

# Installation
To install Qiskit, use pip:

pip install qiskit

# Running the Code
To run the QFT implementation, simply execute the script:

python qft_custom_gates.py

This will output the measurement outcomes of the simulated quantum circuit.

You can also use IBM Quantum Lab to run this, hassle free.
