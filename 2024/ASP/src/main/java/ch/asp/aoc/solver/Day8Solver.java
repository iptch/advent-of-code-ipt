package ch.asp.aoc.solver;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day8Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day8Solver.class);
    Map<Character,List<int[]>> nodes = new HashMap<>();
    List<int[]> antinodes = new ArrayList<>();
    int colMax = 0;
    int rowMax = 0;

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 8 reached");
        char[][] map = FileUtil.readCharacterTable(inputPath);
        loadMap(map);
        findAntinodes();
        logger.info("There are {} unique antinodes", countAntinodes());
    }

    private int countAntinodes(){
        int count = 0;
        for (int[] antinode : antinodes){
            if(antinode[0]>=0 && antinode[0]<=colMax && antinode[1]>=0 && antinode[1]<=rowMax){
                count++;
            }
        }
        return count;
    }

    private void findAntinodes(){
        for (Entry<Character, List<int[]>> entry : nodes.entrySet()) {
            List<int[]> antennas = entry.getValue();
            for (int i=0; i<antennas.size(); i++){
                for (int j=i+1; j<antennas.size(); j++){
                    int[] antennaA = antennas.get(i);
                    int[] antennaB = antennas.get(j);

                    int diffCol = antennaA[0] - antennaB[0];
                    int diffRow = antennaA[1] - antennaB[1];

                    int firstCol = antennaA[0];
                    int firstRow = antennaA[1];

                    int secondCol = antennaB[0];
                    int secondRow = antennaB[1];

                    boolean exists = false;
                    while(firstCol>=0 && firstCol <= colMax && firstRow>=0 && firstRow <= rowMax){
                        exists = false;
                        for (int[] entires : antinodes){
                            if (entires[0]==firstCol && entires[1]==firstRow){
                                exists=true;
                            }
                        }
    
                        if (!exists){
                            antinodes.add(new int[]{firstCol,firstRow});
                        }
                        firstCol += diffCol;
                        firstRow += diffRow;
                    }

                    while(secondCol>=0 && secondCol <= colMax && secondRow>=0 && secondRow <= rowMax){
                        exists = false;
                        for (int[] entires : antinodes){
                            if (entires[0]==secondCol && entires[1]==secondRow){
                                exists=true;
                            }
                        }
    
                        if (!exists){
                            antinodes.add(new int[]{secondCol,secondRow});
                        }
                        secondCol -= diffCol;
                        secondRow -= diffRow;
                    }
                }
            }

        }
    }

    private void loadMap(char[][] map){
        colMax = map.length-1;
        rowMax = map[0].length-1;
        for (int col=0;col< map.length;col++){
            for (int row=0;row< map[0].length;row++){
                if (Character.isLetter(map[col][row]) || Character.isDigit(map[col][row])){
                    List<int[]> list = nodes.get(map[col][row]);
                    if (list == null){
                        list = new ArrayList<>();
                    }
                    list.add(new int[]{col,row});
                    nodes.put(map[col][row], list);
                }
            }
        }
    }
}
