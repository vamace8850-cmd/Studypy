# StudyPy - Premium Educational Resource Hub

A beautifully designed, modern website for sharing and discovering premium study resources with a stunning **Neo-Edu Glow Theme** featuring warm neon aesthetics.

## 🌟 Features

### Design & Theme
- **Black & Warm Neon Glow** - Premium dark theme with warm white neon (#fcebd2) and gold accents (#d3a26f)
- **Glassmorphism Cards** - Modern card design with backdrop blur and glowing effects
- **Smooth Animations** - Floating particles, glow pulses, fade-in effects, and hover animations
- **Fully Responsive** - Mobile-first, fully responsive layout for all devices

### Sections

#### 1. **Sticky Navigation Bar**
- Logo with glowing effect
- Menu items: Home, Resources, Categories, Notes, PPTs, About, Contact
- Search functionality with modal
- Dark/Light mode toggle
- Smooth hover effects with glowing highlights
- Mobile hamburger menu

#### 2. **Hero Section**
- Centered StudyPy logo with animated glow
- Bold "StudyPy" heading with neon effect
- "Light Up Your Learning" subtext
- Two CTA buttons with neon glow
- Animated floating particles background
- Radial glow ambiance

#### 3. **Announcement Bar**
- Glowing strip at the top
- Updates about new resources
- Animated pulse effect

#### 4. **Resources Section (Main Feature)**
- Premium card grid layout
- Filter options (Class, Subject, Format)
- Sort options (Newest, Most Downloaded, Trending)
- Resource details:
  - Title and description
  - Category tag (PDF, PPT, ZIP, Worksheet, Question Bank)
  - File size and upload date
  - Download count and star rating
  - Preview and Download buttons
- Neon glow hover effects with shadow
- Smooth glassmorphism design

#### 5. **Trending Section**
- Top 6 most downloaded resources
- Glowing outline cards
- "🔥 Trending" badge
- Download count and ratings
- Trending number indicator

#### 6. **Categories Section**
- Organized category blocks
- Classes (6-12)
- Subjects (Maths, Physics, Chemistry, Biology, SST, English)
- File Types (PDF, PPT, Notes, Worksheets, Question Banks)
- Cool emoji icons with hover animations
- Glowing borders and effects

#### 7. **About Section**
- StudyPy branding and logo
- Company mission and description
- Statistics (Resources, Users, Downloads)
- Social media links (Instagram, YouTube, Telegram)
- Glowing logo animation

#### 8. **Contact Section**
- Contact form with validation
- Contact information
- Email, address, and hours
- Form submission handling

#### 9. **Footer**
- Quick links to sections
- Resource categories
- Social media icons
- Copyright and legal links
- Soft neon top border with glow

### Interactive Features
- ✨ Dark/Light mode toggle with persistence
- 🔍 Search functionality
- ❤️ Favorite button with toggle
- 📥 Download button with feedback
- 👁️ Preview button
- 🎯 Active navigation highlighting on scroll
- 📱 Mobile-responsive hamburger menu
- ⚡ Smooth scroll animations
- 🎨 Hover effects and transitions

## 🎨 Color Scheme

```css
Primary Background: #000000 (Pure Black)
Secondary Background: #0a0a0a, #111111 (Deep Grey)
Neon White: #fcebd2, #f5e9d8 (Warm White)
Gold/Copper Accent: #d3a26f, #caa06a
Glowing Border: rgba(252, 235, 210, 0.2-0.5)
```

## 🔤 Typography

- **Headings**: Montserrat, Poppins (700-800 weight)
- **Body**: Inter (400-600 weight)
- **Monospace**: JetBrains Mono (Code elements)

## 📂 Project Structure

```
study-py/
├── index.html          # Main HTML file with all sections
├── css/
│   └── styles.css      # Complete styling with animations
├── js/
│   └── script.js       # Interactive features and animations
├── assets/
│   └── icons/          # Icon assets (if needed)
├── .github/
│   └── copilot-instructions.md  # Development guidelines
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No server required - runs as static HTML/CSS/JS

### Installation

1. **Clone or Download** the project
2. **Open** `index.html` in your web browser
3. **Enjoy** the StudyPy experience!

### For Development

1. Open the project in VS Code
2. Use **Live Server** extension for development
3. Edit `css/styles.css` for styling changes
4. Edit `js/script.js` for interactivity changes
5. Edit `index.html` for structural changes

## 🎯 Features Guide

### Dark/Light Mode
- Toggle in the navbar (sun/moon icon)
- Preference is saved to localStorage
- Smooth transition between themes

### Search
- Click search icon in navbar
- Type to search resources
- Press Escape to close modal

### Filtering & Sorting
- Use dropdown filters to narrow down resources
- Sort by Newest, Most Downloaded, or Trending
- Filters update the resource grid in real-time

### Favorites
- Click the heart icon on any resource card
- Heart fills when favorited
- State persists during session

### Download
- Click Download button on resource cards
- Button shows feedback during download
- Simulates a 1.5 second download process

## 🔧 Customization

### Changing Colors
Edit the CSS variables in `styles.css` (lines 12-24):
```css
--bg-primary: #000000;           /* Change background */
--neon-white: #fcebd2;           /* Change neon glow */
--gold-accent: #d3a26f;          /* Change accent */
```

### Adding Resources
Edit the resource data in `js/script.js` or modify the HTML directly in `index.html`.

### Changing Fonts
Update the `@import` links in `index.html` and the CSS variables in `styles.css`.

## 🎬 Animations

- **Floating Particles**: Dynamic particles in hero section
- **Glow Pulse**: Breathing glow effect on hero background
- **Fade In Up**: Cards fade in with upward movement
- **Hover Effects**: Cards lift and glow on hover
- **Navigation Glow**: Underline animation on nav links
- **Logo Float**: Logo gently bobs up and down

## 📱 Responsive Breakpoints

- **Mobile**: < 480px (2-column grid, single-column forms)
- **Tablet**: 480px - 768px (adjusted spacing)
- **Desktop**: > 768px (full multi-column layout)

## ♿ Accessibility

- Semantic HTML structure
- ARIA labels on interactive elements
- Keyboard navigation support
- Color contrast compliant
- Focus states on interactive elements

## 🌐 Browser Support

- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 Performance

- Optimized CSS with minimal repaints
- Efficient JavaScript with debouncing
- Smooth animations using transform and opacity
- Minimal external dependencies (Google Fonts only)

## 🛠️ Advanced Customization

### Adding New Sections
1. Create a new `<section>` in `index.html`
2. Add corresponding CSS in `styles.css`
3. Add JavaScript interactivity in `js/script.js` if needed

### Modifying Animations
- Edit `@keyframes` in `css/styles.css`
- Adjust `--transition-*` variables for timing
- Use Chrome DevTools to test animation timing

### Database Integration
- Replace sample resource data in `js/script.js` with API calls
- Use `fetch()` to load resources from backend
- Update `renderResources()` function for new data structure

## 🐛 Troubleshooting

### Theme not persisting?
- Check browser's localStorage is enabled
- Clear cache and reload

### Animations stuttering?
- Disable some particle animations in `createParticles()`
- Reduce particle count

### Mobile menu not closing?
- Check z-index values in CSS
- Ensure hamburger toggle has proper event listeners

## 📄 License

This project is a premium educational resource hub template. Feel free to use and modify for your needs.

## 🤝 Contributing

To improve this project:
1. Test on multiple devices
2. Suggest UI/UX improvements
3. Report bugs and issues
4. Share design enhancements

## 📞 Support

For questions or issues:
- Check the code comments
- Review CSS variable definitions
- Test in Chrome DevTools
- Check browser console for errors

## 🎉 Credits

Created with ❤️ for educational excellence.

**StudyPy** - Light Up Your Learning ✨

---

### Version: 1.0.0
### Last Updated: December 2024
