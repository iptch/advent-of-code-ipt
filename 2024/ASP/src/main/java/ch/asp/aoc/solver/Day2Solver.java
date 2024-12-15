package ch.asp.aoc.solver;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day2Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day2Solver.class);

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 2 reached");
        List<List<Integer>> list = FileUtil.readUnevenHorizonalListsAsInt(inputPath);
    
        logger.info("For part one the number of safe reports are {}", getNumberOfSafeReports(list));
        logger.info("For part two the number of safe reports are {}", getNumberOfSafeReportsWithDampener(list));
    }

    private int getNumberOfSafeReports(List<List<Integer>> list){
        int safeReports = 0;
        for (List<Integer> levels : list) {
            if (isSafe(levels,1,3) || isSafe(levels, -3, -1)){
                safeReports++;
            } 
        }
        return safeReports;
    }

    private int getNumberOfSafeReportsWithDampener(List<List<Integer>> list) {
        int safeReports = 0;
        for (List<Integer> levels : list) {
            if (isSafe(levels,1,3) || isSafe(levels, -3, -1)){
                safeReports++;
            } else {
                for (int i=0;i<levels.size();i++){
                    List<Integer> smallerList = new ArrayList<>(levels);
                    smallerList.remove(i); 
                    if (isSafe(smallerList,1,3) || isSafe(smallerList, -3, -1)){
                        safeReports++;
                        i = levels.size();
                    }
                }
            }
        }
        return safeReports;
    }


    private boolean isSafe(List<Integer> levels, int low, int high){
        int left = levels.get(0);
        int right = levels.get(1);
        if (left-right >= low && left-right <= high){
            left = right;
            for (int i=2;i<levels.size();i++) {
                right = levels.get(i);
                if (left-right < low || left-right > high){
                    return false;
                }
                left = right;
            }
            return true;
            
        }
        return false;
    }
}
