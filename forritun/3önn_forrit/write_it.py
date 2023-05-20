# shows how to write a text file

print "create a text file with writelines() method"
text_file = open("write_it.txt", "w"
Lines = ["Line1\n",
        "This is line 2\n",
        "And this makes this line 3\n"]
text_file.writelines(lines)
text_file.close()
                 
text_file = open("write_it.txt", "r")
print text_file.read()
text_file.close()
                 



 
