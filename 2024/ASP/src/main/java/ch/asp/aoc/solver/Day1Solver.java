package ch.asp.aoc.solver;

import java.util.HashMap;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;
import ch.asp.aoc.util.SortUtil;

public class Day1Solver implements DaySolver {
    private static final Logger logger = LoggerFactory.getLogger(Day1Solver.class);
    private Map<Integer, Integer> apperancesMap = new HashMap<Integer, Integer>();

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 1 reached");
        int[][] list = FileUtil.readEvenVerticalListsAsInt(inputPath, 2);
        
        SortUtil.sort(list[0]); 
        SortUtil.sort(list[1]);

        logger.info("For part one the diff is {}", getDiff(list[0], list[1]));
        logger.info("For part two the similarity is {}", getSimilarityScore(list[0], list[1]));
    }

    private int getDiff(int[] listA, int[] listB){
        int listSize = listA.length;
        int sum = 0;
        int temp = 0;
        if(listSize != listB.length){
            logger.error("Lists are not the same size list A is {} list B is {}", listSize, listB.length);
            return 0;
        }
        for (int i=0; i< listSize;i++){
            temp = listA[i]-listB[i];
            if (temp < 0){
                temp *= -1;
            }
            sum += temp;
        }
        return sum;
    }

    private int getSimilarityScore(int[] listA, int[] listB){
        int similarity = 0;
        for (int i : listA) {
            similarity += i*getApperances(i, listB);
        }
        return similarity;
    }

    private int getApperances(int val, int[] list){
        Integer apperances = apperancesMap.get(val);

        if (apperances != null){
            return apperances;
        }

        int count = 0;
        for (int i : list) {
            if (i==val){
                count++;
            }
        }
        apperancesMap.put(val, count);
        return count;
    }
}