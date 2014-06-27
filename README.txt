Run a command whenever contents of a file/set of files/files in a directory changes.

Example Usage:
onchange.py 'shell command to generate list of files you care about' <command to run on change>
onchange.py 'find . -name \*.c' make new_target

You can also pass in a filename
onchange.py somefile ...  -> onchange.py 'echo somefile' ...
And also
onchage.py somedir ... -> onchange.py 'find somedir -type f' ...

This is essentially a cheap way to do incremental compilation when using non IDE environment
