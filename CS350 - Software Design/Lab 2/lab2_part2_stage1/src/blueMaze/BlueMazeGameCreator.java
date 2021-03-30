package blueMaze;

import maze.*;

public class BlueMazeGameCreator extends MazeGameCreator{
//    @Override
    public Wall MakeWall(){
//        BlueWall blueWall = new BlueWall();
        return new BlueWall(); // blueWall;
    }

//    @Override
    public Room MakeRoom(int roomNum){
        return new GreenRoom(roomNum);
    }

//    @Override
    public Door MakeDoor(Room room1, Room room2){
        return new BrownDoor(room1, room2);
    }
}
