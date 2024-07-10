class TestData():
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    CREATE_USER = MAIN_URL + "/api/auth/register"
    LOGIN_USER = MAIN_URL + "/api/auth/login"
    USER_DATA = MAIN_URL + "/api/auth/user"
    CREATE_ORDER = MAIN_URL + "/api/orders"
    
    ROOLS_HASH = {
        "Флюоресцентная булка R2-D3": "61c0c5a71d1f82001bdaaa6d",
        "Краторная булка N-200i": "61c0c5a71d1f82001bdaaa6c"
    }
    SAUCES_HASH = {
        "Соус Spicy-X": "61c0c5a71d1f82001bdaaa72",
        "Соус фирменный Space Sauce": "61c0c5a71d1f82001bdaaa73",
        "Соус традиционный галактический": "61c0c5a71d1f82001bdaaa74",
        "Соус с шипами Антарианского плоскоходца": "61c0c5a71d1f82001bdaaa75"
    }
    FILLINGS_HASH = {
        "Мясо бессмертных моллюсков Protostomia": "61c0c5a71d1f82001bdaaa6f",
        "Говяжий метеорит (отбивная)": "61c0c5a71d1f82001bdaaa70",
        "Биокотлета из марсианской Магнолии": "61c0c5a71d1f82001bdaaa71",
        "Филе Люминесцентного тетраодонтимформа": "61c0c5a71d1f82001bdaaa6e",
        "Хрустящие минеральные кольца": "61c0c5a71d1f82001bdaaa76",
        "Плоды Фалленианского дерева": "61c0c5a71d1f82001bdaaa77",
        "Кристаллы марсианских альфа-сахаридов": "61c0c5a71d1f82001bdaaa78",
        "Мини-салат Экзо-Плантаго": "61c0c5a71d1f82001bdaaa79",
        "Сыр с астероидной плесенью": "61c0c5a71d1f82001bdaaa7a",
    }
    
    INGREDIENTS_SUITES = [
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус фирменный Space Sauce"], FILLINGS_HASH["Плоды Фалленианского дерева"]),
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус традиционный галактический"], FILLINGS_HASH["Кристаллы марсианских альфа-сахаридов"]),
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус с шипами Антарианского плоскоходца"], FILLINGS_HASH["Мини-салат Экзо-Плантаго"]),
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус Spicy-X"], FILLINGS_HASH["Сыр с астероидной плесенью"])
        
    ]
    
    REQUIRED_REGISTRATION_FIELD_SUITES = [
        {
            "email": "email",
            "name": "name" 
        },
        {
            "password": "password",
            "name": "name"
        },
        {
            "email": "email",
            "password": "password"
        }]
