import sys
import os
from fastmcp import FastMCP
from fastapi import FastAPI

# PATH FIX
current_file = os.path.abspath(__file__)
src_dir = os.path.dirname(current_file)
project_root = os.path.dirname(src_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.tools.jobs import get_public_jobs

# MCP Server
mcp = FastMCP("TuriyaRecruitment")
mcp.add_tool(get_public_jobs)

# Get MCP ASGI app
mcp_app = mcp.http_app()

# ✅ Pass mcp_app.lifespan to FastAPI
app = FastAPI(title="Turiya MCP Server", lifespan=mcp_app.lifespan)

@app.get("/health")
def health():
    return {"status": "ok", "server": "TuriyaRecruitment"}

# Mount MCP app
app.mount("/mcp", mcp_app)

if __name__ == "__main__":
    print("Run with: uvicorn src.main:app --host 0.0.0.0 --port 8002")

# import sys
# import os
# from fastmcp import FastMCP
# from starlette.routing import Mount, Route
# from starlette.applications import Starlette
# from starlette.responses import JSONResponse

# # PATH FIX
# current_file = os.path.abspath(__file__)
# src_dir = os.path.dirname(current_file)
# project_root = os.path.dirname(src_dir)
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

# from src.tools.jobs import get_public_jobs

# # MCP Server
# mcp = FastMCP("TuriyaRecruitment")
# mcp.add_tool(get_public_jobs)

# # Health endpoint
# async def health(request):
#     return JSONResponse({"status": "ok", "server": "TuriyaRecruitment"})

# # Build app: health at /health, MCP at root (exposes /sse, /mcp etc)
# app = Starlette(routes=[
#     Route("/health", health),
#     Mount("/", app=mcp.http_app()),
# ])

# if __name__ == "__main__":
#     print("Run with: uvicorn src.main:app --host 0.0.0.0 --port 8002")

# import sys
# import os
# from fastmcp import FastMCP
# from fastapi import FastAPI

# # PATH FIX
# current_file = os.path.abspath(__file__)
# src_dir = os.path.dirname(current_file)
# project_root = os.path.dirname(src_dir)
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

# from src.tools.jobs import get_public_jobs

# # MCP Server
# mcp = FastMCP("TuriyaRecruitment")
# mcp.add_tool(get_public_jobs)

# # FastAPI app
# app = FastAPI(title="Turiya MCP Server")

# # Health check (optional but useful)
# @app.get("/health")
# def health():
#     return {"status": "ok", "server": "TuriyaRecruitment"}

# # Mount MCP → exposes /mcp/sse and /mcp/messages/
# app.mount("/mcp", mcp.http_app())

# if __name__ == "__main__":
#     print("Run with: uvicorn src.main:app --host 0.0.0.0 --port 8002")

# import sys
# import os
# from fastmcp import FastMCP
# from fastapi import FastAPI

# # PATH FIX (keep)
# current_file = os.path.abspath(__file__)
# src_dir = os.path.dirname(current_file)
# project_root = os.path.dirname(src_dir)
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

# from src.tools.jobs import get_public_jobs

# # MCP Server
# mcp = FastMCP("TuriyaRecruitment")
# mcp.add_tool(get_public_jobs)

# # FastAPI app with MCP mounted
# app = FastAPI(title="Turiya MCP Server")
# app.mount("/mcp", mcp.http_app())

# # NO uvicorn.run() here - systemd handles it
# if __name__ == "__main__":
#     print("Run with: uvicorn src.main:app --host 0.0.0.0 --port 8002 ...")

# import sys
# import os
# from fastmcp import FastMCP
# import uvicorn
# from fastapi import FastAPI

# # --- PATH FIX: Allow imports from project root ---
# # (Keep this block, it is safe and helpful)
# current_file = os.path.abspath(__file__)
# src_dir = os.path.dirname(current_file)
# project_root = os.path.dirname(src_dir)

# if project_root not in sys.path:
#     sys.path.insert(0, project_root)
# # -------------------------------------------------


# from src.tools.jobs import get_public_jobs


# # Initialize Server
# mcp = FastMCP("TuriyaRecruitment")


# # Add Tools
# mcp.add_tool(get_public_jobs)

# # Replace the entire if __name__ block in src/main.py

# if __name__ == "__main__":
#     app = FastAPI(title="Turiya MCP Server")
#     app.mount("/mcp", mcp.http_app())  # MCP protocol at /mcp
    
#     uvicorn.run(
#         "src.main:app",
#         host="0.0.0.0",
#         port=8002,
#         ssl_keyfile="/etc/ssl/certs/STAR.turiyaskills.co/STAR.turiyaskills.co.key",
#         ssl_certfile="/etc/ssl/certs/STAR.turiyaskills.co/STAR.turiyaskills.co.crt",
#         log_level="info",
#         reload=False
#     )


# --- PRODUCTION HTTP SERVER FOR AWS ---
# Runs HTTPS on port 8002, accessible remotely
# MCP endpoint available at /mcp (SSE, tools, calls)
# if __name__ == "__main__":
#     mcp.run(
#         transport="http",
#         host="0.0.0.0",  # Bind to all interfaces (required for AWS)
#         port=8002,       # Your chosen port
        
#         # SSL/TLS for production (matches your certs)
#         ssl_certfile="/etc/ssl/certs/STAR.turiyaskills.co/STAR.turiyaskills.co.crt",
#         ssl_keyfile="/etc/ssl/certs/STAR.turiyaskills.co/STAR.turiyaskills.co.key"
#     )

# import sys
# import os
# from fastmcp import FastMCP

# # --- PATH FIX: Allow imports from project root ---
# # (Keep this block, it is safe and helpful)
# current_file = os.path.abspath(__file__)
# src_dir = os.path.dirname(current_file)
# project_root = os.path.dirname(src_dir)

# if project_root not in sys.path:
#     sys.path.insert(0, project_root)
# # -------------------------------------------------

# from src.tools.jobs import get_public_jobs

# # Initialize Server
# mcp = FastMCP("TuriyaRecruitment")

# # Add Tools
# mcp.add_tool(get_public_jobs)

# # --- CRITICAL CHANGE FOR AWS ---
# # Only run local interactive mode if you run the file manually.
# # When AWS/Uvicorn runs this, it ignores this block and just grabs the 'mcp' object.
# if __name__ == "__main__":
#     mcp.run()

# # from fastmcp import FastMCP
# # from src.tools.jobs import get_public_jobs

# # # 1. Create the MCP Server
# # mcp = FastMCP("TuriyaRecruitment")

# # # 2. Register the tools
# # # We import the function and add it to the server here
# # mcp.add_tool(get_public_jobs)

# # # 3. Run the server
# # if __name__ == "__main__":
# #     mcp.run()
# import sys
# import os

# # --- PATH FIX: Allow imports from project root ---
# # Get the absolute path to 'src/main.py'
# current_file = os.path.abspath(__file__)
# # Get the 'src' directory
# src_dir = os.path.dirname(current_file)
# # Get the project root (one level up)
# project_root = os.path.dirname(src_dir)

# # Add project root to system path so "from src.tools" works
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)
# # -------------------------------------------------

# from fastmcp import FastMCP
# # This import will now work because we added project_root to sys.path
# from src.tools.jobs import get_public_jobs

# # Initialize Server
# mcp = FastMCP("TuriyaRecruitment")

# # Add Tools
# mcp.add_tool(get_public_jobs)

# if __name__ == "__main__":
#     mcp.run()