from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.circuit.library import UnitaryGate
import numpy as np



# From the lecture notes, we manually obtain
# a unitary U which represents the QFT.
# What our goal is is to construct a circuit such that 
# its end result applies the unitary U on the inputs.

n = 3
i=0
initial_states= ['000','001','010','011','100','101','110','111']
while i<n:
    for state in initial_states:
