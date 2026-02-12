Movie Production Studio 🎬
A Flask web application that uses Google Gemini AI to generate complete movie production packages including screenplays, character descriptions, production complexity scores, and video animation prompts.

Features
🎭 AI-Powered Screenplay Generation - Get detailed screenplay outlines from simple movie ideas
👥 Character Development - Automatically generate character profiles with descriptions
📊 Production Complexity Analysis - Receive complexity scores (1-10) for production planning
🎥 Video Animation Prompts - Get AI-ready prompts for video generation tools
📱 Responsive Dashboard - Beautiful Tailwind CSS interface that works on all devices
⚡ Video Demo Generation - Generate video demos with loading states (placeholder feature)
Setup Instructions
1. Install Dependencies
pip install -r requirements.txt
2. Get Your Google Gemini API Key
Go to Google AI Studio
Sign in with your Google account
Click "Create API Key"
Copy your API key
3. Configure Environment Variables
Create a .env file in the root directory:

# Copy the example file
cp .env.example .env
Edit the .env file and add your API key:

GOOGLE_API_KEY=your-actual-api-key-here
Alternative: Set the environment variable directly in your terminal:

PowerShell:

$env:GOOGLE_API_KEY="your-api-key-here"
Command Prompt:

set GOOGLE_API_KEY=your-api-key-here
Linux/Mac:

export GOOGLE_API_KEY="your-api-key-here"
4. Run the Application
python app.py
The application will start at: http://127.0.0.1:5000

Testing the Gemini API Connection
Run the test script to verify your API key and connection:

python tmp_rovodev_test_gemini.py
This will:

✅ Check if the API key is set
✅ Test the Gemini API connection
✅ Verify JSON parsing
✅ Display sample output
Usage
Enter a Movie Idea: Type your movie concept in the input box
Click Generate: The AI will create a complete production package
View Results:
Left Panel: Screenplay outline and video animation prompt
Right Panel: Production Bible with characters and complexity score
Generate Video Demo: Click the button to generate a video (currently returns dummy video)
Project Structure
.
├── app.py                      # Flask application and routes
├── templates/
│   └── index.html             # Main dashboard UI (Tailwind CSS)
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── .env                      # Your API keys (not in git)
└── README.md                 # This file
API Endpoints
GET/POST /
Main application route that displays the dashboard and processes movie ideas.

POST /generate_video
Generates a video demo from the video animation prompt.

Request:

{
  "video_demo_prompt": "Your video prompt here"
}
Response:

{
  "success": true,
  "video_url": "https://example.com/video.mp4",
  "message": "Video generated successfully!"
}
Technologies Used
Backend: Flask (Python)
AI: Google Gemini API
Frontend: HTML, Tailwind CSS, JavaScript
Environment Management: python-dotenv
Future Enhancements
🎬 Integrate real video generation API (Runway, Pika, Stability AI)
💾 Save generated content to database
📥 Export to PDF/JSON
🎨 Custom styling options
🔄 Project management features
👤 User authentication
Troubleshooting
"GOOGLE_API_KEY environment variable not set"
Make sure you've created a .env file with your API key or set the environment variable in your terminal.

"Error generating content"
Check your API key is valid
Ensure you have internet connection
Verify the API key has proper permissions
JSON Parsing Errors
The application handles JSON extraction from markdown code blocks automatically. If issues persist, check the Gemini API response format.

License
MIT License - Feel free to use and modify for your projects!

Support
For issues or questions, please check the Google Gemini API Documentation.
