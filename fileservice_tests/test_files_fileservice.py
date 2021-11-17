import json
from unittest import TestCase


from framework.fileservice_api_wrapper import APIFile
from framework.fileservice_data_generator import AttributesGenerator, ExpersionDateGenerator
from framework.fileservice_file_generator import FileGenerator


class APIFiletests(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.api_files = APIFile()
        cls.api_file = FileGenerator()
        cls.api_attributes = AttributesGenerator()
        cls.exp_date = ExpersionDateGenerator()

    def setUp(self) -> None:
        file = self.api_file.get_file_image_png()
        self.new_file = self.api_files.add_file_fileservice(file)

    def test_getting_file_info(self):
        """"Проверяем что возвращается информация о документе"""
        document_info = self.api_files.get_file_fileservice(self.new_file['data'])
        self.assertEqual(document_info['data']['id'], self.new_file['data'])

    def test_update_expiration_date_file(self):
        """"Проверяем что у файла поменялась expirationDate"""
        payload = self.exp_date.get_expersion_date()
        updated_file = self.api_files.update_expiration_date_file_fileservice(self.new_file['data'], json.dumps(payload))
        #найти этот файл и проверить дату в базе данных
        self.assertEqual(updated_file.status_code, 200)

    def test_delete_files_with_exp_date(self):
        """Проверка удаления файлов с истекшим сроком жизни"""
        payload = self.exp_date.get_expersion_date()
        self.api_files.update_expiration_date_file_fileservice(self.new_file['data'], json.dumps(payload))
        self.api_files.delete_expired_files_from_fileservice()
        find_url_file = self.api_files.get_url_downloads_file_fileservice(self.new_file['data'])
        self.assertEqual(find_url_file['error']['code'], 'NotFound')

    def test_get_url_downloads_file(self):
        """"Проверяем что возвращается адрес для скачивания файла"""
        url_downloads = self.api_files.get_url_downloads_file_fileservice(self.new_file['data'])
        downloads_file = self.api_files.downloads_nginx(url_downloads['data'])
        self.assertEqual(downloads_file.status_code, 200)

    def test_downloads_file(self):
        """"Проверяем что файл скачивается """
        downloads_file = self.api_files.get_downloads_file_fileservice(self.new_file['data'])
        self.assertEqual(downloads_file.status_code, 200)

    def tearDown(self) -> None:
        self.api_files.delete_file_fileservice(self.new_file['data'])