from .constants import (
    POLYSEED_LANG_SIZE,
    POLYSEED_NUM_WORDS,
    NUM_CHARS_PREFIX
)
from .exceptions import (
    PolyseedLanguageException,
    PolyseedMultipleLanguagesException
)

from typing import List, Dict
from unicodedata import normalize


# Import language data from other files
from .lang_en import polyseed_lang_en
# from lang_jp import polyseed_lang_jp
# from lang_ko import polyseed_lang_ko
# from lang_es import polyseed_lang_es
# from lang_zh_s import polyseed_zh_s
# from lang_zh_t import polyseed_zh_t
# from lang_fr import polyseed_lang_fr
# from lang_it import polyseed_lang_it
# from lang_cs import polyseed_lang_cs
# from lang_pt import polyseed_lang_pt

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

    languages: List = [
        # sorted wordlists first
        # https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md
        polyseed_lang_en,
        # polyseed_lang_jp,
        # polyseed_lang_ko,
        # polyseed_lang_es,
        # polyseed_lang_fr,
        # polyseed_lang_it,
        # polyseed_lang_cs,
        # polyseed_lang_pt,
        # polyseed_zh_s,
        # polyseed_zh_t,
    ]

    @classmethod
    def get_num_langs(cls) -> int:
        return len(cls.languages)

    @classmethod
    def polyseed_get_lang(i: int) -> Dict:
        assert 0 <= i < cls.get_num_langs()
        return languages[i]

    @staticmethod
    def get_lang_name(lang: Dict) -> str:
        return lang["name"]

    @staticmethod
    def get_lang_name_en(lang: Dict) -> str:
        return lang["name_en"]

    @staticmethod
    def lang_search(lang: Dict, word: str, cmp) -> int:
        if lang["is_sorted"]:
            try:
                idx = lang["words"].index(word)
                return idx
            except ValueError:
                return -1
        else:
            for i, w in enumerate(lang["words"]):
                if cmp(word, w) == 0:
                    return i
            return -1

    @staticmethod
    def compare_str(key: str, elm):  # TODO: ?
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
        key, elm = a, b
        return compare_str_noaccent(key, elm)

    @staticmethod
    def compare_prefix_noaccent(key, elm, n):
        key = "".join(c for c in key if ord(c) < 128)
        elm = "".join(c for c in elm if ord(c) < 128)
        return compare_prefix(key, elm, n)

    @staticmethod
    def compare_prefix_noaccent_wrap(key, elm):
        return compare_prefix_noaccent(key, elm, NUM_CHARS_PREFIX)

    @staticmethod
    def get_comparer(lang: Dict):
        if lang["has_prefix"]:
            if lang["has_accents"]:
                return compare_prefix_noaccent_wrap
            else:
                return compare_prefix_wrap
        else:
            if lang["has_accents"]:
                return compare_str_noaccent_wrap
            else:
                return compare_str_wrap

    @staticmethod
    def polyseed_lang_find_word(lang: Dict, word: str):
        cmp = get_comparer(lang)
        return lang_search(lang, word, cmp)

    @staticmethod
    def phrase_decode(phrase: str, lang_out=None) -> List[int]:
        out: List[int] = [0] * POLYSEED_NUM_WORDS
        have_lang = False
        for lang in languages:
            cmp = get_comparer(lang)
            success = True
            for wi, word in enumerate(phrase):
                value = lang_search(lang, word, cmp)
                if value < 0:
                    success = False
                    break
                out[wi] = value
            if not success:
                continue
            if have_lang:
                raise PolyseedMultipleLanguagesException()
            have_lang = True
            if lang_out is not None:
                lang_out[:] = [lang]
        if not have_lang:
            raise PolyseedLanguageException()
        return out

    @staticmethod
    def phrase_decode_explicit(phrase: str, lang: Dict) -> List[int]:
        out: List[int] = []
        cmp = get_comparer(lang)
        for wi, word in enumerate(phrase):
            value = lang_search(lang, word, cmp)
            if value < 0:
                raise PolyseedLanguageException()
            out.append(value)
        return out


    @staticmethod
    def polyseed_lang_check(lang: Dict):
        # check the language is sorted correctly
        if lang["is_sorted"]:
            cmp = get_comparer(lang)
            prev = lang["words"][0]
            for word in lang["words"][1:]:
                assert cmp(prev, word) < 0, "incorrectly sorted wordlist"
                prev = word

        # all words must be in NFKD
        for word in lang["words"]:
            norm = normalize("NFKD", word)
            assert word == norm, "incorrectly normalized wordlist"

        # accented languages must be composed
        assert not lang["has_accents"] or lang["compose"]

        # normalized separator must be a space
        separator = normalize("NFKD", lang["separator"])
        assert separator == " "
