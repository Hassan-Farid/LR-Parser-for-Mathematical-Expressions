#Importing parsing table datastructure
from parsing_table import ParseTable
#Importing Lexer class to generate a lexer instance for the parser
from lexer import Lexer
#Importing Node class to store the results of parse tree as a set of nodes
from tree_node import Node

#Parser class to create a parse for parsing a provided string
class Parser:
    
    #A parser takes into account certain parameters
    def __init__(self, string, operators, grammar):
        #Initializes the string value to parse
        self.string = string 
         #Uses the token information to generate a lexer for parser
        self.lexer = Lexer(self.string, operators)
        #Initializes the grammar that string must follow
        self.grammar = grammar 
        #Initializes a parsing table to ensure string follows grammar
        self.parse_table = ParseTable()
        #Initializes a memo dictionary to cache results for 
        #first values if need arises 
        self.memo = {} 
        #Initializes a list to store all the possible 
        #productions of the grammar
        self.productions = [] 
        #Initializes the order of precedence to be 
        #followed by the operators during parsing
        self.precendence = operators
        
    #Parser provides a method to return its parsing table
    def get_parse_table(self):
        #Adds the first table to parse table
        self.add_first_table()
        #Adds the follow table to parse table
        self.add_follow_table()
        #Generates the parsing table for the parser using first and follow tables
        self.parse_table.generate_parse_table()
        return self.parse_table
    
    #Parser provides a method to check if the string follows the given grammar via its parsing table
    def check_string(self):
        return self.parse_table.check_string(self.string)
    
    #Parser provides a method to generate the postfix
    #string for parse tree generation
    def get_postfix(self, tokens):
        stack = [] #Stack datastructure to keep track of the characters
        postfix = [] #Postfix list to contain the strings in a postfix order
        
        #Iterate over all the tokens in the generated tokens list
        for token in tokens:
            # If the token is an operand, then do not push it to stack. 
            # Instead, pass it to the output.
            if token.isalnum():
                postfix.append(token)

            # Before you can push the operator onto the stack, 
            # you have to pop the stack until you find an operator
            # with a lower priority than the current operator.
            # The popped stack elements are written to output.
            else:
                while stack and (self.precendence[stack[-1]] 
                                 >= self.precendence[token]):
                    postfix.append(stack.pop())
                stack.append(token)

        # After the entire expression is scanned, 
        # pop the rest of the stack 
        # and write the operators in the stack to the output.
        while stack:
            postfix.append(stack.pop())
            
        #Return the generated postfix string value as result
        return postfix

    #Parser provides a method to generate a parse tree 
    #from the provided string if it follows grammar
    def generate_parse_tree(self):
        #Generate the tree if and only if the given 
        #string verifies the grammar
        if self.check_string():
            #Generate list of tokens to utilize
            tokens = self.lexer.tokenize()
            #Create postfix string from generated tokens
            postfix_string = self.get_postfix(tokens)
            #Creating stack to generate the tree
            stack = []
            #Iterate over each token in generated postfix string
            for token in postfix_string:
                #In case token is a space, leave it be
                if token == ' ':
                    continue
                
                #Check if the token is a operator
                if token in self.precendence.keys():
                    #If yes then select the last two elements from stack 
                    sec, first = stack.pop(), stack.pop()
                    #Generate a Node using the values with operator
                    #being root and values being children
                    stack.append(Node(token, sec, first))
                else:
                    #If no, then simply add the token to the stack
                    stack.append(token)
                
        #Return the first item of the stack which will
        #contain the parse tree for the expression
        return stack[0]
    
    #Parser provides a method to view contents of the first table
    def get_first_table(self):
        return self.parse_table.get_first_table()

    #Parser provides a method to add a first table to its parsing table
    def add_first_table(self):
        #The method iterates over all the non-terminals on left-side of grammar
        #Uses these to add corresponding first values to its parsing table
        for key in self.grammar.keys():
            self.parse_table.add_first_record(key, self.get_first(key))
    
    #Parser provides a method to generate the first values
    #for a specific key in the grammar
    def get_first(self, key):
        #Initialize a list to return as the list of first values
        first = []
        #Generate the rule using given grammar and key
        rule = self.grammar[key]
        #Result value to compute the corresponding first values
        #per each production
        result = []
        #Check if the first for the symbol has already been calculated
        if key in self.memo.keys():
            return self.memo[key]
        
        #For each production in the rule loop
        for prod in rule:
            #For each symbol in the production loop
            for symbol in prod:
                #If the symbol is a non-terminal then call the first method 
                #on that symbol to get its first values
                if symbol.isupper():
                    #Compute first values for the symbol
                    res = self.get_first(symbol)
                    #Cache the results in a memo object 
                    self.memo[symbol] = res
                    #Add the obtained result 
                    result.extend(res) 
                    break
                else: 
                    #If symbol is terminal then add it to the result
                    # and terminate loop for first
                    result.append(symbol) 
                    break
            #Add only those values to the first list which are not already added
            first.extend(sorted(list(
                set(first).symmetric_difference(set(result)))))
            
        self.memo[key] = first #Cache obtained first values to memo object
        return sorted(list(set(first))) #Return the first list
    
    #Parser provides a method to view contents of the follow table
    def get_follow_table(self):
        return self.parse_table.get_follow_table()
    
    #Parser provides a method to compute all productions 
    #that are generated by the grammar
    def get_all_productions(self):
        #Iterates over for each rule in the grammar
        for rule in self.grammar.values():
            #Adds the production from each rule into
            #the productions list
            for prod in rule:
                self.productions.append(prod)
    
    #Parser provides a method to add a follow table to its parsing table
    def add_follow_table(self):
        #Generate a set of all possible productions of the grammar
        self.get_all_productions()
        #The method iterates over all the non-terminals on left-side of grammar
        #Uses these to add corresponding follow values to its parsing table
        for key in self.grammar.keys():
            self.parse_table.add_follow_record(key, self.get_follow(key))
    
    #Parser provides a method to determine the follow values for a key
    def get_follow(self, key):
        #Generate a list to store the follow values
        follow = []
        #Iterate over each production in the productions list
        for prod in self.productions:
            #Loop over the length of each production
            for i in range(len(prod)):
                #Check if the current value is the key for
                #which follow values are required
                if prod[i] == key:
                    #Try if its not the last item in the production selected
                    try:
                        #Check the next symbol in the production
                        next_symbol = prod[i+1]
                        #If the next symbol is a non-terminal
                        if next_symbol.isupper():
                            #Get the first value of that non-terminal 
                            #via the cached results in memo dictionary
                            next_first = self.memo[next_symbol]
                            #Add only unique members from the first list
                            #into follow list
                            follow.extend(list(
                                set(follow).symmetric_difference(set(next_first))
                                ))
                        else:
                            #If the next symbol is a terminal,
                            #simply add it to follow list
                            follow.append(next_symbol)
                    except:
                        #In case there is no more values left in production,
                        #add a '$' symbol to the list
                        follow.append("$")
        #Return a sorted list of only unique values from follow list
        return sorted(list(set(follow)))