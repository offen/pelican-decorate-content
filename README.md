# pelican-decorate-content

A Pelican plugin for rule-based addition of classes to your content. This can be useful when you use a functional CSS toolset (e.g. Tachyons) to style your site and do not want to write custom CSS targeting your content.

## Installation

Install from PyPi:

```
pip install pelican_decorate_content
```

## Usage

In your `pelicanconf.py` import the plugin and add it to `PLUGINS`:

```py
from pelican_decorate_content import decorate_content

# ...

PLUGINS = [decorate_content,] # mix and match with other plugins as needed
```

## Configuration

### Global settings

Global configuration happens in a `DECORATE_CONTENT` setting in `pelicanconf.py`. It is a dict that maps CSS selectors to a list of classes that will be added to each match:

```py
DECORATE_CONTENT = {
    'h1': ['f2', 'normal', 'lh-title', 'mt3', 'ma0', 'mb3'],
    'h2': ['f25', 'normal', 'lh-title', 'mt4', 'ma0', 'mb3'],
    'h3': ['f5', 'normal', 'mt5', 'ma0', 'mb3'],
    'h4': ['f5', 'normal', 'mt4', 'ma0', 'mb1'],
    'h5': ['f5', 'normal', 'mt2', 'ma0', 'mb1'],
    'h6': ['f5', 'lh-solid', 'normal', 'ma0', 'light-silver'],
}
```

### Overrides on article or page level

Overrides for these global defaults can be added in your article or page's front matter by defining a JSON string as `decorate_content`:

```yaml
decorate_content: '{"h1": ["f3", "bold"]}' # this overrides the entire key
```

## License

Copyright 2020 Frederik Ring - Available under the MIT License
