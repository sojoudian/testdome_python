def group_by_owners(files):
    result = {}
    for file, owner in files.items():  # use files.iteritems() on Python 2.x
        result[owner] = result.get(owner, []) + [file]  # you can use setdefault(), too
    return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
