import java.util.HashMap;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;


public class Day12 {
    public static void main(String[] args) {
        ArrayList<String> fileData = getFileData("src/data");
        HashMap<String, Integer> registers = new HashMap<>();
        registers.put("a", 0);
        registers.put("b", 0);
        registers.put("c", 0);
        registers.put("d", 0);

        int currentInstruction = 0;

        while (currentInstruction < fileData.size()) {
            String instruction = fileData.get(currentInstruction);
            String instructionName = instruction.split(" ")[0];
            if (instructionName.equals("cpy")) {
                String letters = "abcd";
                int value;
                String v = instruction.split(" ")[1];
                if (letters.contains(v)) {
                    value = registers.get(v);
                }
                else {
                    value = Integer.parseInt(instruction.split(" ")[1]);
                }
                String register = instruction.split(" ")[2];
                registers.put(register, value);
                currentInstruction++;
            }
            if (instructionName.equals("inc")) {
                String register = instruction.split(" ")[1];
                registers.put(register, registers.get(register)+1);
                currentInstruction++;
            }
            if (instructionName.equals("dec")) {
                String register = instruction.split(" ")[1];
                registers.put(register, registers.get(register)-1);
                currentInstruction++;
            }
            if (instructionName.equals("jnz")) {
                String register = instruction.split(" ")[1];
                String letters = "abcd";
                int value;
                String v = instruction.split(" ")[1];
                if (letters.contains(v)) {
                    value = registers.get(v);
                }
                else {
                    value = Integer.parseInt(instruction.split(" ")[1]);
                }
                int jumpValue = Integer.parseInt(instruction.split(" ")[2]);
                if (value != 0) {
                    currentInstruction += jumpValue;
                }
                else {
                    currentInstruction++;
                }
            }
        }

        System.out.println(registers);

    }

    public static ArrayList<String> getFileData(String fileName) {
        ArrayList<String> fileData = new ArrayList<String>();
        try {
            File f = new File(fileName);
            Scanner s = new Scanner(f);
            while (s.hasNextLine()) {
                String line = s.nextLine();
                if (!line.equals(""))
                    fileData.add(line);
            }
            return fileData;
        }
        catch (FileNotFoundException e) {
            return fileData;
        }
    }

}