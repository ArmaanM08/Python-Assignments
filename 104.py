class Writer:
    def write(self):
        print("Writing...")

class Editor:
    def edit(self):
        print("Editing...")

class Author(Writer, Editor):
    pass


author = Author()
author.write()
author.edit()