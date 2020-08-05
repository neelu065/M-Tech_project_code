import csv


def func_value(file):
    """
    Input = function value file location.
    Output = Cl and Cd of the function evalution.
    """
    
    with open( file ) as f:
        csv_reader = csv.DictReader(f)
    
        for row in csv_reader:
            Cl , Cd  = row['       "CL"       '] , row['       "CD"       ']
    
    return float(Cl) , float(Cd)
        
Cl , Cd = func_value('history.csv')