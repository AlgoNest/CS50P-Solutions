from datetime import date
import re
import sys
import inflect
def main():
    try:
        year, month, day = correct_format_of_date(input("Date of Birth: "))
    except:
        sys.exit("Invalid Date")

    date_of_birth = date(int(year), int(month), int(day))
    today_date = date.today()
    day = today_date - date_of_birth
    result_in_minute = day.days * 24 * 60
    p = inflect.engine()
    Final_result = p.number_to_words(result_in_minute, andword="")
    print(Final_result.capitalize() + " minutes")






def correct_format_of_date(date):
    #                          year                 month           day
    match = re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",date.strip())
    if match:
        year, month, day = date.split("-")
        return year, month, day

if __name__ == "__main__":
    main()
# 1999-01-01
