# 🆓 Free APIs Required for Movie Production Studio

## Current APIs Used

### 1. ✅ **Google Gemini API** (AI Text Generation)
- **Purpose**: Generate screenplays, characters, complexity scores, and video prompts
- **Current Model**: `gemini-2.5-flash`
- **Free Tier**: 
  - ✅ 15 requests per minute
  - ✅ 1,500 requests per day
  - ✅ 1 million tokens per minute
- **Get API Key**: https://makersuite.google.com/app/apikey
- **Cost**: **100% FREE** (No credit card required)
- **Documentation**: https://ai.google.dev/docs

**Alternative Free AI APIs:**
- **OpenAI GPT-3.5-turbo**: $0.002/1K tokens (requires credit card)
- **Anthropic Claude**: Limited free tier with credit card
- **Hugging Face Inference API**: Free tier available
- **Groq**: Fast inference, generous free tier
- **Together.ai**: Free credits on signup

---

## 🎥 Recommended APIs for Video Generation (Future Enhancement)

### 2. **Runway ML API** (AI Video Generation)
- **Purpose**: Generate video demos from text prompts
- **Free Tier**: 
  - ⚠️ Limited free credits on signup (~125 credits)
  - Each video generation costs 5-10 credits
- **Pricing**: Paid plans start at $12/month
- **Get API Key**: https://runwayml.com/
- **Best For**: High-quality AI video generation

### 3. **Pika Labs** (AI Video Generation)
- **Purpose**: Text-to-video and image-to-video
- **Free Tier**: 
  - ⚠️ Limited free generations per month
- **Pricing**: Paid plans available
- **Website**: https://pika.art/
- **Status**: Currently in beta, API access limited

### 4. **Stability AI Video** (AI Video Generation)
- **Purpose**: Stable Video Diffusion
- **Free Tier**: 
  - ⚠️ Limited free credits
- **Pricing**: Pay-per-use model
- **Get API Key**: https://platform.stability.ai/
- **Best For**: Image-to-video conversion

### 5. ✅ **Replicate API** (AI Models Marketplace)
- **Purpose**: Access multiple AI models including video generation
- **Free Tier**: 
  - ✅ $0.01 free credit on signup
  - Pay-per-use after that (very affordable)
- **Models Available**:
  - Stable Video Diffusion
  - AnimateDiff
  - Text-to-video models
- **Get API Key**: https://replicate.com/
- **Pricing**: ~$0.001-0.01 per generation
- **Documentation**: https://replicate.com/docs

### 6. ✅ **Hugging Face Inference API** (AI Models) - IMPLEMENTED! ✨
- **Purpose**: Text-to-video generation (AI-powered videos)
- **Free Tier**: 
  - ✅ Completely free for public models
  - ✅ ~50-100 video generations per day
  - ✅ No credit card required
- **Models Available**:
  - ✨ **Text-to-Video** (damo-vilab, zeroscope) - **ACTIVE IN YOUR APP**
  - Text-to-image (Stable Diffusion)
  - Image-to-video models
  - Text generation
- **Current Implementation**:
  - ✅ 3 video models with automatic fallbacks
  - ✅ 16-frame videos (~2-3 seconds)
  - ✅ Artistic/stylized output (not photorealistic)
  - ✅ 30-120 second generation time
- **Get API Key**: https://huggingface.co/settings/tokens
- **Cost**: **FREE** (Rate limited but generous)
- **Documentation**: https://huggingface.co/docs/api-inference
- **Setup Guide**: See `VIDEO_GENERATION_GUIDE.md`

---

## 🖼️ Image Generation APIs (For Storyboarding)

### 7. ✅ **DALL-E 3 (OpenAI)** 
- **Purpose**: Generate concept art and storyboards
- **Free Tier**: ❌ Requires payment ($0.04/image for 1024x1024)
- **Get API Key**: https://platform.openai.com/

### 8. ✅ **Stable Diffusion (Stability AI)**
- **Purpose**: Generate images from text
- **Free Tier**: 
  - ✅ Free tier available (25 credits on signup)
- **Get API Key**: https://platform.stability.ai/
- **Pricing**: $0.002-0.008 per image

### 9. ✅ **Replicate - Stable Diffusion**
- **Purpose**: Image generation
- **Free Tier**: ✅ Small free credit
- **Get API Key**: https://replicate.com/
- **Models**: SDXL, Stable Diffusion 1.5, 2.1, etc.

---

## 🎵 Audio/Music Generation APIs (For Soundtracks)

### 10. ✅ **Suno AI** (Music Generation)
- **Purpose**: Generate soundtrack music
- **Free Tier**: ✅ Limited free generations per day
- **Website**: https://suno.ai/
- **Status**: Web interface, API coming soon

### 11. ✅ **MusicGen (via Hugging Face)**
- **Purpose**: AI music generation
- **Free Tier**: ✅ Completely free via Hugging Face
- **Access**: https://huggingface.co/spaces/facebook/MusicGen
- **Cost**: **FREE**

### 12. **ElevenLabs** (Voice Generation)
- **Purpose**: Generate character voices/narration
- **Free Tier**: 
  - ✅ 10,000 characters per month
  - ✅ 3 custom voices
- **Get API Key**: https://elevenlabs.io/
- **Pricing**: Free tier → $5/month for more

---

## 📊 Additional Useful APIs

### 13. ✅ **The Movie Database (TMDb) API**
- **Purpose**: Get movie data, posters, cast info for reference
- **Free Tier**: ✅ Completely free
- **Get API Key**: https://www.themoviedb.org/settings/api
- **Rate Limit**: 40 requests per 10 seconds
- **Cost**: **FREE**

### 14. ✅ **OMDb API** (Open Movie Database)
- **Purpose**: Movie information and metadata
- **Free Tier**: ✅ 1,000 requests per day
- **Get API Key**: http://www.omdbapi.com/apikey.aspx
- **Cost**: **FREE**

### 15. ✅ **Firebase** (Database & Storage)
- **Purpose**: Store generated content, user data
- **Free Tier**: 
  - ✅ 1 GB storage
  - ✅ 10 GB monthly transfer
  - ✅ 50K reads/day, 20K writes/day
- **Setup**: https://firebase.google.com/
- **Cost**: **FREE** (generous limits)

---

## 🚀 Quick Setup Instructions

### Currently Required (Working Now):
```bash
# 1. Google Gemini API
GOOGLE_API_KEY=your-key-here
```

### For Video Generation Enhancement:
```bash
# 2. Choose ONE video API:
REPLICATE_API_TOKEN=your-replicate-token
# OR
HUGGINGFACE_API_TOKEN=your-hf-token
# OR
STABILITY_API_KEY=your-stability-key
```

### Optional Enhancements:
```bash
# 3. For music/audio:
ELEVENLABS_API_KEY=your-elevenlabs-key

# 4. For movie data:
TMDB_API_KEY=your-tmdb-key

# 5. For database (Firebase):
FIREBASE_CONFIG=your-firebase-config-json
```

---

## 💰 Cost Comparison (Monthly)

| Feature | Free Option | Paid Option |
|---------|-------------|-------------|
| **AI Text Generation** | Gemini (FREE) | OpenAI GPT-4 ($20/mo) |
| **Video Generation** | Hugging Face (FREE, limited) | Runway ($12/mo) |
| **Image Generation** | Replicate ($0.01 free) | DALL-E 3 ($0.04/image) |
| **Voice Generation** | ElevenLabs (10K chars/mo) | ElevenLabs ($5/mo) |
| **Database** | Firebase (FREE tier) | Firebase ($25/mo) |
| **Music Generation** | MusicGen (FREE) | Suno Pro ($10/mo) |

**Total Free Setup Cost**: $0/month ✅  
**Total Enhanced Setup Cost**: ~$12-50/month

---

## 🎯 Recommended Free Stack

### **Tier 1: Completely Free (Current)**
```
✅ Google Gemini API - Text generation (FREE forever)
✅ Hugging Face - Image/video models (FREE, rate limited)
✅ Firebase - Database & storage (FREE tier)
✅ TMDb - Movie data (FREE)
```

### **Tier 2: Minimal Cost (~$1-5/month)**
```
✅ Replicate - Video generation ($0.01 startup credit)
✅ Stability AI - Image generation (25 free credits)
✅ ElevenLabs - Voice (10K chars free)
```

### **Tier 3: Professional (~$50/month)**
```
🔥 Runway ML - High-quality video ($12/mo)
🔥 OpenAI GPT-4 - Better text ($20/mo)
🔥 ElevenLabs Pro - Unlimited voice ($5/mo)
🔥 Suno Pro - Music generation ($10/mo)
```

---

## 🔧 Integration Priority

**Phase 1 (Current - FREE):**
- ✅ Gemini API for text generation

**Phase 2 (Next - FREE):**
- 🎯 Hugging Face for basic video/image generation
- 🎯 Firebase for saving projects
- 🎯 TMDb for movie reference data

**Phase 3 (Future - Paid):**
- 🎯 Replicate/Runway for professional video
- 🎯 ElevenLabs for character voices
- 🎯 Suno for soundtrack generation

---

## 📝 Notes

- **Most APIs require email verification only** (no credit card)
- **Free tiers are usually enough for development/testing**
- **Rate limits can be worked around with caching**
- **Start free, upgrade only when needed**

## 🆘 Support Links

- Gemini API Help: https://ai.google.dev/docs
- Hugging Face Community: https://discuss.huggingface.co/
- Replicate Discord: https://discord.gg/replicate
- Stack Overflow: Tag `google-gemini` or `huggingface`
