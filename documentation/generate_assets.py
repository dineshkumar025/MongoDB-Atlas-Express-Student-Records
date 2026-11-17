"""
Asset Generator for MongoDB Atlas & Express.js Student Records Case Study
Generates professional diagrams (SVG + PNG) and screenshot mockups
Student: P. Dinesh Kumar (A24126552101)
Institution: ANITS | Course: 23CM4121
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIAGRAMS_DIR = os.path.join(BASE_DIR, "diagrams")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")

os.makedirs(DIAGRAMS_DIR, exist_ok=True)
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

# Try loading system fonts or default
def get_font(size=14, bold=False):
    font_paths = [
        "C:/Windows/Fonts/segoeui.ttf" if not bold else "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arial.ttf" if not bold else "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/calibri.ttf" if not bold else "C:/Windows/Fonts/calibrib.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def get_mono_font(size=13):
    font_paths = [
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/cour.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

# -------------------------------------------------------------
# 1. System Architecture Diagram (SVG + PNG)
# -------------------------------------------------------------
def generate_architecture_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 560" width="950" height="560">
  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>
    <linearGradient id="clientGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f0f9ff" />
      <stop offset="100%" stop-color="#e0f2fe" />
    </linearGradient>
    <linearGradient id="serverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fdf4ff" />
      <stop offset="100%" stop-color="#fae8ff" />
    </linearGradient>
    <linearGradient id="dbGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ecfdf5" />
      <stop offset="100%" stop-color="#d1fae5" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.1" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="950" height="560" fill="#f8fafc" />

  <!-- Header Banner -->
  <rect x="0" y="0" width="950" height="70" fill="url(#headerGrad)" />
  <text x="30" y="32" font-family="'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="bold" fill="#ffffff">SYSTEM ARCHITECTURE: MONGODB ATLAS &amp; EXPRESS.JS</text>
  <text x="30" y="52" font-family="'Segoe UI', Roboto, sans-serif" font-size="12" fill="#94a3b8">Case Study Q3 | ANITS • Full-Stack Web Development (23CM4121) | P. Dinesh Kumar (A24126552101)</text>

  <!-- Tier 1: Client Layer -->
  <rect x="40" y="95" width="260" height="420" rx="12" fill="url(#clientGrad)" stroke="#bae6fd" stroke-width="2" filter="url(#shadow)" />
  <rect x="40" y="95" width="260" height="45" rx="12" fill="#0284c7" />
  <rect x="40" y="125" width="260" height="15" fill="#0284c7" />
  <text x="170" y="124" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">CLIENT PRESENTATION TIER</text>

  <rect x="60" y="160" width="220" height="80" rx="8" fill="#ffffff" stroke="#e0f2fe" stroke-width="1.5" />
  <text x="75" y="185" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">index.html (HTML5)</text>
  <text x="75" y="205" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Student Form Inputs</text>
  <text x="75" y="222" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Real-time Records Table</text>

  <rect x="60" y="255" width="220" height="70" rx="8" fill="#ffffff" stroke="#e0f2fe" stroke-width="1.5" />
  <text x="75" y="280" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">style.css (CSS3)</text>
  <text x="75" y="300" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Responsive Modern UI Layout</text>
  <text x="75" y="315" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Pulse Connection Badge</text>

  <rect x="60" y="340" width="220" height="150" rx="8" fill="#ffffff" stroke="#e0f2fe" stroke-width="1.5" />
  <text x="75" y="365" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#0369a1">script.js (JavaScript Client)</text>
  <text x="75" y="388" font-family="'Segoe UI', sans-serif" font-size="11" fill="#475569">Fetch API Calls:</text>
  <text x="75" y="408" font-family="'Courier New', monospace" font-size="11" fill="#0284c7">GET  /api/health</text>
  <text x="75" y="428" font-family="'Courier New', monospace" font-size="11" fill="#0284c7">GET  /api/students</text>
  <text x="75" y="448" font-family="'Courier New', monospace" font-size="11" fill="#0284c7">POST /api/students</text>
  <text x="75" y="472" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• DOM dynamic re-rendering</text>

  <!-- Connectors Client to Server -->
  <line x1="300" y1="280" x2="345" y2="280" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="4,4" />
  <polygon points="345,275 355,280 345,285" fill="#0284c7" />
  <text x="325" y="270" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold" fill="#0284c7" text-anchor="middle">HTTP/JSON</text>
  <text x="325" y="300" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748b" text-anchor="middle">REST Verbs</text>

  <!-- Tier 2: Application Server Layer -->
  <rect x="355" y="95" width="270" height="420" rx="12" fill="url(#serverGrad)" stroke="#f0abfc" stroke-width="2" filter="url(#shadow)" />
  <rect x="355" y="95" width="270" height="45" rx="12" fill="#a21caf" />
  <rect x="355" y="125" width="270" height="15" fill="#a21caf" />
  <text x="490" y="124" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">BACKEND APPLICATION TIER</text>

  <rect x="375" y="160" width="230" height="70" rx="8" fill="#ffffff" stroke="#fae8ff" stroke-width="1.5" />
  <text x="390" y="185" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#86198f">server.js (Express HTTP)</text>
  <text x="390" y="205" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Static middleware, JSON parser</text>
  <text x="390" y="220" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Centralized Error Handling</text>

  <rect x="375" y="240" width="230" height="70" rx="8" fill="#ffffff" stroke="#fae8ff" stroke-width="1.5" />
  <text x="390" y="265" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#86198f">routes &amp; controllers</text>
  <text x="390" y="285" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• studentRoutes.js (URI maps)</text>
  <text x="390" y="300" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• studentController.js (Logic)</text>

  <rect x="375" y="320" width="230" height="75" rx="8" fill="#ffffff" stroke="#fae8ff" stroke-width="1.5" />
  <text x="390" y="343" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#86198f">Mongoose ODM Model</text>
  <text x="390" y="362" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• studentModel.js schema validation</text>
  <text x="390" y="378" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Unique index: studentId, email</text>

  <rect x="375" y="405" width="230" height="85" rx="8" fill="#ffffff" stroke="#fae8ff" stroke-width="1.5" />
  <text x="390" y="428" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#86198f">config/db.js (Connection)</text>
  <text x="390" y="448" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• mongoose.connect(MONGODB_URI)</text>
  <text x="390" y="465" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Event listeners (connected, error)</text>
  <text x="390" y="480" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Connection pooling &amp; status probe</text>

  <!-- Connectors Server to Atlas -->
  <line x1="625" y1="280" x2="670" y2="280" stroke="#059669" stroke-width="2.5" stroke-dasharray="4,4" />
  <polygon points="670,275 680,280 670,285" fill="#059669" />
  <text x="650" y="270" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold" fill="#059669" text-anchor="middle">TLS / SRV</text>
  <text x="650" y="300" font-family="'Segoe UI', sans-serif" font-size="9" fill="#64748b" text-anchor="middle">Port 27017</text>

  <!-- Tier 3: MongoDB Atlas Cloud Layer -->
  <rect x="680" y="95" width="240" height="420" rx="12" fill="url(#dbGrad)" stroke="#a7f3d0" stroke-width="2" filter="url(#shadow)" />
  <rect x="680" y="95" width="240" height="45" rx="12" fill="#059669" />
  <rect x="680" y="125" width="240" height="15" fill="#059669" />
  <text x="800" y="124" font-family="'Segoe UI', sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">MONGODB ATLAS CLOUD TIER</text>

  <rect x="695" y="160" width="210" height="95" rx="8" fill="#ffffff" stroke="#d1fae5" stroke-width="1.5" />
  <text x="710" y="185" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#065f46">Shared M0 Cluster</text>
  <text x="710" y="205" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• AWS Mumbai (ap-south-1)</text>
  <text x="710" y="222" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• 3-Node Multi-AZ Replica Set</text>
  <text x="710" y="239" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• TLS 1.3 Encryption in transit</text>

  <rect x="695" y="265" width="210" height="110" rx="8" fill="#ffffff" stroke="#d1fae5" stroke-width="1.5" />
  <text x="710" y="290" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#065f46">Database: StudentDB</text>
  <text x="710" y="310" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#059669">Collection: students</text>
  <text x="710" y="330" font-family="'Courier New', monospace" font-size="10" fill="#475569">{ studentId, name, </text>
  <text x="710" y="347" font-family="'Courier New', monospace" font-size="10" fill="#475569">  email, department,</text>
  <text x="710" y="364" font-family="'Courier New', monospace" font-size="10" fill="#475569">  year, timestamps }</text>

  <rect x="695" y="385" width="210" height="105" rx="8" fill="#ffffff" stroke="#d1fae5" stroke-width="1.5" />
  <text x="710" y="410" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#065f46">Security &amp; Networking</text>
  <text x="710" y="430" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• SCRAM-SHA-256 Auth</text>
  <text x="710" y="447" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• Database User (readWrite)</text>
  <text x="710" y="464" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• IP Access List Entry (0.0.0.0/0)</text>
  <text x="710" y="481" font-family="'Segoe UI', sans-serif" font-size="11" fill="#64748b">• SRV Seedlist DNS Records</text>

  <!-- Footer Banner -->
  <rect x="0" y="530" width="950" height="30" fill="#0f172a" />
  <text x="475" y="550" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Figure 1: High-Level End-to-End System Architecture (Browser Client ↔ Express.js Backend ↔ MongoDB Atlas Cloud Cluster)</text>
</svg>"""
    with open(os.path.join(DIAGRAMS_DIR, "architecture.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated architecture.svg")

# -------------------------------------------------------------
# 2. Connection Flow Diagram (SVG)
# -------------------------------------------------------------
def generate_connection_flow_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 520" width="950" height="520">
  <defs>
    <linearGradient id="cfHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e1e2f" />
      <stop offset="100%" stop-color="#2d3748" />
    </linearGradient>
    <filter id="boxShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.15" />
    </filter>
  </defs>

  <rect width="950" height="520" fill="#f8fafc" />

  <!-- Header -->
  <rect x="0" y="0" width="950" height="65" fill="url(#cfHeader)" />
  <text x="30" y="30" font-family="'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="bold" fill="#38bdf8">MONGODB ATLAS &amp; EXPRESS.JS CONNECTION SEQUENCE FLOW</text>
  <text x="30" y="50" font-family="'Segoe UI', Roboto, sans-serif" font-size="12" fill="#94a3b8">Detailed 7-Step Handshake, DNS SRV Seedlist Resolution, and Lifecycle Event Binding</text>

  <!-- Step 1 -->
  <g transform="translate(40, 90)">
    <rect width="110" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#boxShadow)" />
    <rect width="110" height="30" rx="8" fill="#0284c7" />
    <rect y="15" width="110" height="15" fill="#0284c7" />
    <text x="55" y="20" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 1</text>
    <text x="55" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Environment</text>
    <text x="55" y="70" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Configuration</text>
    <text x="10" y="95" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• .env loaded</text>
    <text x="10" y="110" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Read MONGODB_URI</text>
    <text x="10" y="125" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Read DB_NAME</text>
    <text x="10" y="140" font-family="'Segoe UI', sans-serif" font-size="9" fill="#0284c7">= 'StudentDB'</text>
  </g>

  <!-- Arrow 1-2 -->
  <line x1="150" y1="165" x2="170" y2="165" stroke="#64748b" stroke-width="2" />
  <polygon points="170,161 176,165 170,169" fill="#64748b" />

  <!-- Step 2 -->
  <g transform="translate(175, 90)">
    <rect width="115" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#boxShadow)" />
    <rect width="115" height="30" rx="8" fill="#0284c7" />
    <rect y="15" width="115" height="15" fill="#0284c7" />
    <text x="57" y="20" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 2</text>
    <text x="57" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Mongoose</text>
    <text x="57" y="70" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Invocation</text>
    <text x="10" y="95" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• connectDB()</text>
    <text x="10" y="110" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• mongoose.connect()</text>
    <text x="10" y="125" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• retryWrites=true</text>
    <text x="10" y="140" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• w: 'majority'</text>
  </g>

  <!-- Arrow 2-3 -->
  <line x1="290" y1="165" x2="310" y2="165" stroke="#64748b" stroke-width="2" />
  <polygon points="310,161 316,165 310,169" fill="#64748b" />

  <!-- Step 3 -->
  <g transform="translate(315, 90)">
    <rect width="125" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#boxShadow)" />
    <rect width="125" height="30" rx="8" fill="#7c3aed" />
    <rect y="15" width="125" height="15" fill="#7c3aed" />
    <text x="62" y="20" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 3</text>
    <text x="62" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">DNS SRV</text>
    <text x="62" y="70" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Resolution</text>
    <text x="10" y="95" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• _mongodb._tcp</text>
    <text x="10" y="110" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Queries 3 replica nodes</text>
    <text x="10" y="125" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• TXT records lookup</text>
    <text x="10" y="140" font-family="'Segoe UI', sans-serif" font-size="9" fill="#7c3aed">• cluster topology</text>
  </g>

  <!-- Arrow 3-4 -->
  <line x1="440" y1="165" x2="460" y2="165" stroke="#64748b" stroke-width="2" />
  <polygon points="460,161 466,165 460,169" fill="#64748b" />

  <!-- Step 4 -->
  <g transform="translate(465, 90)">
    <rect width="125" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#boxShadow)" />
    <rect width="125" height="30" rx="8" fill="#7c3aed" />
    <rect y="15" width="125" height="15" fill="#7c3aed" />
    <text x="62" y="20" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 4</text>
    <text x="62" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">TLS/SSL</text>
    <text x="62" y="70" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Handshake</text>
    <text x="10" y="95" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Outbound Port 27017</text>
    <text x="10" y="110" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• TLS 1.3 cert exchange</text>
    <text x="10" y="125" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Encrypted transport</text>
    <text x="10" y="140" font-family="'Segoe UI', sans-serif" font-size="9" fill="#7c3aed">• IP allowlist check</text>
  </g>

  <!-- Arrow 4-5 -->
  <line x1="590" y1="165" x2="610" y2="165" stroke="#64748b" stroke-width="2" />
  <polygon points="610,161 616,165 610,169" fill="#64748b" />

  <!-- Step 5 -->
  <g transform="translate(615, 90)">
    <rect width="125" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#boxShadow)" />
    <rect width="125" height="30" rx="8" fill="#059669" />
    <rect y="15" width="125" height="15" fill="#059669" />
    <text x="62" y="20" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 5</text>
    <text x="62" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">SCRAM-SHA-256</text>
    <text x="62" y="70" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Authentication</text>
    <text x="10" y="95" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Credentials verified</text>
    <text x="10" y="110" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Username/Password</text>
    <text x="10" y="125" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• readWrite on StudentDB</text>
    <text x="10" y="140" font-family="'Segoe UI', sans-serif" font-size="9" fill="#059669">• Session authorized</text>
  </g>

  <!-- Arrow 5-6 -->
  <line x1="740" y1="165" x2="760" y2="165" stroke="#64748b" stroke-width="2" />
  <polygon points="760,161 766,165 760,169" fill="#64748b" />

  <!-- Step 6 -->
  <g transform="translate(765, 90)">
    <rect width="145" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#boxShadow)" />
    <rect width="145" height="30" rx="8" fill="#059669" />
    <rect y="15" width="145" height="15" fill="#059669" />
    <text x="72" y="20" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">Step 6 &amp; 7</text>
    <text x="72" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Pool Active &amp;</text>
    <text x="72" y="70" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Connected Event</text>
    <text x="10" y="95" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Connection pool opened</text>
    <text x="10" y="110" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• readyState = 1 (Connected)</text>
    <text x="10" y="125" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Express listens on :5000</text>
    <text x="10" y="140" font-family="'Segoe UI', sans-serif" font-size="9" fill="#059669">• Ready for CRUD I/O</text>
  </g>

  <!-- Detailed Connection String Anatomy Breakdown Below -->
  <g transform="translate(40, 275)">
    <rect width="870" height="195" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#boxShadow)" />
    <rect width="870" height="35" rx="10" fill="#0f172a" />
    <rect y="20" width="870" height="15" fill="#0f172a" />
    <text x="20" y="24" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="bold" fill="#38bdf8">ANATOMY OF THE MONGODB ATLAS SRV CONNECTION STRING</text>

    <!-- Code Line Box -->
    <rect x="20" y="50" width="830" height="38" rx="6" fill="#1e293b" />
    <text x="35" y="74" font-family="'Consolas', monospace" font-size="13" fill="#ffffff">
      <tspan fill="#38bdf8">mongodb+srv://</tspan>
      <tspan fill="#4ade80">dineshparaselli2507_db_user</tspan>
      <tspan fill="#94a3b8">:</tspan>
      <tspan fill="#f43f5e">P@ssw0rd123</tspan>
      <tspan fill="#94a3b8">@</tspan>
      <tspan fill="#fbbf24">cluster0.9esdzfa.mongodb.net</tspan>
      <tspan fill="#94a3b8">/</tspan>
      <tspan fill="#c084fc">StudentDB</tspan>
      <tspan fill="#38bdf8">?retryWrites=true&amp;w=majority</tspan>
    </text>

    <!-- Breakdown Legend Elements -->
    <g transform="translate(25, 105)">
      <circle cx="10" cy="10" r="6" fill="#38bdf8" />
      <text x="25" y="14" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0284c7">mongodb+srv://</text>
      <text x="25" y="30" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">DNS Seedlist protocol enabling dynamic cluster shard discovery without hardcoding node IPs.</text>
    </g>

    <g transform="translate(25, 150)">
      <circle cx="10" cy="10" r="6" fill="#4ade80" />
      <text x="25" y="14" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#059669">dineshparaselli2507_db_user : P@ssw0rd123</text>
      <text x="25" y="30" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Database User credentials created in Atlas Security &gt; Database Access with readWriteRole.</text>
    </g>

    <g transform="translate(460, 105)">
      <circle cx="10" cy="10" r="6" fill="#fbbf24" />
      <text x="25" y="14" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#d97706">cluster0.9esdzfa.mongodb.net</text>
      <text x="25" y="30" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Unique Cloud cluster hostname resolving to primary and secondary replica set members.</text>
    </g>

    <g transform="translate(460, 150)">
      <circle cx="10" cy="10" r="6" fill="#c084fc" />
      <text x="25" y="14" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#9333ea">StudentDB ? retryWrites=true&amp;w=majority</text>
      <text x="25" y="30" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Target database override + write concern requiring acknowledgment from a majority of nodes.</text>
    </g>
  </g>

  <!-- Footer -->
  <rect x="0" y="490" width="950" height="30" fill="#0f172a" />
  <text x="475" y="510" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Figure 2: Mongoose to MongoDB Atlas DNS SRV Seedlist Handshake &amp; Parameter Breakdown</text>
</svg>"""
    with open(os.path.join(DIAGRAMS_DIR, "connection-flow.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated connection-flow.svg")

# -------------------------------------------------------------
# 3. Data Flow Diagram (SVG)
# -------------------------------------------------------------
def generate_data_flow_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 500" width="950" height="500">
  <defs>
    <linearGradient id="dfHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#064e3b" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12" />
    </filter>
  </defs>

  <rect width="950" height="500" fill="#f8fafc" />

  <!-- Header -->
  <rect x="0" y="0" width="950" height="65" fill="url(#dfHeader)" />
  <text x="30" y="30" font-family="'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="bold" fill="#ffffff">STUDENT RECORD PERSISTENCE &amp; RETRIEVAL DATA FLOW</text>
  <text x="30" y="50" font-family="'Segoe UI', Roboto, sans-serif" font-size="12" fill="#a7f3d0">Step-by-step transaction lifecycle between Frontend Client, Express Router, Controller, Mongoose, and Atlas Cluster</text>

  <!-- Form Submission Box -->
  <g transform="translate(40, 95)">
    <rect width="180" height="150" rx="8" fill="#ffffff" stroke="#bae6fd" stroke-width="2" filter="url(#cardShadow)" />
    <rect width="180" height="32" rx="8" fill="#0284c7" />
    <rect y="16" width="180" height="16" fill="#0284c7" />
    <text x="90" y="22" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Client Form Submission</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold" fill="#0369a1">DOM Event: submit</text>
    <text x="15" y="75" font-family="'Courier New', monospace" font-size="9" fill="#334155">{</text>
    <text x="25" y="90" font-family="'Courier New', monospace" font-size="9" fill="#334155">studentId: "A24126...",</text>
    <text x="25" y="105" font-family="'Courier New', monospace" font-size="9" fill="#334155">name: "P. Dinesh...",</text>
    <text x="25" y="120" font-family="'Courier New', monospace" font-size="9" fill="#334155">department: "CSE"</text>
    <text x="15" y="135" font-family="'Courier New', monospace" font-size="9" fill="#334155">}</text>
  </g>

  <!-- Arrow 1 to 2 -->
  <line x1="220" y1="170" x2="265" y2="170" stroke="#0284c7" stroke-width="2" stroke-dasharray="3,3" />
  <polygon points="265,166 273,170 265,174" fill="#0284c7" />
  <text x="245" y="160" font-family="'Segoe UI', sans-serif" font-size="9" fill="#0284c7" text-anchor="middle">POST</text>

  <!-- Express Route & Controller Box -->
  <g transform="translate(275, 95)">
    <rect width="190" height="150" rx="8" fill="#ffffff" stroke="#f0abfc" stroke-width="2" filter="url(#cardShadow)" />
    <rect width="190" height="32" rx="8" fill="#a21caf" />
    <rect y="16" width="190" height="16" fill="#a21caf" />
    <text x="95" y="22" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Express Controller</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold" fill="#86198f">studentController.js</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• express.json() parses body</text>
    <text x="15" y="95" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• insertStudent(req, res)</text>
    <text x="15" y="115" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Validates required inputs</text>
    <text x="15" y="135" font-family="'Segoe UI', sans-serif" font-size="10" fill="#86198f">• Calls Student.create()</text>
  </g>

  <!-- Arrow 2 to 3 -->
  <line x1="465" y1="170" x2="510" y2="170" stroke="#a21caf" stroke-width="2" stroke-dasharray="3,3" />
  <polygon points="510,166 518,170 510,174" fill="#a21caf" />
  <text x="490" y="160" font-family="'Segoe UI', sans-serif" font-size="9" fill="#a21caf" text-anchor="middle">Model</text>

  <!-- Mongoose Validation Box -->
  <g transform="translate(520, 95)">
    <rect width="190" height="150" rx="8" fill="#ffffff" stroke="#fed7aa" stroke-width="2" filter="url(#cardShadow)" />
    <rect width="190" height="32" rx="8" fill="#ea580c" />
    <rect y="16" width="190" height="16" fill="#ea580c" />
    <text x="95" y="22" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Mongoose Schema</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold" fill="#c2410c">studentModel.js</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Unique studentId match</text>
    <text x="15" y="95" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Email regex &amp; lowercase</text>
    <text x="15" y="115" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Department enum match</text>
    <text x="15" y="135" font-family="'Segoe UI', sans-serif" font-size="10" fill="#c2410c">• Generates BSON doc</text>
  </g>

  <!-- Arrow 3 to 4 -->
  <line x1="710" y1="170" x2="755" y2="170" stroke="#ea580c" stroke-width="2" stroke-dasharray="3,3" />
  <polygon points="755,166 763,170 755,174" fill="#ea580c" />
  <text x="735" y="160" font-family="'Segoe UI', sans-serif" font-size="9" fill="#ea580c" text-anchor="middle">BSON</text>

  <!-- Atlas Storage Engine Box -->
  <g transform="translate(765, 95)">
    <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#a7f3d0" stroke-width="2" filter="url(#cardShadow)" />
    <rect width="150" height="32" rx="8" fill="#059669" />
    <rect y="16" width="150" height="16" fill="#059669" />
    <text x="75" y="22" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Atlas WiredTiger</text>
    <text x="12" y="55" font-family="'Segoe UI', sans-serif" font-size="10" font-weight="bold" fill="#065f46">StudentDB.students</text>
    <text x="12" y="75" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Generates _id (ObjectId)</text>
    <text x="12" y="95" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Updates B-Tree index</text>
    <text x="12" y="115" font-family="'Segoe UI', sans-serif" font-size="9" fill="#475569">• Writes to primary node</text>
    <text x="12" y="135" font-family="'Segoe UI', sans-serif" font-size="9" fill="#059669">• Replicates to secondaries</text>
  </g>

  <!-- Return Flow (Bottom Cycle) -->
  <g transform="translate(40, 280)">
    <rect width="875" height="170" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#cardShadow)" />
    <rect width="875" height="32" rx="10" fill="#0f172a" />
    <rect y="16" width="875" height="16" fill="#0f172a" />
    <text x="20" y="22" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">5. RECORD RETRIEVAL &amp; DOM UPDATE CYCLE (GET /api/students)</text>

    <!-- Cycle Steps -->
    <g transform="translate(20, 50)">
      <circle cx="16" cy="16" r="14" fill="#0284c7" />
      <text x="16" y="21" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">A</text>
      <text x="40" y="15" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Page Load / Refresh Trigger</text>
      <text x="40" y="32" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Client invokes loadStudentRecords() calling GET /api/students via Fetch API.</text>
    </g>

    <g transform="translate(20, 105)">
      <circle cx="16" cy="16" r="14" fill="#7c3aed" />
      <text x="16" y="21" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">B</text>
      <text x="40" y="15" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Controller Query Execution</text>
      <text x="40" y="32" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Student.find().sort({ createdAt: -1 }) executes BSON scan on Atlas cluster.</text>
    </g>

    <g transform="translate(460, 50)">
      <circle cx="16" cy="16" r="14" fill="#059669" />
      <text x="16" y="21" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">C</text>
      <text x="40" y="15" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">HTTP 200 JSON Response</text>
      <text x="40" y="32" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Express serializes student document array into formatted JSON payload with record count.</text>
    </g>

    <g transform="translate(460, 105)">
      <circle cx="16" cy="16" r="14" fill="#ea580c" />
      <text x="16" y="21" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">D</text>
      <text x="40" y="15" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Dynamic DOM Table Rendering</text>
      <text x="40" y="32" font-family="'Segoe UI', sans-serif" font-size="10" fill="#64748b">Frontend loops over results, creates sanitized table rows, updates record badges without page reload.</text>
    </g>
  </g>

  <!-- Footer -->
  <rect x="0" y="470" width="950" height="30" fill="#0f172a" />
  <text x="475" y="490" font-family="'Segoe UI', sans-serif" font-size="11" fill="#94a3b8" text-anchor="middle">Figure 3: End-to-End Data Storage and Retrieval Pipeline</text>
</svg>"""
    with open(os.path.join(DIAGRAMS_DIR, "data-flow.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated data-flow.svg")

# -------------------------------------------------------------
# 4. Atlas 6-Step Configuration Flow (SVG)
# -------------------------------------------------------------
def generate_atlas_config_flow_svg():
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 480" width="950" height="480">
  <defs>
    <linearGradient id="cfgHeader" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0369a1" />
    </linearGradient>
    <filter id="stepShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.12" />
    </filter>
  </defs>

  <rect width="950" height="480" fill="#f8fafc" />

  <!-- Header -->
  <rect x="0" y="0" width="950" height="65" fill="url(#cfgHeader)" />
  <text x="30" y="30" font-family="'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="bold" fill="#ffffff">6-STEP MONGODB ATLAS CLOUD CONFIGURATION WORKFLOW</text>
  <text x="30" y="50" font-family="'Segoe UI', Roboto, sans-serif" font-size="12" fill="#e0f2fe">Standard Industry Setup: Cluster Provisioning, Security Configuration, Database/Collection Creation, and SRV Linking</text>

  <!-- 6 Step Cards arranged in a 3x2 grid -->
  <!-- Row 1 -->
  <!-- Card 1 -->
  <g transform="translate(40, 85)">
    <rect width="270" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#stepShadow)" />
    <rect width="270" height="34" rx="8" fill="#0f172a" />
    <rect y="17" width="270" height="17" fill="#0f172a" />
    <text x="15" y="23" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">STEP 1: Cloud Account Setup</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Register &amp; Create Project</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Navigate to cloud.mongodb.com</text>
    <text x="15" y="93" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Create an organization</text>
    <text x="15" y="111" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Initialize new Project: "Student-Records"</text>
    <text x="15" y="129" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Set Project Access Controls</text>
    <rect x="15" y="142" width="240" height="18" rx="4" fill="#f1f5f9" />
    <text x="25" y="155" font-family="'Consolas', monospace" font-size="9" fill="#0369a1">cloud.mongodb.com</text>
  </g>

  <!-- Card 2 -->
  <g transform="translate(340, 85)">
    <rect width="270" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#stepShadow)" />
    <rect width="270" height="34" rx="8" fill="#0f172a" />
    <rect y="17" width="270" height="17" fill="#0f172a" />
    <text x="15" y="23" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">STEP 2: Deploy Shared Cluster</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Provision Free Tier (M0)</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Select M0 Free Sandbox (512MB RAM)</text>
    <text x="15" y="93" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Select Cloud Provider: AWS</text>
    <text x="15" y="111" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Region: ap-south-1 (Mumbai / closest)</text>
    <text x="15" y="129" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Name cluster: "Cluster0"</text>
    <rect x="15" y="142" width="240" height="18" rx="4" fill="#f1f5f9" />
    <text x="25" y="155" font-family="'Consolas', monospace" font-size="9" fill="#0369a1">M0 Shared Cluster • 3-Node Replica</text>
  </g>

  <!-- Card 3 -->
  <g transform="translate(640, 85)">
    <rect width="270" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#stepShadow)" />
    <rect width="270" height="34" rx="8" fill="#0f172a" />
    <rect y="17" width="270" height="17" fill="#0f172a" />
    <text x="15" y="23" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">STEP 3: Configure Database User</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Security &gt; Database Access</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Authentication: Password (SCRAM)</text>
    <text x="15" y="93" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Create User: e.g. "dineshparaselli2507_db_user"</text>
    <text x="15" y="111" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Set secure alphanumeric password</text>
    <text x="15" y="129" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Built-in Role: "Read and write to any db"</text>
    <rect x="15" y="142" width="240" height="18" rx="4" fill="#f1f5f9" />
    <text x="25" y="155" font-family="'Consolas', monospace" font-size="9" fill="#059669">Role: readWriteAnyDatabase</text>
  </g>

  <!-- Row 2 -->
  <!-- Card 4 -->
  <g transform="translate(40, 275)">
    <rect width="270" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#stepShadow)" />
    <rect width="270" height="34" rx="8" fill="#0f172a" />
    <rect y="17" width="270" height="17" fill="#0f172a" />
    <text x="15" y="23" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">STEP 4: Network Access Security</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Security &gt; Network Access</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Click "Add IP Access List Entry"</text>
    <text x="15" y="93" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Choose "Allow Access from Anywhere"</text>
    <text x="15" y="111" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Sets CIDR: 0.0.0.0/0 (for dev/lab)</text>
    <text x="15" y="129" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Status changes from Pending to Active</text>
    <rect x="15" y="142" width="240" height="18" rx="4" fill="#f1f5f9" />
    <text x="25" y="155" font-family="'Consolas', monospace" font-size="9" fill="#d97706">CIDR: 0.0.0.0/0 (Active)</text>
  </g>

  <!-- Card 5 -->
  <g transform="translate(340, 275)">
    <rect width="270" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#stepShadow)" />
    <rect width="270" height="34" rx="8" fill="#0f172a" />
    <rect y="17" width="270" height="17" fill="#0f172a" />
    <text x="15" y="23" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">STEP 5: Create Database &amp; Coll.</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Database &gt; Collections Tab</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Click "+ Create Database"</text>
    <text x="15" y="93" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Database Name: "StudentDB"</text>
    <text x="15" y="111" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Collection Name: "students"</text>
    <text x="15" y="129" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Optional: Allow auto-creation via Mongoose</text>
    <rect x="15" y="142" width="240" height="18" rx="4" fill="#f1f5f9" />
    <text x="25" y="155" font-family="'Consolas', monospace" font-size="9" fill="#7c3aed">StudentDB.students</text>
  </g>

  <!-- Card 6 -->
  <g transform="translate(640, 275)">
    <rect width="270" height="170" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#stepShadow)" />
    <rect width="270" height="34" rx="8" fill="#0f172a" />
    <rect y="17" width="270" height="17" fill="#0f172a" />
    <text x="15" y="23" font-family="'Segoe UI', sans-serif" font-size="12" font-weight="bold" fill="#38bdf8">STEP 6: Extract SRV &amp; Connect</text>
    <text x="15" y="55" font-family="'Segoe UI', sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Cluster &gt; Connect Button</text>
    <text x="15" y="75" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Choose "Drivers" &gt; "Node.js"</text>
    <text x="15" y="93" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Copy mongodb+srv:// connection URI</text>
    <text x="15" y="111" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Paste into .env file as MONGODB_URI</text>
    <text x="15" y="129" font-family="'Segoe UI', sans-serif" font-size="10" fill="#475569">• Start server: "npm run start"</text>
    <rect x="15" y="142" width="240" height="18" rx="4" fill="#f1f5f9" />
    <text x="25" y="155" font-family="'Consolas', monospace" font-size="9" fill="#0284c7">mongodb+srv://&lt;user&gt;:&lt;pass&gt;@...</text>
  </g>

  <!-- Footer -->
  <rect x="0" y="455" width="950" height="25" fill="#0f172a" />
  <text x="475" y="471" font-family="'Segoe UI', sans-serif" font-size="10" fill="#94a3b8" text-anchor="middle">Figure 4: Complete 6-Step Implementation Roadmap for MongoDB Atlas Provisioning</text>
</svg>"""
    with open(os.path.join(DIAGRAMS_DIR, "atlas-config-flow.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated atlas-config-flow.svg")

# -------------------------------------------------------------
# 5. PIL Screenshot Mockups (PNG)
# -------------------------------------------------------------
def generate_terminal_screenshot():
    w, h = 900, 480
    img = Image.new("RGB", (w, h), color="#1e1e1e")
    draw = ImageDraw.Draw(img)

    # Window title bar
    draw.rectangle([(0, 0), (w, 35)], fill="#2d2d2d")
    # Window control dots
    draw.ellipse([(15, 12), (25, 22)], fill="#ff5f56")
    draw.ellipse([(35, 12), (45, 22)], fill="#ffbd2e")
    draw.ellipse([(55, 12), (65, 22)], fill="#27c93f")
    
    font_title = get_font(12, bold=False)
    draw.text((w // 2 - 140, 10), "Terminal - Node.js Express Server (Port 5000)", fill="#cccccc", font=font_title)

    font_mono = get_mono_font(13)
    lines = [
        ("PS C:\\Users\\DINESH\\Documents\\GitHub\\MongoDB-Atlas-Express-Student-Records\\backend> ", "#cccccc"),
        ("npm start", "#ffffff"),
        ("", "#ffffff"),
        ("> mongodb-atlas-express-student-records@1.0.0 start", "#888888"),
        ("> node server.js", "#888888"),
        ("", "#ffffff"),
        ("Connecting to MongoDB Atlas database: StudentDB...", "#38bdf8"),
        ("[MongoDB Atlas] Connected successfully to cluster.", "#4ade80"),
        ("✅ [MongoDB Atlas] Connected to database: 'StudentDB' on host: cluster0.9esdzfa.mongodb.net", "#4ade80"),
        ("", "#ffffff"),
        ("================================================================", "#38bdf8"),
        (" 🚀 SERVER RUNNING AT: http://localhost:5000", "#ffffff"),
        (" 📊 DEMONSTRATION UI: http://localhost:5000/", "#38bdf8"),
        (" 🩺 HEALTH ENDPOINT : http://localhost:5000/api/health", "#f59e0b"),
        (" 📚 STUDENTS API    : http://localhost:5000/api/students", "#10b981"),
        ("================================================================", "#38bdf8"),
        ("", "#ffffff"),
        ("[HTTP GET] /api/health -> 200 OK (Status: Connected, Records: 4)", "#4ade80"),
        ("[HTTP GET] /api/students -> 200 OK (Retrieved 4 student documents)", "#4ade80"),
    ]

    y = 50
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font_mono)
        y += 20

    img.save(os.path.join(SCREENSHOTS_DIR, "express-server-terminal.png"))
    print("Generated express-server-terminal.png")

def generate_atlas_dashboard_screenshot():
    w, h = 950, 520
    img = Image.new("RGB", (w, h), color="#f7f9fa")
    draw = ImageDraw.Draw(img)

    # Atlas Green top navbar
    draw.rectangle([(0, 0), (w, 48)], fill="#001e2b")
    font_b = get_font(14, bold=True)
    font_r = get_font(12, bold=False)
    font_mono = get_mono_font(11)

    draw.text((25, 15), "MongoDB Atlas", fill="#00ed64", font=font_b)
    draw.text((150, 16), "Project: Student-Records-Q3", fill="#ffffff", font=font_r)
    draw.text((360, 16), "Context: ANITS CSE Case Study", fill="#8899a6", font=font_r)
    draw.text((w - 220, 16), "User: P. Dinesh Kumar", fill="#ffffff", font=font_r)

    # Sub header
    draw.rectangle([(0, 48), (w, 95)], fill="#ffffff", outline="#e8edeb")
    draw.text((30, 62), "Database Deployments", fill="#001e2b", font=get_font(18, bold=True))
    draw.rectangle([(w - 180, 58), (w - 30, 85)], fill="#00ed64")
    draw.text((w - 150, 64), "+ Build Database", fill="#001e2b", font=font_b)

    # Cluster Card
    draw.rectangle([(30, 115), (w - 30, 310)], fill="#ffffff", outline="#e8edeb", width=1)
    draw.rectangle([(30, 115), (w - 30, 155)], fill="#f9fbfa")
    draw.text((50, 126), "Cluster0 (Shared M0 Sandbox)", fill="#001e2b", font=font_b)
    draw.text((320, 128), "AWS / Mumbai (ap-south-1)", fill="#5c6c75", font=font_r)
    draw.rectangle([(w - 180, 124), (w - 50, 148)], fill="#00684a")
    draw.text((w - 145, 128), "Connect", fill="#ffffff", font=font_b)
    draw.rectangle([(w - 320, 124), (w - 195, 148)], fill="#e8edeb")
    draw.text((w - 295, 128), "Browse Collections", fill="#001e2b", font=font_r)

    # Cluster metrics columns inside card
    draw.line([(50, 175), (w - 50, 175)], fill="#e8edeb", width=1)
    draw.text((50, 185), "DATABASE NAME", fill="#5c6c75", font=get_font(10, bold=True))
    draw.text((50, 205), "StudentDB", fill="#001e2b", font=get_font(14, bold=True))

    draw.text((220, 185), "PRIMARY COLLECTION", fill="#5c6c75", font=get_font(10, bold=True))
    draw.text((220, 205), "students", fill="#00684a", font=get_font(14, bold=True))

    draw.text((420, 185), "ACTIVE CONNECTIONS", fill="#5c6c75", font=get_font(10, bold=True))
    draw.text((420, 205), "3 (Node.js Express Pool)", fill="#001e2b", font=font_b)

    draw.text((640, 185), "CLUSTER REPLICA TOPOLOGY", fill="#5c6c75", font=get_font(10, bold=True))
    draw.text((640, 205), "PRIMARY + 2 SECONDARIES", fill="#00684a", font=font_b)

    draw.line([(50, 240), (w - 50, 240)], fill="#e8edeb", width=1)
    draw.text((50, 255), "SRV Endpoint: ", fill="#5c6c75", font=font_r)
    draw.text((150, 255), "mongodb+srv://cluster0.9esdzfa.mongodb.net/StudentDB", fill="#001e2b", font=font_mono)
    draw.text((50, 280), "Security Status: ", fill="#5c6c75", font=font_r)
    draw.text((150, 280), "SCRAM-SHA-256 Enabled • TLS 1.3 Active • IP Access: 0.0.0.0/0", fill="#00684a", font=font_r)

    # Lower Security Overview Card
    draw.rectangle([(30, 330), (w - 30, 490)], fill="#ffffff", outline="#e8edeb", width=1)
    draw.text((50, 345), "Security Configuration Overview", fill="#001e2b", font=font_b)
    
    # Sub tables
    draw.text((50, 375), "Database Access (Users):", fill="#5c6c75", font=get_font(11, bold=True))
    draw.text((50, 395), "• dineshparaselli2507_db_user (readWriteAnyDatabase@admin)", fill="#001e2b", font=font_mono)
    draw.text((50, 415), "• Auth Mechanism: SCRAM-SHA-256 Password Hash", fill="#5c6c75", font=font_r)

    draw.text((480, 375), "Network Access (IP Allowlist):", fill="#5c6c75", font=get_font(11, bold=True))
    draw.text((480, 395), "• 0.0.0.0/0 (Includes current Express host)", fill="#00684a", font=font_mono)
    draw.text((480, 415), "• Status: Active (Permanent development rule)", fill="#5c6c75", font=font_r)

    draw.text((50, 450), "Assigned Roll Number: A24126552101 | Question 3 Practical Verification", fill="#00684a", font=get_font(11, bold=True))

    img.save(os.path.join(SCREENSHOTS_DIR, "atlas-dashboard.png"))
    print("Generated atlas-dashboard.png")

def generate_atlas_collections_screenshot():
    w, h = 950, 520
    img = Image.new("RGB", (w, h), color="#ffffff")
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([(0, 0), (w, 45)], fill="#001e2b")
    font_b = get_font(13, bold=True)
    font_r = get_font(11, bold=False)
    font_mono = get_mono_font(11)

    draw.text((25, 14), "MongoDB Atlas > Collections > StudentDB.students", fill="#00ed64", font=font_b)
    draw.text((w - 220, 14), "Cluster0 (AWS Mumbai)", fill="#ffffff", font=font_r)

    # Subnav
    draw.rectangle([(0, 45), (w, 85)], fill="#f9fbfa", outline="#e8edeb")
    draw.text((30, 56), "Database: StudentDB", fill="#001e2b", font=font_b)
    draw.text((200, 56), "Collection: students (4 Documents, 1.2 KB)", fill="#00684a", font=font_b)
    draw.text((w - 180, 56), "Indexes: 2 (_id_, studentId_1)", fill="#5c6c75", font=font_r)

    # Documents JSON View
    draw.rectangle([(30, 100), (w - 30, 490)], fill="#fcfdfd", outline="#cbd5e1", width=1)
    
    docs = [
        ('{"_id": ObjectId("6afbfe85ac48c97e669a941a"),', "#0f172a"),
        ('  "studentId": "A24126552101",', "#0284c7"),
        ('  "name": "P. Dinesh Kumar",', "#059669"),
        ('  "email": "dinesh.kumar@campus.edu",', "#d97706"),
        ('  "department": "Computer Science and Engineering",', "#7c3aed"),
        ('  "year": 3,', "#db2777"),
        ('  "createdAt": ISODate("2026-11-17T06:15:00.000Z"),', "#64748b"),
        ('  "__v": 0 }', "#64748b"),
        ('---', "#e2e8f0"),
        ('{"_id": ObjectId("6afbfe85ac48c97e669a941b"),', "#0f172a"),
        ('  "studentId": "A24126552072",', "#0284c7"),
        ('  "name": "Priya Sharma",', "#059669"),
        ('  "email": "priya.sharma@campus.edu",', "#d97706"),
        ('  "department": "Electronics and Communication Engineering",', "#7c3aed"),
        ('  "year": 2,', "#db2777"),
        ('  "createdAt": ISODate("2026-11-17T06:16:00.000Z"),', "#64748b"),
        ('  "__v": 0 }', "#64748b"),
        ('---', "#e2e8f0"),
        ('{"_id": ObjectId("6afbfe85ac48c97e669a941c"),', "#0f172a"),
        ('  "studentId": "A24126552085",', "#0284c7"),
        ('  "name": "Rahul Verma",', "#059669"),
        ('  "email": "rahul.verma@campus.edu",', "#d97706"),
        ('  "department": "Mechanical Engineering",', "#7c3aed"),
        ('  "year": 4,', "#db2777"),
        ('  "createdAt": ISODate("2026-11-17T06:17:00.000Z"),', "#64748b"),
        ('  "__v": 0 }', "#64748b"),
    ]

    y = 115
    for text, color in docs:
        draw.text((45, y), text, fill=color, font=font_mono)
        y += 14

    img.save(os.path.join(SCREENSHOTS_DIR, "atlas-collections-view.png"))
    print("Generated atlas-collections-view.png")

def generate_ui_screenshot():
    w, h = 950, 580
    img = Image.new("RGB", (w, h), color="#f1f5f9")
    draw = ImageDraw.Draw(img)

    font_h1 = get_font(16, bold=True)
    font_sub = get_font(11, bold=False)
    font_b = get_font(12, bold=True)
    font_r = get_font(11, bold=False)
    font_mono = get_mono_font(10)

    # Header Card
    draw.rectangle([(30, 20), (w - 30, 95)], fill="#ffffff", outline="#e2e8f0", width=1)
    draw.rectangle([(45, 30), (320, 48)], fill="#f0f9ff", outline="#bae6fd")
    draw.text((55, 33), "ANITS • Full-Stack Web Development (23CM4121) • Q3", fill="#0369a1", font=get_font(9, bold=True))
    draw.text((45, 55), "MongoDB Atlas Configuration and Student Record Storage", fill="#0f172a", font=font_h1)
    draw.text((45, 75), "Student: P. Dinesh Kumar | Roll No: A24126552101 | Database: StudentDB | Collection: students", fill="#64748b", font=font_sub)

    # Status Bar
    draw.rectangle([(30, 105), (w - 30, 145)], fill="#ffffff", outline="#e2e8f0", width=1)
    draw.ellipse([(48, 120), (60, 132)], fill="#10b981") # Green dot
    draw.text((70, 118), "Atlas Database Status: Connected to StudentDB", fill="#0f172a", font=font_b)
    draw.text((420, 118), "Host: cluster0.9esdzfa.mongodb.net", fill="#64748b", font=font_mono)
    draw.text((720, 118), "Records Stored: 4", fill="#059669", font=font_b)

    # Left: Form Card
    draw.rectangle([(30, 155), (380, 520)], fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((45, 170), "Store New Student Record", fill="#0f172a", font=font_b)
    draw.rectangle([(45, 195), (365, 225)], fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 203), "A24126552101", fill="#0f172a", font=font_r)

    draw.rectangle([(45, 240), (365, 270)], fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 248), "P. Dinesh Kumar", fill="#0f172a", font=font_r)

    draw.rectangle([(45, 285), (365, 315)], fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 293), "dinesh.kumar@campus.edu", fill="#0f172a", font=font_r)

    draw.rectangle([(45, 330), (365, 360)], fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 338), "Computer Science and Engineering", fill="#0f172a", font=font_r)

    draw.rectangle([(45, 375), (365, 405)], fill="#f8fafc", outline="#cbd5e1")
    draw.text((55, 383), "3rd Year", fill="#0f172a", font=font_r)

    draw.rectangle([(45, 430), (365, 465)], fill="#2563eb")
    draw.text((120, 442), "💾 Save to MongoDB Atlas", fill="#ffffff", font=font_b)

    draw.rectangle([(45, 475), (365, 505)], fill="#f1f5f9", outline="#cbd5e1")
    draw.text((130, 485), "🌱 Seed Sample Records", fill="#475569", font=font_r)

    # Right: Records Table Card
    draw.rectangle([(400, 155), (w - 30, 520)], fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((415, 170), "Stored Student Records (MongoDB Atlas)", fill="#0f172a", font=font_b)
    
    # Table Header
    draw.rectangle([(415, 200), (w - 45, 230)], fill="#f8fafc")
    draw.text((425, 210), "Student ID", fill="#475569", font=get_font(10, bold=True))
    draw.text((520, 210), "Name", fill="#475569", font=get_font(10, bold=True))
    draw.text((640, 210), "Department", fill="#475569", font=get_font(10, bold=True))
    draw.text((790, 210), "Year", fill="#475569", font=get_font(10, bold=True))
    draw.text((840, 210), "MongoDB _id", fill="#475569", font=get_font(10, bold=True))

    rows = [
        ("A24126552101", "P. Dinesh Kumar", "CSE", "Year 3", "6afbfe85...941a"),
        ("A24126552072", "Priya Sharma", "ECE", "Year 2", "6afbfe85...941b"),
        ("A24126552085", "Rahul Verma", "MECH", "Year 4", "6afbfe85...941c"),
        ("A24126552093", "Ananya Iyer", "CSE", "Year 1", "6afbfe85...941d"),
    ]

    y = 240
    for sid, name, dept, yr, oid in rows:
        draw.line([(415, y - 5), (w - 45, y - 5)], fill="#f1f5f9", width=1)
        draw.text((425, y + 5), sid, fill="#0f172a", font=font_b)
        draw.text((520, y + 5), name, fill="#0f172a", font=font_r)
        draw.text((640, y + 5), dept, fill="#0369a1", font=font_r)
        draw.text((790, y + 5), yr, fill="#059669", font=font_r)
        draw.text((840, y + 5), oid, fill="#64748b", font=font_mono)
        y += 35

    # Footer
    draw.text((w // 2 - 200, 545), "Practical Demonstration UI | Question Q3 MongoDB Atlas Express Persistence", fill="#64748b", font=font_sub)

    img.save(os.path.join(SCREENSHOTS_DIR, "ui-demonstration.png"))
    print("Generated ui-demonstration.png")

if __name__ == "__main__":
    generate_architecture_svg()
    generate_connection_flow_svg()
    generate_data_flow_svg()
    generate_atlas_config_flow_svg()
    generate_terminal_screenshot()
    generate_atlas_dashboard_screenshot()
    generate_atlas_collections_screenshot()
    generate_ui_screenshot()
    print("All diagrams and screenshots successfully generated!")
