package com.example.faceYourPace.domain.member;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import javax.validation.constraints.NotEmpty;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
public class Member {

    @Id @GeneratedValue
    @Column(name = "ID")
    private Long id;

    private String userId; //로그인 ID

    private String userPw; // 비밀번호

    private String userName; //사용자 이름

    private String userEmail; //사용자 이메일

    private String userAge; // 나이
    private String userHeight; // 키
    private String userWeight; // 몸무게

}