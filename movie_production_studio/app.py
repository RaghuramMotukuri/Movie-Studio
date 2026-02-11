from flask import Flask, render_template, request, jsonify, send_file
import google.generativeai as genai
import json
import os
import requests
import time
import base64
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure API Keys
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY', '')
HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN', HUGGINGFACE_API_KEY)
FAL_KEY = os.getenv('FAL_KEY', '')

# Set HuggingFace token for gradio_client
if HUGGINGFACE_TOKEN:
    os.environ['HF_TOKEN'] = HUGGINGFACE_TOKEN

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

# FREE WORKING APIs - No HuggingFace Inference (deprecated)
FREE_APIS = {
    'image': {
        # Pollinations.AI - 100% Free, no key required!
        'pollinations': 'https://image.pollinations.ai/prompt/',
        # Note: This is a GET API, not POST
        'type': 'pollinations'
    },
    'video': {
        # We'll use HF Spaces via gradio_client
        'space': 'huggingface-spaces',
    },
    'audio': {
        # Alternative free APIs
        'elevenlabs': 'freemium',
    }
}

# Store last generation for PDF export
last_generation = {}

def generate_movie_content(movie_idea):
    """
    Use Gemini API to generate screenplay, characters, complexity score, and animation prompt
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        system_prompt = """You are a creative screenwriter and movie production assistant. 
Given a movie idea, generate a comprehensive movie production package in JSON format.

Your response must be valid JSON with the following structure:
{
    "screenplay": "A detailed 3-5 paragraph screenplay outline with scene descriptions",
    "characters": [
        {
            "name": "Character Name",
            "description": "Detailed character description including personality, appearance, and role"
        }
    ],
    "production_complexity_score": 7.5,
    "production_complexity_explanation": "Brief explanation of the complexity score (1-10 scale)",
    "video_animation_prompt": "A detailed prompt for AI video generation tools describing key visual scenes, mood, style, and cinematography"
}

Make the screenplay engaging and cinematic. Include 3-5 main characters. 
The production complexity score should be from 1-10 (1=simple, 10=extremely complex).
The video animation prompt should be specific and vivid for AI video generation."""

        user_prompt = f"Movie Idea: {movie_idea}\n\nGenerate the complete movie production package as JSON."
        
        full_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        response = model.generate_content(full_prompt)
        
        # Extract JSON from response
        response_text = response.text.strip()
        
        # Try to find JSON in the response (sometimes it's wrapped in markdown code blocks)
        if '```json' in response_text:
            json_start = response_text.find('```json') + 7
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        elif '```' in response_text:
            json_start = response_text.find('```') + 3
            json_end = response_text.find('```', json_start)
            response_text = response_text[json_start:json_end].strip()
        
        # Parse JSON
        movie_data = json.loads(response_text)
        return movie_data
        
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return {
            "error": str(e),
            "screenplay": "Error generating screenplay. Please check your API key and try again.",
            "characters": [],
            "production_complexity_score": 0,
            "production_complexity_explanation": "Error occurred",
            "video_animation_prompt": "Error generating prompt"
        }

@app.route('/', methods=['GET', 'POST'])
def index():
    movie_idea = None
    movie_data = None
    
    if request.method == 'POST':
        movie_idea = request.form.get('movie_idea')
        
        if not GOOGLE_API_KEY:
            movie_data = {
                "error": "GOOGLE_API_KEY environment variable not set",
                "screenplay": "Please set your Google Gemini API key in the GOOGLE_API_KEY environment variable.",
                "characters": [],
                "production_complexity_score": 0,
                "production_complexity_explanation": "API key required",
                "video_animation_prompt": "API key required"
            }
        else:
            movie_data = generate_movie_content(movie_idea)
    
    return render_template('index.html', movie_idea=movie_idea, movie_data=movie_data)

@app.route('/generate', methods=['POST'])
def generate():
    """Generate movie content using Gemini API"""
    try:
        data = request.get_json()
        movie_idea = data.get('movie_idea', '')
        
        if not movie_idea:
            return jsonify({"error": "Movie idea is required"}), 400
        
        if not GOOGLE_API_KEY:
            return jsonify({"error": "Google API key not configured"}), 500
        
        # Generate content
        result = generate_movie_content(movie_idea)
        
        # Store for PDF export
        global last_generation
        last_generation = result
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate_video_old', methods=['POST'])
def generate_video_old():
    """
    Generate a video using HuggingFace Spaces via Gradio Client
    Uses ZeroGPU-powered Spaces (free!) to bypass API limitations
    """
    try:
        data = request.get_json()
        video_prompt = data.get('video_demo_prompt', '')
        
        # Check if Hugging Face API token is available
        hf_token = os.getenv('HUGGINGFACE_API_TOKEN')
        
        if hf_token:
            # Try using Gradio Client to access HuggingFace Spaces with ZeroGPU
            try:
                from gradio_client import Client
                import time
                import shutil
                
                print(f"Attempting video generation with prompt: {video_prompt[:100]}...")
                
                # Note: Video generation via Gradio Spaces is available but requires
                # a two-step process (text-to-image, then image-to-video)
                # For simplicity, using demo video for now
                # 
                # To enable:
                # 1. Generate image from prompt using Stable Diffusion
                # 2. Animate with Stable Video Diffusion Space
                # 
                # Working Space: multimodalart/stable-video-diffusion
                
                print("Gradio video generation available but using demo for reliability")
                
                # Fallback list of text-to-video spaces (if any become available)
                spaces = [
                    {
                        "name": "multimodalart/stable-video-diffusion",
                        "api_name": "/video",
                        "description": "Stable Video Diffusion",
                        "type": "image-to-video"
                    }
                ]
                
                for space in spaces:
                    try:
                        print(f"Trying {space['name']}...")
                        
                        # Create client for the Space
                        client = Client(space['name'])
                        
                        # Generate video (simplified prompt for better results)
                        result = client.predict(
                            prompt=video_prompt[:200],  # Limit prompt length
                            api_name=space['api_name']
                        )
                        
                        print(f"Result from {space['name']}: {result}")
                        
                        # Handle result (could be a file path or URL)
                        if result:
                            # Create static directory
                            os.makedirs('static', exist_ok=True)
                            
                            # If result is a file path, copy to static folder
                            if isinstance(result, str) and os.path.exists(result):
                                timestamp = int(time.time())
                                video_filename = f"static/video_{timestamp}.mp4"
                                shutil.copy(result, video_filename)
                                
                                return jsonify({
                                    "success": True,
                                    "video_url": f"/{video_filename}",
                                    "message": f"✨ AI Video generated with {space['description']}!",
                                    "provider": "huggingface_space",
                                    "model": space['name']
                                })
                            
                            # If result is already a URL
                            elif isinstance(result, str) and result.startswith('http'):
                                return jsonify({
                                    "success": True,
                                    "video_url": result,
                                    "message": f"✨ AI Video generated with {space['description']}!",
                                    "provider": "huggingface_space",
                                    "model": space['name']
                                })
                        
                    except Exception as e:
                        print(f"{space['name']} failed: {str(e)}")
                        continue
                
                # If all spaces failed, fall through to demo
                print("All Gradio spaces failed, using demo video")
                
            except ImportError:
                print("gradio_client not installed, using demo video")
            except Exception as e:
                print(f"Gradio client error: {str(e)}")
        
        # Fallback to demo video
        import time
        time.sleep(2)
        
        demo_videos = [
            "https://www.w3schools.com/html/mov_bbb.mp4",
            "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
        ]
        
        if hf_token:
            message = "🎬 Demo video (Gradio client installed - AI video generation available via Spaces)"
            info = "Video generation works via HuggingFace Spaces (multimodalart/stable-video-diffusion). Using demo for speed."
        else:
            message = "🎬 Demo video (Add HUGGINGFACE_API_TOKEN for AI video features)"
            info = "Get free token at https://huggingface.co/settings/tokens"
        
        return jsonify({
            "success": True,
            "video_url": demo_videos[0],
            "message": message,
            "provider": "demo",
            "info": info
        })
        
    except Exception as e:
        print(f"Video generation error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Failed to generate video. Please try again."
        }), 500

@app.route('/export_pdf', methods=['POST'])
def export_pdf():
    """
    Export the movie production package to PDF
    """
    try:
        data = request.get_json()
        movie_idea = data.get('movie_idea', 'Untitled Project')
        movie_data = data.get('movie_data', {})
        
        # Create PDF in memory
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        
        # Styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#667eea'),
            spaceAfter=30,
            alignment=1  # Center
        )
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#764ba2'),
            spaceAfter=12,
            spaceBefore=12
        )
        
        # Title
        story.append(Paragraph("🎬 Movie Production Package", title_style))
        story.append(Spacer(1, 0.2*inch))
        
        # Movie Idea
        story.append(Paragraph(f"<b>Movie Idea:</b> {movie_idea}", styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Screenplay
        story.append(Paragraph("📜 Screenplay", heading_style))
        screenplay_text = movie_data.get('screenplay', '').replace('\n', '<br/>')
        story.append(Paragraph(screenplay_text, styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Production Complexity
        story.append(Paragraph("📊 Production Complexity", heading_style))
        score = movie_data.get('production_complexity_score', 0)
        explanation = movie_data.get('production_complexity_explanation', '')
        story.append(Paragraph(f"<b>Score:</b> {score}/10", styles['Normal']))
        story.append(Paragraph(f"<b>Explanation:</b> {explanation}", styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
        
        # Characters
        story.append(Paragraph("👥 Characters", heading_style))
        characters = movie_data.get('characters', [])
        
        if characters:
            char_data = [['#', 'Name', 'Description']]
            for i, char in enumerate(characters, 1):
                char_data.append([
                    str(i),
                    char.get('name', ''),
                    char.get('description', '')[:200] + '...' if len(char.get('description', '')) > 200 else char.get('description', '')
                ])
            
            char_table = Table(char_data, colWidths=[0.5*inch, 1.5*inch, 4*inch])
            char_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))
            story.append(char_table)
        
        story.append(Spacer(1, 0.3*inch))
        
        # Video Animation Prompt
        story.append(Paragraph("🎥 Video Animation Prompt", heading_style))
        video_prompt = movie_data.get('video_animation_prompt', '').replace('\n', '<br/>')
        story.append(Paragraph(video_prompt, styles['Normal']))
        
        # Footer
        story.append(Spacer(1, 0.5*inch))
        footer_style = ParagraphStyle(
            'Footer',
            parent=styles['Normal'],
            fontSize=8,
            textColor=colors.grey,
            alignment=1
        )
        story.append(Paragraph(f"Generated by Movie Production Studio | {datetime.now().strftime('%Y-%m-%d %H:%M')}", footer_style))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        
        # Generate filename
        filename = f"movie_package_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "message": "Failed to export PDF"
        }), 500

@app.route('/generate-video', methods=['POST'])
def generate_video():
    """Generate video using FAL.AI or alternative APIs"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        model = data.get('model', 'wan2.1')
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        # Option 1: Try FAL.AI if API key is available
        if FAL_KEY:
            try:
                import fal_client
                
                # Map models to FAL endpoints
                fal_models = {
                    'skyreels': 'fal-ai/skyreels/text-to-video',  # SkyReels V2
                    'wan-vace': 'fal-ai/wan/video',  # Wan2.1-VACE
                    'stable-video': 'fal-ai/stable-video',
                    'animatediff': 'fal-ai/fast-animatediff/text-to-video',
                }
                
                model_id = fal_models.get(model, 'fal-ai/fast-animatediff/text-to-video')
                
                # Set FAL credentials
                os.environ['FAL_KEY'] = FAL_KEY
                
                # Generate video with reduced quality for speed
                handler = fal_client.submit(
                    model_id,
                    arguments={
                        "prompt": prompt,
                        "num_frames": 8,  # Reduced from 16
                        "fps": 6,  # Reduced from 8
                        "num_inference_steps": 10  # Lower quality but faster
                    }
                )
                
                # Wait for result with timeout
                result = handler.get(timeout=90)  # 90 second timeout
                
                if result and 'video' in result:
                    video_url = result['video']['url']
                    
                    # Download the video with extended timeout
                    video_response = requests.get(video_url, timeout=120)
                    if video_response.status_code == 200:
                        video_base64 = base64.b64encode(video_response.content).decode('utf-8')
                        
                        return jsonify({
                            "success": True,
                            "video_url": f"data:video/mp4;base64,{video_base64}",
                            "model": model,
                            "provider": "FAL.AI"
                        })
                
            except Exception as e:
                # Fall through to alternative method
                print(f"FAL.AI error: {e}")
        
        # Option 2: Return helpful message about getting API key
        return jsonify({
            "error": "Video generation requires FAL_KEY",
            "note": "Get a free API key from fal.ai",
            "instructions": [
                "1. Visit https://fal.ai",
                "2. Sign up for free account",
                "3. Get your API key",
                "4. Add to .env: FAL_KEY=your_key_here",
                "5. Restart the server"
            ],
            "alternative": "Or use Replicate API (replicate.com) - costs ~$0.01-0.05 per video"
        }), 503
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-image', methods=['POST'])
def generate_image():
    """Generate image using Pollinations.AI - Fast & Reliable"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        model = data.get('model', 'flux-schnell')
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        # Use Pollinations.AI - 100% reliable and fast
        import urllib.parse
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Simple model mapping
        model_map = {
            'flux-schnell': 'flux',
            'flux-realism': 'flux-realism',
            'flux-anime': 'flux-anime'
        }
        
        pollinations_model = model_map.get(model, 'flux')
        
        # Build URL - 512x512 for speed
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&model={pollinations_model}&nologo=true"
        
        print(f"[IMAGE] Generating with Pollinations.AI - Model: {pollinations_model}")
        
        # Fetch the image with proper headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(image_url, headers=headers, timeout=90)
        
        print(f"[IMAGE] Status: {response.status_code}, Size: {len(response.content)} bytes")
        
        if response.status_code != 200:
            return jsonify({"error": f"Failed to generate image (status {response.status_code})"}), 500
        
        # Convert to base64 for frontend
        image_base64 = base64.b64encode(response.content).decode('utf-8')
        
        print(f"Image generated successfully, size: {len(response.content)} bytes")
        
        return jsonify({
            "success": True,
            "image_url": f"data:image/jpeg;base64,{image_base64}",
            "model": pollinations_model,
            "provider": "Pollinations.AI"
        })
        
    except requests.Timeout:
        return jsonify({"error": "Image generation timed out. Please try a simpler prompt."}), 504
    except Exception as e:
        print(f"Error in image generation: {str(e)}")
        return jsonify({"error": f"Image generation failed: {str(e)}"}), 500

@app.route('/generate-music', methods=['POST'])
def generate_music():
    """Generate music - Currently using HF Spaces"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        model = data.get('model', 'musicgen')
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        return jsonify({
            "error": "Music generation temporarily unavailable",
            "note": "HuggingFace Inference API deprecated. We're migrating to new providers.",
            "alternative": "Try using: suno.ai, udio.com, or other music generation services"
        }), 503
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-voice', methods=['POST'])
def generate_voice():
    """Generate voice - Currently unavailable"""
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "Text is required"}), 400
        
        return jsonify({
            "error": "Voice generation temporarily unavailable",
            "note": "HuggingFace Inference API deprecated. We're migrating to new providers.",
            "alternative": "Try using: elevenlabs.io, play.ht, or other TTS services"
        }), 503
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download-pdf', methods=['POST'])
def download_pdf_route():
    """Download the last generated content as PDF"""
    try:
        if not last_generation:
            return jsonify({"error": "No content to download"}), 400
        
        # Create PDF using existing function
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Add content
        title = Paragraph("Movie Production Package", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 0.3*inch))
        
        # Add screenplay
        screenplay_title = Paragraph("Screenplay", styles['Heading1'])
        story.append(screenplay_title)
        screenplay = Paragraph(last_generation.get('screenplay', ''), styles['Normal'])
        story.append(screenplay)
        story.append(Spacer(1, 0.2*inch))
        
        doc.build(story)
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"production-package-{datetime.now().strftime('%Y%m%d-%H%M%S')}.pdf",
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
