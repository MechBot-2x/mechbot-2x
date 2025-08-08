#!/bin/bash
# Build MechBot 2.0 artifacts
output_dir=$1
python -m build --outdir $output_dir
