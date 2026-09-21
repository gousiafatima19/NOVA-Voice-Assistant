# 🚀 NOVA — Personalized AI Voice Assistant

### *Your Voice. Your Tasks. A Smarter Way.*

NOVA is a personalized AI-powered voice assistant designed to make everyday tasks and computer interaction simpler, faster, and more convenient.

Users can communicate with NOVA using natural **voice or text commands** to manage reminders, notes, shopping lists, expenses, study plans, goals, and other everyday tasks. NOVA also supports selected computer actions through a controlled local desktop agent.

---

## 🌐 Live Demo

### 🚀  NOVA

 **[ NOVA — Live Application](https://nova-voice-assistant-three.vercel.app/)**
# 📖 About the Project

In today's busy world, people manage multiple responsibilities at the same time — classes, assignments, meetings, deadlines, shopping, personal tasks, and goals.

With so many things to remember, small but important tasks can easily be forgotten.

NOVA is designed to act as a **personalized everyday assistant**.

Instead of manually opening different applications, searching through menus, or typing every task separately, users can simply tell NOVA what they need.

For example:

> **"NOVA, remind me to attend my meeting at 4 PM."**

> **"Save a note that I need to submit the project report."**

> **"Add milk to my shopping list."**

For supported computer actions:

> **"Open Calculator."**

> **"Take a screenshot."**

The main idea behind NOVA is simple:

### **Instead of remembering everything and manually performing every small task, users can simply tell NOVA what they need.**

---

# ✨ Key Features

### 🎙️ Voice Interaction
Interact with NOVA using natural voice commands.

### 💬 Text Interaction
Communicate with NOVA through text commands.

### 📝 Notes
Create and manage personal notes.

### ⏰ Reminders
Create reminders for meetings, assignments, deadlines, and important activities.

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
Perform selected computer actions through the NOVA Local Agent.

Supported actions include:

- Opening applications
- Opening folders
- Taking screenshots
- Muting the system
- Other predefined actions

### 🔐 Controlled Device Access
Computer actions are restricted using an allowlist-based mechanism so that only predefined and approved actions can be executed.

### 🤖 AI-Powered Understanding
NOVA processes natural-language commands, identifies the user's intent, and routes the request to the appropriate functionality.

---

# 🏗️ System Architecture

NOVA follows a **hybrid cloud + local architecture**.

<pre>
                         ┌─────────────────────────┐
                         │          USER           │
                         │      Voice / Text       │
                         └────────────┬────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────┐
                    │       1. USER BROWSER           │
                    │                                 │
                    │ Voice Input • Text Input        │
                    │ Notes • Reminders • Shopping    │
                    │ Study Plans • Goals • Account   │
                    └───────────────┬─────────────────┘
                                    │
                               HTTPS / JSON
                                    │
                                    ▼
                    ┌─────────────────────────────────┐
                    │      2. FRONTEND — VERCEL       │
                    │                                 │
                    │ HTML • CSS • JavaScript         │
                    │ Voice Interface • API Calls     │
                    └───────────────┬─────────────────┘
                                    │
                                 REST API
                                    │
                                    ▼
                    ┌─────────────────────────────────┐
                    │       3. BACKEND — RENDER       │
                    │                                 │
                    │ Flask • Authentication          │
                    │ Users • Notes • Reminders       │
                    │ Expenses • Shopping • Goals     │
                    │ Study Plans • Chat History      │
                    └───────────────┬─────────────────┘
                                    │
                     ┌──────────────┴──────────────┐
                     │                             │
                     ▼                             ▼
          ┌──────────────────────┐      ┌────────────────────────┐
          │    4. DATABASE       │      │  5. AI BRIDGE + BRAIN │
          │                      │      │                        │
          │ Supabase             │      │ Groq + GPT-OSS         │
          │ PostgreSQL           │      │ Intent Detection       │
          │ pgvector             │      │ Natural Language       │
          │                      │      │ Tool Routing            │
          └──────────────────────┘      └───────────┬────────────┘
                                                     │
                                                Device Actions
                                                     │
                                                     ▼
                                      ┌──────────────────────────┐
                                      │    6. NOVA LOCAL AGENT   │
                                      │       User's Laptop      │
                                      │                          │
                                      │ Python • Flask           │
                                      │ PyAutoGUI • Windows EXE  │
                                      │ Allowlisted Actions      │
                                      └────────────┬─────────────┘
                                                   │
                                                   ▼
                                      ┌──────────────────────────┐
                                      │     USER'S COMPUTER       │
                                      │                          │
                                      │   Approved Local Actions │
                                      └──────────────────────────┘
</pre>

---

# 🔄 How NOVA Works

The complete workflow is:

**User → Voice/Text → Frontend → Flask Backend → AI Brain → Intent Detection → Database or Local Agent → Result**

### Step-by-step

1. The user gives NOVA a voice or text command.
2. The frontend receives the user's input.
3. The frontend sends the request to the Flask backend.
4. The backend processes the request.
5. The AI Brain understands the user's intention.
6. NOVA determines the required functionality or action.
7. If it is a data-related task, the information is stored or retrieved from Supabase.
8. If it is a supported computer action, the request is sent to the NOVA Local Agent.
9. The Local Agent checks whether the action is allowed.
10. The approved action is performed on the user's computer.
11. NOVA returns the result to the user.

---

# 🧩 Example — Creating a Reminder

### User says:

> **"NOVA, remind me to study at 7 PM."**

### Workflow:

**Voice Input**  
↓  
**Frontend**  
↓  
**Flask Backend**  
↓  
**AI Processing**  
↓  
**Intent: Reminder**  
↓  
**Supabase / PostgreSQL**  
↓  
**Reminder Stored**  
↓  
**Response to User**

---

# 💻 Example — Opening Calculator

### User says:

> **"NOVA, open Calculator."**

### Workflow:

**Voice Input**  
↓  
**Frontend**  
↓  
**Flask Backend**  
↓  
**AI Brain**  
↓  
**Intent: OPEN_APP**  
↓  
**NOVA Local Agent**  
↓  
**Allowlist Check**  
↓  
**PyAutoGUI**  
↓  
**Calculator Opens**

---

# 🧠 AI Layer

The AI layer acts as the intelligence behind NOVA.

It processes natural-language requests, identifies the user's intent, and determines the appropriate functionality or action.

### AI Components

| Component | Purpose |
|---|---|
| **Groq** | AI inference |
| **GPT-OSS** | AI model used by the NOVA Brain |
| **Intent Detection** | Identifies what the user wants |
| **Tool Routing** | Routes requests to the appropriate functionality |
| **Gemini API** | AI / embedding-related functionality |

### Example Intent Mapping

| User Command | Detected Intent | Result |
|---|---|---|
| "Remind me to study at 7" | Reminder | Creates reminder |
| "Save this note" | Note | Saves note |
| "Add milk" | Shopping | Adds shopping item |
| "Open Calculator" | Device Action | Opens application |
| "Take a screenshot" | Device Action | Takes screenshot |

---

# 💻 NOVA Local Agent

The **NOVA Local Agent** is a desktop component that runs on the user's computer.

It acts as a controlled bridge between the NOVA system and the user's computer.

### Technologies Used

- Python
- Flask
- PyAutoGUI
- Windows executable

The Local Agent performs only predefined and approved computer actions.

---

# 🔐 Security

Since NOVA can interact with a user's computer, device control is restricted.

NOVA uses an **allowlist-based security approach**.

Only predefined actions can be executed.

### Example Allowed Actions

`OPEN_APP`

`TAKE_SCREENSHOT`

`OPEN_FOLDER`

`MUTE`

This prevents unrestricted or arbitrary computer commands from being executed.

Additional security considerations include:

- User authentication
- User-specific data
- Restricted device actions
- Controlled agent communication
- HTTPS communication
- Environment variables for sensitive credentials

> **Never commit API keys, passwords, tokens, or other secrets to the repository.**

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **HTML5** | Frontend structure |
| **CSS3** | UI styling and layout |
| **JavaScript** | Frontend functionality |
| **voice.js** | Voice interaction |
| **Python** | Backend and local agent |
| **Flask** | Backend and local server |
| **Vercel** | Frontend deployment |
| **Render** | Backend / service deployment |
| **Supabase** | Database platform |
| **PostgreSQL** | Structured data storage |
| **pgvector** | Vector embeddings and semantic search |
| **Groq** | AI inference |
| **GPT-OSS** | AI model |
| **Gemini API** | AI / embedding-related functionality |
| **Resend** | Email service |
| **PyAutoGUI** | Desktop automation |
| **HTTPS** | Secure communication |
| **JSON** | Data exchange |

---

# 📁 Project Structure

<pre>
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
</pre>

---

# ⚙️ Installation & Setup

## Prerequisites

Before running NOVA locally, install:

- Python 3.x
- Git
- A modern web browser
- Required API credentials
- Supabase configuration
- Required Python dependencies

## 1. Clone the Repository

`git clone PASTE_YOUR_GITHUB_REPOSITORY_LINK_HERE`

`cd NOVA`

## 2. Install AI Dependencies

`cd ai`

`pip install -r requirements.txt`

Configure the required environment variables before running the service.

Example:

`GROQ_API_KEY=your_api_key`

## 3. Install Backend Dependencies

`cd ../backend/database`

`pip install -r requirements.txt`

Configure the required database and service environment variables.

## 4. Run the Frontend

The frontend can be run locally using a development server such as **Live Server** in Visual Studio Code.

## 5. Run the Local Agent

The NOVA Local Agent runs on the user's Windows computer and handles supported local computer actions.

---

# ☁️ Deployment

NOVA uses separate services for different parts of the application.

**Frontend**  
↓  
**Vercel**  
↓  
**Flask Backend**  
↓  
**Render**  
↓  
**Supabase Database + AI Services**  
↓  
**NOVA Local Agent**  
↓  
**User's Computer**

This hybrid architecture combines:

- Cloud-based processing
- Persistent data storage
- AI capabilities
- Personalized user data
- Controlled local computer interaction

---

# 🎯 Project Objectives

The main objectives of NOVA are to:

- Make everyday computer interaction easier
- Provide natural voice and text interaction
- Help users manage daily tasks through one assistant
- Reduce the need to switch between multiple applications
- Provide personalized user accounts and data
- Connect natural-language commands with useful actions
- Enable controlled computer automation
- Maintain restricted and secure device interaction

---

# 🌍 Target Users

### 🎓 Students

Manage study plans, reminders, notes, goals, and academic tasks.

### 👩‍💼 Office Workers

Manage meetings, reminders, notes, deadlines, and everyday work tasks.

### 👨‍👩‍👧 Everyday Users

Manage shopping lists, expenses, reminders, and personal tasks.

### 👴 Older Users

Voice interaction can make simple computer tasks easier by reducing the need to navigate through multiple menus.

---

# 💡 Why NOVA?

Many everyday tasks require users to open different applications and manually enter information.

NOVA brings several of these functions together through one personalized assistant.

For example:

> **"NOVA, remind me about my meeting at 4 PM, save a note to send the report, and add milk to my shopping list."**

Instead of manually opening multiple applications, the user can communicate naturally with NOVA.

NOVA focuses on combining:

### **AI Understanding + Personalized Tasks + Controlled Computer Actions**

---

# 🚀 Future Scope

Possible future enhancements include:

- 📅 Calendar synchronization
- 📱 Mobile application
- 🎙️ Wake-word activation
- 🧠 Deeper personalization
- 📴 Improved offline capabilities
- 🔌 Additional integrations
- 🏢 Enterprise version
- 🔄 Automatic agent updates

# 📌 Project Status

### 🟢 Active Development

NOVA is an AI assistant project focused on natural-language interaction, everyday task management, personalized user experiences, and controlled desktop automation.

---

## 📄 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for the complete license terms.

---

<div align="center">

# NOVA

### *Your Voice. Your Tasks. A Smarter Way.*


</div>
