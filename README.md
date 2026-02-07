# Corrosion Detection (YOLOv5)

Project overview
- Detect corrosion in images using a YOLOv5-based detector. This repository contains training and inference scripts, a YOLO-formatted dataset split (`train/`, `valid/`, `test/`), alerting utilities, and a bundled `yolov5-master/` codebase for model training and export.

Features
- Single-class corrosion detection (custom dataset)
- Inference script with configurable confidence threshold
- Training pipeline compatible with YOLOv5
- Optional SMS/Twilio notifications for detected events

Requirements
- Python 3.8+ (see `requirements.txt`)
- Recommended: a CUDA-enabled GPU for training

Quick start (inference)
- Place or download model weights (`best.pt`) locally — weights are excluded from this repo by default.

PowerShell:
```powershell
python detect.py --weights best.pt --source test/images --conf 0.25
```

Training (example)
- Ensure `data.yaml` points to your dataset paths and classes.

PowerShell:
```powershell
python train.py --data data.yaml --cfg yolov5s.yaml --weights '' --epochs 50
```

Dataset format
- Uses YOLO format: one `.txt` label file per image with `class x_center y_center width height` (normalized).
- Directory layout:
	- `train/images`, `train/labels`
	- `valid/images`, `valid/labels`
	- `test/images`, `test/labels`

Model weights and large files
- Do not commit large model files (e.g., `*.pt`) directly. Use Git LFS or provide download instructions for weights.

Enable Git LFS (optional):
```powershell
git lfs install
git lfs track "*.pt"
git add .gitattributes
git commit -m "Track .pt with Git LFS"
```

Repository layout
- `detect.py` — run inference and save results
- `train.py` — training entry point (wraps YOLOv5 training)
- `data.yaml` — dataset config used for training
- `twilio_notification.py`, `sms.py` — utilities to send SMS notifications
- `yolov5-master/` — contained YOLOv5 code for training/exporting

Tips & troubleshooting
- If inference fails due to missing weights, download or copy `best.pt` to the repository root.
- For faster inference/training, install the GPU build of PyTorch matching your CUDA version as listed in `requirements.txt`.
- Inspect `test/labels` to verify annotation alignment with images.

Contributing
- Open issues or pull requests for bugs, improvements, or dataset changes. Include reproducible steps and sample images when possible.

License & contact
- Add a license file if you plan to make the repo public. For questions, add your contact details or open an issue.

Files added/changed
- `.gitignore` — ignores model weights, caches, and logs
- `README.md` — this file

Next actions
- I can initialize a local git repo and make the initial commit, or prepare instructions to push to GitHub. Tell me which you prefer.

What to include in the GitHub repo
- Include: project code and scripts (`detect.py`, `train.py`, `sms.py`, `twilio_notification.py`), configuration files (`data.yaml`, `requirements.txt`, `README.md`), and any small helper scripts or docs.

What to exclude (already in `.gitignore`)
- Model weights and large binaries: `*.pt`, `best.pt`, `yolov5s.pt`, `weights/`
- Dataset images and media: `train/images/`, `valid/images/`, `test/images/` (keep label files if you want small examples)
- Experiment outputs and logs: `runs/`, `logs/`
- Vendored repo git metadata: `yolov5-master/.git/`

How to share weights and large data
- Use Git LFS to track `*.pt` if you want the weights in the remote repo, or host model weights on a release, cloud storage (AWS S3, Google Drive) or artifact storage and provide a download link in this `README.md`.

Example: add a small section with a download link and checksum for `best.pt` so users can reproduce inference locally.

