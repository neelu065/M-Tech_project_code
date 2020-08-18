import numpy as np
import csv
# main function
# which call all the functions present in this script

def airfoil(m,p,t,angle,point):
    m = m/100
    p = p/10
    t = t/100
    c = 1
    x = np.linspace(0, c, point)
    data     = foil(m, p, t, x, c)                                              # function call (1)
    aoa_foil = foil_aoa(data,angle)                                             # function call (2)
    fprint   = fileprint(data,aoa_foil,point)                                   # function call (3)
    return()



# function call (1)
#def foil(m, p, t, x, c):
def foil(m, p, t, x, c):
    yc = np.where((x >= 0) & (x <= (c * p)),                                     # camber line
    m * (x / np.power(p, 2)) * (2.0 * p - (x / c)),
    m * ((c - x) / np.power(1 - p, 2)) * (1.0 + (x / c) - 2.0 * p))

    yt = 5 * t * (0.2969 * np.sqrt(x)                                           # thickness distance
        - 0.1260 * x
        - 0.3516 * np.power(x, 2)
        + 0.2843 * np.power(x, 3)
        - 0.1015 * np.power(x, 4))
    if (m == 0 or p == 0):                                                      # slope line
        slope = 0
    else:
        slope = np.where((x >= 0) & (x <= (c * p)),
        ((2.0 * m) / np.power(p, 2)) * (p - x / c),
        ((2.0 * m) / np.power(1 - p, 2)) * (p - x / c))
    th = np.arctan(slope)
    return  (x - yt*np.sin(th), yc + yt*np.cos(th),
            x + yt*np.sin(th), yc - yt*np.cos(th))


# function call (2)                                                             # function to rotate the airfoil by defined value
def foil_aoa(data,angle):
    if angle == 0:
        return(data)
    else:
        angle = -( angle * (np.pi/180) )
        xu = np.cos(angle) * data[0] - np.sin(angle) * data[1]
        yu = np.sin(angle) * data[0] + np.cos(angle) * data[1]
        xl = np.cos(angle) * data[2] - np.sin(angle) * data[3]
        yl = np.sin(angle) * data[2] + np.cos(angle) * data[3]
    return(xu,yu,xl,yl)


#function call (3)                                                              # To print values into the file
def fileprint(data,aoa_foil,point):
    NDIM = 2                                                                    # Dimension value(in this case it 2D)
    with open('airfoil_aoa.x','w') as f:
        f.write(' {} \n {} \t 1 \n {} \t 1 \n '.format(NDIM,point,point))
        writer = csv.writer(f, delimiter='\t')
        for iter in range(4):
            writer.writerow(aoa_foil[iter])
    return ()
