from project_storage.category import Category
from project_storage.document import Document
from project_storage.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        self.__add_in_current_list(category, self.categories)

    def add_topic(self, topic: Topic):
        self.__add_in_current_list(topic, self.topics)

    def add_document(self, document: Document):
        self.__add_in_current_list(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_obj_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_obj_by_id(self.topics, topic_id)
        topic.topic = new_topic
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_obj_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_obj_by_id(self.categories, category_id)
        self.__remove_obj(self.categories, category)

    def delete_topic(self, topic_id):
        topic = self.__find_obj_by_id(self.topics, topic_id)
        self.__remove_obj(self.topics, topic)

    def delete_document(self, document_id):
        document = self.__find_obj_by_id(self.documents, document_id)
        self.__remove_obj(self.documents, document)

    def get_document(self, document_id):
        document = self.__find_obj_by_id(self.documents, document_id)
        return document

    @staticmethod
    def __add_in_current_list(objects, list_to_add):
        if objects not in list_to_add:
            list_to_add.append(objects)

    @staticmethod
    def __find_obj_by_id(obj, ids):
        for objects in obj:
            if objects.id == ids:
                return objects

    @staticmethod
    def __remove_obj(list_to_remove, obj):
        list_to_remove.remove(obj)

    def __repr__(self):
        result = '\n'.join([str(obj) for obj in self.documents])
        return result
