import os
import sys

# Ensure apps/api is in the Python module search path for Vercel Serverless Functions
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)

candidate_paths = [
    os.path.join(root_dir, "apps", "api"),
    os.path.join(current_dir, "apps", "api"),
    os.path.join(os.getcwd(), "apps", "api"),
    os.path.join(current_dir, "..", "apps", "api"),
]

for p in candidate_paths:
    abs_p = os.path.abspath(p)
    if os.path.isdir(abs_p) and abs_p not in sys.path:
        sys.path.insert(0, abs_p)

from app.main import app

# Vercel Python runtime detects ASGI `app` directly
__all__ = ["app"]
