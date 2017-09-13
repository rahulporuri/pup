from pip import parseopts
from pip.commands.list import ListCommand
from pip.utils import get_installed_distributions

from traits.api import HasTraits, List, Str
from traitsui.api import Group, Item, View


class InstalledPkgsList(HasTraits):
    results_list = List(Str, ["No results to display"])

    list_group = Group(
        Item('_'),
        Item('results_list', style='readonly'),
        Item('_'),
    )

    view = View(
        list_group,
        title='ListEditor',
        buttons=['OK'],
        resizable=True,
    )

    def main(self):
        cmd_name, cmd_args = parseopts(['list'])
        list_ = ListCommand()
        opts, args = list_.parse_args(cmd_args)

        pkgs = get_installed_distributions(
            local_only=opts.local,
            user_only=opts.user,
            editables_only=opts.editable
        )

        # FIXME : hack for the moment
        # figure out how to use ListCommand.output_package_listing_*
        pkgs = [pkg.__str__() for pkg in pkgs]
        self.results_list = list(pkgs)
        self.configure_traits()
    

if __name__ == "__main__":
    InstalledPkgsList().list()
