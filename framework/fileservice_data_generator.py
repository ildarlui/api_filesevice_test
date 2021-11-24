import random
from framework.fileservice_DTO import FileServiceDocumentDTO, FileServiceTemplateDTO


class Constants_FS:
    PUBLIC = 'Public'
    COMMON = 'Common'
    TEMP = 'Temp'
    INTERNET_ACQUIRING = 'InternetAcquiring'
    BANK_GUARANTEE = 'BankGuarantee'
    MERCHANT_ACQUIRING = 'MerchantAcquiring'
    SHOWCASE = 'Showcase'
    SHOWCASE_TEST = 'ShowcaseTest'
    ENITITY_ID = '9103bb2b-226b-9c6e-9649-0cd39a0d6d9a'


class DocumentDataGenerator:

    def generator_payload_document_for_fileservice(self):
        payload = self.get_random_fileservice_document()
        return payload

    def random_bucket(self):
        return random.choice([Constants_FS.PUBLIC, Constants_FS.COMMON, Constants_FS.TEMP])

    def get_random_fileservice_document(self):
        FS_document = FileServiceDocumentDTO
        FS_document.bucket = Constants_FS.PUBLIC
        FS_document.entityType = Constants_FS.INTERNET_ACQUIRING
        FS_document.entityArea = Constants_FS.SHOWCASE
        FS_document.entityId = Constants_FS.ENITITY_ID
        FS_document.documentId = ''
        FS_document.hasAttachedSign = ''
        FS_document.signatureId = ''
        return FS_document



class TemplateDataGenerator:

    def generator_payload_template_for_fileservice(self):
        payload = self.get_random_fileservice_template()
        return payload

    def get_random_fileservice_template(self):
        FS_template = FileServiceTemplateDTO
        FS_template.bucket = Constants_FS.PUBLIC
        FS_template.entityType = Constants_FS.INTERNET_ACQUIRING
        FS_template.entityArea = Constants_FS.SHOWCASE
        return FS_template


class AttributesGenerator:

    def get_attributes(self):
        attributes = {"attributes": {
            "additionalProp1": ["string1"],
            "additionalProp2": ["string2"]}}
        return attributes

class ExpersionDateGenerator:

    def get_expersion_date(self):
        expiration_date = {"expirationDate": "2021-10-08T07:47:33.090Z"}
        return expiration_date
