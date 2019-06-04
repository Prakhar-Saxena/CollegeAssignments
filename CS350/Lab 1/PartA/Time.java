public class Time {
    protected int hours;
    protected int minutes;
    protected int seconds;
    protected String meridiem;

    public Time() {
        hours = 0;
        minutes = 0;
        seconds = 0;
        meridiem = "AM";
    }

    public Time(int h, int m, int s, String ampm) {
        hours = h;
        minutes = m;
        seconds = s;
        if(ampm != "AM" && ampm != "PM")
            System.out.print("error");
        else
            meridiem = ampm;

    }

    public Time(int h, int m, String ampm) {
        hours = h;
        minutes = m;
        seconds = 0;
        if(ampm != "AM" && ampm != "PM")
            System.out.print("error");
        else
            meridiem = ampm;
    }

    public int getHours() {
        return hours;
    }

    public int getMinutes() {
        return minutes;
    }

    public int getSeconds() {
        return seconds;
    }

    public String getMeridiem() {
        return meridiem;
    }

    public void setHours(int h){
        if(h>12)
            return;
        else
            hours = h;
    }

    public void setMinutes(int m){
        if(m>=60)
            return;
        else
            minutes = m;
    }

    public void setSeconds(int s){
        if(s>=60)
            return;
        else
            seconds = s;
    }

    public void setMeridiem(String ampm){
        if(ampm != "AM" && ampm != "PM")
            return;
        else
            meridiem = ampm;
    }

    public void incrementTime() {
        seconds++;
        if(seconds == 60) {
            minutes++;
            seconds = 0;
        }
        if(minutes == 60) {
            hours++;
            minutes = 0;
        }
        if(hours == 13) {
            meridiem = (meridiem=="AM")?"PM":"AM";
            hours = 1;
        }
    }

    public void addMinutes(int m){
        if(m>=60)
            return;
        minutes += m;
        if(minutes >= 60){
            hours += (int) (minutes/60);
            minutes += ((int) (minutes/60));
        }
        if(hours == 13) {
            meridiem = (meridiem=="AM")?"PM":"AM";
            hours = 1;
        }
    }

    public void addTime(Time newTime){
        seconds += newTime.getSeconds();
        if(seconds >= 60){
            minutes += (int) (seconds/60);
            seconds -= ((int) (seconds/60));
        }
        if(minutes >= 60){
            hours += (int) (minutes/60);
            minutes += ((int) (minutes/60));
        }
        if(hours > 12){
            //dunno do something..
        }
    }

    public boolean isEqualTo(Time time2){
        if(hours == time2.getHours() && minutes == time2.getMinutes() && meridiem == time2.getMeridiem())
            return true;
        else
            return false;
//        int compare1 = (hours*60*60) + (minutes*60) + seconds + (meridiem=="PM"?(12*60*60):0);
//        int compare2 = (time2.getHours()*60*60) + (time2.getMinutes()*60) + (time2.getSeconds()) + (time2.getMeridiem()=="PM"?(12*60*60):0);
//        return compare1>=compare2?true:false;
    }
}