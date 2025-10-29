import asyncio
import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from agents import Runner, trace
from agent import create_agent
from utils import extract_text_from_pdf

load_dotenv()

async def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # -------------------------
    # STEP 1: Read + Upload PDF
    # -------------------------
    pdf_path = "sample.pdf"  # Replace with your static PDF
    print(f"Reading PDF: {pdf_path}\n")
    text = extract_text_from_pdf(pdf_path)

    print("Uploading file to OpenAI...")
    file_upload = client.files.create(
        file=("sample.txt", text.encode("utf-8")),
        purpose="assistants",
    )
    print(f"Uploaded file ID: {file_upload.id}")

    # Wait a moment to avoid 404 (file not fully registered yet)
    time.sleep(3)

    print("Creating vector store...")
    vector_store = client.vector_stores.create(name="pdf-insight-vectors")
    print(f"Vector store ID: {vector_store.id}")

    print("Indexing file into vector store...")
    # ✅ Use the recommended API for batching and polling
    indexed = client.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=[("sample.txt", text.encode("utf-8"))],
    )
    print("Vector store ready.\n")

    # -------------------------
    # STEP 2: Create Agent
    # -------------------------

    agent = create_agent(vector_store.id)

    # -------------------------
    # STEP 3: Run Agent
    # -------------------------
    with trace("Generate PDF Insights"):
        result = await Runner.run(agent, "Summarize the PDF into 5 insights.")

        print("\n### Structured Insights ###\n")
        print(result.final_output.model_dump_json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())
