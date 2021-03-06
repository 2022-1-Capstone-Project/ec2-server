package com.example.faceYourPace.repository;

import com.example.faceYourPace.domain.member.Member;
import com.example.faceYourPace.domain.music.Music;
import lombok.RequiredArgsConstructor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import java.util.List;
import java.util.Optional;

@Repository
@RequiredArgsConstructor
public class MemberRepository {

    private final EntityManager em;
    private Member member;

    public void save(Member member) {
        em.persist(member);
    }

    public Member findOne(Long id) {
        return em.find(Member.class, id);
    }


    public List<Member> findAll() {
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }

    public List<Member> findByUserId(String userId) {
        return em.createQuery("select m from Member m where m.userId = :userId", Member.class)
                .setParameter("userId", userId)
                .getResultList();
    }




    /*
    Member member = em.createQuery(
                    "SELECT m from Member m WHERE m.userId = :userId", Member.class)
            .setParameter("userId", userId)
            .getSingleResult();


     */


}
