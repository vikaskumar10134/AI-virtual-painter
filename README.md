Touch-Based Dual-Brush Drawing App

<sub>A multi-touch drawing system with two brushes and gesture-based tool selection.</sub>

🔥 Key Features
<table> <tr> <td width="150"><b><span style="color:#ff4da6">Pink Brush</span></b></td> <td>Soft-highlight stroke for markup and emphasis.</td> </tr> <tr> <td><b><span style="color:#4d79ff">Blue Brush</span></b></td> <td>Primary drawing stroke for lines and shapes.</td> </tr> <tr> <td><b>Eraser</b></td> <td>Clears strokes using background overwrite.</td> </tr> <tr> <td><b>Two Modes</b></td> <td> <b>Selection Mode</b> via <i>two fingers</i><br> <b>Draw Mode</b> via <i>one finger</i> </td> </tr> </table>
🎨 Tools Overview (With Color Highlights)
1. Pink Brush

<span style="background-color:#ffe6f2; padding:4px; border-radius:4px;">Color: #FF66CC</span>
Used for highlighting or soft strokes.
Low opacity and smoother blending.

2. Blue Brush

<span style="background-color:#e6ecff; padding:4px; border-radius:4px;">Color: #3366FF</span>
Used for primary drawing, solid outlines, handwriting.

3. Eraser

<span style="background-color:#f2f2f2; padding:4px; border-radius:4px;">Removes existing strokes by overwriting pixels.</span>

🧭 Modes of Interaction (Color-Coded Explanation)
Mode 1 — Selection Mode

<span style="color:#ff9900"><b>Activated using TWO fingers</b></span>

What happens here:

App enters selection mode

Displays selectable tools

User picks:

<span style="color:#ff4da6"><b>Pink Brush</b></span>

<span style="color:#4d79ff"><b>Blue Brush</b></span>

<span style="color:#222"><b>Eraser</b></span>

Internal Condition:

if touchCount == 2:
    mode = "SELECTION"

Mode 2 — Draw Mode

<span style="color:#00aa00"><b>Activated using ONE finger</b></span>

What happens here:

After selecting a tool, move one finger to draw

The system renders strokes based on the active tool

Internal Condition:

if touchCount == 1 and mode == "DRAW":
    drawStroke(currentTool, touchCoordinates)

🔧 Working Architecture (Color Highlighted Diagram)
+------------------------+
|       Touch Input      |
+-----------+------------+
            |
            v
+------------------------+        +----------------------------------+
|  Gesture Detector      | -----> | Selection Mode Handler (2-finger)|
+------------------------+        +----------------------------------+
            |
            v
+------------------------+        +----------------------------------+
|   Draw Mode Engine     | <----- | Active Tool: Pink / Blue / Eraser|
+------------------------+        +----------------------------------+
            |
            v
+------------------------+
|     Canvas Renderer    |
+------------------------+

📂 Folder Structure
/project-root
│
├── src/
│   ├── app.js
│   ├── gestures.js
│   ├── drawEngine.js
│   ├── canvas.js
│   └── styles.css
│
├── assets/
│   └── icons/
│
└── README.md

🚀 User Flow (With Color Emphasis)
START
  |
  +--> TWO fingers →  [Selection Mode Activated]
  |          |
  |          +--> Choose Tool:
  |                 • Pink Brush
  |                 • Blue Brush
  |                 • Eraser
  |
  +--> ONE finger →  [Draw Mode Activated]
             |
             +--> Draw with selected tool
  |
 END

📌 Future Enhancements

Add brush size slider

Pressure sensitivity support

Undo / redo buffer

Save canvas to PNG

Zoom & pan gestures

Multi-stroke smoothing
