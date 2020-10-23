import glob
import os
import socket


hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)


os.getcwd()


results = open("Results.txt", "w")




myFiles = glob.glob('*.txt')
count = 0
largestfilesize = 0
largestfilename = ''
results.write("Text files in current directory = ")
for i in myFiles:
    results.write(i + " ")
    
for x in myFiles:
    
    #get number of words in a file
    file = open(x, "rt")
    data = file.read()
    words = data.split()
    results.write(" \n Total word count for " + x + " = %d \n " %  len(words))
    #count total number of words in all files together
    count = count + len(words)
    #find file with largest amount of words
    if len(words) > largestfilesize:
        largestfilesize = len(words)
        largestfilename = x

    
results.write(" \n Total word count of all text files = %d \n" % count)
results.write(" \n Largest text file = " + largestfilename + "\n" )
results.write(" \n Your Computer name = " + hostname + " \n" )
results.write(" \n Your IPAddr = " + IPAddr + " \n" )
results.close()
read = open("Results.txt", "r")
print(read.read())
