package ch.asp.aoc.solver;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day7Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day7Solver.class);

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 7 reached");
        List<List<Long>> lists = FileUtil.readUnevenHorizonalListsAsLong(inputPath);
        Long sum = (long)0;
        
        for(List<Long> list : lists){
            if (check(list)){
                sum += list.get(0);
            }
        }

        logger.info("The sum of all correct calibrations is {}", sum);
    }

    private boolean check(List<Long> list) {
        Long calibration = list.get(0);
        List<Long> subResults = new ArrayList<>();
        subResults.add(list.get(1));

        for(int i=2; i<list.size(); i++) {
            List<Long> newResults = new ArrayList<>();
            for(Long subResult : subResults) {
                newResults.add(subResult * list.get(i));
                newResults.add(subResult + list.get(i));
                newResults.add(Long.valueOf(subResult.toString().concat(list.get(i).toString())));
            }
            subResults = newResults;
        }
        return subResults.contains(calibration);
    }
}
