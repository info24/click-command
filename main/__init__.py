import click
from click_flask_command.cli import testcli

@click.group()
def click_command():
	''' main
	'''
	pass

@click_command.command()
def init():
	'''click init function'''
	color = 'red'
	click.echo(click.style('我被主人初始化啦，嘻嘻！！ %s' % color, fg=color))


click_command.add_command(testcli, 'testcli')

