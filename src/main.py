from GUI import TextEditor, Window, Menu, Font, StdFonts, application
from GUI.StdMenus import basic_menus

font_size = StdFonts.application_font.size
mono_font = Font("Courier", font_size)
sans_font = Font("Helvetica", font_size)

tab_text = \
"""X----X----X
A\tB\tC"""

test_text = \
"""This is just an example of
how you could insert any text that you want
in this editor at any time
"""

menus = [
    Menu("Test", [
        ("Set Text/4", 'set_text_cmd'),
        ("Monospaced Font/5", 'mono_cmd'),
        ("Sans-Serif Font/6", 'sans_cmd'),
    ]),
]


class TestWindow(Window):

    def setup_menus(self, m):
        Window.setup_menus(self, m)
        m.show_selection_cmd.enabled = True
        m.set_selection_cmd.enabled = True
        m.show_text_cmd.enabled = True
        m.set_text_cmd.enabled = True
        m.mono_cmd.enabled = True
        m.sans_cmd.enabled = True
        m.show_tab_spacing_cmd.enabled = True

    def set_text_cmd(self):
        self.view.text = test_text

    def mono_cmd(self):
        self.view.font = mono_font
        self.setup_tabs()

    def sans_cmd(self):
        self.view.font = sans_font
        self.setup_tabs()

    def setup_tabs(self):
        self.view.tab_spacing = self.view.font.width("X----")


def make_window():
    win = TestWindow(position=(10, 50), size=(600, 800), auto_position=True, title='The JSONing')
    view = TextEditor(width=600, height=800, scrolling='hv', anchor='ltrb')
    win.view = view
    win.setup_tabs()
    view.text = tab_text
    win.add(view)
    view.become_target()
    win.show()

make_window()

app = application()
app.menus = basic_menus() + menus
app.run()