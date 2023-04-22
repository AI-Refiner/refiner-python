# AI-Refiner

## Using the Embeddings CLI
The Embeddings CLI is a command-line interface that allows you to convert text, images, audio, HTML, JSON, and YAML data to embeddings. Embeddings can be used to create visualization tools, model training and tuning tools and benchmarking and evaluation tools.

## Installation
To use the Embeddings CLI, you'll need to install the necessary dependencies. You can do this by running the following command:

`pip install -r requirements.txt`

This will install the required libraries, including spacy, torch, torchvision, beautifulsoup4, json, and yaml.

## Help
To  see the available sub-commands run the help option.
` python cli.py  --help`

## Usage
Once you have installed the dependencies, you can use the Embeddings CLI to convert your data to embeddings. Here are the available sub-commands:


## string_to_embeddings
This sub-command takes a string as input and writes the corresponding embeddings. To use this sub-command, run the following command:

`python cli.py string_to_embeddings --string "example string" --output-file /path/to/output.txt`


## text_to_embeddings
This sub-command takes a text file as input and writes the corresponding embeddings. To use this sub-command, run the following command:

`python cli.py text_to_embeddings --input-file /path/to/input.txt --output-file /path/to/output.txt`

## csv_to_embeddings
This sub-command takes a CSV file as input and writes the corresponding embeddings. To use this sub-command, run the following command:

`python cli.py csv_to_embeddings --input-file /path/to/input.csv --output-file /path/to/output.txt`

## html_to_embeddings
This sub-command takes an HTML file as input and writes the corresponding embeddings. To use this sub-command, run the following command:

`python cli.py html_to_embeddings --input-file /path/to/input.html --output-file /path/to/output.txt`

## json_to_embeddings
This sub-command takes a JSON file as input and writes the corresponding embeddings. To use this sub-command, run the following command:

`python cli.py json_to_embeddings --input-file /path/to/input.json --output-file /path/to/output.txt`


## yaml_to_embeddings
This sub-command takes a YAML file as input and writes the corresponding embeddings. To use this sub-command, run the following command:

`python cli.py yaml_to_embeddings --input-file /path/to/input.yaml --output-file /path/to/output.txt`


## image_to_embeddings
This sub-command takes an image file as input and writes the corresponding embeddings. To use this sub-command, run the following command:

`python cli.py image_to_embeddings --input-file /path/to/input.jpg --output-file /path/to/output.txt`


## json_to_csv
This sub-command takes a json file as input and converts it to csv. To use this sub-command, run the following command:

`python cli.py json_to_csv --input-file /path/to/input.json --output-file /path/to/output.csv`


## Conclusion
The Embeddings CLI is a useful tool for converting text, HTML, JSON, and YAML data to embeddings, as well as converting images to embeddings. With this guide, you should now be able to use the CLI to perform these tasks on your own data.
