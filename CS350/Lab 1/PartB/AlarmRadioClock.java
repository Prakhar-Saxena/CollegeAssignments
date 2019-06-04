public class AlarmRadioClock {
    AlarmClock alarmClock;
    Radio radio;

    public AlarmRadioClock(){
        alarmClock = new AlarmClock();
        radio = new Radio();
    }

    public AlarmRadioClock(int h, int m, int s, String ampm, int alarmH, int alarmM, String alarmAmpm, int freq, String mod){
        alarmClock = new AlarmClock(h,m,s,ampm,alarmH,alarmM,alarmAmpm);
        radio = new Radio(freq, mod);
    }

    public String displayTime(){
        return alarmClock.displayCurrentTime();
    }

    public String displayRadioStation(){
        return radio.displayRadioStation();
    }

    public String displayAlarmTime(){
        return alarmClock.displayAlarmTime();
    }

    public void setTime(int h, int m, int s, String ampm){
        alarmClock.setCurrentTime(h,m,s,ampm);
    }

    public void setAlarmTime(int h, int m, String ampm){
        alarmClock.setAlarmTime(h,m,ampm);
    }

    public void turnOffAlarm(){
        alarmClock.stopAlarm();
    }

    public void snoozeAlarm(){
        alarmClock.snooze();
    }

    public void checkAlarm(){
        String newAlarmString = "The radio is playing " + radio.getRadioStation();
        alarmClock.setAlarmString(newAlarmString);
        alarmClock.checkAlarm();
    }

    public void setRadioStation(int freq, String mod){
        radio.setStation(freq, mod);
    }

    public void setVolume(int v){
        radio.setVolume(v);
    }

    public void turnOnRadio(){
        radio.turnOn();
    }

    public void turnOffRadio(){
        radio.turnOff();
    }

    public void tick(){
        alarmClock.tick();
    }
}
