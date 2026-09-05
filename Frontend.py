import streamlit as st
import speech_recognition as sr
import streamlit.components.v1 as components
from main import ask_cypher

# 1. Page Config & Sci-Fi Modern UI Styling
st.set_page_config(page_title="CYPHER V 1.0 HUD Interface", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@500;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Rajdhani', sans-serif;
        background-color: #030a16;
        color: #00f3ff;
    }

    .stApp {
        background: radial-gradient(circle, #051329 0%, #02060d 100%);
    }

    /* Glowing HUD Title */
    .hud-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        color: #00f3ff;
        text-shadow: 0 0 10px #00f3ff, 0 0 20px #00f3ff, 0 0 40px #00a8ff;
        letter-spacing: 4px;
        margin-bottom: 5px;
    }

    .hud-sub {
        text-align: center;
        color: #00a8ff;
        font-size: 1.1rem;
        letter-spacing: 3px;
        margin-bottom: 25px;
    }

    /* Glassmorphism Futuristic Cards */
    .hud-card {
        background: rgba(4, 20, 40, 0.6);
        border: 1px solid #00f3ff;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.2);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
    }

    /* Sci-Fi Futuristic Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #0052d4, #4364f7, #00f3ff);
        color: #ffffff;
        font-family: 'Orbitron', sans-serif;
        font-weight: 700;
        border: 1px solid #00f3ff;
        border-radius: 6px;
        padding: 12px 24px;
        box-shadow: 0 0 15px rgba(0, 243, 255, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .stButton>button:hover {
        background: linear-gradient(45deg, #00f3ff, #0052d4);
        box-shadow: 0 0 30px #00f3ff;
        color: #000;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown('<div class="hud-title">CYPHER V 1.0</div>', unsafe_allow_html=True)
st.markdown('<div class="hud-sub">[ VIRTUAL TACTICAL INTELLIGENCE SYSTEM ]</div>', unsafe_allow_html=True)
st.write("---")

# Browser Speech Output Function
def speak_in_browser(text):
    # Take only the first 2 sentences
    sentences = text.replace("\n", " ").split(".")
    short_text = ".".join(sentences[:2]).strip()

    if short_text:
        short_text += "."

    safe_text = short_text.replace("\\", "\\\\").replace('"', '\\"')

    js_code = f"""
        <script>
            var msg = new SpeechSynthesisUtterance("{safe_text}");
            msg.lang = "en-IN";
            msg.rate = 1.0;
            msg.pitch = 1.0;

            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(msg);
        </script>
    """

    components.html(js_code, height=0)

# Safe Microphone Voice Recognition Function
def takeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("⚡ [SYSTEM STATUS: LISTENING MODE ENGAGED] Speak Now...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5)
            st.warning("🔄 [PROCESSING AUDIO DATA...]")
            query = r.recognize_google(audio, language="en-IN")
            return query
    except OSError:
        st.error("❌ Microphone access error! Check PyAudio installation or device connection.")
        return None
    except sr.WaitTimeoutError:
        st.warning("⚠️ Listening timed out. No speech detected.")
        return None
    except Exception:
        return None

# Main HUD Interface Layout
col1, col2 = st.columns([1.2, 2])

with col1:
    st.markdown('<div class="hud-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #00f3ff; font-family: Orbitron;'>CYPHER CORE</h3>", unsafe_allow_html=True)
    
    # Realistic 3D Rotating Earth Globe using Three.js Texture Mapping
    three_js_real_earth = """
    <div id="earth-container" style="width: 100%; height: 210px; display: flex; justify-content: center; align-items: center;"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script>
        const container = document.getElementById('earth-container');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
        camera.position.z = 210;

        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(200, 200);
        container.appendChild(renderer.domElement);

        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 1.2);
        scene.add(ambientLight);
        const pointLight = new THREE.PointLight(0x00f3ff, 1.5);
        pointLight.position.set(100, 100, 100);
        scene.add(pointLight);

        // Earth Sphere Creation
        const geometry = new THREE.SphereGeometry(65, 64, 64);
        
        // High Quality Sci-Fi Earth Texture Map
        const textureLoader = new THREE.TextureLoader();
        const earthTexture = textureLoader.load('https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/textures/planets/earth_atmos_2048.jpg', () => {
            renderer.render(scene, camera);
        });

        const material = new THREE.MeshPhongMaterial({
            map: earthTexture,
            shininess: 25
        });

        const earth = new THREE.Mesh(geometry, material);
        scene.add(earth);

        // Holographic Outer Atmosphere Ring
        const ringGeo = new THREE.SphereGeometry(68, 32, 32);
        const ringMat = new THREE.MeshBasicMaterial({
            color: 0x00f3ff,
            wireframe: true,
            transparent: true,
            opacity: 0.12
        });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        scene.add(ring);

        function animate() {
            requestAnimationFrame(animate);
            earth.rotation.y += 0.006;
            ring.rotation.y += 0.003;
            renderer.render(scene, camera);
        }
        animate();
    </script>
    """
    components.html(three_js_real_earth, height=220)
    
    st.markdown("<p style='text-align: center; color: #00a8ff;'>SYSTEM STATUS: ONLINE</p>", unsafe_allow_html=True)
    
    # Action Button
    if st.button("INITIALIZE VOICE INPUT 🎙️", use_container_width=True):
        query = takeCommand()
        if query:
            st.session_state['user_said'] = query
            # Send the user's question to Gemini
            st.session_state['cypher_reply'] = ask_cypher(query)
        else:
            st.session_state['user_said'] = "NO VOICE DATA DETECTED"
            st.session_state['cypher_reply'] = "Access Denied. Voice signal not recognized or microphone unavailable."
            
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="hud-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00f3ff; font-family: Orbitron;'>TACTICAL DISPLAY TERMINAL</h3>", unsafe_allow_html=True)
    
    if 'user_said' in st.session_state:
        st.success(f"👤 **USER COMMAND:** {st.session_state['user_said']}")
        st.markdown(f"### 🤖 **C.Y.P.H.E.R:** {st.session_state['cypher_reply']}")
        speak_in_browser(st.session_state['cypher_reply'])
    else:
        st.info("SYSTEM READY. AWAITING USER COMMAND...")
        
    st.markdown('</div>', unsafe_allow_html=True)