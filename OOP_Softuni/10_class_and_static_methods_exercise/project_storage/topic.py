class Topic:

    def __init__(self, id_topics, topic, storage_folder):
        self.id = id_topics
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder
        return

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
