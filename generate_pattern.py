import os
import sys
import google.generativeai as genai

# Setup Gemini API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_integration_doc(pattern_name):
    # Use Gemini 1.5 Flash for speed and free tier efficiency
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Act as a Senior Solutions Architect. Create a technical Markdown documentation file for the integration pattern: '{pattern_name}'.
    
    Structure the output exactly like this:
    # {pattern_name}
    
    ## Description
    (Provide a deep technical summary)
    
    ## When to Use
    (Bullet points for ideal use cases)
    
    ## When Not to Use
    (Bullet points for constraints or anti-patterns)
    
    ## Pattern Diagram (Mermaid)
    ```mermaid
    (Generate a valid Mermaid.js flowchart or sequence diagram illustrating this pattern)
    """

# Generate content
response = model.generate_content(prompt)
content = response.text

# Save file to 'patterns' folder
os.makedirs("patterns", exist_ok=True)
filename = f"patterns/{pattern_name.lower().replace(' ', '_')}.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Gemini Agent successfully created: {filename}")
if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "API Gateway"
    generate_integration_doc(name)
