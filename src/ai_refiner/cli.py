#!/usr/bin/python

import click
import uuid

from refiner import Refiner

###
## CLI command group
###
@click.group()
def cli():
    """A CLI wrapper for the Refiner API."""

# Write embeddings to Pinecone database
@cli.command()
@click.option('--text', required=True)
@click.option('--index-id', required=True)
@click.option('--vector-id', required=False)
@click.option('--namespace', required=False)
def create(text, index_id, vector_id, namespace):
    """
    Create embeddings from text and write to Refiner.
    """

    click.echo('Creating Embeddings...')
    
    refiner_client = Refiner()

    payload = {
        "id": vector_id or str(uuid.uuid4()),
        "text": text,
        "metadata": {
            "text": text
        }
    }
    
    response = refiner_client.create(payload, index_id, namespace=namespace)
    click.echo(response)


@cli.command()
@click.option('--text', required=True)
@click.option('--index-id', required=True)
@click.option('--limit', required=False)
@click.option('--namespace', required=False)
def search(text, index_id, limit, namespace):
    """Search for a text embedding in Refiner"""

    click.echo('Searching Refiner...')

    refiner_client = Refiner()
    results = refiner_client.search(text, index_id, limit=limit, namespace=namespace)
    click.echo('Results: {}'.format(results))

###
## Main function
###
if __name__ == '__main__':
    cli()
