package com.example.faceYourPace.cmd;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.PumpStreamHandler;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class ConnectS3 extends Thread{

    public static String create(String musicName){
        System.out.println("Python Call");
        String[] command = new String[3];
        command[0] = "python3";
        command[1] = "/home/ubuntu/face-your-pace-function/fyp_download/result/connectS3.py"; // 파이썬 파일 위치
        command[2] = musicName; // 음악 링크

        System.out.println(musicName);
        System.out.println(command[2]);

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
        System.out.println("mp3 파일 다운 완료");

        return outputStream.toString();

    }
}
