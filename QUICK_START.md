# StudyPy - Quick Start Guide

## 🚀 How to Run the Website

### Option 1: Using VS Code Live Server (Recommended)

1. **Install Live Server Extension**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Live Server"
   - Install by Ritwick Dey

2. **Start the Server**
   - Right-click on `index.html`
   - Select "Open with Live Server"
   - Your default browser will open the website

3. **Enjoy!**
   - The website will automatically refresh when you save changes
   - You'll see the full StudyPy experience

### Option 2: Using Python Built-in Server

1. **Open Terminal in Project Directory**
   ```powershell
   cd c:\Users\Admin\Desktop\study-py
   ```

2. **Start Python Server**
   ```powershell
   python -m http.server 8000
   ```

3. **Open in Browser**
   - Go to: `http://localhost:8000`

### Option 3: Using Node.js HTTP Server

1. **Install http-server globally**
   ```powershell
   npm install -g http-server
   ```

2. **Start the Server**
   ```powershell
   http-server
   ```

3. **Open in Browser**
   - Go to: `http://127.0.0.1:8080` (or the URL shown in terminal)

### Option 4: Direct Browser Open

1. **Simply open the file**
   - Double-click `index.html`
   - Or right-click → Open with → Your Browser

2. **Note**: Some JavaScript features may be limited without a proper server

---

## 🎨 What to Expect

When you open the website, you'll see:

✨ **Stunning Dark Theme**
- Black background with warm neon glow
- Glowing text and borders
- Smooth animations and transitions

📱 **Fully Responsive Design**
- Perfect on desktop, tablet, and mobile
- Hamburger menu on smaller screens
- Optimized touch interactions

⚡ **Interactive Features**
- Dark/Light mode toggle
- Search functionality
- Filter and sort resources
- Favorite/like buttons
- Working contact form
- Smooth scroll animations

🎯 **Complete Sections**
- Sticky navigation bar
- Hero section with animated logo
- Resources grid with cards
- Trending section
- Categories showcase
- About & Contact sections
- Professional footer

---

## 🔧 Development Tips

### Edit Styles
- Open `css/styles.css`
- Make changes
- Save (Live Server will auto-refresh)

### Edit Content
- Open `index.html`
- Modify text, add resources
- Save to see changes

### Edit Interactivity
- Open `js/script.js`
- Modify JavaScript
- Save and check browser console for errors

### Test Responsive Design
- Press F12 to open DevTools
- Click Device Toolbar (Ctrl+Shift+M)
- Test on various screen sizes

### Check for Errors
- Press F12 → Console tab
- Look for any red error messages
- Fix issues in the code

---

## 💡 Customization Ideas

1. **Add Real Resources**
   - Replace sample data in `js/script.js`
   - Add actual PDF/PPT files

2. **Connect to Database**
   - Replace filter/sort with API calls
   - Load resources from backend server

3. **Add User Accounts**
   - Add login/signup page
   - Save favorites to database
   - Track downloads per user

4. **Change Colors**
   - Edit CSS variables in `styles.css` (top of file)
   - Adjust colors to match your brand

5. **Add More Sections**
   - Create new HTML sections
   - Style with CSS
   - Add JavaScript for interactivity

---

## 📞 Troubleshooting

### Website looks broken?
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R)
- Check browser console for errors (F12)

### Animations not smooth?
- Try different browser
- Close other applications
- Check graphics settings

### Mobile menu stuck?
- Refresh page
- Clear browser cache
- Try different browser

### Images not loading?
- For file:// URLs, some images may not load
- Use a proper web server (options above)

---

## 🎉 You're All Set!

Enjoy your **StudyPy** experience! 

**Light Up Your Learning** ✨

For more information, see `README.md`
