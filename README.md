# python-puppeteer-uptime-checker

 Python version of the [Simple Puppeteer uptime checker](https://github.com/theDavidBarton/simple-puppeteer-uptime-checker).

## Install

```
$ pip install -r requirements.txt
```

_Note:_ This project depends on deprecated [pyppeteer](https://github.com/pyppeteer/pyppeteer) pckage. As it is is unmaintained and has been outside of minor changes for a long time. They advise considering [playwright-python](https://github.com/microsoft/playwright-python) as an alternative.

## Setup

Create a [site-config.json](./site-config.json) at the root of your Node.js project with the (1) sites you want to monitor, and (2) add one key element's [selector](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors) as well per url (be careful using simply `"body"`, as even error pages has a valid `<body>` element).

In this example the first site will throw an error due to bad ssl certificate:

```json
[
  { "site": "https://expired.badssl.com/", "selector": "#dashboard" },
  { "site": "https://badssl.com/", "selector": "#dashboard" },
  { "site": "https://google.com", "selector": "body" }
]
```

## Run monitoring

```
$ python main.py
```

Output:
```
$ python main.py
- https://expired.badssl.com/ retries after 1 unsuccessful attempt(s)
- https://expired.badssl.com/ retries after 2 unsuccessful attempt(s)
- https://expired.badssl.com/ retries after 3 unsuccessful attempt(s)
HEALTH CHECK FAILED on https://expired.badssl.com/ with HTTP unknown status (PageError)
HEALTH CHECK PASSED on https://badssl.com/ with HTTP 200
HEALTH CHECK PASSED on https://google.com with HTTP 200
```

## GitHub Actions usage

Example:

```yml
name: monitoring
on:
  workflow_dispatch:
jobs:
  run-health-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - name: Use Python 3
        uses: actions/setup-python@v3
        with:
          python-version: 3.12
      - name: Install project
        run: pip install -r requirements.txt
      - name: Run health check
        run: python main.py
 ```

# License

MIT License

Copyright (c) 2023 David Barton
