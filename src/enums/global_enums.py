from enum import Enum

class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = 'Status differs from expected status.'
    WRONG_ELEMENT_COUNT = 'Length differs from expected Length'
    WRONG_NUMBER = 'Number differs from expected number'