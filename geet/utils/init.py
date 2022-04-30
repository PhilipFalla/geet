'''
[Module] Init command utils.
'''
import os


def write_file(name: str, lines: list) -> None:

    with open(name, 'w') as writer:
        writer.write('\n'.join(lines))


def get_init_files() -> dict:

    initial_files = {
        '.geet/.geetignore': [".geet/.geetignore", ".geet/.hashdict.json", ".DS_Store\n"],
        '.geet/.hashdict.json': ["{\"README.md\": \"1ea4b01b49eae1fd044238ae5423222eac5495ce\"}\n"],
        'README.md': ["### Geet", "Fresh geet repository.\n"]
    }

    return initial_files


def file_exists(path: str, name: str) -> bool:

    return os.path.exists(path + name)
