
# Create the about.html (About Page)
about_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About - Notebook and Nest</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;600&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-container">
            <a href="index.html" class="site-logo">Notebook and Nest</a>
            <nav>
                <button class="mobile-menu-toggle" aria-label="Toggle menu">☰</button>
                <ul id="nav-menu">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="about.html" class="active">About</a></li>
                    <li><a href="resources.html">Resources</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="narrow-container">
        <h1 class="section-title">About Me</h1>
        
        <div class="about-section">
            <div class="profile-image">👩‍🏫</div>
            <div class="bio-content">
                <h2>Hello, I'm [Your Name]</h2>
                <p>Welcome to Notebook and Nest! I'm a homeschooling mom and PhD candidate in English Literature, navigating the beautiful intersection of raising readers and becoming a scholar.</p>
                
                <p>My days are filled with read-alouds, math lessons, nature walks, and research on children's literature—specifically how speculative fiction explores themes of sacrifice, innocence, and growing up. From Tolkien to contemporary middle grade authors, I'm fascinated by how stories shape young minds and imaginations.</p>
                
                <p>I live in Maine with my family, where we embrace the changing seasons through nature study, outdoor adventures, and plenty of hot cocoa by the fire. Our homeschool is eclectic and literature-rich, drawing from classical education, Charlotte Mason principles, and our own interests.</p>
            </div>
        </div>

        <section class="section">
            <h2>About This Blog</h2>
            <p>Notebook and Nest is where my two worlds meet. In my "notebook," I share my academic journey—research insights, book recommendations, and reflections on children's literature and literary theory. In my "nest," I document our homeschooling adventures—curriculum choices, what's working (and what's not), and the everyday joys of learning alongside my children.</p>
            
            <p>Whether you're a fellow homeschooler, a lover of children's literature, an academic parent, or simply curious about how these paths can intertwine, I hope you'll find something here that resonates.</p>
            
            <h2>What You'll Find Here</h2>
            <p><strong>Homeschool Reflections:</strong> Practical tips, curriculum reviews, day-in-the-life posts, and honest reflections on the homeschool journey.</p>
            
            <p><strong>Literary Explorations:</strong> Book recommendations, discussions of children's and young adult literature, and insights from my academic research.</p>
            
            <p><strong>PhD Life:</strong> Updates on my dissertation progress, research methodologies, academic writing tips, and the challenges of graduate school while homeschooling.</p>
            
            <p><strong>Resources:</strong> Curated lists of books, curricula, academic articles, and tools that have been helpful on both journeys.</p>
            
            <h2>Let's Connect</h2>
            <p>I'd love to hear from you! Feel free to reach out through the <a href="contact.html">contact page</a> or connect with me on social media. Whether you want to discuss a book, share homeschool encouragement, or chat about academic life, I'm always happy to connect with kindred spirits.</p>
        </section>
    </main>

    <footer>
        <div class="footer-content">
            <div class="footer-links">
                <a href="index.html">Home</a>
                <a href="blog.html">Blog</a>
                <a href="about.html">About</a>
                <a href="resources.html">Resources</a>
                <a href="contact.html">Contact</a>
            </div>
            <p class="copyright">© 2025 Notebook and Nest. All rights reserved.</p>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>"""

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

print("✓ About page created: about.html")
