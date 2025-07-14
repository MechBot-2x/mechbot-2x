# backend/Dockerfile (Optimizado para GPU)
FROM python:3.10-slim as builder
RUN pip install --user onnxruntime-gpu==1.16.0  # Soporte CUDA

FROM nvidia/cuda:12.2-base
COPY --from=builder /root/.local /usr/local
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64  # Soporte NVIDIA
