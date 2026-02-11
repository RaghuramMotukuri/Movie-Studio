# 📝 Changelog

## Version 2.0 - 2026-02-10

### 🎉 Major Release - All Features Added!

#### ✨ New Features

1. **💾 Project Management (Local Storage)**
   - Save up to 10 projects in browser storage
   - Load saved projects instantly
   - Delete unwanted projects
   - View project metadata (date, characters, complexity)
   - Beautiful modal interface for project browsing

2. **📄 PDF Export**
   - Professional PDF generation with ReportLab
   - Color-coded sections and tables
   - Complete production package included
   - Auto-timestamped filenames
   - One-click download

3. **🎥 Video Generation API Integration**
   - Hugging Face API integration (text-to-video)
   - Free tier support
   - Fallback to demo video if no API key
   - Model: damo-vilab/text-to-video-ms-1.7b
   - 30-60 second generation time

4. **🌐 Deployment Support**
   - Created `Procfile` for Render/Heroku
   - Created `vercel.json` for Vercel
   - Created `runtime.txt` for Python version
   - Updated `.gitignore` for deployment
   - Added gunicorn for production server

5. **📚 Comprehensive Documentation**
   - `DEPLOYMENT_GUIDE.md` - 6 deployment options with step-by-step instructions
   - `FREE_APIS_GUIDE.md` - 15+ free APIs with setup guides
   - `FEATURES_GUIDE.md` - Complete feature documentation
   - `QUICK_START.md` - 60-second setup guide
   - `PROJECT_STATUS.md` - Current project status
   - `CHANGELOG.md` - This file

#### 🔧 Technical Improvements

- Added `reportlab==4.0.7` for PDF generation
- Added `Pillow==10.1.0` for image processing
- Added `requests==2.31.0` for HTTP requests
- Added `gunicorn==21.2.0` for production deployment
- Updated `google-generativeai` to 0.8.5
- Updated Flask to 3.1.2

#### 🎨 UI Enhancements

- Added "Save Project" button (blue)
- Added "My Projects" button (green)
- Added "Export to PDF" button (red)
- Added projects modal with beautiful card layout
- Improved button layouts and spacing
- Added loading states for all async operations
- Better error messaging

#### 🐛 Bug Fixes

- Fixed confusion about "Failed to generate script" error message
- Verified all API endpoints working correctly
- Tested PDF export functionality
- Confirmed localStorage save/load working

---

## Version 1.0 - Initial Release

### Features

1. **AI-Powered Generation**
   - Screenplay generation with Gemini API
   - Character creation (3-5 characters)
   - Production complexity scoring (1-10)
   - Video animation prompts

2. **Beautiful UI**
   - Tailwind CSS design
   - Purple/blue gradient theme
   - Responsive layout
   - Loading spinners

3. **Video Demo**
   - Placeholder video generation
   - Video player integration
   - Download button

4. **Core Functionality**
   - Flask web server
   - Environment variable support
   - Error handling
   - JSON response parsing

---

## Roadmap

### Potential Future Features

- [ ] User authentication
- [ ] Cloud database integration (Firebase)
- [ ] Multiple theme options
- [ ] Export to JSON
- [ ] Email sharing
- [ ] Music generation (Suno/MusicGen)
- [ ] Voice generation (ElevenLabs)
- [ ] Image generation for storyboards
- [ ] Version history for projects
- [ ] Collaborative editing
- [ ] Analytics dashboard
- [ ] Custom complexity parameters

---

## Migration Notes

### From v1.0 to v2.0

**New Dependencies Required**:
```bash
pip install reportlab Pillow
```

**New Environment Variables (Optional)**:
```bash
HUGGINGFACE_API_TOKEN=your-token-here
```

**No Breaking Changes**: All v1.0 features still work exactly the same!

---

## Credits

- **AI**: Google Gemini 2.5 Flash
- **Video**: Hugging Face (damo-vilab/text-to-video-ms-1.7b)
- **PDF**: ReportLab
- **UI**: Tailwind CSS
- **Framework**: Flask

---

*Stay tuned for more updates!* 🚀
