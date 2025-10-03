import requests
import base64
import zlib

def generate_plantuml_url(puml_content):
    # Remove @startuml and @enduml
    content = puml_content.replace('@startuml', '').replace('@enduml', '')
    
    # Compress the PlantUML content
    zlibbed = zlib.compress(content.encode('utf-8'))
    compressed = base64.b64encode(zlibbed)
    
    # Create URL for the PlantUML server
    url = f"http://www.plantuml.com/plantuml/png/{compressed.decode('utf-8')}"
    return url

def download_diagram(puml_file, output_file):
    # Read the PlantUML content
    with open(puml_file, 'r') as f:
        content = f.read()
    
    # Generate URL
    url = generate_plantuml_url(content)
    
    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print(f"Successfully generated diagram: {output_file}")
    else:
        print(f"Error generating diagram: {response.status_code}")

if __name__ == "__main__":
    puml_file = "class_diagram.puml"
    output_file = "class_diagram.png"
    download_diagram(puml_file, output_file)