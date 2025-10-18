
# Create a README file with GitHub Pages deployment instructions
readme_content = """# Notebook and Nest
A personal website for sharing homeschooling and PhD journey content.

## About
This is a simple, static website designed to be hosted on GitHub Pages. It features a clean, warm neutral color palette suitable for both homeschool and literary academic audiences.

## Pages Included
- **Home** (index.html) - Welcome page with featured blog posts
- **Blog** (blog.html) - Full blog post listing
- **About** (about.html) - About the author and the blog
- **Resources** (resources.html) - Curated homeschool and academic resources
- **Contact** (contact.html) - Contact form and social media links

## Design Features
- Warm, neutral color palette (cream, beige, sage green, terracotta)
- Fully responsive design (mobile, tablet, desktop)
- Clean typography using Google Fonts
- Accessible and readable layout
- Smooth transitions and hover effects

## How to Deploy on GitHub Pages

### Method 1: Using GitHub Web Interface (No Command Line Required)

1. **Create a GitHub Account**
   - Go to https://github.com and sign up for a free account
   - Verify your email address

2. **Create a New Repository**
   - Click the "+" icon in the top right corner
   - Select "New repository"
   - Name it: `yourusername.github.io` (replace "yourusername" with your actual GitHub username)
   - Make sure it's set to "Public"
   - Click "Create repository"

3. **Upload Your Files**
   - On your repository page, click "uploading an existing file"
   - Drag and drop all the website files:
     - index.html
     - blog.html
     - about.html
     - resources.html
     - contact.html
     - styles.css
     - script.js
   - Add a commit message like "Initial website upload"
   - Click "Commit changes"

4. **Enable GitHub Pages**
   - Go to your repository's "Settings" tab
   - Scroll down to "Pages" in the left sidebar
   - Under "Source", select "Deploy from a branch"
   - Select "main" branch and "/ (root)" folder
   - Click "Save"

5. **Access Your Website**
   - Your website will be live at: `https://yourusername.github.io`
   - It may take 5-10 minutes for the first deployment

### Method 2: Using Git Command Line

```bash
# Clone your repository
git clone https://github.com/yourusername/yourusername.github.io.git
cd yourusername.github.io

# Add your website files to the folder
# (Copy all HTML, CSS, and JS files to this directory)

# Add files to git
git add .

# Commit changes
git commit -m "Initial website upload"

# Push to GitHub
git push origin main
```

## Customization Tips

### Update Your Information
1. **About Page** - Replace placeholder text with your actual bio
2. **Profile Image** - Add your actual photo or logo
3. **Contact Page** - Update email address and social media links
4. **Blog Posts** - Replace placeholder posts with your actual content

### Colors
The color scheme is defined in the `:root` section of `styles.css`:
- `--bg-primary`: #FAF8F5 (soft cream)
- `--bg-secondary`: #F5F1E8 (warm beige)
- `--accent-sage`: #A8B5A0 (sage green)
- `--accent-rust`: #C57B57 (warm terracotta)
- `--text-dark`: #2C2C2C (dark charcoal)

### Making the Contact Form Work
The contact form is currently non-functional (static HTML only). To make it work, integrate one of these services:
- **Formspree** (https://formspree.io/) - Free tier available, easy setup
- **Netlify Forms** (requires hosting on Netlify)
- **EmailJS** (https://www.emailjs.com/) - Free tier available
- **Google Forms** - Create a form and embed it

### Adding Blog Posts
To add new blog posts:
1. Create individual HTML files for each post (e.g., `post-1.html`)
2. Update the "Read More" links in `blog.html` to point to these files
3. Use the same template structure as the other pages
4. Add the post preview to both `index.html` and `blog.html`

### Custom Domain (Optional)
To use a custom domain:
1. Purchase a domain from a registrar (Namecheap, Google Domains, etc.)
2. In your repository, create a file named `CNAME` (no extension)
3. Add your domain name to the file (e.g., `www.yoursite.com`)
4. Configure your domain's DNS settings according to GitHub's instructions:
   https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

## File Structure
```
yourusername.github.io/
├── index.html          # Home page
├── blog.html           # Blog listing page
├── about.html          # About page
├── resources.html      # Resources page
├── contact.html        # Contact page
├── styles.css          # Main stylesheet
├── script.js           # JavaScript functionality
└── README.md           # This file
```

## Technologies Used
- HTML5
- CSS3
- JavaScript (ES6)
- Google Fonts (Lora & Open Sans)

## Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License
This website template is free to use and customize for personal projects.

## Support
For GitHub Pages documentation, visit:
https://docs.github.com/en/pages

For questions about this template, feel free to reach out through the website's contact page.

---

© 2025 Notebook and Nest. Built with love for homeschoolers and literature lovers.
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✓ README.md created with deployment instructions")
print("\nAll files created successfully!")
print("\nFiles included:")
print("  • index.html (Home page)")
print("  • blog.html (Blog page)")
print("  • about.html (About page)")
print("  • resources.html (Resources page)")
print("  • contact.html (Contact page)")
print("  • styles.css (Stylesheet)")
print("  • script.js (JavaScript)")
print("  • README.md (Deployment guide)")
