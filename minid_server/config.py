class Config(object):
    DEBUG = True
    TESTING = True
    
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/minid.db"

    HOSTNAME = "http://localhost:5000/"
    LANDING_PAGE = "http://localhost:5000/minid/landingpage"

    EZID_SERVER =  "https://ezid.cdlib.org"
    EZID_SCHEME = "ark:/"
    EZID_SHOULDER = "99999/fk4"
    EZID_USERNAME = "apitest"
    EZID_PASSWORD = "apitest"

    SERVICE_TOKENS = ['']


    TEST_EZID_SERVER =  "https://ezid.cdlib.org"
    TEST_EZID_SCHEME = "ark:/"
    TEST_EZID_SHOULDER = "99999/fk4"
    TEST_EZID_USERNAME = "apitest"
    TEST_EZID_PASSWORD = "apitest"

    AWS_ACCESS_KEY_ID = ""
    AWS_SECRET_ACCESS_KEY = ""


