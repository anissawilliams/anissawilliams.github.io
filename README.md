# Anissa Williams - Data Portfolio

A config-driven portfolio site with Garnet & Gold theming.

## 🚀 Quick Start

### Option 1: GitHub Pages (Recommended - Free, No Wake-up)

1. Create a new GitHub repo named `anissawilliams.github.io` (or any name)
2. Upload all files from this folder to the repo
3. Go to **Settings → Pages → Source** → Select `main` branch
4. Your site will be live at `https://anissawilliams.github.io`

### Option 2: Netlify (Also Free, No Wake-up)

1. Go to [netlify.com](https://netlify.com) and sign in with GitHub
2. Click "Add new site" → "Import an existing project"
3. Connect your GitHub repo
4. Deploy! (Netlify auto-detects static sites)

---

## 📝 How to Update Your Portfolio

### Editing Content

All content is controlled by `config.yaml`. Edit this file to:

- Update your bio/tagline
- Add/remove projects
- Change project descriptions
- Update links

```yaml
# Example: Adding a new project
projects:
  - id: "my-new-project"
    title: "My New Project"
    short_description: "One-liner for the homepage card"
    long_description: |
      Longer description that appears on the project page.
      Can be multiple lines.
    tags:
      - "Python"
      - "ML"
    featured: true  # Makes it appear larger/first
    screenshots:
      - "my-project-1.png"
      - "my-project-2.png"
    links:
      github: "https://github.com/anissawilliams/my-project"
      live: "https://my-project-demo.com"
      colab: "https://colab.research.google.com/..."
```

### Adding Screenshots

1. Add your image files to `assets/projects/`
2. Update `config.yaml` with the filenames:
   ```yaml
   screenshots:
     - "my-screenshot.png"
   ```

### Adding a New Project Page

1. Copy any existing file in `projects/` (they're all the same template)
2. Rename it to match your project ID: `my-new-project.html`
3. Add the project to `config.yaml`

That's it! The page auto-loads content from the config.

---

## 📁 File Structure

```
portfolio/
├── index.html              # Homepage
├── config.yaml             # ✏️ EDIT THIS to update content
├── README.md               # This file
├── assets/
│   ├── headshot.png        # Your photo
│   └── projects/           # 📸 Drop screenshots here
│       ├── java-tutor-1.png
│       ├── cfb-chaos-1.png
│       └── ...
└── projects/               # Individual project pages
    ├── java-tutor.html
    ├── cfb-chaos.html
    └── ...
```

---

## 🎨 Theme Colors

The portfolio uses FSU/CofC Garnet & Gold:

- **Garnet**: `#782F40`
- **Gold**: `#CEB888`

To customize colors, edit the `:root` CSS variables in `index.html`.

---

## 💡 Tips

1. **Screenshots matter**: Coaches will scan visually first. Add your best viz screenshots!

2. **Featured projects**: Set `featured: true` for your top 2-3 projects. They appear larger and first.

3. **Keep descriptions short**: The homepage cards should be scannable. Save details for project pages.

4. **Test locally**: Open `index.html` in your browser to preview changes before pushing.
   - Note: Due to CORS, you may need to run a local server:
   ```bash
   python -m http.server 8000
   # Then open http://localhost:8000
   ```

5. **Commit often**: GitHub Pages auto-deploys on every push to main.

---

## 🐛 Troubleshooting

**Site not updating?**
- GitHub Pages can take 1-2 minutes to deploy
- Hard refresh your browser (Cmd+Shift+R or Ctrl+Shift+R)

**Screenshots not showing?**
- Check the filename matches exactly (case-sensitive)
- Make sure the image is in `assets/projects/`

**YAML errors?**
- Use a YAML validator: https://yamlvalidator.com
- Watch for indentation (use spaces, not tabs)

---

Built with ☕ and data.
