import click

from ..utils.function import foo
from .son import son

@click.group()
def testcli():
    """testcli."""
    pass


@testcli.command()
def init():
	"""inits"""
	value = foo()
	print("inits...", value)

testcli.add_command(son, 'son')

if __name__ == "__main__":
	testcli()