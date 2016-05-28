import sys
import gtk

class Builder(gtk.Builder):
	def get_widget_prefix(self, prefix):
		for widget in self.get_objects():
			if 'get_name' in dir(widget):
				if widget.get_name().startswith(prefix):
					yield widget
		return
Builder.get_widget = Builder.get_object

gtk.Builder = Builder
