package com.example.faceYourPace.web.login;

import lombok.Data;

import javax.validation.constraints.NotEmpty;

@Data
public class LoginForm {

    @NotEmpty
    private String userId;

    @NotEmpty
    private String userPw;
}
