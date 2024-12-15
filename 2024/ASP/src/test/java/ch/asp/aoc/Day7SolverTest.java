package ch.asp.aoc;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

import java.util.List;

import org.junit.jupiter.api.Test;

import ch.asp.aoc.solver.Day7Solver;
import ch.asp.aoc.util.FileUtil;

class Day7SolverTest {
    
    @Test
    void testCheck() {
        Day7Solver solver = new Day7Solver();
        
        java.lang.reflect.Method checkMethod;
        try {
            checkMethod = Day7Solver.class.getDeclaredMethod("check", List.class);
            checkMethod.setAccessible(true);
            List<List<Long>> testCases = FileUtil.readUnevenHorizonalListsAsLong("files/day7.txt");
            
            boolean[] expectedResults = {
                true,
                true,
                false,
                false,
                false,
                false,
                false,
                false,
                true
            };
            
            for (int i = 0; i < testCases.size(); i++) {
                boolean result = (boolean) checkMethod.invoke(solver, testCases.get(i));
                assertEquals(expectedResults[i], result);
            }

            long sum = testCases.stream()
                .filter(list -> {
                    try {
                        return (boolean) checkMethod.invoke(solver, list);
                    } catch (Exception e) {
                        return false;
                    }
                })
                .mapToLong(list -> list.get(0))
                .sum();
            
            assertEquals(3749, sum, "Total calibration sum should be 3749");
            
        } catch (Exception e) {
            fail("Test failed due to exception: " + e.getMessage());
        }
    }
}