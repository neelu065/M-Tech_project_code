import numpy as np
import matplotlib.pyplot as plt

number_of_wings  = 1000

y = []
exceeding_wing_index = []
span_length = []
for i in range(number_of_wings):
    with open('output_files/perturbed_cp/cp_{}.csv'.format(i+1)) as f:
        f = np.loadtxt(f)
        y.append(f[-1][1])
	
    if not ( 2.4 <= f[-1][1] <= 3.6):
        exceeding_wing_index.append(i+1)
        span_length.append(f[-1][1])

print('exceeding span_length wings are = {}'.format(exceeding_wing_index))

print('corresponding span_length are = {}'.format(span_length))
print('max length of span = {}'.format( max(y)))

print('min length of span = {}'.format( min(y)))

plt.figure(1)

plt.plot(range(1,number_of_wings+1), y,'*')

plt.xlim(1,1000)
plt.ylim(0,4)

plt.xlabel('Number_of_wings')
plt.ylabel('Span_length')
plt.savefig('spanlength.png', dpi = 300)
plt.show()
