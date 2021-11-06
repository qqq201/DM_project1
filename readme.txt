1. List missing-value attributes
>   py main.py <input file> list-missing

Example:
    py main.py input.csv list-missing


2. Count number of missing-value rows
>   py main.py <input file> count-missing

Example:
    py main.py input.csv count-missing


3. Impute missing value with method: mean, median (for numeric), mode (for categorical)
>   py main.py <input file> impute --method=<method> --attributes <attribute 1> <attribute 2> ... --output=<output file>

Example:
    py main.py input.csv impute --method=mean --attributes weight --output=output.csv
    py main.py input.csv impute --method=median --attributes weight height --output=output.csv
    py main.py input.csv impute --method=mode --attributes gender --output=output.csv


4. Remove missing-value rows or columns with threshold (0 - 100)
>   py main.py <input file> remove-missing --type=<type> --threshold=<threshold> --output=<output file>

Example:
    py main.py input.csv remove-missing --type=row --threshold=50 --output=output.csv
    py main.py input.csv remove-missing --type=column --threshold=10 --output=output.csv


5. Remove duplicate rows
>   py main.py <input file> remove-duplicate --output=<output file>

Example:
    py main.py input.csv remove-duplicate --output=output.csv

6. Normalize with min_max or z_score
>   py main.py <input file> normalize --method=<method> --attrbute= --output=<output file>

Example:
    py main.py input.csv normalize --method=min_max --attrbute=height --output=output.csv
    py main.py input.csv normalize --method=z_score --attrbute=weight --output=output.csv


7. Calculate expression
>   py main.py <input file> mutate --new-attr=<name> --expression <expression> --output=output.csv

Example:
    py main.py input.csv mutate --new-attr=bmi --expression weight / (height * height) --output=output.csv
