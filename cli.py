import click
import spacy
import json
import yaml
import torch
import pandas as pd
import torchvision.transforms as transforms
from torchvision import models
from PIL import Image
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")
model = models.resnet50(weights='ResNet50_Weights.DEFAULT')
model.eval()

@click.group()
def cli():
    pass


@cli.command()
@click.option('--input-file', '-i', required=True)
@click.option('--output-file', '-o', required=True)
def json_to_csv(input_file, output_file):
    """Converts a JSON file to CSV"""
    print("Converting JSON to CSV...")
    with open(input_file, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame.from_dict(data, orient='index')
        df.to_csv(output_file, index_label='Id')
        click.echo('CSV file saved at {}'.format(output_file))

    
@cli.command()
@click.option('--string', required=True)
@click.option('--output-file', required=False)
def string_to_embeddings(string, output_file=None):
    """
    text string
    """
    print("Converting string to embeddings...")
    doc = nlp(string)
    embeddings = doc.vector

    if output_file:
        with open(output_file, 'w') as f:
            f.write(str(embeddings))
    else:
        print(embeddings)

# create a command to parse a text file
# and return the embeddings
@cli.command()
@click.option('--input-file', required=True)
@click.option('--output-file', required=False)
def text_to_embeddings(input_file, output_file=None):
    """
    path to text file
    """
    print("Converting text file to embeddings...")
    print("Creating embeddings...""")
    if output_file:
        print("Saving embeddings to {}".format(output_file))    
    with open(input_file, 'r') as i:
        text = i.read()
        doc = nlp(text)
        embeddings = doc.vector

    if output_file:
        with open(output_file, 'w') as o:
            o.write(str(embeddings))
    else:
        print(embeddings)

# create a command to convert csv file to embeddings
@cli.command()
@click.option('--input-file', required=True)
@click.option('--output-file', required=False)
@click.option('--rows', required=False)
def csv_to_embeddings(input_file, output_file=None, rows=None):
    """
    path to csv file
    """
    print("Converting csv file to embeddings...")
    print("Creatings embeddings for the first {} rows".format(rows or '10'))
    if output_file:
        print("Saving embeddings to {}".format(output_file))

    # read first 10 rows of csv file in chunks and convert to embeddings
    # code: 
    with open(input_file, 'r') as i:
        for _ in range(int(rows) or 10):
            chunk = i.readline()
            doc = nlp(chunk)
            embeddings = doc.vector

            if output_file:
                with open(output_file, 'w') as o:
                    o.writelines(str(embeddings))
            else:
                print(embeddings)



@cli.command()
@click.option('--input-file', required=True)
@click.option('--output-file', required=False)
def html_to_embeddings(input_file, output_file=None):
    """
    path to html file
    """    
    print("Converting html file to embeddings...")
    print("Creating embeddings...""")
    if output_file:
        print("Saving embeddings to {}".format(output_file))    
    with open(input_file, 'r') as i:
        soup = BeautifulSoup(i, 'html.parser')
        text = soup.get_text()
        doc = nlp(text)
        embeddings = doc.vector

    if output_file:
        with open(output_file, 'w') as o:
            o.write(str(embeddings))
    else:
        print(embeddings)

@cli.command()
@click.option('--input-file', required=True)
@click.option('--output-file', required=False)
def json_to_embeddings(input_file, output_file=None):
    """
    path to json file
    """    
    print("Converting json file to embeddings...")
    print("Creating embeddings...""")
    if output_file:
        print("Saving embeddings to {}".format(output_file))    
    with open(input_file, 'r') as i:
        data = json.load(i)
        text = json.dumps(data)
        doc = nlp(text)
        embeddings = doc.vector

    if output_file:
        with open(output_file, 'w') as o:
            o.write(str(embeddings))
    else:
        print(embeddings)

@cli.command()
@click.option('--input-file', required=True)
@click.option('--output-file', required=False)
def yaml_to_embeddings(input_file, output_file=None):
    """
    path to yaml file
    """
    print("Converting yaml file to embeddings...")
    print("Creating embeddings...""")
    if output_file:
        print("Saving embeddings to {}".format(output_file))        
    with open(input_file, 'r') as i:
        data = yaml.safe_load(i)
        text = yaml.dump(data)
        doc = nlp(text)
        embeddings = doc.vector

    if output_file:
        with open(output_file, 'w') as o:
            o.write(str(embeddings))
    else:
        print(embeddings)

@cli.command()
@click.option('--input-file', required=True)
@click.option('--output-file', required=False)
def image_to_embeddings(input_file, output_file=None):
    """path to image file"""
    print("Converting image file to embeddings...")
    print("Creating embeddings...""")
    if output_file:
        print("Saving embeddings to {}".format(output_file))      
    image = Image.open(input_file)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

    embeddings = output[0].numpy()

    if output_file:
        with open(output_file, 'w') as o:
            o.write(str(embeddings))
    else:
        print(embeddings)

if __name__ == '__main__':
    cli()
