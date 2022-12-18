from tkinter import *
from tkinter import filedialog


class FileExplorer:
    def __init__(self):
        self.__file_explorer = Tk()
        self.__folder_path = None
        self.__project_path = None

    def find_folder(self, project_path=None):
        self.__project_path = project_path
        self.__init_file_explorer()
        self.__file_explorer.after_idle(self.__find_folder)
        self.__file_explorer.mainloop()
        return self.__folder_path

    def __find_folder(self):
        self.__folder_path = filedialog.askdirectory(
            initialdir=self.__project_path)
        self.__destroy_file_explorer()

    def __init_file_explorer(self):
        if self.__file_explorer == None:
            self.__file_explorer = Tk()

    def __destroy_file_explorer(self):
        self.__file_explorer.destroy()
        self.__file_explorer = None
