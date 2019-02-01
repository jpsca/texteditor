#!/usr/bin/env python
"""
"""
import io
import os
import re
import sys
import subprocess
import tempfile

from distutils.spawn import find_executable


__version__ = '1.0.0'

EDITOR = 'EDITOR'

COMMON_EDITORS = [
    'subl',
    'vscode',
    'atom',
]

THE_GREY_ONES = [
    'vim',
    'emacs',
]

MACOS_EDITORS = [
    # Only in MacOS, the "shell commands" are not installed by default
    '/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl',
    '/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code',
    '/Applications/Atom.app/Contents/Resources/app/atom.sh',
    '/Applications/TextMate.app/Contents/Resources/mate',
    '/Applications/Brackets.app/Contents/Resources/brackets.sh',
] + COMMON_EDITORS + THE_GREY_ONES + [
    '/Applications/TextEdit.app/Contents/MacOS/TextEdit',
]

# In some linuxes `vim` and/or `emacs` come preinstalled, but we don't want
# to throw you to their unfamiliar UI unless there are other options.
# If you are using them you probably have set your $EDITOR variable anyway.
LINUX_EDITORS = COMMON_EDITORS + [
    'kate',
    'geany',
    'gedit',
    'nano',
] + THE_GREY_ONES

WINDOWS_EDITORS = COMMON_EDITORS + THE_GREY_ONES + [
    r'C:\Program Files (x86)\Notepad++\notepad++.exe',
    'notepad.exe',
]

EDITORS = {
    'darwin': MACOS_EDITORS,
    'linux': LINUX_EDITORS,
    'win': WINDOWS_EDITORS,
}


def get_possible_editors():
    sys_platform = sys.platform

    for platform in EDITORS:
        if sys_platform.startswith(platform):
            return EDITORS[platform]

    return COMMON_EDITORS + THE_GREY_ONES


def split_editor_cmd(cmd):
    """Split by spaces unless escaped.

    >>> split_editor_cmd('my\\ editor --wait')
    ['my\\ editor', '--wait']
    """
    return re.split(r'(?<!\\)\s+', cmd)


def get_editor():
    cmd = os.getenv(EDITOR)
    if cmd:
        return split_editor_cmd(cmd)

    editors = get_possible_editors()
    for cmd in editors:
        binpath = find_executable(cmd)
        if binpath:
            return [binpath]

    # You might only see this error on Linux
    raise RuntimeError(
        'Unable to find a text editor. '
        'Please set your $EDITOR environment variable.'
    )


def run(cmd):
    """A separated function for easy testing."""
    proc = subprocess.Popen(cmd, close_fds=True)
    proc.communicate()


def open(text=None, filename=None, extension='txt', encoding=None):
    cmd = get_editor()

    if filename is None:
        suffix = '.' + extension.strip('.')
        tmp = tempfile.NamedTemporaryFile(suffix=suffix)
        filename = tmp.name

    if text is not None:
        with io.open(filename, mode='wt', encoding=encoding) as file:
            file.write(text)

    cmd += [filename]
    run(cmd)

    with io.open(filename, mode='rt', encoding=encoding) as file:
        return file.read()


def cli():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    open_parser = subparsers.add_parser('open', help='Open a file to edit')
    open_parser.set_defaults(cmd=open)
    open_parser.add_argument(
        '--text', type=str, nargs='?', required=False,
        help='The starting content for the edited file.'
    )
    open_parser.add_argument(
        '--filename', type=str, nargs='?', required=False,
        help='Edit this file instead of creating a temporary one'
    )
    open_parser.add_argument(
        '--extension', type=str, nargs='?', required=False,
        help='Use this extension for the temporary file'
    )
    open_parser.add_argument(
        '--encoding', type=str, nargs='?', required=False,
        help='Use this encoding instead of the platform default'
    )

    kwargs = vars(parser.parse_args())
    if 'cmd' in kwargs:
        cmd = kwargs.pop('cmd')
        print(cmd(**kwargs))


if __name__ == '__main__':
    cli()
