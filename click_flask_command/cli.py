import click

from utils.function import foo

@click.group()
def testcli():
    """testcli."""
    pass


@testcli.command()
def init():
	"""inits"""
	value = foo()
	print("inits...", value)

if __name__ == "__main__":
	testcli()