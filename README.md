## Important steps to execute the code.

Please **do not** rename the respective folder names as they are all interconnected to each other.
 
Instead copy both the folders and place inside new directory and execute the files as follows.

> - **sbatch Project_code_fNRAND1/compute_wait.sh**
>
>> This is hold the entire node(28 CPU) in compute nodes exclusive for USER.

> - **sbatch wing_FFD_SVD/wing(1000)_generator.sh**
>
>> This will create the 1000 random wings within given constraints.


> - **sbatch wing_FFD_SVD/SVD_files/principal_wings_20/svd_wings_principal.sh**
>
>> This will calculate the SVD for those 1000 randomly created wings and place the output inside the Project_code_fNRAND1/optimizer_input folder.


> - **python Project_code_fNRAND1/run_optimizer.py**
>
>> This will fire 20 jobs into cluster(compute node) and DE generation are involved in this.  
>> Since there is communication error with license file(-17), above command cannot be submitted.  
>> However, except meshing, all work is carried out in compute node.


> - **python Project_code_fNRAND1/paraview_gen.py**
>
>> This will generate the solution (*.vtk) files in the optimizer_output/solution_final/ (volume_flow and surface_flow)/ *.     
>> Above command should be executed only after all generation are completed.

**Note: All the above commands has to be executed by directing the terminal to *README.md* location**.

___Any queries please follow @ neelu065@gmail.com___

