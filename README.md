# TextEditor

Programmatically open your system's $EDITOR from your Python program.
Is like `webbrowser` but for text editors.

```python
import texteditor

text = texteditor.open('This is the default content')
```

Opens a temporary file with some content to edit, and returns the new content when
the user closes the editor.

```python
text = texteditor.open(file='README.md')
# texteditor.open(b"This'll overwrite the former content!", file='README.md')
```

You can also edit an existing text file. If the file cannot be opened, an `OSError`
is raised.


## Installation

Using `pip` of course!

```
pip install texteditor
```


## API

texteditor.**open**(text=None, file=None, suffix=None, encoding=None)

Opens `file` or a new temporary file in the default editor.

text:
	The content for the edited file. This will also be used instead of the
	original contents of `file` if one is also defined.

file:
	Edit this file instead of a new temporary one.

suffix:
	When editing a new temporary file, this will help the editor recognize the
	intended filetype, so syntax highlighting and custom settings for that
	filetype can be used.
	Ignored if `file` is defined.

encoding:
	To encode the content and decode the result, `texteditor.open()` uses the default
	encoding for the platform, but you can use an `encoding` argument to specify
	any text encoding supported by Python.


## How it Works

`texteditor.open()` first looks for the `$EDITOR` environment variable. If set, it uses
the value as-is, including any command-line argument, without fallbacks.

If no `$EDITOR` is set, the function will search through a list of known editors, and
use the first one that founds on the system.


## Contribute

This might have notice this project does not have a `setup.py` file.
It uses a new-standard `pyproject.toml` config file and [Poetry](https://poetry.eustace.io/)
to manage its dependencies. This will create and use a `virtualenv` environment for
this specific project (read more about it in its [Poetry documentation](https://poetry.eustace.io/docs/cli/#install)).

```
poetry install
```

After that, to run the tests, use:

```
pytest .
```
