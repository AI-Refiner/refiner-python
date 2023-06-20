#!/usr/bin/python
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
@click.option('--config-file', required=False)
@click.option('--batch-size', required=False, type=click.INT)
@click.option('--pool-threads', required=False, type=click.INT)
@click.option('--openai-api-key', required=False)
@click.option('--pinecone-api-key', required=False)
@click.option('--pinecone-environment-name', required=False)
def create(text, index_id, metadata, vector_id, namespace, config_file, batch_size, pool_threads, openai_api_key, pinecone_api_key, pinecone_environment_name):
    """
    Create embeddings from text and write to Refiner.
    """

    click.echo('Creating Embeddings...')

    refiner_client = Embeddings(
        config_file, openai_api_key, pinecone_api_key, pinecone_environment_name)

    vid = vector_id or str(uuid.uuid4())

    payload = {
        "id": vid,
        "text": text
    }

    if metadata:
        payload['metadata'] = metadata

    response = refiner_client.create(
        payload, index_id, namespace=namespace, batch_size=batch_size, pool_threads=pool_threads)

    if response.get('error', None):
        click.echo('Error: {}'.format(response['error']))
        return

    click.echo('{} {}'.format(vid, response))


@cli.command()
@click.option('--text', required=True)
@click.option('--index-id', required=True)
@click.option('--limit', required=False, type=click.INT, default=1)
@click.option('--namespace', required=False)
@click.option('--config-file', required=False)
@click.option('--openai-api-key', required=False)
@click.option('--pinecone-api-key', required=False)
@click.option('--pinecone-environment-name', required=False)
def search(text, index_id, limit, namespace, config_file, openai_api_key, pinecone_api_key, pinecone_environment_name):
    """Search for a text embedding in Refiner"""

    click.echo('Searching Refiner...')

    refiner_client = Embeddings(
        config_file, openai_api_key, pinecone_api_key, pinecone_environment_name)
    results = refiner_client.search(
        text, index_id, limit, namespace=namespace)
    if results.get('error', None):
        click.echo('Error: {}'.format(results['error']))
        return
    click.echo(results)


###
# Main function
###
if __name__ == '__main__':
    cli()
