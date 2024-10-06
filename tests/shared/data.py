class TestData():
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    CREATE_USER_URL = MAIN_URL + "/api/auth/register"
    LOGIN_USER_URL = MAIN_URL + "/api/auth/login"
    USER_DATA_URL = MAIN_URL + "/api/auth/user"
    CREATE_ORDER_URL = MAIN_URL + "/api/orders"
    
    CORRECT_INGREDIENT_PAYLOAD = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa6d",
            "61c0c5a71d1f82001bdaaa73",
            "61c0c5a71d1f82001bdaaa77"]
    }

    WRONG_INGREDIENT_HASH = {
        "ingredients": [
            "61c0c5a71d1f82001bdaa111",
            "61c0c5a71d1f82001bdaa222",
            "61c0c5a71d1f82001bdaa333"]
    }
    
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

    EXPECTED_THREE_INGREDIENTS_SUITES = [
        {
            "success": True,
            "name": "Фалленианский space флюоресцентный бургер",
            "order": {
                "ingredients": [
                    {
                        "_id": "61c0c5a71d1f82001bdaaa6d",
                        "name": "Флюоресцентная булка R2-D3",
                        "type": "bun",
                        "proteins": 44,
                        "fat": 26,
                        "carbohydrates": 85,
                        "calories": 643,
                        "price": 988,
                        "image": "https://code.s3.yandex.net/react/code/bun-01.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/bun-01-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/bun-01-large.png",
                        "__v": 0
                    },
                    {
                        "_id": "61c0c5a71d1f82001bdaaa73",
                        "name": "Соус фирменный Space Sauce",
                        "type": "sauce",
                        "proteins": 50,
                        "fat": 22,
                        "carbohydrates": 11,
                        "calories": 14,
                        "price": 80,
                        "image": "https://code.s3.yandex.net/react/code/sauce-04.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/sauce-04-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/sauce-04-large.png",
                        "__v": 0
                    },
                    {
                        "_id": "61c0c5a71d1f82001bdaaa77",
                        "name": "Плоды Фалленианского дерева",
                        "type": "main",
                        "proteins": 20,
                        "fat": 5,
                        "carbohydrates": 55,
                        "calories": 77,
                        "price": 874,
                        "image": "https://code.s3.yandex.net/react/code/sp_1.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/sp_1-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/sp_1-large.png",
                        "__v": 0
                    }
                ],
                "owner": {
                },
                "status": "done",
                "name": "Фалленианский space флюоресцентный бургер",
                "price": 1942
            }
        },
        {
            "success": True,
            "name": "Альфа-сахаридный традиционный-галактический флюоресцентный бургер",
            "order": {
                "ingredients": [
                    {
                        "_id": "61c0c5a71d1f82001bdaaa6d",
                        "name": "Флюоресцентная булка R2-D3",
                        "type": "bun",
                        "proteins": 44,
                        "fat": 26,
                        "carbohydrates": 85,
                        "calories": 643,
                        "price": 988,
                        "image": "https://code.s3.yandex.net/react/code/bun-01.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/bun-01-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/bun-01-large.png",
                        "__v": 0
                    },
                    {
                        "_id": "61c0c5a71d1f82001bdaaa74",
                        "name": "Соус традиционный галактический",
                        "type": "sauce",
                        "proteins": 42,
                        "fat": 24,
                        "carbohydrates": 42,
                        "calories": 99,
                        "price": 15,
                        "image": "https://code.s3.yandex.net/react/code/sauce-03.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/sauce-03-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/sauce-03-large.png",
                        "__v": 0
                    },
                                        {
                        "_id": "61c0c5a71d1f82001bdaaa78",
                        "name": "Кристаллы марсианских альфа-сахаридов",
                        "type": "main",
                        "proteins": 234,
                        "fat": 432,
                        "carbohydrates": 111,
                        "calories": 189,
                        "price": 762,
                        "image": "https://code.s3.yandex.net/react/code/core.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/core-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/core-large.png",
                        "__v": 0
                    }
                ],
                "owner": {
                },
                "status": "done",
                "name": "Альфа-сахаридный традиционный-галактический флюоресцентный бургер",
                "price": 1765
            },
        },
        {
            "success": True,
            "name": "Экзо-плантаго антарианский флюоресцентный бургер",
            "order": {
                "ingredients": [
                    {
                        "_id": "61c0c5a71d1f82001bdaaa6d",
                        "name": "Флюоресцентная булка R2-D3",
                        "type": "bun",
                        "proteins": 44,
                        "fat": 26,
                        "carbohydrates": 85,
                        "calories": 643,
                        "price": 988,
                        "image": "https://code.s3.yandex.net/react/code/bun-01.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/bun-01-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/bun-01-large.png",
                        "__v": 0
                    },
                    {
                        "_id": "61c0c5a71d1f82001bdaaa75",
                        "name": "Соус с шипами Антарианского плоскоходца",
                        "type": "sauce",
                        "proteins": 101,
                        "fat": 99,
                        "carbohydrates": 100,
                        "calories": 100,
                        "price": 88,
                        "image": "https://code.s3.yandex.net/react/code/sauce-01.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/sauce-01-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/sauce-01-large.png",
                        "__v": 0
                    },
                                        {
                        "_id": "61c0c5a71d1f82001bdaaa79",
                        "name": "Мини-салат Экзо-Плантаго",
                        "type": "main",
                        "proteins": 1,
                        "fat": 2,
                        "carbohydrates": 3,
                        "calories": 6,
                        "price": 4400,
                        "image": "https://code.s3.yandex.net/react/code/salad.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/salad-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/salad-large.png",
                        "__v": 0
                    }
                ],
                "owner": {
                },
                "status": "done",
                "name": "Экзо-плантаго антарианский флюоресцентный бургер",
                "price": 5476
            }
        },
        {
            "success": True,
            "name": "Spicy флюоресцентный астероидный бургер",
            "order": {
                "ingredients": [
                    {
                        "_id": "61c0c5a71d1f82001bdaaa6d",
                        "name": "Флюоресцентная булка R2-D3",
                        "type": "bun",
                        "proteins": 44,
                        "fat": 26,
                        "carbohydrates": 85,
                        "calories": 643,
                        "price": 988,
                        "image": "https://code.s3.yandex.net/react/code/bun-01.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/bun-01-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/bun-01-large.png",
                        "__v": 0
                    },
                    {
                        "_id": "61c0c5a71d1f82001bdaaa72",
                        "name": "Соус Spicy-X",
                        "type": "sauce",
                        "proteins": 30,
                        "fat": 20,
                        "carbohydrates": 40,
                        "calories": 30,
                        "price": 90,
                        "image": "https://code.s3.yandex.net/react/code/sauce-02.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/sauce-02-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/sauce-02-large.png",
                        "__v": 0
                    },
                                        {
                        "_id": "61c0c5a71d1f82001bdaaa7a",
                        "name": "Сыр с астероидной плесенью",
                        "type": "main",
                        "proteins": 84,
                        "fat": 48,
                        "carbohydrates": 420,
                        "calories": 3377,
                        "price": 4142,
                        "image": "https://code.s3.yandex.net/react/code/cheese.png",
                        "image_mobile": "https://code.s3.yandex.net/react/code/cheese-mobile.png",
                        "image_large": "https://code.s3.yandex.net/react/code/cheese-large.png",
                        "__v": 0
                    }
                ],
                "owner": {
                },
                "status": "done",
                "name": "Spicy флюоресцентный астероидный бургер",
                "price": 5220
            }
        }   
    ]
    
    INGREDIENTS_HASH_AND_EXPECT_SUITES = [
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус фирменный Space Sauce"], FILLINGS_HASH["Плоды Фалленианского дерева"], EXPECTED_THREE_INGREDIENTS_SUITES[0]),
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус традиционный галактический"], FILLINGS_HASH["Кристаллы марсианских альфа-сахаридов"], EXPECTED_THREE_INGREDIENTS_SUITES[1]),
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус с шипами Антарианского плоскоходца"], FILLINGS_HASH["Мини-салат Экзо-Плантаго"], EXPECTED_THREE_INGREDIENTS_SUITES[2]),
        (ROOLS_HASH["Флюоресцентная булка R2-D3"], SAUCES_HASH["Соус Spicy-X"], FILLINGS_HASH["Сыр с астероидной плесенью"], EXPECTED_THREE_INGREDIENTS_SUITES[3])
    ]