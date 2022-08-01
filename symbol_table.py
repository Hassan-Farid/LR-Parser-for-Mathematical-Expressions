#SymbolTable class to generate symbol table for a Lexer and Parser to use
class SymbolTable:
    
    #SymbolTable uses a dictionary to store its contents
    def __init__(self):
        self.table = {}
        
    #SymbolTable provides a method to add a symbol
    #and its respective type to the table
    def add_symbol(self, symbol, symbol_type):
        self.table[symbol] = symbol_type
        
    #SymbolTable provides a method to display the contents of its table
    def __repr__(self):
        repr_str = "{:<8} {:<15} \n".format('Value','Type')
        for val, type in self.table.items():
            repr_str += "{:<8} {:<15} \n".format(val, type)
        return "{}".format(repr_str)
    