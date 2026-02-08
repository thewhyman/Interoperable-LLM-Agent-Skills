import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

# Centralized storage to ensure state is shared across Claude, Gemini, and Antigravity
SKILL_DATA_DIR = Path.home() / ".agentskills"
QUEUE_FILE = SKILL_DATA_DIR / "linkedin_post_queue.json"

def ensure_storage():
    """Ensures the centralized storage directory exists."""
    SKILL_DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not QUEUE_FILE.exists():
        with open(QUEUE_FILE, "w") as f:
            json.dump([], f)

def fix_quarantine():
    """Automates macOS security fixes for the skill's scripts."""
    if os.uname().sysname == "Darwin":
        print("🔧 [macOS] Path found. Clearing quarantine attributes...")
        try:
            # Clear quarantine on all .py files in the skill directory
            subprocess.run(["xattr", "-rd", "com.apple.quarantine", str(SKILL_DIR)], 
                           stderr=subprocess.DEVNULL)
            print("✅ Security attributes cleared. Agent should now have full access.")
        except Exception as e:
            print(f"❌ Failed to clear quarantine: {e}")
    else:
        print("ℹ️ Non-macOS system detected. Skipping security attributes fix.")

def load_queue():
    ensure_storage()
    with open(QUEUE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_queue(queue):
    with open(QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=2)

def get_recommended_time():
    """Calculates the next best LinkedIn posting slot with 48h breathing room."""
    now = datetime.now()
    queue = load_queue()
    
    # Find the latest scheduled post to ensure breathing room
    latest_time = now
    for p in queue:
        p_time = datetime.fromisoformat(p["scheduled_at"])
        if p_time > latest_time:
            latest_time = p_time
            
    # Buffer is 48 hours after the latest post (or now)
    buffer_start = latest_time + timedelta(hours=48)
    
    # Recommended slots (Day of week, Hour, Minute)
    slots = [
        (1, 10, 0),  # Tuesday 10:00 AM
        (2, 12, 0),  # Wednesday 12:00 PM
        (3, 9, 0),   # Thursday 09:00 AM
        (0, 14, 0),  # Monday 02:00 PM
    ]
    
    # Look ahead 14 days to find the next available slot after buffer_start
    for i in range(14):
        check_date = buffer_start + timedelta(days=i)
        day_of_week = check_date.weekday()
        
        # Check if today (in loop) has a matching slot
        for slot_day, slot_hour, slot_min in slots:
            if day_of_week == slot_day:
                target = check_date.replace(hour=slot_hour, minute=slot_min, second=0, microsecond=0)
                if target >= buffer_start:
                    return target.isoformat()
    
    return buffer_start.isoformat() # Fallback

def notify(title, message):
    script = f'display notification "{message}" with title "{title}" sound name "Crystal"'
    subprocess.run(["osascript", "-e", script])

def check_queue():
    queue = load_queue()
    now = datetime.now()
    ready_posts = []

    for post in queue:
        if post["status"] == "pending":
            scheduled_at = datetime.fromisoformat(post["scheduled_at"])
            if now >= scheduled_at:
                ready_posts.append(post)

    if ready_posts:
        count = len(ready_posts)
        msg = f"You have {count} LinkedIn post{'s' if count > 1 else ''} ready to ship!"
        notify("Agent Skills", msg)
        print(f"READY: {count} posts found.")
    else:
        print("Empty or no pending posts due yet.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="LinkedIn Post Queue Manager")
    parser.add_argument("command", choices=["check", "list", "mark-posted", "setup", "remove", "recommend"], help="Command to run")
    parser.add_argument("--id", help="Post ID for context (mark-posted, remove)")
    
    args = parser.parse_args()
    
    if args.command == "setup":
        print("🚀 Starting LinkedIn Post Manager Setup...")
        ensure_storage()
        print(f"📂 Centralized queue initialized at: {QUEUE_FILE}")
        fix_quarantine()
        print("✅ Setup complete.")
    elif args.command == "check":
        check_queue()
    elif args.command == "list":
        for p in load_queue():
            print(f"[{p['status'].upper()}] {p['id']} - {p['scheduled_at']}")
    elif args.command == "mark-posted":
        if not args.id:
            print("Error: --id required")
            exit(1)
        q = load_queue()
        for p in q:
            if p["id"] == args.id:
                p["status"] = "posted"
        save_queue(q)
        print(f"Marked {args.id} as posted.")
    elif args.command == "remove":
        if not args.id:
            print("Error: --id required")
            exit(1)
        q = load_queue()
        new_q = [p for p in q if p["id"] != args.id]
        if len(new_q) < len(q):
            save_queue(new_q)
            print(f"✅ Removed post {args.id} from the queue.")
        else:
            print(f"ℹ️ Post {args.id} not found in queue.")
    elif args.command == "recommend":
        print(get_recommended_time())
