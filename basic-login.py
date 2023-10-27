import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Page1(Gtk.Window):
    def __init__(self):
        super().__init__(title="Page 1")
        self.set_default_size(1000, 800)

        self.username_entry = Gtk.Entry()
        self.username_entry.set_placeholder_text("Username")
        self.password_entry = Gtk.Entry()
        self.password_entry.set_placeholder_text("Password")
        self.button_next = Gtk.Button(label="Next")
        self.button_next.connect("clicked", self.on_next_clicked)

        # Center-aligned layout
        center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_valign(Gtk.Align.CENTER)
        center_box.pack_start(self.username_entry, False, False, 10)
        center_box.pack_start(self.password_entry, False, False, 10)
        center_box.pack_start(self.button_next, False, False, 10)

        self.add(center_box)

    def on_next_clicked(self, widget):
        self.hide()
        page2.show()

class Page2(Gtk.Window):
    def __init__(self):
        super().__init__(title="Page 2")
        self.set_default_size(1000, 800)

        self.button_back = Gtk.Button(label="Back")
        self.button_back.connect("clicked", self.on_back_clicked)
        self.add(self.button_back)

    def on_back_clicked(self, widget):
        self.hide()
        page1.show()

page1 = Page1()
page2 = Page2()

page1.connect("destroy", Gtk.main_quit)
page2.connect("destroy", Gtk.main_quit)

page1.show_all()

Gtk.main()


 









