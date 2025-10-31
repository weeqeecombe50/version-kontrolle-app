class VersionControl:
    def __init__(self):
        self.versions = {}

    def save_version(self, file_name, content):
        self.versions[file_name] = content

    def get_version(self, file_name):
        return self.versions.get(file_name, None)

    def restore_version(self, file_name):
        # Logik zur Wiederherstellung der Version
        pass
