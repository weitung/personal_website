# RL-SAR: A Robotic System for Fine-Grained RFID Localization using RL-based Synthetic Aperture Radar
![Intro Pic](/asset/image/projects/rlsar_pic.png)
Efficient localization of RFID-tagged items is crucial in scenarios that require tracking and managing a large inventory. Current systems for fine-grained RFID localization have shown limitations since they only collect measurements on a pre-defined trajec- tory or optimize measurement locations for a single tag. Thus, there is a need for an RFID localization system that can autonomously optimize for multiple tags and adaptively relocalize tags with lower confidence to achieve a more precise and efficient localization.
We introduce RL-SAR, an end-to-end autonomous Synthetic Aperture Radar (SAR) based RFID localization system, utilizing a Reinforcement Learning (RL) al- gorithm to determine the most optimal trajectory for localizing multiple tags. We implemented this system with an antenna moving on a ceiling-mounted 2D track. The core of the system is a RL-based trajectory optimization algorithm for collecting RF measurements. Based on these RF measurements, we developed a data processing pipeline to compute the estimated tag locations along with their confidence metrics, derived from the RF SAR hologram. The RL algorithm leverages confidence metrics associated with the tags and is capable of learning a strategy that minimizes the antenna’s traveled distance while enhancing the localization accuracy.
We built and evaluated a proof-of-concept prototype of RL-SAR. Experimental evaluation demonstrates a mean 3D localization accuracy of 0.244m and the capability to locate 15 tags within an average scanning distance of 19.14 m. We compared our algorithm to naive baselines and show that the baselines require 86% longer trajectory than RL-SAR. Our results show the potential for achieving robust and efficient localization to enhance the current inventory processes across the manufacturing, retail, and logistics sectors.
