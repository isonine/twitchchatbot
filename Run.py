import string
from selenium import webdriver
from wordcloud import WordCloud
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
import time

time1 = int(time.time())
time2 = int(time.time())+300
s = openSocket()
joinRoom(s)
readbuffer = ""
messageList = []
#driver=webdriver.Chrome()
#driver.get("https://twitch.tv/proleaguecsgo")
while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			user = getUser(line)
			message = str(getMessage(line)).replace("\r","")
			messageList.append(message)

			time1 = int(time.time())
			print user + " typed :    " + message + "             " + str(time2-time1)
			#word cloud
			if "makecloud" in message or (time2-time1)<=0:
				time1 = int(time.time())
				time2 = time1+300
				messageListFinal=str(messageList)
				messageListFinal=messageListFinal.replace(","," ")
				messageListFinal=messageListFinal.replace("'","")
				wordcloud = WordCloud(width=1200, height=1200).generate(messageListFinal)
				image = wordcloud.to_image()
				image.show()
				messageList=[]
				print("i hope it worked")


