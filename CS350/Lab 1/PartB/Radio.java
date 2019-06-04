public class Radio {
    boolean isOn;
    int stationFrequency;
    String stationModulation; //either FM or AM
    int volume;

    public Radio() {
        isOn = true;
        stationModulation = "AM";
        stationFrequency = 0;
        volume = 50;
    }

    public Radio(int freq, String mod){
        isOn = true;
        stationModulation = mod;
        stationFrequency = freq;
        volume = 50;
    }

    public String displayRadioStation(){
        if(isOn) {
            String output = stationFrequency + " " + stationModulation;
            System.out.println(output);
            return output;
        }
        else{
            System.out.println("Radio is Off.");
            return null;
        }
    }

    public String getRadioStation(){
        String output = stationFrequency + " " + stationModulation;
        //System.out.println(output);
        return output;
    }

    public void turnOn() {
        isOn = true;
    }

    public void turnOff() {
        isOn = false;
    }

    public void setStation(int freq,String mod) {
        if (freq >= 0){
            stationFrequency = freq;
        }
        else{
            System.out.println("Frequency out of range");
            return;
        }

        if (mod != "AM" && mod != "FM"){
            System.out.println("modulation error");
            return;
        }
        else{
            stationModulation = mod;
        }
    }

    public void setVolume(int v) {
        if (v <= 100 && v >= 0) {
            volume = v;
        }
        else{
            System.out.println("volume value out of range");
            return;
        }
    }
}