from project_storage.category import Category
from project_storage.topic import Topic


class Document:

    def __init__(self, id_document, category_id, topic_id, file_name):
        self.id = id_document
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, id_new: int, category: Category, topic: Topic, file_name: str):
        return cls(id_new, category.id, topic.id, file_name)

    def add_tag(self, tags_content):
        if tags_content not in self.tags:
            self.tags.append(tags_content)
        return

    def remove_tag(self, tags_content):
        if tags_content in self.tags:
            self.tags.remove(tags_content)
        return

    def edit(self, file_name):
        self.file_name = file_name
        return

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {', '.join(self.tags)}"
