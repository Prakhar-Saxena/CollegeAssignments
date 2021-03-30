package maze;

public interface MazeGame {
    public Maze CreateMaze(MazeFactory mazeFactory);
    public Maze loadMaze(MazeFactory mazeFactory, String path);
}
