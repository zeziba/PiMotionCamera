from os.path import join, split
from os import listdir, getcwd
from PIL import Image, ImageTk


class Loader:

    def __init__(self, save_location: str=getcwd()):
        self._path = save_location if save_location else None
        self._files = list()
        self.cache = dict()

        self.__current_index = 0

        self._load_files()

    def _load(self, img_location: str):
        self.cache[img_location] = Image.open(img_location)

    def read(self, img_location):
        try:
            self._load(img_location)
            return True
        except FileNotFoundError as error:
            print(error)
            return False

    def _load_files(self):
        """
        Function Works as required
        :return:
        """
        self._files = [join(self._path, file) for file in listdir(self._path)
                       if ".png" in split(file)[1]]

    def change_index(self, move_by):
        self.__current_index += move_by
        if self.__current_index < 0:
            self.__current_index += len(self._files)
        if self.__current_index > len(self._files) - 1:
            self.__current_index -= len(self._files)

    def __call__(self, size=(200, 200), *args, **kwargs):
        if self.read(self._files[self.__current_index]):
            return ImageTk.PhotoImage(self.cache[self._files[self.__current_index]].resize(size, Image.ANTIALIAS))
        else:
            print("FAIL")

    def __str__(self):
        return "".join('{:<3}:{:^}\n'.format(index, img) for index, img in enumerate(self._files))

if __name__ == "__main__":
    test = Loader(getcwd())
    print(test)