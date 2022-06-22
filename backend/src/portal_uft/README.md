# portal_uft

Portal da UFT utilizando Plone 6.

## Features

### CORS settings

Implement CORS settings for this package

### Content types

- Training

### Initial content

This package contains a simple volto configuration.

Installation
------------

Install portal_uft by adding it to your buildout:
```ini
[buildout]

...

eggs =
    portal_uft
```

Then running `buildout`

And to create the Plone site:

```shell
./bin/instance run scripts/create_site.py
```

## Contribute

- [Issue Tracker](https://github.com/ericof/portal-uft/issues)
- [Source Code](https://github.com/ericof/portal-uft/)

## License

The project is licensed under the GPLv2.
