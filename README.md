
# 📰 Fake News Detection & String Similarity

A project for detecting fake news using NLP and machine learning, and for calculating string similarity using edit distance. Built with Python, scikit-learn, pandas, and NLTK.

## 🎯 Features
- Fake news classification (Jupyter notebook)
- String similarity calculation (Python script)
- Clean, readable code
- Easy setup and reproducibility

## 🚀 Quick Start
1. **Clone Repository**
   ```bash
   git clone https://github.com/TutulMajumder/fake-news-detection.git
   cd fake-news-detection
   ```
2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # or
   source venv/bin/activate # macOS/Linux
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download Dataset**
   - Go to [Kaggle Fake News Classification](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)
   - Download the dataset and place it in your project folder

5. **Run the Notebook**
   - Open `Fake_News_detection.ipynb` in Jupyter or VS Code
   - Follow the steps for preprocessing, training, and evaluation

6. **Run the String Similarity Script**
   ```bash
   python similarity.py
   ```

## 🏗️ Project Structure
```
Fake_News_Detection/
├── Fake_News_detection.ipynb   # Main notebook for fake news detection
├── similarity.py               # Script for string similarity calculation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT License
├── README.md                   # Project documentation
```

## 📊 Model Details
- **Notebook:** Uses TF-IDF, Naive Bayes, and standard NLP preprocessing
- **Similarity Script:** Calculates edit distance and similarity percentage between two strings

## 💻 Technology Stack
- Python 3.8+
- Pandas, NumPy
- scikit-learn
- NLTK
- Jupyter Notebook / VS Code

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 🤝 Contributing
Contributions are welcome!
- Fork the repository
- Create a branch (`git checkout -b feature/improvement`)
- Commit your changes
- Push and open a Pull Request

## 📞 Support
- Open an issue on GitHub for bugs or questions

## ⭐ Acknowledgements
- [Kaggle Fake News Classification Dataset](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)

---
If you found this project useful, please star the repo!
