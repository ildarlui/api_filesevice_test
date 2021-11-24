import json
from unittest import TestCase

from framework.fileservice_api_wrapper import APIDocument, APIFile
from framework.fileservice_data_generator import Constants_FS, AttributesGenerator, DocumentDataGenerator
from framework.fileservice_file_generator import FileGenerator


class APIDocumentTests(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.api_document = APIDocument()
        cls.api_files = APIFile()
        cls.api_file = FileGenerator()
        cls.api_attributes = AttributesGenerator()
        cls.data_generator = DocumentDataGenerator()

    def setUp(self) -> None:
        self.main_payload = self.data_generator.generator_payload_document_for_fileservice()
        self.main_payload.entityArea = 'Showcase'
        files = self.api_file.get_file_document_docx()
        self.new_document = self.api_document.add_document_fileservice(self.main_payload.__dict__, files)

    def test_getting_document_info(self):
        """"Проверяем что возвращается информация о документе"""
        document_info = self.api_document.get_document_fileservice(self.new_document['data'])
        self.assertEqual(document_info['data']['id'], self.new_document['data'])

    def test_getting_signature_info(self):
        """"Проверяем что возвращается информация о подписи"""
        files = self.api_file.get_file_signature_sig()
        document_id = self.new_document['data']
        add_signature = self.api_document.add_signature_for_document_fileservice(files, document_id)
        signature_id = add_signature.json()['data']
        signature_info = self.api_document.get_signature_info(document_id, signature_id)
        self.assertEqual(signature_info['data']['id'], signature_id)
        self.assertEqual(signature_info['data']['document_id'], document_id)

    def test_add_signature_for_document(self):
        """"Проверяем что загруженная подпись прикрепляется к документу"""
        files = self.api_file.get_file_signature_sig()
        add_signature = self.api_document.add_signature_for_document_fileservice(files, self.new_document['data'])
        signature_id = add_signature.json()['data']
        signature_info = self.api_document.get_signature_info(self.new_document['data'], signature_id)
        self.assertEqual(signature_info['data']['id'], signature_id)
        self.assertEqual(signature_info['data']['documentId'], self.new_document['data'])

    def test_add_signature_from_file_for_document(self):
        """"Проверяем что подпись из файлов прикрепляется к документу"""
        file = self.api_file.get_file_signature_sig()
        file_id = self.api_files.add_file_fileservice(file)['data']
        payload = {'signatureFileId': f'{file_id}'}
        document_id = self.new_document['data']
        add_signature = self.api_document.add_signature_from_files_for_document_fileservice(payload, document_id)
        signature_id = add_signature.json()['data']
        document_info = self.api_document.get_document_fileservice(self.new_document['data'])
        print(type(signature_id))
        self.assertEqual(document_info['data']['id'], document_id)
        self.assertIn(signature_id, document_info['data']['signatureIds'])

    def test_delete_signature(self):
        """"Проверяем что подпись удаляется из документа"""
        file = self.api_file.get_file_signature_sig()
        file_id = self.api_files.add_file_fileservice(file)['data']
        payload = {'signatureFileId': f'{file_id}'}
        document_id = self.new_document['data']
        signature_id = self.api_document.add_signature_from_files_for_document_fileservice(payload, document_id).json()['data']
        self.api_document.delete_signature_from_files_for_document_fileservice(document_id, signature_id)
        document_info = self.api_document.get_document_fileservice(self.new_document['data'])
        self.assertNotIn('signatureIds', document_info['data'])

    def test_get_url_downloads_document(self):
        """"Проверяем что возвращается адрес для скачивания документа"""
        url_downloads = self.api_document.get_url_downloads_document_fileservice(self.new_document['data'])
        downloads_document = self.api_document.downloads_nginx(url_downloads['data'])
        self.assertEqual(downloads_document.status_code, 200)
        print(url_downloads['data'])
        downloads_url_data_test = f"/{self.main_payload.bucket.lower()}/{self.main_payload.entityType.lower()}/" \
               f"{self.main_payload.entityArea.lower()}/{Constants_FS.ENITITY_ID.replace('-', '')}/"
        #Вставить id
        self.assertIn(downloads_url_data_test, url_downloads['data'])

    def test_downloads_document(self):
        """"Проверяем что документ скачивается """
        downloads_document = self.api_document.get_downloads_document_fileservice(self.new_document['data'])
        self.assertEqual(downloads_document.status_code, 200)

    def test_add_attributes_for_document(self):
        """"Проверяем что появляются атрибуты """
        payload = self.api_attributes.get_attributes()
        self.api_document.add_document_attributes_fileservice(self.new_document['data'], json.dumps(payload))
        document_with_attributes = self.api_document.get_document_fileservice(self.new_document['data'])
        self.assertEqual(document_with_attributes['data']['attributes'], payload['attributes'])

    def test_delete_attributes_from_document(self):
        """"Проверяем что удаляются атрибуты """
        payload = json.dumps(self.api_attributes.get_attributes())
        self.api_document.add_document_attributes_fileservice(self.new_document['data'], payload)
        self.api_document.get_document_fileservice(self.new_document['data'])
        self.api_document.delete_document_attributes_fileservice(self.new_document['data'], payload)
        document_no_attributes = self.api_document.get_document_fileservice(self.new_document['data'])
        self.assertNotIn('attributes', document_no_attributes['data'])

    def test_search_documents_for_enityid_and_attributes_from_fileservice(self):
        """Проверяем поиск документа по родительской сущности и атрибутам"""
        payload = json.dumps(self.api_attributes.get_attributes())
        self.api_document.add_document_attributes_fileservice(self.new_document['data'], payload)
        info_document = self.api_document.get_document_fileservice(self.new_document['data'])
        params = {'entityId': Constants_FS.ENITITY_ID, 'additionalProp1': 'string1', 'additionalProp2': 'string2', 'limit': 10, 'offset': 0}
        search_document_list = self.api_document.search_document_list_fileservice(params)
        self.assertIn(info_document['data'], search_document_list['data'])

    def test_search_documents_for_enityid(self):
        """Проверяем поиск документа по родительской сущности"""
        payload = json.dumps(self.api_attributes.get_attributes())
        self.api_document.add_document_attributes_fileservice(self.new_document['data'], payload)
        info_document = self.api_document.get_document_fileservice(self.new_document['data'])
        params = {'entityId': Constants_FS.ENITITY_ID, 'limit': 10, 'offset': 0}
        search_document_list = self.api_document.search_document_list_fileservice(params)
        self.assertIn(info_document['data'], search_document_list['data'])

    def test_search_documents_for_attributes_from_fileservice(self):
        """Проверяем поиск документа по атрибутам"""
        payload = json.dumps(self.api_attributes.get_attributes())
        self.api_document.add_document_attributes_fileservice(self.new_document['data'], payload)
        info_document = self.api_document.get_document_fileservice(self.new_document['data'])
        params = {'entityId': '', 'attributes.additionalProp1': 'string1', 'attributes.additionalProp2': 'string2', 'limit': 10, 'offset': 0}
        search_document_list = self.api_document.search_document_list_fileservice(params)
        self.assertIn(info_document['data'], search_document_list['data'])

    # def test_error_format_signature(self):
    #     """"Проверяем что выдается ошибка при загрузке подписи другого формата"""
    #     files = self.api_file.get_file_image_png()
    #     documentId = self.new_document['data']
    #     add_signature = self.api_document.add_signature_for_document_fileservice(files, documentId)
    #     self.assertEqual(add_signature.status_code, 400)

    def tearDown(self) -> None:
        self.api_document.delete_document_fileservice(self.new_document['data'])
