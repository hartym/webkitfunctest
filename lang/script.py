import gtk

class Script(object):
    def __init__(self, source):
		self.source = source
		self.p_currentline = 0
		self.report = []

    def __call__(self, view, frame):
		try:
			currentline = self.source[self.p_currentline]
		except IndexError:
			print '\n'.join(self.report)
			gtk.main_quit()
			return

		self.p_currentline += 1

		# run
		getattr(self, 'run_%s' % currentline[0])(view, frame, *currentline[1:])

    def run_open(self, view, frame, url):
        view.open(url)

    def run_assert(self, view, frame, *args):
		if str(frame.get_data_source().get_data()).find(args[0]) == -1:
			self.report += ['FAIL >>> line %d failed: %r' % (self.p_currentline, args)]
		else:
			self.report += ['PASS >>> line %d' % self.p_currentline]

		return self(view, frame)

