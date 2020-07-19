import os
from unittest.mock import MagicMock

import pytest

from texteditor import EDITOR
from texteditor import main as texteditor


def test_EDITOR_used():
    os.environ[EDITOR] = "/path/to/myeditor"
    _run = texteditor.run
    texteditor.run = MagicMock()

    texteditor.open()

    args, kw = texteditor.run.call_args
    cmd = args[0]
    assert cmd[0] == "/path/to/myeditor"
    assert cmd[-1].endswith(".txt")  # the filename

    texteditor.run = _run


def test_EDITOR_with_args():
    os.environ[EDITOR] = "/path/to/myeditor --wait"
    _run = texteditor.run
    texteditor.run = MagicMock()

    texteditor.open()

    args, kw = texteditor.run.call_args
    cmd = args[0]
    assert cmd[0] == "/path/to/myeditor"
    assert cmd[1] == "--wait"
    assert cmd[-1].endswith(".txt")  # the filename

    texteditor.run = _run


def test_EDITOR_with_args_and_spaces():
    os.environ[EDITOR] = "/path\\ to/myeditor --wait"
    _run = texteditor.run
    texteditor.run = MagicMock()

    texteditor.open()

    args, kw = texteditor.run.call_args
    cmd = args[0]
    assert cmd[0] == "/path\\ to/myeditor"
    assert cmd[1] == "--wait"
    assert cmd[-1].endswith(".txt")  # the filename

    texteditor.run = _run


def test_set_extension():
    os.environ[EDITOR] = "myeditor"
    _run = texteditor.run
    texteditor.run = MagicMock()

    texteditor.open(extension="md")

    args, kw = texteditor.run.call_args
    cmd = args[0]
    assert cmd[0] == "myeditor"
    assert cmd[-1].endswith(".md")  # the filename

    texteditor.run = _run


def test_use_filename():
    os.environ[EDITOR] = "myeditor"
    texteditor.run = MagicMock()
    _run = texteditor.run

    texteditor.open(filename="README.md")

    args, kw = texteditor.run.call_args
    cmd = args[0]
    assert cmd[0] == "myeditor"
    assert cmd[-1] == "README.md"  # the filename

    texteditor.run = _run


def test_get_editor():
    os.environ[EDITOR] = ""
    texteditor.run = MagicMock()
    texteditor.open()

    args, kw = texteditor.run.call_args
    cmd = args[0]
    assert cmd[0] == "code"


def test_no_editor_available():
    os.environ[EDITOR] = ""

    def find_nothing(_):
        return None

    _find_executable = texteditor.find_executable
    texteditor.find_executable = find_nothing
    _run = texteditor.run
    texteditor.run = MagicMock()

    # inconceivable!
    with pytest.raises(RuntimeError):
        texteditor.open()

    texteditor.find_executable = _find_executable
    texteditor.run = _run
