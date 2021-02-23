import os
from colorama import Fore, Back, Style
def cls():
	linux = 'clear'
	termux = 'clear'
	windows = 'cls'
	os.system([linux, termux, windows][os.name == 'nt'])
cls()
print(Fore.GREEN)
banner = '\n'
banner += ' ###################################\n'
banner += ' # ZIP Password BruteForce         #\n'
banner += ' ###################################\n'
banner += ' # Coded By Fearless327            #\n'
banner += ' ###################################\n'
banner += ' GitHub:\n'
banner += ' https://github.com/Fearless327/ZIP-Pass-BruteForce\n\n'
banner += ' [1] Zip Password Cracker\n'
banner += ' [0] Exit\n'
print(Fore.GREEN)
print banner

a=input(" [?] Enter Number : ")
if a==0:
 import os
 cls()
 print " [!] Thank You! For Using My Program. Good Bye :)"
 quit()
elif a==1:

 import zipfile
 import os
 from time import time
 print(Fore.RED)
 cls()
 textzippass = ''' #########################################
  Zip Password Brute Force (Top Speed)  
#########################################
 '''
 print textzippass
 file_path = raw_input (" [+] ZIP File Address: ")
 print ""
 word_list = raw_input (" [+] Password List Address: ")
 print(Fore.GREEN)
 def main(file_path, word_list):
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print " [!] Please check the file's Path. It doesn't seem to be a ZIP file."
		quit()

	password = None 
	i = 0 
	c_t = time()
	with open(word_list, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			try:
				zip_.extractall(pwd=password)
				t_t = time() - c_t 
				print "\n [*] Password Found! \n" + " [*] The Password!: "+password+"\n"
				print " [***] Took %f seconds to Srack the Password. That is, %i attempts per second." % (t_t,i/t_t)
				quit()
			except Exception:
				pass
		print " [X] Password Not Found! "
		quit()
 main(file_path, word_list)
