"""Console script for hexplorer."""

import click


@click.version_option(package_name="hexplorer")
@click.command()
def cli(args=None):
    """Console script for hexplorer."""
    click.echo("Replace this message by putting your code into hexplorer.cli.cli")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
