import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Arc

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
qc.barrier()

qc.swap(0,2)

qc.h(2)

qc.append(cR2dag,[2,1])
qc.h(1)

qc.append(cR3dag,[2,0])
qc.append(cR2dag,[1,0])
qc.h(0)

fig = qc.draw(output='mpl', fold=-1)
ax = fig.axes[0]

fig.set_size_inches(10, 5)

def draw_curly_brace(ax, x_start, x_end, y, text, color='black'):
    mid = (x_start + x_end) / 2
    dx = (x_end - x_start) / 4
    arc1 = Arc((x_start+dx/2, y), width=dx*2, height=0.3, theta1=180, theta2=360, color=color, linewidth=2)
    arc2 = Arc((mid, y), width=dx, height=0.3, theta1=180, theta2=360, color=color, linewidth=2)
    arc3 = Arc((x_end-dx/2, y), width=dx*2, height=0.3, theta1=180, theta2=360, color=color, linewidth=2)
    for arc in [arc1, arc2, arc3]:
        ax.add_patch(arc)
    ax.text(mid, y-0.50, text, ha='center', va='top', fontsize=20, color=color)

draw_curly_brace(ax, x_start=0, x_end=5.5, y=-2.4, text='U', color='blue')
draw_curly_brace(ax, x_start=8, x_end=13.5, y=-2.4, text='U†', color='red')

plt.show()
