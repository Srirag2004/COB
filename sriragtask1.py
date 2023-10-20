#phase 1 task 1 srirag

def countUniqueWords(fileName):

	file = open(fileName, 'r')

	read_file = file.read().lower()
	words_in_file = read_file.split()

	count_map = {}
	for i in words_in_file:
		if i in count_map:
			count_map[i] += 1
		else:
			count_map[i] = 1
	count = 0

	for i in count_map:
		if count_map[i] == 1:
			count += 1
	file.close()
	return count



with open("srirag.txt", "w") as file:
	file.write("Most streets are two-way streets...why does that make love so special?\
	Curling is the best sport named after something you do to your hair \
	Pantone is a colour but also the singular version of pants\
	for selected questions")

print('Number of unique words in the file are:',
	countUniqueWords('srirag.txt'))
