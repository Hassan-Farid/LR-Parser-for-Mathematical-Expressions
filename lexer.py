#Importing symbol table datastructure
from symbol_table import SymbolTable

#Lexer class to tokenize a provided string into a set of tokens 
class Lexer:
    
    # Lexer takes into account a string to generate tokens from it
    def __init__(self, string, operators):
        #String to use for tokenization
        self.string = string 
        #Symbol table to store token information
        self.symbol_table = SymbolTable() 
        #List containing only the operator symbols
        self.operators = list(operators.keys())
        #Tokens to generate as output from string 
        self.tokens = [] 
        
    # Lexer can generate tokens from the provided string 
    def tokenize(self):
        #Current token extracted
        curr_token = ''
        #Cursor value to keep track of string completion  
        cursor = 0 
        #Default token type set to 'INTEGER'
        token_type = 'INTEGER' 
        
        #If the string is empty, then return an empty list
        if len(self.string) == 0:
            return []
        
        #For each character in string till its completion
        while (cursor < len(self.string)):
            # If the type of character matches that of an identifier
            # i.e. has a alphabet in it
            if (self.string[cursor].isalpha()):
                #Add the character to current token value
                #and set type to 'IDENTIFIER'
                curr_token += self.string[cursor]
                token_type = 'IDENTIFIER'
                
            #If the type of character matches that of a digit
            #i.e. has a number in it 
            elif (self.string[cursor].isdigit()):
                #Add the character to current token
                curr_token += self.string[cursor] 
                
            #If the type of character matches that of an operator 
            elif self.string[cursor] in self.operators:
                #Add the current token into the generated tokens list
                self.tokens.append(curr_token)
                #Add the current token and its type to 
                #the symbol table for future use
                self.symbol_table.add_symbol(curr_token, token_type)
                #Add the operator value to the generated tokens list
                self.tokens.append(self.string[cursor])
                #Add the type of operator and operator value to symbol table
                self.symbol_table.add_symbol(self.string[cursor], 'OPERATOR')
                #Reset the value of current token and token type
                curr_token = ''
                token_type = 'INTEGER'
                
            else:
                #In case the string contains some other character,
                #the lexer ignores it
                #We add the current token to the token generated list
                self.tokens.append(curr_token)
                #Add the token value and its type to the symbol table
                self.symbol_table.add_symbol(curr_token, token_type)
                #Reset value for current token and token type
                curr_token = ''
                token_type = 'INTEGER'
                
            #Increment the cursor value to point to the next character    
            cursor += 1
            
        #In case the cursor has reached the end, 
        #we add whatever remaining value of token to tokens list
        self.tokens.append(curr_token)
        #Add the last token into symbol table along with its type
        self.symbol_table.add_symbol(curr_token, token_type)
        #Return filtered version of the tokens 
        #i.e. without the spaces 
        return self.filter_tokens()
        
    # Lexer provides a method to remove spaces
    # from list of generated tokens
    def filter_tokens(self):
        return [token for token in self.tokens if token != '']
    
    # Lexer provides a method to provide the 
    # contents of its symbol table
    def get_symbol_table(self):
        return self.symbol_table
    
    # Lexer provides a method to represent its generated 
    # tokens list when called with print function
    def __repr__(self):
        return "Tokens generated: {}".format(self.tokens)
    
    

    
    