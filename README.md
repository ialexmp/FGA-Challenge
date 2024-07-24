# Face & Gesture Analysis Challenge - Face Recognition (1st Place)

## Introduction
Welcome to the repository for the Face Recognition system, developed for the Face & Gesture Analysis Challenge at Pompeu Fabra University (UPF)!

This repository contains detailed documentation, code, models, and resources that contributed to the achievement of 1st place 🏆.

The system excels in efficiency, accuracy, and robustness, meeting the stringent criteria set by the challenge organizers. Users are invited to explore the work, use it as a learning resource, or build upon it for their own projects.


## Challenge Overview
The Face Recognition Lab 4 project aimed to create an automatic face recognition system capable of identifying users from a given database in various facial images. Our objective was to develop a system that:
- Identifies if a user from a predefined database is present in an image.
- Returns the identity of the user if present or "-1" if no user is found or the face does not match any user in the database.

## Objective
The goal of this project is to develop a face recognition system using MATLAB or Python that:
- Identifies if a user from a predefined database is present in an image.
- Returns the identity of the user if present or "-1" if no user is found or the face does not match any user in the database.

## Datasets
- **Training Dataset**: Contains 1200 images with known identities for development and evaluation. Each image includes:
  - Bounding box of the face.
  - Identity of the first face (between 1 and 80 for users, -1 for impostors or no face).

- **Test Dataset**: Also contains 1200 images for final evaluation, not provided to participants. It will test the system's performance.

## Performance Specifications
The face recognition system must meet the following criteria on the Test Database:

- **Accuracy**: F1-score ≥ 0.20
- **Speed**: Average processing time ≤ 3 seconds per image
- **Implementation**: Must run without errors or exceptions in MATLAB or Python
- **Model Size**: Code and model files must not exceed 80 MB
- **Model Depth**: Maximum of 10 layers and 2 submodels
- **Model Parameters**: Less than 1 million parameters

### Accuracy Calculation
The F1-score is calculated using:
\[ F1 = \frac{2 \times \text{True Positives}}{2 \times \text{True Positives} + \text{False Negatives} + \text{False Positives}} \]

## Implementation Details
- The system must accept an image and a model as input arguments and return an identity (positive integer or -1).
- Only the two largest faces in an image will be considered, and only one identity must be returned.
- The system should run in MATLAB or Python with any external sources properly referenced and instructions for installation provided.
- Code, models, and libraries must be submitted in a single submission not exceeding 80 MB.

