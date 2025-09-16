# FOSSEE Workshop Booking – UI/UX Enhancement

This repository contains my submission for the **FOSSEE Python Screening Task 1: UI/UX Enhancement**.  

The base project was cloned from the official repository:  
👉 [https://github.com/FOSSEE/workshop_booking](https://github.com/FOSSEE/workshop_booking)  

My task was to improve the **UI/UX** of the website while keeping the core Django structure intact.  


## Demo Video

You can watch the demo video here: [View Demo Video](https://drive.google.com/file/d/1cJ5fHD8SXNxURQJS3ve9PqNgGrqIXgfo/view?usp=sharing)


---

## 🚀 Setup Instructions

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/workshop_booking.git
   cd workshop_booking
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:  
   👉 `http://127.0.0.1:8000/`

---

## 🎨 Design Improvements

Here are the major UI/UX enhancements I implemented:

- **Responsive Navbar**
  - Redesigned with Bootstrap 5.
  - Collapsible menu for mobile devices.
  - Active page highlighting for better navigation.

- **Authentication Pages**
  - Login, logout, and forgot password forms redesigned with **Bootstrap cards** and **form groups**.
  - Clean visual hierarchy with consistent button styles.
  - Fixed password reset form by removing the invalid `add_class` filter.

- **Mobile-First Layout**
  - Used Bootstrap’s grid system to ensure readability on small screens.
  - Optimized spacing, padding, and alignment for mobile devices.

- **Improved Visual Hierarchy**
  - Headings styled with `fw-bold` and spacing utilities.
  - Muted text for descriptions and helper messages.
  - Cards and shadows for content separation.

- **Consistent Theme**
  - Standard Bootstrap colors (`primary`, `secondary`, `success`) applied across all templates.
  - Buttons and links styled consistently for clarity.

- **Accessibility**
  - Proper use of `<label>` elements for form inputs.
  - Bootstrap `aria` attributes leveraged for better screen-reader compatibility.

---

## 🧠 Reasoning

### 1. What design principles guided your improvements?
- **Clarity & Readability:** Forms and navigation were reorganized with proper labels and spacing.  
- **Consistency:** Colors, buttons, and typography now follow Bootstrap’s design system.  
- **Accessibility:** Labels, aria attributes, and semantic HTML used for inclusivity.  
- **Mobile-first:** Optimized for students accessing on small screens.  

### 2. How did you ensure responsiveness across devices?
- Used **Bootstrap 5 grid system** (`row`, `col-md-*`, `container-fluid`).  
- Navbar is fully collapsible using the Bootstrap `navbar-toggler`.  
- Spacing utilities (`mt-3`, `mb-4`, `p-2`) scale well on all screen sizes.  
- Verified layouts in desktop and mobile views.  

### 3. What trade-offs did you make between design and performance?
- Chose Bootstrap CDN instead of bundling assets → improves maintainability and speed but depends on external network availability.  
- Avoided heavy animations and extra libraries → kept load times fast, but at the cost of minimal interactivity flair.  

### 4. What was the most challenging part of the task and how did you approach it?
- **Challenge:** Fixing broken filters like `add_class` while keeping forms styled cleanly.  
- **Approach:** Removed invalid template filters and used Bootstrap’s native form-control classes directly in templates.  
- Ensured forms looked consistent without needing extra libraries.  

---


## 📸 Screenshots
### Before

<img width="1919" height="897" alt="Screenshot 2025-09-16 151129" src="https://github.com/user-attachments/assets/9c6af540-2633-4574-b2ca-165a0079be51" />




### After

### Login Page
<img width="1900" height="893" alt="Screenshot 2025-09-16 220112" src="https://github.com/user-attachments/assets/919bac68-8477-4cd2-be01-103290f6a71c" />
### Registration Page
<img width="1901" height="895" alt="Screenshot 2025-09-16 220615" src="https://github.com/user-attachments/assets/613caf77-6628-43a8-9e0d-d08116433fe4" />
### Home Page
<img width="1896" height="879" alt="Screenshot 2025-09-16 220257" src="https://github.com/user-attachments/assets/6908e90d-7952-4e71-9143-fe68fc07d436" />
### WorkShop Statistics
<img width="1898" height="888" alt="Screenshot 2025-09-16 220340" src="https://github.com/user-attachments/assets/41f7c283-9e70-4ed7-b141-0efe73da056a" />
### Propose Workshop
<img width="1901" height="894" alt="Screenshot 2025-09-16 220405" src="https://github.com/user-attachments/assets/373eedbd-81ba-441c-a333-db5ea96b303f" />
### Workshop Type
<img width="1916" height="889" alt="Screenshot 2025-09-16 220424" src="https://github.com/user-attachments/assets/236ae8f9-34bc-4209-aa2f-1ec0e4718dc1" />
### Profile
<img width="1919" height="885" alt="Screenshot 2025-09-16 220503" src="https://github.com/user-attachments/assets/1449871e-1db3-48e9-9020-03fc51bf7a56" />
### Change Password
<img width="1895" height="890" alt="Screenshot 2025-09-16 220529" src="https://github.com/user-attachments/assets/795da250-a0ef-46a2-9ffd-e25b40575cb4" />
### Logout
<img width="1919" height="896" alt="Screenshot 2025-09-16 220551" src="https://github.com/user-attachments/assets/fcf6c7d9-40f7-4780-bfd9-33d9dc1cd5f1" />
### Forgot Password
<img width="1919" height="897" alt="Screenshot 2025-09-16 220944" src="https://github.com/user-attachments/assets/78007e51-ec5d-4ae3-af3e-7de772212ce5" />




---
