package com.infotact.atmosync.controller;

import com.infotact.atmosync.entity.SensorData;
import com.infotact.atmosync.service.SensorDataService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/sensors")
public class SensorDataController {

    private final SensorDataService service;

    public SensorDataController(SensorDataService service) {
        this.service = service;
    }

    @PostMapping
    public SensorData saveSensorData(@RequestBody SensorData sensorData) {
        return service.saveSensorData(sensorData);
    }

    @GetMapping
    public List<SensorData> getAllSensorData() {
        return service.getAllSensorData();
    }

    @GetMapping("/{id}")
    public SensorData getSensorDataById(@PathVariable Long id) {
        return service.getSensorDataById(id);
    }

    @DeleteMapping("/{id}")
    public String deleteSensorData(@PathVariable Long id) {
        service.deleteSensorData(id);
        return "Sensor data deleted successfully.";
    }
}