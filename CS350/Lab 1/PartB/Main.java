public class Main {
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        int i;
        int seconds;
        AlarmRadioClock myClock = new AlarmRadioClock(8, 0,0, "AM", 8, 5, "AM", 1060, "AM");
        myClock.displayAlarmTime();
        myClock.displayTime();
        for (i = 0; i < 5; i++) {
            System.out.print("Time: ");
            myClock.displayTime();
            for (seconds = 0; seconds < 60; seconds++) {
                myClock.checkAlarm();
                myClock.tick();
            }
            myClock.checkAlarm();
        }

        myClock.snoozeAlarm();

        for(i = 0; i < 9; i++) {
            System.out.print("Time: ");
            myClock.displayTime();
            for(seconds = 0; seconds < 60; seconds++) {
                myClock.checkAlarm();
                myClock.tick();
            }
        }
    }
}
