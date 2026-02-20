# University Graphics & Algorithms Project

A comprehensive collection of computer graphics algorithms and image processing implementations, including Bresenham's line, circle, and ellipse drawing algorithms, convolution-based image filtering, and binary number comparison algorithms.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
  - [Bresenham's Line Algorithm](#bresenhams-line-algorithm)
  - [Bresenham's Circle Algorithm](#bresenhams-circle-algorithm)
  - [Bresenham's Ellipse Algorithm](#bresenhams-ellipse-algorithm)
  - [Image Convolution](#image-convolution)
  - [Binary Number Comparison](#binary-number-comparison)
- [Requirements](#requirements)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project implements fundamental computer graphics algorithms and image processing techniques commonly used in computer science and graphics programming. The implementations are educational and demonstrate core concepts in rasterization, image filtering, and binary arithmetic.

## Features

- ✅ **Bresenham's Line Drawing Algorithm** - Efficient line rasterization
- ✅ **Bresenham's Circle Drawing Algorithm** - Fast circle generation
- ✅ **Bresenham's Ellipse Drawing Algorithm** - Ellipse rasterization
- ✅ **Image Convolution** - Multiple filter implementations (blur, edge detection, sharpening)
- ✅ **Binary Number Comparison** - Grouping and comparison algorithms

## Project Structure

```
university/
├── geraphik/                    # Graphics algorithms
│   ├── bresenham_line/          # Line drawing implementation
│   │   ├── line.py
│   │   └── line.png
│   ├── bresenham_circle/        # Circle drawing implementation
│   │   ├── circle.py
│   │   └── circle_figure.png
│   ├── bresenham_ellipse/       # Ellipse drawing implementation
│   │   ├── ellipse.py
│   │   └── ellipse.png
│   └── convolution/             # Image processing
│       ├── convolution.py
│       ├── image.jpg
│       └── filtered_image*.jpg
└── madar/                       # Binary number algorithms
    └── az-madar.py
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Dependencies

Install required packages:

```bash
pip install matplotlib numpy pillow
```

Or using requirements.txt:

```bash
pip install -r requirements.txt
```

## Usage

### Running Bresenham's Line Algorithm

```bash
cd geraphik/bresenham_line
python line.py
```

### Running Bresenham's Circle Algorithm

```bash
cd geraphik/bresenham_circle
python circle.py
```

### Running Bresenham's Ellipse Algorithm

```bash
cd geraphik/bresenham_ellipse
python ellipse.py
```

### Running Image Convolution

```bash
cd geraphik/convolution
python convolution.py
```

**Note:** Update the image path in `convolution.py` (line 26) to point to your image file.

### Running Binary Number Comparison

```bash
cd madar
python az-madar.py
```

## Algorithms

### Bresenham's Line Algorithm

**File:** `geraphik/bresenham_line/line.py`

Bresenham's line algorithm is an efficient method for drawing lines on a raster display. It uses only integer arithmetic, making it faster than algorithms that require floating-point calculations.

**How it works:**
1. Calculates the difference in x and y coordinates (dx, dy)
2. Determines the step direction (sx, sy)
3. Uses an error term to decide whether to increment y when moving along x (or vice versa)
4. Generates all points on the line between two endpoints

**Parameters:**
- `x1, y1`: Starting point coordinates
- `x2, y2`: Ending point coordinates

**Example:**
```python
points = bresenham(21, 12, 29, 16)
```

### Bresenham's Circle Algorithm

**File:** `geraphik/bresenham_circle/circle.py`

This algorithm draws circles efficiently using only integer arithmetic. It exploits the eight-way symmetry of circles to generate all points.

**How it works:**
1. Starts at the top of the circle (x=0, y=radius)
2. Uses a decision parameter `d` to choose between moving right or diagonally down-right
3. Plots points in all eight octants simultaneously using symmetry
4. Continues until the algorithm reaches the 45° line

**Parameters:**
- `x_center, y_center`: Center coordinates of the circle
- `radius`: Radius of the circle

**Example:**
```python
points = bresenham_circle(0, 15, 15)
```

### Bresenham's Ellipse Algorithm

**File:** `geraphik/bresenham_ellipse/ellipse.py`

An extension of Bresenham's algorithm for drawing ellipses. It handles the two regions of an ellipse separately due to different slopes.

**How it works:**
1. Divides the ellipse into two regions at the point where the slope equals -1
2. In region 1 (dx < dy): Moves horizontally, adjusting y when needed
3. In region 2 (y > 0): Moves vertically, adjusting x when needed
4. Uses four-way symmetry to plot points in all quadrants

**Parameters:**
- `x_center, y_center`: Center coordinates
- `a`: Semi-major axis (horizontal radius)
- `b`: Semi-minor axis (vertical radius)

**Example:**
```python
points = bresenham_ellipse(0, 2, 10, 2)
```

### Image Convolution

**File:** `geraphik/convolution/convolution.py`

Implements 2D convolution for image filtering. Convolution is a fundamental operation in image processing used for blurring, sharpening, edge detection, and more.

**How it works:**
1. Slides a kernel (filter matrix) over the image
2. At each position, multiplies overlapping values and sums them
3. The result becomes the new pixel value
4. Applies three different filters:
   - **Filter 1**: Box blur (averaging filter)
   - **Filter 2**: Edge detection (Laplacian-like)
   - **Filter 3**: Sharpening filter

**Filters:**
- **Blur Filter**: `[[1,1,1], [1,1,1], [1,1,1]]` - Averages neighboring pixels
- **Edge Detection**: `[[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]` - Highlights edges
- **Sharpening**: `[[0,-1,0], [-1,5,-1], [0,-1,0]]` - Enhances image details

**Usage:**
```python
filtered_image = convolve(image_array, kernel)
```

### Binary Number Comparison

**File:** `madar/az-madar.py`

Implements a binary number grouping and comparison algorithm. It generates groups of binary numbers and categorizes them based on similarity.

**How it works:**
1. **`generic_list(n)`**: Generates n groups, each containing 9 binary numbers (5-bit each)
2. **`convert(num)`**: Converts binary digits (0→1, 1→0) - complement operation
3. **`plus(num1, num2)`**: Adds two binary numbers using binary arithmetic
4. **`minus(num1, num2)`**: Subtracts num2 from num1 using two's complement
5. **`Comparison(group)`**: Compares all pairs in a group and categorizes similar numbers

**Algorithm Flow:**
- Generates 50 groups of 9 binary numbers each
- Compares each number with all others in the group
- Groups numbers that are similar (difference < threshold) in more than 4 out of 9 positions
- Returns categorized groups

## Requirements

- **Python**: 3.7+
- **matplotlib**: For plotting and visualization
- **numpy**: For numerical operations and array handling
- **Pillow (PIL)**: For image loading and processing

## Examples

### Example 1: Drawing a Line

```python
from geraphik.bresenham_line.line import bresenham
import matplotlib.pyplot as plt

points = bresenham(0, 0, 10, 5)
x_coords, y_coords = zip(*points)
plt.scatter(x_coords, y_coords)
plt.show()
```

### Example 2: Drawing a Circle

```python
from geraphik.bresenham_circle.circle import bresenham_circle
import matplotlib.pyplot as plt

points = bresenham_circle(0, 0, 10)
x_coords, y_coords = zip(*points)
plt.scatter(x_coords, y_coords)
plt.show()
```

### Example 3: Image Filtering

```python
from geraphik.convolution.convolution import convolve
from PIL import Image
import numpy as np

image = Image.open('image.jpg').convert('L')
image_array = np.array(image)

# Edge detection kernel
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

filtered = convolve(image_array, kernel)
result = Image.fromarray(filtered.astype(np.uint8))
result.save('output.jpg')
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is for educational purposes.

---

# 📖 راهنمای فارسی

## معرفی پروژه

این پروژه مجموعه‌ای جامع از الگوریتم‌های گرافیک کامپیوتری و پردازش تصویر است که شامل الگوریتم‌های ترسیم خط، دایره و بیضی برزنهام، فیلترگذاری تصویر با کانولوشن، و الگوریتم‌های مقایسه اعداد باینری می‌شود.

## ویژگی‌ها

- ✅ **الگوریتم ترسیم خط برزنهام** - رسترایز کردن کارآمد خطوط
- ✅ **الگوریتم ترسیم دایره برزنهام** - تولید سریع دایره
- ✅ **الگوریتم ترسیم بیضی برزنهام** - رسترایز کردن بیضی
- ✅ **کانولوشن تصویر** - پیاده‌سازی چندین فیلتر (تار کردن، تشخیص لبه، تیز کردن)
- ✅ **مقایسه اعداد باینری** - الگوریتم‌های گروه‌بندی و مقایسه

## ساختار پروژه

```
university/
├── geraphik/                    # الگوریتم‌های گرافیک
│   ├── bresenham_line/          # پیاده‌سازی ترسیم خط
│   │   ├── line.py
│   │   └── line.png
│   ├── bresenham_circle/        # پیاده‌سازی ترسیم دایره
│   │   ├── circle.py
│   │   └── circle_figure.png
│   ├── bresenham_ellipse/       # پیاده‌سازی ترسیم بیضی
│   │   ├── ellipse.py
│   │   └── ellipse.png
│   └── convolution/             # پردازش تصویر
│       ├── convolution.py
│       ├── image.jpg
│       └── filtered_image*.jpg
└── madar/                       # الگوریتم‌های اعداد باینری
    └── az-madar.py
```

## نصب

### پیش‌نیازها

- Python 3.7 یا بالاتر
- pip (مدیر بسته Python)

### وابستگی‌ها

نصب پکیج‌های مورد نیاز:

```bash
pip install matplotlib numpy pillow
```

## نحوه استفاده

### اجرای الگوریتم خط برزنهام

```bash
cd geraphik/bresenham_line
python line.py
```

### اجرای الگوریتم دایره برزنهام

```bash
cd geraphik/bresenham_circle
python circle.py
```

### اجرای الگوریتم بیضی برزنهام

```bash
cd geraphik/bresenham_ellipse
python ellipse.py
```

### اجرای کانولوشن تصویر

```bash
cd geraphik/convolution
python convolution.py
```

**توجه:** مسیر تصویر در فایل `convolution.py` (خط 26) را به فایل تصویر خود تغییر دهید.

### اجرای مقایسه اعداد باینری

```bash
cd madar
python az-madar.py
```

## توضیح الگوریتم‌ها

### الگوریتم خط برزنهام

**فایل:** `geraphik/bresenham_line/line.py`

الگوریتم خط برزنهام روشی کارآمد برای ترسیم خطوط روی نمایشگر رستری است. این الگوریتم فقط از محاسبات عدد صحیح استفاده می‌کند و سریع‌تر از الگوریتم‌هایی است که نیاز به محاسبات اعشاری دارند.

**نحوه کار:**
1. تفاوت مختصات x و y را محاسبه می‌کند (dx, dy)
2. جهت حرکت را تعیین می‌کند (sx, sy)
3. از یک پارامتر خطا برای تصمیم‌گیری در مورد افزایش y هنگام حرکت در راستای x استفاده می‌کند
4. تمام نقاط روی خط بین دو نقطه انتهایی را تولید می‌کند

**پارامترها:**
- `x1, y1`: مختصات نقطه شروع
- `x2, y2`: مختصات نقطه پایان

### الگوریتم دایره برزنهام

**فایل:** `geraphik/bresenham_circle/circle.py`

این الگوریتم دایره‌ها را به صورت کارآمد با استفاده از محاسبات عدد صحیح ترسیم می‌کند. از تقارن هشت‌گانه دایره برای تولید تمام نقاط استفاده می‌کند.

**نحوه کار:**
1. از بالای دایره شروع می‌کند (x=0, y=radius)
2. از یک پارامتر تصمیم `d` برای انتخاب بین حرکت به راست یا مورب پایین-راست استفاده می‌کند
3. نقاط را در هر هشت اکتانت به طور همزمان با استفاده از تقارن رسم می‌کند
4. تا رسیدن به خط 45 درجه ادامه می‌دهد

**پارامترها:**
- `x_center, y_center`: مختصات مرکز دایره
- `radius`: شعاع دایره

### الگوریتم بیضی برزنهام

**فایل:** `geraphik/bresenham_ellipse/ellipse.py`

گسترش الگوریتم برزنهام برای ترسیم بیضی. این الگوریتم دو ناحیه بیضی را به دلیل شیب‌های مختلف به صورت جداگانه مدیریت می‌کند.

**نحوه کار:**
1. بیضی را در نقطه‌ای که شیب برابر -1 است به دو ناحیه تقسیم می‌کند
2. در ناحیه 1 (dx < dy): به صورت افقی حرکت می‌کند و در صورت نیاز y را تنظیم می‌کند
3. در ناحیه 2 (y > 0): به صورت عمودی حرکت می‌کند و در صورت نیاز x را تنظیم می‌کند
4. از تقارن چهارگانه برای رسم نقاط در تمام ربع‌ها استفاده می‌کند

**پارامترها:**
- `x_center, y_center`: مختصات مرکز
- `a`: نیم‌محور بزرگ (شعاع افقی)
- `b`: نیم‌محور کوچک (شعاع عمودی)

### کانولوشن تصویر

**فایل:** `geraphik/convolution/convolution.py`

کانولوشن دو بعدی برای فیلترگذاری تصویر را پیاده‌سازی می‌کند. کانولوشن یک عملیات اساسی در پردازش تصویر است که برای تار کردن، تیز کردن، تشخیص لبه و موارد دیگر استفاده می‌شود.

**نحوه کار:**
1. یک کرنل (ماتریس فیلتر) را روی تصویر می‌لغزاند
2. در هر موقعیت، مقادیر همپوشانی را ضرب کرده و جمع می‌کند
3. نتیجه به عنوان مقدار پیکسل جدید استفاده می‌شود
4. سه فیلتر مختلف اعمال می‌کند:
   - **فیلتر 1**: تار کردن جعبه‌ای (فیلتر میانگین)
   - **فیلتر 2**: تشخیص لبه (شبیه لاپلاسین)
   - **فیلتر 3**: فیلتر تیز کردن

**فیلترها:**
- **فیلتر تار کردن**: `[[1,1,1], [1,1,1], [1,1,1]]` - میانگین پیکسل‌های مجاور
- **تشخیص لبه**: `[[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]` - برجسته کردن لبه‌ها
- **تیز کردن**: `[[0,-1,0], [-1,5,-1], [0,-1,0]]` - بهبود جزئیات تصویر

### مقایسه اعداد باینری

**فایل:** `madar/az-madar.py`

الگوریتم گروه‌بندی و مقایسه اعداد باینری را پیاده‌سازی می‌کند. این الگوریتم گروه‌هایی از اعداد باینری تولید کرده و آن‌ها را بر اساس شباهت دسته‌بندی می‌کند.

**نحوه کار:**
1. **`generic_list(n)`**: n گروه تولید می‌کند که هر کدام شامل 9 عدد باینری 5 بیتی است
2. **`convert(num)`**: ارقام باینری را تبدیل می‌کند (0→1, 1→0) - عملیات متمم
3. **`plus(num1, num2)`**: دو عدد باینری را با استفاده از محاسبات باینری جمع می‌کند
4. **`minus(num1, num2)`**: num2 را از num1 با استفاده از متمم دو کم می‌کند
5. **`Comparison(group)`**: تمام جفت‌ها را در یک گروه مقایسه کرده و اعداد مشابه را دسته‌بندی می‌کند

**جریان الگوریتم:**
- 50 گروه از 9 عدد باینری تولید می‌کند
- هر عدد را با تمام اعداد دیگر در گروه مقایسه می‌کند
- اعدادی که در بیش از 4 موقعیت از 9 موقعیت مشابه هستند را گروه‌بندی می‌کند
- گروه‌های دسته‌بندی شده را برمی‌گرداند

## نیازمندی‌ها

- **Python**: 3.7+
- **matplotlib**: برای رسم و تجسم
- **numpy**: برای عملیات عددی و مدیریت آرایه
- **Pillow (PIL)**: برای بارگذاری و پردازش تصویر

## مثال‌ها

### مثال 1: ترسیم یک خط

```python
from geraphik.bresenham_line.line import bresenham
import matplotlib.pyplot as plt

points = bresenham(0, 0, 10, 5)
x_coords, y_coords = zip(*points)
plt.scatter(x_coords, y_coords)
plt.show()
```

### مثال 2: ترسیم یک دایره

```python
from geraphik.bresenham_circle.circle import bresenham_circle
import matplotlib.pyplot as plt

points = bresenham_circle(0, 0, 10)
x_coords, y_coords = zip(*points)
plt.scatter(x_coords, y_coords)
plt.show()
```

### مثال 3: فیلترگذاری تصویر

```python
from geraphik.convolution.convolution import convolve
from PIL import Image
import numpy as np

image = Image.open('image.jpg').convert('L')
image_array = np.array(image)

# کرنل تشخیص لبه
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

filtered = convolve(image_array, kernel)
result = Image.fromarray(filtered.astype(np.uint8))
result.save('output.jpg')
```

## مشارکت

مشارکت‌ها خوش‌آمد هستند! لطفاً Pull Request ارسال کنید.

## مجوز

این پروژه برای اهداف آموزشی است.

