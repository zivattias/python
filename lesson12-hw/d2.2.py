class InvalidPage(Exception):
    def __init__(self):
        super().__init__('Invalid page number')


class EBook:

    def __init__(self, book_path: str, words_num: int):

        self.book_path = book_path
        self.pages: dict[int: str] = {}

        with open(book_path, 'r') as fh:
            content = fh.read()

        all_words: list[str] = content.split()
        page_num = 0
        for i in range(0, len(all_words), words_num):
            page_words = all_words[i: i + words_num]
            self.pages[page_num] = " ".join(page_words)
            page_num += 1

    def __iter__(self):
        self.page_num = 0
        return self

    def __next__(self):
        if self.page_num == self.get_total_pages():
            raise StopIteration

        self.content = self.get_page_content(self.page_num)
        self.page_num += 1

        return self.page_num, self.content

    def get_total_pages(self):
        return len(self.pages)

    def get_page_content(self, page_num) -> str:
        if page_num not in self.pages:
            raise InvalidPage()
        return self.pages[page_num]


if __name__ == '__main__':
    book = EBook('./alice_in_wonderland.txt', 1000)
    # print(f"Total pages: {book.get_total_pages()}")
    # print(f"Page 1: {book.get_page_content(1)}")
    # print(book.__dict__)
    for page_num, page_content in book:
        print(f"Page {page_num}: {page_content}")
