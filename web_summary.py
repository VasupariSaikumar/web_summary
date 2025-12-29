import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# 1. BRAIN: Function to talk to your Local LLM
def get_llm_response(prompt):
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    
    response = client.chat.completions.create(
        model="llama3.2:latest", # Or llama3, depending on what you have
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 2. SCRAPER: Function to get data from a website
def get_website_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Get the title (h1) and all text (p)
    title = soup.find("h1").text if soup.find("h1") else "No Title Found"
    paragraphs = soup.find_all("p")
    content = "\n".join([p.text for p in paragraphs])
    
    return title, content

# 3. MAIN EXECUTION: Connecting the dots
def main():
    target_url = "https://books.toscrape.com/"
    print(f"Scraping {target_url}...")
    
    # Step A: Get the raw data
    title, body = get_website_info(target_url)
    
    # Step B: Create the "Final Prompt" (The Instruction + Data)
    final_prompt = f"""
    You are a professional marketing assistant. 
    Using the following website content, create a short, professional brochure.
    
    Website Title: {title}
    Website Content: {body}
    
    Brochure Output:
    """
    
    # Step C: Send it to the Brain
    print("Generating brochure with AI...")
    brochure = get_llm_response(final_prompt)
    
    # Step D: See the result
    print("-" * 30)
    print(brochure)

if __name__ == "__main__":
    main()