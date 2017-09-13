from traits.api import HasTraits, Button, Int
from traitsui.api import View


class MainOptionsWindow(HasTraits):
    list_pkgs = Button('List pkgs')
    search_pkgs = Button('Search pkgs')
    
    def _list_pkgs_fired(self):
        from list_pkgs import main
        main()

    def _search_pkgs_fired(self):
        from search import main
        main()

    traits_view = View(
        'list_pkgs',
        'search_pkgs',
        title='Pup',
        buttons=['OK'],
        resizable=True
    )


opts_windows = MainOptionsWindow()


if __name__ == '__main__':
    opts_windows.configure_traits()
