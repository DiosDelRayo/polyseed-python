from .constants import (
    POLYSEED_LANG_SIZE,
    POLYSEED_NUM_WORDS,
    NUM_CHARS_PREFIX
)
from .exceptions import (
    PolyseedLanguageException,
    PolyseedMultipleLanguagesException,
    PolyseedLanguageNotFoundException
)

from typing import List, Dict, Tuple
from unicodedata import normalize

class Language:

    code: str
    name: str
    name_en: str
    separator: str
    is_sorted: bool
    has_prefix: bool
    has_accents: bool
    compose: bool
    words: List[str]

    languages: Dict = {}

    @classmethod
    def register(cls) -> None:
        cls.languages[cls.code] = cls

    @classmethod
    def get_lang_by_code(cls, code: str) -> 'Language':
        if code not in cls.languages:
            raise PolyseedLanguageNotFoundException()
        return cls.languages[code]

    @classmethod
    def get_lang_by_name_en(cls, name: str) -> 'Language':
        for lang in cls.languages.values():
            if lang.name_en == name:
                return lang
        raise PolyseedLanguageNotFoundException()

    @classmethod
    def get_lang_count(cls) -> int:
        return len(cls.languages)

    @classmethod
    def get_lang(cls, i: int) -> 'Language':
        if 0 < i or i > cls.get_lang_count():
            raise PolyseedLanguageNotFoundException()
        return cls.get_lang_by_code(list(cls.languages.keys())[i])

    @classmethod
    def search(cls, word: str, cmp) -> int:
        if cls.is_sorted:
            try:
                return cls.words.index(word)
            except ValueError:
                return -1
        for i, w in enumerate(cls.words):
            if word == w:
                return i
        return -1

    @staticmethod
    def compare_str(key: str, elm):
        for i, (k, e) in enumerate(zip(key, elm)):
            if k == "\0" or k != e:
                break
        else:
            i += 1
        return (ord(key[i:]) > ord(elm[i:])) - (ord(key[i:]) < ord(elm[i:]))


    @staticmethod
    def compare_str_wrap(key, elm):
        return compare_str(key, elm)


    @staticmethod
    def compare_prefix(key, elm, n):
        for i in range(1, n + 2):
            if i == n + 1 and key[i:] == "\0":
                break
            if i > len(key) or i > len(elm) or key[i - 1] != elm[i - 1]:
                break
        return (ord(key[i:]) > ord(elm[i:])) - (ord(key[i:]) < ord(elm[i:]))

    @staticmethod
    def compare_prefix_wrap(key, elm):
        return compare_prefix(key, elm, NUM_CHARS_PREFIX)

    @staticmethod
    def compare_str_noaccent(key, elm):
        key = "".join(c for c in key if ord(c) < 128)
        elm = "".join(c for c in elm if ord(c) < 128)
        return compare_str(key, elm)

    @staticmethod
    def compare_str_noaccent_wrap(key, elm):
        return compare_str_noaccent(key, elm)

    @staticmethod
    def compare_prefix_noaccent(key, elm, n):
        key = "".join(c for c in key if ord(c) < 128)
        elm = "".join(c for c in elm if ord(c) < 128)
        return compare_prefix(key, elm, n)

    @staticmethod
    def compare_prefix_noaccent_wrap(key, elm):
        return compare_prefix_noaccent(key, elm, NUM_CHARS_PREFIX)

    @classmethod
    def get_comparer(cls):
        if cls.has_prefix:
            if cls.has_accents:
                return cls.compare_prefix_noaccent_wrap
            else:
                return cls.compare_prefix_wrap
        if cls.has_accents:
            return cls.compare_str_noaccent_wrap
        else:
            return cls.compare_str_wrap

    @classmethod
    def find_word(cls, word: str) -> int:
        cmp = cls.get_comparer()
        return cls.search(word, cmp)

    @classmethod
    def phrase_encode(cls, data: List[int]) -> str:
        return cls.separator.join([cls.words[i] for i in data])

    @classmethod
    def phrase_decode(cls, phrase: List[str]) -> Tuple[List[int], 'Language']:
        out: List[int] = [0] * POLYSEED_NUM_WORDS
        have_lang = False
        for lang in cls.languages.values():
            cmp = lang.get_comparer()
            success = True
            for wi, word in enumerate(phrase):
                value = lang.search(word, cmp)
                # value = lang.words.index(word)
                if value < 0:
                    success = False
                    break
                out[wi] = value
            if not success:
                continue
            if have_lang:
                raise PolyseedMultipleLanguagesException()
            have_lang = True
        if not have_lang:
            raise PolyseedLanguageException()
        return out, lang

    @classmethod
    def phrase_decode_explicit(cls, phrase: str) -> List[int]:
        out: List[int] = []
        cmp = cls.get_comparer()
        for wi, word in enumerate(phrase):
            value = cls.search(word, cmp)
            if value < 0:
                raise PolyseedLanguageException()
            out.append(value)
        return out


    @classmethod
    def check(cls):
        # check the language is sorted correctly
        if cls.is_sorted:
            cmp = cls.get_comparer()
            prev = cls.words
            for word in cls.words[1:]:
                assert cmp(prev, word) < 0, "incorrectly sorted wordlist"
                prev = word

        # all words must be in NFKD
        for word in cls.words:
            norm = normalize("NFKD", word)
            assert word == norm, "incorrectly normalized wordlist"

        # accented languages must be composed
        assert not cls.has_accents or cls.compose

        # normalized separator must be a space
        separator = normalize("NFKD", cls.separator)
        assert separator == " "

from .lang_en import LanguageEnglish
# Import language data from other files
from .lang_jp import LanguageJapanese
from .lang_ko import LanguageKorean
from .lang_es import LanguageSpanish
from .lang_zh_s import LanguageChineseSimplified
from .lang_zh_t import LanguageChineseTraditional
from .lang_fr import LanguageFrench
from .lang_it import LanguageItalian
from .lang_cs import LanguageCzech
from .lang_pt import LanguagePortuguese
