from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__make_album()

    def __make_album(self):
        album = []
        for row in range(self.pages):
            album.append([])
        return album

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        separator = '-' * 11
        result = ''
        for r in range(len(self.photos)):
            result += separator + '\n'
            if not len(self.photos[r]):
                result += '\n'
            else:
                res = ''
                for c in self.photos[r]:
                    res = ' '.join(['[]' for _ in self.photos[r]])
                result += res + '\n'
        result += separator
        return result
