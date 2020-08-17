# Your code here


def finder(files, queries):
    """
    Return a list of files that match the queries
    """
    # Create a list of file names mapped to all paths that lead to them
    paths = {}
    for file in files:
        fname = file.split('/')[-1]
        paths[fname] = paths.get(fname, [])
        paths[fname].append(file)

    # Iterate over all queries, and add the file paths pointing to each query
    # to result and return it
    result = []
    for query in queries:
        result += paths.get(query, [])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
