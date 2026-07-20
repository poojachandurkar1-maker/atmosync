package com.infotact.atmosync.service;

import com.infotact.atmosync.entity.SensorData;
import com.infotact.atmosync.repository.SensorDataRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SensorDataService {

    private final SensorDataRepository repository;

    public SensorDataService(SensorDataRepository repository) {
        this.repository = repository;
    }

    public SensorData saveSensorData(SensorData sensorData) {
        return repository.save(sensorData);
    }

    public List<SensorData> getAllSensorData() {
        return repository.findAll();
    }

    public SensorData getSensorDataById(Long id) {
        return repository.findById(id).orElse(null);
    }

    public void deleteSensorData(Long id) {
        repository.deleteById(id);
    }
}