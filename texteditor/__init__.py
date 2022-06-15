import os
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path
from shutil import which
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional, Union


EDITOR = "EDITOR"

# I'm NOT including vim or emacs in this list because:
#
# 1. If you are using it, you know what the EDITOR variable is, and you
# probably has set it already.
#
# 2. If you aren't using it, finding yourself in their UI for the first time
# is going to be super confusing, in fact "How to exit vim" is a common
# Stack Overflow question. Having to google how to set an EDITOR variable is a
# less scary alternative.
COMMON_EDITORS = [
    "code --new-window --wait",
    "subl --new-window --wait"
    "atom --new-window --wait",
]

MACOS_EDITORS = COMMON_EDITORS + [
    # The -t flag make MacOS open the default *editor* for the file
    "open -t --new --wait-apps",
]

LINUX_EDITORS = COMMON_EDITORS + [
    "geany -imnst",
    "gedit -s",
    "nano",
]

WINDOWS_EDITORS = COMMON_EDITORS + [
    '"C:/Program Files (x86)/sublime text 3/subl.exe" --new-window --wait',
    "notepad++.exe -multiInst -notabbar -nosession -noPlugin",
    (
        '"C:/Program Files (x86)/Notepad++/notepad++.exe"'
        " -multiInst -notabbar -nosession -noPlugin"
    ),
]

EDITORS = {"darwin": MACOS_EDITORS, "linux": LINUX_EDITORS, "win": WINDOWS_EDITORS}


def get_possible_editors() -> "List[str]":
    sys_platform = sys.platform

    for platform in EDITORS:
        if sys_platform.startswith(platform):
            return EDITORS[platform]

    return COMMON_EDITORS


def get_editor() -> "List[str]":
    cmd = os.getenv(EDITOR)
    if cmd:
        return shlex.split(cmd)

    editors = get_possible_editors()
    for cmd in editors:
        splitcmd = shlex.split(cmd)
        binpath = which(splitcmd[0])
        if binpath:
            return splitcmd

    # You might only see this error on Linux
    raise RuntimeError(
        "Unable to find a text editor. Please set your $EDITOR environment variable."
    )


def run(cmd: "List[str]") -> None:
    """A separated function for easy testing."""
    proc = subprocess.Popen(cmd, close_fds=True)
    proc.communicate()


def open(
    text: "Optional[str]" = None,
    filename: "Union[str, Path, None]" = None,
    extension: str = "txt",
    encoding: "Optional[str]" = None
) -> str:
    cmd = get_editor()

    if filename is None:
        suffix = "." + extension.strip(".")
    else:
        filename = Path(filename)
        suffix = "-" + filename.name
        if text is None:
            text = filename.read_text(encoding=encoding)

    temp = get_temp(suffix)
    if text is not None:
        temp.write_text(text, encoding=encoding)

    cmd += [str(temp)]
    run(cmd)

    result = temp.read_text(encoding=encoding)
    if filename:
        filename.write_text(result, encoding=encoding)
    try:
        temp.unlink()
    except FileNotFoundError:
        pass
    return result


def get_temp(suffix: str = "") -> Path:
    path = Path(tempfile.gettempdir())
    path.mkdir(exist_ok=True, parents=True)
    temp = path / (os.urandom(16).hex() + suffix)
    temp.touch()
    return temp


def cli() -> None:  # pragma: no cover
    import argparse

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    open_parser = subparsers.add_parser("open", help="Open a file to edit")
    open_parser.set_defaults(cmd=open)
    open_parser.add_argument(
        "--text",
        type=str,
        nargs="?",
        required=False,
        help="The starting content for the edited file.",
    )
    open_parser.add_argument(
        "--filename",
        type=str,
        nargs="?",
        required=False,
        help="Edit this file instead of creating a temporary one",
    )
    open_parser.add_argument(
        "--extension",
        type=str,
        nargs="?",
        required=False,
        help="Use this extension for the temporary file",
    )
    open_parser.add_argument(
        "--encoding",
        type=str,
        nargs="?",
        required=False,
        help="Use this encoding instead of the platform default",
    )

    kwargs = vars(parser.parse_args())
    if "cmd" in kwargs:
        cmd = kwargs.pop("cmd")
        print(cmd(**kwargs))
