import Famcy
from flask import render_template

class WeitungPersonalPageStyle(Famcy.FamcyStyle):
	def __init__(self, title=""):
		super(WeitungPersonalPageStyle, self).__init__()

		# set default value
		self.title = title
		self.desc = ""

		self.loader = Famcy.FamcyStyleLoader()
		self.color_theme = Famcy.FamcyColorTheme()
		self.nav_bar = Famcy.FamcyStyleNavBtns()

	def setHeadScript(self, title=None, desc=None):
		if title:
			self.title = title
		if desc:
			self.desc = desc

	def render(self, extra_script, content, background_flag=False, route="", time=5000, form_init_js=None, end_script="", **kwargs):

		html_header = self.setDashboardHTMLHeader()
		end_js = end_script+self.setDashboardJavaScript()
		color_theme = self.color_theme.render()
		load_spinner = self.loader.render()

		# nav_bar = self.nav_bar.render()

		body_on_load = "background_loop('" + self.main_url + str(route) + "/bgloop" + "', '" + str(route) + "', " + str(time) + ");console.log('start!')" if background_flag else ""
		return render_template("portfolio.html", form_init_js=form_init_js, load_spinner=load_spinner, color_theme=color_theme, html_header=html_header, content=content, extra_script=extra_script, end_js=end_js, body_on_load=body_on_load)
