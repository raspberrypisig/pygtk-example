import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window(title="Raspberry Pi SIG")
window.set_size_request(800, 600)
window.set_position(Gtk.WindowPosition.CENTER)
window.connect('delete_event', Gtk.main_quit)
window.show_all()
Gtk.main()
