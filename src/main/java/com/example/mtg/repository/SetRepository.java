package com.example.mtg.repository;


import com.example.mtg.persistence.model.Set;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface SetRepository extends JpaRepository<Set, Long> {
    List<Set> findByid(Long id);
}