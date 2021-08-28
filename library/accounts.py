"""this module will manage the accounts information, librarian or member"""

from enum import Enum

class IdStatus(Enum):
    none, active, blocked, blacklisted, cancelled = 0, 1, 2, 3, 4,


class Account:
    """General account
    Librarian and member will be inherited
    """
    def __init__(self, name, email, phone, id_status):
        self.name = name
        self.email = email
        self.phone = phone
        self.id_status = id_status
        self.id = None
        self.password = None


class Librarian(Account):
    """this class will store the librarian data"""
    def __int__(self, name, email, phone, admin_id, id_status=IdStatus.active):
        super().__init__(name, email, phone, id_status)
        self.id = admin_id


class MemberAccount(Account):
    def __init__(self, name, email, phone, member_id, id_status=IdStatus.active):
        super().__init__(name, email, phone, id_status)
        self.id = member_id
        self.books_issued = []



