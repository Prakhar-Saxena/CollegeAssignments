public class AlarmClock extends Clock{
    protected boolean isOn;
    protected Time alarmTime;
    protected Time snoozeAlarmTime;
    protected boolean isBuzzing; // true if alarm goes off
    protected boolean snoozed;
    protected String alarmString = "BUZZ, BUZZ, BUZZ";

    public AlarmClock(){
        isOn = true;
        alarmTime = new Time();
        isBuzzing = false;
        snoozed = false;
    }

    public AlarmClock(int h, int m, int s, String ampm, int alarmH, int alarmM, String alarmAmpm) {
        alarmTime = new Time(alarmH, alarmM, alarmAmpm);
        snoozeAlarmTime = alarmTime;
        currentTime = new Time(h, m, s, ampm);
        isOn = true;
        isBuzzing = false;
        snoozed = false;
        checkAlarm();
    }

    public Time getAlarmTime(){
        return alarmTime;
    }

    public Time getSnoozeAlarmTime(){
        return snoozeAlarmTime;
    }

    public void setAlarmTime(int h, int m, String ampm) {
        isOn = true;
        alarmTime = new Time(h, m, ampm);
    }

    public boolean isSnoozed(){
        return snoozed;
    }

    public String getAlarmString(){
        return alarmString;
    }

    public void setAlarmString(String str){
        alarmString = str;
    }

    public boolean checkAlarm() {
        //System.out.print(currentTime.isEqualTo(alarmTime));
        if (isSnoozed()){
            if(currentTime.isEqualTo(snoozeAlarmTime)) {
                isBuzzing = true;
                System.out.println(alarmString);

                return true;
            }
            else {
                return false;
            }
        }
        else{
            if(currentTime.isEqualTo(alarmTime)) {
                isBuzzing = true;
                System.out.println(alarmString);
                return true;
            }
            else {
                return false;
            }
        }

    }

    public void snooze() { //9 minute snooze
        isBuzzing = false;
        snoozed = true;
        snoozeAlarmTime = alarmTime;
        snoozeAlarmTime.addMinutes(9);
        checkAlarm();
    }

    public void stopAlarm(){
        isBuzzing = false;
        snoozed = false;
        snoozeAlarmTime = alarmTime;
    }

    public String displayAlarmTime(){
        String output = String.format("%02d",alarmTime.getHours()) + ":" + String.format("%02d",alarmTime.getMinutes()) + ":" + String.format("%02d",alarmTime.getSeconds()) + " " + alarmTime.getMeridiem();
        System.out.println(output);
        return output;
    }
}