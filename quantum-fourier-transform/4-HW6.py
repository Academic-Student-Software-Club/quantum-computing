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

R2 = np.array([[1,0],[0,np.e**(2*np.pi*1j/4)]],dtype=complex)
R2dag = R2.conj().T
R3 = np.array([[1,0],[0,np.e**(2*np.pi*1j/8)]],dtype=complex)
R3dag = R3.conj().T

R2gate = UnitaryGate(R2,label="R2")
R2daggate = UnitaryGate(R2dag,label="R2+")

R3gate = UnitaryGate(R3,label="R3")
R3daggate = UnitaryGate(R3dag,label="R3+")


cR2 = R2gate.control(1,label="")
cR2dag = R2daggate.control(1,label="")

cR3 = R3gate.control(1,label="")
cR3dag = R3daggate.control(1,label="")


qc = QuantumCircuit(3)

qc.h(0)
qc.append(cR2,[1,0])
qc.append(cR3,[2,0])

qc.h(1)
qc.append(cR2,[2,1])

qc.h(2)

qc.swap(0,2)
unitary = Operator(qc)
print("Normal QFT:")
print(qc)

qc.swap(0,2)

qc.h(2)

qc.append(cR2dag,[2,1])
qc.h(1)

qc.append(cR3dag,[2,0])
qc.append(cR2dag,[1,0])
qc.h(0)
print(qc)

unitary = Operator(qc).data
threshold = 1e-10
unitary.real[np.abs(unitary.real) < threshold] = 0
unitary.imag[np.abs(unitary.imag) < threshold] = 0
print("QFT * IQFT of 3 qubit system:")
print(unitary)




