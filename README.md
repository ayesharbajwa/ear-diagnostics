# ear-diagnostics
Cambridge Engineering IIA project - GM1 2017. Diagnosis of ear problems.

CODE REPOSITORY for CamEar: Improving the Diagnosis of Ear Pathologies

We have created a device and system, branded "CamEar", that improves the diagnosis of ear pathologies. In the device, we combine the capabilities of ear temperature measurement, hearing test administration, and the capture of tympanic membrane (eardrum) images. In particular, we have targeted the diagnosis of two types of ear infection: Acute otitis media (AOM) is a bacterial infection that often requires antibiotics, while Otitis media with effusion (OME) does not require antibiotics. Our prototype system is able to distinguish an AOM infected tympanic membrane from a normal and healthy tympanic membrane with 90 ± 3% accuracy, helping GPs prevent the overprescription of antibiotics.

This repository includes implementation for:
  - hearing test (and demo)
  - camera feed and image capture
  - image pre-processing
  - feature extraction
  - convolution neural network (CNN) analysis
  - dataset building and augmentation
  - plotting and data display capabilities
  - GUI ”works-like” model integrating above functions
  - integration with the L2S2 database
