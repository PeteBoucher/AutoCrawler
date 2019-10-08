import os
import shutil
from unittest import TestCase

from main import AutoCrawler

PROJECT_DIRS = ['./__pycache__', './docs', './chromedriver']

PROJECT_FILES = {'./collect_links.py', './keywords.txt', './README.md',
                 './requirements.txt', './main.py', './LICENSE'}


class TestAutoCrawler(TestCase):

    # def test_all_dirs_should_return_dirs_in_project(self):
    #     self.assertTrue(set(AutoCrawler.all_dirs('.')).issuperset(set(PROJECT_DIRS)),
    #                     "Should include all dirs in the project root")

    def test_all_dirs_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            AutoCrawler.all_dirs('nom/existent/dir')
            # Should raise an exception

    # def test_all_filrs_should_return_dirs_in_project(self):
    #     self.assertTrue(set(AutoCrawler.all_files('.')).issuperset(set(PROJECT_FILES)),
    #                     "Should include all files in the project root")

    def test_all_files_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            AutoCrawler.all_dirs('nom/existent/dir')
            # Should raise an exception

    def test_get_extension_from_link_jpg(self):
        self.assertEqual(AutoCrawler.get_extension_from_link('www.hotel.ca/ifornia.jpg'), 'jpg')

    def test_get_extension_from_link_jpeg(self):
        self.assertEqual(AutoCrawler.get_extension_from_link('www.hotel.ca/ifornia.jpeg'), 'jpg')

    def test_get_extension_from_link_gif(self):
        self.assertEqual(AutoCrawler.get_extension_from_link('www.hotel.ca/ifornia.gif'), 'gif')

    def test_get_extension_from_link_png(self):
        self.assertEqual(AutoCrawler.get_extension_from_link('www.hotel.ca/ifornia.png'), 'png')

    def test_get_extension_from_link_tiff(self):
        self.assertEqual(AutoCrawler.get_extension_from_link('www.hotel.ca/ifornia.tiff'), 'jpg')

    def test_get_extension_from_link_empty(self):
        self.assertEqual(AutoCrawler.get_extension_from_link(''), 'jpg')

    def test_validate_image_jpg(self):
        self.assertEqual('jpg', AutoCrawler.validate_image('mocks/biplane.jpg'))

    def test_validate_image_jpeg(self):
        self.assertEqual('jpg', AutoCrawler.validate_image('mocks/triplane.jpeg'))

    def test_validate_image_gif(self):
        self.assertEqual('gif', AutoCrawler.validate_image('mocks/jet.gif'))

    def test_validate_image_not_exists(self):
        with self.assertRaises(FileNotFoundError):
            AutoCrawler.validate_image('mocks/nothing.jpg')

    def test_make_dir(self):
        test_directory_name = 'testDir'

        AutoCrawler.make_dir(test_directory_name)
        self.assertIn(test_directory_name, os.listdir('.'), "Should create a test directory")

        # cleanup
        os.rmdir(test_directory_name)

    def test_make_dir_new_path(self):
        test_root = 'path/'
        test_path = f'{test_root}to/testDir'

        AutoCrawler.make_dir(test_path)
        self.assertTrue(os.path.exists(test_path), "Should create a test directory at the given path")

        # cleanup
        shutil.rmtree(test_root)

    def test_get_keywords(self):
        keywords = AutoCrawler.get_keywords('mocks/keywords.txt')
        self.assertIn('cat', keywords, "Should be a list of keywords including 'cat'")
