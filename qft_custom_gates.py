#Python implementation of the Quantum Fourier Transform (QFT) using Qiskit. In this implementation, we'll build our own gates for the QFT:
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Define the single-qubit rotation gate.
def single_qubit_rotation(circuit, qubit, angle):
    circuit.u1(angle, qubit)

# Define the controlled rotation gate
def controlled_rotation(circuit, control_qubit, target_qubit, angle):
    circuit.cu1(angle, control_qubit, target_qubit)

# Define the Quantum Fourier Transform (QFT) gate
def qft(circuit, n):
    for j in range(n):
        circuit.h(j)
        for k in range(j+1, n):
            angle = 2 * np.pi / (2 ** (k - j + 1))
            controlled_rotation(circuit, k, j, angle)

# Create a quantum circuit with 3 qubits
n_qubits = 3
qc = QuantumCircuit(n_qubits)

# Apply the QFT gate to the circuit
qft(qc, n_qubits)

# Measure the qubits
qc.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()

# Get the counts
counts = result.get_counts(qc)
print("Measurement outcome:", counts)
