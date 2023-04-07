#Python program to count the frequency of words in a file.

text = open("program 1.txt", "r")  # Open the file in read mode
d = dict()    # Create an empty dictionary

# Loop through each line of the file
for line in text:
	
	line = line.strip()# Remove the leading spaces and newline character

	
	line = line.lower()# Convert the characters in line to
                           # lowercase to avoid case mismatch
                           
	words = line.split(" ")# Split the line into words
						

	# Iterate over each word in line
	for word in words:
		# Check if the word is already in dictionary
		if word in d:
			# Increment count of word by 1
			d[word] = d[word] + 1
		else:
			# Add the word to dictionary with count 1
			d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
	print(key, ":", d[key])
