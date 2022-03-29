import os
import PySimpleGUI as sg
from docx2pdf import convert

# https://holypython.com/gui-with-python-file-browser-and-input-form-pysimplegui-part-iii/

class ManualsDocToPDFSendFTP:

	path_base = None

	def run(self):

		sg.FileBrowse()
		layout = [[sg.Text("Choose a file: "), sg.FileBrowse()]]
		window = sg.Window('My File Browser', layout, size=(300,200))

		for base, dirs, files in os.walk(self.path_base):
			x = convert(base)
			print('	convert ALL files in {} docx to PDF end!!'.format(base))


if __name__ == "__main__":
	
	o = ManualsDocToPDFSendFTP()
	# "C:\\Users\\csanchez\\Dropbox\\SLAMnet\\clientes\\WELLDEX\\gastos\\"
	o.path_base = input('Root path: ')

	o.run()