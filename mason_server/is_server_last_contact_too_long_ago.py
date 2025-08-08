import datetime
import time

from Server import Server


def is_it(server:Server)->bool:
    now:datetime.datetime = datetime.datetime.now()
    difference:datetime.timedelta = now - server.last_contact
    difference_in_seconds:int = difference.seconds
    
    if difference_in_seconds > 15:
        return True 
    else:
        return False




if __name__ == "__main__":
    test_server = Server("dont_care_about_me", 100, 50, 50)
    time.sleep(65)
    is_it(test_server)