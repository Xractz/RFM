#Script by https://t.me/IlhamWI
#407 Authentic Exploit
	

MT = "\033[31;1m"
MG = "\033[31;2m"
C = "\033[0m"
BG = "\033[37;7;1m"
Y = "\033[33;1;3m"
H = "\033[32;1m"
W = "\033[37;1m"
U = "\033[4m"

exploit = [
"/filemanager/dialog.php",
"/admin/filemanager/dialog.php",
"/admin/js/filemanager/dialog.php",
"/admin/js/plugins/filemanager/dialog.php",
"/admin/js/tinymce/filemanager/dialog.php",
"/admin/js/tiny_mce/filemanager/dialog.php",
"/admin/js/tinymce/plugins/filemanager/dialog.php",
"/admin/assets/plugins/filemanager/dialog.php",
"/admin/plugins/filemanager/dialog.php",
"/admin/tinymce/filemanager/dialog.php",
"/admin/tinymce/plugins/filemanager/dialog.php",
"/admin/tinymce/js/tinymce/filemanager/dialog.php",
"/assets/filemanager/dialog.php",
"/assets/js/filemanager/dialog.php",
"/assets/js/plugins/filemanager/dialog.php",
"/assets/js/tinymce/filemanager/dialog.php",
"/assets/js/tiny_mce/filemanager/dialog.php",
"/assets/js/tinymce/plugins/filemanager/dialog.php",
"/assets/assets/plugins/filemanager/dialog.php",
"/assets/plugins/filemanager/dialog.php",
"/assets/tinymce/filemanager/dialog.php",
"/assets/tinymce/plugins/filemanager/dialog.php",
"/assets/tinymce/js/tinymce/filemanager/dialog.php",
"/assets/tiny_mce/js/tinymce/plugins/filemanager/dialog.php",
"/js/filemanager/dialog.php",
"/tinymce/filemanager/dialog.php",
"/file_manager/filemanager/dialog.php",
"/responsivefilemanager/filemanager/dialog.php",
"/responsive_filemanager/filemanager/dialog.php",
"/assets/file_manager/filemanager/dialog.php",
"/admin/js/filemanager/dialog.php",
"/assets/lib/filemanager/dialog.php",
"/panel/filemanager/dialog.php",
"/plugins/filemanager/dialog.php",
"/third_party/filemanager/dialog.php",
"/rfm/filemanager/dialog.php",
"/public/filemanager/dialog.php",
"/libs/filemanager/dialog.php",
"/includes/filemanager/dialog.php",
"/media/filemanager/dialog.php",
"/editor/filemanager/dialog.php",
"/scripts/filemanager/dialog.php",
"/jscripts/filemanager/dialog.php",
"/jscripts/tinymce/plugins/filemanager/dialog.php",
"/jscripts/tinymce/js/tinymce/plugins/filemanager/dialog.php",
"/tiny_mce/plugins/filemanager/dialog.php",
"/tiny_mce/js/tinymce/plugins/filemanager/dialog.php",
"/tinymce/js/tinymce/plugins/filemanager/dialog.php",
"/tinymce/filemanager/dialog.php",
"/phpformbuilder/plugins/filemanager/dialog.php",
"/static/plugins/filemanager/dialog.php",
"/include/filemanager/dialog.php"
]



def logo():
	os.system('clear')
	print(C + MT + """\t ______    _______  __   __ 
\t|    _ |  |       ||  |_|  |  """ + H + """* """ + W + """Author  : Ilham Wahyudi""" + MT + """
\t|   | ||  |    ___||       |  """ + H + """* """ + W + """Contact : """ + U + """https://t.me/ilhamw""" + C + MT + """
\t|   |_||_ |   |___ |       |  """ + H + """* """ + W + """Team    : 407 Authenic Exploit""" + MT + """
\t|    __  ||    ___||""" + MG + """       |  """ + C + H + """* """ + W + """Info    : Auto scan vulnerability """ + MG + """
\t|   |  | ||   |    | ||_|| |\t\t""" + C + W + """  Responsive File Manager""" + MG + """
\t|___|  |_||""" + C + Y + """Checker  v0.1""" +  C + MG + """||_|""" + C + W + """\t\t  in Python 3 with threads""")
	print(BG + "\t            Vulnerability Responsive File Manager Checker           \n\n" + C)
	
def check(site):
	try:
		r = requests.get(site)
		cek = r.status_code
		if '200' in str(cek):
			print(C + W +"\tConnected to " + U + site + C + W +" [" + H + str(cek) + W + "]")
		else:
			print(C + W +"\tDisconnected " + U + site + C + W +" [" + MT + str(cek) + W + "]")
	except:
		print(C + MT +"\t*" + W + " Site ERROR")
		sys.exit()


def starting(site):
	for i in exploit:
		r = requests.get(site+i).text
		if '<div class="uploader">' in str(r):
			print(H + "* " + W + U + site + str(i) + C + W +" [" + H + "Found" + W + "]")
			xmd = input("\tContinue (y/n) : ")
			if xmd == "n" :
				sys.exit()
			elif xmd == "y" :
				continue
			else:
				print(MT + "\t* " + W + "ERROR")
				sys.exit()
				
		elif '<title>Not Acceptable!</title>' in str(r):
			print(W +"\t" + U + site + C + W +" [" + MT + "Mod Security Detected" + W + "]")
			sys.exit()
		else:
			print(MT + "* " + W + site + str(i) + C + W +" [" + MT + "Not Found" + W + "]")
			
def menu():
	logo()
	print(W + "\tPlease use http or https")
	site = input("\tSite : " + U)
	check(site)
	print(C + 	"\tStarting...\n")
	time.sleep(2)
	t = threading.Thread(target=starting, args=(site,))
	t.start()
		
if __name__ == '__main__':
	try:
		import os, sys, time, requests
		import threading
	except:
		logo()
		print(MT + "\t* " + W + "Module requests not installed")
		print(MT + "\t* " + W + "pip install requests")
		sys.exit()
	menu()