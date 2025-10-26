
import numpy as np
from sympy import symbols
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
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

# construct unique cV and cVdag gates
V_gate = UnitaryGate(V,label="V")
Vdag_gate = UnitaryGate(Vdag,label="V+")
cV = V_gate.control(1,label="")
cVdag = Vdag_gate.control(1,label="")

X = np.array([[0,1],[1,0]])

# Controlled V on bits [1,2]

qc.append(cV,[1,2])
qc.barrier()
# CNOT on [0,1]
qc.cx(0,1)
qc.barrier()

# Controlled Vdagger on bits [1,2] 

qc.append(cVdag,[1,2])
qc.barrier()

# CNOT on [0,1]
qc.cx(0,1)
qc.barrier()

# Controlled V on bits [0,2]
qc.append(cV,[0,2])


# Initial state and Evolution

if 1==1:
    initial_states=['000','010','100','110','111']
    
    for state in initial_states:
    
        psi_in = Statevector.from_label(state)
        psi_out = psi_in.evolve(qc.reverse_bits())
        psi_out_dict = psi_out.to_dict()
        print(" ")
        print("Evolution of |"+state+">")
        for basis, amplitude in psi_out_dict.items():
            print(f"|{basis}>: {np.round(amplitude,2)}")
    print(" ")

if 1==1:
    print("Unitary H:")
    print(H)
    print("----------")
    print(" ")
    print("Unitary V:")
    print(V)
    print("----------")
    print(" ")
    print("Unitary V+:")
    print(Vdag)
    print("----------")
    print(" ")
    print("Unitary V@V+:")
    print(np.round(V@Vdag,2))
    print("----------")
    print(" ")
    print("Unitary V@V:")
    print(np.round(V@V,2))
    print("----------")
    print(" ")
    print("Unitary V@V+@V:")
    print(np.round(V@np.round(Vdag@V,2),2))
    print("----------")
    print(" ")

print("Unitary V @ X @ V+ @ X @ V :")
print(np.round(V@X@Vdag@X@V,2))
print("----------")
print(" ")
print("Unitary H:")
print(np.round(H,2))
print("----------")
print(" ")
unitary = Operator(qc.reverse_bits()).data
print(np.round(unitary,2))

print(qc)