from ebook import EBook

if __name__ == '__main__':
    book = EBook('alice_in_wonderland.txt', 1000)

    print(book.get_total_pages())
    print(book.display_page_content(1))
    book.store_bookmark('test', 10)
    book.store_bookmark('test1', 10)
    book.store_bookmark('test2', 11)

    book.delete_bm_by_name("test1")
    book.delete_bm_by_name('test2')
    book.store_bookmark('a', 13)
    book.store_bookmark('b', 14)
    book.store_bookmark('c', 15)
    book.store_bookmark('d', 13)
    book.store_bookmark('e', 13)


    book.display_bookmarks()

    book.delete_bm_by_name('a')
    book.delete_all_bm_for_page(10)
    print('\n')
    book.display_bookmarks()
    book.display_page_by_bm('b')
    book.display_page_by_bm('d')
    book.display_page_by_bm('c')
    book.store_bookmark('c', 16)
    book.display_page_by_bm('c')