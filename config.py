import os
import sys
from pathlib import Path

# Paths
BASE_DIR = Path("/root/YT_AlexCarterTrading")
REPO_DIR = BASE_DIR
TRANSCRIPTS_DIR = BASE_DIR / "YT_AlexCarterTrading_Transcript"
CATALOG_FILE = BASE_DIR / "catalog.json"
STATE_FILE = BASE_DIR / "state.json"
WORK_DIR = BASE_DIR / "work"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
LOG_FILE = Path("/var/log/yt_alexcartertrading.log")

# Channel Information
CHANNEL_ID = "UCKUbY0KPIN0KwD8UbmGgRFg"
CHANNEL_NAME = "Alex Carter"
CHANNEL_HANDLE = "@AlexCarterTrading"
CHANNEL_URL = "https://www.youtube.com/@AlexCarterTrading"
RSS_FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
CHANNEL_DOMAIN = "Trading Algorithmique, Agents IA de Trading, Grok Bots, Claude Code, Muse Wonder, Pine Script, TradingView, Scalping, Stratégies Crypto, Automatisation"

# Models
VISUAL_GEMINI_MODEL = "gemini-3.5-flash-lite"
AUDIO_GEMINI_MODEL = "gemini-3.5-flash-lite"
WHISPER_MODEL = "large-v3-turbo"
MODEL_SIGNATURE = f"whisper-v3-large-turbo+{VISUAL_GEMINI_MODEL}"

# API Keys & Network
GEMINI_KEYS_FILE = BASE_DIR / "gemini_keys.txt"
PROXY = "socks5://127.0.0.1:4001"
PLAYER_CLIENT = "android"

# Processing parameters
BATCH_SIZE = 7
MAX_BLOCK_DURATION = 32.0
MIN_BLOCK_DURATION = 18.0
FRAME_DIFF_THRESHOLD = 15.0
FRAME_MAX_WIDTH = 1280

# Ensure directories exist
BASE_DIR.mkdir(parents=True, exist_ok=True)
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
WORK_DIR.mkdir(parents=True, exist_ok=True)