from datetime import date,timedelta

tiangan = date(2025,1,5)
dizhi = date(2025,1,7)
tiangan_wenben = {0:"甲",1:"乙",2:"丙",3:"丁",4:"戊",5:"己",6:"庚",7:"辛",8:"壬",9:"癸"}
tiangan_suhxing = {0:"阳木",1:"阴木",2:"阳火",3:"阴火",4:"阳土",5:"阴土",6:"阳金",7:"阴金",8:"阳水",9:"阴水"}
dizhi_wenben = {0:"子",1:"丑",2:"寅",3:"卯",4:"辰",5:"巳",6:"午",7:"未",8:"申",9:"酉",10:"戌",11:"亥"}
dizhi_suxing = {0:"阳水",1:"阴土",2:"阳木",3:"阴木",4:"阳土",5:"阴火",6:"阳火",7:"阴土",8:"阳金",9:"阴金",10:"阳土",11:"阴水"}
with open("shuxing.ics","a",encoding="utf-8") as f:
    f.write("BEGIN:VCALENDAR\n")
    f.write("PRODID:-//frz114514 v1.0//CN\n")
    f.write("VERSION:2.0\n")
    f.write("CALSCALE:GREGORIAN\n")
    f.write("METHOD:PUBLISH\n")
    f.write("X-WR-CALNAME:天干地支\n")
    f.write("X-WR-TIMEZONE:Asia/Shanghai\n")
    f.write("X-WR-CALDESC:脚本更新时间：2025-9-27\n")
    f.write("BEGIN:VTIMEZONE\n")
    f.write("TZID:Asia/Shanghai\n")
    f.write("X-LIC-LOCATION:Asia/Shanghai\n")
    f.write("BEGIN:STANDARD\n")
    f.write("TZOFFSETFROM:+0800\n")
    f.write("TZOFFSETTO:+0800\n")
    f.write("TZNAME:CST\n")
    f.write("DTSTART:19700101T000000\n")
    f.write("END:STANDARD\n")
    f.write("END:VTIMEZONE\n")

def shuxing(time):
    a = [1,2]
    a[0] = ((time - tiangan).days)%10 #0-9
    a[1] = ((time - dizhi).days)%12 #0-11
    return a

def ics_out(out,time):
        with open("shuxing.ics","a",encoding="utf-8") as f:
            f.write("BEGIN:VEVENT\n")
            f.write("DTSTART;VALUE=DATE:{}\n".format(time.strftime("%Y%m%d")))
            f.write("DTEND;VALUE=DATE:{}\n".format((time+timedelta(days=1)).strftime("%Y%m%d")))
            f.write("UID:{}@frz114514\n".format(time.strftime("%Y%m%d")))
            f.write("CREATED:{}T000001\n".format(time.strftime("%Y%m%d")))
            f.write("LAST-MODIFIED:{}T104007\n".format(time.strftime("%Y%m%d")))
            f.write("SUMMARY:{}{}日,{},{}\n".format(tiangan_wenben[out[0]],dizhi_wenben[out[1]],tiangan_suhxing[out[0]],dizhi_suxing[out[1]]))
            f.write("DESCRIPTION:a\n")
            f.write("STATUS:CONFIRMED\n")
            f.write("TRANSP:TRANSPARENT\n")
            f.write("SEQUENCE:1\n")
            f.write("END:VEVENT\n")

def main():
    start_date = date(date.today().year, 2, 1)
    end_date = date(date.today().year+1, 1, 30)
    current_date = start_date
    while current_date <= end_date:
        out = (shuxing(current_date))
        ics_out(out,current_date)
        current_date += timedelta(days=1)

if __name__ == "__main__":
    main()