

class FileGenerator:

    def get_file_document_docx(self):
        file = [('document', ('Проект банковской гарантии.docx', open('C:/Проект банковской гарантии.docx', 'rb'),
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))]
        return file

    def get_file_image_png(self):
        file = [('template', ('python-error.png', open('C:/python-error.png', 'rb'), 'image/png'))]
        return file

    def get_file_signature_sig(self):
        file = [('signature',('ValidSign_2222995569.sig', open('C:/ValidSign_2222995569.sig', 'rb'),
                              'application/octet-stream'))]
        return file

    def get_file_document_docx_with_signature_sig(self):
        document = [('document', ('Проект банковской гарантии.docx', open('C:/Проект банковской гарантии.docx', 'rb'),
                            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'))]
        signature = [('signature',
               ('ValidSign_2222995569.sig', open('C:/ValidSign_2222995569.sig', 'rb'), 'application/octet-stream'))]
        files = document+signature
        return files