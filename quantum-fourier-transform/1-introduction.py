from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
import numpy as np
np.set_printoptions(suppress=True,formatter={'all': lambda x: "{:.4g}".format(x)})
from sympy import symbols
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator, Statevector
from qiskit.visualization import plot_state_city

########################
# I dont actually know how this worked.
# I copied this example just to try it out,
# but I need to use my IBM minutes
# and I dont wanna.
########################

initial_states = ["00",'01','10','11']
U = np.zeros((len(initial_states),len(initial_states)),dtype=complex)
n = 0
m = 0

while n < len(initial_states):
    m=0
    while m < len(initial_states):
        U[n,m]= U[n,m]+np.e**(2j * np.pi *n*m/len(initial_states))
        m = m+1
    n = n+1

threshold = 1e-10
U.real[np.abs(U.real)<threshold]=0
U.imag[np.abs(U.imag)<threshold]=0

print(U)




if 1==2:
    for state in initial_states:
        sv = Statevector.from_label(state)
        arr = np.array(sv)
        col = arr.reshape(-1,1)
        print("col:")
        print(col)
        U2 = np.append(U2,col,axis=1)
    print("total U")
    U2 = U2[:,1:]
    print(U2)