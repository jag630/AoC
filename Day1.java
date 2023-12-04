//Advent of Code Day 1

import java.io.*;
import java.util.*;

public class HelloWorld {
	public static void main(String[] args) throws FileNotFoundException {
		System.out.println(calc(false));
		System.out.println(calc(true));
	}
	public static int calc(boolean words) throws FileNotFoundException {
		ArrayList<String> filelist = new ArrayList<String>();
		Scanner s = new Scanner(new File("day1.txt"));
		while (s.hasNext()){
		    filelist.add(s.next());
		}
		s.close();
		Integer thesum = 0;
		ArrayList<Integer> hits = new ArrayList<Integer>();
		HashMap<String, Integer> vals = new HashMap<String, Integer>();
		String[] nums = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
		
		for(int x = 1; x < 10; x++) {
			if(words) vals.put(nums[x], x);
			vals.put(Integer.toString(x), x);
		}
	
		for(String line: filelist) {
			hits.clear();
			for(int x = 0; x < line.length(); x++) {
				for(String str: vals.keySet()) {
					if(line.substring(x,line.length()).startsWith(str)){
						hits.add(vals.get(str));
					}
				}
			}
			thesum += hits.get(0)*10 + hits.get(hits.size()-1);
		}
		return thesum;
	}
}
