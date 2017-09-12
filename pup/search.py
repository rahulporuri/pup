from __future__ import print_function

from pip import parseopts
from pip.commands.search import SearchCommand


if __name__ == "__main__":
    search = SearchCommand()
    _, cmd_args = parseopts(['search', 'numpy'])
    opts, args = search.parse_args(cmd_args)

    results = search.search(args, opts)
    print(*["{}: {}".format(result['name'], result['version']) for result in results], sep='\n')
