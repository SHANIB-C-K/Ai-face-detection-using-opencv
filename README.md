# 🎭 Face Detection using OpenCV

A simple yet powerful real-time face detection application using OpenCV. This project captures video from a webcam, detects faces with a Haar cascade classifier, and highlights detected faces with a bounding box. Perfect for beginners exploring computer vision! 🚀

---

## ✨ Features
✅ Captures video from the default webcam 📷  
✅ Converts frames to grayscale for efficient face detection 🎞️  
✅ Uses Haar cascade classifier to detect faces 🧑‍💻  
✅ Draws rectangles around detected faces 🔳  
✅ Displays live video feed with detection in real-time ⏳  
✅ Exit anytime by pressing the 'q' key ⌨️

---

## 📦 Requirements
Ensure you have Python installed on your system. Then, install the required dependencies with:

```bash
pip install opencv-python
```

---

## 🚀 Setup & Usage
1. **Clone this repository:**
   ```bash
   git clone [https://github.com/your-username/face-detection-opencv.git](https://github.com/SHANIB-C-K/Ai-face-detection-using-opencv.git
   cd Ai-face-detection-using-opencv
   ```
2. **Download the Haar cascade XML file:**
   - Ensure `haarcascade_frontalface_default.xml` is in the project directory.
   - If missing, download it from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades).

3. **Run the script:**
   ```bash
   python main.py
   ```

---

## 📂 File Structure
```
📂 Ai-face-detection-using-opencv/
├── 📄 haarcascade_frontalface_default.xml
├── 📜 main.py
├── 📖 README.md
```

---

## 🛠️ Troubleshooting
- 📂 **Missing cascade file?** Download it from the official OpenCV repository.
- 🎯 **Face detection accuracy issues?** Try adjusting the parameters in `detectMultiScale()`.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👨‍💻 Author
**SHANIB C K** - [GitHub Profile]([https://github.com/SHANIB-C-K](https://github.com/SHANIB-C-K)

💡 *Feel free to fork, modify, and contribute to this project!* 🚀

