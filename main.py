from math_parser import Parser
from utils import *

def main():
    #Parse the required grammar, operators and strings from their files
    grammar = parse_grammar('./inputfiles/grammar.txt')
    operators = parse_operators('./inputfiles/operators.txt')
    strings = parse_inputs('./inputfiles/strings.txt')
    
    #Counter variable for naming output files for strings
    counter = 1
    
    #Iterate over each string in the inputted strings
    for string in strings:
        #Create a parser with the provided parameters for each string
        parser = Parser(string, operators, grammar)
        #Generate a parse table for each string
        parser.get_parse_table()
        #Generate a parse tree for each string and
        #store it into corresponding json
        with open('./outputfiles/expr{}.json'.format(counter), 'w') as file:
            parse_tree = parser.generate_parse_tree()
            file.write(parse_tree.to_json())
        #Increment the counter
        counter += 1
        
if __name__ == "__main__":
    main()
    
    