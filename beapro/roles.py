from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'ban_user':True,
        'read_complients':True,
        'add_blog':True,
        'ban_user':True,
        'verify_user':True,
        'view_wallet':True
    }

class Tutor(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'ban_user':True,
        'add_blog':True,
    }

class Student(AbstractUserRole):
    available_permissions = {
        'view_blog': True,
        'ban_user':True,
        'add_feedback':True
    }