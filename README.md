# Family Law Guides

This is a production-ready, statically generated site optimized for organic SEO traffic and Google AdSense.

## Structure
- `index.html`: The homepage.
- `directory/index.html`: Real attorney directory.
- `assets/css/index.css`: Shared global CSS.
- `assets/js/`: Search logic and attorney JSON data.
- `generate_*.py`: Python scripts to auto-generate state, educational, and international articles from templates.

## How to Add New Articles
1. Open the relevant Python generator script (e.g., `generate_edu_guides.py`).
2. Add your new article data (title, desc, slug, content) to the `guides` array.
3. Run `python generate_edu_guides.py` from the root directory.
4. Run `python build_search_index.py` to update the search JSON file.
5. Run `python generate_sitemap.py` to recreate the sitemap.

## AdSense & Analytics Placeholders
- **AdSense Client ID**: Currently set to `ca-pub-YOUR_CLIENT_ID`. Run a global find and replace across all Python scripts and `index.html` files to replace this with your actual AdSense publisher ID.
- **GA4**: Currently set to `G-XXXXXXXXXX`. Replace this with your Google Analytics Measurement ID.
- **Search Console**: Currently set to `YOUR_GSC_VERIFICATION_STRING`.

## Local Development
Run a simple HTTP server to test the site locally:
```bash
python -m http.server
```
Navigate to `http://localhost:8000` in your browser.
