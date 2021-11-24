from project_spoopify.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for albums in self.albums:
            if albums.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for albums in self.albums:
            if albums.name == album_name:
                if albums.published:
                    return "Album has been published. It cannot be removed."
                else:
                    self.albums.remove(albums)
                    return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        a = f"Band {self.name}"
        for al in self.albums:
            a += f'\n{al.details()}'

        return a
