class Author:
    all = []
    
    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        try:
            if isinstance(name, str):
                self._name = name
            else:
                raise ValueError('Name must be of string type.')
        except Exception as e:
            print(f'Error: {e}')

   
         
    def contracts(self):
         contract_list = []
         for contract in Contract.all:
              if contract.author == self:
                 contract_list.append(contract)
         return contract_list

                 
    def books(self):
        author_books = []
        for contract in Contract.all:
             if contract.author == self:
                  author_books.append(contract.book)
        return author_books
    
    def sign_contract(self, book, date, royalties):
         if isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
              new_contract = Contract(self, book, date, royalties)
              return new_contract
         else:
              raise ValueError('Invalid input for book, date, or royalties.')
         
    def total_royalties(self):
         total = 0
         for contract in Contract.all:
              if contract.author == self:
                   total += contract.royalties 
         return total
              

              
          



class Book:
    all = []
    def __init__(self, title):
       self._title = title
       Book.all.append(self)

    @property
    def title(self):
           return self._title
    @title.setter
    def title(self, title):
           try:
              if isinstance(title, str):
                 self._title = title
              else:
                 raise ValueError('Title must be a string.')
           except Exception as e:
                  print(f'Error: {e}')

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
                
            if contract.book == self:
                contract_list.append(contract)
        return contract_list
    
    def authors(self):
        contract_author = []
        for contract in Contract.all:
            if contract.book == self:
                contract_author.append(contract.author)
        return contract_author
               
          


               

                  
class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError('Author must be an instance of the Author class.')

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise ValueError('Book must be an instance of the Book class.')

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise ValueError('Date must be a string.')

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise ValueError('Royalties must be an integer.')

    @classmethod
    def contracts_by_date(cls, date):
        same_date = []
        for contract in cls.all:
            if contract.date == date:
                same_date.append(contract)
        return same_date

         
