import utils.status as status_utils
import utils.init as init_utils
from pyfiglet import Figlet
import click
import time
import sys
import os


@click.group()
def cli():
    pass


@cli.command()
def banner():

    figlet = Figlet(font='slant')
    print(figlet.renderText('geet'))


@cli.command()
def status():

    path = status_utils.get_current_path()
    new_files = status_utils.scan_for_new_files(path)
    deleted_files = status_utils.scan_for_deleted_files(path)
    modified_files = status_utils.scan_for_modified_files(path)

    status_message = '''
    On branch 'master'
    Your branch is up to date with 'origin/master'.

    Uncommited changes:
        (use "geet commit <comment>..." to commit these changes)
        (use "geet restore <commit>..." to discard changes in working directory)
    ''' 
    print(status_message)

    files_changed = False

    for file in deleted_files:
        files_changed = True
        print('             deleted:', file, end='\n')
    
    for file in modified_files:
        files_changed = True
        print('             modified:', file, end='\n')

    for file in new_files:
        files_changed = True
        print('             added:', file, end='\n')

    if not files_changed:
        print('        < There are no changes in the repository... >')


@cli.command()
def init():

    path = status_utils.get_current_path()
    initial_files = init_utils.get_init_files()
    config_files = list(initial_files)[:2]
    first_validation = init_utils.file_exists(path, config_files[0])
    second_validation = init_utils.file_exists(path, config_files[1])

    if first_validation and second_validation:
        print('Invalid operation: a geet repository already exists in this directory.')
        return None

    user_input = input('Creating geet repository in {} [press enter to continue]: '.format(path))
    
    if user_input != "":
        print('Canceling...')
        sys.exit(0)
 
    print('Initializing...')
    time.sleep(1)
    os.mkdir('.geet')
    os.mkdir('.geet/objects')

    for file in initial_files:
        init_utils.write_file(file, initial_files[file])

    print('Geet repository successfully created.')


@cli.command()
@click.option('-m', help='Commit message')
def commit(m):
    click.echo('Geet commit...')
    click.echo(m)


@cli.command()
def push():
    click.echo('Geet push...')


if __name__ == '__main__':
    cli()
