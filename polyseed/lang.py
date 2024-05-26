from unicodedata import normalize

POLYSEED_LANG_SIZE = 2048
POLYSEED_NUM_WORDS = 24
NUM_CHARS_PREFIX = 4

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

languages = [
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

NUM_LANGS = len(languages)


def polyseed_get_num_langs():
    return NUM_LANGS


def polyseed_get_lang(i: int):
    assert 0 <= i < NUM_LANGS
    return languages[i]


def polyseed_get_lang_name(lang: str):
    assert lang is not None
    return lang["name"]


def polyseed_get_lang_name_en(lang):
    assert lang is not None
    return lang["name_en"]


def lang_search(lang, word, cmp):
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


def compare_str(key, elm):
    for i, (k, e) in enumerate(zip(key, elm)):
        if k == "\0" or k != e:
            break
    else:
        i += 1
    return (ord(key[i:]) > ord(elm[i:])) - (ord(key[i:]) < ord(elm[i:]))


def compare_str_wrap(a, b):
    key, elm = a, b
    return compare_str(key, elm)


def compare_prefix(key, elm, n):
    for i in range(1, n + 2):
        if i == n + 1 and key[i:] == "\0":
            break
        if i > len(key) or i > len(elm) or key[i - 1] != elm[i - 1]:
            break
    return (ord(key[i:]) > ord(elm[i:])) - (ord(key[i:]) < ord(elm[i:]))


def compare_prefix_wrap(a, b):
    key, elm = a, b
    return compare_prefix(key, elm, NUM_CHARS_PREFIX)


def compare_str_noaccent(key, elm):
    key = "".join(c for c in key if ord(c) < 128)
    elm = "".join(c for c in elm if ord(c) < 128)
    return compare_str(key, elm)


def compare_str_noaccent_wrap(a, b):
    key, elm = a, b
    return compare_str_noaccent(key, elm)


def compare_prefix_noaccent(key, elm, n):
    key = "".join(c for c in key if ord(c) < 128)
    elm = "".join(c for c in elm if ord(c) < 128)
    return compare_prefix(key, elm, n)


def compare_prefix_noaccent_wrap(a, b):
    key, elm = a, b
    return compare_prefix_noaccent(key, elm, NUM_CHARS_PREFIX)


def get_comparer(lang):
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


def polyseed_lang_find_word(lang, word: str):
    cmp = get_comparer(lang)
    return lang_search(lang, word, cmp)


def polyseed_phrase_decode(phrase, lang_out=None):
    idx_out = [0] * POLYSEED_NUM_WORDS
    have_lang = False
    for lang in languages:
        cmp = get_comparer(lang)
        success = True
        for wi, word in enumerate(phrase):
            value = lang_search(lang, word, cmp)
            if value < 0:
                success = False
                break
            idx_out[wi] = value
        if not success:
            continue
        if have_lang:
            return "POLYSEED_ERR_MULT_LANG", None
        have_lang = True
        if lang_out is not None:
            lang_out[:] = [lang]
    if have_lang:
        return "POLYSEED_OK", idx_out
    else:
        return "POLYSEED_ERR_LANG", None


def polyseed_phrase_decode_explicit(phrase, lang, idx_out):
    cmp = get_comparer(lang)
    for wi, word in enumerate(phrase):
        value = lang_search(lang, word, cmp)
        if value < 0:
            return "POLYSEED_ERR_LANG"
        idx_out[wi] = value
    return "POLYSEED_OK"


def polyseed_lang_check(lang):
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
