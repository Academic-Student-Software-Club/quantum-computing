import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city


qc = QuantumCircuit(2)
H=(1/np.sqrt(2))*np.array([[1,1],[1,-1]])
qc.unitary(Operator(H),[0],label="H")
unitary = Operator(qc).data
print(np.round(unitary,3))

print("---------------")
qc2 = QuantumCircuit(2)

qc2.unitary(Operator(H),[1],label="H")
unitary2 = Operator(qc2).data
print(np.round(unitary2,3))
