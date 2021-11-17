
from pip._vendor import requests

from framework.fileservice_data_generator import DocumentDataGenerator, TemplateDataGenerator

BASE_API_URL = 'http://fileservice-low-p2-fileservice.kubernetes.moduldev.ru'


class APIDocument:

    def add_document_fileservice(self, payload, files):
        url = f'{BASE_API_URL}/api/documents'
        response = requests.request("POST", url, data=payload, files=files)
        return response.json()

    def get_document_fileservice(self, documentId):
        url = f'{BASE_API_URL}/api/documents/{documentId}'
        response = requests.get(url)
        return response.json()

    def delete_document_fileservice(self, documentId):
        url = f'{BASE_API_URL}/api/documents/{documentId}'
        response = requests.request("DELETE", url)
        return response.json()

    def add_signature_for_document_fileservice(self, files, documentId):
        url = f'{BASE_API_URL}/api/documents/{documentId}/signatures'
        response = requests.request("POST", url, files=files)
        return response

    def add_signature_from_files_for_document_fileservice(self, payload, documentId):
        url = f'{BASE_API_URL}/api/documents/{documentId}/signatures'
        response = requests.request("POST", url, data=payload)
        return response

    def delete_signature_from_files_for_document_fileservice(self, documentId, signatureId):
        url = f'{BASE_API_URL}/api/documents/{documentId}/signatures/{signatureId}'
        response = requests.request("DELETE", url)
        return response

    def get_signature_info(self, documentId, signatureId):
        url = f'{BASE_API_URL}/api/documents/{documentId}/signatures/{signatureId}'
        response = requests.request("GET", url)
        return response.json()

    def search_document_list_fileservice(self, params):
        url = f'{BASE_API_URL}/api/documents'
        response = requests.request("GET", url, params=params)
        return response.json()

    def add_document_attributes_fileservice(self, documentId, payload):
        url = f'{BASE_API_URL}/api/documents/{documentId}/attributes'
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    def delete_document_attributes_fileservice(self, documentId, payload):
        url = f'{BASE_API_URL}/api/documents/{documentId}/attributes'
        headers = {'Content-Type': 'application/json'}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response

    def get_downloads_document_fileservice(self, documentId):
        url = f'{BASE_API_URL}/api/documents/{documentId}/downloads'
        response = requests.request("GET", url)
        return response

    def get_url_downloads_document_fileservice(self, documentId):
        url = f'{BASE_API_URL}/api/documents/{documentId}/urls'
        response = requests.request("GET", url)
        return response.json()

    def downloads_nginx(self, data):
        url = f"http://172.21.28.6:9000{data}"
        response = requests.request("GET", url)
        return response



class APIFile:

    def add_file_fileservice(self, file):
        url = f"{BASE_API_URL}/api/files"
        response = requests.request("POST", url, files=file)
        return response.json()

    def update_expiration_date_file_fileservice(self, fileId, payload):
        url = f"{BASE_API_URL}/api/files/{fileId}/"
        headers = {'Content-Type': 'application/json'}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        return response

    def delete_file_fileservice(self, fileId):
        url = f"{BASE_API_URL}/api/files/{fileId}"
        response = requests.request("DELETE", url)
        return response

    def get_file_fileservice(self, fileIdId):
        url = f'{BASE_API_URL}/api/files/{fileIdId}'
        response = requests.get(url)
        return response.json()

    def get_url_downloads_file_fileservice(self, fileId):
        url = f"{BASE_API_URL}/api/files/{fileId}/urls"
        response = requests.request("GET", url)
        return response.json()

    def get_downloads_file_fileservice(self, fileId):
        url = f"{BASE_API_URL}/api/files/{fileId}/downloads"
        response = requests.request("GET", url)
        return response

    def delete_expired_files_from_fileservice(self):
        url = f"{BASE_API_URL}/api/files/expired"
        response = requests.request("DELETE", url)
        return response

    def downloads_nginx(self, data):
        url = f"http://172.21.28.6:9000{data}"
        response = requests.request("GET", url)
        return response


class APITemplate:

    def add_template_for_fileservice(self, payload, file):
        url = f'{BASE_API_URL}/api/templates'
        response = requests.request("POST", url, data=payload, files=file)
        return response.json()


    def get_template_from_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}'
        response = requests.request("GET", url)
        return response.json()

    def delete_template_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}'
        response = requests.request("DELETE", url)
        return response.json()

    def get_templates_list_fileservice(self, params):
        url = f'{BASE_API_URL}/api/templates'
        response = requests.request("GET", url, params=params)
        return response

    def get_downloads_template_from_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}/downloads'
        response = requests.request("GET", url)
        return response

    def get_url_downloads_template_from_fileservice(self, templateId):
        url = f'{BASE_API_URL}/api/templates/{templateId}/urls'
        response = requests.request("GET", url)
        return response.json()

    def downloads_nginx(self, data):
        url = f"http://172.21.28.6:9000{data}"
        response = requests.request("GET", url)
        return response
