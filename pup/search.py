from pip import parseopts
from pip.commands.search import SearchCommand

from traits.api import HasTraits, List, Str
from traitsui.api import CheckListEditor, Group, UItem, View


class SearchList(HasTraits):
    search_results_list = List(Str, ["No results to display"])

    # FIXME : haven't figured out how to scroll through the checklist
    # which is why we are using 6 cols to display the list/data
    checklist = List(
        editor=CheckListEditor(
            name='search_results_list',
            cols=6,
        )
    )

    checklist_group = Group(
        '10',
        UItem('checklist', style='custom'),
        '_', '10',
    )

    view = View(
        checklist_group,
        title='CheckListEditor',
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
