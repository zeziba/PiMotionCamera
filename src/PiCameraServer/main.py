from subprocess import Popen, getoutput
from os import getcwd, listdir, mkdir, chmod, stat, system
from os.path import join
from time import sleep

"""
Purpose:
    Locate and connect to RPINAS network to store images when available
    Disconnect from server when finished storing images
"""


class ConnectionManager:

    def __init__(self, user='root', password='pi', location="/mnt/smbServer"):
        self.queue = []
        self.server_location = location
        self.server_IP = None
        self.password = password
        self.user = user
        self.connection = False

    def make_connection(self, timeout=10):
        def find_server():
            return getoutput(['nmblookup \'RPINAS\'', '|', 'grep \'[0-9.]{7,15}\''])

        status = False
        self.server_IP = False
        print("Locating server and attempting to connect.")
        try:
            if not stat(self.server_location):
                mkdir(self.server_location)
                chmod(self.server_location, 755)
                print("Created server mount location at %s." % self.server_location)
            status = True
        except FileExistsError or FileNotFoundError or PermissionError as error:
            print(error)
        if status:
            self.server_IP = find_server()
            print("Attempting to mount %s at %s." % (self.server_IP, self.server_location))
            if 'failed' not in self.server_IP:
                system('mount -t cifs -o userename=%s,password=%s //%s/data %s' %
                       (self.user, self.password, self.server_IP, self.server_location))
                self.connection = True
            else:
                print("Failed to locate the server.")
                for i in range(timeout):
                    sleep(1)
                    print("Retrying to locate server in %s seconds" % (timeout - i))
                if timeout <= 0:
                    print("Failed to locate the server")
                    return False
                self.make_connection(timeout - 5)

    def close_connection(self, timeout=10):
        if self.connection:
            print("Attempting to close the server: %s, mounted at %s" % (self.server_IP, self.server_location))
            result = system('umount -t auto %s' % self.server_location)
            if result:
                print("Disconnection was a success")
            else:
                print("Disconnection failed, retrying in %s" % timeout)
                for i in range(timeout):
                    sleep(1)
                    print("Retrying in %s seconds." % (timeout - i))
                if timeout <= 0:
                    print("Disconnection Failed.")
                    return False
                self.close_connection(timeout - 5)
        else:
            print("No Connection to disconnect.")

    def __copy_file(self, destination, file):
        self.queue.append(Popen(["cp", file, destination]))

    def copy_files(self, source, destination):
        files = [join(source, file) for file in listdir(source)]
        for file in files:
            self.__copy_file(destination, file)

    @staticmethod
    def _check(command):
        command.communicate()

    def check_all(self):
        for command in self.queue:
            self._check(command=command)

if __name__ == '__main__':
    manager = ConnectionManager()
    manager.make_connection()
    manager.copy_files(join(getcwd(), "test_folder_source"), join(getcwd(), "test_folder_destination"))
    manager.check_all()
    sleep(10)
    manager.close_connection()
