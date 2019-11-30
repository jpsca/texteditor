# TextEditor

Programmatically open the system's editor from your Python program (like [webbrowser](https://docs.python.org/3.7/library/webbrowser.html) but for text editors).

Unlike other libraries, *TextEditor* makes an effort to find the text editor the users really prefer, specially for those that doesn't know what an `EDITOR` environment variable is.

```python
import texteditor

text = texteditor.open('This is the starting content')
```

Opens a temporary file with some content to edit, and returns the new content when
the user closes the editor.

```python
text = texteditor.open(filename='README.md')

# text = texteditor.open("This will be used instead of the file content", filename='README.md')
```

You can also edit an existing text file. If the file cannot be opened, an `OSError` is raised.


## Installation

Using `pip` of course!

```
python -m pip install texteditor
```

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

If no `$EDITOR` is set, it will try to guess.

On MacOS, it calls the system default for *editing* that file extension.

In other operating systems, the function will search through a *very short* list of known editors, and use the
first one that founds.

You might notice that vim and Emacs are not in that short list, that's because:

1. If you are using it, you know what the `EDITOR` variable is, and you probably has set it already.
2. If you aren't using it, finding yourself in their UI for the first time is going to be super confusing.
   In fact "How to exit vim" is a common Stack Overflow question. Having to google how to set an EDITOR
   variable is a less scary alternative.

