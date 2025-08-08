```python
# Model conversion to ONNX (scripts/convert_model.py)
python convert_model.py \
  --input=model/xgboost_v2.h5 \
  --output=onnx/xgboost_v2.onnx \
  --quantize
```
