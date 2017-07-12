import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('practice.glade')
window = builder.get_object('mainwindow')
window.connect('delete_event', Gtk.main_quit)

texteditor = builder.get_object('texteditor')
buffer = texteditor.get_buffer()
buffer.set_text('type some text here')

window.show_all()
Gtk.main()
