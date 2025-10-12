from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit.quantum_info import Statevector
import numpy as np

UH = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
# UAC = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])

zero= Statevector.from_label('0')
one = Statevector.from_label('1')

psi_1 = zero^one

psi_1.draw("latex")
