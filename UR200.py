#Coded by Bizhan001
print ('UR200 v1.00')
#Importing the URL library 
import urllib.request

#The Notes and texts 
print("welcome to UR200 !")
print("read the README file for more information")
input ("press enter to continue ")
print(" ")

#The target URL 
url = input (" Enter the Target URL :  ")

#setting the target URL
weburl = urllib.request.urlopen(url)

#the result of URL opening request
urlcode = str(weburl.getcode())

#checking if target URL is valid or reachable
if urlcode == '200' :
	print ("Target URL : " , url )
	#setting the valid URL for starting the search
	ValidURL = url 

#the wordlist for brute forcing directories of Target URL
filename = input ("Enter the Wordlist file name :  ")
#checking if wordlist exist and setting it as valid wordlist
wordlist = None
try :
	wordlist = open(filename)
	print ('wordlist : ',wordlist)
except :
	print ("No such a file! Exiting program...")
	exit()

print(" ")
#everything is OK isn't it?
print (" Every thing is ready for starting the search")
print ("Target URL : " , url )
print ('wordlist : ',filename)
input ('press enter to start , or press ctrl+C to exit')
#a list for collecting url's
url_list = []
#starting brute force 
for word in wordlist :
	print ('searching for file or directory named' , word)
	test = url + "/" + word
	try :
		weburl = urllib.request.urlopen(test)
		testcode = str(weburl.getcode())
		if testcode == '200' :
			print ('a file or url found! :' , test)
			print ('saving the url')
			url_list.append(test)
	except :
		print (" ")
print ("The valid direcory and files that I've found :")
print (" ")
for url in url_list :
	print (url)