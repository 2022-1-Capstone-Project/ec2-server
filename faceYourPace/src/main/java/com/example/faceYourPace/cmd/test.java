package com.example.faceYourPace.cmd;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.PumpStreamHandler;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class test extends Thread{


//    String eventIdx;
//    String userIdx;
//    String instaUrl;
//    public InstagramCrawler(String eventIdx, String userIdx, String instaUrl){
//        this.eventIdx = eventIdx;
//        this.userIdx = userIdx;
//        this.instaUrl = instaUrl;
//
//    }

    public static String create(String eventIdx, String userIdx, String instaUrl){
        System.out.println("Python Call");
        String[] command = new String[5];
        command[0] = "python3";
        //command[1] = "\\workspace\\java-call-python\\src\\main\\resources\\test.py";
        command[1] = "/Users/chaehuiseon/chs_documents/data_test/instacrawler3.py";
        command[2] = eventIdx;
        System.out.println(eventIdx);
        //command[2] = "1";
        command[3] = userIdx;
        System.out.println(userIdx);
        //command[3] = "20195542";
        command[4] = "'"+instaUrl+"'";
        System.out.println(command[4]);
        //command[4] = "'https://www.instagram.com/p/CdUwjoApaUR/?utm_source=ig_web_copy_link'";
        //command[0] = "python3";
        //command[1] = "/Users/chaehuiseon/chs_documents/data_test/test.py";
        //command[2] = "3";
        //command[3] = "4";
        //command[4] = "1";
        System.out.println(command.toString());
        try {
            return execPython(command);
        } catch (Exception e) {
            e.printStackTrace();
            return "error";
        }
    }

    public static String execPython(String[] command) throws IOException, InterruptedException {
        CommandLine commandLine = CommandLine.parse(command[0]);
        for (int i = 1, n = command.length; i < n; i++) {
            commandLine.addArgument(command[i]);
        }

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PumpStreamHandler pumpStreamHandler = new PumpStreamHandler(outputStream);
        DefaultExecutor executor = new DefaultExecutor();
        executor.setStreamHandler(pumpStreamHandler);
        int result = executor.execute(commandLine);

        System.out.println("result: " + result);
        System.out.println("output: " + outputStream.toString());

        return outputStream.toString();

    }




}