class TestData():
    MAIN_URL = "https://stellarburgers.nomoreparties.site"
    CREATE_USER = MAIN_URL + "/api/auth/register"
    
    UNEXIST_REQUIRED_REGISTRATION_FIELD = [{
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
    