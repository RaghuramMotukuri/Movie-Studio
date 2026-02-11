# 🎬 Movie Production Studio - Quick Reference

## 🚀 Server Info
**URL**: http://127.0.0.1:5000
**Status**: ✅ Running
**API Keys**: ✅ Configured

## 🎨 Available Models

### 📸 Image Generation (4 models)
1. **FLUX.1 Schnell** ⭐ RECOMMENDED - Fastest & best quality
2. SDXL Base - Detailed images
3. SDXL Turbo - Quick iterations  
4. Playground V2.5 - Aesthetic style

### 🎥 Video Generation (4 models)
1. **AnimateDiff** ⭐ RECOMMENDED - Best motion quality
2. Zeroscope V2 - Good balance
3. ModelScope - Fast generation
4. Stable Video Diffusion - Cinematic

### 🎵 Music Generation (3 models)
1. **MusicGen Large** ⭐ RECOMMENDED - Professional quality
2. MusicGen Small - Fast generation
3. AudioLDM2 - Sound effects

### 🎙️ Voice Generation
1. **Bark** - Natural text-to-speech

### ✍️ Script Generation
1. **Google Gemini 2.5 Flash** - AI screenplay writer

## ⚡ Quick Start

### Generate Script
```
Input: "A detective story in 1940s noir style"
Output: Complete screenplay, characters, production notes
```

### Create Image
```
Model: FLUX.1 Schnell
Prompt: "Film noir detective in fedora, 1940s, dramatic shadows"
Time: ~5 seconds
```

### Generate Video
```
Model: AnimateDiff
Prompt: "Detective walking down rainy street, noir style, cinematic"
Time: ~30 seconds
```

### Create Music
```
Model: MusicGen Large
Prompt: "Jazz noir saxophone theme, moody, 1940s detective film"
Time: ~20 seconds
```

### Generate Voice
```
Model: Bark
Text: "The city never sleeps, and neither do I"
Time: ~8 seconds
```

## 🎯 Best Practices

### ✅ DO:
- Use FLUX.1 for all image generation (fastest + best)
- Use AnimateDiff for high-quality videos
- Be specific in prompts (lighting, style, mood)
- Start with fast models, refine with slow ones
- Download results immediately (not stored)

### ❌ DON'T:
- Use vague prompts ("make a video")
- Expect instant results (some models take time)
- Generate very long videos (30s max)
- Forget to specify style and mood

## 📝 Prompt Templates

### Image Prompts
```
[Subject], [Action], [Setting], [Lighting], [Style], [Quality]

Example:
"Cyberpunk detective, examining hologram, neon-lit office, 
dramatic blue lighting, blade runner style, 8k photorealistic"
```

### Video Prompts
```
[Scene], [Motion], [Camera], [Style], [Mood]

Example:
"Flying car gliding through futuristic city, smooth tracking shot,
cyberpunk aesthetic, atmospheric and moody"
```

### Music Prompts
```
[Genre], [Instruments], [Mood], [Reference], [Length]

Example:
"Epic orchestral, powerful brass and strings, heroic and uplifting,
Hans Zimmer style, cinematic film score"
```

### Voice Prompts
```
Just write natural dialogue - the AI handles tone and emotion

Example:
"The case was closed, but the mystery lingered in my mind."
```

## 🔧 Troubleshooting

### Model is Loading (503 error)
- **Wait**: 20-30 seconds for model to load
- **Retry**: Click generate again
- **Normal**: First request often triggers loading

### API Error
- **Check**: Your HuggingFace token is valid
- **Verify**: Internet connection is stable
- **Try**: Different model if one fails

### Slow Generation
- **Use**: Faster models (SDXL Turbo, MusicGen Small)
- **Add**: HuggingFace API token for priority
- **Wait**: Complex prompts take longer

### No Results
- **Simplify**: Your prompt might be too complex
- **Check**: Browser console for errors
- **Refresh**: Page and try again

## 🎬 Production Workflow

### Step 1: Script (5 min)
1. Enter movie idea
2. Generate with Gemini
3. Review and refine

### Step 2: Concept Art (15 min)
1. Use FLUX.1 Schnell
2. Generate key characters
3. Create environment concepts
4. Design props and items

### Step 3: Storyboard (30 min)
1. Add frames to storyboard
2. Generate scene images
3. Add descriptions
4. Organize shot sequence

### Step 4: Video Clips (1 hour)
1. Select key scenes
2. Generate with AnimateDiff
3. Review and refine
4. Download clips

### Step 5: Audio (30 min)
1. Generate background music
2. Create sound effects
3. Generate voice dialogue
4. Download all audio

### Step 6: Export (5 min)
1. Export storyboard as PDF
2. Download all assets
3. Organize in production folder

## 💡 Pro Tips

1. **Batch Generate**: Create multiple variations quickly
2. **Mix Models**: Use different models for different needs
3. **Save Prompts**: Keep successful prompts for reference
4. **Iterate Fast**: Generate quickly, refine later
5. **Use Shot List**: Plan before generating
6. **Copy Prompts**: Use script's video prompt for consistency

## 🎨 Keyboard Shortcuts

- **Enter**: Submit in any input field
- **Ctrl+C**: Copy generated prompt
- **Ctrl+V**: Paste into new field
- **Ctrl+S**: Download result (when available)

## 📊 System Requirements

- **Browser**: Chrome, Firefox, Edge (latest)
- **Connection**: Stable internet (for API calls)
- **Storage**: None (results not stored server-side)
- **Memory**: 2GB+ RAM recommended

## 🔐 API Keys Used

```env
GOOGLE_API_KEY=AIzaSy... (Gemini)
HUGGINGFACE_API_KEY=hf_WpBS... (All HF models)
```

Both keys are configured and working! ✅

## 📱 Features

✅ Modern dark mode interface
✅ Bento grid layout
✅ Smooth animations
✅ Toast notifications
✅ Loading indicators
✅ Error handling
✅ PDF export
✅ Responsive design
✅ Keyboard support
✅ Copy to clipboard

## 🌟 What Makes This Special

- **100% Free** - All APIs are free to use
- **No Sign-up** - Start creating immediately
- **Unlimited** - No generation limits
- **Modern UI** - Beautiful dark mode interface
- **Fast** - Optimized with your API tokens
- **Complete** - Full production pipeline
- **Professional** - Industry-standard tools

## 📞 Need Help?

- Check error messages (they're helpful!)
- Read model documentation
- Try different prompts
- Use recommended models
- Be patient with loading times

---

**Enjoy creating! 🎬✨**
