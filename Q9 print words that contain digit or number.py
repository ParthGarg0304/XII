"""A text file contains alphanumeric text (poem.txt). Write a program that reads
this text file and prints only those words that contain digit / number from the
file."""

#A Text file poem.txt was created explicitly

f= open("poem.txt","r")
for line in f:
  words =line.split()
  for i in words:
      for letter in i :
          if(letter.isdigit()):
              print(i)
              break

f.close()
