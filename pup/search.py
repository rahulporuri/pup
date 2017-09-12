from pip import parseopts
from pip.commands.search import SearchCommand

from traits.api import HasTraits, List, Str
from traitsui.api import Group, Item, View


class SearchList(HasTraits):
    search_results_list = List(Str, ["No results to display"])

    list_group = Group(
        Item('_'),
        Item('search_results_list', style='readonly'),
        Item('_'),
    )

    view = View(
        list_group,
        title='ListEditor',
        buttons=['OK'],
        resizable=True,
    )


if __name__ == "__main__":
    search = SearchCommand()
    _, cmd_args = parseopts(['search', 'numpy'])
    opts, args = search.parse_args(cmd_args)

    results = search.search(args, opts)
    results_list = [
        "{}: {}".format(result['name'], result['version'])
        for result in results
    ]

    search_list = SearchList(search_results_list=results_list)
    search_list.configure_traits()
