# Run CAN bus stress test
python test/can_stress.py \
  --duration=1h \
  --msg-rate=5000/s \
  --bus=can0
