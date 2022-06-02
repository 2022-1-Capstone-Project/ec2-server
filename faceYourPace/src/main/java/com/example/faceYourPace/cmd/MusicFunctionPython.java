package com.example.faceYourPace.cmd;

import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;
import org.apache.commons.exec.PumpStreamHandler;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

// 음악 저장 후 config 생성시 불러옴
public class MusicFunctionPython {

    public static String create(String audio_path, String save_path, String musicStart, String musicEnd, String target_bpm){
        System.out.println("Python Call");
        String[] command = new String[7];
        command[0] = "python3";
        //command[1] = "\\workspace\\java-call-python\\src\\main\\resources\\test.py";
        command[1] = "\"/home/ubuntu/face-your-pace-function/fyp_musicmodify/fyp_musicmodify.py\"";
        System.out.println("command[1]:" + command[1]);
        command[2] = audio_path;
       // System.out.println("wav_path:" + audio_path);
        System.out.println("command[2]:" + command[2]);
       //command[2] = "1";
        command[3] = save_path;
        System.out.println("command[3]:" + command[3]);
	// System.out.println("save_path:" + save_path);
        command[4] = "\"" + musicStart + "\"";
       // System.out.println("start:" + musicStart);
        System.out.println("command[4]:" + command[4]);
	command[5] = "\"" + musicEnd + "\"";
       // System.out.println("end:" + musicEnd);
        System.out.println("command[5]:" + command[5]);
	command[6] = "\"" + target_bpm + "\"";
       // System.out.println("bpm:" + target_bpm);
	System.out.println("command[6]:" + command[6]);
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
        int result = executor.execute(commandLine); // 여기서 오류남
        System.out.println("result: " + result);
        System.out.println("output: " + outputStream.toString());
        System.out.println("mp3 파일 다운 완료");

        return outputStream.toString();

    }

}
