import sys
import os
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

username = ""
password = ""

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(1000, 800)

        # Create a top-level container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Create a label for the title
        title_label = Gtk.Label()
        
        # Set text and attributes using Pango markup
        title_markup = "<span size='xx-large' weight='bold'>Hardening Script</span>"
        title_label.set_markup(title_markup)
        title_label.set_justify(Gtk.Justification.CENTER)
        title_label.set_halign(Gtk.Align.CENTER)

        # Add the title label to the top of the main container
        main_box.pack_start(title_label, False, False, 0)
        
        # Create a Box for username and password input fields
        input_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        # Username Entry
        username_entry = Gtk.Entry()
        username_entry.set_placeholder_text("Username")
        username_entry.connect("changed", self.on_username_changed)
        
        # Password Entry
        password_entry = Gtk.Entry()
        password_entry.set_placeholder_text("Password")
        password_entry.set_visibility(False)  # Make the password entry hide characters
        password_entry.connect("changed", self.on_password_changed)

        input_box.pack_start(username_entry, False, False, 0)
        input_box.pack_start(password_entry, False, False, 0)
        
        # Add the input box to the main container
        main_box.pack_start(input_box, False, False, 0)

        # Create the content of your main window here, e.g., buttons, labels, etc.
        main_content = Gtk.Box()
        # Add your content to the main_content Box

        # Create a ScrolledWindow to contain the main content
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled_window.add(main_content)

        # Pack the ScrolledWindow beneath the title
        main_box.pack_start(scrolled_window, True, True, 0)

        # Add the main_box to the window
        self.add(main_box)

    def on_username_changed(self, widget):
        global username
        username = widget.get_text()

    def on_password_changed(self, widget):
        global password
        password = widget.get_text()

command = "echo" + password
os.system(command)

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
