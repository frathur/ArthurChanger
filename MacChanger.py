import subprocess
import re
from colorama import Fore, Back, init, Style

init() 
subprocess.call(["figlet","ArthurChanger"])

def mac_changer():
	subprocess.call(["sudo","ifconfig",interface,"down"])
	subprocess.call(["sudo","ifconfig",interface,"hw","ether",mac_address])
	subprocess.call(["sudo","ifconfig",interface,"up"])

def show_new_mac():
	ifconfig = subprocess.check_output(["ifconfig",interface])
	new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
	
	if new_mac:
		return new_mac.group(0)
	else:
		return None 
	
try:	
	interface = input("[*] Choose Interface: ")
	mac_address = input("[*] Enter new MAC-Address: ")
	mac_changer()
	change_adr = show_new_mac()

	if mac_address==change_adr:
		print(Fore.GREEN+"""
			+- - - - - - - - - - - - - - - - - - - - +
			| 	     CONGRATULATIONS 		 |
			|    MAC-ADDRESS CHANGED SUCCESSFULLY    |
			+- - - - - - - - - - - - - - - - - - - - +
		"""+Style.RESET_ALL)
		confirm = input("Do you want to confirm if your mac-address has been change Yes(Y) / No(N):")
		
		if confirm.upper() == "Y" or confirm.upper() == "YES":
			print(Fore.BLUE+"[*]",Fore.GREEN+"ether = ",Fore.RED+change_adr)
		else:
			print(Fore.GREEN+"\tYou can check manually by using (ifconfig <interface>)")
	else:
		print(Fore.RED+"\tError Occured, restart with a valid Address")
except Exception as e:
	print(Fore.RED+f"Error Message: {e}")




