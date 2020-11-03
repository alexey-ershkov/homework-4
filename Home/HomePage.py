from Base import Page
from Home.HomeComponents import *


class HomePage(Page):
    PATH = 'home/'

    def open(self):
        super(HomePage, self).open()
        self.utils.close_banner_if_exists()
        self.utils.close_mini_banner_if_exists()

    @property
    def utils(self):
        return Utils(self.driver)

    @property
    def folders(self):
        return Folders(self.driver)

    @property
    def files(self):
        return Files(self.driver)

    @property
    def history(self):
        return FileHistory(self.driver)

    @property
    def download(self):
        return Download(self.driver)

    @property
    def favorites(self):
        return Favorites(self.driver)

    @property
    def copy(self):
        return Copy(self.driver)

    @property
    def move(self):
        return Move(self.driver)

    @property
    def rename(self):
        return Rename(self.driver)

    @property
    def share(self):
        return Share(self.driver)
