
# Create the blog.html (Blog Page)
blog_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - Notebook and Nest</title>
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
                    <li><a href="blog.html" class="active">Blog</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="resources.html">Resources</a></li>
                    <li><a href="contact.html">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container">
        <h1 class="section-title">Blog</h1>
        
        <div class="blog-grid">
            <article class="post-card">
                <div class="post-image">📚</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">October 15, 2025</span>
                        <span class="post-category category-phd">PhD</span>
                    </div>
                    <h3>Finding Balance: Homeschool Planning and Dissertation Writing</h3>
                    <p class="post-excerpt">Juggling homeschool lesson plans and academic research requires intentional scheduling and grace. Here's what I've learned about managing both worlds.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>

            <article class="post-card">
                <div class="post-image">🏔️</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">October 10, 2025</span>
                        <span class="post-category category-homeschool">Homeschool</span>
                    </div>
                    <h3>Our Fall Literature Unit: The Hobbit and World Building</h3>
                    <p class="post-excerpt">This month we're diving into Tolkien's world. Discover how we're connecting literature, geography, and creative writing through this beloved classic.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>

            <article class="post-card">
                <div class="post-image">✨</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">October 5, 2025</span>
                        <span class="post-category category-homeschool">Homeschool</span>
                    </div>
                    <h3>Academic Virtues and Character Education at Home</h3>
                    <p class="post-excerpt">What does it mean to cultivate intellectual virtues in our children? Reflections on building character through classical education.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>

            <article class="post-card">
                <div class="post-image">📖</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">September 28, 2025</span>
                        <span class="post-category category-phd">PhD</span>
                    </div>
                    <h3>Reading Notes: Literalism in Contemporary Children's Literature</h3>
                    <p class="post-excerpt">Exploring themes of literalism and imagination in modern children's fiction. How contemporary authors navigate the tension between realism and wonder.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>

            <article class="post-card">
                <div class="post-image">☀️</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">September 20, 2025</span>
                        <span class="post-category category-homeschool">Homeschool</span>
                    </div>
                    <h3>Morning Time Routines That Actually Work</h3>
                    <p class="post-excerpt">After years of trial and error, here's our current morning time routine that brings peace and learning to our homeschool day.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>

            <article class="post-card">
                <div class="post-image">🔬</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">September 12, 2025</span>
                        <span class="post-category category-phd">PhD</span>
                    </div>
                    <h3>Research Update: Sacrifice of Innocence in Speculative Fiction</h3>
                    <p class="post-excerpt">Progress report on my dissertation research examining how children's speculative fiction handles themes of sacrifice and coming of age.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>

            <article class="post-card">
                <div class="post-image">🎨</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">September 5, 2025</span>
                        <span class="post-category category-homeschool">Homeschool</span>
                    </div>
                    <h3>Integrating Art and Literature Study</h3>
                    <p class="post-excerpt">How we use picture study and hands-on art projects to deepen our understanding of the books we're reading together.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>

            <article class="post-card">
                <div class="post-image">💭</div>
                <div class="post-content">
                    <div class="post-meta">
                        <span class="post-date">August 28, 2025</span>
                        <span class="post-category category-phd">PhD</span>
                    </div>
                    <h3>The Rhetoric of Wonder in Middle Grade Fiction</h3>
                    <p class="post-excerpt">How do authors create and sustain a sense of wonder in middle grade literature? Examining narrative techniques across contemporary works.</p>
                    <a href="#" class="read-more">Read More</a>
                </div>
            </article>
        </div>
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

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_html)

print("✓ Blog page created: blog.html")
