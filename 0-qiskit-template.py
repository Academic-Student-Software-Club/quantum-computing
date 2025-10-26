# This file contains the template for 
# all the libraries/initial definitions
# I like using with qiskit.

import numpy as np
# Sets the numpy arrays to truncate numbers with many digits down to 4.
np.set_printoptions(suppress=True,formatter={'all': lambda x: "{:.4g}".format(x)})
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city

from qiskit.circuit.library import HGate
import cmath

NUM_BITS = ""
qc = QuantumCircuit(NUM_BITS)


unitary = Operator(qc.reverse_bits()).data


# This, for every initial state I want, 
# displays the final state(s) 
# as a result of evolution through the circuit.
initial_states=['000','010','100','110','111']
    
for state in initial_states:
    psi_in = Statevector.from_label(state)
    # I had to reverse the bits here to make it a little
    # easier to see. Same answer, just with *our* 
    # notation of qubit order.
    psi_out = psi_in.evolve(qc.reverse_bits())
    psi_out_dict = psi_out.to_dict()
    print(" ")
    print("Evolution of |"+state+">")
    for basis, amplitude in psi_out_dict.items():
        print(f"|{basis}>: {amplitude}")

# This suppresses the tiny tiny numbers 
# that result from Python being Python.
threshold = 1e-10
unitary.real[np.abs(unitary.real) < threshold] = 0
unitary.imag[np.abs(unitary.imag) < threshold] = 0