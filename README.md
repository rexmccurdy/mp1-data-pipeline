# MP1 Data Processing Pipeline

This pipeline will load, validate, and process a data file. The configuration file determines how data is processed.

## Description

This pipeline will take a data file (.csv of .json), loading it as a pandas DataFrame object if the filepath is valid. 

Along with the data file, a .yaml file is taken to configure which processing steps are used. The configuration file is used to validate the columns of the data through required columns and numeric columns.

Next, the data is processed according to the configurations set in the config file. This includes dropping duplicate rows, dropping rows/columns with missing values, and removing rows with numerical outliers.

Finally, cleaned data is saved to the output file path which is given. Logger messages and cleaning report are printed.

Functions for each step (loading, validating, processing, saving) are found in the src/ directory. The config/ directory contains the .yaml configuration file and the fixtures/ directory contains the data file. .gitignore, requirements.txt, and README.md are saved in the repository root along with pipeline.py which runs the pipeline.

## Use

pipeline.py is the main function file and takes the following:

- "--input", "-i: input filepath
- "--output", "-o": output filepath
- "--config", "-c": configuration filepath
- "--verbose", "-v": sets logger level to DEBUG instead of INFO

Example input:

python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose

Logger output:

>20:30:12 INFO     src.utils - Input file validated: config/config.yaml\
20:30:12 INFO     src.utils - Input file validated: fixtures/sample_data.csv\
20:30:12 INFO     src.data_loaders - Loaded CSV file: fixtures/sample_data.csv (100 rows)\
20:30:12 INFO     src.data_loaders - Loaded YAML file: config/config.yaml\
20:30:12 DEBUG    __main\__ - Input files loaded: fixtures/sample_data.csv, config/config.yaml\
20:30:12 DEBUG    src.data_validator - Invalid value found in column 'rating' at row 95: not_available\
20:30:12 DEBUG    src.data_validator - Invalid value found in column 'rating' at row 96: error\
20:30:12 DEBUG    src.data_validator - Valid rows remaining: 98. Removed 2 rows with invalid numeric values\
20:30:12 INFO     __main\__ - Rows before validation: 100. Rows after validation: 98\
20:30:12 DEBUG    src.data_processor - Removed 2 duplicate rows\
20:30:12 DEBUG    src.data_processor - Dropped 2 rows with missing values\
20:30:12 DEBUG    src.data_processor - 2 rows removed using iqr method with a threshold of 1.5\
20:30:12 INFO     __main\__ - Processing complete: 98 -> 92 rows\
20:30:12 INFO     src.data_output - 92 rows saved to output/clean.csv\
20:30:12 INFO     __main\__ - Saved cleaned data to output/clean.csv\

Example for output file is in output/clean.csv

