/* ===================================
   MOVIE PRODUCTION STUDIO - MAIN JS
   Modern Interactions & API Calls
   =================================== */

// Smooth scroll to tools section
function scrollToTools() {
    document.getElementById('tools').scrollIntoView({ 
        behavior: 'smooth',
        block: 'start'
    });
}

// Toast notification system
function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    const icon = type === 'success' ? 'check-circle' : 
                 type === 'error' ? 'exclamation-circle' : 
                 'info-circle';
    
    toast.innerHTML = `
        <i class="fas fa-${icon}" style="font-size: 1.5rem; color: ${
            type === 'success' ? '#22c55e' : 
            type === 'error' ? '#ef4444' : 
            'var(--accent-blue)'
        }"></i>
        <span>${message}</span>
    `;
    
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

// Loading overlay
function showLoading(show = true) {
    const overlay = document.getElementById('loadingOverlay');
    if (show) {
        overlay.classList.add('active');
    } else {
        overlay.classList.remove('active');
    }
}

// Generate Script
async function generateScript() {
    const movieIdea = document.getElementById('movieIdea').value;
    
    if (!movieIdea.trim()) {
        showToast('Please enter a movie idea', 'error');
        return;
    }
    
    showLoading(true);
    
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ movie_idea: movieIdea })
        });
        
        const data = await response.json();
        
        if (data.error) {
            showToast(data.error, 'error');
        } else {
            displayScriptResult(data);
            showToast('Script generated successfully!', 'success');
        }
    } catch (error) {
        showToast('Failed to generate script. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

function displayScriptResult(data) {
    const resultDiv = document.getElementById('scriptResult');
    resultDiv.innerHTML = `
        <div style="padding: 1.5rem;">
            <h4 style="color: var(--accent-blue); margin-bottom: 1rem; font-size: 1.25rem;">
                <i class="fas fa-film"></i> Generated Production Package
            </h4>
            
            <div style="margin-bottom: 1.5rem;">
                <h5 style="color: var(--text-primary); margin-bottom: 0.5rem;">Screenplay</h5>
                <p style="color: var(--text-secondary); line-height: 1.8;">${data.screenplay}</p>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <h5 style="color: var(--text-primary); margin-bottom: 0.5rem;">Characters</h5>
                ${data.characters.map(char => `
                    <div style="background: var(--bg-primary); padding: 1rem; border-radius: var(--radius-md); margin-bottom: 0.5rem;">
                        <strong style="color: var(--accent-cyan);">${char.name}</strong>
                        <p style="color: var(--text-secondary); margin-top: 0.5rem;">${char.description}</p>
                    </div>
                `).join('')}
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <h5 style="color: var(--text-primary); margin-bottom: 0.5rem;">Production Complexity</h5>
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="background: var(--gradient-primary); padding: 0.5rem 1rem; border-radius: var(--radius-md); font-weight: 700;">
                        ${data.production_complexity_score}/10
                    </div>
                    <p style="color: var(--text-secondary);">${data.production_complexity_explanation}</p>
                </div>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <h5 style="color: var(--text-primary); margin-bottom: 0.5rem;">Video Animation Prompt</h5>
                <p style="color: var(--text-secondary); background: var(--bg-primary); padding: 1rem; border-radius: var(--radius-md); font-style: italic;">
                    ${data.video_animation_prompt}
                </p>
            </div>
            
            <div style="display: flex; gap: 1rem; margin-top: 1.5rem;">
                <button class="btn-outline" onclick="downloadPDF()">
                    <i class="fas fa-file-pdf"></i> Download PDF
                </button>
                <button class="btn-outline" onclick="copyToClipboard('${data.video_animation_prompt.replace(/'/g, "\\'")}')">
                    <i class="fas fa-copy"></i> Copy Video Prompt
                </button>
            </div>
        </div>
    `;
    resultDiv.classList.add('active');
}

// Generate Video
async function generateVideo() {
    const prompt = document.getElementById('videoPrompt').value;
    const model = document.getElementById('videoModel').value;
    
    if (!prompt.trim()) {
        showToast('Please enter a video prompt', 'error');
        return;
    }
    
    showLoading(true);
    showToast('Generating video... This may take 60-90 seconds', 'info');
    
    try {
        // Extended timeout for video generation
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 120000); // 2 minute timeout
        
        const response = await fetch('/generate-video', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                prompt: prompt,
                model: model
            }),
            signal: controller.signal
        });
        
        clearTimeout(timeoutId);
        
        const data = await response.json();
        
        if (data.error) {
            showToast(data.error, 'error');
        } else {
            displayVideoResult(data);
            showToast('Video generated successfully!', 'success');
        }
    } catch (error) {
        if (error.name === 'AbortError') {
            showToast('Video generation timeout - try a shorter/simpler prompt', 'error');
        } else {
            showToast('Failed to generate video. Please try again.', 'error');
        }
    } finally {
        showLoading(false);
    }
}

function displayVideoResult(data) {
    const resultDiv = document.getElementById('videoResult');
    resultDiv.innerHTML = `
        <div style="padding: 1.5rem;">
            <video controls style="width: 100%; border-radius: var(--radius-md); margin-bottom: 1rem;">
                <source src="${data.video_url}" type="video/mp4">
            </video>
            <button class="btn-outline" onclick="window.open('${data.video_url}', '_blank')">
                <i class="fas fa-download"></i> Download Video
            </button>
        </div>
    `;
    resultDiv.classList.add('active');
}

// Generate Image
async function generateImage() {
    const prompt = document.getElementById('imagePrompt').value;
    const model = document.getElementById('imageModel').value;
    
    if (!prompt.trim()) {
        showToast('Please enter an image prompt', 'error');
        return;
    }
    
    showLoading(true);
    showToast('Generating with Pollinations.AI FLUX... (10-30 seconds)', 'info');
    
    try {
        // Create abort controller for timeout
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 90000); // 90 second timeout
        
        const response = await fetch('/generate-image', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                prompt: prompt,
                model: model
            }),
            signal: controller.signal
        });
        
        clearTimeout(timeoutId);
        
        const data = await response.json();
        
        if (data.error) {
            showToast(data.error, 'error');
        } else {
            displayImageResult(data);
            showToast('Image generated successfully!', 'success');
        }
    } catch (error) {
        if (error.name === 'AbortError') {
            showToast('Request timeout - try a simpler prompt or try again', 'error');
        } else {
            showToast('Failed to generate image. Please try again.', 'error');
        }
    } finally {
        showLoading(false);
    }
}

function displayImageResult(data) {
    const resultDiv = document.getElementById('imageResult');
    resultDiv.innerHTML = `
        <div style="padding: 1.5rem;">
            <img src="${data.image_url}" style="width: 100%; border-radius: var(--radius-md); margin-bottom: 1rem;" alt="Generated">
            <button class="btn-outline" onclick="window.open('${data.image_url}', '_blank')">
                <i class="fas fa-download"></i> Download Image
            </button>
        </div>
    `;
    resultDiv.classList.add('active');
}

// Generate Music
async function generateMusic() {
    const prompt = document.getElementById('musicPrompt').value;
    const model = document.getElementById('musicModel').value;
    
    if (!prompt.trim()) {
        showToast('Please enter a music style', 'error');
        return;
    }
    
    showLoading(true);
    showToast('Generating music... This may take a moment', 'info');
    
    try {
        const response = await fetch('/generate-music', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                prompt: prompt,
                model: model
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            showToast(data.error, 'error');
        } else {
            displayMusicResult(data);
            showToast('Music generated successfully!', 'success');
        }
    } catch (error) {
        showToast('Failed to generate music. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

function displayMusicResult(data) {
    const resultDiv = document.getElementById('musicResult');
    resultDiv.innerHTML = `
        <div style="padding: 1rem;">
            <audio controls style="width: 100%;">
                <source src="${data.audio_url}" type="audio/wav">
            </audio>
        </div>
    `;
    resultDiv.classList.add('active');
}

// Generate Voice
async function generateVoice() {
    const text = document.getElementById('voiceText').value;
    
    if (!text.trim()) {
        showToast('Please enter text to convert', 'error');
        return;
    }
    
    showLoading(true);
    
    try {
        const response = await fetch('/generate-voice', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        if (data.error) {
            showToast(data.error, 'error');
        } else {
            displayVoiceResult(data);
            showToast('Voice generated successfully!', 'success');
        }
    } catch (error) {
        showToast('Failed to generate voice. Please try again.', 'error');
    } finally {
        showLoading(false);
    }
}

function displayVoiceResult(data) {
    const resultDiv = document.getElementById('voiceResult');
    resultDiv.innerHTML = `
        <div style="padding: 1rem;">
            <audio controls style="width: 100%;">
                <source src="${data.audio_url}" type="audio/wav">
            </audio>
        </div>
    `;
    resultDiv.classList.add('active');
}

// Storyboard Functions
function addStoryboardFrame() {
    const grid = document.getElementById('storyboardGrid');
    const frameCount = grid.children.length;
    
    const frame = document.createElement('div');
    frame.className = 'storyboard-item';
    frame.innerHTML = `
        <div style="padding: 1rem; text-align: center;">
            <p style="color: var(--text-muted); font-size: 0.875rem;">Frame ${frameCount}</p>
            <input type="text" placeholder="Scene description..." class="modern-input" style="margin-top: 0.5rem; font-size: 0.875rem;">
        </div>
    `;
    
    grid.insertBefore(frame, grid.lastChild);
    showToast('Frame added to storyboard', 'success');
}

// Shot List Functions
function addShot() {
    const shotList = document.getElementById('shotList');
    const shotItem = document.createElement('div');
    shotItem.className = 'shot-item';
    shotItem.innerHTML = `
        <input type="text" placeholder="Shot description..." class="modern-input">
        <div class="shot-details">
            <select class="modern-select small">
                <option>Wide</option>
                <option>Medium</option>
                <option>Close-up</option>
                <option>Extreme Close-up</option>
                <option>Over-the-shoulder</option>
            </select>
            <input type="text" placeholder="Duration (e.g., 5s)" class="modern-input small">
        </div>
    `;
    shotList.appendChild(shotItem);
    showToast('Shot added to list', 'success');
}

// Video Enhancement
function enhanceVideo() {
    const fileInput = document.getElementById('videoUpload');
    
    if (!fileInput.files || !fileInput.files[0]) {
        showToast('Please select a video file first', 'error');
        return;
    }
    
    showLoading(true);
    showToast('Enhancing video... This will take some time', 'info');
    
    // Simulate enhancement (in production, upload to server)
    setTimeout(() => {
        showLoading(false);
        showToast('Video enhancement feature coming soon!', 'info');
    }, 2000);
}

// Utility Functions
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copied to clipboard!', 'success');
    }).catch(() => {
        showToast('Failed to copy', 'error');
    });
}

async function downloadPDF() {
    try {
        const response = await fetch('/download-pdf', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'movie-production-package.pdf';
        a.click();
        showToast('PDF downloaded successfully!', 'success');
    } catch (error) {
        showToast('Failed to download PDF', 'error');
    }
}

// Micro-interactions
document.addEventListener('DOMContentLoaded', () => {
    // Add hover effects to nav links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
        });
    });
    
    // Parallax effect for hero orbs
    document.addEventListener('mousemove', (e) => {
        const orbs = document.querySelectorAll('.gradient-orb');
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        
        orbs.forEach((orb, index) => {
            const speed = (index + 1) * 20;
            orb.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
        });
    });
    
    // Intersection Observer for animations
    const cards = document.querySelectorAll('.bento-card, .feature-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.6s ease-out forwards';
            }
        });
    }, { threshold: 0.1 });
    
    cards.forEach(card => observer.observe(card));
});

// Enter key support for inputs
document.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        const activeElement = document.activeElement;
        
        if (activeElement.id === 'movieIdea') generateScript();
        if (activeElement.id === 'videoPrompt') generateVideo();
        if (activeElement.id === 'imagePrompt') generateImage();
        if (activeElement.id === 'musicPrompt') generateMusic();
        if (activeElement.id === 'voiceText') generateVoice();
    }
});

// ===================================
// DROPDOWN MENU & SMOOTH SCROLL
// ===================================

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const dropdown = document.querySelector('.nav-dropdown');
    if (dropdown && !dropdown.contains(event.target)) {
        // Dropdown will close automatically with CSS :hover
    }
});

// Smooth scroll to tool sections
document.querySelectorAll('a[href^="#tool-"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            // Scroll to element with offset for fixed navbar
            const navbarHeight = 80;
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - navbarHeight;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });

            // Highlight the card briefly
            targetElement.style.animation = 'none';
            setTimeout(() => {
                targetElement.style.animation = 'highlightCard 1s ease-out';
            }, 10);
        }
    });
});

// Add highlight animation
const style = document.createElement('style');
style.textContent = \
    @keyframes highlightCard {
        0% {
            box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
            transform: scale(1);
        }
        50% {
            box-shadow: 0 0 30px 10px rgba(59, 130, 246, 0.4);
            transform: scale(1.02);
        }
        100% {
            box-shadow: var(--shadow-glow);
            transform: scale(1);
        }
    }
\;
document.head.appendChild(style);

// Auto-play videos when they come into view
const observerOptions = {
    threshold: 0.5
};

const videoObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        const video = entry.target;
        if (entry.isIntersecting) {
            video.play().catch(err => console.log('Video autoplay prevented'));
        } else {
            video.pause();
        }
    });
}, observerOptions);

// Observe all example videos
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.example-media video').forEach(video => {
        videoObserver.observe(video);
        
        // Ensure videos loop and are muted
        video.loop = true;
        video.muted = true;
        video.playsInline = true;
        
        // Click to play/pause
        video.addEventListener('click', function() {
            if (this.paused) {
                this.play();
            } else {
                this.pause();
            }
        });
    });
});

// Update active nav link on scroll
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('[id^="tool-"]');
    const navLinks = document.querySelectorAll('.dropdown-item');
    
    let currentSection = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionBottom = sectionTop + section.offsetHeight;
        
        if (window.pageYOffset >= sectionTop && window.pageYOffset < sectionBottom) {
            currentSection = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + currentSection) {
            link.classList.add('active');
        }
    });
});
