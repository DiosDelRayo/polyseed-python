class PolyseedLanguageException(Exception):
    pass

class PolyseedMultipleLanguagesException(PolyseedLanguageException):
    pass

class PolyseedDataFormatException(Exception):
    pass


class PolyseedFeatureUnsupported(Exception):
    pass
