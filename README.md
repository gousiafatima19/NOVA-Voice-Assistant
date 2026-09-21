# NOVA — Personalized AI Voice Assistant

> **Your Voice. Your Tasks. A Smarter Way.**

NOVA is a personalized AI-powered voice assistant designed to make everyday tasks and computer interaction simpler, faster, and more convenient.

Users can communicate with NOVA using natural voice or text commands to manage reminders, notes, shopping lists, expenses, study plans, goals, and other everyday tasks. NOVA can also perform selected computer actions through a controlled local desktop agent.

---

## 🌐 Live Demo

🚀  NOVA :
**https://nova-voice-assistant-three.vercel.app**
## 🌟 About NOVA

In today's busy world, people manage many things at the same time — classes, meetings, assignments, deadlines, shopping, personal tasks, and goals. Because of these busy schedules, it is easy to forget small but important tasks.

NOVA brings several everyday functions together through one personalized assistant.

For example, a user can simply say:

> **"NOVA, remind me to attend my meeting at 4 PM."**

> **"Save a note that I need to submit the project report."**

> **"Add milk to my shopping list."**

For supported computer actions, a user can also say:

> **"Open Calculator."**

> **"Take a screenshot."**

The main idea behind NOVA is simple:

**Instead of remembering everything and manually opening different applications, users can simply tell NOVA what they need.**

---

# ✨ Features

### 🎙️ Voice Interaction
Interact with NOVA using natural voice commands.

### 💬 Text Interaction
Communicate with NOVA through text commands.

### 📝 Notes
Create and manage personal notes.

### ⏰ Reminders
Create reminders for meetings, assignments, deadlines, and other important tasks.

### 🛒 Shopping Lists
Add and manage shopping items using natural commands.

### 💰 Expense Management
Record and manage personal expenses.

### 📚 Study Plans
Organize study-related activities and plans.

### 🎯 Goals
Create and manage personal goals.

### 👤 User Accounts
Maintain separate user accounts and personalized data.

### 💭 Chat History
Maintain relevant interaction history.

### 💻 Computer Actions
Perform selected computer actions through the NOVA local desktop agent.

Supported actions may include:

- Opening applications
- Opening folders
- Taking screenshots
- Muting the system
- Other predefined actions

### 🔐 Controlled Device Access
Computer actions are restricted using an allowlist so that only predefined actions can be executed.

### 🤖 AI-Powered Understanding
Process natural-language commands, identify user intent, and route requests to the appropriate functionality.

---

# 🏗️ System Architecture

NOVA follows a **hybrid cloud + local architecture**.

```text
                         ┌─────────────────────┐
                         │        USER         │
                         │   Voice / Text      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌─────────────────────────────┐
                    │       FRONTEND CLIENT       │
                    │   HTML • CSS • JavaScript   │
                    │        Voice Interface      │
                    │           Vercel            │
                    └──────────────┬──────────────┘
                                   │
                              HTTPS / JSON
                                   │
                                   ▼
                    ┌─────────────────────────────┐
                    │        FLASK BACKEND        │
                    │            Render            │
                    │ Authentication • Tasks       │
                    │ Notes • Reminders • Goals    │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
                    ▼                             ▼
          ┌──────────────────┐          ┌────────────────────┐
          │     SUPABASE     │          │   AI BRIDGE &      │
          │   PostgreSQL     │          │       BRAIN        │
          │    + pgvector    │          │   Groq + GPT-OSS   │
          └──────────────────┘          └─────────┬──────────┘
                                                  │
                                           Tool / Action
                                              Routing
                                                  │
                                                  ▼
                                      ┌────────────────────┐
                                      │     NOVA AGENT     │
                                      │    User's Laptop   │
                                      │ Python • Flask     │
                                      │     PyAutoGUI      │
                                      └─────────┬──────────┘
                                                │
                                                ▼
                                      Approved Computer
                                           Actions
🔄 How NOVA Works
The overall workflow is:
User
  ↓
Voice / Text Input
  ↓
Frontend
  ↓
Flask Backend
  ↓
AI Bridge & Brain
  ↓
Intent Detection
  ↓
 ┌───────────────────────┐
 │                       │
 ▼                       ▼
Database Task        Device Action
 │                       │
 ▼                       ▼
Supabase              NOVA Agent
 │                       │
 └───────────┬───────────┘
             ▼
        Result / Response
             ↓
            User
Example 1 — Creating a Reminder
"Remind me to study at 7 PM."
              ↓
          Frontend
              ↓
        Flask Backend
              ↓
         AI Processing
              ↓
       Intent: Reminder
              ↓
          Supabase
              ↓
       Reminder Stored
              ↓
       Response to User
Example 2 — Opening Calculator
"Open Calculator."
        ↓
    Frontend
        ↓
 Flask Backend
        ↓
  AI Processing
        ↓
 Intent: OPEN_APP
        ↓
   NOVA Agent
        ↓
 Allowlist Check
        ↓
    PyAutoGUI
        ↓
 Calculator Opens
🧠 AI Layer
The AI layer acts as the intelligence behind NOVA.
It processes natural-language requests, identifies user intent, and determines the appropriate functionality or action.
AI Components
- Groq — AI inference platform
- GPT-OSS — AI model used by the NOVA Brain
- Intent Detection — Identifies what the user wants
- Tool Routing — Routes requests to the appropriate functionality
- Gemini API — Used for AI/embedding-related functionality
Example
User Command	Intent	Action
"Remind me to study at 7"	Reminder	Create reminder
"Save this note"	Note	Save note
"Add milk"	Shopping	Add shopping item
"Open Calculator"	Device Action	Open application
"Take a screenshot"	Device Action	Capture screenshot


💻 NOVA Local Agent
The NOVA Agent is a local application that runs on the user's computer.
It allows NOVA to perform selected computer actions while keeping device access controlled.
Technologies
- Python
- Flask
- PyAutoGUI
- Windows executable
The local agent communicates with the NOVA system and performs approved actions on the user's computer.
🔐 Security
Since NOVA can interact with the user's computer, controlled execution is an important part of the system.
NOVA uses an allowlist-based approach for device actions.
Only predefined actions are permitted.
Example actions include:
OPEN_APP
TAKE_SCREENSHOT
OPEN_FOLDER
MUTE
This prevents the local agent from accepting arbitrary computer commands.
Additional security considerations include:
- User authentication
- User-specific data
- Restricted device actions
- Controlled backend-to-agent communication
- HTTPS communication
- Environment variables for sensitive credentials
Never upload API keys, passwords, tokens, or other secrets to GitHub.

🛠️ Technology Stack
Technology	Purpose
HTML5	Frontend structure
CSS3	Styling and layout
JavaScript	Frontend functionality
voice.js	Voice interaction
Python	Backend and local agent
Flask	Backend and local agent server
Vercel	Frontend deployment
Render	Backend / service deployment
Supabase	Database platform
PostgreSQL	Structured data storage
pgvector	Vector embeddings and semantic search
Groq	AI inference
GPT-OSS	AI model
Gemini API	AI / embedding-related functionality
Resend	Email service
PyAutoGUI	Computer automation
HTTPS	Secure communication
JSON	Data exchange


📁 Project Structure
NOVA/
│
├── ai/
│   ├── agent.py
│   ├── brain.py
│   ├── bridge.py
│   ├── requirements.txt
│   └── dist/
│       └── NovaAgent.exe
│
├── backend/
│   └── database/
│       ├── app.py
│       ├── database.py
│       ├── migrate_note_embeddings.py
│       └── requirements.txt
│
├── assets/
│   └── images/
│       └── nova-logo.svg
│
├── css/
│   ├── auth.css
│   ├── components.css
│   ├── dashboard.css
│   ├── style.css
│   └── theme.css
│
├── js/
│   ├── api.js
│   ├── auth.js
│   ├── dashboard.js
│   ├── expenses.js
│   ├── file-summarizer.js
│   ├── goals.js
│   ├── main.js
│   ├── notes.js
│   ├── reminders.js
│   ├── shopping.js
│   ├── study_plans.js
│   ├── theme.js
│   └── voice.js
│
├── index.html
├── login.html
├── register.html
├── dashboard.html
├── assistant.html
├── notes.html
├── reminders.html
├── shopping.html
├── expenses.html
├── goals.html
├── study_plans.html
├── profile.html
└── download-agent.html
⚙️ Installation & Setup
Prerequisites
Before running NOVA locally, make sure you have:
- Python 3.x
- Git
- A modern web browser
- Required API credentials
- Supabase configuration
- Required Python dependencies
1. Clone the Repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd NOVA
2. Install AI Dependencies
cd ai
pip install -r requirements.txt
Configure the required environment variables.
Example:
GROQ_API_KEY=your_api_key
3. Install Backend Dependencies
cd ../backend/database
pip install -r requirements.txt
Configure the required database and service environment variables.
4. Run the Frontend
The frontend can be served locally using a development server such as Live Server in VS Code.
5. Run the Local Agent
The NOVA Agent runs locally on the user's Windows computer and handles supported computer actions.
☁️ Deployment
NOVA uses separate services for different parts of the application.
Frontend
   ↓
Vercel
   ↓
Flask Backend
   ↓
Render
   ↓
Supabase Database
   +
AI Bridge / Brain
   ↓
Groq + GPT-OSS
   ↓
NOVA Local Agent
   ↓
User's Computer
The hybrid architecture combines:
- Cloud-based processing
- Persistent data storage
- AI capabilities
- Local computer interaction
🎯 Project Objectives
The main objectives of NOVA are to:
- Make everyday computer interaction easier
- Provide natural voice and text interaction
- Help users manage daily tasks from one assistant
- Reduce the need to switch between multiple applications
- Provide personalized user accounts and data
- Connect natural-language commands with useful actions
- Enable controlled computer automation
- Provide secure and restricted device interaction
🌍 Target Users
🎓 Students
Manage study plans, reminders, notes, and goals.
👩‍💼 Office Workers
Manage meetings, reminders, notes, and everyday work tasks.
👨‍👩‍👧 Everyday Users
Manage shopping lists, expenses, reminders, and personal tasks.
👴 Older Users
Voice-based interaction can make simple computer tasks easier by reducing the need to navigate through multiple menus.
💡 Why NOVA?
Many everyday tasks require users to open different applications and manually enter information.
NOVA brings several of these functions together through a single personalized assistant.
For example:
"NOVA, remind me about my meeting at 4 PM, save a note to send the report, and add milk to my shopping list."

Instead of manually opening several applications, the user can communicate naturally with one assistant.
NOVA focuses on connecting:
AI Understanding + Personalized Tasks + Controlled Computer Actions
🚀 Future Scope
Future improvements may include:
- 📧 Email integration
- 📅 Calendar synchronization
- 📱 Mobile application
- 🎙️ Wake-word activation
- 🔄 Multi-device support
- 🧠 Deeper personalization
- 📴 Improved offline capabilities
- 🔌 Additional integrations
- 🏢 Enterprise version
- 🔄 Automatic agent updates
👥 Team
NOVA — Personalized AI Voice Assistant
Developed by:
- Fokaiha Areeb
- Gousia Fatima
- Firdous Fathima
- Hurriya Zareen
📌 Project Status
Status: Active Development
NOVA is an AI assistant project focused on natural-language interaction, everyday task management, personalized user experiences, and controlled desktop automation.
📄 License
This project is licensed under the MIT License.
The MIT License permits use, copying, modification, merging, publishing, distribution, sublicensing, and selling of copies of the software, subject to the conditions of the license.
See the LICENSE file for the complete license text.
🙏 Acknowledgements
We acknowledge the open-source technologies, frameworks, APIs, and services used in the development of NOVA, including:
- Python
- Flask
- JavaScript
- Supabase
- PostgreSQL
- pgvector
- Vercel
- Render
- Groq
- GPT-OSS
- Gemini API
- Resend
- PyAutoGUI
⭐ Support the Project
If you find NOVA interesting or useful, consider giving the repository a ⭐ on GitHub.
<p align="center">

NOVA
Your Voice. Your Tasks. A Smarter Way.
</p>
```
