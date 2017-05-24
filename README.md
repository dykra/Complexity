# ComplexityEstimator
Measure of presumable complexity using execution time.


       --file file name with function to test
       --fun function to test
       --complexity argument to this option is function which creates the structure
       --clean function to clean after execution (optional)    
       --deadline time limit in seconds
       --estimate option to estimate time or size
              f.ex.: --estimate create_array time 4
                     --estimate create_array size 6
                     
                     
For install use:

pip3 install git+https://github.com/dykra/ComplexityEstimator.git --user

Execution example:

Complexity --file Complexity.functions_and_structures  --fun sort --estimate create_list size 1000 --deadline 10

Files to test have to be included in Complexity package (like functions_and_stryctures.py).
