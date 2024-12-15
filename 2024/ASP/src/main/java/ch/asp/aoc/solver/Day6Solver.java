package ch.asp.aoc.solver;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day6Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day6Solver.class);
    int colSpeed = 0;
    int rowSpeed = 0;
    int colPosition = 0;
    int rowPosition = 0;
    char[][] map;
    char[][] obstacles;

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 6 reached");
        map = FileUtil.readCharacterTable(inputPath);
        obstacles = FileUtil.readCharacterTable(inputPath);
        getStartPosition();
        startGuard();

        printMap(map);
        printMap(obstacles);
        logger.info("The guard was on {} fields", countChars(map,'X'));
        logger.info("The guard could be put in a loop by placing a obstacle in {} possible positions", countChars(obstacles,'O'));  
    }

    private void startGuard(){
        markPosition();
        while (!guardIsLeaving()){
            if (getCharOfNextPosition() == '#'){
                turn();
            } else {
                checkForPossibleLoop();
                move();
                markPosition();
            }
        }
        printMap(map);
    }

    private void checkForPossibleLoop(){
        if (obstacles[colPosition+colSpeed][rowPosition+rowSpeed] == 'O' ||
        map[colPosition+colSpeed][rowPosition+rowSpeed] == 'X'
        ) {
            return;
        }

        int initCol = colPosition;
        int initRow = rowPosition;
        int initSpeedCol = colSpeed;
        int initSpeedRow = rowSpeed;
        char originalChar = map[initCol+initSpeedCol][initRow+initSpeedRow];
        map[initCol+initSpeedCol][initRow+initSpeedRow] = '#';

        List<int[]> visitedStates = new ArrayList<>();
        while (!guardIsLeaving()){
            if (getCharOfNextPosition() == '#'){
                turn();
            } else {
                move();
            }
            if(guardAlreadyVisitedSamePosition(visitedStates)){
                obstacles[initCol+initSpeedCol][initRow+initSpeedRow] = 'O';
                break;
            }
            visitedStates.add(new int[]{colPosition, rowPosition, colSpeed, rowSpeed});
        }

        map[initCol+initSpeedCol][initRow+initSpeedRow] = originalChar;
        colPosition = initCol;
        rowPosition = initRow;
        colSpeed = initSpeedCol;
        rowSpeed = initSpeedRow;
    }

    private boolean guardIsLeaving(){
        return (colSpeed == 1 && colPosition == map.length-1) ||
            (colSpeed == -1 && colPosition == 0) ||
            (rowSpeed == 1 && rowPosition == map[0].length-1) ||
            (rowSpeed == -1 && rowPosition == 0);
    }

    private boolean guardAlreadyVisitedSamePosition(List<int[]> visitedStates){
        return visitedStates.stream()
            .anyMatch(
                s -> s[0] == colPosition && 
                s[1] == rowPosition && 
                s[2] == colSpeed && 
                s[3] == rowSpeed);
    }

    private int countChars(char[][] chars, char sign){
        int count = 0;
        for(int row=0; row<chars.length;row++){
            for(int col=0; col<chars[0].length;col++){
                if (chars[col][row] == sign){
                    count++;
                }
            }
        }
        return count;
    }

    private void markPosition(){
        map[colPosition][rowPosition] = 'X';
    }

    private char getCharOfNextPosition(){
        return map[colPosition+colSpeed][rowPosition+rowSpeed];
    }

    private void move(){
        colPosition += colSpeed;
        rowPosition += rowSpeed;
    }

    private void turn(){
        if (colSpeed == 1){
            colSpeed=0;
            rowSpeed=1;
        } else if (rowSpeed == 1){
            colSpeed=-1;
            rowSpeed=0;
        } else if (colSpeed == -1){
            colSpeed=0;
            rowSpeed=-1;
        } else if (rowSpeed == -1){
            colSpeed=1;
            rowSpeed=0;
        }
    }

    private void getStartPosition(){
        for(int row=0; row<map.length;row++){
            for(int col=0; col<map[0].length;col++){
                if (map[col][row] == '^'){
                    colSpeed = 0; 
                    rowSpeed = -1;
                    rowPosition=row;
                    colPosition=col;
                    row=map.length;
                    col=map[0].length;
                } else if (map[col][row] == 'v'){
                    colSpeed = 0;  
                    rowSpeed = 1;
                    rowPosition=row;
                    colPosition=col;
                    row=map.length;
                    col=map[0].length;
                } else if (map[col][row] == '>'){
                    colSpeed = 1;
                    rowSpeed = 0;
                    rowPosition=row;
                    colPosition=col;
                    row=map.length;
                    col=map[0].length;
                }else if (map[col][row] == '<'){
                    colSpeed = -1;
                    rowSpeed = 0;
                    rowPosition=row;
                    colPosition=col;
                    row=map.length;
                    col=map[0].length;
                }
            }
        }
    }

    private void printMap(char[][] chars){
        String number;
        logger.info("");
        logger.info("                                                                                                        111111111111111111111111111111");
        logger.info("              111111111122222222223333333333444444444455555555556666666666777777777788888888889999999999000000000011111111112222222222");
        logger.info("    0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789");
        logger.info("    __________________________________________________________________________________________________________________________________");
        for(int row=0; row<chars.length;row++){
            String newLine = "";
            for(int col=0; col<chars[0].length;col++){
                newLine = newLine+chars[col][row];
            }
            number = String.valueOf(row);
            if (row <10){
                number = "00"+number;
            } else if (row<100){
                number = "0"+number;
            }

            logger.info("{}|{}|",number,newLine);
        }
        logger.info("    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾");
        logger.info("");
    }
}
