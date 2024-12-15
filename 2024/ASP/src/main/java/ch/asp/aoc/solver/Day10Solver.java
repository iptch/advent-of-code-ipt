package ch.asp.aoc.solver;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day10Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day10Solver.class);
    int[][] map;
    int maxRow;
    int maxCol;
    boolean isPartTwo = true;

    Map<Integer[], List<int[]>> reachedPeaks = new HashMap<>();

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 10 reached");
        map = FileUtil.readIntegerTable(inputPath);

        int sum = 0;

        maxCol = map.length;
        maxRow = map[0].length;

        for (int col=0;col<maxCol;col++){
            for (int row=0;row<maxRow;row++){
                if (map[col][row] == 0){
                    Integer[] start = new Integer[]{col,row};
                    sum = checkAdjustin(start,col,row,0,sum);
                }
            }
        }
        logger.info("There are {} paths", sum);
    }

    private int checkAdjustin(Integer[] start, int col, int row, int currentHeight, int sum){
        if (col+1>=0 && row>=0 && col+1<maxCol && row<maxRow&&map[col+1][row] == currentHeight+1){
            if (currentHeight == 8){
                sum = getSum(start, col+1,row, sum);
            } else{
                sum = checkAdjustin(start, col+1, row, currentHeight+1,sum);
            } 
        }
        if (col>=0 && row+1>=0 && col<maxCol && row+1<maxRow && map[col][row+1] == currentHeight+1){
            if (currentHeight == 8){
                sum = getSum(start, col,row+1, sum);
            } else{
                sum = checkAdjustin(start, col, row+1, currentHeight+1,sum);
            } 
        }

        if (col-1>=0 && row>=0 && col-1<maxCol && row<maxRow && map[col-1][row] == currentHeight+1){
            if (currentHeight == 8){
                sum = getSum(start, col-1,row, sum);
            } else{
                sum = checkAdjustin(start, col-1, row, currentHeight+1,sum);
            } 
        }

        if (col>=0 && row-1>=0 && col<maxCol && row-1<maxRow && map[col][row-1] == currentHeight+1){
            if (currentHeight == 8){
                sum = getSum(start, col,row-1, sum);
            } else{
                sum = checkAdjustin(start, col, row-1, currentHeight+1,sum);
            } 
        }
        return sum;
    }


    private int getSum(Integer[] start, int col, int row, int sum){
        if (!isPartTwo) {
            List<int[]> reached = reachedPeaks.get(start);

            if (reached == null){
                reached = new ArrayList<>();
            }
            int[] currentPeak = new int[]{col,row};
    
            for (int[] rechedPeak : reached){
                if (rechedPeak[0] == col && rechedPeak[1] == row){
                    return sum;
                }
            }
    
            reached.add(currentPeak);
            reachedPeaks.put(start, reached);
        }
        
        return sum+1;
    }
}
