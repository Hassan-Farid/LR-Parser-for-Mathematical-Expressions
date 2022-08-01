#ParseTable class provides a parsing table to use for validating input strings with grammar
class ParseTable:
    
    #ParseTable allocates values for its first column,
    #follow column and parse table datastructure
    def __init__(self):
        self.first = {}
        self.follow = {}
        self.parse_table = {}
        
    #ParseTable provides a method to view the contents of its first table
    def get_first_table(self):
        repr_str = "{:<8} {:<15} \n".format('Symbol','First Values')
        for symbol, first in self.first.items():
            repr_str += "{:<8} {:<15} \n".format(symbol, str(first))
        return "{}".format(repr_str)
        
    #ParseTable provides a method to view the contents of its follow table
    def get_follow_table(self):
        repr_str = "{:<8} {:<15} \n".format('Symbol','Follow Values')
        for symbol, follow in self.follow.items():
            repr_str += "{:<8} {:<15} \n".format(symbol, str(follow))
        return "{}".format(repr_str)    
        
    #ParseTable provides a method to add a record to the first table
    def add_first_record(self, key, first_values):
        self.first[key] = first_values
        
    #ParseTable provides a method to add a record to the follow table
    def add_follow_record(self, key, follow_values):
        self.follow[key] = follow_values
        
    #ParseTable provides a method to generate a parse table
    #using first and follow tables
    def generate_parse_table(self):
        #Iterate over all keys in first table and add its and
        #follows value to corresponding key in parse table
        for key in self.first.keys():
            self.parse_table[key] = {'first': self.first[key],
                                     'follow': self.follow[key]}
            
    #ParseTable provides a method to check if 
    #provided character is in someone's follow table
    def check_char_in_follow(self, char):
        #Iterate over key and values in follow table
        for key, val in self.follow.items():
            #If character matches some value in the 
            #values return the corresponding key
            if char in val:
                return key
        #Otherwise return -1
        return -1

    #ParseTable provides a method to check if provided 
    #character is in provided key's first table
    def check_char_in_first(self, char, key):
        #If character matches some value in the 
        #values of the key return True
        if char in self.first[key]:
            return True
        #Otherwise return False
        return False

    #ParseTable provides a method to ensure that
    #the given string satisfies the grammar
    #This is done with the help of first and follow tables       
    def check_string(self, string):
        #Set the cursor value for string to 0
        cursor = 0
        
        #If the string is empty, then display error 
        #as no string was provided
        if len(string) == 0:
            raise SyntaxError("Didn't get any inputted string")
        
        #If the string's first character is not present in 
        #the first value for starting symbol 'S'
        #Then the string cannot possibly be generated 
        #via the grammar giving syntax error
        if string[cursor] not in self.first['S']:
            raise SyntaxError('Incorrect string provided')
        
        #If the string's first character matches and 
        #its the only character in the string
        #Its obvious the string gets accepted
        if len(string) == 1:
            return True
        
        #Iterating till we complete the total string
        while (cursor < len(string)):
            #Try in case the cursor value points to any 
            #position other than the last one
            try:
                #Check the symbol whose follow table contains
                #the next character of string
                follow_key = self.check_char_in_follow(string[cursor+1])
                #If there is no such symbol then a -1 is resulted 
                #as output which means Syntax Error
                if follow_key == -1:
                    raise SyntaxError("Incorrect syntax")
            #In case the cursor points to the last character 
            #and no syntax error was reported
            #The string gets accepted via the grammar provided
            except:
                #Since all of the strings have been processed
                return True
            #If the current string value is not in 
            #the first table of the follow key
            #Then the string cannot be generated as it also 
            #has to be one of the possible first values
            #that can be generated by the key whose 
            #follow contains its next character
            if self.check_char_in_first(string[cursor], follow_key) == False:
                raise SyntaxError("Incorrect syntax")
            #Otherwise we skip the next character 
            #as it has already been verified
            else:
                cursor += 1
            
            #Increment the cursor value for the loop    
            cursor += 1

    #ParseTable also provides a method to display the contents of its parse table
    def __repr__(self):
        repr_str = "{:<8} {:<15} {:<50}\n".format('Symbol','Follow Values', 'First Values')
        for symbol, tables in self.parse_table.items():
            repr_str += "{:<8} {:<15} {:<15}\n".format(symbol, str(tables['follow']), str(tables['first']))
        return "{}".format(repr_str)
    