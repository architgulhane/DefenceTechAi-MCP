# ⚔🪖 DefenseTechAI – Modern Defense Equipment MCP Server

DefenseTechAI is an intelligent Model Context Protocol (MCP) server designed to provide technical information and categorization for modern defense equipment and technologies. It offers instant access to a curated local database of weapons, as well as dynamic integration with Wikipedia for broader coverage.

---

## 🚀 Features

- **Comprehensive Weapon Database**  
  Query technical details (type, origin, range, speed, usage) for a variety of defense weapons and equipments.

- **Category-Based Resource Access**  
  Retrieve lists of equipment grouped by type (missile, drone, tank, radar, etc.).

- **Wikipedia Integration**  
  If a weapon is not found locally, the server fetches a summary and reference link from Wikipedia.

- **Extensible MCP Tools & Resources**  
  Easily add new tools or resources for custom defense tech queries.
  
  ![Screenshot 2025-06-26 234932](https://github.com/user-attachments/assets/3991a1f3-9707-4412-9548-067713d3b844)

---

## 🏗️ How It Works

- **/tool/tech_info**: Get detailed info about a specific weapon by name.
- **/resource/equipment://{category}**: List all equipment in a given category.
 Unlike large language models (LLMs) that depend on constant internet connectivity, your MCP server runs locally, giving you a critical edge in defense-related environments where security and reliability are non-negotiable.

![WhatsApp Image 2025-06-26 at 23 47 37_0e5bdc5d](https://github.com/user-attachments/assets/45ca92a1-5492-4ba5-b860-ec8c56e8a3c2)

## 📚 Example Usage

- **Get weapon info:**
  - Query: `tech_info(weapon="BrahMos")`
  - Response: `{source: "local", weapon: "BrahMos", ...}`
- **Get equipment by category:**
  - Query: `equipment://missile`
  - Response: `{category: "missile", items: ["BrahMos", "Agni-V"]}`

---

## Caching 
Caching is used in the DefenseTechAI project to make the system faster, more efficient, and usable in restricted or offline environments.

 What Caching Does:

-Stores previously fetched Wikipedia summaries in a local file called cache.json.

-Prevents repeated API calls for the same weapon or topic.

-Ensures quicker response time for frequently asked queries.

-Allows system functionality even without an internet connection.

---

⚔🪖**DefenseTechAI** – In places where the internet is a liability, your MCP becomes a secure, reliable, AI-powered assistant that works anytime, anywhere — even behind firewalls, in bunkers, or inside submarines.


