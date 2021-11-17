

class FileServiceDocumentDTO:
    def __init__(self, bucket=None, entityType=None, entityArea=None, entityId=None,
                 documentId=None, hasAttachedSign=None, signatureId=None):
        self.bucket = bucket
        self.entityType = entityType
        self.entityArea = entityArea
        self.entityId = entityId
        self.documentId = documentId
        self.hasAttachedSign = hasAttachedSign
        self.signatureId = signatureId


class FileServiceTemplateDTO:
    def __init__(self, bucket=None, entityType=None, entityArea=None):
        self.bucket = bucket
        self.entityType = entityType
        self.entityArea = entityArea