import gtk
import webkit

class View(webkit.WebView): pass

class App(object):
	def __init__(self, script):
		self.script = script
		self._window = gtk.Window()
		self.view = View()
		self._window.add(self.view)
		self._window.show_all()
		self.view.connect('load-finished', self._view_load_finished_cb)

	def open(self, uri):
		self.view.open(uri)

	def _view_load_finished_cb(self, view, frame):
		self.script(view, frame)

