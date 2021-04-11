# Site Connectivity Checker V1.0

from  colorama  import  Fore 
from colorama import init
import time
import urllib
from urllib.request import urlopen
import math
init()

exit = "yes"
while exit != "no":
		# FIRST STEP
	print(Fore.GREEN)
	print("First step. Сhecking internet connection")
	url_address = str(input("Enter your URL-address --> "))
	time.sleep(1.5)
	def is_internet():
		# Checking internet connection, using library "urllib"
		try:
			urlopen(url_address, timeout=1)
			return True
		except urllib.error.URLError as Error:
			print(Fore.RED)
			print(Error)
			return False
			k=input("Press close to exit")

	if is_internet():
		print(Fore.GREEN)
		print("There is a connection to the server")
	else:
		print(Fore.RED)
		print("Lost connection")
		print(Fore.WHITE)


		# SECOND STEP
	nf = urlopen(url_address)
	start = time.time()
	page = nf.read()
	end = time.time()
	nf.close()

	ping_time = (end - start) * 10000
	ping_time = math.trunc(ping_time)
	print("Your ping:", ping_time, "ms")
	print(Fore.RED)
	exit = input("Enter 'yes' to retry. To exit enter 'no' --> ")
k=input("Thanks for using;)")