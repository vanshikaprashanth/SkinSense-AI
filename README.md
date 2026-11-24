# SkinSense – AI-Powered Skin Health Monitoring

**Status: Early proof-of-concept / educational prototype.**

SkinSense is a Python prototype for keeping a dated record of skin photos and notes. It currently offers basic technical image information and side-by-side photo tracking. The project title describes the long-term direction: **this version does not contain a trained AI model and does not diagnose skin conditions.**

## Problem idea
People may find it difficult to keep consistent records of visible skin changes over time. Photos taken under different lighting and camera conditions can be misleading, and users may forget when a photo was taken or what they observed.

## Proposed solution
A simple local application to save dated photo check-ins, add notes, review history, compare two photos side by side, and view basic image properties.

## Current features
- JPG, JPEG, and PNG upload.
- Local SQLite metadata storage and local image files.
- Dated check-ins and optional notes.
- Image width, height, and average pixel brightness.
- Side-by-side comparison of two saved photos.

## Technology
Python · Streamlit · Pillow · NumPy · SQLite

## Folder structure
```text
SKINSENSE/
├── app.py
├── app/
│   ├── __init__.py
│   ├── analysis.py
│   ├── comparison.py
│   └── storage.py
├── data/
│   └── .gitkeep
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally
1. Install Python 3.10 or newer.
2. Download/clone this repository and open a terminal in its folder.
3. Create a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install packages: `pip install -r requirements.txt`
5. Start: `streamlit run app.py`
6. Open the local URL shown in the terminal (usually `http://localhost:8501`).

## Privacy and safe use
- Images and database records are stored locally in `data/` on the computer running the app.
- The `data/` directory is excluded from Git. **Never commit personal skin photos, identifiable information, or private health notes to a public repository.**
- Brightness and pixel differences depend on lighting, framing, camera processing, and other factors. They are not clinical indicators.
- This is an educational prototype, not a medical device. It is not intended for diagnosis, screening, treatment selection, or emergency decisions.
- Seek advice from a qualified healthcare professional for persistent, painful, bleeding, rapidly changing, or concerning skin issues.

## Planned work (not implemented)
1. Define a narrow intended use with dermatology and user-experience advisors.
2. Add photo-capture guidance for consistent lighting, distance, angle, and no filters.
3. Explore user-controlled check-in trend summaries.
4. Investigate whether a suitable consented, licensed, representative dataset exists for a narrowly defined research task.
5. Only consider ML after documenting consent/licensing, representation, validation, limitations, and independent expert review.
6. Add authentication, encryption, retention controls, and privacy review before real-user deployment.

## Current limitations
- No trained machine-learning model.
- No skin-condition classification, diagnosis, or risk prediction.
- No login, cloud sync, or secure multi-user deployment.
- Local files are not encrypted by this prototype.

## Disclaimer
SkinSense is an educational software prototype, not a substitute for professional medical advice, diagnosis, or treatment.
