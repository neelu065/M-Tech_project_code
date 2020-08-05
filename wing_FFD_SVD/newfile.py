import numpy as np


def standard_wing ():

    """
    This module will reformat the wing data points into 3 columns
    consisting of x, y, z coordinates of wing
    and write it to file.
    input: raw wing data.
    output: standard file containing 3 columns.
    """

    with open('input_files/wing.txt', 'r') as f:
        with open('output_files/initial_wing.csv','w') as g:
            wing = np.loadtxt(f)

            file = len( wing ) * 4          #This value 4 may vary, keep an eye on this.
            frac = int( file / 3 )

            ad = np.reshape( wing, file)

            x = ad[ 0 : frac ]
            y = ad[ frac : 2 * frac ]
            z = ad[ 2 * frac : 3 * frac ]

            for i in range(len(x)):
                g.write('{0} \t \t {1} \t \t {2}\n'.format( x[i] , y[i] , z[i] ) )
