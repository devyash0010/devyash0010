from pathlib import Path

OUTPUT = Path("info-card.svg")


def make_info_card():
    svg = r'''<svg xmlns="http://www.w3.org/2000/svg"
width="650"
height="680"
viewBox="0 0 650 680">

<rect
    x="2"
    y="2"
    width="646"
    height="676"
    rx="12"
    fill="white"
    stroke="black"
    stroke-width="2"/>

<!-- Terminal header -->
<rect
    x="2"
    y="2"
    width="646"
    height="38"
    rx="12"
    fill="black"/>

<circle cx="22" cy="21" r="6" fill="white"/>
<circle cx="42" cy="21" r="6" fill="white"/>
<circle cx="62" cy="21" r="6" fill="white"/>

<text
    x="85"
    y="26"
    font-family="monospace"
    font-size="14"
    fill="white">
    devyash@fde-terminal:~
</text>


<!-- Name & Title -->
<text
    x="25"
    y="75"
    font-family="monospace"
    font-size="24"
    font-weight="bold"
    fill="black">
    DEVYASH KULSHRESTHA
</text>

<text
    x="25"
    y="102"
    font-family="monospace"
    font-size="14"
    font-weight="bold"
    fill="#555555">
    Aspiring Forward Deployed Engineer (FDE) | AI &amp; Full-Stack
</text>

<line
    x1="25"
    y1="115"
    x2="625"
    y2="115"
    stroke="black"
    stroke-width="1.5"/>


<!-- FDE Profile / Core Competencies -->

<text x="25" y="145" font-family="monospace" font-size="13" font-weight="bold" fill="black">
&gt;_ PROFILE OVERVIEW
</text>

<text x="25" y="170" font-family="monospace" font-size="13" fill="#333333">
Highly adaptive engineer deploying complex AI, Computer Vision, and Full-Stack
</text>
<text x="25" y="190" font-family="monospace" font-size="13" fill="#333333">
solutions directly into mission-critical environments. Expert in constructing
</text>
<text x="25" y="210" font-family="monospace" font-size="13" fill="#333333">
production-grade data pipelines leveraging hybrid intelligent parsing. Driven by
</text>
<text x="25" y="230" font-family="monospace" font-size="13" fill="#333333">
solving real-world, high-impact client bottlenecks through scalable architecture.
</text>


<!-- Advanced Tech Stack -->

<text x="25" y="275" font-family="monospace" font-size="15" font-weight="bold" fill="black">
🛠️ TECH STACK
</text>

<text x="25" y="305" font-family="monospace" font-size="13" font-weight="bold" fill="#111111">
[AI, ML &amp; NLP Systems]
</text>
<text x="25" y="325" font-family="monospace" font-size="13" fill="#444444">
LLMs • RAG Architectures • LangChain • LangGraph • Rule-Based NLP Layering
</text>

<text x="25" y="355" font-family="monospace" font-size="13" font-weight="bold" fill="#111111">
[Computer Vision &amp; OCR Engine]
</text>
<text x="25" y="375" font-family="monospace" font-size="13" fill="#444444">
YOLO • DeepSeek OCR • Chandra OCR Machine • OpenCV • PaddleOCR • Tesseract
</text>

<text x="25" y="405" font-family="monospace" font-size="13" font-weight="bold" fill="#111111">
[Database Architecture]
</text>
<text x="25" y="425" font-family="monospace" font-size="13" fill="#444444">
PostgreSQL • pgvector • SQLAlchemy • Pandas • NumPy • Vector Search Engines
</text>

<text x="25" y="455" font-family="monospace" font-size="13" font-weight="bold" fill="#111111">
[High-Performance Engineering]
</text>
<text x="25" y="475" font-family="monospace" font-size="13" fill="#444444">
FastAPI • WebSockets (Real-time Streaming) • Flask • Node.js • React • Tailwind CSS
</text>

<text x="25" y="505" font-family="monospace" font-size="13" font-weight="bold" fill="#111111">
[DevOps &amp; Infrastructure]
</text>
<text x="25" y="525" font-family="monospace" font-size="13" fill="#444444">
Docker • Nginx (Reverse Proxy &amp; Routing) • Vercel • Linux • Ollama • Git
</text>

<text x="25" y="555" font-family="monospace" font-size="13" font-weight="bold" fill="#111111">
[Languages]
</text>
<text x="25" y="575" font-family="monospace" font-size="13" fill="#444444">
Python • JavaScript • Java • HTML5 • CSS3
</text>


<line
    x1="25"
    y1="610"
    x2="625"
    y2="610"
    stroke="#dddddd"
    stroke-width="1"/>

<!-- Projects Footer -->
<text x="25" y="640" font-family="monospace" font-size="13" font-weight="bold" fill="black">
⚡ ACTIVE PIPELINES: Coaching AI • Universal Timetable Parser
</text>

</svg>'''

    OUTPUT.write_text(svg, encoding="utf-8")
    print(f"Successfully generated FDE profile card: {OUTPUT}")


if __name__ == "__main__":
    make_info_card()
