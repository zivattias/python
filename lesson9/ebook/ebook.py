import json
class EBook:

    def __init__(self, source: str, words_per_page: int):
        self.bookmarks: dict[int, list[str]] = {}
        # Dict mapping ebook to {page num: page content}
        self.__paginated_content: dict[int, str] = dict()

        with open(source, 'r') as fh:
            content = fh.read()

        # Split the entire txt content to words (defaults to whitespace)
        all_words: list[str] = content.split()

        page_num = 1
        for i in range(0, len(all_words), words_per_page):
            page_words = all_words[i: i + words_per_page]
            self.__paginated_content[page_num] = ' '.join(page_words)
            page_num += 1

    def get_total_pages(self) -> int:
        return len(self.__paginated_content)

    def display_page_content(self, page_num: int) -> str | None:
        if page_num not in self.__paginated_content:
            print(f"Page {page_num} not found.")
            return None
        return f"Page {page_num}:\n{self.__paginated_content[page_num]}"

    def store_bookmark(self, bm_name: str, page_num: int):
        if page_num not in self.bookmarks:
            self.bookmarks[page_num] = []
        self.bookmarks[page_num].append(bm_name)

    def delete_bm_by_name(self, bm_name: str):
        for page, bm in self.bookmarks.items():
            for name in bm:
                if name == bm_name:
                    bm.remove(bm_name)

    def display_bookmarks(self):
        for key, value in self.bookmarks.items():
            if len(value) != 0:
                print(f'{key}: {self.bookmarks[key]}')

    def delete_all_bm_for_page(self, page_num: int):
        to_delete: list = []
        for page in self.bookmarks:
            if page == page_num:
                to_delete.append(page)
        for page_to_delete in to_delete:
            del self.bookmarks[page_to_delete]

    def display_page_by_bm(self, bm_name: str):
        for key, value in self.bookmarks.items():
            if bm_name in value:
                print(f"Bookmark: {bm_name} appears on page {key}")


