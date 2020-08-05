import matplotlib.pyplot as plt
import numpy as np
with open('sigma_energy_norm_norm_X.csv') as f:
    f = np.loadtxt(f)
    f = np.transpose(f)

plt.figure(1)
plt.grid(which='both')
plt.plot(f[0], f[2],  linewidth=2 )
plt.xlabel('Number of singular values selected')
plt.ylabel('Norm values')
plt.title('Norm value calculated as:\nNorm(X - X*) / Norm(X)')
plt.semilogy()
plt.savefig('norm_norm_X',dpi=300)

plt.figure(2)
plt.grid(which='both')
plt.plot(f[0], f[1],  linewidth=2 )
plt.xlabel('Number of singular values selected')
plt.ylabel('Energy ($\lambda^2$)')
plt.title(' Energy Plot: \n Norm(X - X*) / Norm(X) ')
plt.savefig('Energy_norm_norm_X',dpi=300)