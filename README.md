# BLASER 2.0 Testing Environment

This repository contains a Jupyter notebook (`blaser_2_test.ipynb`) to test and experiment with BLASER 2.0 for sentence similarity prediction and machine translation evaluation.

## What is BLASER 2.0?

BLASER 2.0 is a family of models for automatic evaluation of machine translation quality based on SONAR (Sentence-level multimOdal and laNguage-Agnostic Representations) embeddings. It predicts cross-lingual semantic similarity between translations and source text.

There are two main models:
- **BLASER 2.0 QE (Quality Estimation)**: Evaluates translations without requiring reference translations
- **BLASER 2.0 Ref**: Uses source, translation, and reference translation for evaluation

## Setup Instructions

### Prerequisites

1. **Install UV** (a faster alternative to pip)
   ```bash
   curl -sSf https://install.python-uv.org | python3
   ```

2. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd BLASER
   ```

### Environment Setup (Using pyproject.toml)

The project includes a `pyproject.toml` file that defines all dependencies and configuration for UV.

1. **Create and activate a virtual environment**
   ```bash
   uv venv create .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

2. **Install all dependencies at once**
   ```bash
   uv pip install -e .
   ```

   This will install all dependencies defined in the pyproject.toml file, including PyTorch and SONAR.

3. **Handle fairseq2 installation**
   After installing the main dependencies, use the included helper script to automatically detect your PyTorch version and install the matching fairseq2:
   
   ```bash
   # Run the helper script to install fairseq2
   python install_fairseq2.py
   ```
   
   Or install manually if needed:
   
   ```bash
   # Check your PyTorch version
   python -c "import torch; print(torch.__version__)"
   
   # Install fairseq2 with the matching version (example for PyTorch 2.0.0+cu118)
   PT_VERSION=2.0.0
   CUDA_VERSION=cu118  # or 'cpu' for CPU-only
   uv pip install fairseq2 --extra-index-url https://fair.pkg.atmeta.com/fairseq2/whl/pt${PT_VERSION}/${CUDA_VERSION}
   ```

3. **Install Jupyter**
   ```bash
   uv pip install jupyter
   ```

### Running the Notebook

1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Open the notebook**
   
   Navigate to and open `blaser_2_test.ipynb`

## Features of the Notebook

- Initialize BLASER 2.0 models and SONAR text embedder
- Test sentence similarity across multiple languages
- Evaluate translations of varying quality
- Interactive text input for custom similarity testing

## Additional Resources

- [SONAR GitHub Repository](https://github.com/facebookresearch/SONAR)
- [BLASER 2.0 QE Model Card](https://huggingface.co/facebook/blaser-2.0-qe)
- [BLASER 2.0 Ref Model Card](https://huggingface.co/facebook/blaser-2.0-ref)

## License

BLASER 2.0 models are released by Meta under a non-commercial license. Please refer to their original license for usage terms.
