package ch.asp.aoc.solver;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day16Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day16Solver.class);

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 16 reached");
        List<List<Integer>> list = FileUtil.readUnevenHorizonalListsAsInt(inputPath);
        logger.info("list loaded: {}", list);
    }
}
