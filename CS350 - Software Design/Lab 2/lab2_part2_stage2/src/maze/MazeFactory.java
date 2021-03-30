/*
 * SimpleMazeGame.java
 * Copyright (c) 2008, Drexel University.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Drexel University nor the
 *       names of its contributors may be used to endorse or promote products
 *       derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY DREXEL UNIVERSITY ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL DREXEL UNIVERSITY BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */
package maze;

import blueMaze.BlueMazeFactory;
import maze.ui.MazeViewer;
import redMaze.RedMazeFactory;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

import static maze.Direction.East;
import static maze.Direction.West;
import static maze.Direction.North;
import static maze.Direction.South;

/**
 * 
 * @author Sunny
 * @version 1.0
 * @since 1.0
 */
public class MazeFactory implements MazeGame
{
	/**
	 * Creates a small maze.
	 */
	public Maze createMaze(MazeFactory mazeFactory)
	{

		Maze maze = new Maze();
		Room room0 = new Room(0);
		Room room1 = new Room(1);
		Wall wall = new Wall();



		room0.setSide(North, wall);
		room0.setSide(South, wall);
		room0.setSide(West,wall);

		room1.setSide(North, wall);
		room1.setSide(South, wall);
		room1.setSide(East, wall);

		Door door01 = new Door(room0, room1);

		room0.setSide(East, door01);
		room1.setSide(West, door01);

		maze.addRoom(room0);
		maze.addRoom(room1);
		maze.setCurrentRoom(0);
//		System.out.println("The maze does not have any rooms yet!");
		return maze;
	}

//	public static MapSite strToMapSite(String str){
//		switch (str){
//			case "wall":
//				Wall wall = new Wall();
//				return wall;
//			case "south":
//				return South;
//			case "East":
//				return East;
//			case "West":
//				return West;
//			default:
//				System.out.println("incorrect direction string entered");
//		}
//	}

	public Maze loadMaze(MazeFactory mazeFactory, final String path)
	{
		try {
			//MazeFactory mazeGameCreator = new MazeFactory();
			Maze maze = mazeFactory.MakeMaze();
			File file = new File(path);
			Scanner scanner = new Scanner(file);
			ArrayList<String> fileContent = new ArrayList<String>();
			ArrayList<Room> rooms = new ArrayList<Room>();
			ArrayList<Door> doors = new ArrayList<Door>();
            HashMap<Room, ArrayList<String>> roomSideElements = new HashMap<Room,ArrayList<String>>();
            //HashMap<Door, ArrayList<String>> doorSideElements = new HashMap<Door,ArrayList<String>>(); //thought I'd need it, but didn't. the ArrayList works fine.
            Direction[] directions = {North,South,East,West};

            while (scanner.hasNextLine()) {
                fileContent.add(scanner.nextLine());
            }

			for (String line : fileContent) {
				String[] parts = line.split(" ");
				if(parts.length<2){
					break;
				}
				String numString = parts[1];
				if (parts[0].equals("room")) {
					int num = Integer.parseInt(numString);
					ArrayList<String> siteInDirections = new ArrayList<String>(); //Arrays.copyOfRange(parts,3,parts.length);
					for (int i = 2; i <= 5; i++) {
						siteInDirections.add(parts[i]);
					}
					Room room = mazeFactory.MakeRoom(num);
					roomSideElements.put(room, siteInDirections);
					rooms.add(room);
				}
			}
			for (String line : fileContent) { // have to do this twice so that I can reference rooms added to doors
				String[] parts = line.split(" ");
				if(parts.length<2){
					break;
				}
				String numString = parts[1];
				if (parts[0].equals("door")) {
//					int doorNum = Integer.parseInt(parts[1]);
					int room1Num = Integer.parseInt(parts[2]);
					int room2Num = Integer.parseInt(parts[3]);
//					Room room1, room2;
//					for(Room room : rooms){
//						if(room.getNumber() == room1Num){
//							room1 = room;
//						}
//						else if(room.getNumber() == room2Num){
//							room2 = room;
//						}
//					}
					Door door = mazeFactory.MakeDoor(rooms.get(room1Num), rooms.get(room2Num));
					if (parts[4].equals("close")) {
						door.setOpen(false);
					} else if (parts[4].equals("open")) {
						door.setOpen(true);
					}
					doors.add(door);
				}
			}
			for (Room room: rooms) {
				ArrayList<String> sideElements = new ArrayList<String>();
				sideElements = roomSideElements.get(room);
				for(int i = 0; i < directions.length; i++){
					String sideElement = sideElements.get(i);

					if(sideElement.equals("wall")){
						room.setSide(directions[i],mazeFactory.MakeWall());
					}
					else if(sideElement.substring(0,1).equals("d")){
						int doorNum = Integer.parseInt(sideElement.substring(1));
						Door door = doors.get(doorNum);
						room.setSide(directions[i],door);
					}
					else{
						Room otherRoom = rooms.get(Integer.parseInt(sideElement));
						room.setSide(directions[i],otherRoom);
					}
				}
				maze.addRoom(room);
			}
			maze.setCurrentRoom(0);
			return maze;
//                String roomOrDoor = parts[0];
//                String numString = (parts[1]);
//                int num = Integer.parseInt(numString);
//                String[] directions = Arrays.copyOfRange(parts, 3, parts.length);
//                ArrayList<MapSite> directionElements = new ArrayList<MapSite>();

//				for (String dir: directions) {
//					switch (dir){
//						case "wall":
//							Wall wall = new Wall();
//							directionElements.add(wall);
//							break;
//							case ""
//					}
//				}
//                String north = parts[2];
//                String south = parts[3];
//                String east = parts[4];
//                String west = parts[5];
//                switch (roomOrDoor) {
//                    case "room":
//                        Room room = new Room(num);
//                        room.setSide(North, north);
//                        break;
//                }
//                Room room = new Room(num);



//			Maze maze = new Maze();
//			System.out.println("Please load a maze from the file!");
//			return maze;
		}
		catch (FileNotFoundException e){
			System.out.println("File Not Found.");
			return null;
		}
	}

	public Maze CreateMaze(MazeFactory mazeFactory){
		return mazeFactory.MakeMaze();
	}

	public Maze MakeMaze(){
		return new Maze();
	}

	public Wall MakeWall(){
		return new Wall();
	}

	public Door MakeDoor(Room room1, Room room2){
		return new Door(room1, room2);
	}

	public Room MakeRoom(int roomNum){
		return new Room(roomNum);
	}

	public static void main(String[] args)
	{
		String path = "./mazes/";
		MazeGame mazeGame = new MazeFactory();
		MazeFactory mazeFactory = null;
		Maze maze = null;//mazeFactory.CreateMaze(mazeFactory);


		if(args.length >= 1) {
			switch (args[1]) {
				case "red":
					mazeFactory = new RedMazeFactory();
					maze = mazeGame.CreateMaze(new RedMazeFactory());
					break;
				case "blue":
					mazeFactory = new BlueMazeFactory();
					maze = mazeGame.CreateMaze(new BlueMazeFactory());
					break;
				default:
					mazeFactory = new MazeFactory();
					maze = mazeGame.CreateMaze(new MazeFactory());
					break;
			}

//			System.out.println(args[0]);

//		Maze maze = createMaze();

			if (args.length > 1) {
				path += args[0];
				maze = mazeGame.loadMaze(mazeFactory, path);
			}
			else{
				maze = mazeGame.CreateMaze(new MazeFactory());
			}
		}
		MazeViewer mazeViewer = new MazeViewer(maze);
		mazeViewer.run();
//		Maze largeMaze = loadMaze("./src/maze/mazes/large.maze");
//		Maze smallMaze = loadMaze("./src/maze/mazes/small.maze");

//		MazeViewer largeMazeViewer = new MazeViewer(largeMaze);
//		MazeViewer smallMazeViewer = new MazeViewer(smallMaze);
//	    largeMazeViewer.run();
//	    smallMazeViewer.run();
	}
}
