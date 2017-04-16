import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we can't search that location")
        return

    text = get_search_text_from_user()
    if not text:
        print("we can't search for nothing")
        return

    matches = search_folders(folder, text)
    match_count = 0
    for match in matches:
        match_count += 1
        print('--------------MATCH-------------')
        print('file: {}'.format(match.file))
        print('line: {}'.format(match.line))
        print('match: {}'.format(match.text))
        print()

    print("found {} matches".format(match_count))


def print_header():
    print("-----------------------------")
    print("          File Search")
    print("-----------------------------")


def get_folder_from_user():
    folder = input("What folder do you want to search?")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for [single phreases only]?")
    return text.lower()


def search_folders(folder, text):
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)

        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file_in:
        line_number = 0
        for line in file_in:
            line_number +=1
            if line.lower().find(search_text) >= 0:
                match = SearchResult(line=line_number, file=filename, text=line.strip())
                yield match


if __name__ == '__main__':
    main()