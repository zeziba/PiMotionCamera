from subprocess import Popen
from os import getcwd, listdir
from os.path import join

"""
Purpose:
    Locate and connect to RPINAS network to store images when available
    Disconnect from server when finished storing images
"""


class ConnectionManager:

    def __init__(self):
        self.queue = []

    @staticmethod
    def make_connection():
        with Popen(["connect_server.sh"]) as conn:
            conn.communicate()

    @staticmethod
    def close_connection():
        with Popen(["disconnect_server.sh"]) as conn:
            conn.communicate()

    def __copy_file(self, destination, file):
        self.queue.append(Popen(["cp", file, destination]))

    def copy_files(self, source, destination):
        files = [join(source, file) for file in listdir(source)]
        for file in files:
            self.__copy_file(destination, file)

    def check_all(self):
        while self.queue:
            self.queue.pop().communicate()

if __name__ == '__main__':
    manager = ConnectionManager()
    manager.copy_files(join(getcwd(), "test_folder_source"), join(getcwd(), "test_folder_destination"))
    manager.check_all()
