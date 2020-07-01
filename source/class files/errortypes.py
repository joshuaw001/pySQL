import sqlite3
class PYSQLError:
    def __init__(self):
        #self.ERROR_ID = 0 #deal with this later
        self.ERROR_TEXT = f"{self.__name__}: Error type can't be specified at this time."
        #insert the database insert
        #code for errors.db here...

class VariableNotActiveError(PYSQLError):
    def __init__(self,varname):
        super().__init__()
        self.ERROR_TEXT = f"{self.__name__}: the variable definition {varname} is in an inactive state. re-activation is required for further use of {varname}."
        self.varname = varname
class VariableWithIncorrectTypeError(PYSQLError):
    pass

class VariableWithNoVariableError(PYSQLError):
    pass

class WrongSyntaxFromInputError(PYSQLError):
    pass

class StringQuoteMismatchedError(PYSQLError):
    pass

class UnsignedNumberHasNegativeValueError(PYSQLError):
    pass

class AttemptedBuiltinVariableDeletionError(PYSQLError):
    pass

class NothingInputtedError(PYSQLError):
    pass

#ended file... for now!!!!!
