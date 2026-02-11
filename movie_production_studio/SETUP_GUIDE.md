# Quick Setup Guide 🚀

## Step-by-Step Instructions

### Step 1: Get Your Google Gemini API Key

1. Open your browser and go to: **https://makersuite.google.com/app/apikey**
2. Sign in with your Google account
3. Click the **"Create API Key"** button
4. Copy the API key (it will look like: `AIzaSy...`)

### Step 2: Install Required Packages

Open your terminal/PowerShell and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- google-generativeai (Gemini API)
- python-dotenv (environment variables)

### Step 3: Set Your API Key

**Option A: Using .env file (Recommended)**

1. Create a file named `.env` in the project root
2. Add this line to the file:
   ```
   GOOGLE_API_KEY=AIzaSy_your_actual_key_here
   ```
3. Save the file

**Option B: Using Environment Variable**

Run this in your terminal before starting the app:

**PowerShell:**
```powershell
$env:GOOGLE_API_KEY="AIzaSy_your_actual_key_here"
```

**Command Prompt:**
```cmd
set GOOGLE_API_KEY=AIzaSy_your_actual_key_here
```

### Step 4: Test Your Setup

Run the test script:

```bash
python tmp_rovodev_test_gemini.py
```

You should see:
- ✅ API Key present: True
- ✅ Gemini API configured
- ✅ JSON parsed successfully
- ✅ ALL TESTS PASSED!

### Step 5: Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### Step 6: Open in Browser

1. Open your browser
2. Go to: **http://127.0.0.1:5000**
3. Enter a movie idea and click "Generate"

## Example Movie Ideas to Try

- "A time-traveling detective solves historical mysteries"
- "An AI becomes self-aware and wants to become human"
- "A chef discovers magical ingredients that bring memories to life"
- "Astronauts find an ancient civilization on Mars"
- "A musician can hear people's emotions as music"

## Troubleshooting

### Problem: "Module not found: google.generativeai"
**Solution:** Run `pip install -r requirements.txt`

### Problem: "API Key not set"
**Solution:** Make sure your `.env` file exists and contains the correct API key

### Problem: "Connection error"
**Solution:** Check your internet connection and verify your API key is valid

### Problem: Port already in use
**Solution:** Change the port in `app.py`:
```python
app.run(debug=True, port=5001)  # Change to 5001 or any available port
```

## What You'll Get

After entering a movie idea, the AI will generate:

1. **📜 Screenplay**: A detailed 3-5 paragraph outline
2. **👥 Characters**: 3-5 main characters with descriptions
3. **📊 Complexity Score**: Production difficulty rating (1-10)
4. **🎥 Video Prompt**: AI-ready prompt for video generation

## Next Steps

Once everything is working:
- Try different movie ideas
- Click "Generate Video Demo" (currently shows a sample video)
- Experiment with the interface
- Check out the code to customize it!

---

**Need Help?**
- Check `README.md` for detailed documentation
- Review the code in `app.py` and `templates/index.html`
- Verify your API key at: https://makersuite.google.com/app/apikey
