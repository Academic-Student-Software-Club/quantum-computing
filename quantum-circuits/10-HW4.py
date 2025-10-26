
import numpy as np
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city

from qiskit.circuit.library import HGate
import cmath

H = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])

# Gets eigenvalues/vectors of H.
e_val,e_vec = np.linalg.eig(H)

# Constructs D and D^{1.2}
D = np.array([[e_val[0],0],[0,e_val[1]]])
Dhalf = np.array([[cmath.sqrt(e_val[0]),0],[0,cmath.sqrt(e_val[1])]])

# Construct K and K^-1
K = e_vec
Kinv = np.linalg.inv(K)

# Now we make V and Vdag, using K * Dhalf * Kinv.

V = K@Dhalf@Kinv
Vdag = V.T.conj()

# And now we construct the circuit.

qc = QuantumCircuit(3)

# Controlled V on bits [1,2]
qc.unitary(Operator(V),[2],label="V")
qc.barrier()
# CNOT on [0,1]
qc.cx(0,1)
qc.barrier()

# Controlled Vdagger on bits [1,2] 

print(qc)

