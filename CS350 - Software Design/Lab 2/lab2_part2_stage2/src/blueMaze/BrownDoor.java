package blueMaze;

import java.awt.*;

import maze.*;

public class BrownDoor extends Door {

    public BrownDoor(Room room1, Room room2) {
        super(room1, room2);
    }

    @Override
    public Color getColor() {
        return new Color(150,75,0);	// no brown color
    }

}