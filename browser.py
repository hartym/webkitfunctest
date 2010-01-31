#!/usr/bin/env python

import gtk
import webkit
import gobject

import ui.window
import lang.script

script = (
		('open', 'http://www.google.fr/'), 
		('assert', 'Google'), 
		('open', 'http://www.perdu.com/'), 
		('assert', 'Trouve'), 
	)

script = lang.script.Script(script)

# init threads
gobject.threads_init()

# create main window
app = ui.window.App(script)
app.open('http://google.fr')
gtk.main()

