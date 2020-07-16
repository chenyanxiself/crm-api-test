from third_auth.main import Main_third_jurisdiction
from seconde_auth.main import Main_two_jurisdiction
from data_auth.data_three_main import Main_Permission_three_domain
from data_auth.data_two_main  import Main_Permission_two_domain


if __name__ =='__main__':
    Main_third_jurisdiction().start()
    Main_two_jurisdiction().start()
    Main_Permission_three_domain().start()
    Main_Permission_two_domain().start()