import uuid


class TokenGenerator:
    @staticmethod
    def generateToken(formData):
        formDataJSON = dict(formData)
        rand_token = uuid.uuid4()
        # /print(rand_token)
        formDataJSON['regToken'] = str(rand_token)
        # print(formDataJSON)
        return formDataJSON
