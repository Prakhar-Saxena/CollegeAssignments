package blueMaze;

import maze.Room;

import java.awt.*;

public class GreenRoom extends Room {
    public GreenRoom(int roomNum){
        super(roomNum); //room has private attributes too..
    }

    @Override
    public Color getColor(){
        return Color.GREEN;
    }
}
