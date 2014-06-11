Run a command whenever contents of a set of files change.

Example Usage:
onchange.py 'shell command to generate list of files you care about' <command to run on change>
onchange.py 'find . -name \*.c' make new_target

This is essentially a cheap way to do incremental compilation when using non IED environment
