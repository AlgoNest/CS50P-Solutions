def main():
        c_time=input("what time is it?")
        time=convert(c_time)
        msg=f_time(time)
        print(msg)

def f_time(time):
        if time >= 7 and time <= 8:
                return"breakfast time"

        elif time >= 12 and time <= 13:
                return"lunch time"

        elif time >= 18 and time <= 19:
                return"dinner time"


def convert(time):
        hours,minutes=time.split(":")
        n_minutes=float(minutes)/60
        return float(hours)+n_minutes

if __name__=="__main__":
 main()
