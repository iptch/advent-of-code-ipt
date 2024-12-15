package ch.asp.aoc;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.solver.Day10Solver;
import ch.asp.aoc.solver.Day11Solver;
import ch.asp.aoc.solver.Day12Solver;
import ch.asp.aoc.solver.Day13Solver;
import ch.asp.aoc.solver.Day14Solver;
import ch.asp.aoc.solver.Day15Solver;
import ch.asp.aoc.solver.Day16Solver;
import ch.asp.aoc.solver.Day17Solver;
import ch.asp.aoc.solver.Day18Solver;
import ch.asp.aoc.solver.Day19Solver;
import ch.asp.aoc.solver.Day1Solver;
import ch.asp.aoc.solver.Day20Solver;
import ch.asp.aoc.solver.Day21Solver;
import ch.asp.aoc.solver.Day22Solver;
import ch.asp.aoc.solver.Day23Solver;
import ch.asp.aoc.solver.Day24Solver;
import ch.asp.aoc.solver.Day25Solver;
import ch.asp.aoc.solver.Day2Solver;
import ch.asp.aoc.solver.Day3Solver;
import ch.asp.aoc.solver.Day4Solver;
import ch.asp.aoc.solver.Day5Solver;
import ch.asp.aoc.solver.Day6Solver;
import ch.asp.aoc.solver.Day7Solver;
import ch.asp.aoc.solver.Day8Solver;
import ch.asp.aoc.solver.Day9Solver;
import ch.asp.aoc.solver.DaySolver;

public class AdventOfCode {
    private static final Logger logger = LoggerFactory.getLogger(AdventOfCode.class);
    
    public static void main(String[] args) {
        logger.info("Advent of Code class started");
        int dayInt = 10;
        DaySolver day = new Day1Solver();

        if (dayInt==2){
            day = new Day2Solver();
        } else if (dayInt==3){
            day = new Day3Solver();
        } else if (dayInt==4){
            day = new Day4Solver();
        } else if (dayInt==5){
            day = new Day5Solver();
        } else if (dayInt==6){
            day = new Day6Solver();
        } else if (dayInt==7){
            day = new Day7Solver();
        } else if (dayInt==8){
            day = new Day8Solver();
        } else if (dayInt==9){
            day = new Day9Solver();
        } else if (dayInt==10){
            day = new Day10Solver();
        } else if (dayInt==11){
            day = new Day11Solver();
        } else if (dayInt==12){
            day = new Day12Solver();
        } else if (dayInt==13){
            day = new Day13Solver();
        } else if (dayInt==14){
            day = new Day14Solver();
        } else if (dayInt==15){
            day = new Day15Solver();
        } else if (dayInt==16){
            day = new Day16Solver();
        } else if (dayInt==17){
            day = new Day17Solver();
        } else if (dayInt==18){
            day = new Day18Solver();
        } else if (dayInt==19){
            day = new Day19Solver();
        } else if (dayInt==20){
            day = new Day20Solver();
        } else if (dayInt==21){
            day = new Day21Solver();
        } else if (dayInt==22){
            day = new Day22Solver();
        } else if (dayInt==23){
            day = new Day23Solver();
        } else if (dayInt==24){
            day = new Day24Solver();
        } else if (dayInt==25){
            day = new Day25Solver();
        } 
        
        day.solve("files/day"+dayInt+".txt");
    }
}
