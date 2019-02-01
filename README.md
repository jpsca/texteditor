# TextEditor

*Like [webbrowser](https://docs.python.org/3.7/library/webbrowser.html) but for the text editor.*

Programmatically open the system's editor from your Python program.

```python
import texteditor

text = texteditor.open('This is the starting content')
```

Opens a temporary file with some content to edit, and returns the new content when
the user closes the editor.

```python
text = texteditor.open(filename='README.md')

# text = texteditor.open(
#     "This will be used instead of the file content", filename='README.md'
# )
```

You can also edit an existing text file. If the file cannot be opened, an `OSError`
is raised.


## Installation

Using `pip` of course!

```
pip install text-editor
```

*Note that the name of the library has a dash: text**-**editor*

## Usage

*texteditor*.**open**(text=None, filename=None, extension='txt', encoding=None)

Opens `filename` or a new temporary file in the default editor.

- *text*:
    The starting content for the edited file. This will also be used instead of the
    original contents of `filename` if one is also defined.

- *filename*:
    Edit this file instead of a new temporary one.

- *extension*:
    When editing a new temporary file, this will help the editor recognize the
    intended filetype, so syntax highlighting and custom settings for that
    filetype can be used. Examples: `txt`, `md`, `ini`.
    Ignored if `filename` is used.

- *encoding*:
    To encode the content and decode the result, `texteditor.open()` uses the default
    encoding for the platform, but you can use an `encoding` argument to specify
    any text encoding supported by Python.


## How it Works

`texteditor.open()` first looks for the `$EDITOR` environment variable. If set, it uses
the value as-is, including any command-line argument, without fallbacks.

If no `$EDITOR` is set, the function will search through a *very short* list of known
editors, and use the first one that founds on the system.


## Contribute

This might have notice this project does not have a `setup.py` file.
It uses a new-standard `pyproject.toml` config file and [Poetry](https://poetry.eustace.io/)
to manage its dependencies. This will create and use a `virtualenv` environment for
this specific project (read more about it in its [Poetry documentation](https://poetry.eustace.io/docs/cli/#install)).

```
poetry install
```

After that, to run the tests, use:

```
pytest tests.py
```
