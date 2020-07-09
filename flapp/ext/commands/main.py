import click


@click.command()
@click.option(
    "-c", "--check", default=False, is_flag=True, help="Setup Application",
)
def init(check=False):
    """Setup application"""
    click.echo("init")
