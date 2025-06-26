# ⚔🪖 DefenseTechAI – Modern Defense Equipment MCP Server

DefenseTechAI is an intelligent Model Context Protocol (MCP) server designed to provide technical information and categorization for modern defense equipment and technologies. It offers instant access to a curated local database of weapons, as well as dynamic integration with Wikipedia for broader coverage.

---

## 🚀 Features

- **Comprehensive Weapon Database**  
  Query technical details (type, origin, range, speed, usage) for a variety of defense weapons and equipment.

- **Category-Based Resource Access**  
  Retrieve lists of equipment grouped by type (missile, drone, tank, radar, etc.).

- **Wikipedia Integration**  
  If a weapon is not found locally, the server fetches a summary and reference link from Wikipedia.

- **Extensible MCP Tools & Resources**  
  Easily add new tools or resources for custom defense tech queries.

---

## 🏗️ How It Works

- **/tool/tech_info**: Get detailed info about a specific weapon by name.
- **/resource/equipment://{category}**: List all equipment in a given category.
 Unlike large language models (LLMs) that depend on constant internet connectivity, your MCP server runs locally, giving you a critical edge in defense-related environments where security and reliability are non-negotiable.


---

## 🛠️ Getting Started

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MCPSERVER
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or, if requirements.txt is not present:
   pip install mcp-server wikipedia
   ```
3. **Run the server**
   ```bash
   python main.py
   ```

---

## 📚 Example Usage

- **Get weapon info:**
  - Query: `tech_info(weapon="BrahMos")`
  - Response: `{source: "local", weapon: "BrahMos", ...}`
- **Get equipment by category:**
  - Query: `equipment://missile`
  - Response: `{category: "missile", items: ["BrahMos", "Agni-V"]}`

---

## 🤖 Powered By
- [mcp-server](https://pypi.org/project/mcp-server/)
- [Wikipedia Python API](https://pypi.org/project/wikipedia/)

---

⚔🪖**DefenseTechAI** – In places where the internet is a liability, your MCP becomes a secure, reliable, AI-powered assistant that works anytime, anywhere — even behind firewalls, in bunkers, or inside submarines.


