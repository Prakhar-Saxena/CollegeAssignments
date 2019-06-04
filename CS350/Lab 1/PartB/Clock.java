public class Clock {
    protected Time currentTime;

    public Clock() {
        currentTime = new Time();
        //currentTime = new Time();
    }

    public Clock(int hours, int minutes, int seconds, String ampm) {
        if(hours > 12 || minutes>59 || seconds>59 || (ampm != "AM" && ampm != "PM") ) {
            return;
        }
        currentTime = new Time(hours, minutes, seconds, ampm);
    }

    public void setCurrentTime(int hours, int minutes, int seconds, String ampm) {
        if(hours > 12 || minutes>59 || seconds>59 || (ampm != "AM" && ampm != "PM") ) {
            return;
        }
        currentTime = new Time(hours, minutes, seconds, ampm);
    }

    public String getCurrentTime() {
        String output = String.format("%02d",currentTime.getHours()) + ":" + String.format("%02d",currentTime.getMinutes()) + ":" + String.format("%02d",currentTime.getSeconds()) + " " + currentTime.getMeridiem();
        return output;
    }

    public String displayCurrentTime() {
        String output = String.format("%02d",currentTime.getHours()) + ":" + String.format("%02d",currentTime.getMinutes()) + ":" + String.format("%02d",currentTime.getSeconds()) + " " + currentTime.getMeridiem();
        System.out.println(output);
        return output;
    }

    public void tick() {
        currentTime.incrementTime();
    }
}