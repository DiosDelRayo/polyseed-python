from typing import Union, Dict
from pathlib import Path
from hashlib import sha256
from lzma import compress as lzma
from base64 import b85encode
from re import search

WORD_PATTERN = r'("|u8")(.*?)",?'
STRING_PATTERN = r'\.([a-z_]+)\s+=\s+(u8)?"(.*)",?'
BOOLEAN_PATTEN = r'\.([a-z_]+)\s+=\s+(true|false),?'
WORDS_PATTEN = r'\.words\s+=\s+{'

TEMPLATE = """
from lzma import decompress as lzma
from base64 import b85decode
from hashlib import sha256

WORDS = '{{ WORDS }}'
words = lzma(b85decode(WORDS.encode()))
assert sha256(words).hexdigest() == '{{ CHECKSUM }}'
words = words.decode().split(' ')

polyseed_lang_en = {
    'name': '{{ name }}',
    'name_en': '{{ name_en }}',
    'separator': '{{ separator }}',
    'is_sorted': {{ is_sorted }},
    'has_prefix': {{ has_prefix }},
    'has_accents': {{ has_accents }},
    'compose': {{ compose }},
    'words': words
}
""".strip()


def check_data_valid(data: Dict) -> None:
    for key, value in data.items():
        if value is None:
            raise Exception(f'Data invalid, {key} is {value}!')
            return False
    if len(data['words']) != 2048:
        raise Exception(f'Data invalid, {len(data["words"])} words, expected: 2048')

def parse_c_file(filename: Union[str, Path]) -> Dict:
    filename = Path(filename).absolute()
    out = {
        'name': None,
        'name_en': None,
        'separator': None,
        'is_sorted': None,
        'has_prefix': None,
        'has_accents': None,
        'compose' : None,
        'words': []
    }
    with open(filename, 'r') as f:
        words: bool = False
        data = [line.strip() for line in f.read().split('\n') if line != '']
        f.close()
    for line in data:
        if not words:
            if (result := search(STRING_PATTERN, line)) and result.group(1) in out:
                out[result.group(1)] = result.group(3)
                continue
            if (result := search(BOOLEAN_PATTEN, line)) and result.group(1) in out:
                out[result.group(1)] = result.group(2) == 'true'
                continue
            if search(WORDS_PATTEN, line):
                words = True
                continue
            continue
        if result := search(WORD_PATTERN, line):
            out['words'].append(result.group(2))
    check_data_valid(out)
    return out

def write_py_file(data: Dict, filename: Union[str, Path]) -> None:
    filename = Path(filename).absolute()

    words_line = ' '.join(data['words'])
    checksum = sha256(words_line.encode()).hexdigest()
    compressed_words = b85encode(lzma(words_line.encode())).decode()
    out = TEMPLATE.replace('{{ WORDS }}', compressed_words).replace('{{ CHECKSUM }}', checksum)
    for key, value in data.items():
        if key == 'words':
            continue
        out = out.replace('{{ ' + key + ' }}', str(value))
    with open(filename, 'w') as f:
        f.write(out)
        f.close()
