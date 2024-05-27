from typing import Union, Dict
from pathlib import Path
from hashlib import sha256
from lzma import compress as lzma
from base64 import b85encode
from re import search
from argparse import ArgumentParser

WORD_PATTERN = r'("|u8")(.*?)",?'
STRING_PATTERN = r'\.([a-z_]+)\s+=\s+(u8)?"(.*)",?'
BOOLEAN_PATTEN = r'\.([a-z_]+)\s+=\s+(true|false),?'
WORDS_PATTEN = r'\.words\s+=\s+{'

TEMPLATE = """
from lzma import decompress as lzma
from base64 import b85decode
from hashlib import sha256
from typing import List
from .lang import Language

WORDS = '{{ WORDS }}'
words = lzma(b85decode(WORDS.encode()))
assert sha256(words).hexdigest() == '{{ CHECKSUM }}'
words = words.decode().split(' ')

class Language{{ class_name }}(Language):

    code: str = '{{ code }}'
    name: str = '{{ name }}'
    name_en: str = '{{ name_en }}'
    separator: str = '{{ separator }}'
    is_sorted: bool = {{ is_sorted }}
    has_prefix: bool = {{ has_prefix }}
    has_accents: bool = {{ has_accents }}
    compose: bool = {{ compose }}
    words: List[str] = words

Language{{ class_name }}.register()
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

def process_source_folder(source_folder: Union[str, Path], target_folder: Union[str, Path]) -> None:
    source_folder = Path(source_folder).absolute()
    target_folder = Path(target_folder).absolute()
    
    if not source_folder.is_dir():
        raise Exception(f'Source folder {source_folder} does not exist.')
        
    if not target_folder.is_dir():
        raise Exception(f'Target folder {target_folder} does not exist.')
        
    c_files = [file for file in source_folder.glob('lang_*.c') if file.is_file()]
    
    for c_file in c_files:
        try:
            parsed_data = parse_c_file(c_file)
            parsed_data['code'] = c_file.stem[5:]
            parsed_data['class_name'] = parsed_data['name_en'].replace(' ','').replace('(', '').replace(')', '')
            print(parsed_data['class_name'])
            target_filename = target_folder / (c_file.stem + '.py')
            write_py_file(parsed_data, target_filename)
        except Exception as e:
            print(f'Error in {c_file}: {e}')
            print(e)

if __name__ == '__main__':
    parser = ArgumentParser(description='Import languages from original polyseed repo')
    parser.add_argument('source', help='Path to the original polyseed source folder')
    parser.add_argument('target', help='Path to the target folder')
    
    args = parser.parse_args()

    process_source_folder(args.source, args.target)
