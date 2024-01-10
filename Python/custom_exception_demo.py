class CustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise CustomError(100)
except CustomError as error:
    print("Exception : ", error.value)
