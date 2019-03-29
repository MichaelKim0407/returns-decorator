# returns-decorator

[![Build Status](https://travis-ci.com/MichaelKim0407/returns-decorator.svg?branch=master)](https://travis-ci.com/MichaelKim0407/returns-decorator)
[![Coverage Status](https://coveralls.io/repos/github/MichaelKim0407/returns-decorator/badge.svg?branch=master)](https://coveralls.io/github/MichaelKim0407/returns-decorator?branch=master)

## Installation

```bash
pip install returns-decorator
```

## Usage

```python
from returns import returns

@returns(int)
def func(...):
    ...
```

The return value will be converted into `int` before returning.

It's the equivalent of:

```
return int(return_value)
```

On every return statement.

---

It's most useful to convert a generator function into a `tuple`/`list`/`set`/`dict`.

```python
@returns(tuple)
def generator_func():
    yield ...
```

Doing this has a better performance than `list.append`.

---

When `None` is a possible return value,
you can pass `allow_none=True` into the decorator.

```python
@returns(int, allow_none=True)
def func(...):
    if ...:
        return None
    return ...
```
