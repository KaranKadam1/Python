import time
from plyer import notification

if __name__== "__main__":

    while True:

        notification.notify(

            title="Please drink water karan!!",
            
            message="The national academies of science, Engineering, and Medicine determined that an adequete daily fluid intake is: About 15.5 Cups(3.7 liters) of fluids a day for a men.",


            timeout=3
        )
        time.sleep(1)
