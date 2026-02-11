# 🎥 How to Enable Video Generation

## Get FAL.AI API Key (FREE!)

FAL.AI offers a **free tier** for video generation. Here's how to get your API key:

### Step 1: Sign Up
1. Visit: https://fal.ai
2. Click "Sign Up" or "Get Started"
3. Sign up with Google/GitHub or email
4. ✅ Free account created!

### Step 2: Get API Key
1. Go to your dashboard: https://fal.ai/dashboard
2. Click on "API Keys" in the sidebar
3. Click "Create new key"
4. Copy your API key (starts with `fal_...`)

### Step 3: Add to Your App
1. Open your `.env` file in the project root
2. Add this line:
   ```
   FAL_KEY=fal_your_key_here
   ```
3. Save the file

### Step 4: Restart Server
```bash
# Stop current server (Ctrl+C)
# Then restart:
python app.py
```

### Step 5: Test Video Generation
1. Go to http://127.0.0.1:5000
2. Find "Text to Video" card
3. Enter prompt: "a cat walking in a garden, sunny day"
4. Select model: "Wan2.1 T2V" or "AnimateDiff"
5. Click "Create Video"
6. Wait 30-60 seconds
7. ✅ Your video appears!

## 💰 FAL.AI Free Tier

- **Cost**: FREE for first requests
- **Credits**: Get free credits monthly
- **Speed**: 30-60 seconds per video
- **Quality**: Professional
- **Models**: AnimateDiff, Stable Video, etc.

## 📊 Video Generation Pricing

| Provider | Free Tier | Cost per Video | Speed |
|----------|-----------|----------------|-------|
| **FAL.AI** | ✅ Yes | ~$0.02-0.05 | 30-60s |
| Replicate | ❌ No | ~$0.01-0.05 | 30-90s |
| Runway ML | ✅ Limited | Credits system | 60s+ |

## 🎬 Available Models

Once you add your FAL_KEY, you'll have access to:

### 1. AnimateDiff (Fast)
- **Best for**: Quick animations, cartoon style
- **Speed**: ~30 seconds
- **Quality**: Good

### 2. Stable Video Diffusion
- **Best for**: Cinematic, realistic videos
- **Speed**: ~60 seconds
- **Quality**: Excellent

### 3. Text-to-Video Models
- **Best for**: General purpose video generation
- **Speed**: ~45 seconds
- **Quality**: Very good

## 🔧 Troubleshooting

### "FAL_KEY not found" error
- Make sure you added FAL_KEY to .env file
- Restart the server after adding the key
- Check that the key starts with `fal_`

### "Insufficient credits" error
- You've used up free credits
- Add payment method or wait for monthly reset
- Alternative: Use Replicate or Runway ML

### Video generation is slow
- First generation may take longer (model loading)
- Subsequent generations are faster
- Expected time: 30-90 seconds

## 🆓 Alternative: Free Video Generation

If you don't want to use FAL.AI, here are alternatives:

### 1. Runway ML (Free Tier)
- Visit: https://runwayml.com
- Sign up for free account
- Use Gen-2 model (limited free generations)
- Generate manually, download, use in your project

### 2. Pika Labs (Discord Bot - Free)
- Join: https://pika.art
- Use Discord bot to generate videos
- Download and upload to your app

### 3. Leonardo.AI (Free Tier)
- Visit: https://leonardo.ai
- Free video generations daily
- Good quality

## ✅ Once You Have FAL_KEY

Your app will support:
- ✅ Text-to-Video generation
- ✅ Multiple video models
- ✅ Professional quality videos
- ✅ Fast generation (30-60s)
- ✅ Direct in-app generation

## 🎯 Quick Start

```bash
# 1. Get your FAL.AI API key from:
https://fal.ai/dashboard/keys

# 2. Add to .env:
echo "FAL_KEY=fal_your_key_here" >> .env

# 3. Restart server:
python app.py

# 4. Test video generation!
# Visit: http://127.0.0.1:5000
```

## 📞 Need Help?

- **FAL.AI Docs**: https://fal.ai/docs
- **FAL.AI Discord**: Join for support
- **Pricing**: https://fal.ai/pricing

---

**Note**: You can use the app without FAL_KEY - image generation and script generation still work perfectly!
