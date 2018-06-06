package com.example.mtg.service;

import com.example.mtg.persistence.model.Set;
import com.example.mtg.repository.SetRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Component
public class SetService {

    @Autowired
    private SetRepository setRepository;

    @Transactional
    public List<Set> findAll() {
        return setRepository.findAll();
    }

    @Transactional
    public List<Set> findByid(Long id) {
        return setRepository.findByid(id);
    }
}
