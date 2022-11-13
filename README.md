# optional-faker

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/PerchunPak/optional-faker/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/optional-faker/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/PerchunPak/optional-faker/branch/master/graph/badge.svg)](https://codecov.io/gh/PerchunPak/optional-faker)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/optional-faker)](https://www.python.org/downloads/)

Small wrapper around faker, to make values optional!

## Example

```py
>>> from faker import Faker
>>> 
>>> fake = Faker()
>>> Faker.seed(0)
>>> 
>>> # `fake.optional` can take any value, and return it, or None.
>>> fake.optional(fake.pystr())
'RNvnAvOpyEVAoNGnVZQU'
>>> # or it can take callable, and *args with **kwargs
>>> # that will be passed to this callable.
>>> fake.optional(fake.pystr, 1, max_chars=10)
None
>>> # there is no explicit check is callable a faker part,
>>> # so you can pass anything.
>>> fake.optional(lambda: "my callable!")
None
```

## Installing

```bash
pip install optional-faker
```

And then you need to import `optional_faker` anywhere but before creating `Faker` instance.

## Installing for local developing

```bash
git clone https://github.com/PerchunPak/optional-faker.git
cd optional-faker
```

### Installing `poetry`

Next we need install `poetry` with [recommended way](https://python-poetry.org/docs/master/#installation).

If you use Linux, use command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you use Windows, open PowerShell with admin privileges and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installing dependencies

```bash
poetry install
```

### If something is not clear

You can always write me!

## Updating

```bash
pip install -U optional-faker
```

### For local development

For updating, just re-download repository,
if you used `git` for downloading, just run `git pull`.

## Thanks

This project was inspired by [faker-optional](https://github.com/lyz-code/faker-optional).

This project was generated with [fire-square-style](https://github.com/fire-square/fire-square-style).
Current template version: [81f29408150f00e921b0de2b50edc9aeaa8048c7](https://github.com/fire-square/fire-square-style/tree/81f29408150f00e921b0de2b50edc9aeaa8048c7).
See what [updated](https://github.com/fire-square/fire-square-style/compare/81f29408150f00e921b0de2b50edc9aeaa8048c7...master).
