import uuid
from hashlib import sha256


class TokenGenerator:
    @staticmethod
    def generateToken(formData):
        dataCollection = {}
        formDataJSON = dict(formData)
        rand_token = uuid.uuid4()
        integrityCheck = sha256(str(rand_token).encode('utf-8')).hexdigest()
        dataCollection["integrity"] = integrityCheck
        formDataJSON['regToken'] = str(rand_token)
        dataCollection['formData'] = formDataJSON
        return dataCollection
