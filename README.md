# AI Editor

App for editing articles with a help from ChatGPT

## Prerequisites

- [Python 3](https://www.python.org/)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)

## Installation

From the root folder, install the dependencies:

```
pipenv install
```

## Usage

1. Put an article you want to edit in the folder "article". Ensure there are no other files in the folder.

2. Run the app:

```
python main.py
```

3. In the folder "Output" you will get a *`output.docx`* file with:
- three propositions of title,
- three propositions of lead,
- selected, interesting quotes (excerpts to be highlighted in the text)
- the edited text.
