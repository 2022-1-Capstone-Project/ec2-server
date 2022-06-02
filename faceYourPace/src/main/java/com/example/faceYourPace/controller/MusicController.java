package com.example.faceYourPace.controller;

import com.example.faceYourPace.cmd.ConnectS3;
import com.example.faceYourPace.cmd.DownloadPython;
import com.example.faceYourPace.cmd.MusicFunctionPython;
import com.example.faceYourPace.domain.PlayList;
import com.example.faceYourPace.domain.member.Member;
import com.example.faceYourPace.domain.member.MemberService;
import com.example.faceYourPace.domain.music.Music;
import com.example.faceYourPace.domain.music.MusicForm;
import com.example.faceYourPace.repository.MemberRepository;
import com.example.faceYourPace.repository.MusicRepository;
import com.example.faceYourPace.service.MusicService;
import com.example.faceYourPace.service.PlayListService;
import com.example.faceYourPace.web.login.LoginController;
import lombok.RequiredArgsConstructor;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequiredArgsConstructor
public class MusicController {

    public final MusicService musicService;
    public final MusicRepository musicRepository;
    public final MemberRepository memberRepository;
    private final MemberService memberService;
    private final PlayListService playListService;
    public Member member;
    private final LoginController loginController;

    @GetMapping("/api/music/add")
    public String createForm(Model model) {
        model.addAttribute("form", new MusicForm());
        return "music 추가 form";
    }

    @PostMapping("/api/music/add") // 메인 홈에서 다운
    public String create(@RequestParam("music_url") String music_url, @RequestParam("userId") String userId, MusicForm form) { // music 추가

        Music music = new Music();
        music.setMusic_url(form.getMusic_url());
        music.setMUserId(form.getMUserId());

        System.out.println("userId:" + userId);
        System.out.println("url:" + music_url);
        // 음악 다운
        System.out.println(music_url);
        String r2 = DownloadPython.create(music_url); // 음악 다운로드(mp3)
        int idx = r2.indexOf("cache");
        String r = r2.substring(idx+5);
        //String r = "title<>03:48<>http://hwi/abc.png";
        System.out.println("downloadPython 완료");

        String[] strArr = r.split("<>");
        System.out.println("r:" + r);
        System.out.println("arr[0]" + strArr[0]);
        System.out.println("arr[1]" + strArr[1]);
        System.out.println("arr[2]" + strArr[2]);

        String title = strArr[0];
        String length = strArr[1];
        String img_url = strArr[2];

        music.setMusicImg_url(img_url);
        music.setLength(length);
        music.setTitle(title);

        musicService.saveMusic(music);
        System.out.println("음악 테이블에 저장 완료");

        String s3T = music.getTitle() + ".mp3";
        String s3T2 = s3T.replaceAll(" ", "");

        musicService.updateS3Title(music.getId(), s3T2); //s3
        System.out.println("s3Title update");

        return "true";
    }

    @PostMapping("/api/music/config") // 안씀
    public String createConfig(@RequestParam("musicName") String musicName) { // music 추가 // 수정하기(update로 구현하기)

        Music music = musicRepository.findMusicName(musicName);
        //Music music = new Music();
        //music.setMusicName(form.getMusicName());
        //music.setMusicStart(form.getMusicStart());
        //music.setMusicEnd(form.getMusicEnd());
        //music.setMusicRepeat(form.getMusicRepeat());
        music.setCreateDate(LocalDateTime.now());
        musicService.saveMusic(music);

        // 음악 변환 후 저장
        //MusicFunctionPython.create(audio_path, save_path, music.getMusicStart(), music.getMusicEnd(), bpm);
        System.out.println("music 설정값 적용 완료");
        return "true";
    }




    @GetMapping("/api/music/list") // music table 전체 출력
    List<Music> getAll() { // 음악리스트 출력
        return musicRepository.findAll();
    }

    @GetMapping("/api/music/list/all") // 특정 userId의 music table 출력
    List<Music> getUserMusic(@RequestParam("userId") String userId) { // (해당 userId의) 음악리스트 출력(수정하기ㅠ)

        return musicRepository.findByMUserId(userId);

    }


    @GetMapping("/api/music/list/userId/name") // 특정 userId의 특정 playlist의 music table 출력
    List<Music> getUserPlayListMusic(@RequestParam("userId") String userId, @RequestParam("name") String name) { // (해당 userId의) 음악리스트 출력

        /*
        List<Music> musics = musicService.findByMUserId(userId);
        List<PlayList> playLists = playListService.findName(name);

        for (PlayList playList : playLists){
            for (Music music : musics){
                if (music.getMUserId().equals(userId) && (playList.getName().equals(name))) {
                    //playListService.playList(member.getId(), name);
                    return musicRepository.findByMUserIdPlayList(userId, name);
                }
            }
        }

         */
        return musicRepository.findByMUserIdPlayList(userId, name);

    }





    @PostMapping("/api/music/{musicId}/edit") // config 페이지 연동
    public String updateMusic(@PathVariable Long musicId, @ModelAttribute("form") MusicForm form) {

        musicService.updateMusic(musicId, form.getMusicStart(), form.getMusicEnd(), form.getMusicRepeat(), form.getTarget_bpm());
        System.out.println("음악 설정 update");
/*
        String bpm;
        if(member.getTarget_pace() == null){ // 타겟 bpm이 없을 경우
            bpm = "0";
        }
        else{
            bpm = member.getTarget_pace();
        }

 */
        Music music = musicRepository.findOne(musicId);
        // 음악 변환 후 저장
        String audio_path = "/home/ubuntu/face-your-pace-function/fyp_download/result/" + music.getTitle().trim() + ".mp3"; // 원본 음악 저장된 위치
        String save_path = "/home/ubuntu/face-your-pace-function/fyp_download/result/" + music.getTitle().trim() + ".wav"; // 변환된 음원 저장할 위치

        System.out.println("audio" + audio_path);
        System.out.println("save" + save_path);
        System.out.println("start" + music.getMusicStart());
        System.out.println("start_len" +  music.getMusicStart().length());
        System.out.println("end" + music.getMusicEnd());
        System.out.println("end_len" + music.getMusicEnd().length());
        System.out.println("bpm" + music.getTarget_bpm());
        System.out.println("bpm_len" + music.getTarget_bpm().length());

        String s3T = music.getTitle() + ".wav"; //
        String s3T2 = s3T.replaceAll(" ", "");

        musicService.updateS3Title(musicId, s3T2);
        System.out.println("s3Title update");

        MusicFunctionPython.create(audio_path, save_path, music.getMusicStart(), music.getMusicEnd(), music.getTarget_bpm());
        System.out.println("music 설정값 적용 완료:" + music.getS3Title());

        ConnectS3.create(music.getS3Title()); // s3 upload

        return "true"; // s3파일명 반환
    }



    @GetMapping("api/music/edit") // 안씀
    public String updateMusicForm(@PathVariable("musicName") Long musicId, Model model) {
        Music music = (Music) musicService.findOne(musicId);

        MusicForm form = new MusicForm();
        form.setId(music.getId());
        form.setMusicName(music.getMusicName());
        form.setMusicStart(music.getMusicStart());
        form.setMusicEnd(music.getMusicEnd());
        form.setMusicRepeat(music.getMusicRepeat());
        form.setMusicImg_url(music.getMusicImg_url());

        model.addAttribute("form", form);
        return "음악 설정 update";
    }

}





