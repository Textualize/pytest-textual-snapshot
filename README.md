# pytest-textual-snapshot

Snapshot testing for Textual apps.

## Installation

Install using `pip`:

```
pip install pytest-textual-snapshot
```

After installing, the `snap_compare` fixture will automatically be made available.

## About

A `pytest-textual-snapshot` test saves an SVG screenshot of a running Textual app to disk. 
The next time the test runs, it takes another screenshot and compares it to the saved one.
If the new screenshot differs from the old one, the test fails.
This is a convenient way to quickly and automatically detect visual regressions in your applications.

## Usage

### Running tests

You can run your tests using `pytest` as normal.

#### My snapshot test failed, what do I do?

If your snapshot test fails, it means that the screenshot taken during the test session
differs from the last screenshot taken.
This change is shown in the failure report, which you'll be given a linked to in the event of a failure.

If the diff shown in the failure report looks correct, you can update the snapshot on disk
by running `pytest` with the `--snapshot-update` flag.

### Writing tests

#### Basic usage

Inject the `snap_compare` fixture into your test and call
it with the path to the Textual app (the file containing the `App` subclass).

```python
def test_something(snap_compare):
    assert snap_compare("path/to/app.py")
``` 

#### Pressing keys

Key presses can be simulated before the screenshot is taken.

```python
def test_something(snap_compare):
    assert snap_compare("path/to/app.py", press=["tab", "left", "a"])
```
