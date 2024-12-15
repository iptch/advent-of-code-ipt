package ch.asp.aoc.solver;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day4Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day4Solver.class);

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 4 reached");
        char[][] chars = FileUtil.readCharacterTable(inputPath);
        int counter = 0;

        for (int i=0;i<chars.length;i++){
            for (int j=0;j<chars[0].length;j++){
                if (chars[i][j] == 'X'){
                    if (i<chars.length-3 && chars[i+1][j] == 'M' && chars[i+2][j] == 'A' && chars[i+3][j] == 'S'){
                        counter++;
                    }
                    if (j<chars[0].length-3 && chars[i][j+1] == 'M' && chars[i][j+2] == 'A' && chars[i][j+3] == 'S' ){
                        counter++;
                    }
                    if (i<chars.length-3 && j<chars[0].length-3 && chars[i+1][j+1] == 'M' && chars[i+2][j+2] == 'A' && chars[i+3][j+3] == 'S'){
                        counter++;
                    }
                    if (i>=3 && chars[i-1][j] == 'M' && chars[i-2][j] == 'A' && chars[i-3][j] == 'S'){
                        counter++;
                    }
                    if (j>=3 && chars[i][j-1] == 'M' && chars[i][j-2] == 'A' && chars[i][j-3] == 'S'){
                        counter++;
                    }
                    if (i>=3 && j>=3 && chars[i-1][j-1] == 'M' && chars[i-2][j-2] == 'A' && chars[i-3][j-3] == 'S'){
                        counter++;
                    }
                    if (j>=3 && i<chars.length-3 && chars[i+1][j-1] == 'M' && chars[i+2][j-2] == 'A' && chars[i+3][j-3] == 'S'){
                        counter++;
                    }
                    if (i>=3 && j<chars[0].length-3 && chars[i-1][j+1] == 'M' && chars[i-2][j+2] == 'A' && chars[i-3][j+3] == 'S'){
                        counter++;
                    }
                } 
            }
        }

        logger.info("For the first part the number of XMAS is {}", counter);
        
        counter = 0;
        for (int i=1;i<chars.length-1;i++){
            for (int j=1;j<chars[0].length-1;j++){
                if (chars[i][j] == 'A' &&
                    ((chars[i+1][j+1] == 'M' && chars[i-1][j-1] == 'S') || (chars[i+1][j+1] == 'S' && chars[i-1][j-1] == 'M')) && 
                    ((chars[i+1][j-1] == 'M' && chars[i-1][j+1] == 'S') || (chars[i+1][j-1] == 'S' && chars[i-1][j+1] == 'M'))){
                    counter++;
                } 
            }
        }
        logger.info("For the second part the number of X-MAS is {}", counter);
    }
}
