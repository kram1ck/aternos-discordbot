"""Custom Exception Classes"""

class NoAnyRoleAttribute(Exception):
    """Raise Exception if there is no discord ROLE_ID and ROLE_NAME"""
    def __str__(self):
        return "ROLE_ID and ROLE_NAME was not found in configs.txt"
    

class NoAnyTokenFound(Exception):
    """Raise Exception if there is no token in environment variables or in configs.txt"""
    def __str__(self):
        return "Bot token was not found in configs.txt or in environment variables"