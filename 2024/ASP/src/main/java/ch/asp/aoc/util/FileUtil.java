package ch.asp.aoc.util;

import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class FileUtil {
    private static final Logger logger = LoggerFactory.getLogger(FileUtil.class);

    public static int[][] readEvenVerticalListsAsInt(String path, int numberOfLists) {
        List<String> lines = readLines(path);
        int[][] lists = new int[numberOfLists][lines.size()];
        int lineNumber = 0;

        for (String line : lines) {
            String[] items = line.trim().split("\\s+");
            for(int i=0;i<numberOfLists;i++){
                lists[i][lineNumber] =Integer.parseInt(items[i]);
            }
            lineNumber++;
        }
        logger.info("Created {} int lists with {} entries each", numberOfLists, lineNumber);
        return lists;
    }

    public static List<List<Integer>> readUnevenHorizonalListsAsInt(String path) {
        List<List<Integer>> list = new ArrayList<>();
        List<String> lines = readLines(path);
        for (String line : lines) {
            String[] items = line.trim().split("[^0-9]+");
            List<Integer> row = new ArrayList<>();
            for(int i=0;i<items.length;i++){
                row.add(Integer.parseInt(items[i]));
            }
            list.add(row);
        }
        logger.info("Created list of list with {} Integer lists", list.size());
        return list;
    }

    public static List<List<Long>> readUnevenHorizonalListsAsLong(String path) {
        List<List<Long>> list = new ArrayList<>();
        List<String> lines = readLines(path);
        for (String line : lines) {
            String[] items = line.trim().split("[^0-9]+");
            List<Long> row = new ArrayList<>();
            for(int i=0;i<items.length;i++){
                row.add(Long.parseLong(items[i]));
            }
            list.add(row);
        }
        logger.info("Created list of list with {} Long lists", list.size());
        return list;
    }

    public static String[][] readLists(String path, int numberOfLists) {
        List<String> lines = readLines(path);
        String[][] lists = new String[numberOfLists][lines.size()];
        int lineNumber = 0;

        for (String line : lines) {
            String[] items = line.trim().split("\\s+");
            for(int i=0;i<numberOfLists;i++){
                lists[i][lineNumber] = items[i];
            }
            lineNumber++;
        }
        logger.info("Created {} String lists with {} entries each", numberOfLists, lineNumber);
        return lists;
    }

    public static char[][] readCharacterTable(String path) {
        List<String> rows = readLines(path);
        int numberOfCols = rows.get(0).length();
        char[][] charTable = new char[numberOfCols][rows.size()];
        int rowNumber = 0;

        for (String row : rows) {
            for(int col=0;col<numberOfCols;col++){
                charTable[col][rowNumber] = row.charAt(col);
            }
            rowNumber++;
        }
        logger.info("Created {} rows and {} cols char table", rows.size(), numberOfCols);
        return charTable;
    }

    public static int[][] readIntegerTable(String path) {
        List<String> rows = readLines(path);
        int numberOfCols = rows.get(0).length();
        int[][] intTable = new int[numberOfCols][rows.size()];
        int rowNumber = 0;

        for (String row : rows) {
            for(int col=0;col<numberOfCols;col++){
                intTable[col][rowNumber] = Character.getNumericValue(row.charAt(col));
            }
            rowNumber++;
        }
        logger.info("Created {} rows and {} cols integer table", rows.size(), numberOfCols);
        return intTable;
    }

    public static String readAsOneString(String path) {
        List<String> list = readLines(path);
        String result = "";
        for(String row : list){
            result += row;
        }
        return result;
    }

    private static List<String> readLines(String resourcePath) {
        try {
            URL resource = FileUtil.class.getClassLoader().getResource(resourcePath);
            if (resource == null) {
                logger.error("Resource {} not found", resourcePath);
            return List.of();
            }
            return Files.readAllLines(Path.of(resource.toURI()));
        } catch (Exception e) {
            logger.error("Could not read file {}", resourcePath, e);
            return List.of();
        }
    }
}
