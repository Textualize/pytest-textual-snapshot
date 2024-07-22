# `pytest-textual-snapshot`

A pytest plugin for snapshot testing Textual applications.

<img width="1325" alt="image" src="https://github.com/user-attachments/assets/a5079356-ef0f-4c7e-9ed2-bf2115e75c4f">

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

You can run your tests using `pytest` as normal. You can use `pytest-xdist` to run your tests in parallel.

#### My snapshot test failed, what do I do?

If your snapshot test fails, it means that the screenshot taken during the test session
differs from the last screenshot taken.
This change is shown in the failure report, which you'll be given a linked to in the event of a failure.

If the diff shown in the failure report looks correct, you can update the snapshot on disk
by running `pytest` with the `--snapshot-update` flag.

### Writing tests

#### Basic usage

Inject the `snap_compare` fixture into your test and call
it with an app instance or the path to the Textual app (the file containing the `App` subclass).

```python
def test_my_app(snap_compare):
    app = MyTextualApp()  # a *non-running* Textual `App` instance
    assert snap_compare(app)
```

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

#### Run code before screenshot

You can run some code before capturing a screenshot using the `run_before` parameter.

```python
def test_something(snap_compare):
    async def run_before(pilot: Pilot):
        await pilot.press("ctrl+p")
        # You can run arbitrary code before the screenshot occurs:
        await disable_blink_for_active_cursors(pilot)
        await pilot.press(*"view")

    assert snap_compare(MyApp(), run_before=run_before)
```

#### Customizing the size of the terminal

If you need to change the size of the terminal (for example to fit in more content or test layout-related code), you can adjust the `terminal_size` parameter.

```python
def test_another_thing(snap_compare):
    assert snap_compare(MyApp(), terminal_size=(80, 34))
```

#### Quickly opening paths in your editor

If you passed a path to `snap_compare`, you can quickly open the path in your editor by setting the `TEXTUAL_SNAPSHOT_FILE_OPEN_PREFIX` environment variable based on the editor you want to use. Clicking on the path in the snapshot report will open the path in your editor.

- `file://` - default, most likely opening in your browser
- `code://file/` - opens the path in VS Code
- `cursor://file/` - opens the path in Cursor
- `pycharm://` - opens the path in PyCharm

