package ch.asp.aoc.solver;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day5Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day5Solver.class);
    Map<Integer,List<Integer>> leftToRight = new HashMap<>();
    List<List<Integer>> falseUpdates = new ArrayList<>();

    @Override
    public void solve(String inputPath) {
        logger.info("Solver for Day 5 reached");
        String input = FileUtil.readAsOneString(inputPath);
        
        Pattern pattern = Pattern.compile("\\d{1,2}\\|\\d{1,2}|\\d{1,2}(,\\d{1,2})*");
        Matcher matcher = pattern.matcher(input);

        int sum = 0;
        while(matcher.find()){
            String match = matcher.group(0);
            if (match.charAt(2)=='|'){
                addToHashMap(match);
            } else {
                List<Integer> updates = getUpdateList(match);
                if(isListCorrect(updates)){
                    sum += updates.get((int)((updates.size()-1)/2));
                }
            }
        }
        logger.info("The sum of middle page number of correctly-ordered updates is {}", sum);

        sum =0;
        for (List<Integer> falseUpdate: falseUpdates){
            fixList(falseUpdate);
            sum += falseUpdate.get((int)((falseUpdate.size()-1)/2));
        }
        logger.info("The sum of middle page number of incorrectly-ordered updates after fixing is {}", sum);
    }

    private void addToHashMap(String rule){
        Integer left = Integer.parseInt(rule.substring(0, 2));
        Integer right = Integer.parseInt(rule.substring(3, 5));
        List<Integer> rightList = leftToRight.get(left);

        if(rightList==null){
            rightList = new ArrayList<>();
            leftToRight.put(left, rightList);
        } 
        rightList.add(right);
    }

    private List<Integer> getUpdateList(String updates){
        List<Integer> updateList = new ArrayList<>();
        for (int i = 0; i < updates.length(); i +=3){
            updateList.add(Integer.parseInt(updates.substring(i, i+2)));
        }
        return updateList;
    }

    private boolean isListCorrect(List<Integer> updates){
        for(int i=0;i<updates.size();i++){
            List<Integer>  followingPages = leftToRight.get(updates.get(i));
            for(int j=i+1;j<updates.size();j++){
                if (!followingPages.contains(updates.get(j))){
                    falseUpdates.add(updates);
                    return false;
                }
            }
        } 
        return true;
    }

    private void fixList(List<Integer> updates){
        Map<Integer, Integer> requiredUpdates = new HashMap<>();
        for (Integer update : updates) {
            requiredUpdates.put(update, 0); 
        }

        for (int i = 0; i < updates.size(); i++) {
            List<Integer> followingPages = leftToRight.get(updates.get(i));
            for (Integer follower : followingPages) {
                if (updates.contains(follower)) {
                    requiredUpdates.put(follower, requiredUpdates.get(follower)+1);
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        Queue<Integer> ready = new LinkedList<>();
        
        for (Map.Entry<Integer, Integer> entry : requiredUpdates.entrySet()) {
            if (entry.getValue() == 0) {
                ready.add(entry.getKey());
            }
        }

        while (!ready.isEmpty()) {
            int current = ready.poll();
            result.add(current);

            List<Integer> followers = leftToRight.get(current);
            if (followers != null) {
                for (Integer follower : followers) {
                    if (updates.contains(follower)) {
                        requiredUpdates.put(follower, requiredUpdates.get(follower)-1);
                        if (requiredUpdates.get(follower) == 0) {
                            ready.add(follower);
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < updates.size(); i++) {
            updates.set(i, result.get(i));
        }
    }
}
