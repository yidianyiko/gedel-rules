# User Lessons

# Cursor Lessons

# Lessons

## User Specified Lessons

- You have a python venv in ./venv. Always activate it when doing Python development. First check if uv is available with `which uv`, if available, activate venv first, then use `uv pip install` to install packages, otherwise use pip.
- Program output should include useful debug information.
- Always read files before editing them.
- Due to Cursor limitations, git/gh multi-line commit messages need to be written to a file first then committed with -F parameter, and add [Cursor] prefix.

## Meta Rules Supplement

- Every time encountering new tasks, tools, or lessons learned, must proactively sync to corresponding md files (todo.md, tools.md, lessons.md), and check if recording is needed after each major operation step. This ensures strict adherence to meta rules and guarantees accumulation and reuse of tasks, tools, and experiences.

## Current Process Lessons Learned

- When developing automation scripts, must strictly compare against target JSON format, not just focus on content fields, but also structure (like list to dict conversion, key naming, etc.).
- Every time encountering new tools, tasks, experiences, must sync to tools.md, todo.md, lessons.md to avoid missing knowledge accumulation.
- Task decomposition, progress tracking, tool registration, and experience summary should become standard steps in every automation workflow.

## Cursor Learned

- Search results need proper handling of different character encodings (UTF-8) to support internationalized queries