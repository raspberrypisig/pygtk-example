import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

clickcount = 1


def clicked(widget):
    global clickcount
    label.set_label("Button was clicked {} times".format(clickcount))
    clickcount = clickcount + 1

window = Gtk.Window(title="Label And Button")
window.set_size_request(800, 600)
window.set_position(Gtk.WindowPosition.CENTER)
window.connect("delete_event", Gtk.main_quit)

box = Gtk.Box(orientation="vertical")

label = Gtk.Label()
label.set_label("I am a label")
box.add(label)

button = Gtk.Button()
button.set_label("I am a button")
button.connect("clicked", clicked)
box.add(button)

window.add(box)

window.show_all()
Gtk.main()
