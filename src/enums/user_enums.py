from enum import Enum


class Gender(Enum):
    female = 'female'
    male = 'male'


class Status(Enum):
    active = 'active'
    inactive = 'inactive'


class UserError(Enum):
    WRONG_EMAIL = 'Email doesn`t contain @'