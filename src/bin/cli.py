#!/usr/bin/python

import json
import time
import click
import uuid
from refiner.embeddings import Embeddings

###
# CLI command group
###


@click.group()
def cli():
    """A CLI wrapper for the Refiner API."""


@cli.command()
@click.option('--text', required=True)
@click.option('--index-id', required=True)
@click.option('--metadata', required=False)
@click.option('--vector-id', required=False)
@click.option('--namespace', required=False)
def create(text, index_id, metadata, vector_id, namespace):
    """
    Create embeddings from text and write to Refiner.
    """

    click.echo('Creating Embeddings...')

    refiner_client = Embeddings()

    vid = vector_id or str(uuid.uuid4())

    payload = {
        "id": vid,
        "text": text
    }

    if metadata:
        payload['metadata'] = metadata

    response = refiner_client.create(
        payload, index_id, namespace=namespace)

    if response.get('error', None):
        click.echo('Error: {}'.format(response['error']))
        return

    click.echo('{} {}'.format(vid, response))


@cli.command()
@click.option('--text', required=True)
@click.option('--index-id', required=True)
@click.option('--limit', required=False, type=click.INT, default=1)
@click.option('--namespace', required=False)
def search(text, index_id, limit, namespace):
    """Search for a text embedding in Refiner"""

    click.echo('Searching Refiner...')

    refiner_client = Embeddings()
    results = refiner_client.search(
        text, index_id, limit, namespace=namespace)
    click.echo(results)


###
# Main function
###
if __name__ == '__main__':
    cli()
