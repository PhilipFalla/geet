from pyfiglet import Figlet
import argparse
import sys
import os
import time
import utils.status as status_utils
import utils.init as init_utils


def print_name():

    figlet = Figlet(font='slant')
    print(figlet.renderText('geet'))


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

    for file in deleted_files:
        print('             deleted:', file, end='\n')
    
    for file in modified_files:
        print('             modified:', file, end='\n')

    for file in new_files:
        print('             added:', file, end='\n')


def init():

    path = status_utils.get_current_path()
    user_input = input('Creating geet repository in {} [press enter to continue]: '.format(path))
    
    if user_input != "":
        print("Canceling...")
        sys.exit(0)
 
    print('Initializing...')
    time.sleep(1)
    os.mkdir('.geet')

    initial_files = init_utils.get_init_files()

    for file in initial_files:
        init_utils.write_file(file, initial_files[file])

    print('Geet repository successfully created.')

# status()
# init()



