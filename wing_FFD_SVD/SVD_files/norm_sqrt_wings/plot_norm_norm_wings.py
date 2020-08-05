import matplotlib.pyplot as plt
import numpy as np
with open('sigma_energy_norm_sqrt_n.csv') as f:
    f = np.loadtxt(f).T

plt.figure(1)
plt.grid(which='both')
plt.plot(f[0], f[2],  linewidth=2 )
plt.xlabel('Number of singular values selected')
plt.ylabel('Norm values')
plt.title(r'Norm value calculated as: Norm(X - X*) / $\sqrt{totalwings}$')
plt.semilogy()
plt.savefig('norm_sqrt_wings',dpi=300)

