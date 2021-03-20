import json 
import os
try:
	from tkinter import *
	from tkinter import messagebox
except:
	import Tkinter
	
# filenameYouwannaOpen 
# variable will create or open a file with the name you specified...

fileNameYouwannaOpen = "content.json";

class loadJsonFileToProgram:

	def __init__(self):
		try:
			f = open(fileNameYouwannaOpen)
			self.data = json.load(f)
		except:
			self.data = "false";



	def DoTheSavings(self,content):
		if self.data == "false":
			makingNewDataContainerFile = []
			makingNewDataContainerFile.insert(0,content)
			with open(fileNameYouwannaOpen, "w") as write_file:
				json.dump(makingNewDataContainerFile, write_file)
		else:
			sameData = self.data
			sameData.insert(0,content)
			with open(fileNameYouwannaOpen, "w") as write_file:
				json.dump(sameData, write_file)



# Creating the loadJsonInstance
load = loadJsonFileToProgram()




def sendDataAndSaveOnJsonFile():

	# this variables are going to be tuples

	phoneNumberDivider = phone.get()
	landlineDivider = landline.get()
	emailsDivider = emails.get()


	NewObject = {
	"Name":name.get(),
	"Lastname": lastname.get(),
	"Notes": notes.get(),
	"Address":address.get(),
	"Phone":phoneNumberDivider.split(" "),
	"Landline":landlineDivider.split(" "),
	"Emails":emailsDivider.split(" "),
	"smsSend":"false"
	}
	# print(NewObject) //// to check values....
	if name.get() == "" or lastname.get() == "" or notes.get() == "" or phone.get() == "" or landline.get() == "" or emails.get()== "":
		messagebox.showinfo('error','you are missing Something')
	else:
		messagebox.showinfo("Info", NewObject)
		load.DoTheSavings(NewObject)
		cleanTextInputs()
	


def cleanTextInputs():
	name.delete("0","end")
	lastname.delete("0","end")
	notes.delete("0","end")
	address.delete("0","end")
	phone.delete("0","end")
	landline.delete("0","end")
	emails.delete("0","end")


root = Tk()
root.title("Client Management")

# space
Label(text="        ", width=30).grid(row=1, column=0)
Label(text="        ", width=30).grid(row=1, column=1)

# name
Label(text="NAME" ,width=30).grid(row=2,column=0)
name = Entry(text="Name", width=30)
name.grid(row=2, column=1)
# last name
Label(text="LAST NAME" ,width=30).grid(row=3,column=0)
lastname = Entry(text="Lastname", width=30)
lastname.grid(row=3, column=1)
# Notes
Label(text="NOTES" ,width=30).grid(row=4,column=0)
notes = Entry(text="Notes", width=30)
notes.grid(row=4, column=1)
# Full address
Label(text="ADDRESS" ,width=30).grid(row=5,column=0)
address = Entry(text="address", width=30)
address.grid(row=5, column=1)
# Phone
Label(text="PHONE NUMBER" ,width=30).grid(row=6,column=0)
phone = Entry(text="PhoneNumber", width=30)
phone.grid(row=6, column=1)
# LandLine
Label(text="LANDLINE" ,width=30).grid(row=7,column=0)
landline = Entry(text="Landline", width=30)
landline.grid(row=7, column=1)
# Emails
Label(text="EMAIL" ,width=30).grid(row=8,column=0)
emails = Entry(text="Email", width=30)
emails.grid(row=8, column=1)

Button(text="Save",width=25 , command = sendDataAndSaveOnJsonFile).grid(row=9, column=1)

# space
Label(text="       ", width=30).grid(row=10, column=0)
Label(text="       ", width=30).grid(row=10, column=1)

# more space
Label(text="       ", width=30).grid(row=11, column=0)
Label(text="       ", width=30).grid(row=11, column=1)

# search part of the program....
objectIndex=None

def deletePosibleClient(index):
	# function to delete clients from the list
	try:
		dataContainerReCall = load.data
		dataContainerReCall.pop(index)
		with open(fileNameYouwannaOpen, "w") as write_file:
			json.dump(dataContainerReCall, write_file)
			messagebox.showinfo('DELETED CLIENT','The client Have been Deleted...')
	except:
		messagebox.showinfo('looking','You dont have eny clients on file')


# function that shows user, what it found... on the jsonfile
def showDataFoundONtheSearch(data,index):
	Label(text="       ", width=30).grid(row=13, column=1)
	Label(text="       ", width=30).grid(row=14, column=1)
	Label(text="       ", width=30).grid(row=15, column=1)
	Label(text=data["Name"],width=25,font=("notepad", 10)).grid(row=16,column=0)
	Label(text=data["Lastname"],width=25,font=("notepad", 10)).grid(row=16,column=1)
	Label(text=data["Notes"],font=("Arial", 10)).grid(row=16,column=2)
	Label(text=data["Address"],width=35,font=("Arial", 10)).grid(row=16,column=3)

	for x in range(len(data['Emails'])):
		Label(text=data["Emails"][x],font=("Arial", 10)).grid(row=17,column=x)

	Label(text="       ", width=30).grid(row=18, column=0)
	Label(text="       ", width=30).grid(row=19, column=0)
	Button(text="delete Client",width=15 , command =  lambda: deletePosibleClient(index)).grid(row=20, column=0)
	Label(text="       ", width=30).grid(row=21, column=6)
	Label(text="       ", width=30).grid(row=22, column=6)
	Label(text="       ", width=30).grid(row=23, column=6)


# query handdler....
def goFindTheData():
	# using the load function from the class find the data on the jsonfile
	number = finder.get().strip()
	dataContainerReCall = load.data
	# if found something change this variable to True  === > itItsFound
	itItsFound = "false"

	# check for values
	if number == "":
		# if search bar empty,give back message 
		messagebox.showinfo('error','Give me something to find')
	else:
		for numberToCheckAllObjectsInsideArray in range(len(dataContainerReCall)):
			for x in dataContainerReCall[numberToCheckAllObjectsInsideArray]["Phone"]:
				if x != number:
					print("not a client phone Number")
					for Y in dataContainerReCall[numberToCheckAllObjectsInsideArray]["Landline"]:
						if Y == number:
							# make sure the found variable its oposite
							if itItsFound == "false":
								showDataFoundONtheSearch(dataContainerReCall[numberToCheckAllObjectsInsideArray],numberToCheckAllObjectsInsideArray)
								itItsFound = "true"
						else:
							print('Not a Lineline Number also...')
				elif x == number:
					# make sure the found variable its oposite
					if itItsFound == "false":
						showDataFoundONtheSearch(dataContainerReCall[numberToCheckAllObjectsInsideArray],numberToCheckAllObjectsInsideArray)
						itItsFound = "true"



Label(text="SEARCH", width=20).grid(row=12, column=0)

finder = Entry(text="find", width=30)
finder.grid(row=12, column=1)

Button(text="Get Client",width=15 , command = goFindTheData).grid(row=12, column=2)
Label(text="    ", width=30).grid(row=12, column=3)


# more space
Label(text="       ", width=30).grid(row=13, column=0)
Label(text="       ", width=30).grid(row=13, column=1)

root.mainloop()
