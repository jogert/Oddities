#### personal work ####
#src@https://developers.google.com/edu/python/regular-expressions
import re


## prompt inputs
word = str(raw_input("<'?' is a wildchar> Word to find: "))
input_file = str(raw_input("<inside pwd> File to search: "))

## convert to wildcard character 
wd_edit = word.replace('?', '\w')
#print wd_edit

## read file
fo = open(input_file, "r")
text = str(fo.read())
fo.close()

## find matches accounting for wildchar
matches = re.findall(wd_edit, text)
if matches:
	print matches
print "I've been hit by like", len(matches), "cars"
print "\t\tyawhhhh.. <drunk deers>"
