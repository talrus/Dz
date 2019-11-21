'''
Your collegue wrote an simple loop to list his favourite animals. 
But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)

If you pass the list of your favourite animals to the function, you should get the list of the animals with orderings and newlines added.
'''
def list_animals(animals):
    string_of_animals = ''
    for i, value in enumerate(animals, 1):
        string_of_animals += str(i) + '. ' + value + '\n'
    return string_of_animals
	