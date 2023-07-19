"""Custom Exception Classes"""

class NoAnyRoleAttribute(Exception):
    """Raise Exception if there is no discord ROLE_ID and ROLE_NAME"""
    def __str__(self):
        return "ROLE_ID and ROLE_NAME was not found in configs.txt"