# 🚀 Deployment Guide - Share Your Movie Production Studio

## Quick Share Options (Easiest to Hardest)

---

## 🌐 Option 1: ngrok (Easiest - 2 minutes)

**Best for**: Quick demos, temporary sharing  
**Cost**: FREE  
**Duration**: Temporary URL (expires when you close it)

### Steps:

1. **Download ngrok**:
   ```bash
   # Download from: https://ngrok.com/download
   # Or using chocolatey:
   choco install ngrok
   ```

2. **Sign up** (free): https://dashboard.ngrok.com/signup

3. **Get your authtoken**:
   - Go to: https://dashboard.ngrok.com/get-started/your-authtoken
   - Copy your token

4. **Configure ngrok**:
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```

5. **Start your Flask app**:
   ```bash
   python app.py
   ```

6. **In a NEW terminal, run ngrok**:
   ```bash
   ngrok http 5000
   ```

7. **Share the URL**:
   - You'll see something like: `https://abc123.ngrok.io`
   - Share this URL with your friends!
   - They can access it from anywhere in the world

**Pros**: ✅ Instant, ✅ No configuration, ✅ HTTPS included  
**Cons**: ❌ URL changes each time, ❌ Temporary

---

## 🌍 Option 2: Render.com (Easy - FREE Forever)

**Best for**: Permanent free hosting  
**Cost**: FREE (with limitations)  
**Duration**: Permanent

### Steps:

1. **Create a GitHub repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   # Create repo on GitHub, then:
   git remote add origin YOUR_GITHUB_URL
   git push -u origin main
   ```

2. **Create files for deployment**:

   **Create `requirements.txt`** (already done ✅)

   **Create `Procfile`**:
   ```
   web: gunicorn app:app
   ```

   **Update `requirements.txt`** to add:
   ```
   gunicorn==21.2.0
   ```

3. **Sign up at Render.com**:
   - Go to: https://render.com/
   - Sign up with GitHub

4. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Configure:
     - **Name**: movie-production-studio
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free

5. **Add Environment Variables**:
   - In Render dashboard, go to "Environment"
   - Add: `GOOGLE_API_KEY` = your-api-key

6. **Deploy**:
   - Click "Create Web Service"
   - Wait 5-10 minutes
   - You'll get a URL like: `https://movie-production-studio.onrender.com`

**Pros**: ✅ Free forever, ✅ Permanent URL, ✅ Auto-deploys from GitHub  
**Cons**: ⚠️ Sleeps after 15 min inactivity (takes 30s to wake up)

---

## ☁️ Option 3: Vercel (Easy - FREE)

**Best for**: Fast deployment, great performance  
**Cost**: FREE  
**Duration**: Permanent

### Steps:

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Create `vercel.json`**:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Deploy**:
   ```bash
   vercel
   ```
   - Login with GitHub/Email
   - Follow prompts
   - Add `GOOGLE_API_KEY` as environment variable when prompted

4. **Share URL**: You'll get `https://your-project.vercel.app`

**Pros**: ✅ Fast deployment, ✅ Great performance, ✅ Custom domains  
**Cons**: ⚠️ Serverless (10s execution limit on free tier)

---

## 🐍 Option 4: PythonAnywhere (Easy - FREE)

**Best for**: Python apps, always-on hosting  
**Cost**: FREE (limited)  
**Duration**: Permanent

### Steps:

1. **Sign up**: https://www.pythonanywhere.com/registration/register/beginner/

2. **Upload code**:
   - Go to "Files" tab
   - Upload your files OR clone from GitHub

3. **Install dependencies**:
   - Go to "Consoles" → "Bash"
   ```bash
   pip install --user Flask google-generativeai python-dotenv
   ```

4. **Configure Web App**:
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - Set source code path: `/home/yourusername/mysite`
   - Edit WSGI file to point to your `app.py`

5. **Set environment variables**:
   - In WSGI file, add:
   ```python
   import os
   os.environ['GOOGLE_API_KEY'] = 'your-key-here'
   ```

6. **Reload**: Click "Reload" button

**Pros**: ✅ Always-on (free tier), ✅ Simple Python hosting  
**Cons**: ⚠️ Limited CPU/bandwidth on free tier

---

## 🌊 Option 5: Heroku (Was FREE, now paid)

**Cost**: $5/month minimum  
**Not recommended** unless you need it for other reasons.

---

## 🏠 Option 6: Your Own Computer (Local Network)

**Best for**: Demo to friends on same WiFi  
**Cost**: FREE  
**Duration**: While your computer is on

### Steps:

1. **Find your local IP**:
   ```bash
   # Windows
   ipconfig
   # Look for "IPv4 Address" (e.g., 192.168.1.100)
   ```

2. **Update Flask to listen on all interfaces**:
   In `app.py`, change:
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```
   To:
   ```python
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000, debug=True)
   ```

3. **Allow through firewall**:
   ```bash
   # Windows Firewall
   # Allow port 5000 in Windows Defender Firewall
   ```

4. **Share the URL**:
   - Friends on same WiFi visit: `http://YOUR_IP:5000`
   - Example: `http://192.168.1.100:5000`

**Pros**: ✅ No signup needed, ✅ Fast  
**Cons**: ❌ Same network only, ❌ Computer must stay on

---

## 🎯 Recommended Option by Use Case

| Use Case | Best Option | Why |
|----------|-------------|-----|
| **Quick demo (right now)** | ngrok | Instant, works anywhere |
| **Permanent free hosting** | Render.com | Free forever, easy setup |
| **Portfolio/production** | Vercel | Fast, professional |
| **Learning/testing** | PythonAnywhere | Always-on, simple |
| **Friends on same WiFi** | Local Network | Fastest, no setup |

---

## 🔒 Security Considerations

### ⚠️ Important: Protect Your API Key!

When sharing publicly:

1. **Don't commit `.env` to GitHub**:
   ```bash
   # Make sure .gitignore includes:
   .env
   ```

2. **Use environment variables on hosting platforms**:
   - Set `GOOGLE_API_KEY` in platform settings (not in code)

3. **Consider API key rotation**:
   - Create separate API keys for development/production

4. **Add rate limiting** (optional):
   ```python
   from flask_limiter import Limiter
   
   limiter = Limiter(app, default_limits=["100 per hour"])
   ```

---

## 📱 Mobile Access

All options above work on mobile browsers!

**QR Code Generator** (for easy sharing):
```python
# Add to your app (optional):
pip install qrcode
```

---

## 🎨 Custom Domain (Optional)

Once deployed, you can add a custom domain:

1. **Buy domain** (Namecheap, Google Domains, etc.)
2. **Add to hosting platform**:
   - Render.com: Settings → Custom Domains
   - Vercel: Settings → Domains
   - PythonAnywhere: Requires paid tier

---

## 📊 Comparison Table

| Platform | Cost | Setup Time | Permanent | Always-On | Custom Domain |
|----------|------|------------|-----------|-----------|---------------|
| **ngrok** | FREE | 2 min | ❌ | While running | ❌ |
| **Render.com** | FREE | 10 min | ✅ | Sleeps after 15m | ✅ (free) |
| **Vercel** | FREE | 5 min | ✅ | ✅ | ✅ (free) |
| **PythonAnywhere** | FREE | 15 min | ✅ | ✅ | ✅ (paid) |
| **Local Network** | FREE | 2 min | ❌ | While PC on | ❌ |

---

## 🚀 My Recommendation

### For Quick Demo (TODAY):
```bash
# 1. Install ngrok
# 2. Run:
ngrok http 5000
# 3. Share the URL!
```

### For Permanent Sharing:
1. Push to GitHub
2. Deploy to **Render.com** (FREE forever)
3. Share the permanent URL

---

## 🆘 Need Help?

**ngrok Issues**:
- Docs: https://ngrok.com/docs
- Dashboard: https://dashboard.ngrok.com/

**Render Issues**:
- Docs: https://render.com/docs
- Community: https://community.render.com/

**General Hosting**:
- StackOverflow: Tag `flask` + platform name

---

## 📦 Files Needed for Deployment

### Required Files:
- ✅ `app.py` (your Flask app)
- ✅ `requirements.txt` (dependencies)
- ✅ `templates/index.html` (UI)
- ✅ `.env.example` (template, don't include actual `.env`)
- ✅ `README.md` (documentation)

### For Render/Heroku:
- ✅ `Procfile` (I'll create this)
- ✅ `runtime.txt` (optional, specify Python version)

### For Vercel:
- ✅ `vercel.json` (I'll create this)

---

Let me know which option you want to use and I'll help you set it up! 🚀
