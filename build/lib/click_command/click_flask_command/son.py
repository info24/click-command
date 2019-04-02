import click

@click.group()
def son():
	pass

@son.command()
def run():
	print("run...")