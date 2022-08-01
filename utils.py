#File containing utility functions for program

#Method to parse grammar from its file
def parse_grammar(filename):
    #Extract data line by line from file
    with open(filename, 'r') as file:
        data = file.readlines()
    
    #Create a grammar dict to store the grammar results
    grammar = {}
    #Iterate over different lines in data
    for line in data:
        #Remove endlines
        line = line.rstrip('\n')
        #Seperate symbol and its productions
        symbol, prod = line.split(' -> ')
        #Enter the list of productions as value
        #for symbol key for grammar
        grammar[symbol] = prod.split(' | ')
        
    #Return the parsed grammar
    return grammar

#Method to parse operators and their precedence from its file
def parse_operators(filename):
    #Extract data line by line from file
    with open(filename, 'r') as file:
        data = file.readlines()
    
    #Create a operator dict to store the operators
    #and their corresponding precedence    
    ops = {}
    #Iterate over different lines in data
    for line in data:
        #Remove endlines
        line = line.rstrip('\n')
        #Seperate operator from its precedence value
        op, pred = line.split(' : ')
        #Enter the numeric precedence as value for symbol key for grammar
        ops[op] = int(pred)
        
    #Return the operators dictionary as output
    return ops

#Method to parse the input strings from its file
def parse_inputs(filename):
    #Extract data line by line from file
    with open(filename, 'r') as file:
        data = file.readlines()
        
    #Generate a list of strings
    strings = []
    #Iterate over each line in data
    for line in data:
        #Remove endlines
        line = line.rstrip('\n')
        #Add the string inputs to the string list
        strings.append(line.strip())
    
    #Return the list of strings
    return strings