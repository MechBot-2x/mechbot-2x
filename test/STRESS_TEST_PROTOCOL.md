## **5. Testing Framework**
```bash
# Run CAN bus stress test
python test/can_stress.py \
  --duration=1h \
  --msg-rate=5000/s \
  --bus=can0
```

📄 `test/LOAD_TESTING.md`
```bash
# Execute API load test
k6 run test/k6/telemetry_test.js \
  --vus 100 \
  --duration 30m
```
