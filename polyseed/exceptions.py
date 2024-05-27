class PolyseedLanguageException(Exception):
    pass

class PolyseedLanguageNotFoundException(Exception):
    pass

class PolyseedMultipleLanguagesException(PolyseedLanguageException):
    pass

class PolyseedDataFormatException(Exception):
    pass


class PolyseedFeatureUnsupported(Exception):
    pass

class PolyseedStringSizeExceededException(Exception):
    pass

class PolyseedWordCountMissmatchException(Exception):
    pass

class PolyseedChecksumException(Exception):
    pass
