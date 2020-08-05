import numpy as np
import matplotlib.pyplot as plt

number_of_wings  = 30

y = []
exceeding_wing_index = []

for i in range(number_of_wings):
    with open('principal_wings/principal_wing_{}.x'.format(i+1)) as f:
    #with open('random_wings/wing_perturbed_{}.x'.format(i+1)) as f:
		f = np.loadtxt(f, skiprows=1)
        y.append(f[1][-1])
        if not ( 2.46 <= f[1][-1] <= 3.54):
            exceeding_wing_index.append(i+1)

print('exceeding span_length wings are = {}'.format(exceeding_wing_index))

print('max length of span = {}'.format( max(y)))

print('min length of span = {}'.format( min(y)))

plt.figure(1)

plt.plot(range(1,number_of_wings+1), y,'*')

plt.xlim(0,number_of_wings+1)
plt.ylim(0,4)

plt.xlabel('Number_of_wings')
plt.ylabel('Span_length')
plt.savefig('spanlength.png', dpi = 300)
plt.show()
