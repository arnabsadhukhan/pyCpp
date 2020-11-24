import subprocess
import os
class PyCpp:
	def __init__(self,filename):
		self.filename = filename
	def compile(self):
		self.name = self.filename.split('.')[0]
		self.cmd = f"g++ {self.filename} -o {self.name}"
		print(os.system(self.cmd))
	def run(self,*args):
		out = subprocess.Popen([self.name]+list(args), stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		stdout,stderr = out.communicate()
		return stdout.decode('utf-8')

