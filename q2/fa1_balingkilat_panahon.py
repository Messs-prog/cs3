class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    #def display_info: pass

class Book (Publication):
    def __init__(self, title, author, pg_num):
        super().__init__(title, author)
        self.pg_num = pg_num
        def set_pg_num:
            self.pg_num = pg_num
        def get_pg_num:
            return pg_num
    
class Magazine(Publication):
    def __init__(self, title, author, iu_num):
        super().__init__(title, author)
        self.iu_num = iu_num
    #add get and set iu_num 

pub = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van dongen, H.")
book = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub.display_info()

print("\nBook Information")
book.set_pg_num(-310)
book.display_info()
print(book.get_pg_num())

print("\nMagazine Information:")
mag.display_info()
print(mag.get_iu_num())
