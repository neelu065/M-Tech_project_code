import csv


def read_cl_cd(population_size, j=0, restart = 'No'):
    """
    This module will read the history
    file and write it to other file for
    further comparision.

    """
    
    CD = []
    Cmx = []
    aoa = []
    count = 0

    if restart == 'No':
        path_folder = 'optimizer_output/su2_solution_files'
    else:
        path_folder = 'optimizer_output/solution_final'

    for i in range(population_size):
        
        print('Reading history_file_{} ... '.format(i + 1))

        with open('{}/history_files/history_{}.csv'.format(path_folder,i + 1)) as f:
            csv_reader = csv.DictReader(f)

            for row in reversed(list(csv_reader)):

                Cl, Cd, CMx, AoA = row['       "CL"       '], row['       "CD"       '], row['       "CMx"      '], row['       "AoA"      ']
                CD.append(float(Cd))
                Cmx.append(float(CMx))
                aoa.append(float(AoA))

                break

        if restart == 'No':
            with open('optimizer_output/fobj_{}.csv'.format(j), 'a') as f:  # File which store the obj func values.

                if count < 1:
                    f.write('\t CL \t \t \t \t  CD \t \t \t \t CMx \t \t \t \t AoA \n ')
                    count += 1

                f.write('{0} \t \t {1} \t \t {2} \t \t {3}\n'.format(Cl, Cd, CMx, AoA))
        
    return CD, Cmx

