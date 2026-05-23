> [!IMPORTANT]
> This project has been consolidated into **[Writer's EDC](https://github.com/sthomasmcclane/writers-edc)**. This repository is now legacy and has been **Archived**. The code remains available for reference, but no further updates will be made here.

# 📝 Disappearing Text Writing App

A minimalist, high-stakes writing environment inspired by "The Most Dangerous Writing App."

## 🚀 The Challenge
Stay focused. Keep typing. If you stop for more than **10 seconds**, your current progress will be wiped clean (though it is automatically saved to `doc.txt` before it disappears, just in case you were actually getting somewhere!).

### 🌈 Visual Feedback
The text color changes as the timer runs down to keep you in the flow:
- **Green**: 10 - 7 seconds remaining.
- **Blue**: 6 - 4 seconds remaining.
- **Red**: 3 - 1 seconds remaining.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sthomasmcclane/Disappearing-Text-Writing-App.git
   cd Disappearing-Text-Writing-App
   ```

2. **Install dependencies**:
   ```bash
   pip install customtkinter
   ```

3. **Run the app**:
   ```bash
   python3 main.py
   ```

## 📸 Screenshots

| Phase | Preview |
| :--- | :--- |
| **Main Screen** | ![app-main](https://i.postimg.cc/Nf7bSR16/Disappearing-Text-1.png) |
| **Warning (Green)** | ![green-text](https://i.postimg.cc/Z5bjS0c1/Disappearing-Text-2.png) |
| **Caution (Blue)** | ![blue-text](https://i.postimg.cc/R0qRW82d/Disappearing-Text-3.png) |
| **Danger (Red)** | ![red-text](https://i.postimg.cc/FHTpsmC1/Disappearing-Text-4.png) |

## 📜 License
This project is open-source and available under the MIT License.
