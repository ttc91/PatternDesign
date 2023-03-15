class EnglishLocalizer:
    def localize(self, msg):
        return msg

class ChineseLocalizer:
    def __init__(self):
        self.translations = {"hello": "你好", "car": "车", "city": "城市"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class VietnameseLocalizer:
    def __init__(self):
        self.translations = {"hello": "xin chào", "car" : "xe", "city" : "thành phố"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

def Factory(language = "English"):

    localizers = {
        "English" : EnglishLocalizer,
        "Chinese" : ChineseLocalizer,
        "Vietnamese" : VietnameseLocalizer
    }

    return localizers[language]();

if __name__ == '__main__':

    v = Factory("Vietnamese")

    print(v.localize("hello"))




