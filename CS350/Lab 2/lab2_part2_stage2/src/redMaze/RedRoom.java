package redMaze;

import maze.Room;

import java.awt.*;

public class RedRoom extends Room {
//    private Color Red = new Color(255,204,204);
    public RedRoom(int roomNum){
        super(roomNum); //room has private attributes too..
    }

    @Override
    public Color getColor(){
        return new Color(255,204,204);
    }
}
