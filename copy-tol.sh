#!/bin/bash
# Script to copy tol directory to docs after Quarto render

# Copy tol directory to docs
cp -r tol docs/

echo "✓ tol directory copied to docs/"
