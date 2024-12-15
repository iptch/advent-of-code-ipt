package ch.asp.aoc.solver;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day3Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day3Solver.class);

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 3 reached");
        String input = FileUtil.readAsOneString(inputPath);
        
        Pattern pattern = Pattern.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)|do\\(\\)|don't\\(\\)");
        Matcher matcher = pattern.matcher(input);

        int result = 0;
        int resultActive = 0;
        boolean isActive = true;

        while(matcher.find()){
            String match = matcher.group(0);
            if (match.startsWith("do(")){
                isActive=true;
            } else if (match.startsWith("don")){
                isActive=false;
            } else {
                int mul = Integer.parseInt(matcher.group(1))*Integer.parseInt(matcher.group(2));
                result += mul;
                if (isActive){
                    resultActive += mul;
                }
            }
        }

        logger.info("The total of the multiplications are {}", result);
        logger.info("The total of active multiplications are {}", resultActive);
    }
}
