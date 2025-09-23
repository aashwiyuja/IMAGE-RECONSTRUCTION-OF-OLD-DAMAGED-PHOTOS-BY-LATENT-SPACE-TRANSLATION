# Image Reconstruction of Old Damaged Photos by Latent Space Translation

## Problem Statement
Old photographs often carry deep emotional and historical value, but many are damaged due to age, scratches, poor resolution, or environmental wear. Traditional restoration methods are manual, time-consuming, and require expert skills. This project aims to automate the restoration of old, damaged photos using deep learning techniques specifically latent space translation to recover both facial details and global image quality.

## Strategies Tried

### Core Components
- **Global Restoration**: A triplet domain translation network handles both structured and unstructured degradation.
- **Face Enhancement**: A progressive generator refines facial regions for high-quality restoration.
- **Scratch Detection**: A dedicated module identifies and masks scratches for targeted repair.
- **GUI Interface**: A user-friendly GUI allows users to upload images and view results interactively.

### Technical Workflow
- **Installation & Setup**:
  - Cloned and integrated `Synchronized-BatchNorm-PyTorch`.
  - Downloaded pretrained models for face landmarks and restoration checkpoints.
  - Installed dependencies via `requirements.txt`.

- **Image Processing**:
  - For clean images: `run.py` with basic arguments.
  - For scratched images: `run.py` with `--with_scratch`.
  - For high-resolution scratched images: `run.py` with `--HR`.

- **Scratch Detection**:
  - Used `detection.py` with configurable input sizes.

- **Training Pipeline**:
  - Created training files from VOC, Flicker Face, DIV2K, and real old photo datasets.
  - Trained VAEs for domain A and B.
  - Trained mapping networks for quality restoration, scratch handling, and multi-scale patch attention.

- **Face Enhancement**:
  - Applied a progressive generator to improve facial clarity and realism.

## What We Aim to Achieve
- **Real-Time Restoration**: Optimize models for faster inference and real-time feedback.
- **Cloud Deployment**: Host the app on platforms like AWS or Azure for broader accessibility.
- **Mobile App Integration**: Build a lightweight version for smartphones.
- **Multi-Face Support**: Enhance the pipeline to handle group photos and complex scenes.
- **Historical Dataset Expansion**: Train on diverse global archives for culturally inclusive restoration.

## Observations from the Project
- **Latent Space Translation is Effective**: It enables nuanced restoration of both global and facial features.
- **Scratch Detection is Crucial**: Accurate masking significantly improves output quality.
- **Training is Resource-Intensive**: High-resolution restoration demands substantial GPU power and memory.
- **GUI Enhances Accessibility**: Non-technical users can easily interact with the system.

## Recommendations & Improvements
- **Model Optimization**: Reduce inference time and memory footprint for broader deployment.
- **Dataset Diversity**: Include more varied photo types (e.g., sepia, grayscale, cultural attire).
- **Interactive Feedback**: Let users adjust restoration intensity or select focus areas.
- **Documentation & Tutorials**: Provide step-by-step guides for installation, training, and usage.
- **Community Contributions**: Open-source parts of the pipeline to encourage collaboration and innovation.
