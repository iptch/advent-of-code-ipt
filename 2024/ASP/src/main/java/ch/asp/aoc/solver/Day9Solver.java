package ch.asp.aoc.solver;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import ch.asp.aoc.util.FileUtil;

public class Day9Solver implements DaySolver{
    private static final Logger logger = LoggerFactory.getLogger(Day9Solver.class);
    List<FileBlock> files; 
    Integer[] disk;
    int lastSetPostion;
    int fileCount = 0;

    @Override
    public void solve(String resourcePath) {
        String input = FileUtil.readAsOneString(resourcePath);
        readDisk(input);
        compactDiskTask2();
        logger.info("Checksum is {}", calculateChecksum());
    }

    private void readDisk(String input) {
        files = new ArrayList<>();
        int position = 0;
        
        for (int i = 0; i < input.length(); i++) {
            int size = Character.getNumericValue(input.charAt(i));
            if (i % 2 == 0) {
                files.add(new FileBlock(fileCount++, size, position));
                position += size;
            } else {

                position += size;
            }
        }
        disk = new Integer[position];

        for (int i = 0; i < fileCount; i++){
            FileBlock currentFile = files.get(i);
            for (int j= 0; j < currentFile.size; j++){
                disk[currentFile.position+j] = currentFile.id;
            }
        }
        lastSetPostion = position-1;
    }

    private void compactDiskTask1() {
        int firstFreePostion = 0;
        while (lastSetPostion>firstFreePostion){
            if (disk[firstFreePostion] == null){
                while (disk[lastSetPostion] == null){
                    lastSetPostion--;
                }
                disk[firstFreePostion] = disk[lastSetPostion];
                disk[lastSetPostion] = null;
            }
            firstFreePostion++;
        }
        lastSetPostion--;
    }

    private void compactDiskTask2() {
        for (int currentId = fileCount - 1; currentId >= 0; currentId--) {
            FileBlock currentFile = files.get(currentId);
            
            int gapPosition = findLeftmostSuitableGap(currentFile.size);
            
            if (gapPosition != -1 && gapPosition < currentFile.position) {
                moveFile(currentFile, gapPosition);
            }
        }
    }

    private int findLeftmostSuitableGap(int neededSize) {
        int currentGapSize = 0;
        int gapStartPosition = -1;
        
        for (int i = 0; i < disk.length; i++) {
            if (disk[i] == null) {
                if (currentGapSize == 0) {
                    gapStartPosition = i;
                }
                currentGapSize++;
                
                if (currentGapSize >= neededSize) {
                    return gapStartPosition;
                }
            } else {
                currentGapSize = 0;
            }
        }
        return -1; 
    }
    
    private void moveFile(FileBlock file, int newPosition) {
        for (int i = 0; i < file.size; i++) {
            disk[newPosition + i] = file.id;
            disk[file.position + i] = null;
        }

        file.position = newPosition;
    }

    private long calculateChecksum(){
        long sum = 0;
        for (int i=0;i<=lastSetPostion;i++){
            if (disk[i] != null){
                sum += i*disk[i];
            }
        }
        return sum;
    }

    class FileBlock {
        int id;
        int size;
        int position;
        
        FileBlock(int id, int size, int position) {
            this.id = id;
            this.size = size;
            this.position = position;
        }
    }
}
