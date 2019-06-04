package redMaze;

import maze.*;

public class RedMazeFactory extends MazeFactory implements MazeGame{
    public Maze CreateMaze(MazeFactory mazeFactory){
        return mazeFactory.MakeMaze();
    }
//    @Override
    public Wall MakeWall(){
//        RedWall redWall = new RedWall();
        return new RedWall(); //redWall;
    }

//    @Override
    public Room MakeRoom(int roomNum){
        return new RedRoom(roomNum);
    }

//    @Override
    public Door MakeDoor(Room room1, Room room2){
        return new Door(room1, room2);
    }
}
