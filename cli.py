import click
import spacy
import json
import yaml
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")
model = models.resnet18(pretrained=True)
model.eval()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--text', '-t', type=str, required=False)
@click.help_option('--help', '-h')
def text_to_embeddings(text):
    """
    text string
    """
    doc = nlp(text)
    embeddings = doc.vector
    print(embeddings)

@cli.command()
@click.argument('html_file')
def html_to_embeddings(html_file):
    with open(html_file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text()
        doc = nlp(text)
        embeddings = doc.vector
        print(embeddings)

@cli.command()
@click.argument('json_file')
def json_to_embeddings(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        text = json.dumps(data)
        doc = nlp(text)
        embeddings = doc.vector
        print(embeddings)

@cli.command()
@click.argument('yaml_file')
def yaml_to_embeddings(yaml_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
        text = yaml.dump(data)
        doc = nlp(text)
        embeddings = doc.vector
        print(embeddings)

@cli.command()
@click.argument('image_file')
def image_to_embeddings(image_file):
    """'path to image file"""
    image = Image.open(image_file)
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
    print(embeddings)

if __name__ == '__main__':
    cli()
