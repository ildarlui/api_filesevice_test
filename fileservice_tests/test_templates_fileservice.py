import json
from unittest import TestCase

from framework.fileservice_api_wrapper import APITemplate
from framework.fileservice_data_generator import TemplateDataGenerator, Constants_FS
from framework.fileservice_file_generator import FileGenerator


class APITemplatetests(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.api_template = APITemplate()
        cls.api_file = FileGenerator()
        cls.data_generator = TemplateDataGenerator()

    def setUp(self) -> None:

        self.main_payload = self.data_generator.generator_payload_template_for_fileservice()
        file = self.api_file.get_file_image_png()
        self.new_template = self.api_template.add_template_for_fileservice(self.main_payload.__dict__, file)

    def test_template_info(self):
        """"Проверяем что возвращается информация о шаблоне"""
        template_info = self.api_template.get_template_from_fileservice(self.new_template['data'])
        self.assertEqual(template_info['data']['id'], self.new_template['data'])

    def test_get_templates_list(self):
        """"Проверяем что возвращается информация со списком шаблонов"""
        params = {'entityId': Constants_FS.ENITITY_ID, 'limit': 10, 'offset': 0}
        template_list_info = self.api_template.get_templates_list_fileservice(params)
        id_ = self.new_template['data']
        template_list_json = template_list_info.json()
        self.assertIn(id_, str(template_list_json['data']))


    def test_downloads_template(self):
        """"Проверяем что шаблон скачивается"""
        url_downloads = self.api_template.get_url_downloads_template_from_fileservice(self.new_template['data'])
        downloads_template = self.api_template.downloads_nginx(url_downloads['data'])
        self.assertEqual(downloads_template.status_code, 200)

    def test_fet_url_downloads_template(self):
        """"Проверяем что возвращается адрес для скачивания шаблона"""
        downloads_template = self.api_template.get_downloads_template_from_fileservice(self.new_template['data'])
        self.assertEqual(downloads_template.status_code, 200)

    def tearDown(self) -> None:
        self.api_template.delete_template_fileservice(self.new_template['data'])