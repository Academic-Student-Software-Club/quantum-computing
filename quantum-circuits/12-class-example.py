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

qc = QuantumCircuit(3)

qc.ch(0,1)
qc.cry((np.pi)/4,1,2)
print(qc)


psi_in = Statevector.from_label('000')
psi_out = psi_in.evolve(qc.reverse_bits())
psi_out_dict = psi_out.to_dict()
print(" ")
print("Evolution of |000>")
for basis, amplitude in psi_out_dict.items():
    print(f"|{basis}>: {amplitude}")
print("-----")

