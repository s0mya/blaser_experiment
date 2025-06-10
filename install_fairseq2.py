#!/usr/bin/env python3
"""
Helper script to install the correct fairseq2 version based on the installed PyTorch.
This script detects your PyTorch version and CUDA capability, then installs
the appropriate fairseq2 package.

Usage:
    python install_fairseq2.py
"""

import subprocess
import sys
import os

def get_pytorch_version():
    """Get the PyTorch version and CUDA capability."""
    try:
        import torch
        pt_version = torch.__version__.split('+')[0]
        if '+' in torch.__version__:
            cuda_version = torch.__version__.split('+')[1]
        else:
            cuda_version = "cpu"
        return pt_version, cuda_version
    except ImportError:
        print("PyTorch is not installed. Please install it first.")
        sys.exit(1)

def install_fairseq2(pt_version, cuda_version):
    """Install fairseq2 with the appropriate version."""
    if cuda_version != "cpu" and not cuda_version.startswith("cu"):
        # Format CUDA version properly
        cuda_version = "cu" + cuda_version.replace("cuda", "").replace(".", "")
    
    print(f"Installing fairseq2 for PyTorch {pt_version} with {cuda_version}")
    
    # Construct the installation command
    cmd = [
        "uv", "pip", "install", "fairseq2",
        f"--extra-index-url=https://fair.pkg.atmeta.com/fairseq2/whl/pt{pt_version}/{cuda_version}"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("fairseq2 installation completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing fairseq2: {e}")
        sys.exit(1)

if __name__ == "__main__":
    pt_version, cuda_version = get_pytorch_version()
    install_fairseq2(pt_version, cuda_version)
