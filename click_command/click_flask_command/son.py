import click

@click.group()
def son():
	'''我是son模块
	'''
	pass

@son.command()
def run():
	'''son模块run
	'''
	print("run... son")